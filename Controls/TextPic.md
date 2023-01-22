# TextPic

==============

Inline images  and hyperlinks for text

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

Provides a html interpreter to add inline images in Text.  HTML code is similar to that used for Unity's native Rich Text HTML

![](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TextPicInspector.jpg)

---------

## Properties

The properties of the TextPic control are as follows:

Property | Description
--------- | --------------
*Image Offset*|Global Image offset
*Image Scaling Factor*|Global scaling factor for all images (they default to match the font size)
*Hyperlink Color*|Override the default color for Hyperlinks
*Icon List*|List of icon replacements and their lookup text
|*Name*|The name of the image, used as the replacement string in the text
|*Sprite*|The sprite to replace text with in the text
|*Offset*|individual offset (as opposed to the Global Image Offset) for this sprite
|*Scale*|individual scale (as opposed to the Global Image Scale Factor) for this sprite
||

*Inherited from Text*

* Character
* Paragraph
* Color / Material and Raycast Target

---------

## Usage

Add TextPic component instead of the standard Text control and decorate with Rich Text HTML, for example:
<a href="http://google.co.uk">Click Me</a>

It can also place Images within blocks of Text by adding Icons to the Icon List with a Name, then instances of that name will be replaced with that Image (careful what name you use :D)

Simply add a new TextPic to the scene using "*UI / Extensions / TextPic*" in the Editor "*GameObject*" menu.

It is also available as a Game Component menu in "*UI / Extensions / TextPic*". You have to remove any existing Text components first, else Unity will warn you.

Additionally, if you want configure hyperlink highlighting colours, simply add a "*Selectable*" component to the same GameObject as the TextPic control and configure it.

> *A Note on Buttons*
> If the TextPic is added as a child of a Button you cannot use the hyperlinks feature of this control, it is purely decorative allowing the text and image replacement.  The TextPic control will add a CanvasGroup control to the TextPic to enable click-through to the button.

---------

## Video Demo

*Click to play*

[![TextPicDemo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TextPicDemo.jpg)](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/TextPicDemo.mp4 "TextPicDemo Demo")

---------

## See also

N/A

---------

## Credits and Donation

* drobina
* w34edrtfg
* playemgames

---------

## External links

* [Sourced from](http://forum.unity3d.com/threads/sprite-icons-with-text-e-g-emoticons.265927/)
