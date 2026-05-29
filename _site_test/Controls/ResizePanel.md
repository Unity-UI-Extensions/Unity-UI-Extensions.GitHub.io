# ResizePanel

A control that allows resizing of a parent panel by dragging a handle, maintaining aspect ratio and respecting min/max size constraints.

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

The ResizePanel control enables users to resize a parent panel by dragging a handle component. It automatically maintains the original aspect ratio and constrains resizing within specified minimum and maximum bounds (calculated as 10% to 1000% of the original size).

---------

## Properties

The properties of the ResizePanel control are as follows:

Property | Description
-|-
*Min Size*|Minimum size constraint for the panel (Vector2). Automatically set to 10% of original dimensions in Awake()
*Max Size*|Maximum size constraint for the panel (Vector2). Automatically set to 1000% of original dimensions in Awake()

---------

## Methods

The ResizePanel control implements Unity's IPointerDownHandler and IDragHandler interfaces but does not expose additional public methods.

Method | Arguments | Description
-|-|-
*OnPointerDown*|PointerEventData|Handles pointer down events to bring panel to front and record starting position
*OnDrag*|PointerEventData|Handles drag events to resize the parent panel while maintaining aspect ratio

---------

## Usage

To use the ResizePanel control:

1. Add the component via "**Add Component -> UI -> Extensions -> RescalePanels -> ResizePanel**"
2. Attach the component to a child GameObject of the panel you want to resize
3. The parent RectTransform will be automatically detected and become resizable
4. Min/Max size constraints are automatically calculated on Awake() as 10% and 1000% of the original panel size

Example code for manual configuration:

```csharp
var resizePanel = resizeHandle.GetComponent<ResizePanel>();
resizePanel.minSize = new Vector2(100, 100);
resizePanel.maxSize = new Vector2(1000, 1000);
```

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [RescalePanel](RescalePanel.md) - Rescales a panel using local scale
* [RescaleDragPanel](RescaleDragPanel.md) - Combines rescaling with drag-to-move functionality

---------

## Credits and Donation

Credits: .entity

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/rescale-panel.309226/)
