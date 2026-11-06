"""
Builds Onyx's 3D GUI models in Blender and exports them for the mod.

Run:  blender -b --factory-startup -P blender/gui_models.py -- <output folder>

Every model is built from scratch here (bevelled, smoothed, made of a few named materials) and written as an
".omesh" file: a tiny text format Onyx reads directly:

    omesh 1
    t <count>
    <x y z  nx ny nz  part>  x3 per triangle

"part" says how the mod colors that triangle at runtime, so the models follow the menu's theme and accent:
    0 base (dark onyx)   1 accent (theme accent)   2 glow (bright accent, unlit)
    3 light (light steel)   4 dark (near black)    5 white (unlit white)    6 gold
Models are centred and scaled to fit a box from -1 to 1.
"""
import bpy
import bmesh
import math
import os
import sys
from mathutils import Vector, Matrix

PARTS = {"base": 0, "accent": 1, "glow": 2, "light": 3, "dark": 4, "white": 5, "gold": 6, "green": 7, "brown": 8, "stone": 9, "red": 10}


# ---------------------------------------------------------------------- scene helpers

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def material(name):
    m = bpy.data.materials.get(name)
    if m is None:
        m = bpy.data.materials.new(name)
    return m


def set_part(obj, part):
    obj.data.materials.clear()
    obj.data.materials.append(material(part))
    return obj


def finish(obj, bevel=0.0, segments=2, smooth=True, angle=40):
    """Bevel the edges a little (catches the light) and smooth the shading, keeping hard edges hard."""
    if bevel > 0:
        m = obj.modifiers.new("bevel", "BEVEL")
        m.width = bevel
        m.segments = segments
        m.limit_method = "ANGLE"
        m.angle_limit = math.radians(30)
    if smooth:
        for p in obj.data.polygons:
            p.use_smooth = True
        if hasattr(obj.data, "set_sharp_from_angle"):
            obj.data.set_sharp_from_angle(angle=math.radians(angle))
    return obj


def cube(size=(1, 1, 1), loc=(0, 0, 0), part="base", bevel=0.04, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.active_object
    o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    return finish(set_part(o, part), bevel)


def cylinder(r=0.5, depth=1, loc=(0, 0, 0), part="base", verts=32, rot=(0, 0, 0), bevel=0.03):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth, vertices=verts, location=loc, rotation=rot)
    return finish(set_part(bpy.context.active_object, part), bevel)


def cone(r1=0.5, r2=0.0, depth=1, loc=(0, 0, 0), part="base", verts=32, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cone_add(radius1=r1, radius2=r2, depth=depth, vertices=verts, location=loc, rotation=rot)
    return finish(set_part(bpy.context.active_object, part))


def sphere(r=0.5, loc=(0, 0, 0), part="base", seg=24, rings=12):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, segments=seg, ring_count=rings, location=loc)
    return finish(set_part(bpy.context.active_object, part), smooth=True, angle=89)


def ico(r=0.5, loc=(0, 0, 0), part="base", sub=1):
    bpy.ops.mesh.primitive_ico_sphere_add(radius=r, subdivisions=sub, location=loc)
    return finish(set_part(bpy.context.active_object, part), smooth=False)


def torus(major=0.5, minor=0.1, loc=(0, 0, 0), part="base", rot=(0, 0, 0), seg=40, mseg=12):
    bpy.ops.mesh.primitive_torus_add(major_radius=major, minor_radius=minor, location=loc, rotation=rot,
                                     major_segments=seg, minor_segments=mseg)
    return finish(set_part(bpy.context.active_object, part), smooth=True, angle=89)


def prism(points2d, depth, loc=(0, 0, 0), part="base", rot=(0, 0, 0), bevel=0.03):
    """An extruded flat shape (points in the XZ plane, extruded along Y)."""
    mesh = bpy.data.meshes.new("prism")
    bm = bmesh.new()
    front = [bm.verts.new((x, -depth / 2, z)) for x, z in points2d]
    back = [bm.verts.new((x, depth / 2, z)) for x, z in points2d]
    bm.faces.new(front[::-1])
    bm.faces.new(back)
    n = len(points2d)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((front[i], front[j], back[j], back[i]))
    bm.normal_update()
    bm.to_mesh(mesh)
    bm.free()
    o = bpy.data.objects.new("prism", mesh)
    bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = rot
    bpy.context.view_layer.objects.active = o
    o.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")
    return finish(set_part(o, part), bevel)


