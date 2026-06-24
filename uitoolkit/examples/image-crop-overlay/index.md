---
layout: example-uitk
title: "Image Crop Overlay"
description: "Pick an avatar image, then pan, pinch-zoom and crop it inside a full-screen modal overlay."
category: "Media"
permalink: /uitoolkit/examples/image-crop-overlay/
tags: [media, image, crop, avatar]
controls:
  - name: "Image Crop Overlay"
    permalink: /uitoolkit/controls/image-crop-overlay/
  - name: "Circular Image Button"
    permalink: /uitoolkit/controls/circular-image-button/
  - name: "Pill Button"
    permalink: /uitoolkit/controls/pill-button/
---

## Overview

This example creates a profile-picture editing flow. It starts with a generated portrait texture, opens `ImageCropOverlayControl` from a `CircularImageButton`, and applies the saved crop back into the screen preview.

## Controls Featured

- [CircularImageButton](/uitoolkit/controls/circular-image-button/) — preview and crop entry point
- [ImageCropOverlayControl](/uitoolkit/controls/image-crop-overlay/) — move/scale crop overlay and texture exporter
- [PillButton](/uitoolkit/controls/pill-button/) — edit and reset actions

## Scene Setup

This package now ships a ready-made sample scene in `Examples~/ImageCropOverlay/ImageCropOverlayDemo.unity`.

If you want to recreate it manually instead:

1. Create a new Unity scene.
2. Add a GameObject with a `UIDocument`.
3. Assign the sample panel settings from `Examples~/Shared/UIToolkitExtensionsExamplePanelSettings.asset`.
4. Add the `ImageCropOverlayDemo` MonoBehaviour from `Examples~/ImageCropOverlay/` to the same GameObject.
5. Press Play.

## What to Expect

The sample screen shows:

- A large `CircularImageButton` displaying the generated portrait.
- A separate saved-preview card showing the current texture state.
- An `Edit Image` button that opens the cropper.
- A `Reset` button that restores the original generated portrait.
- A status line describing crop, cancel, save, and reset actions.

## Key Code Pattern

```csharp
var configuration = new ImageCropOverlayControl.Configuration
{
    Title = "Move and Scale",
    ExportSize = 512,
    CornerRadiusPercent = ImageCropOverlayControl.CircleCornerRadiusPercent,
};

ImageCropOverlayControl.Show(
    imageButton,
    ActiveTexture,
    configuration,
    cropped => ReplaceCroppedTexture(cropped));
```