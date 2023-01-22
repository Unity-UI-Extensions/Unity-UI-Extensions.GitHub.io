# MultiTouch Scroll Rect

==============

Fixed version of the scroll rect to properly handle multiple touches

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

Unity's ScrollRect is behaving erratic when more than one touch is used for drag. It seems to be a bug with the UI system as it jumps between fingers (to moving one). This script fixes it by blocking event data based on touch id.

---------

## Properties

No additional properties, inherits from the original ScrollRect

---------

## Usage

Simply replace the original ScrollRect with the new MultiTouchScrollRect:
Add Component -> UI -> Extensions -> MultiTouchScrollRect

---------

## Video Demo

None, no change to Scroll Rect

---------

## See also

---------

## Credits and Donation

Erdener Gonenc - @PixelEnvision

---------

## External links

[Sourced from](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/3/scrollrectmultitouchfixcs)
