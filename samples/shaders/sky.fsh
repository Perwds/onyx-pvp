#version 330

// Custom skies: every pixel the world didn't draw on (depth = far) gets the chosen sky, looked up by the direction
// it looks in, so the sky turns with the camera like a real one. Far-away terrain is faded into the same sky so
// the horizon has no fog seam. Camera data comes from Onyx in a tiny 8 x 1 picture (two 16-bit values per pixel).
// (26.3 needs explicit locations: the build adds them for that version.)

uniform sampler2D InSampler;
uniform sampler2D MainDepthSampler;
uniform sampler2D SkySampler;
uniform sampler2D CamSampler;

in vec2 texCoord;

out vec4 fragColor;

float cam(int i) {
    vec4 p = texelFetch(CamSampler, ivec2(i / 2, 0), 0);
    vec2 v = (i % 2 == 0) ? p.rg : p.ba;
    return (v.x * 255.0 * 256.0 + v.y * 255.0) / 65535.0;
}

float camRange(int i, float lo, float hi) {
    return lo + cam(i) * (hi - lo);
}

float hash13(vec3 p) {
    p = fract(p * 0.1031);
    p += dot(p, p.zyx + 31.32);
    return fract((p.x + p.y) * p.z);
}

float hash11(float n) {
    return fract(sin(n * 127.1) * 43758.5453);
}

vec3 hash33(vec3 p) {
    return vec3(hash13(p), hash13(p + 17.7), hash13(p + 41.3));
}

// the sky picture, wrapping around sideways, smoothly filtered by hand
vec3 skyTex(vec2 uv) {
    vec2 size = vec2(1024.0, 512.0);
    vec2 p = vec2(fract(uv.x), clamp(uv.y, 0.0, 1.0)) * size - 0.5;
    vec2 f = fract(p);
    ivec2 i0 = ivec2(floor(p));
    ivec2 a = ivec2((i0.x + 1024) % 1024, clamp(i0.y, 0, 511));
    ivec2 b = ivec2((i0.x + 1025) % 1024, clamp(i0.y + 1, 0, 511));
    vec3 c00 = texelFetch(SkySampler, ivec2(a.x, a.y), 0).rgb;
    vec3 c10 = texelFetch(SkySampler, ivec2(b.x, a.y), 0).rgb;
    vec3 c01 = texelFetch(SkySampler, ivec2(a.x, b.y), 0).rgb;
    vec3 c11 = texelFetch(SkySampler, ivec2(b.x, b.y), 0).rgb;
    return mix(mix(c00, c10, f.x), mix(c01, c11, f.x), f.y);
}

// small twinkling stars
float stars(vec3 d, float density, float t) {
    vec3 q = d * 140.0;
    vec3 cell = floor(q);
    float s = 0.0;
    for (int z = 0; z <= 1; z++) for (int y = 0; y <= 1; y++) for (int x = 0; x <= 1; x++) {
        vec3 c = cell + vec3(x, y, z) - 0.5;
        float h = hash13(c);
        if (h > density) continue;
        vec3 pos = c + hash33(c);
        float dist = length(q - pos);
        float tw = 0.65 + 0.35 * sin(t * (1.5 + h * 30.0) + h * 400.0);
        s += smoothstep(0.22, 0.0, dist) * tw * (0.5 + h / density);
    }
    return s;
}

// long straight lines across the sky that meet at bright points, like a star web
float web(vec3 d, float t) {
    float line = 0.0, node = 0.0;
    for (int i = 0; i < 46; i++) {
        float fi = float(i);
        vec3 a = normalize(vec3(hash11(fi) - 0.5, hash11(fi + 0.3) * 0.9 + 0.05, hash11(fi + 0.7) - 0.5));
        vec3 b = normalize(vec3(hash11(fi + 1.1) - 0.5, hash11(fi + 1.5) * 0.9 - 0.15, hash11(fi + 1.9) - 0.5));
        vec3 n = normalize(cross(a, b));
        float off = abs(dot(d, n));
        if (dot(cross(a, d), n) >= 0.0 && dot(cross(d, b), n) >= 0.0) {
            float pulse = 0.55 + 0.45 * sin(t * 0.7 + fi * 1.7);
            line += smoothstep(0.0022, 0.0, off) * pulse + smoothstep(0.008, 0.0, off) * 0.18 * pulse;
        }
        node += smoothstep(0.012, 0.0, length(d - a)) + smoothstep(0.012, 0.0, length(d - b));
    }
    return min(1.5, line) + node;
}

vec3 skyColor(vec3 d, int style, float t, float flash) {
    float u = atan(d.x, d.z) / 6.2831853 + 0.5;
    float v = acos(clamp(d.y, -1.0, 1.0)) / 3.14159265;
    // cloudy skies drift slowly
    float drift = (style == 1 || style == 3) ? 0.004 : (style == 2 ? 0.006 : 0.0007);
    vec3 c = skyTex(vec2(u + t * drift, v));
    float up = clamp(d.y * 4.0 + 0.4, 0.0, 1.0);
    if (style == 4 || style == 5 || style == 6 || style == 8 || style == 10) c += vec3(stars(d, style == 6 ? 0.05 : 0.09, t)) * up;
    if (style == 8) c += vec3(0.85, 0.88, 0.95) * web(d, t) * up;
    if (style == 1 || style == 3) c += flash * (vec3(0.55, 0.5, 0.65) * (0.4 + dot(c, vec3(0.33))));
    return c;
}

void main() {
    vec3 scene = texture(InSampler, texCoord).rgb;
    float depth = texture(MainDepthSampler, texCoord).r;
    int raw = int(camRange(13, 0.0, 64.0) + 0.5);
    bool reversed = raw >= 32;
    int style = raw % 32;
    float fogBlend = cam(14);
    bool isSky = reversed ? depth <= 0.00001 : depth >= 0.99999;
    if (style <= 0 || (!isSky && fogBlend <= 0.0)) {
        fragColor = vec4(scene, 1.0);
        return;
    }
    vec3 fwd = vec3(camRange(0, -1.0, 1.0), camRange(1, -1.0, 1.0), camRange(2, -1.0, 1.0));
    vec3 up = vec3(camRange(3, -1.0, 1.0), camRange(4, -1.0, 1.0), camRange(5, -1.0, 1.0));
    vec3 left = vec3(camRange(6, -1.0, 1.0), camRange(7, -1.0, 1.0), camRange(8, -1.0, 1.0));
    float tanY = camRange(9, 0.0, 4.0), tanX = camRange(10, 0.0, 8.0);
    float far = camRange(11, 0.0, 8192.0);
    float t = camRange(12, 0.0, 1000.0);
    float flash = cam(15);
    vec2 ndc = texCoord * 2.0 - 1.0;
    vec3 dir = normalize(fwd - left * ndc.x * tanX + up * ndc.y * tanY);
    vec3 sky = skyColor(dir, style, t, flash);
    if (isSky) {
        fragColor = vec4(sky, 1.0);
        return;
    }
    // far terrain fades into the sky instead of into fog of the old sky colour
    float n = 0.05;
    float lin;
    if (reversed) {
        lin = n * far / (depth * (far - n) + n);
    } else {
        float z = depth * 2.0 - 1.0;
        lin = (2.0 * n * far) / (far + n - z * (far - n));
    }
    float k = smoothstep(far * 0.14, far * 0.24, lin) * fogBlend;
    fragColor = vec4(mix(scene, sky, k), 1.0);
}
