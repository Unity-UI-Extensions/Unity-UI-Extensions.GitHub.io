# UILineRendererFIFO

A performance-optimized line renderer that uses a first-in-first-out (FIFO) queue for adding and removing points, ideal for drawing dynamic trails or graphs.

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

The UILineRendererFIFO is a refactored and performance-optimized version of UILineRenderer that uses FIFO (first-in-first-out) queue logic. Points are added to the head of the queue and removed from the tail, making it ideal for applications like scrolling graphs, dynamic trails, or real-time data visualization. The component efficiently manages vertex buffers by only rebuilding segments for newly added points.

---------

## Properties

The properties of the UILineRendererFIFO control are as follows:

Property | Description
-|-
*Line Thickness*|Thickness of the drawn line in pixels (default: 1)
*Points*|List of Vector2 points to draw lines between. Can be improved using the Resolution Option from base class

Additional properties available in code:

Property | Return Type | Description
|-|-|-|
|LineThickness|float|Gets or sets the line thickness. Setter marks the component dirty
|Points|List<Vector2>|Gets or sets the points list. Should not be modified directly—use Add/Remove methods instead

---------

## Methods

Method | Arguments | Description
-|-|-
*AddPoint*|Vector2 point|Adds a point to the head of the queue. New points are drawn on the next mesh update
*RemovePoint*|(none)|Removes a point from the tail (FIFO). Triggers a full mesh resize on next update
*ClearPoints*|(none)|Clears all points, segments, and resets the internal state
*Resize*|(none)|Forces a full mesh resize/rebuild on the next update

---------

## Usage

To use the UILineRendererFIFO primitive:

1. Add the component via "**Add Component -> UI -> Extensions -> Primitives -> UILineRendererFIFO**"
2. Set the Line Thickness to control line width
3. Use AddPoint() to add points dynamically at runtime
4. Use RemovePoint() to remove the oldest point (FIFO behavior)
5. The component automatically optimizes rendering by only updating newly added geometry

Example code for dynamic line drawing:

```csharp
using UnityEngine.UI.Extensions;
using System.Collections;

public class FIFOLineExample : MonoBehaviour
{
    public UILineRendererFIFO lineRenderer;
    public int maxPoints = 100;

    void Start()
    {
        lineRenderer.LineThickness = 2f;
        lineRenderer.ClearPoints();
        StartCoroutine(DrawTrail());
    }
    
    IEnumerator DrawTrail()
    {
        while (true)
        {
            // Add new point at mouse position (normalized to RectTransform)
            Vector2 localPoint;
            RectTransformUtility.ScreenPointToLocalPointInRectangle(
                lineRenderer.GetComponent<RectTransform>(),
                Input.mousePosition,
                null,
                out localPoint
            );
            
            lineRenderer.AddPoint(localPoint);
            
            // Remove oldest point if exceeding max
            if (lineRenderer.Points.Count > maxPoints)
            {
                lineRenderer.RemovePoint();
            }
            
            yield return new WaitForSeconds(0.05f);
        }
    }
    
    public void ClearTrail()
    {
        lineRenderer.ClearPoints();
    }
}
```

**Note**: The component includes a 64,000 vertex limit check. If exceeded, the mesh will be cleared and an error logged.

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [UILineRenderer](UILineRenderer.md) - Standard line renderer
* [UILineTextureRenderer](UILineTextureRenderer.md) - Line renderer with texture mapping and caps
* [BezierLineRenderer](BezierLineRenderer.md) - Curved line renderer

---------

## Credits and Donation

Credits: Steve Westhoff, jack.sydorenko, firagon  
Refactored and updated for performance from UILineRenderer

---------

## External links

[Sourced from](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/324)
