# UI Graphic Sector

Unity3d uGUI Custom Graphic that draws an oval sector

<!--![](Images/ Game Image.jpg)-->

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Properties](#properties)
>
> 3 [Methods](#methods)
>
> 4 [Usage](#usage)
>
> 5 [Video Demo](#video-demo)
>
> 6 [See also](#see-also)
>
> 7 [Credits and Donation](#credits-and-donation)
>
> 8 [External links](#external-links)

---------

## Overview

Unity3d uGUI Custom Graphic that draws an oval sector.

### Features

- no custom shaders
- correct input handling
- SpriteBorder support
- 9-slice support
- SpriteAtlas support
- pixelPerUnitMultiplier support
- Anchors for other transforms, including resizing to squeeze content into a sector
- UV-by radius and tile by RectTransform
- free pivot, or generated in the center of the sector
- gradients
- nested sectors can stick to parent
- offset by angle
- pixel offset
- performance-wise

### Known Issues

- automatic navigation not always recognize Selectable in selection wheel, cause it's RectTransforms placed identically. Use explicit navigation instead
- 9-sliced sprites 'shrink' to center, cause uv calculated per-degree
- Tiled mode not support SpriteAtlas, only Single-texture sprites, by design. Cause tiling artifacts through uv repeating, no blowing up geometry as UI.Image.Tiled does.

---------

## Properties

The properties of the Horizontal Scroll Snap control are as follows:

Property | Description
-|-
TBC|TBC

---------

## Methods

Method | Arguments | Description
-|-|-
TBC|TBC|TBC

---------

## Usage

TBC

---------

## Video Demo

[See Source Repository for demonstrations](https://github.com/mitay-walle/com.mitay-walle.ui-graphic-sector?tab=readme-ov-file)

---------

## See also

N/A

---------

## Credits and Donation

Dmitry (mitay-walle)

---------

## External links

[Sourced from](https://github.com/mitay-walle/com.mitay-walle.ui-graphic-sector)
