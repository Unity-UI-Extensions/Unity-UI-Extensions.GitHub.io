#!/usr/bin/env python3
"""
Prepends Jekyll front matter to uGUI control .md files and fixes image paths.
Run from the Unity-UI-Extensions.GitHub.io directory.
"""
import os, re

CONTROLS_DIR = "Controls"

# Map: filename (without .md) -> front matter data
CONTROLS = [
    ("Accordion",              "Accordion",                    "Layout",     "/ugui/controls/accordion/",                      "An Accordion style control with animated expandable/collapsible sections.",                           False, ["layout","accordion","collapse","expand","panel"]),
    ("AutoCompleteComboBox",   "AutoComplete ComboBox",        "Input",      "/ugui/controls/autocomplete-combobox/",          "Combobox with live-filter autocomplete suggestions as the user types.",                              False, ["input","combobox","autocomplete","dropdown","search"]),
    ("BoxSlider",              "Box Slider",                   "Input",      "/ugui/controls/box-slider/",                     "2D drag-handle slider that outputs both X and Y values simultaneously.",                             True,  ["input","slider","2d","xy","drag"]),
    ("CardUI",                 "Card UI",                      "Layout",     "/ugui/controls/card-ui/",                        "2D and 3D card flip/stack animations for content presentation.",                                     False, ["layout","card","flip","3d","animation"]),
    ("ColorPicker",            "Color Picker",                 "Input",      "/ugui/controls/color-picker/",                   "Full HSV colour picker with hex input, alpha slider, and preset swatches.",                         True,  ["input","color","colour","picker","hsv","hex"]),
    ("ComboBox",               "ComboBox",                     "Input",      "/ugui/controls/combobox/",                       "Editable dropdown with keyboard navigation and multi-select capability.",                            False, ["input","combobox","dropdown","select"]),
    ("ContentScrollSnapHorizontal","Content Scroll Snap Horizontal","Layout","/ugui/controls/content-scroll-snap-horizontal/","Snap-to-page horizontal scroll container with automatic page detection.",                            False, ["layout","scroll","snap","horizontal","pagination"]),
    ("CooldownButton",         "Cooldown Button",              "Input",      "/ugui/controls/cooldown-button/",                "Button with an animated cooldown arc that prevents rapid re-clicking.",                              True,  ["input","button","cooldown","timer","animation"]),
    ("CurlyUI",                "CurlyUI",                      "Effects",    "/ugui/controls/curly-ui/",                       "Warps any uGUI graphic with configurable horizontal and vertical curves.",                           True,  ["effects","curve","warp","mesh","distort"]),
    ("DiamondGraph",           "Diamond Graph",                "Primitives", "/ugui/controls/diamond-graph/",                  "Radar/spider chart rendered as a configurable diamond polygon shape.",                               True,  ["primitives","chart","radar","spider","graph","polygon"]),
    ("DropDownList",           "DropDown List",                "Input",      "/ugui/controls/dropdown-list/",                  "Styleable dropdown list with animated open/close and custom item rendering.",                       False, ["input","dropdown","select","list"]),
    ("FancyScrollView",        "Fancy Scroll View",            "Layout",     "/ugui/controls/fancy-scroll-view/",              "High-performance scroll view with virtual item pooling and custom layouts.",                        False, ["layout","scroll","virtual","performance","pooling"]),
    ("FlowLayoutGroup",        "Flow Layout Group",            "Layout",     "/ugui/controls/flow-layout-group/",              "Automatically wraps child elements into rows or columns like CSS flexbox.",                          True,  ["layout","flow","wrap","grid","auto-layout"]),
    ("Gradient",               "Gradient",                     "Effects",    "/ugui/controls/gradient/",                       "Applies a two-colour vertex gradient to any uGUI graphic component.",                               True,  ["effects","gradient","colour","vertex","text"]),
    ("Gradient2",              "Gradient 2",                   "Effects",    "/ugui/controls/gradient2/",                      "Four-corner gradient effect with independent colour control per vertex.",                            False, ["effects","gradient","four-corner","vertex","colour"]),
    ("GridRawImage",           "Grid Raw Image",               "Primitives", "/ugui/controls/grid-raw-image/",                 "RawImage that tiles a texture in a grid pattern with UV offset control.",                           False, ["primitives","image","grid","tile","texture"]),
    ("HorizontalScrollSnap",   "Horizontal Scroll Snap",       "Layout",     "/ugui/controls/horizontal-scroll-snap/",         "Paged horizontal scroll view that snaps to discrete content pages.",                                False, ["layout","scroll","snap","horizontal","pages"]),
    ("LetterSpacing",          "Letter Spacing",               "Effects",    "/ugui/controls/letter-spacing/",                 "Adds configurable character spacing (tracking) to uGUI Text components.",                           True,  ["effects","text","letter-spacing","tracking","typography"]),
    ("MenuSystem",             "Menu System",                  "Navigation", "/ugui/controls/menu-system/",                    "Hierarchical animated menu with slide, fade, and scale transition modes.",                          True,  ["navigation","menu","hierarchy","transition","animated"]),
    ("MonoSpacing",            "Mono Spacing",                 "Effects",    "/ugui/controls/mono-spacing/",                   "Forces monospace character widths on any uGUI Text component.",                                     True,  ["effects","text","monospace","spacing","typography"]),
    ("NonDrawingGraphic",      "Non-Drawing Graphic",          "Utilities",  "/ugui/controls/non-drawing-graphic/",            "Invisible raycast-blocking graphic — enables hit areas without any visual.",                        True,  ["utilities","raycast","invisible","hit-area","clickable"]),
    ("PaginationManager",      "Pagination Manager",           "Utilities",  "/ugui/controls/pagination-manager/",             "Connects a ScrollSnap or ContentScrollSnap to dot-style pagination indicators.",                    False, ["utilities","pagination","dots","scrollsnap","indicator"]),
    ("RadialLayout",           "Radial Layout",                "Utilities",  "/ugui/controls/radial-layout/",                  "Arranges child elements in a circle or arc at configurable radius and angle.",                      True,  ["utilities","layout","radial","circular","arc"]),
    ("RadialSlider",           "Radial Slider",                "Input",      "/ugui/controls/radial-slider/",                  "Circular arc slider with configurable start angle, range, and fill style.",                        True,  ["input","slider","radial","circular","arc"]),
    ("RangeSlider",            "Range Slider",                 "Input",      "/ugui/controls/range-slider/",                   "Dual-handle slider for selecting a minimum/maximum value range.",                                  True,  ["input","slider","range","min","max","dual"]),
    ("RectTransformEditor",    "Rect Transform Editor",        "Utilities",  "/ugui/controls/rect-transform-editor/",          "Editor-only helper that adds extra transform manipulation handles in the Scene view.",               False, ["utilities","editor","rect-transform","inspector","tools"]),
    ("ReorderableList",        "Reorderable List",             "Layout",     "/ugui/controls/reorderable-list/",               "Drag-and-drop list and grid layout with visual reordering feedback.",                               False, ["layout","list","drag","drop","reorder"]),
    ("ResetSelectableHighlight","Reset Selectable Highlight",  "Utilities",  "/ugui/controls/reset-selectable-highlight/",     "Clears stuck hover/selected highlight states on Selectable components.",                            False, ["utilities","selectable","highlight","reset","state"]),
    ("ScrollConflictManager",  "Scroll Conflict Manager",      "Utilities",  "/ugui/controls/scroll-conflict-manager/",        "Resolves scroll direction conflicts when nested ScrollRects overlap.",                              False, ["utilities","scroll","conflict","nested","scrollrect"]),
    ("ScrollRectEx",           "Scroll Rect Ex",               "Layout",     "/ugui/controls/scroll-rect-ex/",                 "Enhanced ScrollRect with momentum, deceleration tuning, and edge effects.",                        False, ["layout","scroll","scrollrect","momentum","enhanced"]),
    ("ScrollRectLinker",       "Scroll Rect Linker",           "Layout",     "/ugui/controls/scroll-rect-linker/",             "Synchronises multiple ScrollRect components so they scroll in tandem.",                            False, ["layout","scroll","sync","linked","scrollrect"]),
    ("ScrollRectTweener",      "Scroll Rect Tweener",          "Layout",     "/ugui/controls/scroll-rect-tweener/",            "Programmatically scrolls a ScrollRect to a target position with easing.",                          False, ["layout","scroll","tween","animate","scrollrect"]),
    ("ScrollSnap",             "Scroll Snap",                  "Layout",     "/ugui/controls/scroll-snap/",                    "Perspective scroll snap with 3D carousel-style page transitions.",                                 True,  ["layout","scroll","snap","perspective","carousel","3d"]),
    ("Segment",                "Segment",                      "Input",      "/ugui/controls/segment/",                        "Individual button segment used as a child within a SegmentedControl.",                              False, ["input","segment","button","selectable"]),
    ("SegmentedControl",       "Segmented Control",            "Input",      "/ugui/controls/segmented-control/",              "iOS-style segmented control for choosing one option from a small set.",                             True,  ["input","segmented","toggle","select","ios"]),
    ("SelectableScaler",       "Selectable Scaler",            "Utilities",  "/ugui/controls/selectable-scaler/",              "Scales a Selectable component up/down on hover and press events.",                                 True,  ["utilities","selectable","scale","hover","press","animation"]),
    ("SelectionBox",           "Selection Box",                "Input",      "/ugui/controls/selection-box/",                  "Drag to draw a rubber-band selection rectangle over multiple UI elements.",                        False, ["input","selection","drag","marquee","multi-select"]),
    ("SoftAlphaMask",          "Soft Alpha Mask",              "Effects",    "/ugui/controls/soft-alpha-mask/",                "Uses a greyscale mask texture to softly clip UI content at the edges.",                            False, ["effects","mask","alpha","clip","soft"]),
    ("Stepper",                "Stepper",                      "Input",      "/ugui/controls/stepper/",                        "+/- increment buttons for numeric input with configurable step size.",                              True,  ["input","stepper","increment","decrement","numeric"]),
    ("TabNavigation",          "Tab Navigation",               "Navigation", "/ugui/controls/tab-navigation/",                 "Keyboard-navigable tab panel system with animated content switching.",                              True,  ["navigation","tabs","keyboard","panel","switch"]),
    ("TableLayoutGroup",       "Table Layout Group",           "Layout",     "/ugui/controls/table-layout-group/",             "CSS-style table layout that arranges UI elements into rows and columns.",                          True,  ["layout","table","grid","rows","columns"]),
    ("TextPic",                "TextPic",                      "Effects",    "/ugui/controls/textpic/",                        "Embeds inline sprite images inside uGUI Text using custom tags.",                                  True,  ["effects","text","sprite","inline","emoji","rich-text"]),
    ("TileSizeFitter",         "Tile Size Fitter",             "Layout",     "/ugui/controls/tile-size-fitter/",               "Constrains child tiles to a fixed aspect ratio within a grid layout.",                             False, ["layout","tile","aspect-ratio","grid","fitter"]),
    ("ToolTip",                "ToolTip",                      "Utilities",  "/ugui/controls/tooltip/",                        "Follows-cursor tooltip that displays rich text on pointer enter/exit.",                            False, ["utilities","tooltip","hover","popup","cursor"]),
    ("UICircleSegmented",      "UI Circle Segmented",          "Primitives", "/ugui/controls/ui-circle-segmented/",            "Segmented ring/pie chart renderer with configurable slice count and gaps.",                        False, ["primitives","circle","pie","ring","segmented","chart"]),
    ("UIFlippable",            "UI Flippable",                 "Effects",    "/ugui/controls/ui-flippable/",                   "Mirrors any graphic component horizontally or vertically at runtime.",                             True,  ["effects","flip","mirror","graphic","transform"]),
    ("UIGraphicSector",        "UI Graphic Sector",            "Primitives", "/ugui/controls/ui-graphic-sector/",              "Renders a filled sector (wedge/pie-slice) graphic with configurable arc.",                        False, ["primitives","sector","arc","wedge","pie","graphic"]),
    ("UIGridRenderer",         "UI Grid Renderer",             "Primitives", "/ugui/controls/ui-grid-renderer/",               "Procedurally renders a grid of lines using Unity's UI mesh system.",                               True,  ["primitives","grid","lines","mesh","renderer"]),
    ("UIHighlightable",        "UI Highlightable",             "Utilities",  "/ugui/controls/ui-highlightable/",               "Adds programmatic hover-highlight colour transitions to any Graphic.",                            True,  ["utilities","highlight","hover","colour","transition"]),
    ("UILineConnector",        "UI Line Connector",            "Primitives", "/ugui/controls/ui-line-connector/",              "Draws connecting lines between RectTransform anchors with configurable width.",                    True,  ["primitives","line","connector","link","bezier"]),
    ("UILineRenderer",         "UI Line Renderer",             "Primitives", "/ugui/controls/ui-line-renderer/",               "Smooth multi-point UI line with configurable thickness, dash, and colour.",                       False, ["primitives","line","polyline","chart","draw"]),
    ("UIParticleSystem",       "UI Particle System",           "Effects",    "/ugui/controls/ui-particle-system/",             "Renders Unity Particle Systems within the uGUI canvas layer.",                                     True,  ["effects","particles","vfx","canvas","render"]),
    ("UIPolygon",              "UI Polygon",                   "Primitives", "/ugui/controls/ui-polygon/",                     "Renders any regular or irregular polygon as a filled UI graphic.",                                False, ["primitives","polygon","shape","graphic","mesh"]),
    ("UIScrollToSelection",    "UI Scroll To Selection",       "Utilities",  "/ugui/controls/ui-scroll-to-selection/",         "Automatically scrolls a ScrollRect to keep the selected element in view.",                        False, ["utilities","scroll","selection","focus","auto-scroll"]),
    ("UIScrollToSelectionXY",  "UI Scroll To Selection XY",   "Utilities",  "/ugui/controls/ui-scroll-to-selection-xy/",      "Auto-scrolls a 2D ScrollRect to keep the selected element in view on both axes.",                  False, ["utilities","scroll","selection","xy","auto-scroll"]),
    ("UISelectableExtension",  "UI Selectable Extension",      "Utilities",  "/ugui/controls/ui-selectable-extension/",        "Extends Selectable with extra state events and programmatic selection.",                           False, ["utilities","selectable","events","extension","state"]),
    ("UIVerticalScroller",     "UI Vertical Scroller",         "Layout",     "/ugui/controls/ui-vertical-scroller/",           "Vertical scroller with centre-focus zooming — elements scale by distance.",                       False, ["layout","scroll","vertical","zoom","scale"]),
    ("UI_InfiniteScroll",      "UI Infinite Scroll",           "Utilities",  "/ugui/controls/ui-infinite-scroll/",             "Loops ScrollRect content indefinitely in horizontal or vertical mode.",                           True,  ["utilities","scroll","infinite","loop","scrollrect"]),
    ("UI_Knob",                "UI Knob",                      "Input",      "/ugui/controls/ui-knob/",                        "Rotary knob input with configurable min/max angle and loop support.",                             False, ["input","knob","rotary","dial","rotate"]),
    ("UI_MagneticInfiniteScroll","UI Magnetic Infinite Scroll","Utilities",  "/ugui/controls/ui-magnetic-infinite-scroll/",    "Infinite scroll with magnetic snap-to-item behaviour and deceleration.",                          False, ["utilities","scroll","infinite","magnetic","snap"]),
    ("UI_ScrollRectOcclusion", "UI Scroll Rect Occlusion",     "Utilities",  "/ugui/controls/ui-scroll-rect-occlusion/",       "Disables off-screen children in a ScrollRect to reduce overdraw cost.",                           False, ["utilities","scroll","occlusion","performance","visibility"]),
    ("UI_TweenScale",          "UI TweenScale",                "Effects",    "/ugui/controls/ui-tween-scale/",                 "Bounce/pulse scale tween on any UI element triggered by pointer events.",                        False, ["effects","tween","scale","bounce","animation"]),
    ("VerticalScrollSnap",     "Vertical Scroll Snap",         "Layout",     "/ugui/controls/vertical-scroll-snap/",           "Paged vertical scroll view that snaps to discrete content pages.",                                False, ["layout","scroll","snap","vertical","pages"]),
    ("uGUITools",              "uGUI Tools",                   "Navigation", "/ugui/controls/ugui-tools/",                     "Editor menu shortcuts for common uGUI operations — align, distribute, reset.",                    False, ["navigation","editor","tools","utilities","shortcuts"]),
]