def text3d(s, size=1.0, depth=0.15, loc=(0, 0, 0), part="base", bevel=0.02):
    bpy.ops.object.text_add(location=loc, rotation=(math.radians(90), 0, 0))
    o = bpy.context.active_object
    o.data.body = s
    o.data.size = size
    o.data.extrude = depth
    o.data.bevel_depth = bevel
    o.data.bevel_resolution = 2
    o.data.align_x = "CENTER"
    o.data.align_y = "CENTER"
    bpy.ops.object.convert(target="MESH")
    o = bpy.context.active_object
    return finish(set_part(o, part), smooth=True, angle=30)


# ---------------------------------------------------------------------- export

def hemisphere(n):
    """n directions spread over the +Z hemisphere (cosine weighted)."""
    out = []
    golden = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        r = math.sqrt((i + 0.5) / n)
        a = i * golden
        out.append(Vector((r * math.cos(a), r * math.sin(a), math.sqrt(max(0.0, 1 - r * r)))))
    return out


RAYS = hemisphere(24)


def bake_ao(tris, size):
    """Ambient occlusion per corner, worked out by casting rays into the finished model (Blender's own ray caster):
    how much of the sky each corner sees. Crevices and inner corners get darker, like a Blender render."""
    deps = bpy.context.evaluated_depsgraph_get()
    scene = bpy.context.scene
    reach = size * 0.45
    cache = {}
    out = []
    for tri, _ in tris:
        row = []
        for p, n in tri:
            key = (round(p.x, 3), round(p.y, 3), round(p.z, 3), round(n.x, 2), round(n.y, 2), round(n.z, 2))
            if key not in cache:
                # a frame around the normal, then the hemisphere rays in it
                t = n.orthogonal().normalized()
                b = n.cross(t)
                origin = p + n * size * 0.004
                open_ = 0
                for d in RAYS:
                    dirv = (t * d.x + b * d.y + n * d.z).normalized()
                    hit = scene.ray_cast(deps, origin, dirv, distance=reach)[0]
                    if not hit:
                        open_ += 1
                cache[key] = open_ / len(RAYS)
            row.append(cache[key])
        out.append(row)
    return out


def detail_for_ao():
    """A light subdivision (shape unchanged) so the occlusion has corners to land on across big faces."""
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and len(obj.data.polygons) < 600:
            m = obj.modifiers.new("ao_detail", "SUBSURF")
            m.subdivision_type = "SIMPLE"
            m.levels = 1
            m.render_levels = 1


def export(path, detail=True):
    """Applies modifiers, triangulates, centres + fits into -1..1, bakes occlusion and writes the .omesh file."""
    if detail:
        detail_for_ao()
    deps = bpy.context.evaluated_depsgraph_get()
    tris = []
    palette = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        ev = obj.evaluated_get(deps)
        me = ev.to_mesh()
        me.calc_loop_triangles()
        mw = obj.matrix_world
        nm = mw.to_3x3().inverted().transposed()
        mname = obj.data.materials[0].name if obj.data.materials else "base"
        if mname.startswith("#"):
            # a custom color ("#rrggbb", "!" at the end = glows): goes in the palette, part 32 + its index
            if mname not in palette:
                palette.append(mname)
            part = 32 + palette.index(mname)
        else:
            part = PARTS.get(mname, 0)
        has_corner = hasattr(me, "corner_normals")
        for lt in me.loop_triangles:
            tri = []
            for k in range(3):
                li = lt.loops[k]
                v = me.vertices[me.loops[li].vertex_index].co
                n = me.corner_normals[li].vector if has_corner else me.loops[li].normal
                if not lt.use_smooth:
                    n = lt.normal
                wp = mw @ v
                wn = (nm @ n).normalized()
                tri.append((wp, wn))
            tris.append((tri, part))
        ev.to_mesh_clear()
    # fit: centre of the bounding box to 0, the largest side to 2
    lo = Vector((1e9, 1e9, 1e9))
    hi = Vector((-1e9, -1e9, -1e9))
    for tri, _ in tris:
        for p, _ in tri:
            lo = Vector((min(lo.x, p.x), min(lo.y, p.y), min(lo.z, p.z)))
            hi = Vector((max(hi.x, p.x), max(hi.y, p.y), max(hi.z, p.z)))
    c = (lo + hi) / 2
    size = max(hi.x - lo.x, hi.y - lo.y, hi.z - lo.z)
    s = 2.0 / size
    ao = bake_ao(tris, size)
    with open(path, "w") as f:
        f.write("omesh 3\n")
        f.write("pal %d\n" % len(palette))
        for name in palette:
            f.write("%s %d\n" % (name[1:7], 1 if name.endswith("!") else 0))
        f.write("t %d\n" % len(tris))
        for (tri, part), occ in zip(tris, ao):
            for (p, n), a in zip(tri, occ):
                q = (p - c) * s
                # Blender is Z-up; Minecraft is Y-up (x stays, y = z, z = -y)
                f.write("%.4f %.4f %.4f %.3f %.3f %.3f %d %.2f\n" % (q.x, q.z, -q.y, n.x, n.z, -n.y, part, a))
    print("wrote", path, len(tris), "triangles")


