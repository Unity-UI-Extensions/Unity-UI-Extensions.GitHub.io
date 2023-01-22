# SelectionBox

==============

An RTS style selection box control

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

A selection box control to enable selecting 2D and 3D content within a Canvas / selectable area

![Selection Box Inspector](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/SelectionBoxInspector.jpg)

---------

## Properties

The properties of the Selectable Scalar control are as follows:

Property | Description
--------- | --------------
*Color*|The color to apply to the selectable.
*Art*|The texture to draw as the background to the selectable area.
*Selection Mask*|The Rect Transform for the area that allows items to be selectable, restricts object being selected.
||

---------

## Usage

Add the Selection Box component to a Canvas element and then define a separate Rect Transform to specify the area of the screen that should be selectable.
Once setup, any objects that are contained within the Selection mask will be selectable.

Additionally, you can customize the graphic used for the "Selection Box" that is drawn using the Art property.

---------

## Video Demo

![Selection Box Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/SelectionBoxDemo.gif)

---------

## See also

N/A

---------

## Credits and Donation

* Korindian
* BenZed

---------

## External links

N/A
