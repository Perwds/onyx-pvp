package com.onyx.pvp.replay;

import net.minecraft.core.RegistryAccess;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * Reads a whole clip once (in the background) and lists what every player did: item switches (what, where it
 * went, how long it took), totem pops and how fast the totem came back, hits with the estimated reach, clicks
 * per second, aim snaps before hits and how fast crystals got broken. Things that look inhumanly fast are
 * flagged. Everything is worked out from what the server sent your client, so reach and timings are estimates
 * (lag shifts them a little): a flag is something to look at, not proof.
 */
public final class ReplayAnalysis {
    public enum Kind {
        SWITCH, POP, RETOTEM, HIT, CPS, SNAP, CRYSTAL
    }

    /** 0 info, 1 suspicious, 2 very suspicious. */
    public record Event(int tick, Kind kind, String player, String text, int level) {
    }

    /** Per-player summary for the inspector header. */
    public static final class Stats {
        public final String name;
        public int hits, pops, switches, flags, maxCps, fastestRetotem = -1, fastestCrystal = -1;
        public double maxReach, reachSum;

        Stats(String name) {
            this.name = name;
        }

        public double avgReach() {
            return hits == 0 ? 0 : reachSum / hits;
        }
    }

    public final List<Event> events = new ArrayList<>();
    public final Map<String, Stats> players = new LinkedHashMap<>();
    public volatile boolean done;
    public volatile float progress;

    private ReplayAnalysis() {
    }

    public Stats stats(String player) {
        return players.computeIfAbsent(player, Stats::new);
    }

    /** Starts reading the clip in the background; check {@link #done}. */
    public static ReplayAnalysis start(ReplayFile.Loaded replay, RegistryAccess regs) {
        ReplayAnalysis a = new ReplayAnalysis();
        Thread t = new Thread(() -> {
            try {
                a.run(replay, regs);
            } catch (Throwable e) {
                System.err.println("[Onyx Replay] analysis stopped: " + e);
            }
            a.done = true;
        }, "Onyx Replay Analysis");
        t.setDaemon(true);
        t.setPriority(Thread.MIN_PRIORITY);
        t.start();
        return a;
    }

    // ------------------------------------------------------------------ tracking

    private static final class Ent {
        final int id;
        final boolean player, crystal;
        String typeName = "Entity";
        int popCheck = -1;
        UUID uuid;
        double x, y, z, bx, by, bz;
        float headYaw, lastYawDelta;
        int lastYawTick;
        final Map<String, String> gear = new HashMap<>();
        final Map<String, Integer> gearChanged = new HashMap<>();
        int popTick = -1, born;
        final java.util.ArrayDeque<Integer> swings = new java.util.ArrayDeque<>();
        int lastCpsFlag = -100;

        Ent(int id, boolean player, boolean crystal) {
            this.id = id;
            this.player = player;
            this.crystal = crystal;
        }

        void moveTo(double nx, double ny, double nz) {
            x = bx = nx;
            y = by = ny;
            z = bz = nz;
        }
    }

    private final Map<Integer, Ent> ents = new HashMap<>();
    private final Map<UUID, String> names = new HashMap<>();

    private String name(Ent e) {
        if (e == null) return "?";
        String n = e.uuid == null ? null : names.get(e.uuid);
        return n != null ? n : e.player ? "Player " + e.id : e.typeName;
    }

    private void add(int tick, Kind kind, Ent who, String text, int level) {
        String n = name(who);
        events.add(new Event(tick, kind, n, text, level));
        if (level > 0) stats(n).flags++;
    }

