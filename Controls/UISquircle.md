# UISquircle

A primitive that renders smooth superellipse shapes (squircles) with configurable curvature, offering an elegant alternative to sharp corners or simple rounded rectangles.

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

The UISquircle primitive renders superellipse shapes (commonly called "squircles") using the mathematical formula |x/a|^n + |y/b|^n = 1. These shapes provide a smooth, aesthetically pleasing alternative to sharp corners or simple rounded rectangles. The component supports two modes: Classic (fits shape to RectTransform dimensions) and Scaled (uniform scaling with configurable radius), and includes quality optimization to reduce vertex count.

---------

## Properties

The properties of the UISquircle control are as follows:

Property | Description
-|-
*Squircle Type*|Shape calculation mode: **Classic** (scales to RectTransform width/height) or **Scaled** (uniform scaling with radius constraint)
*N*|Curvature exponent from 1 to 40 (default: 4). Higher values = sharper corners, lower = rounder. Classic squircle uses n=4
*Delta*|Step size for vertex generation (default: 5). Smaller = more vertices = smoother curve
*Quality*|Vertex optimization threshold (default: 0.1). Higher values = fewer vertices = lower quality
*Radius*|Maximum radius for Scaled mode (default: 1000). Constrains the shape size

---------

## Methods

The UISquircle control does not expose public methods beyond inherited base class functionality.

---------

## Usage

To use the UISquircle primitive:

1. Add the component via "**Add Component -> UI -> Extensions -> Primitives -> Squircle**"
2. Choose Squircle Type:
   - **Classic**: Shape scales to fill RectTransform dimensions (may be non-uniform)
   - **Scaled**: Shape maintains uniform circular scaling within specified radius
3. Adjust **N** to control corner sharpness (4 = classic squircle, lower = rounder, higher = sharper)
4. Tune **Delta** and **Quality** to balance smoothness vs. performance
5. For Scaled mode, set **Radius** to constrain maximum size

Example code for runtime squircle configuration:

```csharp
using UnityEngine.UI.Extensions;

public class SquircleExample : MonoBehaviour
{
    public UISquircle squircle;

    void Start()
    {
        // Configure as classic squircle
        squircle.squircleType = UISquircle.Type.Classic;
        squircle.n = 4f;       // Classic squircle value
        squircle.delta = 3f;   // Smoother curve
        squircle.quality = 0.1f;
    }
    
    void MakeRounder()
    {
        // Lower n = rounder corners
        squircle.n = 2f;
        squircle.SetVerticesDirty();
    }
    
    void MakeSharper()
    {
        // Higher n = sharper corners
        squircle.n = 8f;
        squircle.SetVerticesDirty();
    }
    
    void UseScaledMode()
    {
        // Switch to uniform scaling
        squircle.squircleType = UISquircle.Type.Scaled;
        squircle.radius = 200f;
        squircle.SetVerticesDirty();
    }
}
```

**Performance Note**: The editor inspector displays the current vertex count. Adjust Quality and Delta to optimize. Higher Quality values remove more vertices but may reduce smoothness.

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [UICornerCut](UICornerCut.md) - Cut corner primitive
* [UICircle](UICircle.md) - Circle/arc primitive

---------

## Credits and Donation

Credits: Soprachev Andrei

---------

## External links

*No external source link provided*
