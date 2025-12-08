# BoundToolTip

An alternate Tooltip implementation with central listener

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

A tooltip implementation which uses a manager to control the tooltip appearance, provides a different way to manage multiple tooltips in a scene

---------

## Properties

### Bound Tooltip Item Properties

The properties of the Bound Tooltip Item control are as follows:

Property | Description
|-|-|
*Tooltip Text*|The TextMeshPro text component that will display the tooltip content
*Tool Tip Offset*|Vector3 offset from the trigger position where the tooltip will appear

### Bound Tooltip Trigger Properties

The properties of the Bound Tooltip Trigger control are as follows:

Property | Description
|-|-|
*Text*|The tooltip text to display when this trigger is activated
*Use Mouse Position*|When enabled, tooltip appears at mouse position instead of trigger position
*Offset*|Vector3 offset from the trigger position (used when Use Mouse Position is false)

---------

## Methods

### Bound Tooltip Item Methods

Method | Arguments | Description
-|-|-
*ShowTooltip*|text (string), pos (Vector3)|Displays the tooltip with the specified text at the specified position plus offset
*HideTooltip*|N/A|Hides the tooltip by deactivating the GameObject

### Additional properties available in code

Property | Return Type | Description
|-|-|-|
IsActive|bool|Returns whether the tooltip GameObject is currently active
Instance|BoundTooltipItem|Static singleton instance of the BoundTooltipItem in the scene

---------

## Usage

Add the ToolTip control to your scene using:

"GameObject -> UI -> Extensions -> Bound Tooltip -> Tooltip"

If no tooltip item exists in the scene, one will be created automatically for you.

An additional "Tool Tip Trigger" is also available to activate the tooltip, by adding the relevant component:

"Add Component -> UI -> Extensions -> Bound Tooltip -> Tooltip Trigger"

---------

## Video Demo

"Link to demo video or animated Gifs"

---------

## See also

[ToolTip](/Controls/ToolTip.md)
[HoverToolTip](/Controls/HoverToolTip.md)

---------

## Credits and Donation

Martin Sharkbomb

---------

## External links

[Sourced from](http://www.sharkbombs.com/2015/02/10/tooltips-with-the-new-unity-ui-ugui/)
