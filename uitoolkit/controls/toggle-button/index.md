---
layout: control-uitk
title: "Toggle Button"
description: "Flat toggle switch with animated indicator and on/off label support."
category: "Forms"
permalink: /uitoolkit/controls/toggle-button/
has_video: false
tags: [forms, toggle, switch, button, boolean]
---

<!--![](/uitoolkit/images/ToggleButtonDemo.jpg)-->

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

`ToggleButton` is a simple image button that toggles its selected state on every pointer-down event. `OnClicked` fires on every press regardless of the resulting state, making it straightforward to react to both selection and deselection in a single handler. Use `ForceSelect` and `ForceDeselect` to set state programmatically without firing the event.

Typical use cases:

- Audio mute / unmute toggle
- Dark mode / light mode switch
- Any binary feature toggle with icon feedback

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `IsSelected` | Gets or sets the current selected state. Setting this directly applies or removes the `--selected` modifier but does not fire `OnClicked`. | `bool` |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `toggleButton` | Root element. |
| `toggleButton__image` | The image element. 100% width and height, `scale-to-fit` background. |
| `toggleButton--selected` | Modifier applied when `IsSelected` is `true`. Use in USS to swap icon or apply tint. |

---------

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `OnClicked` | Fired on every pointer-down event, before the state is toggled. The new `IsSelected` value is already reflected when the handler runs. | none |

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetImage(Texture2D texture)` | Sets the background texture of the image element. |
| `ForceSelect()` | Sets `IsSelected = true` and applies `--selected` without firing `OnClicked`. |
| `ForceDeselect()` | Sets `IsSelected = false` and removes `--selected` without firing `OnClicked`. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Toggle Button
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Toggle Button Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions">
    <ext:ToggleButton />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created, so no manual stylesheet reference is required.

---------

## Using the Control

### Audio Toggle

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class AudioToggleController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;
    [SerializeField] private Texture2D _audioOnIcon;
    [SerializeField] private Texture2D _audioOffIcon;

    private ToggleButton _audioToggle;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;

        _audioToggle = new ToggleButton();
        _audioToggle.SetImage(_audioOnIcon);

        // Restore saved preference silently
        bool isMuted = PlayerPrefs.GetInt("AudioMuted", 0) == 1;
        if (isMuted)
            _audioToggle.ForceSelect();

        _audioToggle.OnClicked += OnAudioToggled;
        root.Q<VisualElement>("toolbarContainer").Add(_audioToggle);
    }

    private void OnAudioToggled()
    {
        bool isMuted = _audioToggle.IsSelected;
        AudioListener.volume = isMuted ? 0f : 1f;
        PlayerPrefs.SetInt("AudioMuted", isMuted ? 1 : 0);

        // Swap icon based on new state
        _audioToggle.SetImage(isMuted ? _audioOffIcon : _audioOnIcon);
        Debug.Log($"Audio {(isMuted ? "muted" : "unmuted")}");
    }
}
```

### USS Icon Swap via Modifier

Rather than swapping the texture in code you can declare both icon states in USS:

```uss
.toggleButton__image {
    background-image: url("audio-on.png");
}

.toggleButton--selected .toggleButton__image {
    background-image: url("audio-off.png");
}
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/ToggleButtonDemo.jpg" aria-label="Toggle Button demo">
  <source src="/uitoolkit/images/ToggleButtonDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