# ---------------------------------------------------------------------- the models

def m_logo():
    # a tall faceted onyx crystal with accent bands and a glowing core
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.55, radius2=0.0, depth=0.9, location=(0, 0, 0.45))
    top = set_part(bpy.context.active_object, "base")
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.55, radius2=0.0, depth=1.2, location=(0, 0, -0.6),
                                    rotation=(math.radians(180), 0, 0))
    bot = set_part(bpy.context.active_object, "base")
    finish(top, smooth=False)
    finish(bot, smooth=False)
    torus(0.56, 0.035, loc=(0, 0, 0), part="accent", seg=6, mseg=6)
    ico(0.18, loc=(0, 0, 0.05), part="glow", sub=2)
    for i in range(6):
        a = i * math.pi / 3
        cube((0.03, 0.03, 0.95), loc=(0.29 * math.cos(a), 0.29 * math.sin(a), 0.45), part="accent", bevel=0.0,
             rot=(0, -math.atan2(0.55, 0.9) * math.cos(a), 0)).rotation_euler = (
            -math.atan2(0.55, 0.9) * math.sin(a) * -1, math.atan2(0.55, 0.9) * math.cos(a) * -1, 0)


def m_home():
    cube((1.2, 1.0, 0.8), loc=(0, 0, -0.3), part="base", bevel=0.05)
    prism([(-0.75, 0.1), (0.75, 0.1), (0, 0.75)], 1.15, part="accent", bevel=0.03)
    cube((0.3, 0.06, 0.45), loc=(0, -0.51, -0.47), part="glow", bevel=0.02)
    cube((0.22, 0.06, 0.2), loc=(0.35, -0.51, -0.25), part="light", bevel=0.01)
    cube((0.18, 0.18, 0.4), loc=(0.35, 0.2, 0.55), part="dark", bevel=0.02)


def m_sword():
    # blade with a raised glowing fuller, a chunky crossguard with gems, wrapped grip, gem pommel
    prism([(-0.16, -0.15), (0.16, -0.15), (0.16, 1.2), (0, 1.5), (-0.16, 1.2)], 0.13, part="light", bevel=0.03)
    prism([(-0.035, 0.0), (0.035, 0.0), (0.035, 1.1), (0, 1.22), (-0.035, 1.1)], 0.16, part="glow", bevel=0.0)
    cube((0.85, 0.24, 0.16), loc=(0, 0, -0.2), part="accent", bevel=0.05)
    for x in (-0.38, 0.38):
        ico(0.09, loc=(x, 0, -0.2), part="glow", sub=1)
    cylinder(0.085, 0.5, loc=(0, 0, -0.5), part="dark", verts=16)
    for z in (-0.38, -0.5, -0.62):
        torus(0.09, 0.02, loc=(0, 0, z), part="accent", seg=16, mseg=6)
    ico(0.14, loc=(0, 0, -0.82), part="accent", sub=1)
    for o in bpy.context.scene.objects:
        o.rotation_euler.rotate_axis("Y", math.radians(-35))
        o.location = Matrix.Rotation(math.radians(-35), 4, "Y") @ o.location


def m_hitbox():
    s = 0.7
    for a in (-s, s):
        for b in (-s, s):
            cube((0.08, 0.08, 2 * s + 0.08), loc=(a, b, 0), part="accent", bevel=0.02)
            cube((0.08, 2 * s + 0.08, 0.08), loc=(a, 0, b), part="accent", bevel=0.02)
            cube((2 * s + 0.08, 0.08, 0.08), loc=(0, a, b), part="accent", bevel=0.02)
    for x in (-s, s):
        for y in (-s, s):
            for z in (-s, s):
                ico(0.1, loc=(x, y, z), part="glow", sub=1)
    cube((0.4, 0.4, 0.4), loc=(0, 0, 0), part="base", bevel=0.06)


