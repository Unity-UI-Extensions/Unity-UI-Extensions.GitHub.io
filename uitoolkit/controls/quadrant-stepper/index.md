---
layout: control-uitk
title: "Quadrant Stepper"
description: "Four-directional step selector displayed as an overlay compass widget."
category: "Navigation"
permalink: /uitoolkit/controls/quadrant-stepper/
has_video: false
tags: [navigation, stepper, direction, compass, selector]
---

<!--![](/uitoolkit/images/QuadrantStepperDemo.jpg)-->

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

`QuadrantStepper` is a segmented control that divides its width into equally-sized tap targets. A sliding overlay animates between the selected segment. By default it is created with four equal segments; the option list can be replaced at any time via `SetOptions`. The overlay sits at 90% of the control's height (5% inset top and bottom) to create a floating appearance.

Typical use cases:

- Tab bar or mode switcher
- Category or filter selector
- Any fixed-option segmented navigation control

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `SelectedIndex` | Gets or sets the index of the currently selected segment. | `int` |
| `SelectedText` | Gets the label text of the currently selected segment. | `string` (read-only) |

### USS Custom Properties

| Name | Description | Default |
| --- | --- | --- |
| `--quadrantStepper-animation-duration-ms` | Duration of the sliding overlay animation in milliseconds. | Defined in package USS |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `quadrantStepper` | Root element. |
| `quadrantStepper__overlay` | The sliding highlight overlay. Absolutely positioned. Transitions between segments. |
| `quadrantStepper__segments` | Flex row container holding all segment elements. |
| `quadrantStepper__segment` | Individual segment tap target. Flex-grows equally to divide available width. |
| `quadrantStepper__label` | Text label inside each segment. |
| `is-selected` | Modifier applied to the currently selected segment. |

---------

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `SelectionChanged` | Fired when the selected segment changes via tap or programmatic call (unless suppressed). | `int index, string text` |

---------

## Constructors

| Signature | Description |
| --- | --- |
| `QuadrantStepper()` | Creates a stepper with four default options (`"1"`, `"2"`, `"3"`, `"4"`). |
| `QuadrantStepper(IReadOnlyList<string> options)` | Creates a stepper with the provided option labels. |

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetOptions(IReadOnlyList<string> options)` | Replaces all segment labels. Resets selection to index 0. |
| `SetOptions(IReadOnlyList<string> options, int defaultIndex)` | Replaces all segment labels and sets the initial selection to `defaultIndex`. |
| `bool SetOptions(IReadOnlyList<string> options, string defaultText)` | Replaces labels and attempts to select the segment matching `defaultText`. Returns `true` if the text was found and selected. |
| `SetSelectedIndex(int index)` | Selects the segment at `index` with animation and fires `SelectionChanged`. |
| `SetSelectedIndex(int index, bool notify, bool animate)` | Selects the segment at `index` with optional event notification and animation. |
| `bool TrySetSelectedText(string text, bool notify, bool animate)` | Selects the segment whose label matches `text`. Returns `false` if not found. |
| `ForceUnselect()` | Removes the selection without firing `SelectionChanged`. The overlay is hidden. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Quadrant Stepper
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Quadrant Stepper Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions" editor-extension-mode="False">
    <ext:QuadrantStepper options="About,Goals,Settings,Done" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created in the Editor and in Play Mode, so no manual stylesheet reference is needed while authoring. The starter templates also reference the stylesheet explicitly, which covers player builds; for hand-written UXML or code-first UI in builds, add the stylesheet to your UXML or panel theme.

---------

## Using the Control

### Mode Switcher

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;
using System.Collections.Generic;

public class ModeController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;

    private QuadrantStepper _modeStepper;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;

        var modes = new List<string> { "Daily", "Weekly", "Monthly", "All Time" };
        _modeStepper = new QuadrantStepper(modes);

        // Default to "Weekly" without firing the event
        _modeStepper.SetOptions(modes, defaultIndex: 1);

        _modeStepper.SelectionChanged += (index, text) =>
        {
            Debug.Log($"Mode changed to [{index}] {text}");
            LoadData(text);
        };

        root.Q<VisualElement>("filterContainer").Add(_modeStepper);
    }

    private void LoadData(string period)
    {
        Debug.Log($"Loading data for period: {period}");
    }

    public void ResetToDefault()
    {
        // Restore to "Daily" silently, no animation
        _modeStepper.SetSelectedIndex(0, notify: false, animate: false);
    }
}
```

### Restoring Saved State

```csharp
// Restore selection from saved preference
string savedMode = PlayerPrefs.GetString("selectedMode", "Weekly");
bool found = _modeStepper.TrySetSelectedText(savedMode, notify: false, animate: false);
if (!found)
    _modeStepper.SetSelectedIndex(0, notify: false, animate: false);
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/QuadrantStepperDemo.jpg" aria-label="Quadrant Stepper demo">
  <source src="/uitoolkit/images/QuadrantStepperDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
