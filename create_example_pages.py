#!/usr/bin/env python3
"""
Build the Examples Browser for both packages.

For each example it:
  1. emits an entry into _data/<pkg>_examples.yml  (drives the browser grid,
     each control's "Demonstrated In" block, and each example's "Controls
     demonstrated" list), and
  2. generates the website page <pkg>/examples/<slug>/index.md from the package
     example doc (Documentation~/Examples/<src>), stripping the leading H1 and
     prepending Jekyll front matter.

Example doc bodies live in the packages (canonical). Website pages are generated
artefacts — re-run this after editing any package example doc. Pages are skipped
(with a notice) when their source doc does not exist yet.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
PKG = {
    "ugui": {
        "controls_yml": os.path.join(BASE, "_data", "ugui_controls.yml"),
        "src_dir": os.path.join(BASE, "..", "com.unity.uiextensions-github", "Documentation~", "Examples"),
        "out_dir": os.path.join(BASE, "ugui", "examples"),
        "controls_base": "/ugui/controls/",
        "examples_base": "/ugui/examples/",
        "layout": "example-ugui",
        "data_yml": os.path.join(BASE, "_data", "ugui_examples.yml"),
        "title": "uGUI Examples",
    },
    "uitk": {
        "controls_yml": os.path.join(BASE, "_data", "uitk_controls.yml"),
        "src_dir": os.path.join(BASE, "..", "com.unity.uitoolkitextensions", "Documentation~", "Examples"),
        "out_dir": os.path.join(BASE, "uitoolkit", "examples"),
        "controls_base": "/uitoolkit/controls/",
        "examples_base": "/uitoolkit/examples/",
        "layout": "example-uitk",
        "data_yml": os.path.join(BASE, "_data", "uitk_examples.yml"),
        "title": "UI Toolkit Examples",
    },
}

# (pkg, slug, src_doc, name, category, description, [control_slugs], [tags])
EXAMPLES = [
    # ── UI Toolkit ────────────────────────────────────────────────────────────
    ("uitk", "content-explorer", "ContentExplorer.md", "Content Explorer", "Showcase",
     "A full content-browsing screen that composes scroll-snap, collapsible sections, inputs, a loading state and toasts into one layout.",
     ["scroll-snap", "collapsible-section", "quadrant-stepper", "pill-input-field", "loading-icon", "toast-swipe-dismiss", "pill-button", "icon-label-button"],
     ["showcase", "scroll", "composite", "feed"]),

    ("uitk", "dropdown-phone-entry", "DropDownPhoneEntry.md", "Dropdown Phone Entry", "Forms",
     "A phone-number entry form that pairs a country-code dropdown picker with pill input fields.",
     ["dropdown", "pill-input-field", "pill-button"],
     ["forms", "dropdown", "phone", "input"]),

    ("uitk", "image-crop-overlay", "ImageCropOverlayDemo.md", "Image Crop Overlay", "Media",
     "Pick an avatar image, then pan, pinch-zoom and crop it inside a full-screen modal overlay.",
     ["image-crop-overlay", "circular-image-button", "pill-button"],
     ["media", "image", "crop", "avatar"]),

    ("uitk", "notification-list", "NotificationList.md", "Notification List", "Feedback",
     "A scrollable notification feed with unread-count badges and an elastic, swipe-to-load-more list.",
     ["elastic-list-view", "notification-badge", "pill-button"],
     ["feedback", "list", "notifications", "badge"]),

    ("uitk", "profile-editor", "ProfileEditor.md", "Profile Editor", "Forms",
     "An editable profile screen with an avatar, toggles, and colour-tinted option groups.",
     ["toggle-button", "color-toggle-button", "color-toggle-group", "circular-image-button", "grayscale-image"],
     ["forms", "profile", "toggle", "avatar"]),

    ("uitk", "registration-form", "RegistrationForm.md", "Registration Form", "Forms",
     "A complete mobile-style registration flow with input validation and shake feedback on errors.",
     ["pill-input-field", "rounded-input-field", "pill-selector", "pill-button"],
     ["forms", "registration", "validation", "shake"]),

    ("uitk", "screen-header", "ScreenHeader.md", "Screen Header", "Navigation",
     "Demonstrates the configurable top app-bar: title, notch spacer, and the edge action buttons with their events.",
     ["screen-header"],
     ["navigation", "header", "appbar", "actions"]),

    ("uitk", "scroll-snap-and-dots", "ScrollSnapAndDots.md", "Scroll Snap & Dots", "Navigation",
     "A paged onboarding carousel — a swipeable scroll-snap container kept in sync with page-dot indicators.",
     ["scroll-snap", "page-dot-indicator", "coming-soon-message", "pill-button"],
     ["navigation", "scroll", "pagination", "onboarding"]),

    ("uitk", "scroll-snap-split", "ScrollSnapSplit.md", "Scroll Snap (Split Views)", "Navigation",
     "The same scroll-snap built three ways — pure C#, UXML, and a split layout — to compare authoring styles.",
     ["scroll-snap"],
     ["navigation", "scroll", "uxml", "csharp"]),

    ("uitk", "social-links", "SocialLinks.md", "Social Links", "Forms",
     "An editable social-links section with add/remove rows and a platform picker that hides already-used platforms.",
     ["social-link-container", "pill-button"],
     ["forms", "social", "links", "editable"]),

    ("uitk", "step-wizard", "StepWizard.md", "Step Wizard", "Forms",
     "A multi-step wizard flow with a step progress bar and per-step inputs.",
     ["step-progress-bar", "quadrant-stepper", "rounded-input-field", "pill-button"],
     ["forms", "wizard", "steps", "progress"]),

    ("uitk", "toast-notifications", "ToastNotifications.md", "Toast Notifications", "Feedback",
     "Queued toast messages with swipe-to-dismiss gesture handling.",
     ["toast-swipe-dismiss", "pill-button"],
     ["feedback", "toast", "notifications", "swipe"]),

    # ── uGUI ──────────────────────────────────────────────────────────────────
    ("ugui", "accordion", "Accordion.md", "Accordion", "Layout",
     "Expandable/collapsible panel sections that animate open and closed.",
     ["accordion"], ["layout", "accordion", "collapse"]),

    ("ugui", "card-ui", "CardUI.md", "Card UI", "Layout",
     "2D and 3D card stack, popup, and expand animations for presenting content.",
     ["card-ui"], ["layout", "card", "animation"]),

    ("ugui", "color-picker", "ColorPicker.md", "Color Picker", "Input",
     "A full HSV/RGB colour picker with sliders, presets, and a hex field.",
     ["color-picker"], ["input", "color", "picker"]),

    ("ugui", "combobox", "ComboBox.md", "ComboBox & Dropdowns", "Input",
     "Compares the ComboBox, AutoComplete ComboBox, and DropDown List selection controls side by side.",
     ["combobox", "autocomplete-combobox", "dropdown-list"], ["input", "combobox", "dropdown"]),

    ("ugui", "cooldown-button", "Cooldown.md", "Cooldown Button", "Input",
     "A button with a radial cooldown timer that blocks re-press until it elapses.",
     ["cooldown-button"], ["input", "button", "cooldown"]),

    ("ugui", "curly-ui", "CurlyUI.md", "CurlyUI", "Effects",
     "Bends UI text and images along an editable bezier curve.",
     ["curly-ui"], ["effects", "curve", "bezier"]),

    ("ugui", "fancy-scroll-view", "FancyScrollView.md", "Fancy Scroll View", "Layout",
     "High-performance virtualised scroll views — basic, focus-on, infinite, metaball, and voronoi demos.",
     ["fancy-scroll-view"], ["layout", "scroll", "virtual", "performance"]),

    ("ugui", "flow-layout-group", "FlowLayoutGroup.md", "Flow Layout Group", "Layout",
     "Wraps child elements into rows or columns, like CSS flexbox.",
     ["flow-layout-group"], ["layout", "flow", "wrap"]),

    ("ugui", "grid-raw-image", "GridRawImage.md", "Grid Raw Image", "Primitives",
     "Renders a configurable grid of cells within a single RawImage.",
     ["grid-raw-image"], ["primitives", "grid", "image"]),

    ("ugui", "scroll-snaps", "ScrollSnaps.md", "Scroll Snaps (Horizontal / Vertical / Infinite)", "Layout",
     "Paged horizontal, vertical, content, and infinite scroll-snap containers with pagination.",
     ["horizontal-scroll-snap", "vertical-scroll-snap", "content-scroll-snap-horizontal", "infinite-scroll-snap"],
     ["layout", "scroll", "snap", "pagination"]),

    ("ugui", "input-field-enter-submit", "InputFieldEnterSubmit.md", "Input Field Enter Submit", "Utilities",
     "Submits an InputField when Enter is pressed and refocuses for the next entry.",
     ["input-field-enter-submit"], ["utilities", "input", "submit"]),

    ("ugui", "menu-system", "MenuExample.md", "Menu System", "Navigation",
     "A stack-based menu manager driving animated menu screens.",
     ["menu-system"], ["navigation", "menu", "stack"]),

    ("ugui", "radial-slider", "RadialSlider.md", "Radial Slider", "Input",
     "A circular slider whose value is set by dragging around an arc.",
     ["radial-slider"], ["input", "slider", "radial"]),

    ("ugui", "reorderable-list", "ReorderableList.md", "Reorderable List", "Layout",
     "Drag-to-reorder list items within a list and between lists.",
     ["reorderable-list"], ["layout", "list", "drag", "reorder"]),

    ("ugui", "scroll-conflict-manager", "ScrollRectConflictManager.md", "Scroll Rect Conflict Manager", "Utilities",
     "Resolves nested horizontal/vertical ScrollRect drag conflicts.",
     ["scroll-conflict-manager"], ["utilities", "scroll", "nested"]),

    ("ugui", "selection-box", "SelectionBox.md", "Selection Box", "Input",
     "Drag a marquee box to multi-select items.",
     ["selection-box"], ["input", "selection", "marquee"]),

    ("ugui", "ui-circle-progress", "UICircleProgress.md", "UI Circle Progress", "Primitives",
     "Uses UICircle as an animated radial progress indicator.",
     ["ui-circle"], ["primitives", "circle", "progress"]),

    ("ugui", "ui-circle-segmented", "UICircleSegmented.md", "UI Circle Segmented", "Primitives",
     "A segmented circular gauge with configurable fill segments.",
     ["ui-circle-segmented"], ["primitives", "circle", "gauge"]),

    ("ugui", "ui-knob", "UIKnob.md", "UI Knob", "Input",
     "A rotary knob control driven by drag input.",
     ["ui-knob"], ["input", "knob", "rotary"]),

    ("ugui", "ui-line-renderer", "UILineRenderer.md", "UI Line Renderer", "Primitives",
     "Draws polylines in UI space, including the list-based variant.",
     ["ui-line-renderer", "ui-line-renderer-list"], ["primitives", "line", "renderer"]),

    ("ugui", "ui-particle-system", "UIParticleSystem.md", "UI Particle System", "Effects",
     "Renders Shuriken-style particles inside the UI canvas.",
     ["ui-particle-system"], ["effects", "particles"]),

    ("ugui", "ui-vertical-scroller", "UIVerticalScroller.md", "UI Vertical Scroller", "Layout",
     "A vertical scroller that scales and highlights the centred item.",
     ["ui-vertical-scroller"], ["layout", "scroll", "vertical"]),
]


def parse_controls(yml_path):
    """slug -> {name, permalink} from a *_controls.yml file (simple line parse)."""
    out = {}
    name = slug = permalink = None
    with open(yml_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^- name:\s*(.*)", line)
            if m:
                name = m.group(1).strip().strip('"')
            m = re.match(r"^  slug:\s*(.*)", line)
            if m:
                slug = m.group(1).strip()
            m = re.match(r"^  permalink:\s*(.*)", line)
            if m:
                permalink = m.group(1).strip()
                if slug:
                    out[slug] = {"name": name, "permalink": permalink}
    return out


def yml_escape(s):
    if re.search(r'[:"\'#]', s) or s.strip() != s:
        return '"' + s.replace('"', '\\"') + '"'
    return s


def write_data_yml(pkg, entries, controls_map):
    cfg = PKG[pkg]
    lines = [
        f"# {cfg['title']} — {len(entries)} example scenes",
        "# Generated by create_example_pages.py — do not edit by hand.",
        "# Each example lists the controls it demonstrates (drives the examples",
        "# browser, the per-control \"Demonstrated In\" block, and cross-links).",
        "",
    ]
    for e in entries:
        controls = [controls_map.get(s) for s in e["controls"]]
        controls = [c for c in controls if c]
        permalinks = " ".join(c["permalink"] for c in controls)
        lines.append(f"- name: {yml_escape(e['name'])}")
        lines.append(f"  slug: {e['slug']}")
        lines.append(f"  permalink: {cfg['examples_base']}{e['slug']}/")
        lines.append(f"  category: {e['category']}")
        lines.append(f"  description: {yml_escape(e['description'])}")
        lines.append(f"  preview_image: \"\"")
        lines.append(f"  has_video: false")
        lines.append(f"  tags: [{', '.join(e['tags'])}]")
        lines.append(f"  control_permalinks: \"{permalinks}\"")
        lines.append(f"  controls:")
        for c in controls:
            lines.append(f"    - name: {yml_escape(c['name'])}")
            lines.append(f"      permalink: {c['permalink']}")
        lines.append("")
    with open(cfg["data_yml"], "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(f"  wrote {os.path.relpath(cfg['data_yml'], BASE)} ({len(entries)} entries)")


# UITK package example docs link to control docs as ../Controls/<File>.md.
# Map those filenames to website control URLs so generated pages link correctly.
UITK_DOCFILE_TO_SLUG = {
    "ScrollSnap": "scroll-snap", "CollapsibleSection": "collapsible-section",
    "QuadrantStepper": "quadrant-stepper", "PillInputField": "pill-input-field",
    "RoundedInputField": "rounded-input-field", "PillSelector": "pill-selector",
    "ToggleButton": "toggle-button", "ColorToggleButton": "color-toggle-button",
    "ColorToggleGroup": "color-toggle-group", "StepProgressBar": "step-progress-bar",
    "PageDotIndicator": "page-dot-indicator", "LoadingIcon": "loading-icon",
    "ToastSwipeDismissManipulator": "toast-swipe-dismiss", "ComingSoonMessage": "coming-soon-message",
    "PillButton": "pill-button", "CircularImageButton": "circular-image-button",
    "IconLabelButton": "icon-label-button", "GrayscaleImage": "grayscale-image",
    "DropDownControl": "dropdown", "ImageCropOverlayControl": "image-crop-overlay",
    "DropDownMenuControl": "dropdown-menu", "ScreenHeader": "screen-header",
    "ElasticListView": "elastic-list-view", "NotificationBadge": "notification-badge",
    "SocialLinkContainer": "social-link-container",
}


def rewrite_uitk_control_links(body):
    def repl(m):
        fname = m.group(1)
        slug = UITK_DOCFILE_TO_SLUG.get(fname)
        return f"](/uitoolkit/controls/{slug}/)" if slug else m.group(0)
    # ](../Controls/PillButton.md)  and  ](../Controls/PillButton)
    body = re.sub(r"\]\(\.\./Controls/([A-Za-z0-9_]+)(?:\.md)?\)", repl, body)
    # Any remaining relative .md link (e.g. package utility docs not on the site):
    # collapse [Text](../something.md) -> Text so we never emit a broken link.
    body = re.sub(r"\[([^\]]+)\]\(\.{1,2}/[^)]*\.md\)", r"\1", body)
    return body


def _yq(s):
    # Escape for a YAML double-quoted scalar.
    return s.replace("\\", "\\\\").replace('"', '\\"')


def make_front_matter(pkg, e, controls):
    cfg = PKG[pkg]
    tags = "[" + ", ".join(e["tags"]) + "]"
    fm = [
        "---",
        f"layout: {cfg['layout']}",
        f'title: "{_yq(e["name"])}"',
        f'description: "{_yq(e["description"])}"',
        f'category: "{_yq(e["category"])}"',
        f"permalink: {cfg['examples_base']}{e['slug']}/",
        f"tags: {tags}",
        "controls:",
    ]
    for c in controls:
        fm.append(f'  - name: "{_yq(c["name"])}"')
        fm.append(f"    permalink: {c['permalink']}")
    fm.append("---")
    fm.append("")
    fm.append("")
    return "\n".join(fm)


def write_pages(pkg, entries, controls_map):
    cfg = PKG[pkg]
    os.makedirs(cfg["out_dir"], exist_ok=True)
    made = skipped = 0
    for e in entries:
        controls = [controls_map.get(s) for s in e["controls"]]
        controls = [c for c in controls if c]
        src = os.path.join(cfg["src_dir"], e["src"])
        if not os.path.exists(src):
            print(f"  PENDING DOC: {pkg}/{e['slug']}  (missing {e['src']})")
            skipped += 1
            continue
        with open(src, encoding="utf-8") as f:
            body = f.read()
        body = re.sub(r"^#\s+\S[^\n]*\n+", "", body, count=1)  # strip leading H1
        if pkg == "uitk":
            body = rewrite_uitk_control_links(body)
        out_dir = os.path.join(cfg["out_dir"], e["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(make_front_matter(pkg, e, controls) + body)
        made += 1
    print(f"  {pkg}: {made} pages generated, {skipped} pending docs")


def main():
    controls = {p: parse_controls(PKG[p]["controls_yml"]) for p in PKG}
    for pkg in PKG:
        entries = [dict(zip(
            ["pkg", "slug", "src", "name", "category", "description", "controls", "tags"], e))
            for e in EXAMPLES if e[0] == pkg]
        print(f"== {pkg} ({len(entries)} examples) ==")
        write_data_yml(pkg, entries, controls[pkg])
        write_pages(pkg, entries, controls[pkg])


if __name__ == "__main__":
    main()
