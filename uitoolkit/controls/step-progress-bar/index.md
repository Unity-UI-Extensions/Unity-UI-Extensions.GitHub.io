---
layout: control-uitk
title: "Step Progress Bar"
description: "Segmented progress bar with labelled milestone steps and fill animation."
category: "Feedback"
permalink: /uitoolkit/controls/step-progress-bar/
has_video: false
tags: [feedback, progress, steps, bar, milestone]
---

![Step Progress Bar example](step-progress-bar-example.png)

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

`StepProgressBar` is a horizontal progress bar that expresses progress as a fraction of discrete steps. The fill width is `NormalizedProgress × 100%`. The gradient is generated from two colors (inner and outer) into a 256 × 1 `Texture2D`. A warning is logged and `maxSteps` is clamped to `1` when a non-positive value is passed to `SetProgress`.

Typical use cases:

- Onboarding flow completion indicator
- Multi-step form or wizard progress
- Task or challenge completion tracker

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `NormalizedProgress` | Gets the current fill fraction in `[0, 1]`. Computed from `CurrentSteps / MaxSteps`. | `float` (read-only) |
| `CurrentSteps` | Gets the current step count. | `int` (read-only) |
| `MaxSteps` | Gets the total number of steps. | `int` (read-only) |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `stepProgressBar` | Root element. |
| `stepProgressBar__background` | Background track. `border-radius: 4px`, `overflow: hidden`. |
| `stepProgressBar__fill` | Fill element. Width is driven inline as a percentage. |

---------

## Events

This control does not emit events.

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetProgress(int steps, int maxSteps)` | Sets the current and maximum steps. Recomputes `NormalizedProgress` and updates the fill width. Logs a warning if `maxSteps <= 0` and clamps it to `1`. |
| `SetInnerColor(string hex)` | Sets the inner (left-edge) gradient color. Rebuilds the gradient texture. |
| `SetOuterColor(string hex)` | Sets the outer (right-edge) gradient color. Rebuilds the gradient texture. |
| `SetGradientColors(string innerColorHex, string outerColorHex)` | Convenience method that sets both gradient colors in one call. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Step Progress Bar
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Step Progress Bar Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions" editor-extension-mode="False">
    <ext:StepProgressBar current-steps="2" max-steps="4" inner-color="#4A90E2" outer-color="#7B68EE" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created in the Editor and in Play Mode, so no manual stylesheet reference is needed while authoring. The starter templates also reference the stylesheet explicitly, which covers player builds; for hand-written UXML or code-first UI in builds, add the stylesheet to your UXML or panel theme.

---------

## Using the Control

### Onboarding Progress

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class OnboardingProgressController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;

    private StepProgressBar _progressBar;
    private int _currentStep = 0;
    private const int TotalSteps = 5;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;

        _progressBar = new StepProgressBar();
        _progressBar.SetGradientColors(innerColorHex: "#e94560", outerColorHex: "#9b1d35");
        _progressBar.SetProgress(_currentStep, TotalSteps);

        root.Q<VisualElement>("progressContainer").Add(_progressBar);
    }

    public void AdvanceStep()
    {
        _currentStep = Mathf.Min(_currentStep + 1, TotalSteps);
        _progressBar.SetProgress(_currentStep, TotalSteps);
        Debug.Log($"Progress: {_progressBar.NormalizedProgress:P0}");
    }
}
```

### Dynamic Color Feedback

```csharp
// Green when complete, default brand color otherwise
private void RefreshBarColor()
{
    if (_progressBar.CurrentSteps >= _progressBar.MaxSteps)
        _progressBar.SetGradientColors("#18cc6e", "#0d7a42");
    else
        _progressBar.SetGradientColors("#e94560", "#9b1d35");
}
```

---------

## Video Demo

<video class="demo-video" autoplay loop muted playsinline poster="step-progress-bar-example.png" aria-label="Step Progress Bar demo">
  <source src="step-progress-bar-demo.webm" type="video/webm">
</video>

### Example Scenes

This control is demonstrated in the following package example:

- [Step Wizard](/uitoolkit/examples/step-wizard/)

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
