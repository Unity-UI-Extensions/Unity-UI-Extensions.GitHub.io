# UI_MagneticInfiniteScroll

An extension of the InfiniteScroll control that adds a hot spot region to anchor child elements when scrolling finishes.

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

The Magnetic Infinite Scroll Rect script causes content items for a Scroll Rect to loop indefinitely as the user scrolls.  When scrolling stops, content is anchored to a defined pivot point

![](Images/MagneticInfiniteScrollInspector.jpg)

It also allows you determine whether the control starts on awake or via code.

---------

## Properties

The properties of the Scroll Rect Infinite component are as follows:

Property | Description
-|-
*Init By User*|Should this activate automatically or only on request.
*Pivot*|The anchor point to stop content at
*Max Speed for Magnetic*|The maximum speed that allows you to activate the magnet to center on the pivot.
*Index Start*|The index of the object which must be initially centered.
*Time For Deceleration*|The time to decelerate and aim to the pivot.

---------

## Methods

Method | Arguments | Description
-|-|-
*SetNewItems*|newItems (List of Transform Items)|Appends a list of items to the Infinite Scroll child list
*SetContentInPivot*|Index|Moves the content to set the selected child in the pivot zone

---------

## Usage

> Requires a configured ScrollRect.  Which will be added by  default.

Simply add the default Scroll Rect Infinite component to a Scroll Rect using:

"Add Component -> UI -> Extensions -> UI Magnetic Infinite Scroll"

---------

## Video Demo

![](Images/MagneticInfiniteScrollDemo.gif)

---------

## See also

* [InfiniteScroll](/Controls/UI_InfiniteScroll.md)
* [Scroll Rect Occlusion](/Controls/UI_ScrollRectOcclusion.md)
* [Scroll Rect Tweener](/Controls/ScrollRectTweener.md)
* [Scroll Rect Linker](/Controls/ScrollRectLinker.md)
* [Scroll Rect Conflict Manager](/Controls/ScrollConflictManager.md)

---------

## Credits and Donation

Credit [Febo Zodiaco](https://bitbucket.org/FeboGamedeveloper/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/349/magnticinfinitescroll](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/349/magnticinfinitescroll)
