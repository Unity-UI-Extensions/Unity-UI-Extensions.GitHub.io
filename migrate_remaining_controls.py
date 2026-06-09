#!/usr/bin/env python3
"""
migrate_remaining_controls.py — finish the uGUI control documentation.

Gives the remaining 36 uGUI controls a proper Jekyll documentation page
(prepends `layout: control-ugui` front matter to their Controls/*.md) and adds
them to _data/ugui_controls.yml so they appear in the controls listing. This
brings every one of the 100 uGUI controls to "has a documentation page".

Demo media (screenshots / video) can be added later — preview_image is left
blank, which renders the placeholder card (same as the UI Toolkit controls).

Run from the Unity-UI-Extensions.GitHub.io directory:  python migrate_remaining_controls.py
Idempotent: skips files that already have front matter / data entries.
"""
import os
import re

CONTROLS_DIR = "Controls"
DATA_FILE = os.path.join("_data", "ugui_controls.yml")

# filename (no .md), title, category, slug, description, tags
REMAINING = [
    ("BestFitOutline", "Best Fit Outline", "Effects", "best-fit-outline",
     "Outline effect that scales correctly with a Text component's best-fit sizing.",
     ["effects", "outline", "text", "best-fit"]),
    ("BoundToolTip", "Bound ToolTip", "Utilities", "bound-tooltip",
     "Tooltip driven by a central listener for displaying data-bound content on hover.",
     ["utilities", "tooltip", "hover", "bound"]),
    ("CLFZ2", "CLZF2 Compression", "Utilities", "clzf2-compression",
     "LZF compression helper for compressing UI or save data at runtime.",
     ["utilities", "compression", "lzf", "data"]),
    ("CurvedLayout", "Curved Layout", "Layout", "curved-layout",
     "Arranges child elements along a configurable curve.",
     ["layout", "curve", "curved", "arrange"]),
    ("CurvedText", "Curved Text", "Effects", "curved-text",
     "Bends legacy uGUI Text along a curve (for projects not using TextMeshPro).",
     ["effects", "text", "curve", "bend"]),
    ("CylinderText", "Cylinder Text", "Effects", "cylinder-text",
     "Curved text effect that wraps text around a cylindrical surface.",
     ["effects", "text", "cylinder", "curve"]),
    ("DragCorrector", "Drag Corrector", "Utilities", "drag-corrector",
     "Manages the EventSystem drag threshold for high-DPI displays.",
     ["utilities", "drag", "dpi", "eventsystem"]),
    ("ExtensionsToggle", "Extensions Toggle", "Input", "extensions-toggle",
     "Enhanced Toggle with additional event types and toggle behaviours.",
     ["input", "toggle", "events", "selectable"]),
    ("ExtensionsToggleGroup", "Extensions Toggle Group", "Input", "extensions-toggle-group",
     "Manages a group of Extensions Toggle components with single or multi selection.",
     ["input", "toggle", "group", "selection"]),
    ("GamePadInputModule", "GamePad Input Module", "Utilities", "gamepad-input-module",
     "Stripped-down input module for gamepad and keyboard UI navigation.",
     ["utilities", "gamepad", "input", "navigation", "keyboard"]),
    ("HoverToolTip", "Hover ToolTip", "Utilities", "hover-tooltip",
     "Basic tooltip that appears on pointer hover.",
     ["utilities", "tooltip", "hover", "popup"]),
    ("ImageExtended", "Image Extended", "Primitives", "image-extended",
     "Improved Image control with rotation support and filled type without a sprite.",
     ["primitives", "image", "rotation", "filled"]),
    ("Infinite Scroll Snap", "Infinite Scroll Snap", "Layout", "infinite-scroll-snap",
     "Endlessly looping scroll-snap layout for UI elements.",
     ["layout", "scroll", "snap", "infinite", "loop"]),
    ("InputFieldEnterSubmit", "Input Field Enter Submit", "Utilities", "input-field-enter-submit",
     "Automatically submits an InputField when the Enter key is pressed.",
     ["utilities", "inputfield", "enter", "submit"]),
    ("InputFocus", "Input Focus", "Utilities", "input-focus",
     "Enhanced InputField for forms — Enter to submit plus focus management.",
     ["utilities", "inputfield", "focus", "forms"]),
    ("MinMaxSlider", "Min Max Slider", "Input", "min-max-slider",
     "Dual-handle slider for selecting a value range between minimum and maximum bounds.",
     ["input", "slider", "range", "min", "max"]),
    ("MultiTouchScrollRect", "MultiTouch Scroll Rect", "Layout", "multitouch-scroll-rect",
     "ScrollRect fix that correctly handles multiple simultaneous touches.",
     ["layout", "scroll", "multitouch", "scrollrect"]),
    ("NicerOutline", "Nicer Outline", "Effects", "nicer-outline",
     "Improved outline effect with cleaner corners than the built-in Outline.",
     ["effects", "outline", "text", "polish"]),
    ("PPIViewer", "PPI Viewer", "Utilities", "ppi-viewer",
     "Displays the current screen DPI/PPI on a Text component.",
     ["utilities", "dpi", "ppi", "debug", "text"]),
    ("RaycastMask", "Raycast Mask", "Utilities", "raycast-mask",
     "Enhanced mask that uses image alpha for accurate raycast hit-testing.",
     ["utilities", "raycast", "mask", "alpha", "hit-area"]),
    ("RescaleDragPanel", "Rescale Drag Panel", "Utilities", "rescale-drag-panel",
     "Drag a rescaled panel to reposition it within a canvas, compensating for scale.",
     ["utilities", "drag", "rescale", "panel"]),
    ("RescalePanel", "Rescale Panel", "Utilities", "rescale-panel",
     "Rescales a parent panel by dragging a handle while keeping it anchored.",
     ["utilities", "rescale", "panel", "drag", "handle"]),
    ("ResizePanel", "Resize Panel", "Utilities", "resize-panel",
     "Resize a parent panel by dragging a handle, maintaining aspect ratio.",
     ["utilities", "resize", "panel", "drag", "handle"]),
    ("ReturnKeyTrigger", "Return Key Trigger", "Utilities", "return-key-trigger",
     "Binds the Return key within an InputField to a button or toggle action.",
     ["utilities", "inputfield", "return", "key", "trigger"]),
    ("Scroller", "Scroller", "Layout", "scroller",
     "Scroller component of the FancyScrollView system for advanced scrolling.",
     ["layout", "scroll", "fancyscrollview"]),
    ("Serialization", "Serialization", "Utilities", "serialization",
     "Serialization utilities for UI components.",
     ["utilities", "serialization", "save", "data"]),
    ("ShaderEffects", "Shader Effects Suite", "Effects", "shader-effects",
     "Collection of shader-based blending-mode effects for UI elements.",
     ["effects", "shader", "blend", "suite"]),
    ("UICircle", "UI Circle", "Primitives", "ui-circle",
     "Customisable circle/arc primitive with progress indication and fill modes.",
     ["primitives", "circle", "arc", "progress", "shape"]),
    ("UICornerCut", "UI Corner Cut", "Primitives", "ui-corner-cut",
     "Renders rectangles with selectively cut corners for non-square panels.",
     ["primitives", "corner", "cut", "rectangle", "shape"]),
    ("UIImageCrop", "UI Image Crop", "Effects", "ui-image-crop",
     "Shader-based crop of a UI image along the X and Y axes without masks.",
     ["effects", "image", "crop", "shader"]),
    ("UILineRendererFIFO", "UI Line Renderer (FIFO)", "Primitives", "ui-line-renderer-fifo",
     "Performance line renderer using a first-in-first-out point queue.",
     ["primitives", "line", "fifo", "performance", "draw"]),
    ("UILineRendererList", "UI Line Renderer (List)", "Primitives", "ui-line-renderer-list",
     "Renders multiple connected line segments from a point list.",
     ["primitives", "line", "list", "polyline", "draw"]),
    ("UILineTextureRenderer", "UI Line Texture Renderer", "Primitives", "ui-line-texture-renderer",
     "Textured UI line renderer with UV mapping and automatic end caps.",
     ["primitives", "line", "texture", "uv", "draw"]),
    ("UISquircle", "UI Squircle", "Primitives", "ui-squircle",
     "Renders smooth superellipse (squircle) shapes with configurable curvature.",
     ["primitives", "squircle", "superellipse", "shape", "rounded"]),
    ("UIWindowBase", "UI Window Base", "Layout", "ui-window-base",
     "Draggable window for RectTransforms with bounds checking within the canvas.",
     ["layout", "window", "draggable", "panel"]),
    ("switchToRectTransform", "Switch To RectTransform", "Utilities", "switch-to-recttransform",
     "RectTransform extension that moves one RectTransform onto another.",
     ["utilities", "recttransform", "extension", "transform"]),
]