def make_front_matter(name, category, permalink, description, has_video, tags):
    tags_str = ", ".join(tags)
    video_str = "true" if has_video else "false"
    return f"""---
layout: control-ugui
title: "{name}"
description: "{description}"
category: "{category}"
permalink: {permalink}
has_video: {video_str}
tags: [{tags_str}]
---
"""

def process_file(filename, name, category, permalink, description, has_video, tags):
    filepath = os.path.join(CONTROLS_DIR, filename + ".md")
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has front matter
    if content.startswith("---"):
        print(f"  SKIP (already has front matter): {filename}.md")
        return

    # Build front matter
    fm = make_front_matter(name, category, permalink, description, has_video, tags)

    # Fix relative image paths: ](Images/ -> ](/Controls/Images/
    content = re.sub(r'\]\(Images/', '](/Controls/Images/', content)

    # Also fix src="Images/ in any HTML img tags
    content = re.sub(r'src="Images/', 'src="/Controls/Images/', content)

    # Write updated file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fm + content)

    print(f"  OK: {filename}.md")


if __name__ == "__main__":
    print(f"Processing {len(CONTROLS)} control files...")
    for entry in CONTROLS:
        filename, name, category, permalink, description, has_video, tags = entry
        process_file(filename, name, category, permalink, description, has_video, tags)
    print("Done.")
