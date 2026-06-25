---
layout: control-ugui
title: "Selectable Scaler"
description: "Scales a Selectable component up/down on hover and press events."
category: "Utilities"
permalink: /ugui/controls/selectable-scaler/
has_video: true
tags: [utilities, selectable, scale, hover, press, animation]
---
# Selectable Scalar

A simple tween scaler to affect Rect Transform scale on other controls.

<!--![](/ugui/images/ Game Image.jpg)-->

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

A simple Tween enhancement that scales another RectTransform according to a preset curve.

![](/ugui/images/SelectableScalarInspector.jpg)

---------

## Properties

The properties of the Selectable Scalar control are as follows:

Property | Description
-|-
*Anim Curve*|The curve that will be used to scale the Rect Transform in and out.
*Speed*|The speed at which the animation will take effect.
*Target*|The target for the animation.

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

Like with other Layout controls, simply add this control to any control that has a *Selectable* component (e.g. Button, NonGraphicSelectable) through the Add Component menu as follows:

"Add Component -> UI -> Extensions -> Selectable Scalar"

---------

## Video Demo

<video class="demo-video" controls preload="metadata" loop muted playsinline poster="/ugui/images/SelectableScalarDemo.jpg" aria-label="Selectable Scaler demo">
  <source src="/ugui/images/SelectableScalarDemo.webm" type="video/webm">
</video>

---------

## See also

* [UI_TweenScale](/ugui/controls/ui-tween-scale/)

---------

## Credits and Donation

Tomek S

---------

## External links

[Sourced from](https://pastebin.com/NXYu37jC)
