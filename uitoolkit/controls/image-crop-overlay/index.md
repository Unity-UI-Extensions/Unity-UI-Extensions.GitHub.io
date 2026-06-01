---
layout: control-uitk
title: "Image Crop Overlay"
description: "Full-screen modal image cropper with drag-to-pan, pinch-to-zoom, and configurable square export."
category: "Utilities"
permalink: /uitoolkit/controls/image-crop-overlay/
has_video: false
tags: [utilities, image, crop, modal, editor, avatar, zoom, pan]
---

## Summary

`ImageCropOverlayControl` is a full-screen modal cropper for square image exports. It displays the source `Texture2D` inside a movable and zoomable viewport, then exports the visible area to a new `Texture2D` when the user confirms. The crop shape is configurable — circular for avatars, square, or any custom normalised corner radius. Interaction is fully gesture-driven: drag to pan, pinch to zoom on multi-touch devices, or scroll-wheel to zoom on desktop.

The control is shown via a static `Show()` factory method rather than being added to the hierarchy directly. When the user taps Cancel or Save the overlay removes itself automatically.

Typical use cases:

- Profile picture editing before upload
- Cover-image cropping with a fixed export size
- Any UI Toolkit workflow that needs a self-contained move-and-scale image confirmation step

## Configuration

`ImageCropOverlayControl.Configuration` is a sealed class that customises every aspect of the overlay. All properties have sensible defaults.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `Title` | `string` | `"Move and Scale"` | Text shown in the header bar. |
| `CancelLabel` | `string` | `"Cancel"` | Label for the cancel button. |
| `SaveLabel` | `string` | `"Save"` | Label for the save/confirm button. |
| `ExportSize` | `int` | `512` | Side length in pixels of the exported square `Texture2D`. |
| `ScreenMarginPx` | `float` | `48f` | Minimum screen-edge margin around the panel in pixels. |
| `MaxViewportWidthRatio` | `float` | `0.9f` | Maximum fraction of screen width the crop viewport may occupy. |
| `MaxZoom` | `float` | `4f` | Maximum zoom multiplier the user can reach. |
| `CornerRadiusPercent` | `Vector4` | `CircleCornerRadiusPercent` | Normalised per-corner radius of the crop mask (0–0.5 for each corner). Use `CircleCornerRadiusPercent` for a circle or `Vector4.zero` for a sharp square. |

## USS Classes

| Class | Description |
| --- | --- |
| `imageCropOverlay` | Full-screen modal root element. |
| `imageCropOverlay__panel` | Centred container hosting the header, viewport, and footer. |
| `imageCropOverlay__header` | Header row containing the title label. |
| `imageCropOverlay__title` | Title label text element. |
| `imageCropOverlay__viewportHost` | Layout host used to centre the crop viewport. |
| `imageCropOverlay__viewport` | Clipped crop viewport that receives drag, pinch, and wheel input. |
| `imageCropOverlay__image` | Absolute-positioned image surface rendered inside the viewport. |
| `imageCropOverlay__footer` | Footer row containing the action buttons. |
| `imageCropOverlay__buttonSlot` | Layout slot wrapping each footer button. |
| `imageCropOverlay__button` | Shared style class applied to both footer buttons. |
| `imageCropOverlay__button--cancel` | Modifier applied to the cancel button. |
| `imageCropOverlay__button--save` | Modifier applied to the save/confirm button. |

## Public API

| Signature | Description |
| --- | --- |
| `static ImageCropOverlayControl Show(VisualElement anchor, Texture2D sourceTexture, Configuration configuration, Action<Texture2D> onConfirmed, Action onCancelled = null)` | Creates and displays the overlay on the anchor's panel root. Returns the created overlay, or `null` if the panel cannot be resolved. |
| `static Vector4 CreateUniformCornerRadiusPercent(float percent)` | Creates a clamped, uniform normalised corner-radius vector (all four corners the same value). |
| `static Vector4 ResolveNormalizedCornerRadiusPercent(VisualElement sourceElement, Vector4 fallback)` | Converts the source element's resolved pixel corner radii into normalised percentages for the crop mask. |

### Static Fields

| Name | Type | Description |
| --- | --- | --- |
| `CircleCornerRadiusPercent` | `Vector4` | Preset `(0.5, 0.5, 0.5, 0.5)` — produces a fully circular crop mask. |

## Using the Control

### Profile Picture / Avatar Crop

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class AvatarCropExample : MonoBehaviour
{
    [SerializeField] private UIDocument document;
    [SerializeField] private Texture2D  avatarSource;

    private CircularImageButton _avatarButton;

    private void OnEnable()
    {
        var root = document.rootVisualElement;

        _avatarButton = new CircularImageButton();
        _avatarButton.SetImage(avatarSource);
        _avatarButton.Clicked += OpenCropper;

        root.Add(_avatarButton);
    }

    private void OpenCropper()
    {
        var configuration = new ImageCropOverlayControl.Configuration
        {
            Title               = "Move and Scale",
            ExportSize          = 512,
            CornerRadiusPercent = ImageCropOverlayControl.CircleCornerRadiusPercent,
        };

        ImageCropOverlayControl.Show(
            _avatarButton,
            avatarSource,
            configuration,
            cropped => _avatarButton.SetImage(cropped));
    }
}
```

### Square Crop with Cancel Callback

```csharp
var configuration = new ImageCropOverlayControl.Configuration
{
    Title               = "Crop Cover Image",
    CancelLabel         = "Discard",
    SaveLabel           = "Apply",
    ExportSize          = 1024,
    MaxZoom             = 6f,
    CornerRadiusPercent = Vector4.zero,  // sharp square
};

ImageCropOverlayControl.Show(
    anchor         : coverButton,
    sourceTexture  : rawCoverPhoto,
    configuration  : configuration,
    onConfirmed    : tex => UploadCoverImage(tex),
    onCancelled    : () => Debug.Log("Crop cancelled"));
```

### Matching the Crop Shape to an Existing Element

```csharp
// Mirror the corner radius of whatever button launched the crop
var configuration = new ImageCropOverlayControl.Configuration
{
    ExportSize          = 512,
    CornerRadiusPercent = ImageCropOverlayControl.ResolveNormalizedCornerRadiusPercent(
                              launchButton,
                              ImageCropOverlayControl.CircleCornerRadiusPercent),
};

ImageCropOverlayControl.Show(launchButton, sourceTexture, configuration, OnCropSaved);
```
