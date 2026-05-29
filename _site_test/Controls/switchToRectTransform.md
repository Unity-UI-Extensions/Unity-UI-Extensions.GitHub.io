# SwitchToRectTransform

RectTransform extension method to move one RectTransform to another

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

A programmatic extension that enables you, through code to move a RectTransform from one point on a screen to another point on the screen using a target RectTransform.  This aligns all the Anchors, Pivots and offsets of the Target RectTransform.

---------

## Properties

This is a static extension method; there are no inspector properties.

---------

## Methods

Method | Arguments | Description
-|-|-
*switchToRectTransform*|RectTransform source, RectTransform target|Moves `source` to match anchors/pivots/offsets of `target` in screen space.

---------

## Usage

Using this utility through code is very simply, just call:

```csharp
sourceRectTransform.switchToRectTransform(targetRectTransform);
```

And the Source (from) Rect Transform will be moved to mimic the Target (to) RectTransform position.

---------

## Video Demo

N/A

---------

## See also

N/A

---------

## Credits and Donation

* Izitmee
* Brave Michael

---------

## External links

* Izitmee - [http://forum.unity3d.com/threads/find-anchoredposition-of-a-recttransform-relative-to-another-recttransform](http://forum.unity3d.com/threads/find-anchoredposition-of-a-recttransform-relative-to-another-recttransform.330560/#post-2300992)
* Brave Michael - [http://forum.unity3d.com/threads/find-anchoredposition-of-a-recttransform-relative-to-another-recttransform](http://forum.unity3d.com/threads/find-anchoredposition-of-a-recttransform-relative-to-another-recttransform.330560/#post-2300992)