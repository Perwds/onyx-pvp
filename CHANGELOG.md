# Changelog

Every Onyx PvP version, newest first.

## 1.6.37

### NEW
- Friends watching your app can click in it, if you let them. In Apps, turn on Friends Can Click for that one app (it asks you twice, and it's off again every time you pin an app). It's mouse only, never the keyboard, and you get told when someone's clicking.

### FIXED / CHANGED
- Watching a friend's app is much smoother. While lots is changing you get a small live picture several times a second, and it goes sharp again once it settles. Small changes like a click stay sharp.
- Watching no longer stutters your game, and sharing your app is much lighter on your PC.
- Clicking your own pinned app lands in the right place when it's showing at a lower quality than its window.
- Everyone needs this version: 1.6.36 and older can't see apps shared from it.

## 1.6.36

### FIXED / CHANGED
- Deep Snow no longer tears into folded sheets and spikes on uneven ground. It's one smooth surface now, across steps, pits and the far edge of its range.
- Snow carries on round lanterns, fences and other small things standing on it, instead of leaving a hole with the snow hanging in the air beside it.

## 1.6.35

### NEW
- Apps are all on one screen now. Click any app, open or not, and it's pinned in front of you. Your pinned apps have a Friends Can See switch, and your friends' apps are listed with a Watch button that works from anywhere. If nothing's coming from a friend, it says why.
- Friends are rebuilt. One Friends screen (Home tab, the title screen, or a key you pick), and one friend list for everything: models no longer have their own list.
- Add someone by name, even if they're offline. They get a request to accept, and once you've both added each other you're connected. Friends already on your list connect by themselves once you've both updated.
- Every friend has a checklist saying what's working and what isn't (online, added you back, status, cosmetics, out of date), with a button to fix what can be fixed. My Setup does the same for your side, like a cape that's too big to share.
- My Configs (Menu Settings): save your whole setup under a name and load it back. Friends, waypoints and keys are kept out of them, so loading one leaves those alone, and a file is safe to give someone. What you had is kept as Before Last Load, so a load can be undone.

### FIXED / CHANGED
- Seeing a friend's app only needs you to have added each other. It used to need status sharing on both sides too.
- A shared app keeps working after either of you restarts the game.
- When you add your first friend, status sharing turns on: it only ever goes to friends who added you back, sealed so only they can read it. Turn it off in Friends any time.

## 1.6.34

### NEW
- Waypoints are rebuilt. Folders on the left, a full editor on the right, a floating item icon with the name and [distance] under it, and presets. Markers stay visible through walls.
- Block Overlay for waypoints: tint the real surfaces of an area with its own outline. Mark it by right-clicking two corners in the world, or tint just one block type. Through Walls is singleplayer only, so it can't show caves or ores on a server.
- Friends' apps now come through at up to 4K instead of a tiny blurry picture. Only the parts that change are sent, so a still page stays sharp. Both of you need this version.
- Watch a friend's app full screen, with zoom, next to the new Friends See It At setting.

### FIXED / CHANGED
- Long text no longer loses letters on curved floating menus, and tab names aren't cut off on friends' menus.
- Friends' menus now say their settings are hidden.

## 1.6.33

### FIXED / CHANGED
- Crash at startup on 26.3 from the new home screen (Components not bound yet).
- Home screen: your skin looks at the mouse, not away from it.
- Realistic boats rock on 26.3 too.

### NEW
- Open To Friends: Use A Relay (on by default). Friends join through bore.pub, a free public relay, so nothing has to reach
  your PC and there's nothing to set up on your router. It's run by someone else and your game passes through it.
  Turn it off to go direct instead.
- Frog theme: a soft watercolour frog sits in the corner of the menu and the home screen, and blinks. The little frogs in the
  Frog Pond background are the same frog now.

## 1.6.32

### NEW
- Fabric API is inside Onyx now: you don't need to install it.
- New home screen: "Hello, your name" with Play, Settings, Skins, Achievements and Marketplace, your skin beside it and a big
  picture when you hover. The older Onyx one is still in Menu Settings (Hello Home Screen).
- Desktop Apps: pin apps that are minimized, or start one that isn't open at all (Start An App That Isn't Open). The real
  window stays out of sight until you unpin it.
- Desktop Apps: Friends Can See, for one app at a time. Friends who share with you see it where you pinned it, as a small
  picture every 2 seconds, encrypted.
- Red flash round the screen when you've got no totem in your hands (Combat, Totems & Nametags). It starts once you've held one.
- World Look: Ray Traced look (mirror water, sun shadows, lit fog round lamps), on any card.
- World Look: Save / Load your own presets.
- World Look: Chromatic Aberration switch, off unless you turn it on.
- World Look: Auto Quality steps quality down when the game stays slow.
- Frog theme, Frog Pond background and Frog Pond menu preset.

### FIXED / CHANGED
- Open To Friends always gives you an address to send and copies it. If your router won't open the port, it says what's in
  the way instead of giving you nothing.
- Reflections on wet ground under a block came out as noise.
- World map: your marker no longer drifts against the map when you move it.
- World Look: fixed shader code only NVIDIA cards forgive (glitches on AMD, Intel and older cards), bad pixels can't flash
  black or white now, and lamps cost a lot less.

## 1.6.31

### NEW
- RTX Remix preset (1.21.11 only, World Look > RTX Remix): real path tracing by NVIDIA RTX Remix, ported to 1.21.11 from
  NVIDIA's 1.21.1 mod. Off unless you turn it on, and it needs a game restart either way. It needs an RTX 30 series
  card or newer, and a 1 GB download of NVIDIA's runtime the first time. It's a beta: heavy, not for PvP, and rain, snow,
  particles and stars aren't drawn yet. World Look's own shaders go off while it's on and come back after.
  NVIDIA's runtime can send session info and crash reports to NVIDIA, on by default: its Permissions tab turns that off.

## 1.6.30

### FIXED / CHANGED
- World Look: lamps no longer brighten as you walk up to them and dim as you walk off. Lamps are found up to 48
  blocks away (it was 14 to 24) and their light stays on what's round them much further out. When there are more lamps
  than fit, the furthest ones fade instead of switching off.
- World Look: puddles stay put when you move. Fixed three things: they swayed with view bobbing as you walked, their
  edges changed as you walked towards them, and they could jump a block for a frame at a block's edge.
- The wet look on the ground reaches further from you.

## 1.6.29

### FIXED / CHANGED
- Practice, Spear Mace > Attribute Swap: now about the spear. Hit with the spear and swap to the mace in the same
  tick (or mace to spear). Spear jabs count now too. No sword in this kit, and you have Saturation the whole drill.
- Download Worlds: Enter in the key box uses the key, quotes/spaces copied with it are dropped, and if CurseForge
  turns the key down you're told so plainly (back at the key box) instead of an error over the search list.

## 1.6.28

### FIXED / CHANGED
- Friends panel: a check code next to each friend you share with. Compare it with your friend (voice or chat): if
  it's the same for both of you, nobody has swapped the keys in the shared database. (Your status is sealed so
  other people reading the database can't read it, but the database itself is open, so this is how you make sure.)
- Practice: only a world just made with the Practice World button gets the practice rules (before, a different world
  opened right after a failed create could get them).
- Practice: Lunge Slam spots the spear lunge properly.

## 1.6.27

