---
layout: control-ugui
title: "Scroll Conflict Manager"
description: "Resolves scroll direction conflicts when nested ScrollRects overlap."
category: "Utilities"
permalink: /ugui/controls/scroll-conflict-manager/
has_video: false
tags: [utilities, scroll, conflict, nested, scrollrect]
---
# Scroll Conflict Manager

Resolves dragging issues with nested Scroll Rect's

<!--![](/ugui/images/ Game Image.jpg)-->

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

The Scroll Conflict Manager solves the dragging issue with child Scroll Rect's. Natively, nested Scroll Rect's will only allow scrolling in the direction of a child Scroll Rect.
This component solves this problem allowing free movement, locked to the initial direction of the drag.

![](/ugui/images/ScrollRectConflictManagerInspector.jpg)

---------

## Properties

The properties of the ScrollrectConflictManager control are as follows:

Property | Description
-|-
*Parent Scroll Rect*|The Rect Transform of the parent Scroll Rect

---------

## Methods

Method | Arguments | Description
-|-|-
*SetParentScrollRect*|ScrollRect|Resets the parent scroll rect for the manager and re-initializes the dependencies

---------

## Usage

Simply add the default Scroll Rect Conflict Manager component to an existing Scroll Rect using:

"Add Component -> UI -> Extensions -> Scrollrect Conflict Manager"

Then assign the parent Scroll Rect to the control.

---------

## Video Demo

[![Scroll Rect Conflict Manager Demo](/ugui/images/ScrollRectConflictManagerDemo.jpg)](https://youtu.be/1ZNIrdlV9QY?t=9m19s "Scroll Rect Conflict Manager Demo")

---------

## See also

* [Scroll Rect Infinite](/ugui/controls/ui-infinite-scroll/)
* [Scroll Rect Magnetic Infinite](/ugui/controls/ui-magnetic-infinite-scroll/)
* [Scroll Rect Occlusion](/ugui/controls/ui-scroll-rect-occlusion/)
* [Scroll Rect Tweener](/ugui/controls/scroll-rect-tweener/)
* [Scroll Rect Linker](/ugui/controls/scroll-rect-linker/)

---------

## Credits and Donation

Credit [srinivas sunil ]()

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/21/develop_53/diff](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/21/develop_53/diff)
