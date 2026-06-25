# Missing Demo Content — uGUI &amp; UI Toolkit Controls

The controls listed here now have **complete documentation pages and are listed**
on the site (shown with a placeholder card) — they are only **missing demo media**
(screenshots / GIFs).

To add demo media: drop at least one screenshot or GIF into `ugui/images/`,
reference it in the control's `.md` file, set `preview_image` for the control in
`_data/ugui_controls.yml`, then remove it from this list.

---

## uGUI Controls Pending Demo Media (43)

> Count derived from `_data/ugui_controls.yml`: of 101 controls, **58** have a
> `preview_image` and **43** are still blank (`preview_image: ""`). The 43 blank
> entries are listed below.

| Control | File | Notes |
|---|---|---|
| BestFitOutline | `ugui/controls/best-fit-outline/index.md` | Text effect — needs before/after screenshot |
| BoundToolTip | `ugui/controls/bound-tooltip/index.md` | Tooltip variant — needs inspector screenshot |
| CLFZ2 | `ugui/controls/clzf2-compression/index.md` | Compression utility — needs usage screenshot |
| CurvedLayout | `ugui/controls/curved-layout/index.md` | Layout — needs arc arrangement demo |
| CurvedText | `ugui/controls/curved-text/index.md` | Text effect — needs curve demo screenshot |
| CylinderText | `ugui/controls/cylinder-text/index.md` | Text effect — needs cylinder wrap demo |
| DragCorrector | `ugui/controls/drag-corrector/index.md` | Utility — needs inspector screenshot |
| ExtensionsToggle | `ugui/controls/extensions-toggle/index.md` | Toggle — needs screenshot |
| ExtensionsToggleGroup | `ugui/controls/extensions-toggle-group/index.md` | Toggle group — needs screenshot |
| GamePadInputModule | `ugui/controls/gamepad-input-module/index.md` | Input module — needs inspector screenshot |
| HoverToolTip | `ugui/controls/hover-tooltip/index.md` | Tooltip — needs hover state GIF |
| ImageExtended | `ugui/controls/image-extended/index.md` | Image extension — needs screenshot |
| Infinite Scroll Snap | `ugui/controls/infinite-scroll-snap/index.md` | Scroll — needs demo GIF (note: has `InfiniteScrollInspector.jpg` in Images/ but not linked) |
| InputFieldEnterSubmit | `ugui/controls/input-field-enter-submit/index.md` | Input utility — needs demo GIF |
| InputFocus | `ugui/controls/input-focus/index.md` | Input utility — needs demo GIF |
| MinMaxSlider | `ugui/controls/min-max-slider/index.md` | Slider — needs screenshot (note: has no image files in Images/) |
| MultiTouchScrollRect | `ugui/controls/multitouch-scroll-rect/index.md` | ScrollRect fix — no visual change, needs usage note |
| NicerOutline | `ugui/controls/nicer-outline/index.md` | Outline effect — needs before/after screenshot |
| PPIViewer | `ugui/controls/ppi-viewer/index.md` | Utility — needs runtime screenshot |
| RaycastMask | `ugui/controls/raycast-mask/index.md` | Utility — needs hit-area demo screenshot |
| RescaleDragPanel | `ugui/controls/rescale-drag-panel/index.md` | Panel — needs resize GIF |
| RescalePanel | `ugui/controls/rescale-panel/index.md` | Panel — needs resize GIF |
| ResizePanel | `ugui/controls/resize-panel/index.md` | Panel — needs resize GIF |
| ReturnKeyTrigger | `ugui/controls/return-key-trigger/index.md` | Input utility — needs demo GIF |
| Scroller | `ugui/controls/scroller/index.md` | Scroll utility — needs screenshot |
| Serialization | `ugui/controls/serialization/index.md` | Utility — needs usage code example or screenshot |
| ShaderEffects | `ugui/controls/shader-effects/index.md` | Effects — needs screenshot |
| UIHorizontalScroller | `ugui/controls/ui-horizontal-scroller/index.md` | Layout — needs horizontal scrolling demo screenshot or GIF |
| UICircle | `ugui/controls/ui-circle/index.md` | Primitive — needs shape screenshot |
| UICornerCut | `ugui/controls/ui-corner-cut/index.md` | Effect — needs before/after screenshot |
| UIImageCrop | `ugui/controls/ui-image-crop/index.md` | Image utility — needs crop demo screenshot |
| UILineRendererFIFO | `ugui/controls/ui-line-renderer-fifo/index.md` | Line renderer variant — needs demo |
| UILineRendererList | `ugui/controls/ui-line-renderer-list/index.md` | Line renderer variant — needs demo |
| UILineTextureRenderer | `ugui/controls/ui-line-texture-renderer/index.md` | Line renderer variant — needs demo |
| UISquircle | `ugui/controls/ui-squircle/index.md` | Primitive — needs squircle shape screenshot |
| UIWindowBase | `ugui/controls/ui-window-base/index.md` | Window — needs screenshot |
| switchToRectTransform | `ugui/controls/switch-to-recttransform/index.md` | Utility — needs inspector/usage screenshot |
| Diamond Graph | `ugui/controls/diamond-graph/index.md` | Primitive — needs radar/stat-graph screenshot |
| Grid Raw Image | `ugui/controls/grid-raw-image/index.md` | Primitive — needs grid render screenshot |
| Radial Layout | `ugui/controls/radial-layout/index.md` | Layout — needs radial arrangement screenshot |
| UI Circle Segmented | `ugui/controls/ui-circle-segmented/index.md` | Primitive — needs segmented-circle screenshot |
| UI Graphic Sector | `ugui/controls/ui-graphic-sector/index.md` | Primitive — needs sector/arc screenshot |
| UI Vertical Scroller | `ugui/controls/ui-vertical-scroller/index.md` | Layout — needs vertical scrolling demo GIF |

