# ComboBox

==============

A fixed combobox implementation for text

## Contents

---------

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

Standard combobox style control with support for multiple textual child items.
Similar to the new built in Unity Dropdown control

![ComboBox inspector](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ComboBoxInspector.jpg)

---------

## Properties

The properties of the Box Slider control are as follows:

Property | Description
--------- | --------------
*Available Options*|Array of text based options for the dropdown/selection
*Scroll Bar Width*|The width of the scrollbar when displayed
*Items To Display*|Number of child items to display when opened. *Note default 0 shows NO items.
*Sort Items*|Should the items in the combo box be sorted
*On Selection Changed* (event) |The Event fired when the user selects an option or loses focus
||

---------

## Methods

Method | Arguments | Description
--- | --- | ---
AddItem|String|Adds a single item to the list
RemoveItem|String|Removes a single item from the list
SetAvailableOptions|List of String|Clears the current options and replaces with new list (array or List)
SetAvailableOptions|Array of String|Clears the current options and replaces with new list (array or List)
ResetItems|None|Clears all current options
||

---------

## Usage

Add the combobox control to your scene using:
GameObject -> UI -> Extensions -> ComboBox

Then simply add child elements to the Items property.  

---------

## Video Demo

[![Tutorial Video](http://img.youtube.com/vi/JrEfs47FoOE/0.jpg)](http://www.youtube.com/watch?v=JrEfs47FoOE "ComboBox Tutorial")

---------

## See also

[DropDownList](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/DropDownList)
[AutoCompleteComboBox](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/AutoCompleteComboBox)

---------

## Credits and Donation

Perchik

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/receive-onclick-event-and-pass-it-on-to-lower-ui-elements.293642/)
