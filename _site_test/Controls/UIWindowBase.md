# UIWindowBase

A draggable window for RectTransforms with bounds checking to keep it within the canvas

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

A draggable window implementation for RectTransforms that includes bounds checking to ensure the window stays within the canvas area.

---------

## Properties

The properties of the UI Window Base control are as follows:

Property | Description
-|-
*Keep Window In Canvas*|Number of pixels of the window that must stay inside the canvas view
*Root Transform*|The transform that is moved when dragging, can be left empty in which case its own transform is used

### Additional properties available in code

Property | Return Type | Description
|-|-|-|
ResetCoords|bool (static)|Set to true to reset the window to its original position

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Add the UI Window Base component to a RectTransform using:

"Add Component -> UI -> Extensions -> UI Window Base"

Or alternatively, add it via the GameObject menu:

"GameObject -> UI -> Extensions -> Controls -> UI Window Base"

---------

## Video Demo

N/A

---------

## See also

N/A

---------

## Credits and Donation

GXMark, alexzzzz, CaoMengde777, TroyDavis

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/scripts-useful-4-6-scripts-collection.264161/page-2#post-1834806)
