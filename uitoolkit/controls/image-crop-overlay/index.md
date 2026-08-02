---
layout: control-uitk
title: "Image Crop Overlay"
description: "Full-screen modal image cropper with drag-to-pan, pinch-to-zoom, and configurable square export."
category: "Utilities"
permalink: /uitoolkit/controls/image-crop-overlay/
has_video: false
tags: [utilities, image, crop, editor, overlay]
---

<!--![](/uitoolkit/images/ImageCropOverlayControlDemo.jpg)-->

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Nested Types](#nested-types)
>
> 3 [USS Classes](#uss-classes)
>
> 4 [Public API](#public-api)
>
> 5 [Usage](#usage)
>
> 6 [Using the Control](#using-the-control)
>
> 7 [Video Demo](#video-demo)
>
> 8 [Credits and Donation](#credits-and-donation)
>
> 9 [External links](#external-links)

---------

## Overview

`ImageCropOverlayControl` is a full-screen modal cropper for square image exports. It displays the source image inside a movable and zoomable viewport, then exports the visible area to a new `Texture2D` when the user confirms.

Typical use cases:

- Profile picture editing before upload
- Cover-image cropping with a fixed export size
- Any UI Toolkit workflow that needs a self-contained move-and-scale image confirmation step

---------

## Nested Types

### `Configuration`

`Configuration` customizes the overlay title, button labels, export size, zoom limits, screen margins, viewport width ratio, and normalized corner radius used by the crop viewport mask.

---------

## USS Classes

| Class | Description |
| --- | --- |
| `imageCropOverlay` | Full-screen modal root. |
| `imageCropOverlay__panel` | Centred container for the header, viewport, and footer. |
| `imageCropOverlay__header` | Header row that hosts the title. |
| `imageCropOverlay__title` | Title label. |
| `imageCropOverlay__viewportHost` | Layout host used to centre the crop viewport. |
| `imageCropOverlay__viewport` | Clipped crop viewport that receives drag, pinch, and wheel input. |
| `imageCropOverlay__image` | Absolute-positioned image surface inside the viewport. |
| `imageCropOverlay__footer` | Footer row for the action buttons. |
| `imageCropOverlay__buttonSlot` | Layout slot for each footer button. |
| `imageCropOverlay__button` | Shared button class applied to the cancel/save buttons. |
| `imageCropOverlay__button--cancel` | Modifier for the cancel button. |
| `imageCropOverlay__button--save` | Modifier for the save button. |

---------

## Public API

| Signature | Description |
| --- | --- |
| `Show(VisualElement anchor, Texture2D sourceTexture, Configuration configuration, Action<Texture2D> onConfirmed, Action onCancelled = null)` | Creates and displays the overlay on the anchor's panel root. Returns the created overlay or `null` when it cannot be shown. |
| `CreateUniformCornerRadiusPercent(float percent)` | Creates a clamped, uniform normalized corner-radius vector for the crop mask. |
| `ResolveNormalizedCornerRadiusPercent(VisualElement sourceElement, Vector4 fallback)` | Converts the source element's resolved pixel radii into normalized percentages suitable for the crop mask. |

---------

## Usage

> This control is created from code and has no UXML element or editor menu entry.

Invoke the static `ImageCropOverlayControl.Show(anchor, sourceTexture, configuration, onConfirmed)` from code; the overlay attaches itself to the panel root. The shared extensions stylesheet is applied automatically when the control is created.

---------

## Using the Control

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class AvatarCropExample : MonoBehaviour
{
    [SerializeField] private UIDocument document;
    [SerializeField] private Texture2D avatarSource;

    private CircularImageButton avatarButton;

    private void OnEnable()
    {
        var root = document.rootVisualElement;

        avatarButton = new CircularImageButton();
        avatarButton.SetImage(avatarSource);
        avatarButton.Clicked += OpenCropper;

        root.Add(avatarButton);
    }

    private void OpenCropper()
    {
        var configuration = new ImageCropOverlayControl.Configuration
        {
            Title = "Move and Scale",
            ExportSize = 512,
            CornerRadiusPercent = ImageCropOverlayControl.CircleCornerRadiusPercent,
        };

        ImageCropOverlayControl.Show(
            avatarButton,
            avatarSource,
            configuration,
            cropped => avatarButton.SetImage(cropped));
    }
}
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/ImageCropOverlayControlDemo.jpg" aria-label="Image Crop Overlay demo">
  <source src="/uitoolkit/images/ImageCropOverlayControlDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
