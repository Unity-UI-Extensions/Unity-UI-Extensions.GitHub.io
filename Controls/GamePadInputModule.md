# GamePad Input Module

> [!IMPORTANT]
> ⚠️ This control has been deprecated for Unity 6 and is no longer maintained. It remains documented for legacy reference.

Stripped down SIM Input module for just gamepad/keyboard input

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

Focused input module for just gamepads as opposed to the standard Standalone Input Module

*NOTE, not compatible with the StandaloneInputModule, so please remove / disable this before adding this component

---------

## Properties

Property | Description
-|-
*Actions Per Second*|Repeat rate for move/submit actions while a button is held.
*Repeat Delay*|Delay before repeating move/submit actions.
*Horizontal Axis*|Axis name for horizontal navigation.
*Vertical Axis*|Axis name for vertical navigation.
*Submit Button*|Input name used to trigger Submit.
*Cancel Button*|Input name used to trigger Cancel.
***On Submit*** (event)|Invoked when a submit action is processed.
***On Cancel*** (event)|Invoked when a cancel action is processed.

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

To enable the Gamepad Input Module, simply add the component to the EventSystem using:
Add Component -> UI -> Extensions -> GamePadInputModule

---------

## Video Demo

"Link to demo video or animated Gifs"

---------

## See also

N/A

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

N/A

---------
