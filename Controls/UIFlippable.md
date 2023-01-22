# UIFlippable

==============

A Graphic altering tool which can flip a graphic either Horizontally / Vertically or both.

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

The Flippable effect allows you to flip a graphic either on the Horizontal axis, vertical axis or both through this simple component..

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/UIFlippableInspector.jpg)

*Note* when used with other graphical effects, this component must be ordered the highest, else Unity will report an error. (see usage)

---------

## Properties

The properties of the UI Flippable component are as follows:

Property | Description
--------- | --------------
*Horizontal*|Flip the graphic horizontally
*Vertical*|Flip the graphic vertically
||

---------

## Usage

Available as a Game Component menu in "*UI / Effects / Extensions / Flippable*". Simple add to any Image or Graphic Component.

> *Note*
> Unity has changed it's behaviour about stacking multiple BaseMeshEffects, if the effect alters vertices then the component must be ordered at the top of the components.  
> E.G. UIFlippable must be ordered above OutLine / NicerOutline etc.
> The control will automatically do this when added to a GameObject, but if you reorder it you may get a NullReferenceException.  To fix, either reorder or touch any property.

---------

## Video Demo

*Click to play*

[![UIFlippable Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/UIFlippableDemo.jpg)](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/UIFlippableDemo.mp4 "UIFlippable Demo")

---------

## See also

N/A

---------

## Credits and Donation

Credit ChoMPHi

---------

## External links

Sourced from - [http://forum.unity3d.com/threads/script-flippable-for-ui-graphics.291711/](http://forum.unity3d.com/threads/script-flippable-for-ui-graphics.291711/)
