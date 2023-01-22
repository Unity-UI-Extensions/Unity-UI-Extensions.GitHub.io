# Scroll Rect Tweener

==============

Tweening solution for ScrollRects, adds smoothing automatically

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

The Scroll Rect Tweener is a simple programmatic component that allows you tween from one position on a Scroll Rect to another with a selectable smoothing value

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollRectTweenerInspector.jpg)

---------

## Properties

The properties of the Box Slider control are as follows:

Property | Description
--------- | --------------
*Move Speed*|The default speed that the control moves when Tweening
*Disable Drag While Tweening*|Stops the user from being able to disrupt the tweening motion via touch or pointer
||

The control is mainly used programmatically with the following functions
Function | Arguments | Description
--------- | -------------- | --------------
*ScrollHorizontal*| float (X Value)|X Coordinate to tween to horizontally
*ScrollHorizontal*| float (X Value), float (duration)|X Coordinate to tween to horizontally overriding the default Tween duration
*ScrollVertical*| float (Y Value)|Y Coordinate to tween to vertically
*ScrollVertical*| float (Y Value), float (duration)|Y Coordinate to tween to vertically overriding the default Tween duration
*Scroll*| Vector2 (2D position)|Tween to the provided X / Y coordinates on the Scroll Rect
*Scroll*| Vector2 (2D position), float (duration)|Tween to the provided X / Y coordinates on the Scroll Rect overriding the default Tween duration
||

**Note**
Coordinates are quad based with 0,0 being the bottom left and 1,1 being the top right of the Scroll Rect Area.

---------

## Usage

Simply add the default Scroll Rect Tweener component to a Scroll Rect using "*UI / Extensions / Scroll Rect Tweener*" in the "*Component*" menu.

It is also available as a Game Component menu in "*UI / Extensions / Scroll Rect Tweener*".

---------

## Video Demo

*Click to play*

[![Scroll Rect Tweener  Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollRectTweenerDemo.jpg)](https://youtu.be/1ZNIrdlV9QY?t=5m27s "Scroll Rect Tweener Demo video")

---------

## See also

* [Scroll Rect Infinite](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_InfiniteScroll)
* [Scroll Rect Occlusion](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_ScrollRectOcclusion)
* [Scroll Rect Linker](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollRectLinker)
* [Scroll Rect Conflict Manager](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollConflictManager)

---------

## Credits and Donation

Credit [Martin Sharkbomb ]()

---------

## External links

Sourced from - [http://www.sharkbombs.com/2015/08/26/unity-ui-scrollrect-tools/](http://www.sharkbombs.com/2015/08/26/unity-ui-scrollrect-tools/)
