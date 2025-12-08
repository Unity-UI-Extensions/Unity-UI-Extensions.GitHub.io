# UILineTextureRenderer

A line renderer with UV texture mapping and automatic end caps, supporting both absolute and relative sizing modes.

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

The UILineTextureRenderer draws lines between points with proper UV texture mapping, making it ideal for textured lines and trails. The component automatically adds end caps (24 pixels) to the line segments and supports both relative (scaled to RectTransform) and absolute sizing modes. UVs are configured for proper texture wrapping with left/center/right sections.

---------

## Properties

The properties of the UILineTextureRenderer control are as follows:

Property | Description
-|-
*UV Rect*|UV rectangle used by the texture (default: 0,0,1,1). Defines which portion of the texture to map
*Line Thickness*|Thickness of the drawn line in pixels (default: 2)
*Use Margins*|When enabled, applies margin offsets to the drawing area
*Margin*|Margin offset in pixels (Vector2) applied when Use Margins is enabled
*Relative Size*|When enabled, scales points relative to RectTransform dimensions. When disabled, uses absolute 1:1 scale
*Points*|Array of Vector2 points to draw lines between

Additional properties available in code:

Property | Return Type | Description
|-|-|-|
|uvRect|Rect|Gets or sets the UV rectangle. Setter marks vertices dirty
|Points|Vector2[]|Gets or sets the points array. Setter marks all dirty

---------

## Methods

The UILineTextureRenderer control does not expose public methods beyond the property setters.

---------

## Usage

To use the UILineTextureRenderer primitive:

1. Add the component via "**Add Component -> UI -> Extensions -> Primitives -> UILineTextureRenderer**"
2. Assign a texture/sprite to the Image component (if using a texture)
3. Set the Points array with Vector2 positions (requires at least 2 points)
4. Configure Line Thickness and UV Rect as needed
5. Toggle Relative Size: enabled scales to RectTransform, disabled uses absolute positioning
6. Optionally enable Use Margins and set Margin for offset adjustments

Example code for runtime line creation:

```csharp
using UnityEngine.UI.Extensions;

public class TexturedLineExample : MonoBehaviour
{
    public UILineTextureRenderer lineRenderer;

    void Start()
    {
        // Create a simple line
        lineRenderer.Points = new Vector2[]
        {
            new Vector2(0.1f, 0.1f),
            new Vector2(0.5f, 0.8f),
            new Vector2(0.9f, 0.2f)
        };
        
        lineRenderer.LineThickness = 5f;
        lineRenderer.relativeSize = true;
        lineRenderer.uvRect = new Rect(0, 0, 1, 1);
    }
    
    void DrawPath(Vector2[] pathPoints)
    {
        lineRenderer.Points = pathPoints;
    }
    
    void SetCustomUVMapping()
    {
        // Use only part of the texture
        lineRenderer.uvRect = new Rect(0.25f, 0.25f, 0.5f, 0.5f);
    }
}
```

**Note**: The component automatically adds 24-pixel caps to the start and end of the line. If fewer than 2 points are provided, it defaults to a simple diagonal line from (0,0) to (1,1).

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [UILineRenderer](UILineRenderer.md) - Standard line renderer without texture mapping
* [UILineRendererFIFO](UILineRendererFIFO.md) - FIFO-based line renderer for trails
* [BezierLineRenderer](BezierLineRenderer.md) - Curved line renderer

---------

## Credits and Donation

Credits: jonbro5556  
Based on original LineRender script by jack.sydorenko

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/new-ui-and-line-drawing.253772/)
