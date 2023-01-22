# Vertical Scroll Snap

==============

A paged scroll rect that can work in steps / pages, includes button support.  Now also supports infinite scrolling.

---------

## Contents

> 1 [Overview](#markdown-header-overview)

> 2 [Properties](#markdown-header-properties)

> 3 [Usage](#markdown-header-usage)

> 4 [Video Demo](#markdown-header-video-demo)

> 5 [See also](#markdown-header-see-also)

> 6 [Credits and Donation](#markdown-header-credits-and-donation)

> 7 [External links](#markdown-header-external-links)

---------

## Overview

A scroll snap style control which is focused on a Vertical layout, enabling a paged view of child elements.
Pages can be moved by keys, swipes or via the use of buttons.

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/VSSInspector.jpg)

Now also supports infinite scrolling and additional events for when pages change.

As of Update 1.6, now also supports Scrollbars, *Note* Can only use the Vertical scrollbar in alignment with the direction of the ScrollSnap

---------

## Properties

The properties of the Vertical Scroll Snap control are as follows:

Property | Description
--------- | --------------
*Starting Screen*|The child page that should be displayed on start. Bound to the limits of either the scene child objects or the "Child Objects" array.
*Page Step*|The distance between pages based on the current width of the control.  Higher value equals more spacing.
*Pagination*|The GameObject with a Toggle group that controls toggles active state. Recommended one toggle per-page.
*Next Button*|Button to instruct the control to move to the next page.
*Prev Button*|Button to instruct the control to move to the previous page.
*Transition Speed*|Speed at which the control lerps between pages
*Use Fast Swipe*|When enabled, a swipe only moves to the next page (unless below Fast Swipe Threshold. E.G. slow swipe / drag)
*Fast Swipe Threshold*|An offset height the user must swipe to go to the next / prev page based on the panel height.  Swipe more than the Height + Threshold and the control reverts to normal swipe behaviour
*Swipe Velocity Threshold*|Slowest speed the control must travel at to settle on a page.
*Mask Area*|Maskable area for control, pages outside this area will be made inactive. Used in conjunction with the Mask Buffer.  Recommended to also add a RectMask2D to MaskArea GO.
*Mask Buffer*|The amount of page buffer to surround the Mask Area and control which pages are active / inactive. Lower value equals more active pages.
*Jump On Enable*|By default the container will lerp to the start when enabled in the scene, this option overrides this and forces it to simply jump without lerping
*Restart On Enable*|By default the container will return to the original starting page when enabled, this option overrides this behaviour and stays on the current selection
*Use Parent Transform*|When using prefabs in the ChildObjects array, the control with use the prefab transform values instead of resetting to the parent.
*Child Objects*|An array of prefabs to load the control with. Can EITHER add children in to the scene or via this array but NOT both.
*On Selection Change Start* (event) |The Event fired when the user starts changing the page via swipe or mouse
*On Selection Page Changed* (event) |The Event fired when the current page changes, either via swipe, mouse, Next/Prev Buttons
*On Selection Change End* (event) |The Event fired when the page settles after being changed by swipe or mouse
||

Additional properties available in code:

Property | Return Type | Description
---|---|---
CurrentPage|int|The current snapped page, or selected page as the user swipes
|||

---------

## Usage

Like with other Layout controls, simply add this to the parent RectTransform for a collection of child elements through the Add Component menu as follows:

* "Add Component -> Layout -> Extensions -> VerticalScrollSnap*"

Or alternatively, add the default layout for the control using:

* "*GameObject -> UI -> Extensions -> Vertical Scroll Snap*"

This will give you a standard Scroll Rect setup with the script and a single child example page.

To get access to the Current or snapped page in code, use the **CurrentPage** property details above.  This is also updated as the user swipes.  If you wish to update linked content based on the current page, I recommend using the **OnSelectionPageChanged** event, e.g.

```csharp
    public VerticalScrollSnap vss;

    // Start is called before the first frame update
    void Start()
    {
        vss = GetComponent<VerticalScrollSnap>();
    }

    // Update is called once per frame
    void Update()
    {
        //Checking for the Currentpage
        var theSelectedPageIs = vss.CurrentPage;
    }
```

---------

## Video Demo

The main Vertical / Horizontal demo

[![View Intro Video](http://img.youtube.com/vi/LnKy3_ymEXs/0.jpg)](http://www.youtube.com/watch?v=LnKy3_ymEXs "HSS/VSS walk-through video")

A simple walk-through setting up the Scroll Snap with a perspective view

[![Scroll Snap Perspective View Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollSnapPerspectiveDemo.jpg)](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollSnapPerspectiveDemo.mp4 "Scroll Snap Perspective View Demo")

---------

## See also

* [ContentScrollSnapHorizontal](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ContentScrollSnapHorizontal)
* [HorizontalScrollSnap](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/HorizontalScrollSnap)
* [ScrollSnap](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollSnap)

---------

## Credits and Donation

BinaryX, SimonDarksideJ

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/scripts-useful-4-6-scripts-collection.264161/page-2#post-1945602)