NEW IN 1.6.27: PRACTICE
- Practice World button on the create world screen: a flat world with no structures and no mobs, always noon and
  clear, you keep your things when you die and come straight back.
- In a practice world, press O for the practice menu: pick a kind of PvP, a drill and Easy / Normal / Hard / Expert.
  Each drill gives you its own kit and puts a practice bot in front of you. The score shows at the top of the screen.
  - Sword: Duel (the bot fights back: strafes, crits, combos), Spacing (only hits from 2.7+ blocks count), Timing
    (only fully charged hits count), Combos (hits in a row without getting hit).
  - Mace: Stun Slam (break its shield with the axe, then slam it with the mace before the shield is back),
    Pearl Catch (throw pearls through glowing rings in the air to be caught there; pearls that hit the ground don't
    teleport you), Wind Slam (wind charge up and come down on it: your biggest hit is kept).
  - Crystal: Crystal Speed (crystals a second on the obsidian next to it), Safe Anchor (blow anchors on it without
    hurting yourself), Totems (big hits every few seconds: how fast does your next totem go in?).
  - Spear Mace: Attribute Swap (hit and swap weapons in the same tick), Lunge Slam (lunge with the spear, then slam
    with the mace before you land).
- Harder bots move faster, reach further, hit harder and more often, turn quicker and jump for crits more.
- The practice bot and drills only work in practice worlds, never on servers.

## 1.6.26

### NEW IN 1.6.26
- Sound Studio (Utility tab > Sound Studio): make your own sounds in game.
  - Start from any of the game's sounds (search them) or your own .ogg / .wav files (put them in .minecraft/onyx/sounds).
  - See the wave and drag its two edges to cut it to the part you want.
  - Volume, pitch, fade in, fade out, echo (how much and how far apart), muffle, crunch, and play it backwards.
    You hear it as you change it.
  - Play it when you hit, crit, get a kill, pop a totem, when someone else pops one, or when you get hurt.
  - Or use it instead of the game's own sound (every time the game would play that one).

## 1.6.25

### NEW IN 1.6.25
- Ping on nametags (Combat tab > Totems & Nametags): other players' ping after their name, coloured by how high
  it is. It's what the server reports (some servers fake it).
- A star in front of friends' nametags.
- TPS readout shows about how long the server's ticks take when it's lagging (servers don't send their real tick
  time, so it's worked out from the TPS; singleplayer shows the real one).
- Replay clip inspector (1.21.11 clips): new checks (clicks too even, like an autoclicker; hitting two people at
  once in different directions, like killaura; taking no knockback at all), each player's ping during the clip,
  the server's TPS during the clip, and a verdict per player (nothing odd / worth a look / very suspicious).
  Flags are things to look at, not proof.

## 1.6.24

### NEW IN 1.6.24
- Friends panel (Home tab > Friends > Friends Panel): a panel on the side of your screen with each friend's health
  (and absorption), food, totems left, armour wear, hotbar (their held slot outlined), offhand and effects. Movable
  in the HUD editor.
  - Both of you have to agree: turn on Share My Status and tick the friend, and they do the same for you. You only
    see friends who share back.
  - It's locked so only that friend can read it: a new key every time the game starts, and your status sealed
    separately for each friend (X25519 + AES-GCM). No coordinates or server address are ever sent.
  - Your shared status is taken down when you stop sharing or leave.

## 1.6.23

### NEW IN 1.6.23
- Friends (Home tab > Friends): one friend list used everywhere (your model friends were brought over). Middle-click
  a player to add or remove them, or add players near you from the list.
- Don't hurt friends: your hits on a friend aren't sent, so you can't hit them by accident. Hold Left Alt (or your
  own key) to hit them anyway.
- Chat by who it's from (Utility > Chat By Who It's From): friends, other players, and messages no player sent (the
  server, plugins) each get their own colour and tag in front, can be hidden, and friends can ping you.
- My Chat Rules: up to 8 of your own, a word or /a pattern/, that highlight a line in a colour, ping you, or hide it.
- Friend colour for hitboxes now uses the friend list.

## 1.6.22

### NEW IN 1.6.22
- Light from what you hold (World Look settings > Light): hold a lantern, torch, glowstone, sea lantern, lava bucket
  and so on (either hand) and it lights up what's round you in its own colour (soul lights blue, redstone red...).
  Strongest at night and in caves.
- Swinging lanterns (Shaders tab > More Visuals): hanging lanterns sway from their hook, a little all the time and
  more in the wind and storms, each at its own pace. Lantern Swing slider.
- Banners flap harder in the wind and in storms, with a quicker flutter.

### FIXED
- Slanted light and dark bands across walls when the sun is low (the wall shaded itself).
- Thin lines running through shadows on grass (each grass blade cast a long line).
- Deep snow at night: it stayed dark next to lamps put down after you arrived, and the game's own snow showed
  through it in pale patches.

## 1.6.21

### NEW IN 1.6.21
- Download Worlds (a button on the world list): search CurseForge's maps and worlds and install one with a click, or
  paste a link to any world .zip from any site. The world goes into your saves as its own folder (never over an
  existing one) and shows up in the world list. CurseForge only lets apps search with an API key, which you can get
  free at console.curseforge.com: paste it in once. It's only kept until you close the game unless you tick Remember.
  Some authors only allow downloading on curseforge.com: then Page opens it there.

## 1.6.20

### NEW IN 1.6.20
- Realistic boats (Shaders tab > More Visuals): boats rock gently on the waves (more in storms), lean into their
  turns and lift their front as they speed up. Slider for how much.
- Deep snow: Snow Render Distance setting (Shaders tab > Grass & Snow), now 48 blocks by default (was 20), up to 96.

### FIXED
- With World Look, boats had water drawn inside them.
- Lit lines running through sun shadows (the shadow check stepped past block corners).
- The picture brightening and dimming over and over as you tilt the camera up towards the sun.
- Deep snow: holes round flowers and grass in snowy places, with snow heaped up into flaps round them. Flowers and
  tufts of grass are now buried in the snow (flowers poke up through).
- Butterflies showed up black (and in snowy places).

## 1.6.19

NEW IN 1.6.19 (Shaders tab > More Visuals, only you see them)
- Fireflies: soft blinking yellow-green lights drifting over grass on warm, dry nights (lots in swamps and forests).
- Butterflies: orange, white, blue, yellow, pink and green butterflies flutter round flowers by day and dart off
  when you come close.
- Falling leaves: leaves let go of trees and drift down on the wind, tumbling, then lie on the ground for a few
  seconds. The right colour for each tree (cherry pink, birch, spruce...), with an Autumn Colours option.
- Fish: little schools swim about under the water, turn back at the edges and dart away from you.
- "How Much Of Them" slider for all four.

## 1.6.18

NEW IN 1.6.18 (Shaders tab > More Visuals, only you see them)
- Birds: flocks fly about over the land by day, gulls glide over the sea and beaches, crows come out at dusk. They
  flock together, flap as they climb, keep above the ground and scatter when you come close. Fewer in the rain,
  none at night. Slider for how many.
- Boat wakes: moving boats leave a foam V spreading out behind them on the water, with churned water straight
  behind. Works for everyone's boats.
- Boat spray: water splashes off the front of fast boats.

## 1.6.17

