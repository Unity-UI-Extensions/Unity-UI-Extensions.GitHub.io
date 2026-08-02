---
layout: control-uitk
title: "Pill Button"
description: "Primary CTA button in a rounded pill shape with press flash animation."
category: "Primitives"
permalink: /uitoolkit/controls/pill-button/
has_video: false
tags: [primitives, button, pill, cta, animation]
---

<!--![](/uitoolkit/images/PillButtonDemo.jpg)-->

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

`PillButton` is a rounded, gradient-filled call-to-action button with a flash feedback animation on press. The gradient is generated from two colors (inner and outer) into a 256 × 1 `Texture2D` that is set as the background image. A white overlay fades in briefly on tap to provide tactile feedback. The gradient texture is destroyed when the element detaches from the panel.

Typical use cases:

- Primary call-to-action buttons (Continue, Submit, Get Started)
- Form submission buttons
- Prominent single-action navigation controls

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `Text` | Gets or sets the button label text. | `string` |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `pillButton` | Root element. |
| `pillButton__background` | Gradient background layer. `border-radius: 999px`, `overflow: hidden`. Holds the gradient texture. |
| `pillButton__flash` | White overlay element used for the press flash effect. |
| `pillButton__flash--active` | Modifier that triggers a 100 ms opacity transition on the flash overlay. |
| `pillButton__label` | Text label element centered over the button. |

---------

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `Clicked` | Fired when the button is tapped or clicked. The flash animation plays before this event is dispatched. | none |

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetInnerColor(string hex)` | Sets the inner (left-edge) gradient color using a hex string (e.g. `"#e94560"`). Rebuilds the gradient texture. |
| `SetOuterColor(string hex)` | Sets the outer (right-edge) gradient color using a hex string. Rebuilds the gradient texture. |
| `SetTextColor(Color color)` | Sets the label text color. |
| `SetFontSize(float size)` | Sets the label font size in pixels. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Pill Button
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Pill Button Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions" editor-extension-mode="False">
    <ext:PillButton text="Click Me!" inner-color="#4A90E2" outer-color="#7B68EE" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created in the Editor and in Play Mode, so no manual stylesheet reference is needed while authoring. The starter templates also reference the stylesheet explicitly, which covers player builds; for hand-written UXML or code-first UI in builds, add the stylesheet to your UXML or panel theme.

---------

## Using the Control

### Primary CTA

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class OnboardingFooterController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;

    private PillButton _continueButton;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;

        _continueButton = new PillButton();
        _continueButton.Text = "Continue";
        _continueButton.SetInnerColor("#e94560");
        _continueButton.SetOuterColor("#9b1d35");
        _continueButton.SetTextColor(Color.white);
        _continueButton.SetFontSize(16f);

        _continueButton.Clicked += OnContinueTapped;

        root.Q<VisualElement>("footer").Add(_continueButton);
    }

    private void OnContinueTapped()
    {
        Debug.Log("Continue tapped");
    }
}
```

### Dynamic Color Update

```csharp
// Reflect form validity through button color
private void UpdateButtonState(bool isValid)
{
    if (isValid)
    {
        _continueButton.SetInnerColor("#18cc6e");
        _continueButton.SetOuterColor("#0d7a42");
        _continueButton.Text = "Submit";
    }
    else
    {
        _continueButton.SetInnerColor("#555555");
        _continueButton.SetOuterColor("#333333");
        _continueButton.Text = "Fill all fields";
    }
}
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/PillButtonDemo.jpg" aria-label="Pill Button demo">
  <source src="/uitoolkit/images/PillButtonDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
