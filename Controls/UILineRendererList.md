# UILineRendererList

An advanced line renderer for drawing multiple connected line segments with features including bezier curves, join types (bevel/miter), and line caps.

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

UILineRendererList is an advanced primitive that renders multiple connected line segments with customizable styling options. It extends the basic line rendering capabilities with support for:

- **Bezier Curves**: Optional smoothing of line segments using various Bezier interpolation methods
- **Join Types**: Control how line segments connect with bevel (curved) or miter (sharp) joins
- **Line Caps**: Add end caps to each line segment
- **Line List Mode**: Draw disconnected pairs of lines instead of a continuous path
- **Configurable Thickness**: Adjust line thickness dynamically

This is a more feature-rich alternative to UILineRenderer for complex line drawings.

---------

## Properties

The properties of the UILineRendererList control are as follows:

Property | Description
-|-
*Points*|List of points to draw lines between. Can be improved using the Resolution option.
*Line Thickness*|Thickness of the drawn line in pixels.
*Relative Size*|When true, points use normalized coordinates (0,0 -> 1,1) relative to the RectTransform. When false, uses screen-space coordinates.
*Line List*|When true, points are treated as pairs of disconnected lines. When false, points form a continuous path.
*Line Caps*|Whether to add end caps (circles) at the start and end of each line.
*Bezier Segments Per Curve*|Number of segments to generate per bezier curve for smoothing. Only used when Bezier Mode is not None.
*Line Joins*|The type of join between line segments: Bevel (curved) or Miter (sharp angular).
*Bezier Mode*|The type of Bezier smoothing to apply: None, Quick, Basic, Improved, or Catenary. Cannot be used with manual Resolution setting.
*Driven Externally*|When true, allows external code to drive the rendering without updating from properties.

### Additional properties available in code

Property | Return Type | Description
-|-|-
LineThickness|float|Get or set the line thickness, automatically marks for redraw.
RelativeSize|bool|Get or set whether points are relative or screen-space.
LineList|bool|Get or set whether lines are connected or as pairs.
LineCaps|bool|Get or set whether line caps are drawn.
BezierSegmentsPerCurve|int|Get or set the bezier resolution.

---------

## Methods

Method | Arguments | Description
-|-|-
*SetAllDirty*|N/A|Marks the graphic as dirty and requires a full redraw.
*OnPopulateMesh*|VertexHelper|Internal method that populates the mesh data for rendering.

---------

## Usage

Add the UILineRendererList component to a RectTransform in your UI hierarchy:

"Add Component -> UI -> Extensions -> Primitives -> UILineRendererList"

Then configure the line points and drawing options in the inspector.

Basic usage example:

```csharp
public UILineRendererList lineRenderer;

void Start()
{
    // Create points for the line
    List<Vector2> points = new List<Vector2>
    {
        Vector2.zero,           // Start point
        new Vector2(100, 50),   // Middle point
        new Vector2(200, 0)     // End point
    };
    
    lineRenderer.Points = points;
    lineRenderer.LineThickness = 5f;
}
```

### Drawing with Bezier Curves

To smooth line segments with Bezier interpolation:

```csharp
lineRenderer.BezierMode = UILineRendererList.BezierType.Improved;
lineRenderer.BezierSegmentsPerCurve = 20;
```

### Line Joins and Caps

Configure how segments connect:

```csharp
lineRenderer.LineJoins = UILineRendererList.JoinType.Bevel;  // Curved joins
lineRenderer.LineCaps = true;  // Add end caps
```

---------

## Video Demo

Coming soon...

---------

## See also

* [UILineRenderer](/Controls/UILineRenderer.md)
* [UILineRendererFIFO](/Controls/UILineRendererFIFO.md)
* [UILineTextureRenderer](/Controls/UILineTextureRenderer.md)
* [UILineConnector](/Controls/UILineConnector.md)

---------

## Credits and Donation

jack.sydorenko, firagon

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/new-ui-and-line-drawing.253772/)
[Updated/Refactored from](http://forum.unity3d.com/threads/new-ui-and-line-drawing.253772/#post-2528050)