def m_camera():
    cube((1.3, 0.7, 0.85), part="base", bevel=0.08)
    cylinder(0.32, 0.4, loc=(0, -0.5, 0), part="dark", rot=(math.radians(90), 0, 0))
    torus(0.32, 0.05, loc=(0, -0.7, 0), part="accent", rot=(math.radians(90), 0, 0))
    cylinder(0.22, 0.05, loc=(0, -0.71, 0), part="glow", rot=(math.radians(90), 0, 0))
    cube((0.35, 0.4, 0.18), loc=(-0.35, 0, 0.5), part="accent", bevel=0.04)
    cylinder(0.08, 0.08, loc=(0.45, -0.1, 0.46), part="glow", verts=16)


def m_flame():
    # three twisted flame tongues
    for i, (s, h, ox, part) in enumerate([(0.55, 1.6, 0, "accent"), (0.35, 1.1, 0.25, "glow"), (0.3, 0.9, -0.28, "accent")]):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=s, segments=16, ring_count=10, location=(ox, 0, -0.3))
        o = bpy.context.active_object
        for v in o.data.vertices:
            if v.co.z > 0:
                t = v.co.z / s
                v.co.z *= 1 + (h / s - 1) * t
                taper = 1 - 0.85 * t
                v.co.x *= taper
                v.co.y *= taper
                ang = t * 1.2
                x, y = v.co.x, v.co.y
                v.co.x = x * math.cos(ang) - y * math.sin(ang)
                v.co.y = x * math.sin(ang) + y * math.cos(ang)
        finish(set_part(o, part), smooth=True, angle=89)
    cylinder(0.6, 0.12, loc=(0, 0, -0.75), part="dark", verts=24)


def m_gem():
    # a brilliant-cut diamond: crown + pavilion
    bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=0.75, radius2=0.45, depth=0.35, location=(0, 0, 0.18))
    finish(set_part(bpy.context.active_object, "accent"), smooth=False)
    bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=0.75, radius2=0.0, depth=0.9, location=(0, 0, -0.45),
                                    rotation=(math.radians(180), 0, 0))
    finish(set_part(bpy.context.active_object, "accent"), smooth=False)
    cylinder(0.46, 0.04, loc=(0, 0, 0.37), part="glow", verts=8, bevel=0)
    torus(0.76, 0.03, part="light", seg=8, mseg=6)


def m_cubes():
    cube((0.8, 0.8, 0.8), loc=(-0.45, 0, -0.45), part="base", bevel=0.07)
    cube((0.8, 0.8, 0.8), loc=(0.45, 0, -0.45), part="accent", bevel=0.07)
    cube((0.8, 0.8, 0.8), loc=(0, 0, 0.45), part="light", bevel=0.07)
    for p in ((-0.45, -0.41, -0.45), (0.45, -0.41, -0.45), (0, -0.41, 0.45)):
        cube((0.3, 0.02, 0.3), loc=p, part="glow", bevel=0.0)


def m_monitor():
    cube((1.6, 0.12, 1.0), loc=(0, 0, 0.25), part="dark", bevel=0.05)
    cube((1.45, 0.05, 0.85), loc=(0, -0.06, 0.25), part="glow", bevel=0.0)
    for i, w in enumerate((0.9, 0.6, 1.1)):
        cube((w * 0.6, 0.02, 0.07), loc=(-0.55 + w * 0.3, -0.09, 0.5 - i * 0.18), part="base", bevel=0.0)
    cube((0.15, 0.1, 0.45), loc=(0, 0.05, -0.45), part="base", bevel=0.03)
    cube((0.7, 0.4, 0.07), loc=(0, 0.05, -0.68), part="accent", bevel=0.03)


def m_crown():
    pts = []
    n = 5
    for i in range(n * 2 + 1):
        x = -0.8 + 1.6 * i / (n * 2)
        z = 0.55 if i % 2 == 0 else 0.15
        pts.append((x, z))
    pts = [(-0.8, -0.4)] + pts + [(0.8, -0.4)]
    # bend the flat crown into a ring
    o = prism(pts, 0.08, part="gold", bevel=0.02)
    m = o.modifiers.new("bend", "SIMPLE_DEFORM")
    m.deform_method = "BEND"
    m.deform_axis = "Z"
    m.angle = math.radians(300)
    for i in range(n + 1):
        x = -0.8 + 1.6 * i / n
        ico(0.09, loc=(x, 0, 0.6), part="glow", sub=1)
    torus(0.55, 0.07, loc=(0, 0.3, -0.38), part="accent")