FRONT_MATTER = '''---
layout: control-ugui
title: "{title}"
description: "{desc}"
category: "{cat}"
permalink: /ugui/controls/{slug}/
has_video: false
tags: [{tags}]
---
'''


def prepend_front_matter():
    added = 0
    for fn, title, cat, slug, desc, tags in REMAINING:
        path = os.path.join(CONTROLS_DIR, fn + ".md")
        if not os.path.exists(path):
            print(f"  SKIP (missing): {fn}.md")
            continue
        content = open(path, encoding="utf-8").read()
        if content.lstrip().startswith("---"):
            print(f"  SKIP (already has front matter): {fn}.md")
            continue
        # Fix relative image paths the same way add_frontmatter.py does
        content = re.sub(r'\]\(Images/', '](/Controls/Images/', content)
        content = re.sub(r'src="Images/', 'src="/Controls/Images/', content)
        fm = FRONT_MATTER.format(title=title, desc=desc, cat=cat, slug=slug, tags=", ".join(tags))
        open(path, "w", encoding="utf-8").write(fm + content)
        added += 1
        print(f"  page: {fn}.md  ->  /ugui/controls/{slug}/")
    print(f"  -> {added} documentation pages completed")


def append_data():
    existing = open(DATA_FILE, encoding="utf-8").read()
    lines = ["", "# ── Controls with complete documentation, demo media pending ─────────────────"]
    appended = 0
    for fn, title, cat, slug, desc, tags in REMAINING:
        if f"permalink: /ugui/controls/{slug}/" in existing:
            continue
        lines += [
            "",
            f"- name: {title}",
            f"  slug: {slug}",
            f"  permalink: /ugui/controls/{slug}/",
            f"  category: {cat}",
            f"  description: {desc}",
            '  preview_image: ""',
            "  has_video: false",
            f"  tags: [{', '.join(tags)}]",
        ]
        appended += 1
    if appended:
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    print(f"  -> {appended} listing entries appended to {DATA_FILE}")


if __name__ == "__main__":
    print(f"Completing documentation for {len(REMAINING)} uGUI controls...")
    prepend_front_matter()
    append_data()
    print("Done.")
