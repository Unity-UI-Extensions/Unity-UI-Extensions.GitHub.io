# UICircle

A customizable circle/arc primitive with progress indication, fill modes, and extensive runtime control options.

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

The UICircle primitive renders customizable circles and arcs with optional fill modes. It supports progress indication (useful for loading circles/health bars), arc construction with configurable segments, rotation, thickness control, and padding. The component efficiently uses vertex streams and maps UVs for sprite/texture rendering.

---------

## Properties

The properties of the UICircle control are as follows:

Property | Description
-|-
*Arc Invert*|Inverts the construction direction of the arc (default: true)
*Arc*|Percentage of the entire circumference to draw, from 0 to 1 (default: 1 = full circle)
*Arc Steps*|Number of segments the arc is divided into, from 0 to 1000 (default: 100). Higher values = smoother curves
*Arc Rotation*|Rotation of the geometry around the Z axis in degrees, from 0 to 360 (default: 0)
*Progress*|Progress indicator value from 0 to 1, colors the arc with ProgressColor up to this point (default: 0)
*Progress Color*|Color used for the progress portion of the arc (default: white)
*Fill*|Whether to draw a solid filled circle (true) or hollow ring (false) (default: true)
*Thickness*|Thickness of the ring when Fill is false (default: 5)
*Padding*|Padding applied to the circle diameter (default: 0)

---------

## Methods

Method | Arguments | Description
-|-|-
*SetProgress*|float progress|Sets the progress value (0-1) and updates the mesh
*SetArc*|float arc|Sets the arc percentage (0-1) and updates the mesh
*SetArcSteps*|int steps|Sets the number of arc segments and updates the mesh
*SetInvertArc*|bool invert|Sets whether the arc construction is inverted and updates the mesh
*SetArcRotation*|int rotation|Sets the arc rotation in degrees and updates the mesh
*SetFill*|bool fill|Sets whether the circle is filled or hollow and updates the mesh
*SetBaseColor*|Color color|Sets the base color of the circle and updates the mesh
*UpdateBaseAlpha*|float value|Updates only the alpha channel of the base color and updates the mesh
*SetProgressColor*|Color color|Sets the progress color and updates the mesh
*UpdateProgressAlpha*|float value|Updates only the alpha channel of the progress color and updates the mesh
*SetPadding*|int padding|Sets the padding and updates the mesh
*SetThickness*|int thickness|Sets the thickness (for hollow circles) and updates the mesh

---------

## Usage

To use the UICircle primitive:

1. Add the component via "**Add Component -> UI -> Extensions -> Primitives -> UI Circle**"
2. Configure the arc percentage, steps, and rotation to define the circle shape
3. Enable Fill for a solid circle or disable it and set Thickness for a ring
4. Use Progress and Progress Color for progress indicators
5. Adjust Padding to fit within the RectTransform bounds

Example code for runtime control:

```csharp
using UnityEngine.UI.Extensions;

public class CircleProgressExample : MonoBehaviour
{
    public UICircle progressCircle;

    void Start()
    {
        // Configure as a progress ring
        progressCircle.SetFill(false);
        progressCircle.SetThickness(10);
        progressCircle.SetArc(1f);  // Full circle
        progressCircle.SetBaseColor(Color.gray);
        progressCircle.SetProgressColor(Color.green);
    }
    
    void UpdateProgress(float progress)
    {
        // Update progress from 0 to 1
        progressCircle.SetProgress(progress);
    }
    
    void CreateArc()
    {
        // Create a 270-degree arc rotated 45 degrees
        progressCircle.SetArc(0.75f);
        progressCircle.SetArcRotation(45);
        progressCircle.SetArcSteps(100);
    }
}
```

**Note**: Moving the pivot from center or having a RectTransform smaller than Thickness/Padding can cause unexpected behavior. Test multiple aspect ratios when designing layouts.

---------

## Video Demo

*Video demonstration to be added*

Sample scene: `UICircleProgress`

---------

## See also

* [UILineRenderer](UILineRenderer.md) - Draw custom lines
* [UIPolygon](UIPolygon.md) - Draw custom polygons

---------

## Credits and Donation

Credits: zge, jeremie sellam, tswalker  
Updated from - https://bitbucket.org/tswalker/

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/draw-circles-or-primitives-on-the-new-ui-canvas.272488/#post-2293224)  
[Updated from](https://bitbucket.org/SimonDarksideJ/unity-ui-extensions/issues/65/a-better-uicircle)
