# Scroll Conflict Manager

==============

Resolves dragging issues with nested Scroll Rect's

---------

## Contents

> 1 [Overview](#markdown-header-overview)

> 2 [Properties](#markdown-header-properties)

> 3 [Methods](#markdown-header-methods)

> 4 [Usage](#markdown-header-usage)

> 5 [Demo](#markdown-header-demo)

> 6 [See also](#markdown-header-see-also)

> 7 [Credits and Donation](#markdown-header-credits-and-donation)

> 8 [External links](#markdown-header-external-links)

---------

## Overview

The Scroll Conflict Manager solves the dragging issue with child Scroll Rect's. Natively, nested Scroll Rect's will only allow scrolling in the direction of a child Scroll Rect.
This component solves this problem allowing free movement, locked to the initial direction of the drag.

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollRectConflictManagerInspector.jpg)

---------

## Properties

The properties of the ScrollrectConflictManager control are as follows:

Property | Description
--------- | --------------
*Parent Scroll Rect*|The Rect Transform of the parent Scroll Rect
||

---------

## Methods

Method | Arguments | Description
--- | --- | ---
*SetParentScrollRect*|ScrollRect|Resets the parent scroll rect for the manager and re-initializes the dependencies
||

---------

## Usage

Simply add the default Scroll Rect Conflict Manager component to an existing Scroll Rect using "*UI / Extensions / Scrollrect Conflict Manager*" in the "*Component*" menu, then assign the parent Scroll Rect to the control.

It is also available as a Game Component menu in "*UI / Extensions / Scrollrect Conflict Manager*".

---------

## Video Demo

*Click to play*

[![Scroll Rect Conflict Manager Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ScrollRectConflictManagerDemo.jpg)](https://youtu.be/1ZNIrdlV9QY?t=9m19s "Scroll Rect Conflict Manager Demo")

---------

## See also

* [Scroll Rect Infinite](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_InfiniteScroll)
* [Scroll Rect Magnetic Infinite](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_MagneticInfiniteScroll)
* [Scroll Rect Occlusion](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UI_ScrollRectOcclusion)
* [Scroll Rect Tweener](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollRectTweener)
* [Scroll Rect Linker](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ScrollRectLinker)

---------

## Credits and Donation

Credit [srinivas sunil ]()

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/21/develop_53/diff](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/21/develop_53/diff)
