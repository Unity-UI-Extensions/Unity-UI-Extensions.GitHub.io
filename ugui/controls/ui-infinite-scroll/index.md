---
layout: control-ugui
title: "UI Infinite Scroll"
description: "Loops ScrollRect content indefinitely in horizontal or vertical mode."
category: "Utilities"
permalink: /ugui/controls/ui-infinite-scroll/
has_video: true
tags: [utilities, scroll, infinite, loop, scrollrect]
---
# UI_InfiniteScroll

Loops Scroll Rect content indefinitely
Configures automatically - works in both vertical and horizontal (but not both at the same time) - drag and drop  - can be initialized by code

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

The Infinite Scroll Rect script causes content items for a Scroll Rect to loop indefinitely as the user scrolls.

![](/ugui/images/InfiniteScrollInspector.jpg)

It also allows you determine whether the control starts on awake or via code.

---------

## Properties

The properties of the Scroll Rect Infinite component are as follows:

Property | Description
-|-
*Init By User*|Should this activate automatically or only on request.

---------

## Methods

Method | Arguments | Description
-|-|-
*SetNewItems*|newItems (List of Transform Items)|Appends a list of items to the Infinite Scroll child list

---------

## Usage

> Requires a configured ScrollRect.  Which will be added by  default.

Simply add the default Scroll Rect Infinite component to a Scroll Rect using:

"Add Component -> UI -> Extensions -> UI Infinite Scroll"

---------

## Video Demo

[![Infinite Scroll Demo](http://img.youtube.com/vi/uVTV7Udx78k/0.jpg)](http://www.youtube.com/watch?v=uVTV7Udx78k "Infinite Scroll Demo video")

---------

## See also

* [Magnetic infinite Scroll](/ugui/controls/ui-magnetic-infinite-scroll/)
* [Scroll Rect Occlusion](/ugui/controls/ui-scroll-rect-occlusion/)
* [Scroll Rect Tweener](/ugui/controls/scroll-rect-tweener/)
* [Scroll Rect Linker](/ugui/controls/scroll-rect-linker/)
* [Scroll Rect Conflict Manager](/ugui/controls/scroll-conflict-manager/)

---------

## Credits and Donation

Credit [Tomasz Schelenz](https://bitbucket.org/TomekSzelki/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/81/infinite-scrollrect](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/81/infinite-scrollrect)
