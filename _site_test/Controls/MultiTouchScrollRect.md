# MultiTouch Scroll Rect

Fixed version of the scroll rect to properly handle multiple touches

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

Unity's ScrollRect is behaving erratic when more than one touch is used for drag. It seems to be a bug with the UI system as it jumps between fingers (to moving one). This script fixes it by blocking event data based on touch id.

---------

## Properties

No additional properties, inherits from the original ScrollRect

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Simply replace the original ScrollRect with the new MultiTouchScrollRect:

"*Add Component -> UI -> Extensions -> MultiTouchScrollRect*"

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
