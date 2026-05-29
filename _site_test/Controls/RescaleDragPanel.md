# RescaleDragPanel

A control that enables dragging a rescaled panel to reposition it within a canvas, compensating for the panel's local scale during movement.

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

The RescaleDragPanel control allows users to drag and reposition a panel that may have been rescaled. It automatically accounts for the parent's local scale when calculating drag offsets, ensuring accurate positioning. The panel is constrained to remain within the canvas boundaries during dragging.

---------

## Properties

The RescaleDragPanel control has no serialized properties exposed in the inspector. All functionality is handled internally through automatic canvas and parent detection.

---------

## Methods

The RescaleDragPanel control implements Unity's IPointerDownHandler and IDragHandler interfaces but does not expose additional public methods.

Method | Arguments | Description
-|-|-
*OnPointerDown*|PointerEventData|Handles pointer down events to bring panel to front and calculate initial pointer offset
*OnDrag*|PointerEventData|Handles drag events to reposition the panel, accounting for local scale and clamping to canvas bounds
*ClampToWindow*|PointerEventData|Internal method that clamps the pointer position to canvas boundaries

---------

## Usage

To use the RescaleDragPanel control:

1. Add the component via "**Add Component -> UI -> Extensions -> RescalePanels -> RescaleDragPanel**"
2. Attach the component to a child GameObject of the panel you want to make draggable
3. The parent RectTransform and parent Canvas will be automatically detected
4. Drag the handle to move the panel; it will automatically stay within canvas bounds
5. The control compensates for any local scale applied to the parent, ensuring accurate drag behavior

This control works best when combined with RescalePanel to provide both rescaling and repositioning functionality.

Example setup:

```csharp
// Typically no code configuration needed - add component and it works automatically
// The control self-configures in Awake() by detecting the parent Canvas and RectTransform
```

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [ResizePanel](ResizePanel.md) - Resizes a panel by changing sizeDelta
* [RescalePanel](RescalePanel.md) - Rescales a panel using local scale

---------

## Credits and Donation

Credits: .entity

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/rescale-panel.309226/)
