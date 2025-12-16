# Segment

An individual segment component that acts as a button within a SegmentedControl group. Handles pointer events and selection state for segmented controls.

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

The Segment component is a child element of a SegmentedControl that represents a single selectable option within the control group. Each segment acts as a button and manages its own selection state, visual transitions, and interaction with the parent SegmentedControl.

Segments handle various input methods including pointer clicks, keyboard navigation, and gamepad input. They automatically update their visual appearance based on selection state and support color tint, sprite swap, and animation transitions.

---------

## Properties

The properties of the Segment control are as follows:

Property | Description
-|-
*Interactable*|Whether this segment can be selected or interacted with.
*Transition*|How the segment transitions between selected and unselected states (None, ColorTint, SpriteSwap, or Animation).
*Target Graphic*|The graphic element that will be visually transitioned when the segment is selected.
*Normal Color*|Color when the segment is not selected.
*Highlighted Color*|Color when the segment is highlighted (hovered).
*Pressed Color*|Color when the segment is selected/pressed.
*Disabled Color*|Color when the segment is disabled.
*Color Multiplier*|Multiplier applied to all colors.
*Fade Duration*|How long the color transition takes.
*Sprite State*|Sprites to use for normal, highlighted, pressed, and disabled states.
*Animation Triggers*|Animation parameters for different states.

---------

## Methods

Method | Arguments | Description
-|-|-
*OnPointerClick*|PointerEventData|Handles left mouse click to select this segment.
*OnPointerEnter*|PointerEventData|Handles mouse entering the segment area.
*OnPointerExit*|PointerEventData|Handles mouse leaving the segment area.
*OnPointerDown*|PointerEventData|Handles mouse button press.
*OnPointerUp*|PointerEventData|Handles mouse button release.
*OnSelect*|BaseEventData|Handles UI selection via keyboard/gamepad.
*OnDeselect*|BaseEventData|Handles UI deselection via keyboard/gamepad.
*OnSubmit*|BaseEventData|Handles submission (Enter key/gamepad button) to select this segment.

---------

## Usage

Segment components are automatically created as children of a SegmentedControl and should not be added manually to the scene. To use segmented controls in your UI:

Add the SegmentedControl component to a GameObject:
"Add Component -> UI -> Extensions -> Segmented Control/SegmentedControl"

Or alternatively, use the prefab:
"GameObject -> UI -> Extensions -> Segmented Control"

This will create the SegmentedControl with initial segment children automatically.

To access segments in code:

```csharp
public SegmentedControl segmentedControl;

void Start()
{
    segmentedControl = GetComponent<SegmentedControl>();
    // Access individual segments through the SegmentedControl
    Segment firstSegment = segmentedControl.segments[0];
    
    // Listen to selection changes
    segmentedControl.onValueChanged.AddListener(OnSegmentSelected);
}

void OnSegmentSelected(int segmentIndex)
{
    Debug.Log("Segment " + segmentIndex + " selected");
}
```

---------

## Video Demo

Coming soon...

---------

## See also

* [SegmentedControl](/Controls/SegmentedControl.md)
* [UIButton](/Controls/UIButton.md)
* [SelectableScaler](/Controls/SelectableScaler.md)

---------

## Credits and Donation

David Gileadi

---------

## External links

[Sourced from](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/pull-requests/12)
