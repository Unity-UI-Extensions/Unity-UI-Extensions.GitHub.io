---
layout: control-uitk
title: "Dropdown"
description: "Wheel-style dropdown picker that opens a touch-friendly modal list for single-value selection."
category: "Forms"
permalink: /uitoolkit/controls/dropdown/
has_video: false
tags: [forms, dropdown, picker, wheel, modal, select]
---

## Summary

`DropDownControl` is a wheel-style dropdown picker that opens from an inline trigger and lets the user confirm a single value from a vertically scrollable modal list. The list behaves like a native mobile drum picker — drag to scroll with momentum coasting, flick to spin, and tap to confirm. A full-screen backdrop closes the modal on outside tap.

Typical use cases:

- Dial-code or country-code selection before a phone field
- Compact selectors that need a touch-friendly modal confirmation step
- Any workflow where a finite string list should feel like a native mobile picker rather than a standard dropdown menu

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `Items` | `IReadOnlyList<string>` | Ordered values shown in the picker. Updating the list refreshes the trigger label and the open list content. |
| `Value` | `string` | The currently selected value, or an empty string when `Items` is empty. Read-only. |

## USS Classes

| Class | Description |
| --- | --- |
| `dropDownControl` | Root element for the control. |
| `dropDownControl__trigger` | Closed-state trigger pill. Tap to open the modal picker. |
| `dropDownControl__triggerLabel` | Label showing the current selection inside the trigger. |
| `dropDownControl__triggerIcon` | Chevron icon inside the trigger. |
| `dropDownControl__backdrop` | Full-screen backdrop injected while the picker is open. Tap to dismiss. |
| `dropDownControl__panel` | Floating modal panel that contains the picker list. |
| `dropDownControl__viewport` | Clipped viewport used to display the visible rows. |
| `dropDownControl__list` | Scrolling row container translated by the control logic. |
| `dropDownControl__row` | A single rendered picker row. |
| `dropDownControl__selectionLane` | Highlight lane showing the centred, confirmed selection. |
| `dropDownControl__fadeTop` | Top gradient overlay that de-emphasises off-centre rows. |
| `dropDownControl__fadeBottom` | Bottom gradient overlay that de-emphasises off-centre rows. |
| `dropDownControl--open` | Root modifier applied while the modal picker is visible. |

## Events

| Name | Description | Arguments |
| --- | --- | --- |
| `ValueChanged` | Fired after the user confirms a new selection by tapping the centred row. | `string selectedValue` |
| `OpenStateChanged` | Fired when the modal picker opens or closes. | `bool isOpen` |

## Public Methods

| Signature | Description |
| --- | --- |
| `SetDefault(string value)` | Pre-selects the item matching the supplied value. No-op if the value is not present in `Items`. |

## Using the Control

### Dial-code Picker

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using UnityUIToolkit.Extensions;

public class PhoneEntryController : MonoBehaviour
{
    [SerializeField] private UIDocument document;

    private DropDownControl _dialCodePicker;

    private void OnEnable()
    {
        var root = document.rootVisualElement;

        _dialCodePicker = root.Q<DropDownControl>("dial-code-picker");
        _dialCodePicker.Items = new[] { "+1", "+33", "+34", "+44", "+49", "+61", "+81", "+91" };
        _dialCodePicker.SetDefault("+44");

        _dialCodePicker.ValueChanged      += OnDialCodeChanged;
        _dialCodePicker.OpenStateChanged  += OnPickerOpenStateChanged;
    }

    private void OnDialCodeChanged(string value)
    {
        Debug.Log($"Dial code selected: {value}");
    }

    private void OnPickerOpenStateChanged(bool isOpen)
    {
        // Hide/show surrounding UI while the modal is visible
        _someOtherPanel.SetEnabled(!isOpen);
    }
}
```

### Creating in Code

```csharp
var picker = new DropDownControl
{
    Items = new[] { "+1", "+33", "+44", "+49" },
};

picker.SetDefault("+44");
picker.ValueChanged += selected => Debug.Log($"Selected {selected}");

root.Add(picker);
```

### Swapping Options at Runtime

```csharp
// Refresh the list when the user changes region
private void OnRegionChanged(string region)
{
    _dialCodePicker.Items = RegionDatabase.GetDialCodesForRegion(region);
}
```
