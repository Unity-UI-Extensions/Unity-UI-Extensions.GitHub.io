# UIScrollToSelection

Automatically scrolls a ScrollRect to the currently selected UI element

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

A ScrollRect enhancement that automatically scrolls to the currently selected UI element, useful for keyboard/gamepad navigation.

---------

## Properties

The properties of the UIScrollToSelection control are as follows:

Property | Description
-|-
*Viewport Rect Transform*|View (boundaries/mask) rect transform. Used to check if automatic scroll to selection is required
*Target Scroll Rect*|Scroll rect used to reach selected element
*Scroll Axes*|Allow automatic scrolling only on these axes
*Used Scroll Method*|MOVE_TOWARDS: stiff movement, LERP: smoothed out movement
*Scroll Speed*|Speed at which the scroll rect moves to the selected element
*End Of List Jump Scroll Speed*|Scroll speed used when element to select is out of "JumpOffsetThreshold" range
*Jump Offset Threshold*|If next element to scroll to is located over this screen percentage, use "EndOfListJumpScrollSpeed" to reach this element faster
*Cancel Scroll Mouse Buttons*|Mouse buttons that cancel the automatic scrolling
*Cancel Scroll Keys*|Keyboard keys that cancel the automatic scrolling

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Simply add the component to a ScrollRect using:

"Add Component -> UI -> Extensions -> UIScrollToSelection"

---------

## Video Demo

N/A

---------

## See also

* [UIScrollToSelectionXY](/Controls/UIScrollToSelectionXY.md)

---------

## Credits and Donation

zero3growlithe

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/scripts-useful-4-6-scripts-collection.264161/page-2#post-2011648)
