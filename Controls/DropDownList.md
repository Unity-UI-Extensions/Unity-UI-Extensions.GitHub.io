# DropDownList

==============

A basic drop down list with text and image support

---------

## Contents

> 1 [Overview](#markdown-header-overview)
>
> 2 [Properties](#markdown-header-properties)
>
> 3 [Usage](#markdown-header-usage)
>
> 4 [Video Demo](#markdown-header-video-demo)
>
> 5 [See also](#markdown-header-see-also)
>
> 6 [Credits and Donation](#markdown-header-credits-and-donation)
>
> 7 [External links](#markdown-header-external-links)

---------

## Overview

A more advanced Combobox control with additional support for images and other items in the selection pane

![Drop Down List Inspector](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/DropDownListInspector.jpg)

---------

## Properties

The properties of the Box Slider control are as follows:

Property | Description
--------- | --------------
*Disabled Text Color*|Color of the Autocomplete field when the control is disabled
*Available Options*|Array of child options options for the dropdown/selection. Each child is configured within the array below:
-*Caption*|Text for the Child item
-*Image*|Image displayed next to child item
-*Is Disabled*|Is this child item disabled by default
-*Id*|Unique identity of the drop down item
*Scroll Bar Width*|The width of the scrollbar when displayed
*Items To Display*|Number of child items to display when opened. *Note default 0 shows NO items.
*Select First Item On Start*|Should the first item be auto selected on start
*On Selection Changed* (event) |The Event fired when the user selects an option or loses focus
||

> When managing the control programmatically, make sure you use the following functions to manage the ComboBox contents. **Do NOT update the 'AvailableOptions' list directly**

---------

## Methods

Method | Arguments | Description
--- | --- | ---
*AddItem*|DropDownListItem|Adds a new item to the drop down list and rebuilds the display
*AddItem*|String|Adds a new item to the drop down list and rebuilds the display
*AddItem*|Sprite|Adds a new item to the drop down list and rebuilds the display
*RemoveItem*|DropDownListItem|Removes an item from the drop down list and rebuilds the display
*RemoveItem*|String|Removes an item from the drop down list and rebuilds the display
*RemoveItem*|Sprite|Removes an item from the drop down list and rebuilds the display
*RefreshItems*|Array of supported items (DropDownListItem, String or Sprite)|Clears the current list and rebuilds a new list with the provided items
ResetItems|None|Clears all current options
||

---------

## Usage

Add the DropDownList control to your scene using:
GameObject -> UI -> Extensions -> DropDownList

Then simply add drop down elements to the Items property.  Additionally, Images and other items may be added to enhance the drop down items

---------

## Video Demo

[![Tutorial Video](http://img.youtube.com/vi/JrEfs47FoOE/0.jpg)](http://www.youtube.com/watch?v=JrEfs47FoOE "Dropdown List Tutorial")

---------

## See also

[ComboBox](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/ComboBox)
[AutoCompleteComboBox](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/AutoCompleteComboBox)

---------

## Credits and Donation

Perchik

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/receive-onclick-event-and-pass-it-on-to-lower-ui-elements.293642/)
