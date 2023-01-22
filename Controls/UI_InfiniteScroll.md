# UI_InfiniteScroll

==============

Loops Scroll Rect content indefinitely
Configures automatically - works in both vertical and horizontal (but not both at the same time) - drag and drop  - can be initialized by code

Contents

---------

> 1 [Overview](#markdown-header-overview)

> 2 [Properties](#markdown-header-properties)

> 3 [Methods](#markdown-header-methods)

> 4 [Usage](#markdown-header-usage)

> 5 [Video Demo](#markdown-header-video-demo)

> 6 [See also](#markdown-header-see-also)

> 7 [Credits and Donation](#markdown-header-credits-and-donation)

> 8 [External links](#markdown-header-external-links)

---------

## Overview

The Infinite Scroll Rect script causes content items for a Scroll Rect to loop indefinitely as the user scrolls.

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/InfiniteScrollInspector.jpg)

It also allows you determine whether the control starts on awake or via code.

---------

## Properties

The properties of the Scroll Rect Infinite component are as follows:

Property | Description
--------- | --------------
*Init By User*|Should this activate automatically or only on request.
||

---------

## Methods

Method | Arguments | Description
--- | --- | ---
*SetNewItems*|newItems (List of Transform Items)|Appends a list of items to the Infinite Scroll child list
||

---------

## Usage

> Requires a configured ScrollRect.  Which will be added by  default.

Simply add the default Scroll Rect Infinite component to a Scroll Rect using "*UI / Extensions / UI Infinite Scroll*" in the "*Component*" menu.

---------

## Video Demo

*Click to play*

[![Infinite Scroll Demo](http://img.youtube.com/vi/uVTV7Udx78k/0.jpg)](http://www.youtube.com/watch?v=uVTV7Udx78k "Infinite Scroll Demo video")

---------

## See also

* [Magnetic infinite Scroll](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_MagneticInfiniteScroll)
* [Scroll Rect Occlusion](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_ScrollRectOcclusion)
* [Scroll Rect Tweener](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollRectTweener)
* [Scroll Rect Linker](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollRectLinker)
* [Scroll Rect Conflict Manager](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollConflictManager)

---------

## Credits and Donation

Credit [Tomasz Schelenz](https://bitbucket.org/TomekSzelki/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/81/infinite-scrollrect](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/81/infinite-scrollrect)
