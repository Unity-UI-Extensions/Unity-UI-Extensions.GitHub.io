---
layout: control-ugui
title: "UI Horizontal Scroller"
description: "Horizontal scroller with centre-focus zooming that scales items by distance."
category: "Layout"
permalink: /ugui/controls/ui-horizontal-scroller/
has_video: false
tags: [layout, scroll, horizontal, zoom, scale]
---

Horizontal scrolling layout with automatic element scaling based on distance from a center point, focus detection, and optional navigation buttons.

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

The UI Horizontal Scroller arranges child items in a horizontal strip and continuously scales them based on how close they are to a configurable center viewport. The item nearest the center becomes the focused element. The component can optionally disable interaction on unfocused items, stop inertial overscroll at the ends, and wire left/right navigation buttons.

This control is based on the same zoomed-selector pattern as UI Vertical Scroller, but operates on the X axis.

---------

## Properties

The properties of the UI Horizontal Scroller control are as follows:

Property | Description
-|-
*Scroll Rect*|Reference to the target ScrollRect component. Auto-detected from the same GameObject if not assigned.
*Array Of Elements*|Array of GameObjects to populate inside the scroller. If empty, the control uses the ScrollRect content children.
*Center*|RectTransform defining the center display area where the focused element is magnified. Required.
*Element Size*|RectTransform defining the size and spacing of elements. Defaults to Center if not set.
*Element Shrinkage*|Vector2 controlling the falloff of scale by distance using `1 / (1 + distance * shrinkage)`. Default: `(1/200, 1/200)`.
*Min Scale*|Minimum scale applied to the furthest elements. Default: `(0.7, 0.7)`.
*Starting Index*|Index to focus when the control starts. Default: `-1`.
*Stop Momentum On End*|Stops inertia from overscrolling past the first or last element. Default: `true`.
*Disable Unfocused*|Disables interaction on non-focused items by toggling their CanvasGroup interactable state. Default: `true`.
*Scroll Left Button*|Optional button GameObject used to move focus toward earlier items.
*Scroll Right Button*|Optional button GameObject used to move focus toward later items.
***On Button Clicked*** (event)|Inspector event fired when an element Button is clicked. Provides the clicked item index.
***On Focus Changed*** (event)|Inspector event fired when the centered element changes. Provides the focused item index.

Additional properties available in code:

Property | Return Type | Description
-|-|-
FocusedElementIndex | int | Index of the item currently closest to the center.
Center | RectTransform | Gets or sets the center viewport RectTransform.
Result | string | Text content from the focused element's TMP_Text child, if present.
ScrollingPanel | RectTransform | The ScrollRect content panel that is repositioned while scrolling.

---------

## Methods

Method | Arguments | Description
-|-|-
*Awake* | (none) | Resolves the ScrollRect reference and reports a missing Center setup.
*Start* | (none) | Wires optional navigation buttons and initializes the child collection.
*UpdateChildren* | `int startingIndex = -1, GameObject[] arrayOfElements = null` | Rebuilds the element list, resizes each child to match Element Size, and optionally snaps to a starting element.
*SnapToElement* | `int element` | Instantly repositions the scroller so the specified element becomes centered.
*ScrollLeft* | (none) | Moves the content left by approximately one item step.
*ScrollRight* | (none) | Moves the content right by approximately one item step.

---------

## Usage

To use the UI Horizontal Scroller control:

1. Add the component via "Add Component -> Layout -> Extensions -> Horizontal Scroller".
2. Ensure the GameObject also has a ScrollRect component.
3. Assign the *Center* RectTransform for the focus viewport.
4. Optionally assign *Element Size* if the layout spacing should differ from the center viewport size.
5. Populate *Array Of Elements* or allow the control to read the ScrollRect content children.
6. Ensure each element has a Button component and a CanvasGroup component.
7. Optionally assign left and right navigation buttons.
8. Configure the scaling behavior with *Element Shrinkage* and *Min Scale*.
9. Hook the inspector events if you need click or focus change callbacks.

Example code for programmatic setup:

```csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UI.Extensions;

public class HorizontalScrollerExample : MonoBehaviour
{
    [SerializeField] private UIHorizontalScroller scroller;
    [SerializeField] private RectTransform center;
    [SerializeField] private RectTransform elementSize;
    [SerializeField] private ScrollRect scrollRect;
    [SerializeField] private GameObject[] items;

    private void Start()
    {
        scroller.Center = center;
        scroller.UpdateChildren(0, items);
        scroller.SnapToElement(0);
    }

    public void FocusLastItem()
    {
        scroller.SnapToElement(items.Length - 1);
    }
}
```

> [!NOTE]
>
> - The control expects each scroller item to contain a Button and CanvasGroup.
> - Focus detection reads `TMP_Text` from the focused item to populate `Result`.
> - `On Button Clicked` and `On Focus Changed` are serialized inspector events, not public C# events.

---------

## Video Demo

No dedicated demo media is published yet.

---------

## See also

* [UIVerticalScroller](UIVerticalScroller.md) - Vertical variant of the same zoomed-selector pattern
* [HorizontalScrollSnap](HorizontalScrollSnap.md) - Horizontal snap paging control
* [VerticalScrollSnap](VerticalScrollSnap.md) - Vertical snap paging control

---------

## Credits and Donation

Credits: Ahmad S. Al-Faqeeh  
Based on UI Vertical Scroller by Mrs. YakaYocha

---------

## External links

* [Source issue](https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues/205)
* [UI Vertical Scroller source inspiration](https://www.youtube.com/channel/UCHp8LZ_0-iCvl-5pjHATsgw)