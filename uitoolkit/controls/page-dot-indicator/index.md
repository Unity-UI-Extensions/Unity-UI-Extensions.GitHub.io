---
layout: control-uitk
title: "Page Dot Indicator"
description: "Animated pagination dots that reflect the current page of a scroll view."
category: "Feedback"
permalink: /uitoolkit/controls/page-dot-indicator/
has_video: false
tags: [feedback, pagination, dots, indicator, scroll]
---

<!--![](/uitoolkit/images/PageDotIndicatorDemo.jpg)-->

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

`PageDotIndicator` renders a row of dot indicators that communicate the current position within a paged sequence. All dots up to and including `CurrentPage` are styled as completed. The dot list is rebuilt automatically when `TotalPages` changes. Colors can be overridden via USS custom properties or inline method calls.

Typical use cases:

- Onboarding flow page position dots
- Carousel or `ScrollSnap` position indicator
- Multi-step form or wizard step markers

---------

## Properties

| Name | Description | Options |
| --- | --- | --- |
| `CurrentPage` | Gets or sets the zero-based index of the current page. Updates dot completed state. | `int` |
| `TotalPages` | Gets or sets the total number of dots to render. Changing this value rebuilds all dot elements. | `int` |
| `NormalizedProgress` | Gets the current progress as a value in `[0, 1]`. Computed from `CurrentPage / max(TotalPages - 1, 1)`. | `float` (read-only) |

---------

## USS Classes

| Class | Description |
| --- | --- |
| `pageDotIndicator` | Root element. |
| `pageDotIndicator__dotsContainer` | Flex container that holds the individual dot elements. |
| `pageDotIndicator__dot` | Individual dot element. Fixed at 8 × 8 px with 4 px margin on each side. |
| `pageDotIndicator__dot--completed` | Modifier applied to every dot whose index is less than or equal to `CurrentPage`. |

---------

## Events

This control does not emit events.

---------

## Methods

| Signature | Description |
| --- | --- |
| `SetProgress(int currentPage, int totalPages)` | Sets both `CurrentPage` and `TotalPages` in one call. Rebuilds dots if `totalPages` changed. |
| `SetCompletedColor(string hex)` | Sets the background color of completed dots using a hex string (e.g. `"#e94560"`). |
| `SetPendingColor(string hex)` | Sets the background color of pending (not yet reached) dots using a hex string. |
| `SetColors(string completedHex, string pendingHex)` | Convenience method that sets both completed and pending colors in one call. |

---------

## Usage

> Add the control to your scene using:
>
> GameObject -> UI Toolkit -> Extensions -> Page Dot Indicator
>
> This creates a UIDocument in the scene (plus a PanelSettings with the default runtime theme, if the project has none) and assigns an editable starter template with demo content, copied to *Assets/UI Toolkit Extensions*.
>
> A starter template can also be added to an existing document using:
>
> Assets -> Create -> UI Toolkit -> Extensions -> Page Dot Indicator Starter

Alternatively, drag the control into a document from the UI Builder Library (*Project -> Custom Controls -> UnityUIToolkit.Extensions*) or declare it directly in UXML:

```xml
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:ext="UnityUIToolkit.Extensions" editor-extension-mode="False">
    <ext:PageDotIndicator current-page="1" total-pages="5" completed-color="#FFFFFF" pending-color="#44506A" />
</ui:UXML>
```

The shared extensions stylesheet is applied automatically when the control is created in the Editor and in Play Mode, so no manual stylesheet reference is needed while authoring. The starter templates also reference the stylesheet explicitly, which covers player builds; for hand-written UXML or code-first UI in builds, add the stylesheet to your UXML or panel theme.

---------

## Using the Control

### Syncing with ScrollSnap

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class OnboardingController : MonoBehaviour
{
    [SerializeField] private UIDocument _document;

    private ScrollSnap _scrollSnap;
    private PageDotIndicator _dotIndicator;

    private void OnEnable()
    {
        var root = _document.rootVisualElement;
        _scrollSnap = root.Q<ScrollSnap>("onboardingSnap");

        _dotIndicator = new PageDotIndicator();
        _dotIndicator.SetColors(completedHex: "#e94560", pendingHex: "#555555");
        _dotIndicator.SetProgress(currentPage: 0, totalPages: _scrollSnap.PageCount);

        root.Q<VisualElement>("footerContainer").Add(_dotIndicator);

        _scrollSnap.PageChanged += pageIndex =>
        {
            _dotIndicator.CurrentPage = pageIndex;
        };
    }
}
```

### Standalone Step Indicator

```csharp
// Set up a 5-step progress tracker, starting at step 2
_dotIndicator.SetProgress(currentPage: 2, totalPages: 5);

// Advance one step
_dotIndicator.CurrentPage++;

// Read normalized progress for use in other UI
float progress = _dotIndicator.NormalizedProgress; // 0.0 – 1.0
```

---------

## Video Demo

> Demo video coming soon.

<!--
<video class="demo-video" autoplay loop muted playsinline poster="/uitoolkit/images/PageDotIndicatorDemo.jpg" aria-label="Page Dot Indicator demo">
  <source src="/uitoolkit/images/PageDotIndicatorDemo.webm" type="video/webm">
</video>
-->

---------

## Credits and Donation

SimonDarksideJ

---------

## External links

[UI Toolkit Extensions repository](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions) | [OpenUPM package](https://openupm.com/packages/com.unity.uitoolkitextensions/)

---------
