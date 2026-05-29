# Shader Effects Suite

A collection of shader-based effects that apply different blending modes to UI elements, including additive, multiply, screen, and shine effects.

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Effects](#effects)
>
> 3 [Properties](#properties)
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

The Shader Effects Suite provides a collection of shader-based visual effects for UI elements. Each effect applies a different blending mode to create various visual styles. These effects automatically apply the appropriate shader material to the target graphic component.

All shader effects in this suite share a common implementation pattern: they detect the attached graphic component and apply a specialized shader material that implements the desired blending behavior.

---------

## Effects

### UIAdditiveEffect

**Menu Path:** `UI/Effects/Extensions/UIAdditiveEffect`

Applies additive blending to UI elements. This effect adds the pixel colors together, resulting in a brightening effect. Useful for glow, light, and highlight effects.

**Use Cases:**
- Glow effects
- Light overlays
- Bright highlights
- Additive particle effects in UI

### UISoftAdditiveEffect

**Menu Path:** `UI/Effects/Extensions/UISoftAdditiveEffect`

Applies soft additive blending to UI elements. Similar to additive blending but with reduced intensity, resulting in a gentler brightening effect.

**Use Cases:**
- Softer glow effects
- Subtle light overlays
- Gentle highlights
- Semi-transparent light effects

### UIMultiplyEffect

**Menu Path:** `UI/Effects/Extensions/UIMultiplyEffect`

Applies multiply blending to UI elements. This effect darkens by multiplying pixel colors, resulting in a darkening effect. Useful for shadows and darkening overlays.

**Use Cases:**
- Shadow effects
- Darkening overlays
- Dimming effects
- Dark highlights

### UILinearDodgeEffect

**Menu Path:** `UI/Effects/Extensions/UILinearDodgeEffect`

Applies linear dodge (additive) blending to UI elements. Similar to additive blending with slightly different color mathematics.

**Use Cases:**
- Bright light effects
- Intense glows
- Light trails
- Energy effects

### UIScreenEffect

**Menu Path:** `UI/Effects/Extensions/UIScreenEffect`

Applies screen blending to UI elements. This effect inverts and multiplies pixel colors, resulting in a lightening effect that's gentler than additive blending.

**Use Cases:**
- Screen overlays
- Vignette effects
- Light blending
- Composite lighting

### ShineEffector

**Menu Path:** `UI/Effects/Extensions/Shining Effect`

Creates a moving shine/gloss effect across UI elements. Renders an animated gradient that slides across the target graphic to simulate a glossy or polished surface.

**Use Cases:**
- Glossy button effects
- Shine animations
- Polished surface effects
- Attention-drawing animations

**Properties:**
- *Y Offset* (Range: -1 to 1): Vertical position of the shine effect
- *Width* (Range: 0.1 to 1): Width of the shine gradient

---------

## Properties

All shader effects (except ShineEffector) share these properties:

Property | Description
-|-
*Graphic Component*|The target Graphic component (Image, RawImage, Text) that the effect will be applied to. Automatically detected on the same GameObject.
*Material*|The shader material applied to the graphic. Automatically created using the appropriate shader for the effect type.

ShineEffector-specific properties:

Property | Description
-|-
*Y Offset*|Controls the vertical position of the shine effect. Range from -1 (top) to 1 (bottom).
*Width*|Controls the width/thickness of the shine effect. Range from 0.1 (thin) to 1 (wide).

---------

## Usage

### Basic Effect Application

Simply add the desired effect to a GameObject with a Graphic component (Image, RawImage, or Text):

```csharp
// In editor: Add Component -> UI/Effects/Extensions -> [EffectName]
// Or in code:
var image = GetComponent<Image>();
image.gameObject.AddComponent<UIAdditiveEffect>();
```

The effect will automatically apply its shader material to the graphic component.

### Using Additive Effects

```csharp
public Image glowImage;

void Start()
{
    // Add additive effect to create a glow
    glowImage.gameObject.AddComponent<UIAdditiveEffect>();
}
```

### Using ShineEffector

```csharp
public ShineEffector shineEffect;

void Update()
{
    // Animate the shine effect
    shineEffect.YOffset = Mathf.Sin(Time.time) * 0.5f;
}
```

### Combining Multiple Effects

Multiple effects can be combined for complex visual results:

```csharp
var image = GetComponent<Image>();

// Add multiple effects
image.gameObject.AddComponent<UIMultiplyEffect>();
image.gameObject.AddComponent<UIAdditiveEffect>();
```

Note: When combining effects, be aware that the order and interaction of blending modes will affect the final result.

---------

## Video Demo

Coming soon...

---------

## See also

* [NonDrawingGraphic](/Controls/NonDrawingGraphic.md)
* [UIImageCrop](/Controls/UIImageCrop.md)
* [UIHighlightable](/Controls/UIHighlightable.md)
* [RaycastMask](/Controls/RaycastMask.md)

---------

## Credits and Donation

00christian00, ömer faruk sayılır

---------

## External links

[UIAdditiveEffect Sourced from](http://forum.unity3d.com/threads/any-way-to-show-part-of-an-image-without-using-mask.360085/#post-2332030)
[ShineEffector Sourced from](https://bitbucket.org/snippets/Lordinarius/nrn4L)