---

## UIToolkit Controls — Missing Visual Demos

All 25 UIToolkit controls have **complete text documentation and code examples** but  
**no screenshots or animated demos** yet. They appear on the UIToolkit controls page  
but are marked as lacking visual reference.

| Control | Priority | Notes |
|---|---|---|
| ScrollSnap | High | Core navigation control — needs swipe demo GIF |
| ScreenHeader | High | Top app-bar with title + action buttons — needs screenshot |
| ElasticListView | High | Elastic overscroll + load-more — needs on-device GIF |
| Dropdown | High | Wheel-style value picker — needs modal-open GIF |
| DropDownMenuControl | Medium | Anchored action menu — needs open/overlay GIF |
| SocialLinkContainer | Medium | Editable social links list — needs add/remove GIF |
| NotificationBadge | Medium | Unread-count badge — needs overlay screenshot |
| ImageCropOverlay | Medium | Modal cropper — needs pan/zoom GIF |
| CollapsibleSection | High | Visible expand/collapse — easy GIF to capture |
| StepProgressBar | High | Visual fill progress — needs progress demo |
| PillButton | High | Primary CTA — needs flash animation GIF |
| ColorToggleGroup | High | Tap/drag selection — needs interaction GIF |
| PageDotIndicator | Medium | Pagination dots — needs animated GIF |
| QuadrantStepper | Medium | Step selector overlay — needs GIF |
| PillInputField | Medium | Input with label — needs screenshot |
| RoundedInputField | Medium | Rounded input — needs screenshot |
| PillSelector | Medium | Selector row — needs screenshot |
| CircularImageButton | Medium | Avatar button — needs screenshot |
| GrayscaleImage | Medium | Shader effect — needs before/after |
| LoadingIcon | Medium | Spinner — needs rotation GIF |
| IconLabelButton | Low | Row button — needs screenshot |
| ToggleButton | Low | Toggle — needs screenshot |
| ColorToggleButton | Low | Tinted toggle — needs screenshot |
| ToastSwipeDismissManipulator | Low | Utility manipulator — needs swipe GIF |
| ComingSoonMessage | Low | Placeholder panel — needs screenshot |

---

## How to Contribute Demo Content

1. Capture a screenshot or GIF of the control in action in the Unity Editor or Play Mode
2. Name the file clearly: e.g. `UICircleDemo.gif` or `UICircleInspector.jpg`
3. Place it in `ugui/images/` (for uGUI) or `uitoolkit/controls/images/` (for UIToolkit)
4. Reference it in the control's `.md` file
5. Remove the control from this list (or update its row if it still needs video)
6. The control will automatically appear on the controls listing page on next build
