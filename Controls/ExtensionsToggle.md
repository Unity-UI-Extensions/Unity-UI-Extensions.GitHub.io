# Extensions Toggle

An enhanced Toggle component with additional features including multiple event types and toggle group support.

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

The Extensions Toggle is an enhanced version of Unity's standard Toggle component. It extends the functionality with:

- **Unique Identification**: Each toggle can have a unique ID string for easy reference
- **Dual Event System**: Both `OnValueChanged` (bool) and `OnToggleChanged` (toggle reference) events
- **Enhanced Toggle Group**: Integrates seamlessly with the ExtensionsToggleGroup for managed toggle groups
- **Flexible Transitions**: Supports Color Tint, Sprite Swap, and Animation transitions
- **State Management**: Robust handling of on/off states with proper callback triggering

This component is ideal when you need more control over toggle behavior or require toggle group features beyond Unity's standard Toggle.

---------

## Properties

The properties of the Extensions Toggle control are as follows:

Property | Description
-|-
*Unique ID*|A string identifier for this toggle, useful for identifying which toggle was toggled in callbacks.
*Interactable*|Whether this toggle can be interacted with by the user.
*Toggle Transition*|How the toggle transitions between states: None or Fade.
*Graphic*|The graphic element to transition (typically a checkmark or indicator).
*Group*|The ExtensionsToggleGroup this toggle belongs to. Only one toggle in a group can be on at a time (if group allows).
*Is On*|Whether the toggle is currently in the on state.
*Toggle Transition*|The type of transition when toggling: None or Fade.
*Fade Duration*|How long the fade transition takes when Is On changes.
***On Value Changed*** (event)|Invoked when the toggle state changes, passes the new bool value.
***On Toggle Changed*** (event)|Invoked when the toggle state changes, passes a reference to the toggle itself.

### Additional properties available in code

Property | Return Type | Description
-|-|-
IsOn|bool|Get or set whether the toggle is currently on.
UniqueID|string|Get or set the unique identifier string.
Group|ExtensionsToggleGroup|Get or set the toggle group this toggle belongs to.

---------

## Methods

Method | Arguments | Description
-|-|-
*Set*|value (bool)|Set the toggle state without triggering callbacks.
*Set*|value (bool), sendCallback (bool)|Set the toggle state with optional callback triggering.
*OnPointerClick*|PointerEventData|Handles left mouse click to toggle.
*OnSubmit*|BaseEventData|Handles submission (Enter/Space key or gamepad button) to toggle.

---------

## Usage

Add the Extensions Toggle component to a GameObject:

"Add Component -> UI -> Extensions -> Extensions Toggle"

### Basic Toggle Setup

```csharp
public ExtensionsToggle toggle;

void Start()
{
    // Listen to toggle state changes
    toggle.onValueChanged.AddListener(OnToggleChanged);
}

void OnToggleChanged(bool isOn)
{
    Debug.Log("Toggle is " + (isOn ? "ON" : "OFF"));
}
```

### Using the Toggle with Unique ID

```csharp
public ExtensionsToggle toggle;

void Start()
{
    toggle.UniqueID = "sound_toggle";
    toggle.onToggleChanged.AddListener(OnToggleChanged);
}

void OnToggleChanged(ExtensionsToggle toggleThatChanged)
{
    if (toggleThatChanged.UniqueID == "sound_toggle")
    {
        AudioListener.pause = !toggleThatChanged.IsOn;
    }
}
```

### Using Toggle Groups

```csharp
public ExtensionsToggle option1, option2, option3;
public ExtensionsToggleGroup optionGroup;

void Start()
{
    // Assign toggles to the group
    option1.Group = optionGroup;
    option2.Group = optionGroup;
    option3.Group = optionGroup;
    
    // Only one toggle can be on at a time
    optionGroup.onToggleGroupChanged.AddListener(OnOptionSelected);
}

void OnOptionSelected(bool anyToggleOn)
{
    if (anyToggleOn)
    {
        var selected = optionGroup.SelectedToggle;
        Debug.Log("Selected option: " + selected.UniqueID);
    }
}
```

### Programmatic Toggle Control

```csharp
public ExtensionsToggle toggle;

void Update()
{
    if (Input.GetKeyDown(KeyCode.Space))
    {
        // Toggle the state
        toggle.IsOn = !toggle.IsOn;
    }
}
```

---------

## Video Demo

Coming soon...

---------

## See also

* [ExtensionsToggleGroup](/Controls/ExtensionsToggleGroup.md)
* [UIButton](/Controls/UIButton.md)
* [Selector](/Controls/Selector.md)

---------

## Credits and Donation

Unity UI Extensions Contributors

---------

## External links

[Unity Toggle Documentation](https://docs.unity3d.com/Manual/script-Toggle.html)
