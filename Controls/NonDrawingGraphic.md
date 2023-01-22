# Non-Drawing Graphic

==============

A graphic component with zero draw calls, useful (when paired with a click script or the Selectable Extension) for invisible buttons or hit test blockers.

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

The Non Drawing Graphic component allows you to add a graphic hit testable area with zero draw calls.  The Raycast hit test can also be enabled or disabled (instead of using a CanvasGroup)

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/NonDrawingGraphicInspector.jpg)

It is also very useful when paired with the Selectable Extension to add Click, Release and Hold capabilities.

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/NonDrawingGraphicInspectorClickable.jpg)

---------

## Properties

The properties of the Non Drawing Graphic component are as follows:

Property | Description
--------- | --------------
*Raycast Target*|Should this GO block raycasts or not.  Changeable in code or editor.
||

---------

## Usage

Simply add the default Non Drawing Graphic component to a RectTransform using "*UI / Extensions / Non Drawing Graphic*" in the Editor "*Component*" menu.

It is also available as a Game Component menu in "*UI / Extensions / Non Drawing Graphic*". 

There is also a "Clickable" version, which includes the additional components to make the NonDrawing Graphic support events when clicked.

*Note, in Source there are also two Editor menu's to add an Empty GO with the component attached and on to add the Non Drawing Graphic with the additional Selectable Extension.
These will be added to the asset in the next update.

---------

## Video Demo

*Click to play*

[![Non Drawing Graphic Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/NonDrawingGraphicDemo.jpg)](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/NonDrawingGraphicDemo.mp4 "Non Drawing Graphic Demo")

---------

## See also

* [Selectable Extension](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/UISelectableExtension)
(to add the extended click behaviour to this component)

---------

## Credits and Donation

Credit [Slipp Douglas Thompson / capnslipp ](https://github.com/capnslipp)
Submitted by [PixelEnvision](https://github.com/PixelEnvision)

---------

## External links

Sourced from - [https://gist.github.com/capnslipp/349c18283f2fea316369/](https://gist.github.com/capnslipp/349c18283f2fea316369)
