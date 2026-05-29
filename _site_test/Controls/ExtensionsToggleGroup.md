# Extensions Toggle Group

An enhanced ToggleGroup component that manages a group of ExtensionsToggle components, ensuring only one toggle is active at a time.

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Properties](#properties)
>
> 3 [Methods](#methods)
>
> 4 [Usage](#usage)
>
> 5 [Video Demo](#video-demo)
>
> 6 [See also](#see-also)
>
> 7 [Credits and Donation](#credits-and-donation)
>
> 8 [External links](#external-links)

---------

## Overview

The Extensions Toggle Group is an enhanced version of Unity's standard ToggleGroup that manages ExtensionsToggle components. It ensures that only one toggle in the group can be on at a time (unless `AllowSwitchOff` is enabled) and provides events for monitoring group state changes.

Key features include:

- **Enforced Single Selection**: Only one toggle can be selected at a time
- **Optional Multi-Off Mode**: When enabled, all toggles can be off
- **Dual Event System**: Separate events for group state changes and individual toggle changes
- **Active Toggles Enumeration**: Access all currently active toggles in the group
- **Programmatic Control**: Methods to query and control toggle states

---------

## Properties

The properties of the Extensions Toggle Group control are as follows:

Property | Description
-|-
*Allow Switch Off*|When true, allows all toggles in the group to be off. When false, at least one toggle must be on.
***On Toggle Group Changed*** (event)|Invoked when any toggle in the group changes state, passes whether any toggles are on.
***On Toggle Group Toggle Changed*** (event)|Invoked when a toggle in the group changes, passes the new boolean state.

### Additional properties available in code

Property | Return Type | Description
-|-|-
AllowSwitchOff|bool|Get or set whether all toggles can be off.
SelectedToggle|ExtensionsToggle|Get the currently selected toggle, or null if none selected.

---------

## Methods

Method | Arguments | Description
-|-|-
*NotifyToggleOn*|toggle (ExtensionsToggle)|Internally called when a toggle becomes on. Turns off all other toggles in the group.
*RegisterToggle*|toggle (ExtensionsToggle)|Register an ExtensionsToggle to be managed by this group.
*UnregisterToggle*|toggle (ExtensionsToggle)|Unregister an ExtensionsToggle from this group.
*AnyTogglesOn*|N/A|Returns true if at least one toggle in the group is on.
*ActiveToggles*|N/A|Returns an enumerable collection of all toggles that are currently on.
*SetAllTogglesOff*|N/A|Turns off all toggles in the group.

---------

## Usage

Add the Extensions Toggle Group component to a GameObject, typically the parent of the toggles:

"Add Component -> UI -> Extensions -> Extensions Toggle Group"

### Basic Group Setup

```csharp
public ExtensionsToggleGroup toggleGroup;
public ExtensionsToggle[] toggles;

void Start()
{
    // The toggles should have their Group property set to this group
    // This can be done in the inspector or programmatically:
    foreach (var toggle in toggles)
    {
        toggle.Group = toggleGroup;
    }
    
    // Listen to group changes
    toggleGroup.onToggleGroupChanged.AddListener(OnGroupChanged);
}

void OnGroupChanged(bool anyToggleOn)
{
    Debug.Log("Any toggle on: " + anyToggleOn);
}
```

### Accessing the Selected Toggle

```csharp
public ExtensionsToggleGroup toggleGroup;

void Update()
{
    if (Input.GetKeyDown(KeyCode.E))
    {
        var selected = toggleGroup.SelectedToggle;
        if (selected != null)
        {
            Debug.Log("Currently selected: " + selected.UniqueID);
        }
    }
}
```

### Allowing Multiple Off State

```csharp
public ExtensionsToggleGroup toggleGroup;

void Start()
{
    // Allow all toggles to be off
    toggleGroup.AllowSwitchOff = true;
    
    // Now users can click the selected toggle again to deselect it
}
```

### Querying Active Toggles

```csharp
public ExtensionsToggleGroup toggleGroup;

void CheckActiveToggles()
{
    var activeToggles = toggleGroup.ActiveToggles();
    foreach (var toggle in activeToggles)
    {
        Debug.Log("Active toggle: " + toggle.UniqueID);
    }
}
```

### Controlling Toggles Programmatically

```csharp
public ExtensionsToggleGroup toggleGroup;
public ExtensionsToggle[] optionToggles;

void SelectOption(int index)
{
    if (index >= 0 && index < optionToggles.Length)
    {
        optionToggles[index].IsOn = true;
        // Other toggles in the group will automatically turn off
    }
}

void DeselectAll()
{
    if (toggleGroup.AllowSwitchOff)
    {
        toggleGroup.SetAllTogglesOff();
    }
}
```

---------

## Video Demo

Coming soon...

---------

## See also

* [ExtensionsToggle](/Controls/ExtensionsToggle.md)
* [UIButton](/Controls/UIButton.md)
* [SegmentedControl](/Controls/SegmentedControl.md)

---------

## Credits and Donation

Unity UI Extensions Contributors

---------

## External links

[Unity ToggleGroup Documentation](https://docs.unity3d.com/Manual/script-ToggleGroup.html)