def m_chest():
    cube((1.4, 0.95, 0.7), loc=(0, 0, -0.3), part="base", bevel=0.06)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.48, depth=1.4, vertices=24, location=(0, 0, 0.05), rotation=(0, math.radians(90), 0))
    lid = bpy.context.active_object
    bm = bmesh.new()
    bm.from_mesh(lid.data)
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0), plane_no=(1, 0, 0), clear_inner=True)
    bm.to_mesh(lid.data)
    bm.free()
    finish(set_part(lid, "accent"), bevel=0.02)
    cube((0.24, 0.1, 0.3), loc=(0, -0.5, -0.05), part="gold", bevel=0.03)
    cube((0.08, 0.04, 0.1), loc=(0, -0.56, -0.08), part="glow", bevel=0.0)
    for x in (-0.55, 0.55):
        cube((0.12, 1.0, 1.05), loc=(x, 0, -0.15), part="dark", bevel=0.03)


def m_wrench():
    cylinder(0.12, 1.4, part="light", verts=16, rot=(0, 0, 0))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.38, depth=0.2, vertices=6, location=(0, 0, 0.8))
    head = bpy.context.active_object
    finish(set_part(head, "light"), bevel=0.02)
    cube((0.28, 0.4, 0.45), loc=(0, 0, 0.95), part="dark", bevel=0.0)
    torus(0.28, 0.09, loc=(0, 0, -0.8), part="accent", rot=(math.radians(90), 0, 0))
    for o in bpy.context.scene.objects:
        o.location = Matrix.Rotation(math.radians(40), 4, "Y") @ o.location
        o.rotation_euler.rotate_axis("Y", math.radians(40))


def m_bolt():
    prism([(-0.1, 1.0), (0.55, 1.0), (0.15, 0.15), (0.5, 0.15), (-0.35, -1.0), (-0.05, -0.15), (-0.45, -0.15)], 0.3,
          part="accent", bevel=0.04)
    prism([(-0.02, 0.85), (0.38, 0.85), (0.07, 0.25), (0.33, 0.25), (-0.2, -0.65), (-0.03, -0.05), (-0.3, -0.05)], 0.34,
          part="glow", bevel=0.0)


def m_play():
    cube((1.6, 0.3, 1.1), part="dark", bevel=0.18, )
    prism([(-0.25, -0.35), (0.38, 0), (-0.25, 0.35)], 0.4, loc=(0.03, -0.05, 0), part="glow", bevel=0.03)
    torus(0.52, 0.04, loc=(0, -0.17, 0), part="accent", rot=(math.radians(90), 0, 0))


def m_gear():
    cylinder(0.6, 0.3, part="accent", verts=48, rot=(math.radians(90), 0, 0))
    for i in range(10):
        a = i * 2 * math.pi / 10
        cube((0.22, 0.3, 0.28), loc=(0.68 * math.cos(a), 0, 0.68 * math.sin(a)), part="accent", bevel=0.03,
             rot=(0, -a, 0))
    cylinder(0.25, 0.4, part="dark", verts=32, rot=(math.radians(90), 0, 0))
    cylinder(0.12, 0.45, part="glow", verts=24, rot=(math.radians(90), 0, 0))