NEW IN 1.6.17 (World Look settings > Light, under Glow Only From Lamps)
- Glow Spread: how far the glow round lamps reaches, from tight to big and soft.
- Glow Threshold: how bright part of a lamp has to be to glow (low = the whole block glows).
- Glow Distance: how far away lamps still glow (up to 24 blocks, was 14).
- On / Off key for the lamp glow.
- Your own glow per block: type blocks and strengths (0 to 2), for example diamond_ore=1.5, emerald_ore=1.5,
  redstone_torch=0. Blocks that don't give off light (ores...) can glow too, and 0 stops a lamp glowing.
- The lamp glow is stronger at the same setting.

## 1.6.16

### NEW IN 1.6.16
- Distance fog (World Look settings > Fog): far land fades into a haze the colour of the sky at the horizon, soft
  blue by day and a dark blue-grey at night. Thickest low down, thinner indoors, and the sky near the horizon
  blends in so the land melts into it.
- New look: Moody. Dark and quiet with muted colour, cool blue-grey shade, warm glowing lamps and far land lost in
  haze.
- Some looks now bring a little distance fog when you pick them (Horror, Wasteland, Frozen, Dreamy, Realistic,
  Photorealistic, Cinematic). You can change it after with the slider.

## 1.6.15

### NEW IN 1.6.15
- Lamp-only glow (World Look settings > Light): only real light sources glow (torches, lanterns, glowstone, sea
  lanterns...), in their own colour. Snow, white blocks and the sky don't. Needs World Look on.
- Rim light (World Look settings > Light): soft bright lines along block edges, any colour. Needs World Look on.
- Block face shading slider (Visuals > Lighting & Fog, and World Look > Light): 100% is normal, lower makes the sides
  of blocks as bright as the tops, 0% is a flat cartoony look. Works with or without World Look and with Sodium.
- Pitch Black Nights (World Look > Light): as dark as it goes at night and in caves, no eye adaptation brightening,
  only lamps and torches light things up.
- 3D world map settings panel (top left): detail, view distance (up to 1024 blocks), hill height, camera tilt, haze,
  darker cliff sides, you and your waypoints shown, Go To Me and Reset View. Shows how long each frame takes.
  The map also loads much faster.

## 1.6.14

NEW IN 1.6.14 (item maker, key N)
- Hotbars tab: see and edit your 9 saved creative hotbars. Pick an item from your inventory (or the item you are
  making) and click a slot to put it there, shift-click to drop it in the next free slot, right-click to empty one.
  Load, Save Mine Here and Clear for each row.
- Player tab: change your health, max health, food, saturation, level, game mode, flying, size, speed, reach,
  effects and position. Singleplayer changes apply straight away; on a server it uses commands (needs op).
- Picture as lore: type a file path or link under Name & Lore and the picture is added to the item's lore as
  coloured blocks (choose how many blocks wide).
- The item maker fits small screens better (scrolling hotbars, picture row wraps, a hint for each tab).

## 1.6.13

NEW IN 1.6.13 (Utility tab > Chat & Items)
- Symbol chat: a button above the chat box opens a panel of symbols (stars, hearts, arrows, shapes, maths, music,
  boxes, cards...), click one to type it.
