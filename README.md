# Onyx PvP

A Fabric client mod for Minecraft PvP, focused on visuals, menus and replay tools. It's client-side and has about 38,000 lines of Java.

The full source is private. This repo describes the project and includes two of its shaders.

## Features

- **Custom skies:** skies such as Deep Space, Black Hole and Aurora Night that turn with your camera, with far terrain faded into the sky so there's no fog seam.
- **Combat visuals:** jump circles, target rings, hit markers, light trails, hand glow and explosion effects.
- **Shaders:** 33 block and item shader presets with a custom effect editor.
- **3D menus:** a custom title screen and menus using models made in Blender, plus a floating in-game menu.
- **Replay tools:** clip recording, a replay editor with a timeline, and analysis of item switches, reach and CPS.
- **Watch Together:** shared video links that play in sync, on a screen in the world.
- **Spotify lyrics:** lyrics shown as text in the world, with 10 fonts and 9 animations.
- **Item borders:** coloured borders for items and rarities in inventories and the hotbar.

## How it's built

- One codebase builds for Minecraft 1.21.11, 26.1.2, 26.2 and 26.3 using [Stonecutter](https://stonecutter.kikugie.dev/).
- It hooks into the game with Fabric Mixins, and an in-game test script runner checks releases.
- 3D menu models are made in Blender with baked ambient occlusion and loaded through a custom mesh format.

## Shader samples

- [`samples/sky.fsh`](samples/sky.fsh) draws the custom skies. It looks up each pixel by view direction, using camera data packed into a small texture.
- [`samples/painted.fsh`](samples/painted.fsh) is the post-processing pass behind the Painted World filter.
