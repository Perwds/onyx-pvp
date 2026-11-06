package com.onyx.pvp.gui.three;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

/**
 * A 3D model for the menus, made in Blender (see blender/gui_models.py) and shipped in the mod as
 * assets/onyx/gui_models/NAME.omesh: triangles with normals and a "part" per triangle that says how it is
 * colored (base / accent / glow ...), so models follow the menu's theme.
 */
public final class GuiMesh {
    public static final int BASE = 0, ACCENT = 1, GLOW = 2, LIGHT = 3, DARK = 4, WHITE = 5, GOLD = 6, GREEN = 7, BROWN = 8, STONE = 9, RED = 10;

    /** Per vertex: x y z nx ny nz ao (ao = how much light reaches that corner, baked in Blender); parts per triangle. */
    public static final int STRIDE = 7;
    public final float[] verts;
    public final byte[] parts;
    public final int triangles;

    private static final Map<String, GuiMesh> CACHE = new HashMap<>();

    /** Custom colors of this model (parts 32 and up). */
    public final int[] palette;
    public final boolean[] paletteGlow;

    private GuiMesh(float[] verts, byte[] parts, int[] palette, boolean[] paletteGlow) {
        this.verts = verts;
        this.parts = parts;
        this.palette = palette;
        this.paletteGlow = paletteGlow;
        this.triangles = parts.length;
    }

    /** The named model, or null when it isn't in the mod. */
    public static synchronized GuiMesh get(String name) {
        if (CACHE.containsKey(name)) return CACHE.get(name);
        GuiMesh m = null;
        try (InputStream in = GuiMesh.class.getResourceAsStream("/assets/onyx/gui_models/" + name + ".omesh")) {
            if (in != null) m = read(in);
        } catch (Exception e) {
            System.err.println("[Onyx] couldn't load 3D model " + name + ": " + e);
        }
        CACHE.put(name, m);
        return m;
    }

    private static GuiMesh read(InputStream in) throws Exception {
        BufferedReader r = new BufferedReader(new InputStreamReader(in, StandardCharsets.US_ASCII));
        if (!r.readLine().startsWith("omesh")) throw new IllegalStateException("not an omesh file");
        String line = r.readLine().trim();
        int[] pal = new int[0];
        boolean[] palGlow = new boolean[0];
        if (line.startsWith("pal")) {
            // custom colors (part 32 + index), "1" = glows
            int k = Integer.parseInt(line.split(" ")[1]);
            pal = new int[k];
            palGlow = new boolean[k];
            for (int i = 0; i < k; i++) {
                String[] s = r.readLine().trim().split(" ");
                pal[i] = 0xFF000000 | Integer.parseInt(s[0], 16);
                palGlow[i] = s.length > 1 && s[1].equals("1");
            }
            line = r.readLine().trim();
        }
        int n = Integer.parseInt(line.split(" ")[1]);
        float[] v = new float[n * 3 * STRIDE];
        byte[] parts = new byte[n];
        for (int t = 0; t < n; t++) {
            for (int k = 0; k < 3; k++) {
                String[] s = r.readLine().trim().split(" ");
                int o = (t * 3 + k) * STRIDE;
                for (int i = 0; i < 6; i++) v[o + i] = Float.parseFloat(s[i]);
                v[o + 6] = s.length > 7 ? Float.parseFloat(s[7]) : 1f;
                if (k == 0) parts[t] = (byte) Integer.parseInt(s[6]);
            }
        }
        return new GuiMesh(v, parts, pal, palGlow);
    }
}
