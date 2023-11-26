# CurvedLayout

A curved layout system

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

Similar to the Horizontal and Vertical Layout components provided by Unity, this offers more control both vertically and horizontally with the ability to curve or bend the layout.

---------

## Properties

The properties of the Box Slider control are as follows:

Property | Description
|-|-|
|||
*Curve Alignment*|Based on which anchor should the curve apply.
*Curve Offset*|Vector 3 offset to apply to the curve.
*Item Axis*|The axis along which to place the items, Normalized before use.
*Item Size*|The size of each item along the Normalized axis.
*Center Point*|The slope can be moved by altering this setting, it could be constrained to the 0-1 range, but other values are useful for animations.

---------

## Usage

Like with other Layout controls, simply add this to the parent RectTransform for a collection of child elements through the Add Component menu as follows:
Add Component -> Layout -> Extensions -> Curved Layout.

> Make sure to configure the Item Size, Offset and Axis to apply a curve, else child items will just collate.

---------

## Video Demo

tbc

---------

## See also

* [Radial Layout Group](/Controls/RadialLayout.md)
* [Table Layout Group](/Controls/TableLayoutGroup.md)
* [Flow Layout Group](/Controls/FlowLayoutGroup.md)

---------

## Credits and Donation

Freezy

---------

## External links

[Sourced From](http://forum.unity3d.com/threads/curved-layout.403985/)