- Command keys: up to 8 keys that each send a command or message (/home, /spawn, gg...).
- Component viewer: hold Left Ctrl over an item to see its data components (shift for the item's own ones too).
- Tooltip scroll: the mouse wheel moves tooltips that are too tall or wide for the screen (shift for sideways).
- Fast trading: shift-click a villager trade and it keeps buying it until you run out or it does.
- Clumps: experience is picked up all at once (singleplayer / LAN you host) with one ding instead of a flood.

## 1.6.12

### NEW IN 1.6.12
- Fair-play freecam (Visuals tab > Camera, default key B): press to fly the camera around while your player stands
  still. WASD to move, space / shift for up and down, sprint for faster. On servers it cant pass through blocks and
  stays within a set distance of you (30-100 blocks); in singleplayer it goes anywhere, through walls.

## 1.6.11

### NEW IN 1.6.11
- Instant hit feedback (Utility > Ping Equalizer group): the red flash, hit sound and crit sparks show the moment you
  hit, not after your ping, and the server's late copy is skipped. Looks only, the hit itself is unchanged
  (like BetterHitreg). Off by default.
- Open To Friends (pause menu in singleplayer): opens your world, asks your router to forward the port (UPnP) and
  shows your address to copy and send. No relay servers; if your router won't do it, it tells you which port to
  forward. The port closes again when you leave the world.

## 1.6.10

### NEW IN 1.6.10
- Ping equalizer (Utility tab): holds your ping at a set number (50-500 ms) for fair fights with laggier players,
  on servers that allow it. It always slides there at the speed you set (and back down when you turn it off), never
  jumps, and has no key, so it can't be used like a lag switch. Shows your real ping and what's added.

## 1.6.9

### NEW IN 1.6.9
- Capes from other cape mods: players with no Mojang or Onyx cape show their MinecraftCapes, OptiFine or LabyMod
  cape (Cosmetics > Images, each one can be turned off).
- Account switcher (Accounts button on the Multiplayer screen, or Utility > Little Tools): add Microsoft accounts
  (signs in in your browser) or offline names and swap between them. This session only: nothing is saved on your PC,
  closing the game forgets them. Other accounts get no chat signing keys (those would be saved as a file).

## 1.6.8

### NEW IN 1.6.8
- Resource pack browser: a Find Packs button on the resource pack screen (and Utility > Little Tools). Search
  modrinth, sort by downloads / match / newest / updated, filter by category and your Minecraft version, and
  install with one click straight into your resourcepacks folder.
- Resource pack folders: packs you put inside folders in resourcepacks/ (up to 4 folders deep) show up in the list,
  so you can sort them however you like.

## 1.6.7

### NEW IN 1.6.7
- Smooth swapping (Utility > Little Tools): items slide from slot to slot when you shift-click, use number keys,
  sort or move them, instead of jumping. Slide time setting.
- 2D arrows and tridents: drawn as their flat item picture pointing the way they fly (off by default).
- Natural motion blur (World Look > Camera): the same amount of blur at any FPS, more samples on higher quality and
  smoother streaks.

## 1.6.6

NEW IN 1.6.6 - little tools (Utility tab > Little Tools)
- Chat heads: the sender's head in front of chat lines.
- Chat calculator: type =5*64, =2^10, =sqrt(2) or =3 stacks + 10 in chat; it's worked out on your side and never sent,
  shows stacks and shulkers for big numbers and copies the answer.
- See-through item frames: only the item inside shows (optionally empty frames too).
- Visible barriers: barrier, light and structure void blocks show as see-through boxes.
- Hit range rings: your reach on the ground, and other players' (red when they can reach you).
- Hotbar key labels: the key for each hotbar slot in its corner.

## 1.6.5

NEW IN 1.6.5 - World Look overhaul (Shaders tab > Open World Look Settings)
- Its own screen with the world still showing next to it, so you see every change live: looks as colour cards,
  a quality bar (Potato / Low / Medium / High / Ultra), tabs for Light, Sky, Fog, Rain, Camera and Colour, and
  Hold To Compare to see the plain game for a moment.
- Quality: the lower settings take fewer steps through the fog, shadows, god rays and glow (faster on weak PCs);
  Ultra takes more for smoother light shafts and sharper shadows.
- New effects: eye adaptation (dark places slowly brighten), drops on the lens in the rain (more looking up),
  water running down the screen after swimming, heat haze (nether, deserts at midday), northern lights at night
  (cold places, or anywhere), rainbows after rain, lens flares from the sun, blood moons every few nights,
  low health heartbeat (colour drains, red pulses at the edges).
- Camera & colour on top of any look: cinematic bars, film grain, saturation, contrast, white balance, tint,
  split toning, faded blacks, sepia.
- New looks: Photorealistic, Dreamy, Wasteland, Vibrant Fantasy (inspired by Orange Shaders; Onyx code).

## 1.6.4

NEW IN 1.6.4 - the item editor is now an item maker (N), simpler, like mcstacker
- Make Item: pick any item from the grid on the left (with search), fill in a simple form in the middle and take
  it on the right (creative) or copy the /give. Sections open and close, and only the ones that fit show up:
  name & lore (with gradient/rainbow names), enchantments (just click them, - and + for any level), attributes
  (one click buttons: damage, speed, health, armor, reach, size...), potion effects, leather colour, banner and
  shield patterns, player heads, fireworks and firework stars, books, looks & extras, and the raw NBT for experts.
  The live tooltip shows on the right.
- Make Mob: pick a mob, give it a name, no AI, silent, glowing, cant be hurt, baby, health, size, effects, gear
  (hold your item, wear your armour), armor stand options. Get it as a spawn egg, copy the /summon, or summon it.
- My Items: every item you make is kept here (search, favourites, get it again, edit it, copy, delete).

## 1.6.3

NEW IN 1.6.3 (Visuals tab > More Visuals)
- Spear effects: a spear lunge bursts out of a ring of air with wind streaks, plus droplets, hearts, lightning,
  stars or ghost after-images; a wind trail while charging. Just you or everyone.
- Impact frames: a split second of anime-style flash frames on your kills (or mace smashes, crits, every hit).
  Ink turns the world into black-and-white ink with speed lines; Flash uses Impactful's frames (MIT). Off by default.
- Block place animation (Pop, Stretch, Wobble) with an optional flash, and crumbs puffing out along the edges.
- Particle Rain & Snow: single raindrops that splash and drifting snowflakes instead of the rain sheets. Off by default.

## 1.6.2

NEW IN 1.6.2 - item editor (N, or Utility tab > Item Editor)
- Edits the item in your hand as a draft, then puts it back in your hand or gives you a copy (creative mode), or
  copies it as a /give command or SNBT (works anywhere). Paste an item back from SNBT or a /give command.
- General: the item, count, a different look (item model), name and lore with & colour codes and &#RRGGBB colours,
  unbreakable, glint always/never, rarity, hide the tooltip or parts of it, max stack size, damage, max damage, dye
  colour, custom model data, and whose head a player head is.
- Enchants at any level (1-255), searchable. Attributes: any attribute modifier, amount, add/percent/multiply, slot.
- Effects for potions and tipped arrows: any effect, level and length (or forever), colour and base potion.
- Banner and shield patterns: base colour, layers you add, recolour, move and remove.
- Text: gradient, rainbow and alternating colours over your words, bold/italic/underline/strike, as the name or
  a lore line.
- Components: every data component of the item one by one, to edit as SNBT, remove or add; can show the item's
  own default ones too (take one off the item, or change it).
- Raw: the whole item as SNBT with colours, read as you type, with the wrong line marked in red.

## 1.6.1

### NEW IN 1.6.1
- Isometric minimap (Utility tab > Minimap & World Map > View: Isometric): the land seen from an angle like a little
  diorama, hills, trees and cliffs standing up. North sits up-right, or it turns with you like the normal minimap.
  Hill Height sets how tall the land stands. Waypoints, players, mobs, the cave map, slime chunks, the light overlay
  and the chunk grid all work in it.

## 1.6.0

NEW IN 1.6.0 - minimap, world map, better waypoints (Utility tab > Minimap & World Map, Waypoints)
- Minimap (move it in the HUD editor): the map round you, turning with you or north up (with an arrow), square
  or round, sizes from small to huge (or automatic), zoom (I / O keys). Hold Z for a big one in the middle of the
  screen, zoomed out. Shows waypoints (pulled to the edge when they're further off), players (as their heads),
  hostile and friendly mobs, items and everything else (each can be turned off), names, which way north is,
  and under it your coordinates, and optionally the biome, light level, time (12 or 24 hour) and camera angles.
  Cave mode by itself underground and indoors (how big a roof counts is a setting), and always in the Nether.
  Chunk grid, slime chunks (singleplayer) and a light overlay that marks dark spots where mobs can spawn.
  Fair-Play turns off the entity radar and cave maps. It can be set to show only while you carry an item
  (a compass, say).
- Colours: Vanilla (the paper map colours, with biome grass, leaf and water colours if you like) or Accurate
  (each block's own texture colour, following your resource packs). Terrain Depth and Terrain Slopes shading.
- World map (M): everything you've explored, saved per server or world and dimension. Drag to move, wheel to
  zoom round the mouse. Your waypoints are on it with a list to the side (with a filter); right-click to add a
  waypoint, teleport there, or share, hide or delete one. Your recent footsteps show where you've been.
- Draw and write on the world map: Pen, Path (plain or dotted, with an X at the end), Area (click round it),
  Chunks (paint whole chunks), Text, and an eraser; nine colours; put them in collections you can show or hide
  together. Export the map as a PNG.
- 3D view (the 3D button on the world map): the land you've explored as hills and valleys; drag to turn and
  tilt, wheel to come closer, WASD to move.
- Waypoints: a list (U) with search, sorting (newest, name, distance) and sets you switch between. Each one
  has a name, place, icon (two letters), colour, shape (square, diamond, circle, flag) and set; global ones
  show from anywhere, local ones only close by. Area waypoints cover a box (a second corner), drawn in the
  world. Teleport (needs permission), share in chat, hide, delete. Keep Old Deathpoints keeps the earlier
  death spots as plain waypoints. Hide Coordinates hides them everywhere for streams.
- No Sign Editor When Placing: signs go down blank without the editor popping up (quicker traps).

## 1.5.20

### FIXED IN 1.5.20
- Waving grass jumping about all at once: the drifting gusts were worked out from the wind's speed times the
  time, so whenever the wind changed speed the whole pattern jumped. They move on a little each frame now, and
  the field leans over gradually when the wind turns or picks up.
- Grass range goes out to 64 blocks (fewer blades far off, so it stays fast).
- The sky in snowy places (and other thick-fog biomes) washing out white: thinner snowy-biome fog, and the fog
  over the open sky lets more of the sky through (still meeting the land at the horizon).

## 1.5.19

### NEW IN 1.5.19
- Grass styles (Shaders tab > Grass & Snow > Grass Style): Natural, Vanilla-Like (the game's own tufts,
  everywhere), Realistic (thin pointed blades, packed close) and Wild Meadow (tall, uneven, in patches). New
  Blade Width, Wind Sway and Colour Variety (some blades darker, some gone yellow) sliders; Height now goes up
  to 4.
- Grass grows round small things standing on it: lanterns, torches, flowers, flower pots, fence posts (not
  through slabs, carpets or snow).
- Deep snow is one smooth blanket: small steps in snowy ground become soft slopes, it banks up against walls,
  a lone snowy block gets a rounded cushion with snow heaped round it, and it rounds off where the snow ends.

### FIXED IN 1.5.19
- The grass's wind: blades bend in a curve (the root stays upright), gusts drift across the field in patches
  instead of rolling stripes, and the flutter is calmer.
- Deep snow: no more jagged blue shadow teeth along steps and trails, no dark or blue facets that changed as
  you turned, no tent shapes over single blocks.
- Wet ground soaks up slowly when rain starts (about a minute) and under passing showers too, instead of
  turning wet at once; it dries off slowly after.
- Rain wets the ground a little way in under an overhang from its open side, instead of stopping in a hard
  line at the roof's edge.
- Puddles: sharper, more ragged edges, and their shallow edges show the ground through them while the middle
  is more of a mirror.
- Walking up to lamps: their glow in the fog no longer pops on and off as the nearest ones change, and it, the
  lamps' light on the ground and the bloom all ease off instead of flooding the view.

## 1.5.18

### FIXED IN 1.5.18
- The sun washing the whole view out yellow with a warm look (Golden Hour) and God Rays turned up: the god
  rays counted the whole hazy sky as sunlight once 1.5.17's thicker fog brightened it, and the look's own rays
  were applied on top of the slider's. They now come from the sky near the sun, and ease off rather than
  burning out. The sunlight in the volumetric fog eases off the same way.
- Grass blades turning as you walked: each blade used to turn to face you, so the field shifted with every
  step. Each one now stands its own fixed way.
- The soft glow round bright things is smoother (it could leave faint copies beside bright lamps).

## 1.5.17

### NEW IN 1.5.17
- Waving grass (Shaders tab > Grass & Snow): a field of grass blades over grass blocks that sways in the wind,
  with gusts rolling across it in waves (the same wind as the rain), and parts round players and mobs walking
  through it. Coloured by the biome and lit like the world (dark at night and in caves). Density, Height and
  Range sliders. Onyx's own; works with Sodium; off while a shader pack is on. The game's own short grass
  stays as it is between the blades.
- Deep snow (Shaders tab > Grass & Snow): soft snow over the game's snow that you sink into and plough trails
  through, heaped up at the sides; trails stay and slowly fill back in while it snows. Snow Depth slider and a
  Trails switch.
- Biome fog (World Look > Biome Fog): each biome has its own air, like shader packs: murky green swamps,
  dusty deserts, white mist where it's snowy, humid jungles, grey dark forests, pink cherry groves... It fades
  over a few seconds as you cross between biomes.
- Volumetric fog closer to shader packs: mist lies on the ground wherever the ground is (more at dawn and
  after rain), crisper sun shafts through gaps in the trees (the God Rays slider sets how bright), and lamps
  glow softly in the fog at night and indoors.

### FIXED IN 1.5.17
- Removed the effects on glass (raindrops and wet ground drawn through it): they looked wrong and moved as
  you moved.
- Puddles no longer glitch when you go up or down (the camera height reached the shader rounded to 1/32 of a
  block).
- Snow-covered ground no longer gets puddles while it rains elsewhere (a mistake in 1.5.16).

## 1.5.16

NEW IN 1.5.16 - more realistic rain puddles (World Look)
- Puddles have ragged, natural edges instead of round blobs, a soaked rim round them, and look like clear water:
  looking down you see the dark ground under them with the sky over it, towards the distance they turn into
  sharp mirrors (lanterns, posts, trees and walls all show in them).
- Water runs off where the ground drops away beside a block and gathers against walls; grass soaks up more of
  it, so fewer puddles there than on stone and paths.
- Two layers of raindrop rings, small wind ripples on the puddles, the sun glints off them when it breaks
  through, and lamps shine off wet ground as bright streaks at night (even lamps off screen).

### FIXED IN 1.5.16
- Typing in the menu's search bar on the title screen crashed the game (the Hitboxes tab made item names before
  a world had loaded). Search now also just skips a tab that can't be built instead of breaking the menu.
- Puddles and wet ground no longer change as you walk around: how wet the ground is came from the spot you
  stood on, so walking into another biome or under a passing shower made every puddle in sight grow or
  shrink at once. Now each spot is wet from the weather where it is: deserts and snowy places stay dry, and
  passing showers wet only the ground they're over or have just passed.
- A lantern on a post (or anything short standing on its own) no longer keeps its whole block dry: the rest of
  the block gets its puddle.

### REMOVED IN 1.5.16
- Fine Rain Streaks (the warped-looking World Look rain): the game's own rain shows again.

## 1.5.15

NEW IN 1.5.15 - World Look presets (Shaders tab > World Look > Look Preset)
- 12 whole looks in one pick, Onyx's own (inspired by the feel of shader packs like Bliss, Photon and Solas,
  no code taken from them):
  Onyx (Default) - the look as before.
  Realistic - film-like light, rich natural colour, warm sun and cool shade, a deep blue sky.
  Vibrant - bold saturated colour and a deep sky.
  Soft Warm - pastel and warm with a big soft glow.
  Cinematic - teal shadows, orange light, film contrast.
  Horror - drained colour, thick grey fog, red-tinged shadows, film grain, colour fringes and a slowly
  breathing dark vignette.
  Cartoony - bright colour in flat light bands with ink outlines round everything.
  Noir - black and white, hard contrast, grain.
  Vintage Film - faded sepia film with grain.
  Neon Nights - magenta and cyan with glow round every light.
  Golden Hour - everything in late-afternoon gold with long god rays.
  Frozen - cold, pale and crisp.
- Picking a preset also sets the Brightness, Fog, God Rays and Night Darkness sliders to suit it; every slider
  can still be changed after.

## 1.5.14

FIXED IN 1.5.14 - World Look rain, closer to real rain shaders
- Reflections in wet ground and puddles are no longer warped or smeared: the mirror uses the exact flat face of
  the block (the direction read from the depth picture wobbled), and a reflection ray that only slips behind a
  block no longer counts as hitting it (that stretched blocks into pale ghost copies). Raindrop rings bend
  puddles only slightly.
- Puddles look like dark water: seen from above they show the dark wet ground, and mirror more the flatter you
  look across them (like real water); wet ground is darker and richer.
- Rain: no more long lines across the screen from drops right in front of your face; the nearest drops are a
  couple of blocks away, thin and fine, falling at a slant.
- Stormy nights: the sky is a dark blue-grey with cloud shapes you can see (it went pitch black), and the fog is
  a dark grey-blue instead of black.


NEW IN 1.5.13 - cinematic camera (Modules > Cinematic Camera)
- Cinematic When AFK: after a while without touching anything (AFK After slider, 45 s by default) the camera turns
  into a film crew around you: slow orbits, dollies past, crane shots, low angles, wide and top-down shots, cutting
  to a new one every 10 seconds with a short fade, black bars and no HUD. Any key or mouse movement ends it.
- Cinematic Camera (F7 by default): the same camera, switched on with a key while you keep playing (your keys and
  mouse still move you). The camera never goes through walls; view bobbing and hurt shake are left out of it.
- Normal View Box: while the key mode is on, a box in a corner shows your normal screen: your first-person view with
  your HUD and any menu you open (inventory, chests, the Onyx menu). Box Size, Box Corner,
  Box Updates Every N Frames (it borrows every Nth frame, so it costs no extra FPS), and World Look In The Box (off:
  World Look only on the big screen, which is also faster).
- GUI Only In The Box (on by default): your HUD, chat and any menu you open show only inside the box; the big screen
  is just the cinematic shot. Point and click at menus in the box (the mouse over the box reaches the menu). Off:
  the HUD and menus show on the big screen as usual (and in the box too).
- Pop Out To Its Own Window (Windows): the box becomes its own window you can drag onto another monitor, resize or
  maximise; its place and size are remembered, and closing it puts the box back in the game. While it's popped out,
  menus open on the game screen so you can click them (they show in the window too).
- Its own settings group (Modules > Cinematic Camera): Shot Types (all, close ups, wide shots), Shot Length, Camera
  Speed, Camera Distance, Fade Between Shots, Black Bars and Bar Size, Hide HUD in key mode.
- The AFK frame-rate cap waits while the cinematic is on.

NEW IN 1.5.13 - server macro panel
- Your inventory (E) has a Macros panel on its left: dupe on/off, dupe amount, how often, drop delay, and sellall
  on/off. Click its title to fold it away; it stays folded. Utility > Server Macros > Macro Panel In Inventory hides it.

FIXED IN 1.5.13 - World Look
- Rain puddles at night no longer look like black blotches or shadows: wet ground only darkens a little at night, and
  a puddle mirroring the black sky shows the ground through it (lamps and lit things still reflect in it).
- The ground right around lanterns, fences and chains standing in the rain gets wet too (it stayed in dry squares).

## 1.5.13

NEW IN 1.5.13 - cinematic camera (Modules > Cinematic Camera)
- Cinematic When AFK: after a while without touching anything (AFK After slider, 45 s by default) the camera turns
  into a film crew around you: slow orbits, dollies past, crane shots, low angles, wide and top-down shots, cutting
  to a new one every 10 seconds with a short fade, black bars and no HUD. Any key or mouse movement ends it.
- Cinematic Camera (F7 by default): the same camera, switched on with a key while you keep playing (your keys and
  mouse still move you). The camera never goes through walls; view bobbing and hurt shake are left out of it.
- Normal View Box: while the key mode is on, a box in a corner shows your normal screen: your first-person view with
  your HUD and any menu you open (inventory, chests, the Onyx menu). Box Size, Box Corner,
  Box Updates Every N Frames (it borrows every Nth frame, so it costs no extra FPS), and World Look In The Box (off:
  World Look only on the big screen, which is also faster).
- GUI Only In The Box (on by default): your HUD, chat and any menu you open show only inside the box; the big screen
  is just the cinematic shot. Point and click at menus in the box (the mouse over the box reaches the menu). Off:
  the HUD and menus show on the big screen as usual (and in the box too).
- Pop Out To Its Own Window (Windows): the box becomes its own window you can drag onto another monitor, resize or
  maximise; its place and size are remembered, and closing it puts the box back in the game. While it's popped out,
  menus open on the game screen so you can click them (they show in the window too).
- Its own settings group (Modules > Cinematic Camera): Shot Types (all, close ups, wide shots), Shot Length, Camera
  Speed, Camera Distance, Fade Between Shots, Black Bars and Bar Size, Hide HUD in key mode.
- The AFK frame-rate cap waits while the cinematic is on.

NEW IN 1.5.13 - server macro panel
- Your inventory (E) has a Macros panel on its left: dupe on/off, dupe amount, how often, drop delay, and sellall
  on/off. Click its title to fold it away; it stays folded. Utility > Server Macros > Macro Panel In Inventory hides it.

FIXED IN 1.5.13 - World Look
- Rain puddles at night no longer look like black blotches or shadows: wet ground only darkens a little at night, and
  a puddle mirroring the black sky shows the ground through it (lamps and lit things still reflect in it).
- The ground right around lanterns, fences and chains standing in the rain gets wet too (it stayed in dry squares).

## 1.5.12

NEW IN 1.5.12 - wind, passing showers, sun shadows
- Wind: a direction and strength that drift over time with gusts, stronger in rain and storms (Wind slider).
  Rain blows sideways with it and comes in gusty sheets; clouds drift with it.
- Passing Showers: rain clouds drift across the world even when the server's weather is clear. Far off you see
  the rain hanging under them; when one passes over you it rains on you (with rain sounds) and the ground gets wet.
  How Many Showers slider.
- Sun Shadows: buildings, hills, trees, fences and plants cast shadows in sunlight (soft-edged, bluish like real
  shade), faint ones by moonlight; weaker under clouds. Shadow Darkness slider.
- Realistic Sounds > Wind: you hear the wind, made live, gusting with it, louder out in the open, a whisper indoors.
- Water past the edge of World Look's map (far out at sea) gets the new water look too.

## 1.5.11

NEW IN 1.5.11 - Realistic Sounds (Shaders tab)
- Echo: sounds echo the way the place you're in would (a small room, a big cave, almost none in open fields),
  measured from your surroundings a couple of times a second. Echo Amount slider.
- Muffled Through Walls: sounds on the other side of blocks lose their high end and some volume, more blocks more so.
- Real Thunder: thunder uses real recordings (close cracks, rumbles, far grumbles) picked by how far the strike was,
  arriving later the further it was. Thunder sounds from ImmersiveThunder by netcatgirl (MIT License).

WORLD LOOK in 1.5.11
- Puddles and wet patches stay put as you move (they used to jump every 64 blocks); same for clouds and fog.
- Rain and wet ground show through glass; raindrops bead on glass panes and some run down.
- New rain: thin see-through streaks lit by the sky, lightning and nearby lamps, out of focus up close, a soft sheet
  of rain far away, swaying with the wind.
- More puddles, with sharper mirror reflections; reflections now show the real sky instead of a guessed one, and
  stay dark at night (no more pale patches round lamps).
- Coloured lamp light is a soft tint instead of flooding everything one colour (copper lanterns especially).

## 1.5.10

FIXED IN 1.5.10 - World Look
- Walking and sprinting with view bobbing no longer makes the reflections, fog, clouds and sky swim against the
  world: World Look now follows the same bob (and hurt shake) the game draws with.
- Looking towards the sun no longer washes the screen out white: the glow in the fog, the god rays and the
  sun's halo are all much softer, and rays only come from the brightest parts of the sky.

## 1.5.9

NEW IN 1.5.9 - More Visuals (Shaders tab)
- Sword Slash Trail: a glowing crescent cuts through the air when you swing a sword, axe, trident or mace
  (just you, or everyone nearby), alternating direction each swing, in your colour.
- Totem Spirit: a golden column of light, climbing rings and spiralling strands rise out of anyone who pops a totem.
- Floating Crystals: 1 to 6 small glowing gems circle you in third person, in your colour.
- Weather Alerts: a pop-up when rain or a thunderstorm starts or stops.
- Hit Particles: sparks, stars or hearts burst out where your hits land, in your colour.
- Aura: a soft glow behind you, a breathing ring of light at your feet and motes drifting up (third person).
- Crown: a small turning golden crown with red gems floats over your head (third person).
- Floating Crystals leave a trail of little sparkles.

## 1.5.8

NEW IN 1.5.8 - World Look: rain, fog and reflections
- Ground gets wet gradually when it rains (patch by patch, about 25 seconds to soak) and dries slowly after it
  stops (about a minute and a half); puddles grow as it gets wetter and shrink as it dries.
- Raindrop rings fade in and out smoothly and sit mostly in puddles; the game's blue splash pixels that blinked on
  the ground are hidden while World Look draws the rain.
- New rain: short, thin, faint drops at several distances with a slight slant, no more long lines when you look down.
- Volumetric fog (new switch): drifting fog you can see light in, sun and moon shafts through trees and roofs, and
  glowing halos round lamps. Distance fog takes over past 110 blocks.
- Better reflections: sharper edges, fade out softly at the screen edges, and reflect the sky and clouds when they
  leave the screen. Water has two sizes of waves, calmer far away.
- Water and wet ground now show out to 256 blocks (was 64).

## 1.5.7

### FIXED IN 1.5.7
- No more crash with an Iris shader pack: while a pack is on, Onyx turns off its own screen effects (World Look,
  custom sky, Painted World, its lightning) and the extra layers it draws on your arm and on blocks. They come back
  when you turn the pack off. (The crash was the hand shader drawing your arm a second time.)

NEW IN 1.5.7 - World Look, rebuilt
- Much less bright: new Brightness slider (85% by default), gentler colour curve, glow only around really bright things.
- God rays: sunlight (and faint moonlight) streaming through gaps in clouds, trees and buildings, stronger in fog.
- Fog: thin on clear days, thick in rain and snow, misty at sunrise and sunset, thicker down low, glowing towards the sun.
- Coloured light: lamps light what's around them in their own colour (torches warm, soul fire blue, redstone red,
  sea lanterns cool, amethyst purple...).
