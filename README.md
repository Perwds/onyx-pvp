# Onyx PvP

**One client mod for PvP, visuals, friends and your whole desktop.**

Onyx is a client-side Fabric mod for Minecraft. It needs nothing on the server, and it works without a shader pack. Your skies, menus, replays, maps and even your PC apps all live in one mod.

![Minecraft](https://img.shields.io/badge/Minecraft-1.21.11%20%7C%2026.1.2%20%7C%2026.2%20%7C%2026.3-3c8527)
![Loader](https://img.shields.io/badge/Loader-Fabric-dbb07a)
![Version](https://img.shields.io/badge/Version-1.6.37-5b9bd5)
![Side](https://img.shields.io/badge/Side-Client%20only-0e1115)

> The full source is private. This repo describes the project and includes a few code samples.
> See [Releases](https://github.com/Perwds/onyx-pvp/releases) for notes on major versions, or the [changelog](CHANGELOG.md) for all of them. There are no downloads here.

**Contents:** [At a glance](#at-a-glance) · [Features](#features) · [How it's built](#how-its-built) · [Code samples](#code-samples) · [Credits](#credits) · [Legal](#legal)

## At a glance

| | |
|---|---|
| Minecraft versions | 1.21.11, 26.1.2, 26.2, 26.3 |
| Size | About 63,000 lines of Java |
| World Looks | 18 |
| Skies | 10 |
| Block and item shaders | 41 presets, plus your own |
| Menu themes | 23 |

## Features

### World and visuals

- **World Look:** rain that wets the ground, puddles, sun shadows, deep snow, waving grass and lighting, with 18 styles and presets you can save. No shader pack needed.
- **RTX Remix preset:** a beta path tracing option for 1.21.11 on supported NVIDIA cards.
- **Custom skies:** skies such as Deep Space, Black Hole and Aurora Night that turn with your camera, with far terrain faded into the sky so there's no fog seam.
- **Deep Snow:** soft snow you sink into, which keeps trails where players and mobs walk.
- **Shaders:** 41 block and item shader presets with a custom effect editor.
- **Painted World:** a filter that repaints the game as an oil painting.

### Combat

- **Combat visuals:** jump circles, target rings, hit markers, light trails, hand glow and explosion effects.
- **Hitboxes and HUD:** custom hitbox colours, and a drag-and-drop HUD editor.
- **Practice and kits:** a practice world, plus inventory kits you can bind to keys.
- **Item borders:** coloured borders for items and rarities in inventories and the hotbar.

### Menus

- **3D menus:** a custom title screen and menus using models made in Blender.
- **Floating menu:** the whole menu can hang in the world, flat or curved. Other Onyx players can see it, with your settings hidden.
- **Themes:** 23 themes, from Synthwave to Windows 95 and MS-DOS.
- **Saved configs:** save your whole setup and load it back. Friends, waypoints and keys stay out of the file, so it's safe to share.

### Friends

- **Friends list:** add people by name, even when they're offline. They get a request to accept.
- **Friends checklist:** see what's working with each friend, and fix what isn't in one click.
- **Friends panel:** see friends' health, armour, hotbar and effects, encrypted between the two of you.
- **Cosmetics:** capes, shields, name images, trails and 3D player models that other Onyx players can see.
- **Watch Together:** shared video links that play in sync, on a screen in the world.
- **Open To Friends:** an address friends can join, with no router setup.

### Desktop apps (Windows)

- **Apps in your world:** pin any PC app in the world, whether it's open or not, and use it by aiming and clicking.
- **Share with friends:** show an app to friends at up to 4K. They can watch it full screen from anywhere.
- **Friends can click:** optional for each app, and off until you turn it on. It's mouse only, and only reaches that one app.

### Tools

- **Replay tools:** clip recording, a replay editor with a timeline, and analysis of item switches, reach and CPS.
- **Maps and waypoints:** a minimap, a 3D map and a world map saved per server or world, with waypoints that can tint the real surfaces of an area.
- **Spotify lyrics:** lyrics shown as text in the world, with 10 fonts and 8 animations.
- **Item maker:** build items in a visual editor, then copy the `/give` command.
- **Sound Studio:** change or build the sounds the game plays.

## How it's built

- One codebase builds for Minecraft 1.21.11, 26.1.2, 26.2 and 26.3 using [Stonecutter](https://stonecutter.kikugie.dev/).
- It hooks into the game with 104 Fabric Mixins, and the build checks that every one made it into each jar.
- An in-game test script runner plays through 167 scripts in the real game to check releases.
- 3D menu models are made in Blender with baked ambient occlusion and loaded through a custom mesh format.
- Friend features are sealed with AES-GCM, using X25519 keys agreed between each pair of friends. A check code lets you confirm nobody swapped them.

## Code samples

These are small parts of the project, taken from version 1.5.0. They show how it works, but they won't build on their own.

| File | What it shows |
|---|---|
| [`samples/shaders/sky.fsh`](samples/shaders/sky.fsh) | Draws the custom skies, looking up each pixel by view direction using camera data packed into a small texture. |
| [`samples/shaders/painted.fsh`](samples/shaders/painted.fsh) | The post-processing pass behind the Painted World filter. |
| [`samples/java/ReplayAnalysis.java`](samples/java/ReplayAnalysis.java) | Reads a replay clip and lists item switches, totem pops, reach, CPS and aim snaps for every player, and flags anything inhumanly fast. |
| [`samples/java/GuiMesh.java`](samples/java/GuiMesh.java) | Loads the custom `.omesh` format for 3D menu models, so they can follow the menu's theme. |
| [`samples/blender/gui_models.py`](samples/blender/gui_models.py) | Builds the 3D menu models in Blender and exports them as `.omesh` files. |
| [`samples/tests/combattag.txt`](samples/tests/combattag.txt) | One of the in-game test scripts, which plays through a feature and takes screenshots. |
| [`samples/build/stonecutter.properties.toml`](samples/build/stonecutter.properties.toml) | The per-version settings that let one codebase build for four Minecraft versions. |

## Credits

Created and maintained by [Perwds](https://github.com/Perwds), who wrote Onyx's own code. Many features were inspired by other mods, credited below.

A small number of outside pieces are ported or included, and some libraries ship inside the jar. Each of those is used under its license, with that license kept and the author credited here.

### Inspired by, written from scratch for Onyx

| Project | Author | Idea | License |
|---|---|---|---|
| Spear Effects | RedVortex | Spear effects | MIT |
| A Good Place | enjarai | Block animation | MIT |
| Block Place Particles | | Place particles | CC0 |
| Particle Rain | PigCart | Particle weather | MIT |
| BetterHitreg | jass | Instant hit feedback | Apache 2.0 |
| World Host | Gaming32 | UPnP step for Open To Friends | MIT |
| Ping Equalizer | Ravenclaw | Ping equalizer | MIT |

### Code ported or included

| Project | Author | Used for | License |
|---|---|---|---|
| RTX Remix for Minecraft | NVIDIA | RTX Remix preset (ported to 1.21.11, changed files marked) | Apache 2.0 |
| Customizable Player Models | tom5454 | `.cpmmodel` support: geometry and animation | MIT |
| Shield Statuses, Complete Shield Fixes | Walksy, reiop / hinoob | Shield colours and shield fixes | MIT |
| Lumen Visuals | IkuEatsRamen | World-space menu drawing | MIT |
| authme | Axieum | Microsoft sign-in steps for the account switcher | MIT |
| Apache Commons Math | The Apache Software Foundation | Cubic spline for animations | Apache 2.0 |

### Art and sound

| Project | Author | Used for | License |
|---|---|---|---|
| ImmersiveThunder | netcatgirl | Thunder sounds | MIT |
| Impactful | SirBlAmbo | Impact flash frames | MIT |

### Libraries bundled

| Library | Used for | License |
|---|---|---|
| [Fabric API](https://github.com/FabricMC/fabric) | Mod hooks | Apache 2.0 |
| [TwelveMonkeys ImageIO](https://github.com/haraldk/TwelveMonkeys) | WebP image links | BSD 3-Clause |
| [LWJGL](https://www.lwjgl.org/) NanoVG bindings, [NanoVG](https://github.com/memononen/nanovg) | Smooth menu and HUD drawing | BSD 3-Clause, zlib |
| [JCodec](http://jcodec.org) (includes a port of the JAAD AAC decoder) | Video player | BSD 2-Clause |

### Tools and services

Thanks to [Fabric](https://fabricmc.net/), [Mixin](https://github.com/SpongePowered/Mixin), [Stonecutter](https://stonecutter.kikugie.dev/) and [Blender](https://www.blender.org/), which Onyx is built with, and to these services it can connect to:

- [LRCLIB](https://lrclib.net/) for timed lyrics
- [Modrinth](https://modrinth.com/) and [CurseForge](https://www.curseforge.com/) for the world and pack browsers
- [Firebase](https://firebase.google.com/) for the friends database
- [bore](https://github.com/ekzhang/bore) (bore.pub) for the Open To Friends relay
- [ipify](https://www.ipify.org/) for finding your public address
- MinecraftCapes, OptiFine and LabyMod for other players' capes
- [yt-dlp](https://github.com/yt-dlp/yt-dlp), which you download separately, for video links

## Legal

Onyx is a fan project. It is not affiliated with or endorsed by Mojang, Microsoft or NVIDIA. Minecraft is a trademark of Mojang. All other names belong to their owners.
