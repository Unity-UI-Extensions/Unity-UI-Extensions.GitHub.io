# Missing Demo Content — uGUI Controls

The controls listed here now have **complete documentation pages and are listed**
on the site (shown with a placeholder card) — they are only **missing demo media**
(screenshots / GIFs).

To add demo media: drop at least one screenshot or GIF into `Controls/Images/`,
reference it in the control's `.md` file, set `preview_image` for the control in
`_data/ugui_controls.yml`, then remove it from this list.

---

## uGUI Controls Pending Demo Media (37)

| Control | File | Notes |
|---|---|---|
| BestFitOutline | `Controls/BestFitOutline.md` | Text effect — needs before/after screenshot |
| BoundToolTip | `Controls/BoundToolTip.md` | Tooltip variant — needs inspector screenshot |
| CLFZ2 | `Controls/CLFZ2.md` | Compression utility — needs usage screenshot |
| CurvedLayout | `Controls/CurvedLayout.md` | Layout — needs arc arrangement demo |
| CurvedText | `Controls/CurvedText.md` | Text effect — needs curve demo screenshot |
| CylinderText | `Controls/CylinderText.md` | Text effect — needs cylinder wrap demo |
| DragCorrector | `Controls/DragCorrector.md` | Utility — needs inspector screenshot |
| ExtensionsToggle | `Controls/ExtensionsToggle.md` | Toggle — needs screenshot |
| ExtensionsToggleGroup | `Controls/ExtensionsToggleGroup.md` | Toggle group — needs screenshot |
| GamePadInputModule | `Controls/GamePadInputModule.md` | Input module — needs inspector screenshot |
| HoverToolTip | `Controls/HoverToolTip.md` | Tooltip — needs hover state GIF |
| ImageExtended | `Controls/ImageExtended.md` | Image extension — needs screenshot |
| Infinite Scroll Snap | `Controls/Infinite Scroll Snap.md` | Scroll — needs demo GIF (note: has `InfiniteScrollInspector.jpg` in Images/ but not linked) |
| InputFieldEnterSubmit | `Controls/InputFieldEnterSubmit.md` | Input utility — needs demo GIF |
| InputFocus | `Controls/InputFocus.md` | Input utility — needs demo GIF |
| MinMaxSlider | `Controls/MinMaxSlider.md` | Slider — needs screenshot (note: has no image files in Images/) |
| MultiTouchScrollRect | `Controls/MultiTouchScrollRect.md` | ScrollRect fix — no visual change, needs usage note |
| NicerOutline | `Controls/NicerOutline.md` | Outline effect — needs before/after screenshot |
| PPIViewer | `Controls/PPIViewer.md` | Utility — needs runtime screenshot |
| RaycastMask | `Controls/RaycastMask.md` | Utility — needs hit-area demo screenshot |
| RescaleDragPanel | `Controls/RescaleDragPanel.md` | Panel — needs resize GIF |
| RescalePanel | `Controls/RescalePanel.md` | Panel — needs resize GIF |
| ResizePanel | `Controls/ResizePanel.md` | Panel — needs resize GIF |
| ReturnKeyTrigger | `Controls/ReturnKeyTrigger.md` | Input utility — needs demo GIF |
| Scroller | `Controls/Scroller.md` | Scroll utility — needs screenshot |
| Serialization | `Controls/Serialization.md` | Utility — needs usage code example or screenshot |
| ShaderEffects | `Controls/ShaderEffects.md` | Effects — needs screenshot |
| UIHorizontalScroller | `Controls/UIHorizontalScroller.md` | Layout — needs horizontal scrolling demo screenshot or GIF |
| UICircle | `Controls/UICircle.md` | Primitive — needs shape screenshot |
| UICornerCut | `Controls/UICornerCut.md` | Effect — needs before/after screenshot |
| UIImageCrop | `Controls/UIImageCrop.md` | Image utility — needs crop demo screenshot |
| UILineRendererFIFO | `Controls/UILineRendererFIFO.md` | Line renderer variant — needs demo |
| UILineRendererList | `Controls/UILineRendererList.md` | Line renderer variant — needs demo |
| UILineTextureRenderer | `Controls/UILineTextureRenderer.md` | Line renderer variant — needs demo |
| UISquircle | `Controls/UISquircle.md` | Primitive — needs squircle shape screenshot |
| UIWindowBase | `Controls/UIWindowBase.md` | Window — needs screenshot |
| switchToRectTransform | `Controls/switchToRectTransform.md` | Utility — needs inspector/usage screenshot |

---

## UIToolkit Controls — Missing Visual Demos

All 20 UIToolkit controls have **complete text documentation and code examples** but  
**no screenshots or animated demos** yet. They appear on the UIToolkit controls page  
but are marked as lacking visual reference.

| Control | Priority | Notes |
|---|---|---|
| ScrollSnap | High | Core navigation control — needs swipe demo GIF |
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
3. Place it in `Controls/Images/` (for uGUI) or `uitoolkit/controls/images/` (for UIToolkit)
4. Reference it in the control's `.md` file
5. Remove the control from this list (or update its row if it still needs video)
6. The control will automatically appear on the controls listing page on next build
