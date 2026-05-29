# UICornerCut

A primitive that renders rectangles with selectively cut corners, creating non-square panels with beveled edges and optional color variations.

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

The UICornerCut primitive takes a rectangular RectTransform and cuts off selected corners based on a configurable corner size. This is useful for creating quick and easy non-square panels or images with beveled corners. The component adds additional geometry for cut corners and offsets the ends to simulate the cut appearance. UVs are set for texture mapping (though may be skewed when textures are applied).

---------

## Properties

The properties of the UICornerCut control are as follows:

Property | Description
-|-
*Corner Size*|Size of the corner cuts in pixels (Vector2, default: 16x16)
*Cut UL*|Cut the upper-left corner (default: true)
*Cut UR*|Cut the upper-right corner (default: false)
*Cut LL*|Cut the lower-left corner (default: false)
*Cut LR*|Cut the lower-right corner (default: false)
*Make Columns*|When enabled, up-down colors become left-right colors, changing the color bar orientation
*Use Color Up*|Enable custom color for the upper (or left if Make Columns) cut bars
*Color Up*|Custom color for the upper/left cut bars (when Use Color Up is enabled)
*Use Color Down*|Enable custom color for the lower (or right if Make Columns) cut bars
*Color Down*|Custom color for the lower/right cut bars (when Use Color Down is enabled)

Additional properties available in code:

Property | Return Type | Description
-|-|-
CutUL|bool|Gets or sets whether the upper-left corner is cut. Calling the setter marks the component dirty
CutUR|bool|Gets or sets whether the upper-right corner is cut. Calling the setter marks the component dirty
CutLL|bool|Gets or sets whether the lower-left corner is cut. Calling the setter marks the component dirty
CutLR|bool|Gets or sets whether the lower-right corner is cut. Calling the setter marks the component dirty
MakeColumns|bool|Gets or sets the Make Columns mode. Calling the setter marks the component dirty
UseColorUp|bool|Gets or sets whether to use custom color for upper/left bars
ColorUp|Color32|Gets or sets the custom color for upper/left bars
UseColorDown|bool|Gets or sets whether to use custom color for lower/right bars
ColorDown|Color32|Gets or sets the custom color for lower/right bars

---------

## Methods

The UICornerCut control does not expose public methods beyond the property setters (which automatically call SetAllDirty() to update the mesh).

---------

## Usage

To use the UICornerCut primitive:

1. Add the component via "**Add Component -> UI -> Extensions -> Primitives -> Cut Corners**"
2. Set the Corner Size to define how large the beveled corners should be
3. Enable/disable individual corners (Cut UL, Cut UR, Cut LL, Cut LR) as needed
4. Optionally enable Use Color Up/Down and set custom colors to differentiate cut bars from the main panel
5. Toggle Make Columns to change color bar orientation from horizontal to vertical

Example code for runtime configuration:

```csharp
using UnityEngine.UI.Extensions;

public class CornerCutExample : MonoBehaviour
{
    public UICornerCut panel;

    void Start()
    {
        // Cut all corners with 20px size
        panel.cornerSize = new Vector2(20, 20);
        panel.CutUL = true;
        panel.CutUR = true;
        panel.CutLL = true;
        panel.CutLR = true;
        
        // Color the top/bottom bars differently
        panel.UseColorUp = true;
        panel.ColorUp = new Color32(255, 200, 200, 255);
        panel.UseColorDown = true;
        panel.ColorDown = new Color32(200, 200, 255, 255);
    }
    
    void ToggleUpperCorners()
    {
        // Toggle only upper corners
        panel.CutUL = !panel.CutUL;
        panel.CutUR = !panel.CutUR;
    }
}
```

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [UISquircle](UISquircle.md) - Rounded corner primitive with smooth curves
* [NicerOutline (deprecated)](NicerOutline.md) - Alternative outline effect (deprecated for Unity 6)

---------

## Credits and Donation

Credits: Freezy - ElicitIce.nl

Free for any use and alteration, source code may not be sold without permission.

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/cut-corners-primative.359494/)
