---
layout: example-uitk
title: "Action Menu"
description: "Anchored overflow menus — per-row ··· triggers and a centered card menu, with callback and dismiss handling."
category: "Navigation"
permalink: /uitoolkit/examples/action-menu/
tags: [navigation, menu, overflow, actions]
controls:
  - name: "Dropdown Menu"
    permalink: /uitoolkit/controls/dropdown-menu/
  - name: "Pill Button"
    permalink: /uitoolkit/controls/pill-button/
---

## Overview

This example demonstrates the code-only `DropDownMenuControl` in its two placement modes. Three content rows each carry a "···" overflow button that opens an anchored menu (`AnchorRight`) with **View / Edit / Remove** options — Remove genuinely removes the row. A "Card actions" `PillButton` opens the same menu instance centered on itself (`CenteredOnAnchor`) with card-level actions. A status line reports every chosen action, and the `onDismissed` callback reports when a menu is closed by tapping the backdrop instead.

## Controls Featured

- [DropDownMenuControl](/uitoolkit/controls/dropdown-menu/) — lightweight anchored action menu; constructed once in code and opened from multiple triggers with different placements
- [PillButton](/uitoolkit/controls/pill-button/) — gradient-bordered button used as the centered card-level menu trigger

## Scene Setup

1. Create a new Unity scene.
2. Add an empty GameObject named `ActionMenuDemo` to the scene hierarchy.
3. Add a `UIDocument` component to the GameObject.
4. Create a `PanelSettings` asset (`Assets > Create > UI Toolkit > Panel Settings`) and configure it:
   - **Scale Mode:** Scale With Screen Size
   - **Reference Resolution:** 1080 × 1920
   - **Screen Match Mode:** Match Width Or Height, blended toward Height
5. Assign the `PanelSettings` asset to the `UIDocument` component's **Panel Settings** field.
6. Add the `ActionMenuDemo` MonoBehaviour (found in `Examples~/ActionMenu/`) to the same GameObject.
7. Press **Play**.

## What to Expect

The screen shows a single dark card containing three named item rows and a "Card actions" button:

**Item rows** — each row shows a file name with a circular "···" button on the right. Tapping it opens a `DropDownMenuControl` whose right edge aligns to the button, dropping downward (flipping upward near the bottom of the screen). Choosing **View** or **Edit** updates the status line with the item name; choosing **Remove** deletes that row from the card.

**Card actions** — the `PillButton` under the rows opens the same menu centered over itself with **Share / Duplicate / Archive** options, demonstrating the `CenteredOnAnchor` placement.

**Dismissal** — tapping the transparent backdrop anywhere outside the panel closes the menu without running any option, and the status line reports "Menu dismissed — no action taken" via the `onDismissed` callback.

Because the menu injects its panel into the panel root, it is never clipped by the card or the rows it is anchored to.

## Key Code Patterns

One `DropDownMenuControl` instance serves every trigger — each `Open(...)` call supplies the anchor, options and placement. Note it must be constructed in `Start`/`Awake`, not in a field initializer — Unity does not allow VisualElements to be created from a MonoBehaviour constructor:

```csharp
private DropDownMenuControl actionMenu;

private void Start()
{
    actionMenu = new DropDownMenuControl();
    // ... query triggers and wire callbacks
}

// Per-row overflow menu, anchored to the ··· button
actionMenu.Open(menuButton, new List<DropDownMenuControl.DropDownOption>
{
    new DropDownMenuControl.DropDownOption("View",   () => statusLabel.text = $"Viewing '{itemName}'."),
    new DropDownMenuControl.DropDownOption("Edit",   () => statusLabel.text = $"Editing '{itemName}'."),
    new DropDownMenuControl.DropDownOption("Remove", () => row.RemoveFromHierarchy()),
},
DropDownMenuControl.Placement.AnchorRight,
onDismissed: () => statusLabel.text = "Menu dismissed — no action taken.");
```