- Snow: no harsh white, soft blue shadows, and it glitters as you move. The game's own falling snow stays.
- Smooth Textures: block textures up close are smoothed so you can't see their pixels.
- Corner shadows are smooth now (no more stepped rings on snow), and caves go properly dark.
- Water is darker and deeper, with sun glints on the waves; clouds get silver edges near the sun.
- The Shaders tab is just World Look now (plus Rain, Lightning & Music, Custom Sky). The block / item / hand shader
  effects and Painted World were taken out of the menu and switched off.

NEW IN 1.5.6 - World Look, much more realistic
- Tuned against a real shader-pack video: soft shadows in corners and where blocks meet, real night darkness
  (unlit places go nearly black, lantern-lit places keep their warmth), lanterns and torches spill warm light
  onto the blocks around them, soft dark storm clouds with lighter gaps (lit from inside by lightning) instead of
  blocky ones, fine faint rain streaks instead of the chunky blue ones, deep reflective wavy water, motion blur when
  you turn, a wider warm glow around lights, and a strike now lights the sky instead of turning night into day.
  Each has its own switch in Shaders > World Look (plus Night Darkness and Motion Blur Amount).

NEW IN 1.5.5 - World Look, realistic lightning, music sync
- Shaders > World Look (no shader pack needed): rain makes ground and walls that are open to the sky wet and glossy,
  with real reflections of the world, puddles and raindrop ripples (roofs keep the floor under them dry), misty
  distance in rain, cinematic colours, a soft glow around lights and a vignette. Each part has its own switch,
  plus Wetness, Colour Strength and Reflection Quality.
