#!/usr/bin/env python3
"""
Create UIToolkit control pages in uitoolkit/controls/<slug>/index.md
by reading source docs and prepending Jekyll front matter.
"""

import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UITK_OUT = os.path.join(BASE_DIR, "uitoolkit", "controls")
SRC_CONTROLS = os.path.join(BASE_DIR, "..", "com.unity.uitoolkitextensions", "Documentation~", "Controls")
SRC_ROOT = os.path.join(BASE_DIR, "..", "com.unity.uitoolkitextensions", "Documentation~")

# (slug, source_filename, name, category, description, tags)
CONTROLS = [
    # Navigation
    ("scroll-snap",           "ScrollSnap.md",                    "Scroll Snap",
     "Navigation",
     "Swipe/drag paged scroll container that snaps to discrete pages by index.",
     ["navigation", "scroll", "snap", "pages", "swipe"]),

    ("collapsible-section",   "CollapsibleSection.md",            "Collapsible Section",
     "Navigation",
     "Animated expand/collapse section with header toggle and content container.",
     ["navigation", "collapse", "expand", "accordion", "section"]),

    ("quadrant-stepper",      "QuadrantStepper.md",               "Quadrant Stepper",
     "Navigation",
     "Four-directional step selector displayed as an overlay compass widget.",
     ["navigation", "stepper", "direction", "compass", "selector"]),

    # Forms
    ("pill-input-field",      "PillInputField.md",                "Pill Input Field",
     "Forms",
     "Rounded pill-shaped input field with floating label and validation state.",
     ["forms", "input", "pill", "label", "text-field"]),

    ("rounded-input-field",   "RoundedInputField.md",             "Rounded Input Field",
     "Forms",
     "Card-style text input with rounded corners and focus/error colour states.",
     ["forms", "input", "rounded", "text-field", "focus"]),

    ("pill-selector",         "PillSelector.md",                  "Pill Selector",
     "Forms",
     "Row of pill-shaped radio buttons for exclusive single-option selection.",
     ["forms", "selector", "pill", "radio", "single-select"]),

    ("toggle-button",         "ToggleButton.md",                  "Toggle Button",
     "Forms",
     "Flat toggle switch with animated indicator and on/off label support.",
     ["forms", "toggle", "switch", "button", "boolean"]),

    ("color-toggle-button",   "ColorToggleButton.md",             "Color Toggle Button",
     "Forms",
     "Toggle button that tints itself with a configurable accent colour when active.",
     ["forms", "toggle", "color", "tint", "button"]),

    ("color-toggle-group",    "ColorToggleGroup.md",              "Color Toggle Group",
     "Forms",
     "Horizontally scrollable row of colour-tinted toggle buttons for multi-select.",
     ["forms", "toggle", "group", "color", "multi-select"]),

    # Feedback
    ("step-progress-bar",     "StepProgressBar.md",               "Step Progress Bar",
     "Feedback",
     "Segmented progress bar with labelled milestone steps and fill animation.",
     ["feedback", "progress", "steps", "bar", "milestone"]),

    ("page-dot-indicator",    "PageDotIndicator.md",              "Page Dot Indicator",
     "Feedback",
     "Animated pagination dots that reflect the current page of a scroll view.",
     ["feedback", "pagination", "dots", "indicator", "scroll"]),

    ("loading-icon",          "LoadingIcon.md",                   "Loading Icon",
     "Feedback",
     "Animated spinner/loading indicator with configurable speed and colour.",
     ["feedback", "loading", "spinner", "animation", "indicator"]),

    ("toast-swipe-dismiss",   "ToastSwipeDismissManipulator.md",  "Toast Swipe Dismiss Manipulator",
     "Feedback",
     "Gesture manipulator that allows swiping a toast/notification to dismiss it.",
     ["feedback", "toast", "swipe", "dismiss", "gesture"]),

    ("coming-soon-message",   "ComingSoonMessage.md",             "Coming Soon Message",
     "Feedback",
     "Placeholder panel displaying a styled \"coming soon\" message with icon.",
     ["feedback", "placeholder", "coming-soon", "panel"]),

    # Primitives
    ("pill-button",           "PillButton.md",                    "Pill Button",
     "Primitives",
     "Primary CTA button in a rounded pill shape with press flash animation.",
     ["primitives", "button", "pill", "cta", "animation"]),

    ("circular-image-button", "CircularImageButton.md",           "Circular Image Button",
     "Primitives",
     "Circular avatar/icon button with mask, border, and selected-state styling.",
     ["primitives", "button", "circular", "avatar", "icon"]),

    ("icon-label-button",     "IconLabelButton.md",               "Icon Label Button",
     "Primitives",
     "Horizontal row button combining a left-side icon with label and subtitle text.",
     ["primitives", "button", "icon", "label", "row"]),

    # Utilities
    ("grayscale-image",       "GrayscaleImage.md",                "Grayscale Image",
     "Utilities",
     "Shader-based Image element that renders in greyscale with adjustable intensity.",
     ["utilities", "image", "grayscale", "shader", "effect"]),
]


def make_front_matter(slug, name, category, description, tags):
    tags_str = "[" + ", ".join(tags) + "]"
    return f"""---
layout: control-uitk
title: "{name}"
description: "{description}"
category: "{category}"
permalink: /uitoolkit/controls/{slug}/
has_video: false
tags: {tags_str}
---

"""


def get_source_path(filename):
    # ScrollSnap lives in parent Documentation~ dir, rest in Controls/
    controls_path = os.path.join(SRC_CONTROLS, filename)
    if os.path.exists(controls_path):
        return controls_path
    root_path = os.path.join(SRC_ROOT, filename)
    if os.path.exists(root_path):
        return root_path
    return None


def process_control(slug, filename, name, category, description, tags):
    src = get_source_path(filename)
    if src is None:
        print(f"  MISSING SRC: {filename}")
        return False

    out_dir = os.path.join(UITK_OUT, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.md")

    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip leading H1 title — it's rendered by the layout
    content = re.sub(r'^#\s+\S[^\n]*\n+', '', content, count=1)

    front_matter = make_front_matter(slug, name, category, description, tags)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(front_matter + content)

    print(f"  OK: {slug}/index.md")
    return True


def main():
    os.makedirs(UITK_OUT, exist_ok=True)
    print(f"Creating {len(CONTROLS)} UIToolkit control pages in {UITK_OUT}...")
    ok = 0
    for slug, filename, name, category, description, tags in CONTROLS:
        if process_control(slug, filename, name, category, description, tags):
            ok += 1
    print(f"Done. {ok}/{len(CONTROLS)} pages created.")


if __name__ == "__main__":
    main()
