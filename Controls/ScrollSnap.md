# ScrollSnap

An alternate scroll snap control supporting both Horizontal and Vertical layouts in one control

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

A scroll snap style control which works with both a horizontal and vertical layout, enabling a paged view of child elements.
Pages can be moved by keys, swipes or via the use of buttons.

*Note, should not be used in conjunction with scroll bars as this throws off the view.

---------

## Properties

The properties of the Horizontal Scroll Snap control are as follows:

Property | Description
|-|-|
*Next Button*|Optional button to move the ScrollSnap forward.
*Prev Button*|Optional button to move the ScrollSnap backward.
*Items Visible at once*|How many items should be visible at the same time.
*Auto Layout Items*|Should the ScrollSnap contents be automatically aligned, or left untouched.
*Link Scrollbar Steps*|Use the base ScrollRect steps configuration for the ScrollSnap.
*Link Scrollbar Scroll Sensitivity*|Use the base ScrollRect scroll sensitivity configuration for the ScrollSnap.
*Use Fast Swipe*|Should "Fast Swipe" be used to progress pages.
*Fast Swipe Threshold*|The speed of the ScrollSnap is moving before a "Fast Swipe" motion is detected.
*Direction*|The direction the ScrollSnap flows in, Horizontal or Vertical.
***On Page Change*** (event) |The Event fired when the current page changes, either via swipe, mouse, Next/Prev Buttons

---------

## Methods

Method | Arguments | Description
|-|-|-|
*ChangePage*|Index (int)|Move the ScrollSNap to a specific page (0 indexed)
*CurrentPage*|None|Returns the Current Page selected for the ScrollSnap
*NextScreen*|None|Forces the control to move to the "Next" page
*PreviousScreen*|None|Forces the control to move to the "Previous" page
*ResetPage*|None|Resets the currently selected page to the starting page, usually page 0
*SetLerp*|value (bool)|Enable or disable smooth Lerp movement

---------

## Usage

Like with other Layout controls, simply add this to the parent RectTransform for a collection of child elements through the Add Component menu as follows:
Add Component -> Layout -> Extensions -> ScrollSnap

Or alternatively, add one of the default layouts for the control using:

* GameObject -> UI -> Extensions -> Fixed Item Scroll -> Snap Vertical Single Item
* GameObject -> UI -> Extensions -> Fixed Item Scroll -> Snap Vertical Multiple Items
* GameObject -> UI -> Extensions -> Fixed Item Scroll -> Snap Horizontal Single Item
* GameObject -> UI -> Extensions -> Fixed Item Scroll -> Snap Horizontal Multiple Items

---------

## Video Demo

[tutorial video](https://www.youtube.com/watch?v=KJlIlWHlfMo)

---------

## See also

* [ContentScrollSnapHorizontal](/Controls/ContentScrollSnapHorizontal.md)
* [HorizontalScrollSnap](/Controls/HorizontalScrollSnap.md)
* [VerticalScrollSnap](/Controls/VerticalScrollSnap.md)

---------

## Credits and Donation

BinaryX, xesenix

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/scripts-useful-4-6-scripts-collection.264161/page-2#post-1945602)
