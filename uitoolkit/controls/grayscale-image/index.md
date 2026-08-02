---
layout: control-uitk
title: "Grayscale Image"
description: "Shader-based Image element that renders in greyscale with adjustable intensity."
category: "Utilities"
permalink: /uitoolkit/controls/grayscale-image/
has_video: false
tags: [utilities, image, grayscale, shader, effect]
---

<!--![](/uitoolkit/images/GrayscaleImageDemo.jpg)-->

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Properties](#properties)
>
> 3 [USS Classes](#uss-classes)
>
> 4 [Events](#events)
>
> 5 [Methods](#methods)
>
> 6 [Usage](#usage)
>
> 7 [Using the Control](#using-the-control)
>
> 8 [Video Demo](#video-demo)
>
> 9 [Credits and Donation](#credits-and-donation)
>
> 10 [External links](#external-links)

---------

## Overview

`GrayscaleImage` is an `ImmediateModeElement` that renders a sprite or texture using `Graphics.DrawTexture` and supports toggling a greyscale effect via a material property. The greyscale effect requires a custom `Material` that exposes `_MainTex` and `_GreyscaleEnabled` shader properties; without a compatible material the image renders in full color only.

Typical use cases:

- Profile or media images that switch to greyscale when disabled or locked
- Toggling greyscale on achievement/badge imagery for locked states
- Any image that needs a shader-driven color/greyscale toggle without a separate texture asset

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `SpriteProperty` | The `Sprite` to render. Mutually exclusive with `TextureProperty`. | `Sprite` |
| `TextureProperty` | The `Texture` to render. Mutually exclusive with `SpriteProperty`. | `Texture` |
| `scaleMode` | How the image is scaled within its bounds. | `ScaleMode` |
| `Material` | The material used for rendering. Must expose `_MainTex` and `_GreyscaleEnabled` for the greyscale feature. | `Material` |
| `GreyscaleEnabled` | Gets or sets whether the greyscale shader effect is active. Only functional when a compatible material is assigned. | `bool` |
| `MainTextureProperty` | The shader property name for the main texture. | `string` (default `"_MainTex"`) |
| `GreyscaleToggleProperty` | The shader property name for the greyscale toggle. | `string` (default `"_GreyscaleEnabled"`) |

### Constants

| Name | Value | Description |
| --- | --- | --- |
| `DefaultMainTextureProperty` | `"_MainTex"` | Default shader property name for the main texture. |
| `DefaultGreyscaleToggleProperty` | `"_GreyscaleEnabled"` | Default shader property name for the greyscale toggle. |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `grayscaleImage` | Root element. Dimensions should be set via USS or inline style; the element uses its resolved layout rect for `Graphics.DrawTexture`. |

---------

## Events

This control does not emit events. Repaint is triggered automatically by the immediate-mode element lifecycle.

---------

## Methods

This control exposes its API entirely through properties. No additional public methods are defined beyond those inherited from `ImmediateModeElement`.

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Grayscale Image
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Grayscale Image Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions">
    <ext:GrayscaleImage scale-mode="ScaleToFit" greyscale-enabled="true" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created, so no manual stylesheet reference is required.

---------

## Using the Control

### Toggle Greyscale on a Locked Achievement

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class AchievementBadgeController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;
    [SerializeField] private Sprite _badgeSprite;
    [SerializeField] private Material _greyscaleMaterial; // shader with _MainTex + _GreyscaleEnabled

    private GrayscaleImage _badgeImage;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;

        _badgeImage = new GrayscaleImage();
        _badgeImage.style.width = 80;
        _badgeImage.style.height = 80;
        _badgeImage.SpriteProperty = _badgeSprite;
        _badgeImage.Material = _greyscaleMaterial;
        _badgeImage.scaleMode = ScaleMode.ScaleToFit;

        root.Q<VisualElement>("badgeContainer").Add(_badgeImage);
    }

    public void SetLocked(bool locked)
    {
        _badgeImage.GreyscaleEnabled = locked;
    }
}
```

### Texture-Based Rendering with Custom Property Names

```csharp
// If your shader uses different property names:
_badgeImage.MainTextureProperty = "_BaseMap";
_badgeImage.GreyscaleToggleProperty = "_UseGreyscale";
_badgeImage.TextureProperty = _photoTexture;
_badgeImage.GreyscaleEnabled = true;
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/GrayscaleImageDemo.jpg" aria-label="Grayscale Image demo">
  <source src="/uitoolkit/images/GrayscaleImageDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
