# UIImageCrop

A shader-based effect that crops portions of a UI image along the X and Y axes without using masks, providing efficient partial image rendering.

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

The UIImageCrop effect allows cropping portions of a UI image along X and Y axes without requiring mask components. It applies a custom shader (UI Extensions/UI Image Crop) to the MaskableGraphic component, enabling efficient partial image display through shader-based cropping rather than masking. The component automatically applies the shader material on Start() and in the editor via OnValidate().

---------

## Properties

The properties of the UIImageCrop effect are as follows:

Property | Description
-|-
*XCrop*|Normalized X-axis crop factor from 0 to 1 (default: 0). Crops the image horizontally
*YCrop*|Normalized Y-axis crop factor from 0 to 1 (default: 0). Crops the image vertically

---------

## Methods

Method | Arguments | Description
-|-|-
*SetMaterial*|(none)|Initializes the shader material on the MaskableGraphic component. Automatically called on Start()
*SetXCrop*|float xcrop|Sets the X crop factor (clamped 0-1) and updates the shader property
*SetYCrop*|float ycrop|Sets the Y crop factor (clamped 0-1) and updates the shader property

---------

## Usage

To use the UIImageCrop effect:

1. Add the component via "**Add Component -> UI -> Effects -> Extensions -> UIImageCrop**"
2. The component requires a MaskableGraphic (Image, RawImage, Text, etc.) on the same GameObject
3. The shader material is automatically applied when the component initializes
4. Adjust XCrop and YCrop values in the inspector (0 = no crop, 1 = fully cropped)
5. Use SetXCrop() and SetYCrop() methods for runtime control

Example code for runtime cropping:

```csharp
using UnityEngine.UI.Extensions;

public class ImageCropExample : MonoBehaviour
{
    public UIImageCrop imageCrop;

    void Start()
    {
        // Ensure material is initialized
        imageCrop.SetMaterial();
    }
    
    void CropHorizontally(float amount)
    {
        // Crop from 0 (no crop) to 1 (fully cropped)
        imageCrop.SetXCrop(amount);
    }
    
    void AnimateCrop()
    {
        // Animate cropping over time
        StartCoroutine(AnimateCropCoroutine());
    }
    
    IEnumerator AnimateCropCoroutine()
    {
        float t = 0;
        while (t < 1)
        {
            imageCrop.SetXCrop(t);
            imageCrop.SetYCrop(t);
            t += Time.deltaTime;
            yield return null;
        }
    }
}
```

**Note**: This component must be attached to a GameObject with a MaskableGraphic component (Image, RawImage, Text, etc.). If no graphic is found, an error will be logged.

---------

## Video Demo

*Video demonstration to be added*

---------

## See also

* [SoftMaskScript](../MISSING_DOCUMENTATION.md) - Alternative masking approach (not yet documented)
* [UIFlippable](UIFlippable.md) - Flip images horizontally or vertically

---------

## Credits and Donation

Credits: 00christian00

---------

## External links

[Sourced from](http://forum.unity3d.com/threads/any-way-to-show-part-of-an-image-without-using-mask.360085/#post-2332030)
