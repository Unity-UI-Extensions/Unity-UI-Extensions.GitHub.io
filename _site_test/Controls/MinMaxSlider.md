# MinMaxSlider

A dual-handle slider control for selecting a range of values between minimum and maximum bounds, with optional TextMeshPro display and event callbacks.

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

The MinMaxSlider control provides a dual-handle slider for selecting a range within defined limits. Users can drag either handle independently to adjust the min/max values, or drag the middle area to move both handles together. It supports optional TextMeshPro text displays for showing current values and includes whole number mode for integer-only values.

---------

## Properties

The properties of the MinMaxSlider control are as follows:

Property | Description
-|-
*Custom Camera*|Optional camera to use for input detection. If not set, uses Camera.main
*Slider Bounds*|RectTransform defining the bounds of the slider. Defaults to the component's RectTransform if not set
*Min Handle*|RectTransform for the minimum value handle
*Max Handle*|RectTransform for the maximum value handle
*Middle Graphic*|RectTransform for the visual element displayed between the two handles
*Min Text*|Optional TextMeshProUGUI component to display the current minimum value
*Max Text*|Optional TextMeshProUGUI component to display the current maximum value
*Text Format*|String format for displaying numeric values (default "0"). Use formats like "0.00" for decimals
*Min Limit*|The minimum possible value of the slider range (default 0)
*Max Limit*|The maximum possible value of the slider range (default 100)
*Whole Numbers*|When enabled, slider values snap to whole numbers (integers only)
*Min Value*|The current minimum value selected on the slider (default 25)
*Max Value*|The current maximum value selected on the slider (default 75)
***On Value Changed*** (event)|Event invoked when either slider value changes. Passes min and max values as float parameters

Additional properties available in code:

Property | Return Type | Description
-|-|-
|Values|MinMaxValues|Returns a MinMaxValues struct containing minValue, maxValue, minLimit, and maxLimit
|SliderBounds|RectTransform|Gets or sets the slider bounds RectTransform
|MinHandle|RectTransform|Gets or sets the minimum handle RectTransform
|MaxHandle|RectTransform|Gets or sets the maximum handle RectTransform
|MiddleGraphic|RectTransform|Gets or sets the middle graphic RectTransform
|MinText|TextMeshProUGUI|Gets or sets the minimum value text component
|MaxText|TextMeshProUGUI|Gets or sets the maximum value text component

---------

## Methods

Method | Arguments | Description
-|-|-
*SetLimits*|float minLimit, float maxLimit|Sets the minimum and maximum limits for the slider range. Values are rounded if wholeNumbers is enabled
*SetValues* (overload 1)|MinMaxValues values, bool notify = true|Sets all slider values using a MinMaxValues struct. If notify is true, triggers the onValueChanged event
*SetValues* (overload 2)|float minValue, float maxValue, bool notify = true|Sets the current min/max values while keeping existing limits. If notify is true, triggers the onValueChanged event
*SetValues* (overload 3)|float minValue, float maxValue, float minLimit, float maxLimit, bool notify = true|Sets all slider values and limits. If notify is true, triggers the onValueChanged event

---------

## Usage

To use the MinMaxSlider control:

1. Add the component via "**Add Component -> UI -> Extensions -> Sliders -> MinMax Slider**"
2. Assign RectTransforms for Min Handle, Max Handle, and optionally Middle Graphic and Slider Bounds
3. Optionally assign TextMeshProUGUI components for Min Text and Max Text to display current values
4. Configure Min Limit, Max Limit, Min Value, and Max Value in the inspector
5. Subscribe to the OnValueChanged event to respond to slider changes

Example code for programmatic usage:

```csharp
using UnityEngine.UI.Extensions;

public class MinMaxSliderExample : MonoBehaviour
{
    public MinMaxSlider slider;

    void Start()
    {
        // Set slider limits to 0-1000
        slider.SetLimits(0f, 1000f);
        
        // Set initial values to 200-800
        slider.SetValues(200f, 800f);
        
        // Subscribe to value changes
        slider.onValueChanged.AddListener(OnSliderValueChanged);
    }
    
    void OnSliderValueChanged(float minValue, float maxValue)
    {
        Debug.Log($"Range selected: {minValue} to {maxValue}");
    }
    
    void UpdateRange()
    {
        // Get current values
        var values = slider.Values;
        Debug.Log($"Current range: {values.minValue}-{values.maxValue} (limits: {values.minLimit}-{values.maxLimit})");
    }
}
```

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [RangeSlider](RangeSlider.md) - Alternative range slider implementation
* [BoxSlider](BoxSlider.md) - Two-dimensional slider control
* [RadialSlider](RadialSlider.md) - Circular slider control

---------

## Credits and Donation

Credits: brogan89

---------

## External links

[Sourced from](https://github.com/brogan89/MinMaxSlider)
