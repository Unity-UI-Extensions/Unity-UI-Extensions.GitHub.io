# UI Circle Segmented

Custom graphic for uGUI, circle split into segments.

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

Custom graphic for uGUI, circle split into segments.

### Features

- fill floating
- fill per-sprite-segment
- fill per-vertex
- fill Handle (selected segment only)
- fill Handle Inverted (all except selected segment)
- skip offset
- intersecting (overlapping) segments
- sprite round
- rotate offset
- round gradient
- GC-free
- unified width border / outline mode

![UICircleSegmented Inspector](./Images/UICircleSegmented/Inspector_preview.png)
![UICircleSegmented Inspector](./Images/UICircleSegmented/Inspector_preview.png)

---------

## Properties

![UICircleSegmented Inspector](./Images/UICircleSegmented/Inspector_preview.png)

The properties of the UI Circle Segmented control are as follows:

Property | Description
-|-
*Override Sprite*|Sprite Texture to apply.
*Thickness*|The thickness of the line.
*Fill Amount*|Fill / Progress of the line.
*Invert Fill*|If true, the fill approach is inverted/reversed..
*Fill Pattern*|Default, Handle, Handle Inverted. Method for how the fill is processed.
*Fill Deep*|Floating, Per Vertex, Per Segment.  How the fill is processed.
*Global Degree Offset*|Rotation offset for the control.
*Max Degree*|Maximum fill degrees.
*Segments Count*|How many segments to include in the circle.
*Segments Per Sprite Count*|ALters how many segments are included with each section.
*Segments Degree Offset*|Offsets the rotation of each segment.
*Border*|Border thickness per segment.
*Gradient*|Gradient to apply to the control.
*Diagonal Gradient*|Gradient to apply per segment.
*Gradient Degree Offset*|Rotational effect for the gradient.
***On Cull State Changed*** (event)|Event fired when the element changes.

## Inherited from MaskableGraphic

- Material
- Color
- Raycast Target
- Maskable

The properties of the UI Circle Segmented Curve are as follows:

Property | Description
-|-
*Curve*|Curve to apply to the segments of a target UI Circle Segmented control.
*Circle*|The UI Circle Segmented control to target.

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

TBC

---------

## Video Demo

![demo video](./Images/UICircleSegmented/samples_animated.gif)

Handle | Handle Inverted

![Handle](./Images/UICircleSegmented/wheel_select.gif)

Border Mode

![Border](./Images/UICircleSegmented/border%20example.png)

---------

## See also

Some tips are here: [Accordion Type Layout](https://forum.unity.com/threads/accordion-type-layout.271818/#post-7429499) including how to collapse nested child elements so they no longer appear.

---------

## Credits and Donation

ChoMPHi

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/accordion-type-layout.271818/)

---------