def m_window():
    cube((1.7, 0.12, 1.3), part="base", bevel=0.05)
    cube((1.7, 0.16, 0.22), loc=(0, -0.02, 0.6), part="accent", bevel=0.04)
    for i, c in enumerate(("glow", "light", "light", "glow")):
        x = -0.4 + (i % 2) * 0.8
        z = 0.15 - (i // 2) * 0.55
        cube((0.65, 0.05, 0.42), loc=(x, -0.07, z), part=c, bevel=0.02)
    for k, x in enumerate((0.55, 0.68, 0.81)):
        cylinder(0.045, 0.05, loc=(x, -0.11, 0.6), part="white" if k == 2 else "dark", verts=12, rot=(math.radians(90), 0, 0))


def m_word():
    # the title-screen logo: bevelled ONYX letters with an accent plate behind
    text3d("ONYX", size=1.0, depth=0.18, part="base", bevel=0.03)
    cube((2.6, 0.12, 0.25), loc=(0, 0.25, -0.62), part="accent", bevel=0.04)
    cube((2.3, 0.12, 0.06), loc=(0, 0.2, -0.5), part="glow", bevel=0.0)


def m_world():
    # Singleplayer: a grass block with a little tree on top
    cube((1.2, 1.2, 0.9), loc=(0, 0, -0.25), part="brown", bevel=0.05)
    cube((1.24, 1.24, 0.3), loc=(0, 0, 0.32), part="green", bevel=0.05)
    for x, y in ((-0.4, -0.62), (0.15, -0.62), (0.45, -0.62), (-0.62, 0.1), (-0.62, -0.35)):
        cube((0.16, 0.06, 0.16), loc=(x, y, 0.12), part="green", bevel=0.01)
    cylinder(0.08, 0.5, loc=(0.25, 0.2, 0.7), part="brown", verts=8)
    ico(0.32, loc=(0.25, 0.2, 1.05), part="green", sub=1)
    ico(0.07, loc=(-0.3, -0.2, 0.52), part="red", sub=1)


def m_globe():
    # Multiplayer: a globe with an accent orbit and glowing nodes (players)
    sphere(0.75, part="base", seg=32, rings=16)
    for i in range(6):
        torus(0.76, 0.018, part="accent", rot=(math.radians(90), 0, i * math.pi / 6), seg=32, mseg=4)
    for z in (-0.4, 0.0, 0.4):
        r = math.sqrt(max(0.0, 0.76 ** 2 - z * z))
        torus(r, 0.018, loc=(0, 0, z), part="accent", seg=32, mseg=4)
    torus(1.0, 0.04, part="glow", rot=(math.radians(70), math.radians(20), 0), seg=64, mseg=8)
    for a in (0.3, 2.2, 4.1):
        ico(0.1, loc=(math.cos(a) * 0.98, math.sin(a) * 0.34, math.sin(a) * 0.92 * 0.36), part="white", sub=1)


def m_castle():
    # Realms: a little castle tower with battlements and a banner
    cylinder(0.55, 1.1, loc=(0, 0, -0.2), part="stone", verts=12)
    for i in range(8):
        a = i * 2 * math.pi / 8
        cube((0.18, 0.18, 0.22), loc=(0.48 * math.cos(a), 0.48 * math.sin(a), 0.45), part="stone", bevel=0.02)
    cube((0.3, 0.06, 0.45), loc=(0, -0.55, -0.55), part="dark", bevel=0.02)
    cylinder(0.025, 0.7, loc=(0, 0, 0.75), part="dark", verts=8)
    prism([(0, 0), (0.45, -0.12), (0, -0.25)], 0.03, loc=(0.02, 0, 1.05), part="accent", bevel=0.0)
    cube((0.12, 0.05, 0.18), loc=(0.25, -0.53, 0.0), part="glow", bevel=0.0)
    cube((0.12, 0.05, 0.18), loc=(-0.25, -0.53, 0.1), part="glow", bevel=0.0)


def m_clapper():
    # Replays: a film clapperboard
    cube((1.5, 0.15, 1.0), loc=(0, 0, -0.2), part="dark", bevel=0.04)
    for i in range(5):
        cube((0.18, 0.17, 0.2), loc=(-0.55 + i * 0.28, 0, 0.42), part="white" if i % 2 == 0 else "dark", bevel=0.0, rot=(0, math.radians(25), 0))
    cube((1.52, 0.16, 0.06), loc=(0, 0, 0.33), part="light", bevel=0.01)
    for k, z in enumerate((0.05, -0.2, -0.45)):
        cube((1.2 if k else 0.7, 0.02, 0.05), loc=(-0.1 if k else -0.3, -0.08, z), part="glow" if k == 0 else "base", bevel=0.0)
    ico(0.12, loc=(0.55, -0.1, -0.45), part="red", sub=1)


def m_power():
    # Quit: the power symbol
    bpy.ops.mesh.primitive_torus_add(major_radius=0.7, minor_radius=0.12, major_segments=48, minor_segments=12,
                                     rotation=(math.radians(90), 0, 0))
    ring = bpy.context.active_object
    bm = bmesh.new()
    bm.from_mesh(ring.data)
    # cut the gap at the top
    gone = [v for v in bm.verts if v.co.z > 0.45 and abs(v.co.x) < 0.3]
    bmesh.ops.delete(bm, geom=gone, context="VERTS")
    bm.to_mesh(ring.data)
    bm.free()
    finish(set_part(ring, "accent"), smooth=True, angle=89)
    cube((0.24, 0.24, 0.85), loc=(0, 0, 0.4), part="glow", bevel=0.1)


def m_onyx_settings():
    # Onyx settings: the crystal on a little gear
    m_gear()
    for o in bpy.context.scene.objects:
        o.scale = (0.7, 0.7, 0.7)
        o.location = o.location * 0.7 + Vector((0, 0, -0.35))
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.3, radius2=0.0, depth=0.5, location=(0, -0.3, 0.45))
    finish(set_part(bpy.context.active_object, "glow"), smooth=False)
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.3, radius2=0.0, depth=0.35, location=(0, -0.3, 0.03), rotation=(math.radians(180), 0, 0))
    finish(set_part(bpy.context.active_object, "accent"), smooth=False)


