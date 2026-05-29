# RescalePanel

A control that rescales a parent panel by dragging a handle, adjusting the local scale while keeping the UI element size consistent.

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

The RescalePanel control allows users to rescale a parent panel by dragging a handle. Unlike ResizePanel, this control modifies the parent's local scale rather than its size delta, and automatically adjusts the handle's size delta to maintain visual consistency during scaling.

---------

## Properties

The properties of the RescalePanel control are as follows:

Property | Description
-|-
*Min Size*|Minimum scale constraint for the panel (Vector2). Defines the minimum local scale values for X and Y axes
*Max Size*|Maximum scale constraint for the panel (Vector2). Defines the maximum local scale values for X and Y axes

---------

## Methods

The RescalePanel control implements Unity's IPointerDownHandler and IDragHandler interfaces but does not expose additional public methods.

Method | Arguments | Description
-|-|-
*OnPointerDown*|PointerEventData|Handles pointer down events to bring panel to front and record starting position
*OnDrag*|PointerEventData|Handles drag events to rescale the parent panel by adjusting local scale and compensating handle size

---------

## Usage

To use the RescalePanel control:

1. Add the component via "**Add Component -> UI -> Extensions -> RescalePanels -> RescalePanel**"
2. Attach the component to a child GameObject of the panel you want to rescale
3. The parent Transform will be automatically detected and become rescalable via local scale
4. Configure min/max size constraints in the inspector to limit scaling range

Example code for setting scale constraints:

```csharp
var rescalePanel = rescaleHandle.GetComponent<RescalePanel>();
rescalePanel.minSize = new Vector2(0.5f, 0.5f);  // Minimum 50% scale
rescalePanel.maxSize = new Vector2(3.0f, 3.0f);  // Maximum 300% scale
```

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [ResizePanel](ResizePanel.md) - Resizes a panel by changing sizeDelta
* [RescaleDragPanel](RescaleDragPanel.md) - Combines rescaling with drag-to-move functionality

---------

## Credits and Donation

Credits: .entity

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/rescale-panel.309226/)