    private void run(ReplayFile.Loaded replay, RegistryAccess regs) {
        //? if <26.1 {
        int start = replay.start();
        int total = replay.stream().size();
        for (int i = 0; i < total; i++) {
            ReplayFile.Rec rec = replay.stream().get(i);
            // chunks, maps and the like say nothing about what players did: skip them without unpacking
            if (rec.size() > 6000) continue;
            if ((i & 1023) == 0) progress = (float) i / total;
            net.minecraft.network.protocol.Packet<?> p;
            try {
                p = ReplayCodec.decodeGame(rec.data(), regs);
            } catch (Throwable e) {
                continue;
            }
            int t = rec.tick();
            // things before the clip's start (the part skipped when opening) only set up who is where
            boolean show = t >= start;
            handle(p, t, show);
            if (show) instantRetotems(t);
        }
        events.sort(java.util.Comparator.comparingInt(Event::tick));
        //?}
        progress = 1;
    }

    //? if <26.1 {
    private void handle(net.minecraft.network.protocol.Packet<?> p, int t, boolean show) {
        if (p instanceof net.minecraft.network.protocol.game.ClientboundPlayerInfoUpdatePacket u) {
            for (var e : u.entries()) if (e.profile() != null) names.put(e.profileId(), e.profile().name());
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundAddEntityPacket a) {
            var type = a.getType();
            Ent e = new Ent(a.getId(), type == net.minecraft.world.entity.EntityType.PLAYER, type == net.minecraft.world.entity.EntityType.END_CRYSTAL);
            e.typeName = type.getDescription().getString();
            e.uuid = a.getUUID();
            e.moveTo(a.getX(), a.getY(), a.getZ());
            e.headYaw = a.getYHeadRot();
            e.born = t;
            ents.put(e.id, e);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundRemoveEntitiesPacket r) {
            for (int id : r.getEntityIds()) {
                Ent e = ents.remove(id);
                if (e != null && e.crystal && show) crystalGone(e, t);
            }
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundMoveEntityPacket m) {
            Ent e = ents.get(((com.onyx.pvp.mixin.ReplayMoveEntityAccessor) m).onyx$entityId());
            if (e == null) return;
            if (m.hasPosition()) {
                e.bx += m.getXa() / 4096.0;
                e.by += m.getYa() / 4096.0;
                e.bz += m.getZa() / 4096.0;
                e.x = e.bx;
                e.y = e.by;
                e.z = e.bz;
            }
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundTeleportEntityPacket tp) {
            Ent e = ents.get(tp.id());
            if (e == null) return;
            var v = tp.change().position();
            var rel = tp.relatives();
            e.moveTo(rel.contains(net.minecraft.world.entity.Relative.X) ? e.x + v.x : v.x,
                    rel.contains(net.minecraft.world.entity.Relative.Y) ? e.y + v.y : v.y,
                    rel.contains(net.minecraft.world.entity.Relative.Z) ? e.z + v.z : v.z);
            yaw(e, tp.change().yRot(), t);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundEntityPositionSyncPacket s) {
            Ent e = ents.get(s.id());
            if (e == null) return;
            var v = s.values().position();
            e.moveTo(v.x, v.y, v.z);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundRotateHeadPacket h) {
            Ent e = ents.get(((com.onyx.pvp.mixin.ReplayRotateHeadAccessor) h).onyx$entityId());
            if (e != null) yaw(e, h.getYHeadRot(), t);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundAnimatePacket a) {
            Ent e = ents.get(a.getId());
            if (e == null || !e.player || (a.getAction() != 0 && a.getAction() != 3)) return;
            e.swings.addLast(t);
            while (!e.swings.isEmpty() && e.swings.peekFirst() <= t - 20) e.swings.pollFirst();
            int cps = e.swings.size();
            Stats st = stats(name(e));
            st.maxCps = Math.max(st.maxCps, cps);
            if (show && cps >= 17 && t - e.lastCpsFlag > 40) {
                e.lastCpsFlag = t;
                add(t, Kind.CPS, e, cps + " clicks in one second", cps >= 21 ? 2 : 1);
            }
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundSetEquipmentPacket q) {
            Ent e = ents.get(q.getEntity());
            if (e == null || !e.player) return;
            equipment(e, q.getSlots(), t, show);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundEntityEventPacket ev) {
            Ent e = ents.get(((com.onyx.pvp.mixin.ReplayEntityEventAccessor) ev).onyx$entityId());
            if (e == null || !e.player || ev.getEventId() != 35) return;
            e.popTick = t;
            e.popCheck = t;
            stats(name(e)).pops++;
            if (show) add(t, Kind.POP, e, "popped a totem", 0);
            return;
        }
        if (p instanceof net.minecraft.network.protocol.game.ClientboundDamageEventPacket d) {
            Ent victim = ents.get(d.entityId()), attacker = ents.get(d.sourceCauseId());
            if (victim == null || attacker == null || !attacker.player || attacker == victim) return;
            // only melee: the direct source is the attacker itself (not an arrow, crystal or explosion)
            if (d.sourceDirectId() != d.sourceCauseId()) return;
            double reach = reach(attacker, victim);
            Stats st = stats(name(attacker));
            st.hits++;
            st.reachSum += reach;
            st.maxReach = Math.max(st.maxReach, reach);
            if (!show) return;
            int level = reach > 3.8 ? 2 : reach > 3.35 ? 1 : 0;
            add(t, Kind.HIT, attacker, "hit " + name(victim) + String.format(" from %.2f blocks", reach), level);
            // aim snap: a big turn right before the hit
            if (t - attacker.lastYawTick <= 2 && attacker.lastYawDelta >= 100) {
                add(t, Kind.SNAP, attacker, String.format("turned %.0f° in one tick right before hitting", attacker.lastYawDelta),
                        attacker.lastYawDelta >= 150 ? 2 : 1);
            }
        }
    }

