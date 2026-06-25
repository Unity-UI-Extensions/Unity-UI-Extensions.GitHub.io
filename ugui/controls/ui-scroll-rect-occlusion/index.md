---
layout: control-ugui
title: "UI Scroll Rect Occlusion"
description: "Disables off-screen children in a ScrollRect to reduce overdraw cost."
category: "Utilities"
permalink: /ugui/controls/ui-scroll-rect-occlusion/
has_video: false
tags: [utilities, scroll, occlusion, performance, visibility]
---
# UI_ScrollRectOcclusion

Disables the objects outside of the scrollrect viewport. Useful for scrolls with lots of content

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

The Scroll Rect occlusion script enables and disables Content child items that are outside the visible area of the Scroll Rect.

![](/ugui/images/ScrollRectOcclusionInspector.jpg)

It allows you determine whether it starts on awake or via code.

---------

## Properties

The properties of the Scroll Rect Occlusion component are as follows:

Property | Description
-|-
*Init By User*|Should this occlude automatically or only on request.

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Simply add the default Scroll Rect Occlusion component to a Scroll Rect using:

"Add Component -> UI -> Extensions -> UI Scrollrect Occlusion"

---------

## Video Demo

[![Scroll Rect Occlusion Demo](http://img.youtube.com/vi/uVTV7Udx78k/0.jpg)](http://www.youtube.com/watch?v=uVTV7Udx78k?t=39s "Scroll Rect Occlusion Demo video")

---------

## See also

* [Scroll Rect Infinite](/ugui/controls/ui-infinite-scroll/)
* [Scroll Rect Tweener](/ugui/controls/scroll-rect-tweener/)
* [Scroll Rect Linker](/ugui/controls/scroll-rect-linker/)
* [Scroll Rect Conflict Manager](/ugui/controls/scroll-conflict-manager/)

---------

## Credits and Donation

Credit [Tomasz Schelenz](https://bitbucket.org/TomekSzelki/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/82/scrollrectocclusion](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/82/scrollrectocclusion)