# ---------------------------------------------------------------------- PvP items (HUD), in their own colors

def m_totem():
    gold, dark_gold, eye = "#f2c94c", "#b8862a", "#3ddc84!"
    cube((0.7, 0.5, 0.75), loc=(0, 0, -0.35), part=gold, bevel=0.05)             # body
    cube((0.8, 0.55, 0.6), loc=(0, 0, 0.35), part=gold, bevel=0.06)              # head
    for x in (-0.18, 0.18):
        cube((0.13, 0.06, 0.13), loc=(x, -0.29, 0.38), part=eye, bevel=0.0)      # emerald eyes
    cube((0.3, 0.06, 0.06), loc=(0, -0.29, 0.17), part=dark_gold, bevel=0.0)     # mouth
    for s in (-1, 1):
        cube((0.38, 0.12, 0.5), loc=(s * 0.6, 0, -0.2), part=dark_gold, bevel=0.03, rot=(0, s * math.radians(25), 0))  # wings/arms
    cube((0.5, 0.45, 0.12), loc=(0, 0, -0.78), part=dark_gold, bevel=0.03)       # feet
    cube((0.86, 0.6, 0.08), loc=(0, 0, 0.66), part=dark_gold, bevel=0.02)        # brow


def m_end_crystal():
    glass, core = "#d79bff", "#ff4fd8!"
    cube((0.95, 0.95, 0.95), loc=(0, 0, 0.25), part=glass, bevel=0.04, rot=(math.radians(35), math.radians(30), 0))
    cube((0.6, 0.6, 0.6), loc=(0, 0, 0.25), part="#a14ad6", bevel=0.03, rot=(math.radians(10), math.radians(-40), math.radians(20)))
    ico(0.24, loc=(0, 0, 0.25), part=core, sub=2)
    cube((0.95, 0.95, 0.22), loc=(0, 0, -0.75), part="#3a3a3f", bevel=0.03)     # bedrock base
    for x in (-0.3, 0.1, 0.32):
        cube((0.14, 0.02, 0.06), loc=(x, -0.48, -0.75), part="#55555b", bevel=0.0)


def m_obsidian():
    cube((1.2, 1.2, 1.2), part="#1d1429", bevel=0.05)
    import random
    rnd = random.Random(7)
    for _ in range(26):
        f = rnd.randrange(6)
        a, b = rnd.uniform(-0.45, 0.45), rnd.uniform(-0.45, 0.45)
        sz = rnd.uniform(0.08, 0.18)
        loc = [(0.6, a, b), (-0.6, a, b), (a, 0.6, b), (a, -0.6, b), (a, b, 0.6), (a, b, -0.6)][f]
        cube((sz, sz, sz), loc=loc, part="#5c2e91" if rnd.random() < 0.7 else "#8b55c9", bevel=0.0)


def m_anchor():
    cube((1.2, 1.2, 1.0), loc=(0, 0, -0.1), part="#231933", bevel=0.05)
    for x in (-0.5, 0.5):
        for y in (-0.5, 0.5):
            cube((0.22, 0.22, 1.05), loc=(x, y, -0.08), part="#3b2c55", bevel=0.03)
    cube((0.7, 0.7, 0.08), loc=(0, 0, 0.42), part="#ff9f2e!", bevel=0.0)
    for i in range(4):
        cube((0.16, 0.06, 0.16), loc=(-0.3 + i * 0.2, -0.61, 0.15), part="#ffcc55!", bevel=0.0)


