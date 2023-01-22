# SoftAlphaMask

==============

Shader based mask able to clip images using an alpha mask

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

Where most Alpha Mask effects built into the Unity UI system work on hard transparencies, the Soft Alpha Mask is able to work with alpha mask gradients and includes animation features to enable a smooth transition.

![Soft Alpha Mask Inspector](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/SoftAplhaMaskInspector.jpg)

---------

## Properties

The properties of the Selectable Scalar control are as follows:

Property | Description
--------- | --------------
*Mask Area*|The area that is to be used as the container.
*Alpha Mask*|Texture to be used to do the soft alpha.
*Cut Off*|At what point to apply the alpha min range 0-1.
*Hard Blend*|Implement a hard blend based on the Cutoff.
*Flip Alpha Mask*|Flip the masks alpha value.
*Don't clip Mask Scaling Rect*|If a different Mask Scaling Rect is given, and this value is true, the area around the mask will not be clipped.
||

---------
## Usage

Simply add the "Soft Mask Script" component to an existing UI object and apply a "Mask" texture.  Alter the "Cut Off" value to scale out the masking effect.

There is also a Text version of the Soft Alpha Mask to work with Text Objects.

---------

## Video Demo

![Soft Alpha Mask Demo](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/wiki/Controls/Images/SoftAlphaMaskDemo.gif)

---------

## See also

N/A

---------

## Credits and Donation

Charles Humphrey (@NemoKrad)

---------

## External links

[https://www.youtube.com/watch?v=JVds9P9J_hU](https://www.youtube.com/watch?v=JVds9P9J_hU)
