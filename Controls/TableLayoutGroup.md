# TableLayoutGroup

==============

A table layout system supporting customizable column and row sizes / layout

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

The table layout group allows the layout of child items in to the style of a table.  You can specify how many columns should be supported as well as the size of columns and rows.
Additionally, you can specify padding between the columns and rows.

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TableLayoutGroup.jpg)

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TableLayoutGroupInspector.jpg)

If you wish you can override the fixed row height to allow child elements to set their height.

This control differs to the built in Unity Grid layout, which can only arrange items dynamically in a grid based on the size of the containing RectTransform.

---------

## Properties

The properties of the Box Slider control are as follows:

Property | Description
--------- | --------------
*Start Corner*|The corner to start adding children from
*Column Widths*|An array of floats to denote the width of each column. Content sized to fit
*Minimum Row Height*|The minimum height of child items in a row
*Flexible Row Height*|Are flexible row heights allowed, or should they be fixed to the minimum
*Column Spacing*|The amount of space between each column
*Row Spacing*|The amount of space between each row
||

*Inherited from built-in layoutGroup*

* Padding (sets the padding inside the RectTransform before drawing children)
* Child Alignment

---------

## Usage

Create an Empty GO on a Canvas and add the **Table Layout Group** component object using "*UI / Extensions / Table Layout Group*" in the Editor Add Component menu.

---------

## Video Demo

*Click to play*

[![Table Layout Group Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TableLayoutGroupDemo.jpg)](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TableLayoutGroupDemo.mp4 "Table Layout Group Demo")

---------

## See also

* Unity (built-in) Grid Layout
* [Curved Layout](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/CurvedLayout)
* [Flow Layout Group](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/FlowLayoutGroup)
* [Radial Layout](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/RadialLayout)

---------

## Credits and Donation

Credit [RahulOfTheRamanEffect](https://forum.unity3d.com/members/judah4.34568/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/36](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/36)