def m_glowstone():
    cube((1.2, 1.2, 1.2), part="#c98d36", bevel=0.05)
    import random
    rnd = random.Random(3)
    for _ in range(30):
        f = rnd.randrange(6)
        a, b = rnd.uniform(-0.42, 0.42), rnd.uniform(-0.42, 0.42)
        sz = rnd.uniform(0.12, 0.26)
        loc = [(0.6, a, b), (-0.6, a, b), (a, 0.6, b), (a, -0.6, b), (a, b, 0.6), (a, b, -0.6)][f]
        cube((sz, sz, sz), loc=loc, part="#fff0a8!" if rnd.random() < 0.5 else "#ffd36b!", bevel=0.0)


def apple(gold, aura):
    sphere(0.62, loc=(0, 0, -0.1), part=gold, seg=28, rings=16)
    cylinder(0.05, 0.3, loc=(0.02, 0, 0.6), part="#6b4423", verts=10, rot=(0, math.radians(12), 0))
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.22, segments=12, ring_count=8, location=(0.22, 0, 0.62))
    leaf = bpy.context.active_object
    leaf.scale = (1.0, 0.25, 0.5)
    leaf.rotation_euler = (0, math.radians(-30), 0)
    finish(set_part(leaf, "#4fb043"), smooth=True, angle=89)
    if aura:
        for i in range(8):
            a = i * math.pi / 4
            ico(0.06, loc=(0.85 * math.cos(a), 0.85 * math.sin(a), -0.1 + 0.35 * math.sin(a * 2)), part="#ff7bff!", sub=1)
        torus(0.82, 0.02, loc=(0, 0, -0.1), part="#ff9cff!", rot=(math.radians(70), 0, 0), seg=48, mseg=4)


def m_gapple():
    apple("#f7c948", False)


def m_egapple():
    apple("#ffd447", True)


def m_pearl():
    sphere(0.7, part="#1b5c4f", seg=28, rings=16)
    torus(0.71, 0.05, part="#2fbf9f", rot=(math.radians(60), 0, math.radians(30)), seg=48, mseg=6)
    torus(0.71, 0.04, part="#2fbf9f", rot=(math.radians(-50), math.radians(20), 0), seg=48, mseg=6)
    ico(0.28, loc=(0, -0.48, 0), part="#79ffe2!", sub=2)


def m_xp_bottle():
    cylinder(0.5, 1.0, loc=(0, 0, -0.25), part="#7cc95a", verts=24)
    cylinder(0.22, 0.35, loc=(0, 0, 0.42), part="#7cc95a", verts=16)
    cylinder(0.25, 0.15, loc=(0, 0, 0.66), part="#8a5a32", verts=16)
    ico(0.3, loc=(0, 0, -0.28), part="#c6ff5e!", sub=2)
    for i in range(5):
        a = i * 1.3
        ico(0.06, loc=(0.25 * math.cos(a), 0.25 * math.sin(a) - 0.2, -0.1 + 0.08 * i - 0.3), part="#eaff9c!", sub=1)


MODELS = {
    "totem": m_totem, "end_crystal": m_end_crystal, "obsidian": m_obsidian, "anchor": m_anchor, "glowstone": m_glowstone,
    "gapple": m_gapple, "egapple": m_egapple, "pearl": m_pearl, "xp_bottle": m_xp_bottle,
    "world": m_world, "globe": m_globe, "castle": m_castle, "clapper": m_clapper, "power": m_power,
    "onyx_settings": m_onyx_settings,
    "logo": m_logo, "home": m_home, "pvp": m_sword, "hitboxes": m_hitbox, "camera": m_camera, "fire": m_flame,
    "items": m_gem, "models": m_cubes, "hud": m_monitor, "cosmetics": m_crown, "kits": m_chest,
    "tools": m_wrench, "performance": m_bolt, "video": m_play, "settings": m_gear, "desktop": m_window,
    "word": m_word,
}

if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = argv[0] if argv else os.path.join(os.path.dirname(__file__), "out")
    only = argv[1:] if len(argv) > 1 else list(MODELS)
    os.makedirs(out, exist_ok=True)
    for name in only:
        reset()
        MODELS[name]()
        # a light version for small icons (no extra detail), then the detailed one
        export(os.path.join(out, name + "_lo.omesh"), detail=False)
        export(os.path.join(out, name + ".omesh"))