- Realistic Lightning: jagged branching bolts with a white-hot core and blue glow, flickering re-strikes, a flash
  over the world and thunder that arrives later the farther away it struck. Replaces the game's own bolts.
- Sync With Music: reads how loud the music on your PC is (Spotify, YouTube... never Minecraft's own sounds) and
  pulses the World Look on the beat, speeds up the ripples, and can call lightning down on strong beats.
- Shaders > Follow My Camera: block shaders look like a window you see through (they stay put on your screen as
  you move, like the end portal) instead of being painted on the block. Also fixes the old window effects:
  right in third person, no warping on big faces, no seams between blocks.

NEW IN 1.5.4 - server macros
- Utility > Server Macros, for servers that have /dupe and /sellall: Dupe Macro runs /dupe N every few seconds
  and drops the copies (everything except your held item); Sellall Macro runs /sellall inventory and drops what's
  left (filled shulkers are kept). Each has a toggle key, amount / interval / drop-delay sliders, and both switch
  off when you leave a server (they never start on their own after a restart).

NEW IN 1.5.3 - new title screen
- New Onyx title screen (now on by default): a calm dark grey backdrop, a glowing logo and "Onyx Client" on the
  left with plain glowing text buttons (the one under the mouse gets a soft light bar), your own skin walking in
  from the right and stopping in the middle (then turning to face you and following the mouse with its head),
  your name over its head, white smoke drifting up the right edge and twinkling stars.
  "Normal title screen" (bottom right) still opens the old one; Menu Settings > Onyx Title Screen turns it off.
- No more 3D icons: the title screen and pause menu buttons are plain text, and look presets no longer turn the
  menu's 3D icons on (they are switched off once; Menu Settings > 3D Icons can still turn them back on).

FROM 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.6

NEW IN 1.5.6 - World Look, much more realistic
- Tuned against a real shader-pack video: soft shadows in corners and where blocks meet, real night darkness
  (unlit places go nearly black, lantern-lit places keep their warmth), lanterns and torches spill warm light
  onto the blocks around them, soft dark storm clouds with lighter gaps (lit from inside by lightning) instead of
  blocky ones, fine faint rain streaks instead of the chunky blue ones, deep reflective wavy water, motion blur when
  you turn, a wider warm glow around lights, and a strike now lights the sky instead of turning night into day.
  Each has its own switch in Shaders > World Look (plus Night Darkness and Motion Blur Amount).

NEW IN 1.5.5 - World Look, realistic lightning, music sync
- Shaders > World Look (no shader pack needed): rain makes ground and walls that are open to the sky wet and glossy,
  with real reflections of the world, puddles and raindrop ripples (roofs keep the floor under them dry), misty
  distance in rain, cinematic colours, a soft glow around lights and a vignette. Each part has its own switch,
  plus Wetness, Colour Strength and Reflection Quality.
- Realistic Lightning: jagged branching bolts with a white-hot core and blue glow, flickering re-strikes, a flash
  over the world and thunder that arrives later the farther away it struck. Replaces the game's own bolts.
- Sync With Music: reads how loud the music on your PC is (Spotify, YouTube... never Minecraft's own sounds) and
  pulses the World Look on the beat, speeds up the ripples, and can call lightning down on strong beats.
- Shaders > Follow My Camera: block shaders look like a window you see through (they stay put on your screen as
  you move, like the end portal) instead of being painted on the block. Also fixes the old window effects:
  right in third person, no warping on big faces, no seams between blocks.

NEW IN 1.5.4 - server macros
- Utility > Server Macros, for servers that have /dupe and /sellall: Dupe Macro runs /dupe N every few seconds
  and drops the copies (everything except your held item); Sellall Macro runs /sellall inventory and drops what's
  left (filled shulkers are kept). Each has a toggle key, amount / interval / drop-delay sliders, and both switch
  off when you leave a server (they never start on their own after a restart).

NEW IN 1.5.3 - new title screen
- New Onyx title screen (now on by default): a calm dark grey backdrop, a glowing logo and "Onyx Client" on the
  left with plain glowing text buttons (the one under the mouse gets a soft light bar), your own skin walking in
  from the right and stopping in the middle (then turning to face you and following the mouse with its head),
  your name over its head, white smoke drifting up the right edge and twinkling stars.
  "Normal title screen" (bottom right) still opens the old one; Menu Settings > Onyx Title Screen turns it off.
- No more 3D icons: the title screen and pause menu buttons are plain text, and look presets no longer turn the
  menu's 3D icons on (they are switched off once; Menu Settings > 3D Icons can still turn them back on).

FROM 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.5

NEW IN 1.5.5 - World Look, realistic lightning, music sync
- Shaders > World Look (no shader pack needed): rain makes ground and walls that are open to the sky wet and glossy,
  with real reflections of the world, puddles and raindrop ripples (roofs keep the floor under them dry), misty
  distance in rain, cinematic colours, a soft glow around lights and a vignette. Each part has its own switch,
  plus Wetness, Colour Strength and Reflection Quality.
- Realistic Lightning: jagged branching bolts with a white-hot core and blue glow, flickering re-strikes, a flash
  over the world and thunder that arrives later the farther away it struck. Replaces the game's own bolts.
- Sync With Music: reads how loud the music on your PC is (Spotify, YouTube... never Minecraft's own sounds) and
  pulses the World Look on the beat, speeds up the ripples, and can call lightning down on strong beats.
- Shaders > Follow My Camera: block shaders look like a window you see through (they stay put on your screen as
  you move, like the end portal) instead of being painted on the block. Also fixes the old window effects:
  right in third person, no warping on big faces, no seams between blocks.

NEW IN 1.5.4 - server macros
- Utility > Server Macros, for servers that have /dupe and /sellall: Dupe Macro runs /dupe N every few seconds
  and drops the copies (everything except your held item); Sellall Macro runs /sellall inventory and drops what's
  left (filled shulkers are kept). Each has a toggle key, amount / interval / drop-delay sliders, and both switch
  off when you leave a server (they never start on their own after a restart).

NEW IN 1.5.3 - new title screen
- New Onyx title screen (now on by default): a calm dark grey backdrop, a glowing logo and "Onyx Client" on the
  left with plain glowing text buttons (the one under the mouse gets a soft light bar), your own skin walking in
  from the right and stopping in the middle (then turning to face you and following the mouse with its head),
  your name over its head, white smoke drifting up the right edge and twinkling stars.
  "Normal title screen" (bottom right) still opens the old one; Menu Settings > Onyx Title Screen turns it off.
- No more 3D icons: the title screen and pause menu buttons are plain text, and look presets no longer turn the
  menu's 3D icons on (they are switched off once; Menu Settings > 3D Icons can still turn them back on).

FROM 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.4

NEW IN 1.5.4 - server macros
- Utility > Server Macros, for servers that have /dupe and /sellall: Dupe Macro runs /dupe N every few seconds
  and drops the copies (everything except your held item); Sellall Macro runs /sellall inventory and drops what's
  left (filled shulkers are kept). Each has a toggle key, amount / interval / drop-delay sliders, and both switch
  off when you leave a server (they never start on their own after a restart).

NEW IN 1.5.3 - new title screen
- New Onyx title screen (now on by default): a calm dark grey backdrop, a glowing logo and "Onyx Client" on the
  left with plain glowing text buttons (the one under the mouse gets a soft light bar), your own skin walking in
  from the right and stopping in the middle (then turning to face you and following the mouse with its head),
  your name over its head, white smoke drifting up the right edge and twinkling stars.
  "Normal title screen" (bottom right) still opens the old one; Menu Settings > Onyx Title Screen turns it off.
- No more 3D icons: the title screen and pause menu buttons are plain text, and look presets no longer turn the
  menu's 3D icons on (they are switched off once; Menu Settings > 3D Icons can still turn them back on).

FROM 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.3

NEW IN 1.5.3 - new title screen
- New Onyx title screen (now on by default): a calm dark grey backdrop, a glowing logo and "Onyx Client" on the
  left with plain glowing text buttons (the one under the mouse gets a soft light bar), your own skin walking in
  from the right and stopping in the middle (then turning to face you and following the mouse with its head),
  your name over its head, white smoke drifting up the right edge and twinkling stars.
  "Normal title screen" (bottom right) still opens the old one; Menu Settings > Onyx Title Screen turns it off.
- No more 3D icons: the title screen and pause menu buttons are plain text, and look presets no longer turn the
  menu's 3D icons on (they are switched off once; Menu Settings > 3D Icons can still turn them back on).

FROM 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.2

FIXED IN 1.5.2 - 26.3 menu input
- 26.3: sliders can be dragged again, and text boxes, the search box and typed slider values take typing again.
  26.3 switched Minecraft to new input handling (SDL) that numbers mouse buttons differently (left click
  arrived as a right click) and only sends typed letters when a screen asks for them. Both menus (normal and
  floating) handle that now; other versions are unchanged.
- 26.x: no more crash on startup ("Block models not yet initialized") with mods that hide the loading screen
  (Remove Reloading Screen): the 3D Onyx logo on the title screen now waits until the game has loaded.

FROM 1.5.1 - NanoVG drawing
- The menu and the HUD are now drawn with NanoVG: truly round, anti-aliased corners, smooth outlines and real
  soft shadows instead of stepped pixel corners. Text, items and 3D models still draw on top in the right
  order, and dropdowns / colour pickers get their own layer above the menu.
- Menu Settings > "Smooth Drawing (NanoVG)" turns it off. It also switches itself off (back to the normal
  drawing) when the game runs on Vulkan (26.2+) or if NanoVG can't start. The floating menu keeps its 3D
  drawing.

### FROM 1.5.0
- Custom skies and combat visuals.

## 1.5.1

NEW (Shaders tab)
- Custom Sky: Golden Storm, Gold Waves, Storm Clouds (with lightning), Deep Space, Black Hole, Synthwave
  Sunset, Blood Sky, Star Web (long glowing lines between stars), Orange Sky, Aurora Night. The sky turns
  with your camera like a real one, clouds drift, stars twinkle, far land fades into the new sky (no fog
  seam). Off in the Nether and underwater. Only you see it.
- Combat Visuals:
  - Jump Circles (Ring, Spiral, Double Ring, Shockwave) when players jump.
  - Target Ring: a spinning dashed ring around the player you're fighting, with a second ring moving up
    their body.
  - Hit Markers: X marks fly off where your hits land.
  - Light Trails: glowing ribbons behind you or every player.
  - Hand Glow: a glowing edge around your first-person arm, in any colour.
  - Halo over your head (third person).

### FROM 1.4.14
- Explosion effects, lyrics fixes.

## 1.4.14

### NEW IN 1.4.14
- Explosion Effects (Fire & Overlays tab): when TNT, crystals or anchors blow up near you, a glowing
  yellow fireball swells and fades, a red-orange shockwave ring races out along the ground, orange ember
  flakes flutter down, chunks of the blown-up blocks fly out, tumble and bounce, the screen flashes and the
  camera shakes (stronger the closer you are). Minecraft's own explosion smoke is hidden near the blast, so
  only these show ("Hide Normal Explosion Particles"). Each part can be turned off; only you see them.
- Lyrics "Floating In Front Of Me" now follows you looking up and down (up to 30 degrees), so it stays on
  screen, and lyrics are 50% bigger at the same Size setting.

### FROM 1.4.13
- Glint-style item shaders, hand shader, Ultra 4K shaders, lyrics where you look, new song animation.
