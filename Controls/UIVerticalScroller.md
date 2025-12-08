# UIVerticalScroller

A vertical scrolling layout with automatic element scaling based on distance from center, focus detection, and optional navigation buttons.

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

The UIVerticalScroller creates a vertical scrolling list where elements scale based on their distance from a defined center point. Elements closer to the center appear larger (zoomed), while those farther away shrink according to configurable shrinkage factors and minimum scale constraints. The component automatically detects which element is currently focused (closest to center) and supports optional navigation buttons, click events, and focus-change events.

---------

## Properties

The properties of the UIVerticalScroller control are as follows:

Property | Description
-|-
*Scroll Rect*|Reference to the desired ScrollRect component (auto-detected if not set)
*Array Of Elements*|Array of GameObjects to populate inside the scroller. Auto-populated from children if not set
*Center*|RectTransform defining the center display area (position of zoomed content). Required
*Element Size*|RectTransform defining the size/spacing of elements. Defaults to Center if not set
*Element Shrinkage*|Vector2 controlling scale reduction: scale = 1 / (1 + distance * shrinkage). Default: (1/200, 1/200)
*Min Scale*|Vector2 defining minimum element scale (furthest from center). Default: (0.7, 0.7)
*Starting Index*|Index of the item to focus on start (-1 = no auto-focus). Default: -1
*Stop Momentum On End*|When enabled, stops scrolling past the last element from inertia. Default: true
*Disable Unfocused*|When enabled, sets unfocused items to non-interactable. Default: true
*Scroll Up Button*|Optional button GameObject to scroll up/previous (optional)
*Scroll Down Button*|Optional button GameObject to scroll down/next (optional)
***On Button Clicked*** (event)|Event fired when a specific item is clicked. Exposes the index number of the clicked item (optional)
***On Focus Changed*** (event)|Event fired when the focused item changes. Exposes the new focused item index (optional)

Additional properties available in code:

Property | Return Type | Description
-|-|-
FocusedElementIndex|int|Gets the index of the currently focused element
Center|RectTransform|Gets or sets the center viewport RectTransform
ElementSize|RectTransform|Gets or sets the element size RectTransform
ScrollRectComponent|ScrollRect|Gets or sets the ScrollRect component reference
ArrayOfElements|GameObject[]|Gets or sets the array of element GameObjects
Result|string|Gets the text content of the currently focused element (from TMP_Text component if present)
ScrollingPanel|RectTransform|Gets the scrollable area (content of the ScrollRect)

---------

## Methods

Method | Arguments | Description
-|-|-
*UpdateChildren*|int startingIndex = -1, GameObject[] arrayOfElements = null|Recognizes and resizes children. If arrayOfElements is null, uses ScrollingPanel children. If startingIndex > -1, snaps to that element
*SnapToElement*|int element|Instantly snaps the scroll position to focus on the specified element index
*ScrollUp*|(none)|Scrolls up by approximately element height / 1.2. Called by Scroll Up Button if assigned
*ScrollDown*|(none)|Scrolls down by approximately element height / 1.2. Called by Scroll Down Button if assigned

---------

## Usage

To use the UIVerticalScroller control:

1. Add the component via "**Add Component -> Layout -> Extensions -> Vertical Scroller**"
2. Ensure the GameObject has a ScrollRect component (required)
3. Assign the **Center** RectTransform (defines the zoom/focus area)
4. Optionally assign **Element Size** (defaults to Center if not set)
5. Populate **Array Of Elements** or let the component auto-detect children
6. Configure scaling behavior via **Element Shrinkage** and **Min Scale**
7. Set **Starting Index** to auto-focus an element on start
8. Optionally assign **Scroll Up Button** and **Scroll Down Button** for navigation
9. Subscribe to **On Button Clicked** and **On Focus Changed** events

Example code for programmatic control:

```csharp
using UnityEngine.UI.Extensions;

public class VerticalScrollerExample : MonoBehaviour
{
    public UIVerticalScroller scroller;

    void Start()
    {
        // Subscribe to events
        scroller.onButtonClicked.AddListener(OnItemClicked);
        scroller.onFocusChanged.AddListener(OnFocusChanged);
        
        // Dynamically update children
        GameObject[] items = GetScrollItems();
        scroller.UpdateChildren(0, items);  // Start at index 0
    }
    
    void OnItemClicked(int index)
    {
        Debug.Log($"Item {index} clicked");
        // Snap to clicked item
        scroller.SnapToElement(index);
    }
    
    void OnFocusChanged(int newIndex)
    {
        Debug.Log($"Focus changed to item {newIndex}");
        Debug.Log($"Focused item text: {scroller.Result}");
    }
    
    void NavigateToItem(int index)
    {
        scroller.SnapToElement(index);
    }
    
    GameObject[] GetScrollItems()
    {
        // Return array of GameObjects to display
        return scroller.ScrollingPanel.GetComponentsInChildren<Transform>()
            .Select(t => t.gameObject)
            .Where(g => g != scroller.ScrollingPanel.gameObject)
            .ToArray();
    }
}
```

> [!NOTE]
>
> - The Center RectTransform is required; the component logs an error if not assigned
> - Elements are automatically resized to match Element Size dimensions
> - Each element should have a CanvasGroup for interactability control
> - Text content is extracted from TMP_Text components for the Result property

---------

## Video Demo

[![View Demo Video](http://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/channel/UCHp8LZ_0-iCvl-5pjHATsgw "Mrs. YakaYocha's Channel")

Sample scene: `UIVerticalScrollerDemo`

---------

## See also

* [HorizontalScrollSnap](HorizontalScrollSnap.md) - Horizontal scroll snap control
* [VerticalScrollSnap](VerticalScrollSnap.md) - Vertical scroll snap control
* [ScrollSnapBase](ScrollSnapBase.md) - Base class for scroll snapping

---------

## Credits and Donation

Credits: Mrs. YakaYocha  
Please donate: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RJ8D9FRFQF9VS

---------

## External links

[Sourced from](https://www.youtube.com/channel/UCHp8LZ_0-iCvl-5pjHATsgw)
