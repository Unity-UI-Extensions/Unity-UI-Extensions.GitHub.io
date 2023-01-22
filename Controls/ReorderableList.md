# Re-orderable List

==============

A collection of List Grid control which allow for drag / drop reordering of the child items.  Includes features to move / clone or freeze containers

Contents

---------

> 1 [Overview](#markdown-header-overview)

> 2 [Properties](#markdown-header-properties)

> 3 [Usage](#markdown-header-usage)

> 4 [Video Demo](#markdown-header-video-demo)

> 5 [See also](#markdown-header-see-also)

> 6 [Credits and Donation](#markdown-header-credits-and-donation)

> 7 [External links](#markdown-header-external-links)

---------

## Overview

The Re-orderable list is a very powerful control which includes several "out of the box" setups, including:

* Vertical, Horizontal and Grid layouts
* Vertical, Horizontal and Grid layouts using a ScrollRect

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/ReorderableListInspector.jpg)

The control can be enabled in multiple flavors, featuring such capabilities as:

* Allowing Dragging (allows containers that can be dropped in to but not removed)
* Clone or Move child elements
* Allowing dropping (containers that be dragged from but not dropped in to)

As well as events for each state of the child content as they are interacted with.

---------

## Properties

The properties of the Re-orderable List control are as follows:

Property | Description
--------- | --------------
*Content layout*|The container holding the child content (similar to the ScrollRect content property)
*Draggable Area*|Defaults to the Content Layout / parent rect transform, but can be overridden to identify an alternate supported dragging space
*Is Draggable*|Can child object be dragged from this container
*Clone Dragged Object*|If true, a copy is made of the original content when dragging, else it moves the original child content item
*Is Dropable*|Can objects be dropped in to this container
*On Element Dropped* (event) |The Event fired when a child item is released by a user
*On Element Grabbed* (event) |The Event fired when a child item is being held by the user
*On Element Removed* (event) |The Event fired when a child item is removed from a container
*On Element Added* (event) |The Event fired when a child item is added from a container
||

The properties of the individual Re-orderable List Items are as follows:

Property | Description
--------- | --------------
*Is Grabbable*|Can the object be grabbed from a re-orderable list
*Is Transferable*|Can the object be transferred from one re-orderable list to the next
*Is Droppable In Space*|Can the item be dropped outside of a re-orderable list. *note, once dropped outside they cannot be picked up again.

---------

## Usage

Simply add the default Re-orderable List control to the scene using one of the pre-built options in the Editor "*GameObject*" menu:

* "*UI / Extensions / Re-orderable Lists / Re-orderableList Vertical List*"
* "*UI / Extensions / Re-orderable Lists / Re-orderableList Horizontal List*"
* "*UI / Extensions / Re-orderable Lists / Re-orderableList Grid*"
* "*UI / Extensions / Re-orderable Lists / Re-orderableList Vertical ScrollRect*"
* "*UI / Extensions / Re-orderable Lists / Re-orderableList Horizontal ScrollRect*"
* "*UI / Extensions / Re-orderable Lists / Re-orderableList Grid ScrollRect*"

The base control is also available as a Game Component menu in "*UI / Extensions / Re-orderable List*". However, you will need to manually set up the control.

---------

## Video Demo

*Click to play*

[![View Intro Video](http://i.giphy.com/3o85xri0ARKKSfDHIQ.gif)](https://youtu.be/jpyFiRvSmbg?t=1m33s "Re-Orderable List walk-through video")

---------

## See also

N/A

---------

## Credits and Donation

Credit Ziboo

---------

## External links

Sourced from - [http://forum.unity3d.com/threads/free-reorderable-list.364600/](http://forum.unity3d.com/threads/free-reorderable-list.364600/)
