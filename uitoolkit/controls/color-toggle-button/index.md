---
layout: control-uitk
title: "Color Toggle Button"
description: "Toggle button that tints itself with a configurable accent colour when active."
category: "Forms"
permalink: /uitoolkit/controls/color-toggle-button/
has_video: false
tags: [forms, toggle, color, tint, button]
---

<!--![](/uitoolkit/images/ColorToggleButtonDemo.jpg)-->

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
> 5 [Constructors](#constructors)
>
> 6 [Methods](#methods)
>
> 7 [Usage](#usage)
>
> 8 [Using the Control](#using-the-control)
>
> 9 [Video Demo](#video-demo)
>
> 10 [Credits and Donation](#credits-and-donation)
>
> 11 [External links](#external-links)

---------

## Overview

`ColorToggleButton` extends `ToggleButton` with per-instance tint colors, a ripple press animation, and a selection overlay. The background color is driven entirely by the tint values, making it straightforward to build color-coded toggle grids without USS variants.

Typical use cases:

- Color picker palette items
- Labeled color-coded category toggles
- Any toggle grid where each item has a distinct brand or theme color

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `IsSelected` | Inherited from `ToggleButton`. Gets or sets the selected state. | `bool` |
| `TintColor` | The background tint used when the button is in its default (unselected) state. | `Color` (read-only; use `SetTintColor` to change) |
| `SelectedTintColor` | The background tint used when the button is selected. | `Color` (read-only; use `SetSelectedTintColor` to change) |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `toggleButton` | Root element (inherited from `ToggleButton`). |
| `toggleButton__image` | Image layer, 100% size, scale-to-fit (inherited). |
| `toggleButton--selected` | Modifier applied when selected (inherited). |
| `toggleButton__icon` | Optional icon element overlaid on the colored background. |
| `toggleButton__ripple` | Primary ripple circle that expands on press. |
| `toggleButton__rippleSecondary` | Secondary ripple circle for the layered ripple effect. |
| `toggleButton__selectedOverlay` | Overlay element shown when selected. |
| `toggleButton__selectedOverlay--visible` | Modifier that makes the selected overlay visible. |

---------

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `OnClicked` | Inherited from `ToggleButton`. Fired on every pointer-down regardless of current state. | none |

---------

## Constructors

| Signature | Description |
| --- | --- |
| `ColorToggleButton(Color tintColor)` | Creates a button with the same tint color for both selected and unselected states. |
| `ColorToggleButton(Color tintColor, Color selectedTintColor)` | Creates a button with distinct tints for each state. |

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetTintColor(Color color)` | Updates the unselected background tint at runtime. |
| `SetSelectedTintColor(Color color)` | Updates the selected background tint at runtime. |
| `SetImage(Texture2D texture)` | Inherited. Sets the icon/image on the button. |
| `ForceSelect()` | Inherited. Sets `IsSelected = true` without firing `OnClicked`. |
| `ForceDeselect()` | Inherited. Sets `IsSelected = false` without firing `OnClicked`. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Color Toggle Button
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Color Toggle Button Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions" editor-extension-mode="False">
    <ext:ColorToggleButton tint-color="#FF5A5A" selected-tint-color="#FF9090" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created in the Editor and in Play Mode, so no manual stylesheet reference is needed while authoring. The starter templates also reference the stylesheet explicitly, which covers player builds; for hand-written UXML or code-first UI in builds, add the stylesheet to your UXML or panel theme.

---------

## Using the Control

### Color Palette Grid

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class ColorPaletteController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;

    private static readonly Color[] PaletteColors = new[]
    {
        new Color(0.91f, 0.27f, 0.38f),   // red
        new Color(0.25f, 0.56f, 0.96f),   // blue
        new Color(0.18f, 0.80f, 0.44f),   // green
        new Color(0.98f, 0.75f, 0.18f),   // yellow
    };

    private ColorToggleButton _activeButton;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;
        var row = root.Q<VisualElement>("paletteRow");

        foreach (var color in PaletteColors)
        {
            // Slightly lighter shade for selected state
            var selectedColor = Color.Lerp(color, Color.white, 0.25f);
            var btn = new ColorToggleButton(color, selectedColor);

            btn.OnClicked += () =>
            {
                // Deselect previous
                if (_activeButton != null && _activeButton != btn)
                    _activeButton.ForceDeselect();

                _activeButton = btn;
                Debug.Log($"Selected color: {color}");
            };

            row.Add(btn);
        }
    }
}
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/ColorToggleButtonDemo.jpg" aria-label="Color Toggle Button demo">
  <source src="/uitoolkit/images/ColorToggleButtonDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
