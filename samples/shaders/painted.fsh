#version 330

// Painted World: the scene repainted as an oil painting. The screen is split into cells; each cell paints one
// chunky brush dab (a slightly ragged, rotated block of one flattened colour). Dabs follow the edges in the
// picture, and in the sky they curl around a few swirls with soft rings, like Starry Night. Everything is
// seeded by position, so nothing shimmers from frame to frame.
// (26.3 needs explicit locations: the build adds them for that version.)

uniform sampler2D InSampler;

in vec2 texCoord;

layout(std140) uniform SamplerInfo {
    vec2 OutSize;
    vec2 InSize;
};

layout(std140) uniform PaintConfig {
    float BrushSize;
    float Swirl;
};

out vec4 fragColor;

float hash(vec2 p) {
    p = fract(p * vec2(123.34, 456.21));
    p += dot(p, p + 45.32);
    return fract(p.x * p.y);
}

float luma(vec3 c) {
    return dot(c, vec3(0.299, 0.587, 0.114));
}

// three fixed swirls in the upper half of the screen (x is scaled by the aspect ratio)
const vec3 VORTEX[3] = vec3[3](vec3(0.22, 0.80, 0.16), vec3(0.58, 0.90, 0.12), vec3(0.88, 0.72, 0.14));

// direction of the swirl flow at uv, and how close it is to a swirl's ring
vec2 swirlFlow(vec2 uv, float aspect, out float ring) {
    vec2 flow = vec2(1.0, 0.15); // a gentle sideways wind between the swirls
    ring = 0.0;
    for (int i = 0; i < 3; i++) {
        vec2 d = (uv - VORTEX[i].xy) * vec2(aspect, 1.0);
        float r = length(d);
        float k = VORTEX[i].z / max(r, 0.02);
        flow += vec2(-d.y, d.x) / max(r, 0.001) * k * k * 3.0;
        ring = max(ring, (0.5 + 0.5 * sin(r * 60.0)) * smoothstep(VORTEX[i].z * 2.2, 0.0, r));
    }
    return normalize(flow);
}

// how much this colour at this height looks like sky
float skyness(vec3 c, float y) {
    float blue = smoothstep(0.02, 0.18, c.b - max(c.r, c.g * 0.85));
    return blue * smoothstep(0.35, 0.75, y);
}

void main() {
    float aspect = OutSize.x / OutSize.y;
    float cell = max(3.0, BrushSize * OutSize.y / 1080.0); // brush size in pixels, same look at any resolution
    vec2 px = texCoord * OutSize;
    vec2 inv = 1.0 / OutSize;
    vec2 base = floor(px / cell);

    float bestPri = -1.0;
    vec3 bestCol = vec3(0.0);
    float bestShade = 0.0;
    float nearest = 1e9;
    vec3 nearestCol = vec3(0.0);

    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 id = base + vec2(i, j);
            vec2 centre = (id + 0.5 + (vec2(hash(id), hash(id + 7.13)) - 0.5) * 0.8) * cell;
            vec2 cuv = centre * inv;

            // the dab's colour: a small cross of samples (flattens detail) - also gives the edge direction
            float o = cell * 0.45;
            vec3 c0 = texture(InSampler, cuv).rgb;
            float sky = skyness(c0, cuv.y) * Swirl;
            float ring = 0.0;
            vec2 flow = swirlFlow(cuv, aspect, ring);
            vec2 cuvs = cuv + flow * inv * cell * 1.2 * sky; // in the sky, paint pulls colour along the swirl
            vec3 l = texture(InSampler, cuvs - vec2(o, 0.0) * inv).rgb;
            vec3 r = texture(InSampler, cuvs + vec2(o, 0.0) * inv).rgb;
            vec3 d = texture(InSampler, cuvs - vec2(0.0, o) * inv).rgb;
            vec3 u = texture(InSampler, cuvs + vec2(0.0, o) * inv).rgb;
            vec3 col = (texture(InSampler, cuvs).rgb * 2.0 + l + r + d + u) / 6.0;
            col *= 1.0 + sky * 0.09 * (ring - 0.4); // soft light rings around each swirl

            // stroke direction: along edges (across the colour gradient); in the sky, along the swirl
            vec2 grad = vec2(luma(r) - luma(l), luma(u) - luma(d));
            vec2 dir = length(grad) > 0.04 ? normalize(vec2(-grad.y, grad.x)) : normalize(vec2(cos(hash(id + 3.1) * 6.283), sin(hash(id + 3.1) * 6.283)));
            dir = normalize(mix(dir, flow, clamp(sky * 1.5, 0.0, 1.0)));

            vec2 q = px - centre;
            vec2 along = vec2(dot(q, dir), dot(q, vec2(-dir.y, dir.x)));
            float len = cell * (0.85 + 0.6 * hash(id + 1.7)) * (1.0 + sky * 0.6);
            float wid = cell * (0.48 + 0.22 * hash(id + 2.9));
            // ragged ends and sides, in 2px steps so the dabs look blocky like the reference
            float rag = hash(floor(along.yx / 2.0) + id) - 0.5;
            bool inside = abs(along.x) < len * (1.0 + 0.12 * rag) && abs(along.y) < wid * (1.0 + 0.18 * rag);

            float dist = length(q);
            if (dist < nearest) {
                nearest = dist;
                nearestCol = col;
            }
            float pri = hash(id + 9.4);
            if (inside && pri > bestPri) {
                bestPri = pri;
                bestCol = col;
                // bristle streaks run along the stroke, a lit ridge on one side and a shadow on the other
                float bristle = hash(vec2(floor(along.y * 0.9), id.x * 13.0 + id.y)) - 0.5;
                float ridge = along.y / wid;
                bestShade = bristle * 0.10 + smoothstep(0.55, 0.95, ridge) * 0.07 - smoothstep(-0.55, -0.95, ridge) * 0.07;
            }
        }
    }

    vec3 c = bestPri >= 0.0 ? bestCol * (1.0 + bestShade) : nearestCol;

    // flatten and brighten like paint: fewer tones, a touch more colour, lifted shadows
    c = floor(c * 12.0 + 0.5) / 12.0;
    float lum = luma(c);
    c = mix(vec3(lum), c, 1.18);
    c = c * 0.92 + 0.05;

    // canvas weave and grain
    float weave = sin(px.x * 1.57) * sin(px.y * 1.57);
    float grain = hash(floor(px)) - 0.5;
    c *= 1.0 + weave * 0.02 + grain * 0.018;

    fragColor = vec4(clamp(c, 0.0, 1.0), 1.0);
}
