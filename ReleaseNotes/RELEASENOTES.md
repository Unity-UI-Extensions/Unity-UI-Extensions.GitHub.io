# Unity UI Extensions release notes

This file contains the up to date release notes for each release of the UI Extensions project including release videos where required.

----------------

## 2019.6 - 2.5 - Bug squash

Its been a while since the last update and although Unity keeps changing, thankfully the parts underneath do not.  THanks to some awesome work by our contributors and the test teams, we made a run on some underlying bugs and issues.  If you spot anything else, please log it on the BitBucket site for resolution.

> Be sure to logon to the new [Gitter Chat](https://gitter.im/Unity-UI-Extensions/Lobby) site for the UI Extensions project, if you have any questions, queries or suggestions
>
> Much easier that posting a question / issue on YouTube, Twitter or Facebook :D
>
> ## [UIExtensions Gitter Channel](https://gitter.im/Unity-UI-Extensions/Lobby)


### Added

Nothing new this time, bugfix release.

### Changed

- Updated UI Line connector to use relative position instead of anchored position to verify if the Lines need updating.
- Allow menu prefabs to not have to have canvas components. This allows you to use any type of prefab as a "menu". Adam Kapos mentions the concept on the Unite talk, https://youtu.be/wbmjturGbAQ?t=1654
- Updated segment line drawing for Line Lists. Seems Unity no longer needs UV's to be wrapped manually.
- Updated the AutoCompleteComboBox to display text as entered (instead of all lowercase)
- Updated the ComboBox to display text as entered (instead of all lowercase)
- Updated ComboBox Examples to include programmatic versions
- Further ComboBox improvements including:
  * Upwards panel
  * Start fixes
  * Item Template resize
  * Disabled sorting on combobox as it wasn't working
  * Disabled Slider handle when not in use
  * Updated Example
- Updated the new Input system switch and tested against 2021

### Deprecated

None

### Fixed

- Reordering issue resolved with ScrollRectOcclusion.
- Fixed Sorting at min and max positions for ScrollRect
- Updated ScrollToSelect script provided by zero3growlithe, tested and vastly reduces the previous jitter. Still present but barely noticeable now.
- Fixed Issue # 363 Update Combobox control that takes multiple items programmatically, to only allow distinct items
- Fixed the issues where dragging outside the range slider handle causes the range to update. - Resolves #369
- Resolves an issue with Unity putting the previous controls vertex array in an uninitialised control.
- Applied J.R. Mitchell's fix for the Accordion Controls/Accordion/AccordionElement.cs - resolves: #364
- Resolved issue where the Content Scroll snap issue with only 1 child. Resolves #362
- Updated the PaginationManager to override if the ScrollSnap is in motion.

### Removed

None


## Update 2019.5 - 2.3  - Accelerated Deployment

Since the move to UPM, the team have been able to react quicker and push out fixes a lot easier, without affecting previous installation (whilst still adhering to Unity's backwards compatibility pattern).  So it is with great news we announce this new release, faster that ever :D  (and thanks to UPM, easier to upgrade than ever).
Be sure to also check out the "Examples" option in the Package Manager window to import the samples to your project.


### New / updated features

* Add squircle primitive
* Adding new magnetic scroll control
* Added a static library to collate shaders on first use.
* Finalized new InputManagerHelper, which translates input based on the operating input system, new or old Updated CardStack2D to have defined keyboard input or specific gamepad input over the older axisname for new input system.
* Examples now included with UPM delivery and available as a button on the UPM package manager window
* Updated DropDown and Autocomplete controls based on feedback in #204
* Updated Accordion to support both Vertical as well as Horizontal layout
* Updated ComboBox controls to improve better programmatic controls
* Updates to the Infinite scroll to support content of various sizes
* Updated UI Knob control - enabled dragging outside the target area, added example scene
* Minor update to MagneticInfinite Scroll
* Refactored and extended the ContentScrollSnap control
* Added protection against errors and empty scrollrect content
* Added new SetNewItems function to add children programmatically to the control and reset accordingly
* Patch supplied by a contributor to improve the texture sheet use with the UIParticlesystem
* Added "SetKnobValue" function which allows the setting of Value and loops
* Added the programmatic capability to change the parent scroll rect on the ScrollConflictManager at runtime.

### Examples / Examples / Examples

Examples now have their own package, this simplifies their use and deployment. Especially in 2019 with the UPM deployment.

* New UI Knob examples
* New Magnetic Scroll Example
* Updated ComboBox examples for programmatic testing

### Fixes

* Fix to add a "RequireComponent" to Primitives as Unity 2020 does not add them by default
* Remove old Examples submodule
* Updated submodules to hide Examples folder Additionally, updated Package manifest to allow importing of examples direct from UPM package.
* Fixed hard swipe to ensure it only ever moves one page, no matter how far you swipe.
* Fixed a conflict when using the ScrollConflictManager in child content of a HSS or VSS
* Fix for UI Particle system looping
* Fixed public GoToScreen call to only raise events internally (not multiple)
* Final roll-up and fix. Resolved race condition for associated pagination controls.
* Fixed issue with page events not being raised when inertia was disabled (velocity was always zero)
* When cloned, reorderable list was creating a second List Content component that was not initialized. Refactored to ensure only one list content was present and is initialized correctly
* Reorderable list items marked as transferable, remain transferable after being dropped
* Patch to resolve issues without the new Input System installed
* Refined magnetic scroll and dependencies while documenting Updated example
* Patch Tooltip

### Known issues

No new issues in this release, but check the issues list for things we are currently working on:

* [UI Extensions Issue log](https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues)

## [Installation Instructions](/GettingStarted.md)

As of Unity 2019, there are now two paths for getting access to the Unity UI Extensions project:

- Unity 2019 or higher
The recommended way to add the Unity UI Extensions project to your solution is to use the Unity package Manager. Simply use the Unity Package Manager to reference the project to install it

Alternatively, you can also use the pre-compiled Unity packages if you wish, however, UPM offers full versioning support to allow you to switch versions as you wish.

- Unity 2018 or lower
The pre-compiled Unity assets are the only solution for Unity 2018 or earlier due to the changes in the Unity UI framework in Unity made for 2019.
Either clone / download this repository to your machine and then copy the scripts in, or use the pre-packaged .UnityPackage for your version of Unity and import it as a custom package in to your project.

## Upgrade Notes

Due to the restructure of the package to meet Unity's new package guidelines, we recommend **Deleting the current Unity UI Extensions** folder prior to importing the new package.

For Unity 2019 users using the new UPM deployment, be sure to delete the existing folder in your assets folder before adding the new package to avoid conflict.

----------------

## Update 2019.4 - 2.2  - Back from the future

It's been a long year since the last official release of the Unity UI Extensions project and WOW, have there been a lot of ups and downs.  Big thanks to the community for their support of the project whether that was funds, code or even just testing and helping to iron out some pesky bugs.

> Be sure to logon to the new [Gitter Chat](https://gitter.im/Unity-UI-Extensions/Lobby) site for the UI Extensions project, if you have any questions, queries or suggestions
>
> Much easier that posting a question / issue on YouTube, Twitter or Facebook :D
>
> ## [UIExtensions Gitter Channel](https://gitter.im/Unity-UI-Extensions/Lobby)

### New / updated features

* New UPM deployment for Unity 2019, 2018 will still need to use the asset packages due to Unity compatibility issues.
* Updated the project to the new Unity packaging guidelines, including separating out the examples to a separate package.
* Many line drawing updates, including the ability to draw using a mouse (check the examples)
* Scroll Snaps (HSS/VSS) now have a "Hard Swipe" feature to restrict movement to a single page for each swipe
* Scroll Snaps have also been updated to work better with the UIInfiniteScroll control
* New Unity Card UI controls thanks to @RyanslikeSoCool
* Update to the Fancy Scroll controls with even more added fanciness
* Several updates to adopt newer Unity standards in the controls to ensure full forwards and backwards compatibility

### Examples / Examples / Examples

Examples now have their own package, this simplifies their use and deployment. Especially in 2019 with the UPM deployment.

* Refreshed all examples for Unity 2019
* New Card UI Examples to supplement the new controls
* New Infinite Scroll Snap example
* Fancy Scroll view updated with 2 new examples
* New particle system example, demonstrating programmatic control of the particle system

### Fixes

* Mouse position use updated in
  * RadialSlider
  * ColorSampler
  * TiltWindow
* Check compiler warnings (#197)
* Line Renderer click to add lines (#183)
* ScrollSnap Swiping options - hard fast swipe (#176)
* Shader Loading issue / UIParticleSystem (#229)
* Issue where Menu Prefabs would be disabled instead of their Clones (#210)
* Check ScrollSnapBase update (#265)
* UIInfiniteScroller support for VSS updated and fixes
* Fix to allow radial slider to start from positions other than left
* Fix UI Particles: Texture sheet animation + Random row(#256)
* Fix for wandering ScrollSnap controls due to Local Positioning drift
* Divide By Zero fix for Gradient (#58)

### Known issues

No new issues in this release, but check the issues list for things we are currently working on:

----------------

## Update 2019.1 - formally v2.1  - Going with the times

Given that it's been a while since the last release and a fair few number of fixes have been introduced since the last update, it's only fair I get this point release out for the masses.
This is only a point release and we are still working hard on the next full update

### New / updated features

* Updated and tested with Unity 2018 / 2019
* FancyScrollView updated with newer version (note breaking change)
* Added test version of a LineRender control using a List instead of an array
* New CardUI layout control, for a snazzy flip card system
* New UI Circle Progress indicator control

### Examples / Examples / Examples
(All examples can be deleted without affecting the extensions)

* Added example for CardUI
* Added example for the LineRendererList experiment
* FancyScrollView examples updated to the new version
* Example for new UICircle progress control

### Fixes

* General clean up of build warnings
* Refactored primitive controls to be cleaner
* Various HSS / VSS updates, mostly from the community
* ScrollConflictManager updated to work better with nested HSS/VSS
* UI Knob resolved to with screen space camera
* Fix for the menu system, which was disabling prefabs instead of the scene instance
* Fixed shader in UIParticle System
* TextPic updated to support culling properly
* Reorderable List updated with additional options
* Screenspace overlay support added to the Tooltip control
* UIParticle system now supports 3D rotation
* UIVerticalScroller updated
* Radial slider updated with

### Known issues

No new issues in this release, but check the issues list for things we are currently working on:

* [UI Extensions Issue log](https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues)

## Upgrade Notes

No significant concerns, should be able to update over the 2.1 package.  If upgrading prior to 2.1, we still recommend removing the UnityUIExtensions folder and then re-importing

----------------

## Update 2.0 - The update so big they had to name it twice

[![View 2.0 update Video](http://img.youtube.com/vi/Ivzt9_jhGfQ/0.jpg)](https://www.youtube.com/watch?v=Ivzt9_jhGfQ "Update 2.0 for the Unity UI Extensions Project")

### New / updated features

* Major updates to the Line renderer for texture and positioning support, inc Editor support
* Line Renderer also includes "dotted" line support and the ability to increase the vertex count
* Reorderable list now also works in Screenspace-Camera & Worldspace
* H&V Scroll Snap controls now support scrollbars
* Minor updates to the Gradient 2 control
* Minor updates to all dropdown controls to manage control startup
* Update UI Particle Renderer with new updates, including Texture Sheet animation support
* New Selectable Scalar
* New MonoSpacing text effect
* New Multi-Touch Scrollrect support
* New UI Grid Renderer (handy if you want a UI grid background)
* New CoolDownButton control (adds a timer between button clicks)
* New Curly UI - for those who like their UI Bendy
* New Fancy Scroll View - A programmatic  scroll view
* New UI Line connector control - extends line renderer to draw lines between UI Objects
* New Radial Slider control - for those who like their sliders to curve
* New Stepper control - a +/- control similar to that found on iOS
* New Segmented Control - A button array control similar to that found on iOS
* New UIHighlightable control - just in case the user wasn't sure where they were

### Examples / Examples / Examples

Finally added some proper examples, especially for the newer controls.
These can be found in the Examples folder (which can be safely deleted if you wish)

* ColorPicker - shows the Color Picker UI in both SS and WS
* ComboBox - shows all the different combo box controls
* Cooldown - several example implementations of the cooldown button control using Unity image effects and SAUIM
* CurlyUI - shows off the CurlyUI control
* FancyScrollView - the only REAL way to understand this programmatic control (direct from the contributor)
* HSS-VSS-ScrollSnap - several working examples of the HSS/VSS scroll snaps (not ScrollSnap or FancyScrollView), including a full screen variant
* MenuExample - A demo menu implementation showing off the new MenuManager control
* Radial Slider - Just keep on sliding
* ReorderableList - Several examples of the re-orderable list in action, complete with managed drag / drop features
* ScrollConflictManager - Making ScrollRects get along
* SelectionBox - The RTS selector in action, showing examples of selecting 2D and 3D objects
* Serialisation - Unit test case examples for the serialisation components
* TextEffects - All the Text effects and shaders in one easy to view place
* UIlineRenderer - Several demos / examples for using the Line Renderer and UI Line connector controls
* UIVerticalScrollerDemo - A full screen example of a UIVertical Scroller implementation.

### Fixes

* H&V Scroll Snap Next/Previous Button interactable handler (only enables when there is a child to move to)
* H&V Scroll Snap Swipe logic updated and now includes scaling support
* Editor options for non-drawing graphic control
* Events in ComboBox, Dropdown and autocomplete controls updated to use UI events
* UIFlippable "Argument out of Range" bigfix (pesky component orders with effects)
* All primitive controls will now redraw when enabled in code
* Autocomplete has two lookup text methods now, Array and Linq
* Line renderer pivot fix (now respects the pivot point)
* TextPic rendering and event updates
* Minor tweaks to the UIParticle system to remove "upgrade" errors. Still needs a rework tbh
* Clean up of all unnecessary usings (swept under the rug)

### Known issues

Serialisation functionality has been removed due to several incompatibilities between platforms, suggest the UniversalSerialiser as an alternative. May bring back if there is demand. (or copy out the source from the previous release)

## Upgrade Notes

With this being a major version update, it is recommended to remove the old UI Extensions folder before importing the new asset.

----------------

## Update 1.2

[![View 1.2 update Video](http://img.youtube.com/vi/cWv0A6rEEc8/0.jpg)](https://www.youtube.com/watch?v=cWv0A6rEEc8 "Update 1.2 for the Unity UI Extensions Project")

### New / updated features

* Major updates to the Horizontal and Vertical Scroll Snap controls
* Replacement HSV/Color picker control (and new Box Slider control)
* Fixes / updates to the TextPic control
* Updates to SoftAlphaUI script - improved Text / worldspace support
* Updates to Extensions Toggle - Adds ID and event to publish ID on change
* New Gadient control (gradient 2)
* New UI ScrollRect Occlusion utility
* New UI Tween Scale utility
* New UI Infinite ScrollRect
* New Table Layout Group

### Fixes

* H&V Scroll Snap indexing issues
* H&V Scroll Snap performance updates 
* H&V Scroll Snap Long swipe behavior updated
* H&V Scroll Snap support for Rect Resizing
* TextPic Set set before draw issues
* HSV picker replaced with more generic color picker

### Known issues

* The Image_Extended control has been removed due to Unity upgrade issues. Will return in a future update.

## Upgrade Notes

Although not specifically required, it is recommended to remove the old UI Extensions folder before importing the new asset
The HSS picker especially had a lot of file changes in this update.

>**Note** In Unity 5.5 the particle system was overhauled and several methods were marked for removal. However, the UI Particle System script currently still uses them
> Either ignore these errors or remove the *_UIParticleSystem_* script in the "*Unity UI Extensions / Scripts / Effects*" folder

----------------

## Update 1.1

[![View 1.1 update Video](http://img.youtube.com/vi/JuE0ja5DmV4/0.jpg)](https://www.youtube.com/watch?v=JuE0ja5DmV4 "Update 1.1 for the Unity UI Extensions Project")

> **Note** for 4.6 / 5.1, some features will not be available due to their incompatibility.
> Also the Line Renderer remains unchanged in these releases as the updates do not work with the older system

### New / updated features

* New Polygon primitive
* New UI Vertical Scroller control
* New Curved layout component
* New Shining effect
* New UI Particle system **<-5.3+ only**
* New Scroll Conflict Manager
* Soft Alpha Mask updated in line with SAUI 1.3 release
* Line Renderer has had a complete overhaul, including full programmatic support, Line list and Bezier line rendering
* Horizontal and Vertical Scroll Snaps updated to include a Starting page, current page and transition speed parameters. Plus a new GoToPage, Add and Remove page functions
* Added some script helper functions for LZF compression and Serialization
* Two utilities to help manage drag thresholds on high PPI systems

### Fixes

* Line Render almost completely re-written with tons of fixes
* Radial layout updated to avoid 360 overlap (first and last)
* Scroll Snaps updates to better handle children.
* Scroll Snaps distribute function updated so it can be called onDirty more efficiently.

## Upgrade Notes

Two scripts were moved and need their originals need deleting post upgrade.  Please remove the following files:
* Scripts\ImageExtended
* Scripts\UIImageCrop

----------------

## Update 1.0.6.1

- Minor update to enhance soft alpha mask and add cylinder text plus a fix to letter spacing 

----------------

## Update 1.0.6

[![View 1.0.6 update Video](http://img.youtube.com/vi/jpyFiRvSmbg/0.jpg)](http://www.youtube.com/watch?v=jpyFiRvSmbg "Update 1.0.6 for the Unity UI Extensions Project")

* Added the awesome ReOrderable List control, plus some other minor bugfixes / changes.
* Added a new version of the Scroll Snap control as an alternative to the fixed versions.
* New set of controls including some shader enhanced solutions
* I've added a donate column to the lists.  If you are getting great use out of a control, help out the dev who created it. Optional of course.  Will update with links as I get them.

----------------

## Update 1.0.5

Few minor fixes and a couple of additional scripts.  Predominately created the new 5.3 branch to maintain the UI API changes from the 5.2.1 Patch releases.  5.3 package is 100% compatible with 5.2.1 Patch releases.

----------------

## Update 1.0.4

[![View Getting Started Video](http://img.youtube.com/vi/oF48Qpaq3ls/0.jpg)](http://www.youtube.com/watch?v=oF48Qpaq3ls "Update 1.0.0.4 for the Unity UI Extensions Project")
---

=======================

## Additional Info

=======================

### [How do I get set up?](/GettingStarted.md)

As of Unity 2019, there are now two paths for getting access to the Unity UI Extensions project:

- Unity 2019 or higher
The recommended way to add the Unity UI Extensions project to your solution is to use the Unity package Manager. Simply use the Unity Package Manager to reference the project to install it

Alternatively, you can also use the pre-compiled Unity packages if you wish, however, UPM offers full versioning support to allow you to switch versions as you wish.

- Unity 2018 or lower
The pre-compiled Unity assets are the only solution for Unity 2018 or earlier due to the changes in the Unity UI framework in Unity made for 2019.
Either clone / download this repository to your machine and then copy the scripts in, or use the pre-packaged .UnityPackage for your version of Unity and import it as a custom package in to your project.

### [Contribution guidelines](/ContributionGuidelines.md)

Got a script you want added? Then just fork the [GitHub repository](https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git) and submit a PR.  All contributions accepted (including fixes)

Just ensure:

* The header of the script should match the standard used in all scripts
* The script uses the **Unity.UI.Extensions** namespace so they do not affect any other developments
* (optional) Add Component and Editor options where possible (editor options are in the Editor\UIExtensionsMenuOptions.cs file)

### [License](/License.md)

All scripts conform to the BSD3 license and are free to use / distribute.  See the [LICENSE](/License.md) file for more information 

### [Like what you see?](/FurtherInfo.md)

All these scripts were put together for my latest book Unity3D UI Essentials
Check out the [page on my blog](http://bit.ly/Unity3DUIEssentials) for more details and learn all about the inner workings of the new Unity UI System.

### [The downloads](/Downloads.md)

As this repo was created to support my new Unity UI Title ["Unity 3D UI Essentials"](http://bit.ly/Unity3DUIEssentials), in the downloads section you will find two custom assets (SpaceShip-DemoScene-Start.unitypackage and RollABallSample-Start.unitypackage).  These are just here as starter scenes for doing UI tasks in the book.

I will add more sample scenes for the UI examples in this repository and detail them above over time.

### [Previous Releases](/Downloads.md)

Please see the [full downloads list](/Downloads.md) for all previous releases and their corresponding download links.
