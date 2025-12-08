# ReturnKeyTrigger

Enables you to bind the return key within an InputField control to a button, also supports toggling the highlight of a control or field.

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

If you want to enable a user to use the Return key on finishing entering in a field, the same as a web style control or Submit, this will enabling binding that action to a UI button (aka submit button).
It also allows you to hind to a Highlight effect on the field (e.g. a red highlight for mandatory fields) which will enable/disable based on the submit action.

---------

## Properties

Property | Description
-|-
*Input Field*|InputField listened to for Return key.
*Target Button*|Button invoked when Return is pressed.
*Highlight Target*|Optional GameObject toggled to show validation state.
*Trigger Only When Input Valid*|If enabled, only submits when InputField has text.
***On Submit*** (event)|Event fired when Return key triggers submission.

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Either add the "ReturnKeyTrigger" component to an existing UI InputField control, or create an Empty GameObject and add the "ReturnKeyTrigger" component using:

"Add Component -> UI -> Extensions -> Return Key Trigger"

This will automatically add an Input field if none is present.

---------

## Video Demo

tbc

---------

## See also

N/A

---------

## Credits and Donation

Melang

---------

## External links

N/A
