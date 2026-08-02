---
layout: control-uitk
title: "Icon Label Button"
description: "Horizontal row button combining a left-side icon with label and subtitle text."
category: "Primitives"
permalink: /uitoolkit/controls/icon-label-button/
has_video: false
tags: [primitives, button, icon, label, row]
---

<!--![](/uitoolkit/images/IconLabelButtonDemo.jpg)-->

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

`IconLabelButton` is a full-width row button that pairs a 24 × 24 px icon on the left with a text label. It provides hover and pressed state modifier classes for visual feedback without custom USS.

Typical use cases:

- Menu and navigation row items
- Action list rows (share, delete, report, etc.)
- Settings list entries with a leading icon

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `Text` | Gets or sets the button label text. | `string` |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `iconLabelButton` | Root element. Full-width flex row. |
| `iconLabelButton__button` | Inner button element that wraps icon and label. |
| `iconLabelButton__icon` | Icon element. Fixed at 24 × 24 px. |
| `iconLabelButton__label` | Text label element next to the icon. |
| `iconLabelButton--hover` | Modifier applied on pointer-enter. |
| `iconLabelButton--pressed` | Modifier applied while pointer is held down. |

---------

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `Clicked` | Fired when the button is tapped or clicked. | none |

---------

## Methods

No public methods beyond property access. Use the `Text` property and USS to configure the control.

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Icon Label Button
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Icon Label Button Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions">
    <ext:IconLabelButton text="Click Me!" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created, so no manual stylesheet reference is required.

---------

## Using the Control

### Navigation Menu

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class SideMenuController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;
    [SerializeField] private Texture2D _homeIcon;
    [SerializeField] private Texture2D _profileIcon;
    [SerializeField] private Texture2D _settingsIcon;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;
        var menu = root.Q<VisualElement>("sideMenu");

        menu.Add(CreateMenuRow("Home", _homeIcon, () => NavigateTo("home")));
        menu.Add(CreateMenuRow("Profile", _profileIcon, () => NavigateTo("profile")));
        menu.Add(CreateMenuRow("Settings", _settingsIcon, () => NavigateTo("settings")));
    }

    private IconLabelButton CreateMenuRow(string label, Texture2D icon, System.Action onClicked)
    {
        var btn = new IconLabelButton();
        btn.Text = label;

        // Query by class name (first arg is element name — pass null; second is class name)
        var iconEl = btn.Q(null, IconLabelButton.IconClass);
        if (iconEl != null)
            iconEl.style.backgroundImage = new StyleBackground(icon);

        btn.Clicked += onClicked;
        return btn;
    }

    private void NavigateTo(string screen)
    {
        Debug.Log($"Navigating to: {screen}");
    }
}
```

### USS Customization

Override hover and pressed states in your project USS:

```uss
.iconLabelButton--hover {
    background-color: rgba(255, 255, 255, 0.06);
}

.iconLabelButton--pressed {
    background-color: rgba(255, 255, 255, 0.12);
}
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/IconLabelButtonDemo.jpg" aria-label="Icon Label Button demo">
  <source src="/uitoolkit/images/IconLabelButtonDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
