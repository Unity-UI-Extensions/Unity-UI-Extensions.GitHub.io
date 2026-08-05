# Unity UI Extensions — Website

This repository contains the source for the **Unity UI Extensions** documentation website, built with [Jekyll](https://jekyllrb.com/) and published via GitHub Pages at **<https://unity-ui-extensions.github.io>**.

> Looking for the controls themselves? They live in the package repositories:
>
> - **uGUI:** [com.unity.uiextensions](https://github.com/Unity-UI-Extensions/com.unity.uiextensions)
> - **UI Toolkit:** [com.unity.uitoolkitextensions](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions)

[![openupm](https://img.shields.io/npm/v/com.unity.uiextensions?label=openupm&registry_uri=https://package.openupm.com)](https://openupm.com/packages/com.unity.uiextensions/)

-----

## About the project

Unity UI Extensions is the flagship open-source UI control collection for Unity — **126 battle-tested controls** across two packages, free forever and community-driven since 2015. Version **3.0** is a two-package ecosystem: the proven uGUI library, now joined by a modern UI Toolkit companion.

| Package | ID | Version | Licence | Controls | Examples |
| --- | --- | --- | --- | --- | --- |
| **Unity UI Extensions (uGUI)** | `com.unity.uiextensions` | 3.0.0 | BSD-3-Clause | 101 | 22 |
| **UI Toolkit Extensions** | `com.unity.uitoolkitextensions` | 1.0.0 | MIT | 25 | 12 |

Both packages target **Unity 6000.0+**. (Older Unity versions can continue to use the established uGUI 2.x line.)

Browse everything on the live site:

- [uGUI controls](https://unity-ui-extensions.github.io/ugui/) · [UI Toolkit controls](https://unity-ui-extensions.github.io/uitoolkit/)
- [Changelog](https://unity-ui-extensions.github.io/changelog/) · [Press Kit](https://unity-ui-extensions.github.io/presskit/) · [Support / Donate](https://unity-ui-extensions.github.io/donate/)

-----

## Installation

**Recommended — OpenUPM:**

```shell
openupm add com.unity.uiextensions
openupm add com.unity.uitoolkitextensions
```

**Or via Git URL** (Unity Package Manager → *Add package from git URL*):

```text
https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git
https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git
```

Full install guides: [uGUI](https://unity-ui-extensions.github.io/ugui/install/) · [UI Toolkit](https://unity-ui-extensions.github.io/uitoolkit/install/)

-----

## Building & Testing the Site Locally

This website is a [Jekyll](https://jekyllrb.com/) static site, published through [GitHub Pages](https://pages.github.com/) using the `github-pages` gem. When changes are pushed to the published branch, GitHub builds and deploys the site automatically — there is no manual build or upload step.

To preview your changes locally before pushing:

1. Install the pinned gems (first time only, or after editing the `Gemfile`):

   ```shell
   bundle install
   ```

2. Serve the site locally with auto-rebuild and live reload:

   ```shell
   bundle exec jekyll serve --livereload
   ```

3. Open <http://localhost:4000> in your browser (the site is served from the root, as `baseurl` is empty).

To reproduce the exact static output that GitHub Pages publishes (generated into the `_site/` folder), run:

```shell
bundle exec jekyll build
```

> [!NOTE]
> Changes to `_config.yml` require restarting `jekyll serve` — live reload does not pick up configuration changes. The build also ignores `README.md`, the helper scripts (`*.py`, `*.sh`) and a few other files; see the `exclude` list in `_config.yml` for the full set.

### Testing the donate toast locally

The site shows a slide-in "consider donating" toast after a browser has visited on **5 distinct days** (tracked purely in that browser's `localStorage` — nothing is sent anywhere). Waiting five days to test is no fun, so two URL hashes exist:

- <http://localhost:4000/#donate-toast> — force-show the toast immediately. Test mode neither reads nor writes the stored visit state and skips the GoatCounter events, so it cannot pollute real stats or your own visit count.
- <http://localhost:4000/#donate-toast-reset> — wipe the stored nudge state in the current browser (visit-day count, snoozes, and the permanent opt-out set by clicking Donate), returning it to a first-time visitor.

Normal behaviour outside test mode: the toast appears at most once per 14 days, "Maybe later" / close / <kbd>Esc</kbd> snoozes it for 90 days, and clicking the Donate button retires it permanently for that browser. The same hashes also work on the live site.

-----

## Contributing

Contributions are always welcome — and **not all contributions are cash**. Open a pull request with a new control or a fix, file a clear bug report, improve the docs, or help other developers in the community.

- Report issues / request features: [uGUI issues](https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues) · [UI Toolkit issues](https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/issues)
- Chat & questions: [Gitter](https://app.gitter.im/#/room/#Unity-UI-Extensions_Lobby:gitter.im) · [GitHub Discussions](https://github.com/Unity-UI-Extensions/com.unity.uiextensions/discussions)
- Follow: [Twitter/X](https://twitter.com/search?q=%23unityuiextensions) · [Facebook](https://www.facebook.com/UnityUIExtensions/) · [YouTube](https://www.youtube.com/@UnityUIExtensions)

When adding a uGUI control, use the **`UnityEngine.UI.Extensions`** namespace, match the existing script header, and add editor/menu options where it makes sense.

> **Contribution is optional — the assets and code will always remain FREE.**

-----

## Supporting the project

If UI Extensions has saved you time, you can help keep it maintained. Every contribution goes straight into keeping the project alive and well — there is no paid tier and nothing behind a paywall.

- [GitHub Sponsors](https://github.com/sponsors/SimonDarksideJ) · [Patreon](https://www.patreon.com/UnityUIExtensions) · [Ko-fi](https://ko-fi.com/uiextensions) · [PayPal.me](https://paypal.me/unityuiextensions)
- Grab the package on [itch.io](https://unityuiextensions.itch.io/uiextensions2-0) or the [Unity Asset Store (uGUI)](https://assetstore.unity.com/packages/2d/gui/ui-extensions-175295)

Full details on the [Support page](https://unity-ui-extensions.github.io/donate/).

-----

## Licence

The uGUI package is licensed under **BSD-3-Clause**; the UI Toolkit package under **MIT**. Both are free to use and distribute. Unity UI Extensions is community-maintained and **not affiliated with Unity Technologies**.