    private void yaw(Ent e, float yaw, int t) {
        float d = Math.abs(net.minecraft.util.Mth.wrapDegrees(yaw - e.headYaw));
        e.headYaw = yaw;
        if (d > 0.5f) {
            e.lastYawDelta = t == e.lastYawTick ? Math.max(e.lastYawDelta, d) : d;
            e.lastYawTick = t;
        }
    }

    private void equipment(Ent e, List<com.mojang.datafixers.util.Pair<net.minecraft.world.entity.EquipmentSlot, net.minecraft.world.item.ItemStack>> slots, int t,
                           boolean show) {
        Map<String, String[]> changes = new LinkedHashMap<>(); // slot -> {from, to}
        for (var pr : slots) {
            String slot = slotName(pr.getFirst());
            if (slot == null) continue;
            var stack = pr.getSecond();
            String now = stack.isEmpty() ? "nothing" : stack.getHoverName().getString();
            String before = e.gear.get(slot);
            if (before == null && t - e.born <= 2) {
                // first time this slot is seen (joining, or the start of the clip): not a switch
                e.gear.put(slot, now);
                continue;
            }
            if (before == null) before = "nothing";
            if (now.equals(before)) continue;
            e.gear.put(slot, now);
            changes.put(slot, new String[]{before, now});
        }
        if (changes.isEmpty()) return;
        Stats st = stats(name(e));
        String[] main = changes.get("main hand"), off = changes.get("off hand");
        if (main != null && off != null && main[0].equals(off[1]) && off[0].equals(main[1])) {
            // the two hands traded items: a swap-hands key press
            if (show) {
                st.switches++;
                add(t, Kind.SWITCH, e, main[0] + " → off hand, " + off[0] + " → main hand (swap)", 0);
            }
            changes.remove("main hand");
            changes.remove("off hand");
            e.gearChanged.put("main hand", t);
            e.gearChanged.put("off hand", t);
            retotem(e, off[1], t, show);
        }
        for (var c : changes.entrySet()) {
            String slot = c.getKey();
            Integer last = e.gearChanged.put(slot, t);
            if (!show) continue;
            st.switches++;
            String took = last == null ? "" : ", " + ticks(t - last) + " after the last change";
            add(t, Kind.SWITCH, e, c.getValue()[1] + " → " + slot + " (was " + c.getValue()[0] + ")" + took, 0);
            if (slot.equals("off hand")) retotem(e, c.getValue()[1], t, show);
        }
    }

