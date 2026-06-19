---
layout: default
title: Changelog — Unity UI Extensions
description: Release history and changelog for the Unity UI Extensions uGUI and UIToolkit packages.
permalink: /changelog/
---

<section class="pkg-hero">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">Changelog</span>
    </nav>
    <h1>Changelog</h1>
    <p class="pkg-hero-lead">Release history for both Unity UI Extensions packages.</p>
  </div>
</section>

<section class="section changelog-section" aria-labelledby="changelog-ugui">
  <div class="section-inner">
    <h2 id="changelog-ugui" class="section-title">
      Unity UI Extensions (uGUI)
      <span class="badge-u">com.unity.uiextensions</span>
    </h2>

    <div class="changelog-release">
      <div class="changelog-release-header">
        <h3 class="changelog-version">v3.0.0 — Unity 6, reimagined</h3>
        <time class="changelog-date" datetime="2026-06">June 2026</time>
      </div>
      <p>The V3 relaunch brings full Unity 6 support, a refreshed brand, and the start of a two-package ecosystem — the proven uGUI library you know, now joined by a modern UI Toolkit companion.</p>

      <h4>Highlights</h4>
      <ul>
        <li>Full Unity 6 support — the whole library verified and updated for Unity 6, with legacy dependencies cleared out and the examples refreshed</li>
        <li>Two-package ecosystem — the new <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions" target="_blank" rel="noopener">UI Toolkit Extensions</a> package launches alongside under the shared 3.0 banner</li>
      </ul>

      <h4>Added</h4>
      <ul>
        <li>New control: <code>GridRawImage</code></li>
        <li>New control: <code>UI_Knob2</code> (UI Knob 2)</li>
        <li>New control: UI Segmented Circle / Segmented Control</li>
        <li>New control: UI Graphic Selector</li>
        <li><code>UILineConnector</code>: the pivot can now be used as the reference point when drawing lines (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/pull/490" target="_blank" rel="noopener">#490</a>)</li>
        <li><code>UILineConnector</code>: new "close line" option to finish a line off and fill any gaps at the end</li>
        <li><code>BoxSlider</code>: added <code>SetXWithoutNotify</code> and <code>SetYWithoutNotify</code></li>
      </ul>

      <h4>Fixed</h4>
      <ul>
        <li><code>ReorderableList</code>: fixed a null-reference exception, and resolved element-stacking when moving elements slightly</li>
        <li>Scroll Snap: resolved a race condition that could raise a NaN error when lerping; made rescaling and full-screen scroll snap more resilient</li>
        <li>HSS/VSS: guarded against a divide-by-zero when the scroll snap has a single page; <code>GetCurrentPage</code> made more resilient</li>
        <li>Infinite Scroll: resolved out-of-bounds issues</li>
        <li><code>FlowLayoutGroup</code>: addressed layout issues and fixed the last line overflowing the rect bounds</li>
        <li><code>UIParticleSystem</code>: new "CullingMode" option to resolve unscaled delta time (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues/486" target="_blank" rel="noopener">#486</a> / <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues/487" target="_blank" rel="noopener">#487</a>)</li>
        <li><code>Gradient2</code>: fixed radial triangle add order (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/pull/384" target="_blank" rel="noopener">#384</a>)</li>
        <li><code>ScrollRect</code>: force <code>content</code> setup (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/pull/485" target="_blank" rel="noopener">#485</a>)</li>
        <li><code>UILineConnector</code>: improved point-array calculation (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/pull/495" target="_blank" rel="noopener">#495</a>); refresh on global scale change</li>
      </ul>

      <h4>Changed</h4>
      <ul>
        <li><code>Gradient2</code>: optimised <code>ModifyMesh</code></li>
        <li>Layout groups now rebuild on disable/enable</li>
        <li>General TMPro/Text compatibility housekeeping (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues/477" target="_blank" rel="noopener">#477</a>)</li>
        <li>Compile-flag support for Unity 6 (<a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/pull/493" target="_blank" rel="noopener">#493</a>)</li>
      </ul>

      <h4>Contributors</h4>
      <p>Huge thanks to
        <a href="https://github.com/SimonDarksideJ" target="_blank" rel="noopener">@SimonDarksideJ</a>,
        <a href="https://github.com/bluefallsky" target="_blank" rel="noopener">@bluefallsky</a>,
        <a href="https://github.com/hugoymh" target="_blank" rel="noopener">@hugoymh</a>,
        <a href="https://github.com/JavierMonton" target="_blank" rel="noopener">@JavierMonton</a>,
        <a href="https://github.com/Dover8" target="_blank" rel="noopener">@Dover8</a>,
        <a href="https://github.com/fgrg2801" target="_blank" rel="noopener">@fgrg2801</a> and
        <a href="https://github.com/Moderbord" target="_blank" rel="noopener">@Moderbord</a>.</p>

      <div class="changelog-links">
        <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases/tag/v3.0.0" class="btn btn-ghost btn-sm" target="_blank" rel="noopener">View Release on GitHub</a>
        <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/compare/2.3.2...v3.0.0" class="btn btn-ghost btn-sm" target="_blank" rel="noopener">Full Diff</a>
      </div>
    </div>

    <div class="changelog-release">
      <div class="changelog-release-header">
        <h3 class="changelog-version">v2.3.2 — Rejuvenation</h3>
        <time class="changelog-date" datetime="2023-11-26">26 November 2023</time>
      </div>
      <p>End-of-year maintenance release focusing on bug fixes and 2023 LTS compatibility. FlowLayoutGroup updated to latest upstream; deprecated Text components tagged with obsolete attributes.</p>

      <h4>Added</h4>
      <ul>
        <li>Added <code>CalculatePointOnCurve</code> for <code>UILineRenderer</code> (<a href="https://github.com/victornor" target="_blank" rel="noopener">@victornor</a>)</li>
        <li>Added argument to <code>UpdateLayout</code> on HSS/VSS to move to a new starting page</li>
        <li>Added extra event on <code>AutoCompleteComboBox</code> to fire when an item is selected with its display name</li>
      </ul>

      <h4>Fixed</h4>
      <ul>
        <li>Fixed null reference exception with <code>ResetSelectableHighlight</code> (<a href="https://github.com/FejZa" target="_blank" rel="noopener">@FejZa</a>)</li>
        <li>Resolved issue where the last line in a <code>FlowLayoutGroup</code> would overflow the rect bounds</li>
        <li>Fixed <code>GetPosition</code> when Segments is null (<a href="https://github.com/victornor" target="_blank" rel="noopener">@victornor</a>)</li>
        <li>Fixed <code>NicerOutline</code> color alpha loss when <code>m_UseGraphicAlpha</code> is true (<a href="https://github.com/wanliyun" target="_blank" rel="noopener">@wanliyun</a>)</li>
        <li>Updated <code>Accordion</code> to force enumerated start, resolving issue <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues/455" target="_blank" rel="noopener">#455</a></li>
      </ul>

      <h4>Changed</h4>
      <ul>
        <li>Updated implementations for Unity 2023 LTS support</li>
        <li><code>FlowLayoutGroup</code> updated to latest upstream (likely final update as author has stopped active development)</li>
      </ul>

      <h4>Deprecated</h4>
      <ul>
        <li>All deprecated Text-based components now carry <code>[Obsolete]</code> attributes. These components do not function in Unity 2022+. Migrate to TextMeshPro equivalents.</li>
      </ul>

      <h4>Breaking Changes</h4>
      <p>Customers upgrading from Unity 2018/2019 to Unity 2020+ must manually replace <code>Text</code>-based UI components with <code>TextMeshPro</code> equivalents. See the <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/discussions/428" target="_blank" rel="noopener">deprecation discussion on GitHub</a> for details.</p>

      <div class="changelog-links">
        <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases/tag/2.3.2" class="btn btn-ghost btn-sm" target="_blank" rel="noopener">View Release on GitHub</a>
        <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/compare/2.3.1...2.3.2" class="btn btn-ghost btn-sm" target="_blank" rel="noopener">Full Diff</a>
      </div>
    </div>

    <div class="changelog-older">
      <p>For earlier release history, see the <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/blob/main/CHANGELOG.md" target="_blank" rel="noopener">full CHANGELOG on GitHub</a>.</p>
    </div>

  </div>
</section>

<section class="section changelog-section uitk-context" aria-labelledby="changelog-uitk">
  <div class="section-inner">
    <h2 id="changelog-uitk" class="section-title">
      UIToolkit Extensions
      <span class="badge-t">com.unity.uitoolkitextensions</span>
    </h2>

    <div class="changelog-release">
      <div class="changelog-release-header">
        <h3 class="changelog-version">v1.0.0 — Launch</h3>
        <time class="changelog-date">Coming Soon</time>
      </div>
      <p>Initial public release of the UIToolkit Extensions package. Full details will be published on launch.</p>
      <p>20 controls across Navigation, Forms, Feedback, Primitives, and Utilities categories — built for Unity 2022.3+ runtime UI.</p>

      <div class="changelog-links">
        <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/releases" class="btn btn-ghost btn-sm" target="_blank" rel="noopener">Releases on GitHub</a>
      </div>
    </div>

  </div>
</section>

<section class="cta-band" aria-labelledby="cta-changelog">
  <div class="cta-band-inner">
    <h2 id="cta-changelog">Found a bug or have a suggestion?</h2>
    <p>Both packages are community maintained — contributions and issue reports are always welcome.</p>
    <div class="cta-actions">
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues" class="btn btn-u" target="_blank" rel="noopener">uGUI Issues</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/issues" class="btn btn-t" target="_blank" rel="noopener">UIToolkit Issues</a>
      <a href="https://github.com/Unity-UI-Extensions" class="btn btn-ghost" target="_blank" rel="noopener">GitHub Organisation</a>
    </div>
  </div>
</section>