    /** A totem back in the off hand after a pop: how long did it take? */
    private void retotem(Ent e, String offNow, int t, boolean show) {
        if (e.popTick < 0 || !offNow.toLowerCase(java.util.Locale.ROOT).contains("totem")) return;
        int took = t - e.popTick;
        e.popTick = -1;
        e.popCheck = -1;
        if (took > 60) return;
        Stats st = stats(name(e));
        st.fastestRetotem = st.fastestRetotem < 0 ? took : Math.min(st.fastestRetotem, took);
        if (show) add(t, Kind.RETOTEM, e, "totem back in off hand " + ticks(took) + " after popping", took <= 1 ? 2 : took <= 2 ? 1 : 0);
    }

    /**
     * A pop where the off hand never showed empty: the totem was put back before the server even sent the empty
     * hand (the same tick). Checked a few ticks after the pop.
     */
    private void instantRetotems(int t) {
        for (Ent e : ents.values()) {
            if (e.popCheck < 0 || t - e.popCheck < 3) continue;
            int pop = e.popCheck;
            e.popCheck = -1;
            Integer changed = e.gearChanged.get("off hand");
            String off = e.gear.getOrDefault("off hand", "");
            if ((changed == null || changed < pop) && off.toLowerCase(java.util.Locale.ROOT).contains("totem")) {
                e.popTick = -1;
                Stats st = stats(name(e));
                st.fastestRetotem = 0;
                add(pop, Kind.RETOTEM, e, "totem was back in the off hand instantly (it never showed empty after the pop)", 1);
            }
        }
    }

    private void crystalGone(Ent c, int t) {
        int lived = t - c.born;
        // whoever swung this tick or the one before and is closest
        Ent best = null;
        double bestD = 7 * 7;
        for (Ent e : ents.values()) {
            if (!e.player || e.swings.isEmpty() || e.swings.peekLast() < t - 1) continue;
            double d = (e.x - c.x) * (e.x - c.x) + (e.y - c.y) * (e.y - c.y) + (e.z - c.z) * (e.z - c.z);
            if (d < bestD) {
                bestD = d;
                best = e;
            }
        }
        if (best == null) return;
        Stats st = stats(name(best));
        st.fastestCrystal = st.fastestCrystal < 0 ? lived : Math.min(st.fastestCrystal, lived);
        add(t, Kind.CRYSTAL, best, "broke a crystal " + ticks(lived) + " after it appeared", lived <= 0 ? 2 : lived <= 1 ? 1 : 0);
    }

    private static String slotName(net.minecraft.world.entity.EquipmentSlot s) {
        return switch (s) {
            case MAINHAND -> "main hand";
            case OFFHAND -> "off hand";
            case HEAD -> "helmet";
            case CHEST -> "chestplate";
            case LEGS -> "leggings";
            case FEET -> "boots";
            default -> null;
        };
    }

    /** Distance from the attacker's eyes to the nearest point of the victim's box (players: 0.6 x 1.8). */
    private static double reach(Ent a, Ent v) {
        double ex = a.x, ey = a.y + 1.62, ez = a.z;
        double hw = 0.3, h = v.player ? 1.8 : 1.95;
        double cx = Math.max(v.x - hw, Math.min(ex, v.x + hw));
        double cy = Math.max(v.y, Math.min(ey, v.y + h));
        double cz = Math.max(v.z - hw, Math.min(ez, v.z + hw));
        return Math.sqrt((ex - cx) * (ex - cx) + (ey - cy) * (ey - cy) + (ez - cz) * (ez - cz));
    }
    //?}

    public static String ticks(int t) {
        return t + (t == 1 ? " tick" : " ticks") + " (" + t * 50 + " ms)";
    }
}
