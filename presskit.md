---
layout: default
title: Press Kit
description: Press kit for Unity UI Extensions — the flagship open-source UI control collection for Unity uGUI and UI Toolkit. Facts, descriptions, logos and downloads for press, storefronts and content creators.
permalink: /presskit/
---

<style>
  /* Press-kit-scoped styles — layout helpers only; colours/fonts inherit from neon.css */
  .pk-wrap { padding-bottom: 2rem; }
  .pk-actions { display:flex; flex-wrap:wrap; gap:.75rem; justify-content:center; margin-top:1.5rem; }
  .pk-factsheet { width:100%; border-collapse:collapse; }
  .pk-factsheet th, .pk-factsheet td { text-align:left; vertical-align:top; padding:.7rem 1rem; border-bottom:1px solid var(--border, rgba(255,0,153,.18)); }
  .pk-factsheet th { width:34%; white-space:nowrap; color:var(--text-2, #dd88ff); font-weight:600; font-family:'JetBrains Mono', monospace; font-size:.85rem; }
  .pk-factsheet td { color:var(--text, #fff); }
  .pk-factsheet code { font-size:.85em; }
  .pk-assets { display:grid; grid-template-columns:repeat(auto-fill, minmax(220px,1fr)); gap:1rem; }
  .pk-asset { border:1px solid var(--border, rgba(255,0,153,.18)); border-radius:6px; overflow:hidden; background:var(--bg-2, #08080e); display:flex; flex-direction:column; }
  .pk-asset-prev { background:#050508; padding:1rem; display:flex; align-items:center; justify-content:center; min-height:140px; }
  .pk-asset-prev img { max-width:100%; max-height:160px; height:auto; }
  .pk-asset-meta { padding:.7rem .9rem; display:flex; flex-direction:column; gap:.35rem; border-top:1px solid var(--border, rgba(255,0,153,.18)); }
  .pk-asset-name { font-weight:600; font-size:.9rem; }
  .pk-asset-dl { font-family:'JetBrains Mono', monospace; font-size:.78rem; }
  .pk-swatches { display:flex; flex-wrap:wrap; gap:.6rem; }
  .pk-swatch { display:flex; align-items:center; gap:.5rem; font-family:'JetBrains Mono', monospace; font-size:.8rem; padding:.4rem .7rem; border:1px solid var(--border, rgba(255,0,153,.18)); border-radius:4px; }
  .pk-dot { width:16px; height:16px; border-radius:3px; display:inline-block; }
  .pk-chiplist { display:flex; flex-wrap:wrap; gap:.4rem; }
  .pk-twocol { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; }
  @media (max-width:720px){ .pk-twocol{ grid-template-columns:1fr; } .pk-factsheet th{ width:42%; } }

  /* Two-package cards: keep the "Explore" buttons aligned to the bottom of each card,
     regardless of differing description / stat-line heights. */
  .packages-grid .package-card { display:flex; flex-direction:column; }
  .packages-grid .package-card > .btn { margin-top:auto; }
</style>

<div class="pk-wrap">

<!-- ─────────────────────────── HERO ─────────────────────────── -->
<section class="hero">
  <div class="container">
    <p class="hero-eyebrow">Press &amp; Media Kit</p>
    <h1 class="hero-title">Unity UI <span class="hl-u">Extensions</span> — Press Kit</h1>
    <p class="hero-sub">
      Everything press, storefronts and content creators need — facts, descriptions, logos and downloads.
      <strong>Two packages. One ecosystem.</strong>
    </p>
    <div class="pk-actions">
      <a href="{{ site.pdf_downloads_base }}/Unity-UI-Extensions-PressKit.pdf" class="btn btn-u" download>↓ Download Press Kit (PDF)</a>
      <a href="{{ '/assets/downloads/Unity-UI-Extensions-Brand-Assets.zip' | relative_url }}" class="btn btn-t" download>↓ Brand Assets (.zip)</a>
      <a href="https://github.com/Unity-UI-Extensions" target="_blank" rel="noopener" class="btn btn-ghost">View on GitHub</a>
    </div>
  </div>
</section>

<!-- ─────────────────────────── STATS ─────────────────────────── -->
<section class="stats-band" aria-label="Project statistics">
  <div class="stats-band-inner">
    <div class="stat-item"><span class="stat-number" data-count="126">0</span><span class="stat-label">UI Controls</span></div>
    <div class="stat-item"><span class="stat-number" data-count="34">0</span><span class="stat-label">Example Scenes</span></div>
    <div class="stat-item"><span class="stat-number" data-count="2">0</span><span class="stat-label">Packages</span></div>
    <div class="stat-item"><span class="stat-number" data-count="2015">0</span><span class="stat-label">Since</span></div>
  </div>
</section>

<!-- ─────────────────────────── FACTSHEET ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Factsheet</h2>
      <p class="section-sub">The quick reference. Everything in one table.</p>
    </div>
    <div class="card">
      <table class="pk-factsheet">
        <tr><th>Project</th><td>Unity UI Extensions</td></tr>
        <tr><th>Release</th><td>Version <strong>3.0</strong> — a two-package ecosystem relaunch</td></tr>
        <tr><th>Maintainer</th><td>Simon “darkside” Jackson (<a href="https://github.com/SimonDarksideJ" target="_blank" rel="noopener">@SimonDarksideJ</a>) &amp; a global community of contributors</td></tr>
        <tr><th>Community since</th><td>2015</td></tr>
        <tr><th>Packages</th><td>uGUI — <code>com.unity.uiextensions</code> (v3.0.0, BSD-3-Clause)<br>UI Toolkit — <code>com.unity.uitoolkitextensions</code> (v1.0.0, MIT)</td></tr>
        <tr><th>Engine</th><td>Unity 6 (6000.0+) <span class="badge badge-ghost">2.x line remains for older Unity</span></td></tr>
        <tr><th>Controls</th><td><strong>126</strong> total — 101 uGUI · 25 UI Toolkit</td></tr>
        <tr><th>Examples</th><td><strong>34</strong> playable example scenes (22 uGUI · 12 UI Toolkit)</td></tr>
        <tr><th>Price</th><td>Free — 100% open source, no lock-in</td></tr>
        <tr><th>Distribution</th><td>Unity Package Manager (OpenUPM &amp; git URL) · Itch.io · <a href="https://assetstore.unity.com/packages/2d/gui/ui-extensions-175295" target="_blank" rel="noopener">Unity Asset Store</a> (uGUI; UI Toolkit listing coming soon)</td></tr>
        <tr><th>Website</th><td><a href="https://unity-ui-extensions.github.io">unity-ui-extensions.github.io</a></td></tr>
        <tr><th>Source</th><td>uGUI — <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions" target="_blank" rel="noopener">com.unity.uiextensions</a><br>UI Toolkit — <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions" target="_blank" rel="noopener">com.unity.uitoolkitextensions</a></td></tr>
        <tr><th>Community</th><td><a href="https://app.gitter.im/#/room/#Unity-UI-Extensions_Lobby:gitter.im" target="_blank" rel="noopener">Gitter</a> · <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/discussions" target="_blank" rel="noopener">GitHub Discussions</a></td></tr>
        <tr><th>Support</th><td><a href="https://github.com/sponsors/SimonDarksideJ" target="_blank" rel="noopener">GitHub Sponsors</a> · <a href="https://www.patreon.com/UnityUIExtensions" target="_blank" rel="noopener">Patreon</a> · <a href="https://ko-fi.com/uiextensions" target="_blank" rel="noopener">Ko-fi</a> · <a href="https://paypal.me/unityuiextensions" target="_blank" rel="noopener">PayPal.me</a> · <a href="https://unityuiextensions.itch.io/uiextensions2-0" target="_blank" rel="noopener">itch.io</a> · <a href="https://assetstore.unity.com/packages/2d/gui/ui-extensions-175295" target="_blank" rel="noopener">Unity Asset Store (uGUI)</a><!-- UI Toolkit Asset Store (live on publish): <a href="https://assetstore.unity.com/packages/tools/gui/ui-toolkit-extensions-387946" target="_blank" rel="noopener">Unity Asset Store (UI Toolkit)</a> --><br>Full details on the <a href="{{ '/donate/' | relative_url }}">Support page</a></td></tr>
        <tr><th>Press contact</th><td><a href="mailto:uiextensions@zenithmoon.com">uiextensions@zenithmoon.com</a> · maintainer via GitHub / Patreon</td></tr>
      </table>
    </div>
  </div>
</section>

<!-- ─────────────────────────── DESCRIPTION ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Description</h2>
    </div>

    <p style="font-size:1.15rem; line-height:1.6;"><strong>Stop rebuilding UI from scratch.</strong> Unity UI Extensions is the flagship open-source UI control collection for Unity — 126 battle-tested controls for both <strong>uGUI</strong> and <strong>UI Toolkit</strong>. The controls you would build anyway are already here, polished and edge-case handled.</p>

    <h3>One-liner</h3>
    <p>126 battle-tested, free, open-source UI controls for Unity uGUI and UI Toolkit. Two packages. One ecosystem.</p>

    <h3>Short description</h3>
    <p>Unity UI Extensions gives Unity developers 126 production-ready UI controls across two packages — accordions, colour pickers, scroll snapping, line renderers, radial layouts, pill buttons, step progress bars, toasts and dozens more. UPM-first, fully customisable, examples included. Community-driven since 2015, 100% free and open source.</p>

    <h3>Boilerplate</h3>
    <p>Unity UI Extensions is the flagship open-source UI control collection for Unity. Community-driven since 2015, the project provides 126 battle-tested, production-ready UI controls for both Unity uGUI and UI Toolkit. It is 100% free and open source, distributed UPM-first via OpenUPM and git URL, and licensed under BSD-3-Clause (uGUI) and MIT (UI Toolkit). The project is maintained by Simon “darkside” Jackson and a global community of contributors. <em>Not affiliated with Unity Technologies.</em></p>
  </div>
</section>

<!-- ─────────────────────────── PACKAGES ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">The two-package ecosystem</h2>
      <p class="section-sub">Version 3.0 unifies two co-equal packages under one banner.</p>
    </div>
    <div class="grid-2 packages-grid">

      <article class="package-card package-card--u">
        <div class="package-card-top">
          <span class="badge badge-u">uGUI</span>
          <h3 class="package-card-name">Unity UI Extensions</h3>
          <p class="package-id"><code>com.unity.uiextensions</code></p>
          <p class="package-card-desc">The original and largest collection — 101 production-ready controls for Unity’s uGUI system, refined over a decade of community use. This is the V3 release.</p>
        </div>
        <ul class="footer-links" style="margin:.5rem 0 1rem;">
          <li>Version 3.0.0 · Unity 6000.0+ · BSD-3-Clause</li>
          <li>101 controls · ~195 runtime scripts · 22 example scenes</li>
          <li>Categories: Controls · Primitives · Layouts · Effects &amp; Utilities</li>
        </ul>
        <a href="{{ '/ugui/' | relative_url }}" class="btn btn-u btn-sm">Explore uGUI</a>
      </article>

      <article class="package-card package-card--t">
        <div class="package-card-top">
          <span class="badge badge-t">UI Toolkit</span>
          <h3 class="package-card-name">Unity UI Toolkit Extensions</h3>
          <p class="package-id"><code>com.unity.uitoolkitextensions</code></p>
          <p class="package-card-desc">The modern companion — 25 USS-themable, data-driven controls built from the ground up for Unity 6’s UI Toolkit runtime.</p>
        </div>
        <ul class="footer-links" style="margin:.5rem 0 1rem;">
          <li>Version 1.0.0 · Unity 6000.0+ · MIT</li>
          <li>25 controls · ~26 runtime scripts · 12 example scenes</li>
          <li>Built with USS · fully themable · data-driven UI</li>
        </ul>
        <a href="{{ '/uitoolkit/' | relative_url }}" class="btn btn-t btn-sm">Explore UI Toolkit</a>
      </article>

    </div>
  </div>
</section>

<!-- ─────────────────────────── FEATURES ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Key features</h2>
    </div>
    <div class="features-grid">
      <div class="feature-item"><div class="feature-icon">🚀</div><h3 class="feature-title">Ship weeks faster</h3><p class="feature-desc">The controls you would build anyway — polished and edge-case handled.</p></div>
      <div class="feature-item"><div class="feature-icon">🧪</div><h3 class="feature-title">Production battle-tested</h3><p class="feature-desc">A decade of community use, bug reports and fixes since 2015.</p></div>
      <div class="feature-item"><div class="feature-icon">📦</div><h3 class="feature-title">UPM-first</h3><p class="feature-desc">OpenUPM or git URL. Clean dependency management, no asset-import drama.</p></div>
      <div class="feature-item"><div class="feature-icon">🎨</div><h3 class="feature-title">Fully customisable</h3><p class="feature-desc">Inspector-exposed for uGUI, USS-themable for UI Toolkit.</p></div>
      <div class="feature-item"><div class="feature-icon">📖</div><h3 class="feature-title">Examples included</h3><p class="feature-desc">34 playable example scenes across both packages.</p></div>
      <div class="feature-item"><div class="feature-icon">🤝</div><h3 class="feature-title">Open contribution</h3><p class="feature-desc">BSD-3 &amp; MIT. PRs welcome, every contributor credited.</p></div>
    </div>
  </div>
</section>

<!-- ─────────────────────────── SELECTED CONTROLS ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Selected controls</h2>
      <p class="section-sub">A taste of what ships in each package.</p>
    </div>
    <div class="pk-twocol">
      <div>
        <p><span class="badge badge-u">uGUI</span></p>
        <div class="pk-chiplist">
          <span class="control-tag">Accordion</span><span class="control-tag">ColorPicker</span><span class="control-tag">ComboBox</span><span class="control-tag">AutoComplete ComboBox</span><span class="control-tag">Reorderable List</span><span class="control-tag">FancyScrollView</span><span class="control-tag">UILineRenderer</span><span class="control-tag">UISquircle</span><span class="control-tag">Radial Layout</span><span class="control-tag">Scroll Snap (H/V/Child)</span><span class="control-tag">UIParticleSystem</span><span class="control-tag">UIKnob</span><span class="control-tag">Range Slider</span><span class="control-tag">+ 70 more</span>
        </div>
      </div>
      <div>
        <p><span class="badge badge-t">UI Toolkit</span></p>
        <div class="pk-chiplist">
          <span class="control-tag">PillButton</span><span class="control-tag">ToggleButton</span><span class="control-tag">ColorToggleGroup</span><span class="control-tag">CircularImageButton</span><span class="control-tag">IconLabelButton</span><span class="control-tag">Stepper</span><span class="control-tag">PillSelector</span><span class="control-tag">DropDownControl</span><span class="control-tag">ScrollSnap</span><span class="control-tag">PageDotIndicator</span><span class="control-tag">StepProgressBar</span><span class="control-tag">CollapsibleSection</span><span class="control-tag">LoadingIcon</span><span class="control-tag">ToastSwipeDismiss</span><span class="control-tag">ImageCropOverlayControl</span><span class="control-tag">+ more</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─────────────────────────── HISTORY ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">History</h2>
    </div>
    <p>Unity UI Extensions began in <strong>2015</strong> as a community home for the UI controls Unity developers kept rebuilding. Over a decade it grew into the largest open-source collection for Unity’s uGUI system, sustained by hundreds of community contributions, bug reports and fixes — the long tail that turns a control from “works in a demo” into “ships in a game”.</p>
    <p><strong>Version 3.0</strong> is the relaunch: the uGUI package steps up to a modern Unity 6 release, a brand-new <strong>UI Toolkit</strong> package brings the same philosophy to Unity’s modern runtime, and the whole project gains a refreshed identity and a redesigned documentation site. Two packages, one ecosystem — built by the community, free forever.</p>
  </div>
</section>

<!-- ─────────────────────────── BRAND / LOGO ASSETS ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Logos &amp; brand assets</h2>
      <p class="section-sub">Use freely in coverage. Please don’t alter the logo gradient or stretch the mark.</p>
    </div>

    <div class="pk-swatches mb-4">
      <span class="pk-swatch"><span class="pk-dot" style="background:#ff0099;"></span> #ff0099 <em style="color:var(--text-2,#dd88ff)">uGUI / magenta</em></span>
      <span class="pk-swatch"><span class="pk-dot" style="background:#00ffee;"></span> #00ffee <em style="color:var(--text-2,#dd88ff)">UI Toolkit / cyan</em></span>
      <span class="pk-swatch"><span class="pk-dot" style="background:linear-gradient(135deg,#ff0099,#00ffee);"></span> brand gradient</span>
      <span class="pk-swatch"><span class="pk-dot" style="background:#050508; border:1px solid #333;"></span> #050508 <em style="color:var(--text-2,#dd88ff)">background</em></span>
    </div>
    <p style="color:var(--text-2,#dd88ff);">Typefaces: <strong>Orbitron</strong> (display / wordmark) · <strong>Inter</strong> (body) · <strong>JetBrains Mono</strong> (code).</p>

    {% assign brand_master = "logo-primary.svg,logo-icon-square.svg,logo-wordmark-horizontal.svg,logo-monochrome.svg,social-banner-og-1200x630.svg,unity-store-hero.svg,twitter-header-1500x500.svg,itchio-cover-630x500.svg,feature-graphic.svg" | split: "," %}
    {% assign brand_ugui = "logo-ugui-wordmark.svg,logo-ugui-icon.svg,unity-store-hero-ugui.svg,itchio-cover-ugui-630x500.svg,social-banner-ugui-1200x630.svg" | split: "," %}
    {% assign brand_uitk = "logo-uitoolkit-wordmark.svg,logo-uitoolkit-icon.svg,unity-store-hero-uitoolkit.svg,itchio-cover-uitoolkit-630x500.svg,social-banner-uitoolkit-1200x630.svg" | split: "," %}

    <h3 style="margin-top:1.75rem;">Master brand <span style="color:var(--text-2,#dd88ff); font-weight:400;">— represents both packages (magenta → cyan)</span></h3>
    <div class="pk-assets mt-2">
      {% for asset in brand_master %}
      <div class="pk-asset">
        <div class="pk-asset-prev"><img src="{{ '/assets/img/presskit/' | append: asset | relative_url }}" alt="{{ asset }}" loading="lazy"></div>
        <div class="pk-asset-meta"><span class="pk-asset-name">{{ asset }}</span><a class="pk-asset-dl" href="{{ '/assets/img/presskit/' | append: asset | relative_url }}" download>↓ SVG</a></div>
      </div>
      {% endfor %}
    </div>

    <h3 style="margin-top:1.75rem; color:#ff0099;">uGUI package <span style="color:var(--text-2,#dd88ff); font-weight:400;">— magenta</span></h3>
    <div class="pk-assets mt-2">
      {% for asset in brand_ugui %}
      <div class="pk-asset">
        <div class="pk-asset-prev"><img src="{{ '/assets/img/presskit/' | append: asset | relative_url }}" alt="{{ asset }}" loading="lazy"></div>
        <div class="pk-asset-meta"><span class="pk-asset-name">{{ asset }}</span><a class="pk-asset-dl" href="{{ '/assets/img/presskit/' | append: asset | relative_url }}" download>↓ SVG</a></div>
      </div>
      {% endfor %}
    </div>

    <h3 style="margin-top:1.75rem; color:#00ffee;">UI Toolkit package <span style="color:var(--text-2,#dd88ff); font-weight:400;">— cyan</span></h3>
    <div class="pk-assets mt-2">
      {% for asset in brand_uitk %}
      <div class="pk-asset">
        <div class="pk-asset-prev"><img src="{{ '/assets/img/presskit/' | append: asset | relative_url }}" alt="{{ asset }}" loading="lazy"></div>
        <div class="pk-asset-meta"><span class="pk-asset-name">{{ asset }}</span><a class="pk-asset-dl" href="{{ '/assets/img/presskit/' | append: asset | relative_url }}" download>↓ SVG</a></div>
      </div>
      {% endfor %}
    </div>

    <p class="mt-3"><a href="{{ '/assets/downloads/Unity-UI-Extensions-Brand-Assets.zip' | relative_url }}" class="btn btn-ghost btn-sm" download>↓ Download all brand assets (.zip)</a></p>
  </div>
</section>

<!-- ─────────────────────────── DOWNLOADS ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Downloads</h2>
    </div>
    <ul class="footer-links">
      <li><a href="{{ site.pdf_downloads_base }}/Unity-UI-Extensions-PressKit.pdf" download>📄 Press Kit (PDF)</a> — this page, print-ready</li>
      <li><a href="{{ '/assets/downloads/Unity-UI-Extensions-Brand-Assets.zip' | relative_url }}" download>🗜 Brand assets (.zip) — logos &amp; promo graphics</a></li>
      <li><a href="{{ site.pdf_downloads_base }}/Unity-UI-Extensions-uGUI-Documentation.pdf" download>📄 uGUI — control reference (PDF)</a> · <a href="{{ '/ugui/controls/' | relative_url }}">browse online</a></li>
      <li><a href="{{ site.pdf_downloads_base }}/Unity-UI-Extensions-UIToolkit-Documentation.pdf" download>📄 UI Toolkit — control reference (PDF)</a> · <a href="{{ '/uitoolkit/controls/' | relative_url }}">browse online</a></li>
    </ul>
    <p style="color:var(--text-2,#dd88ff); font-size:.85rem;">All PDFs are generated from the live docs by <code>generate_pdfs.py</code> (headless Chrome) and rebuilt on every site deploy.</p>
  </div>
</section>

<!-- ─────────────────────────── QUOTES ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Quotes</h2>
    </div>
    <blockquote class="callout callout--note">
      “Two packages, one ecosystem — that is the whole story of 3.0. For ten years the community has built the controls you would build anyway, polished them, and handled the edge cases so you do not have to. The controls you would build anyway are already here. Ship faster. Build better.”
      <br><strong>— Simon “darkside” Jackson, project maintainer</strong>
    </blockquote>
    <p style="color:var(--text-2,#dd88ff);">Shipped a game or app with UI Extensions? We’d love to feature your quote — get in touch via GitHub or Gitter.</p>
  </div>
</section>

<!-- ─────────────────────────── LINKS ─────────────────────────── -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Links</h2>
    </div>
    <div class="grid-3">
      <div class="footer-col">
        <p class="footer-col-title">Packages</p>
        <ul class="footer-links">
          <li><a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions" target="_blank" rel="noopener">uGUI on GitHub</a></li>
          <li><a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions" target="_blank" rel="noopener">UI Toolkit on GitHub</a></li>
          <li><a href="https://openupm.com/packages/com.unity.uiextensions/" target="_blank" rel="noopener">OpenUPM — uGUI</a></li>
          <li><a href="https://unityuiextensions.itch.io/uiextensions2-0" target="_blank" rel="noopener">Itch.io — uGUI</a></li>
          <li><a href="https://assetstore.unity.com/packages/2d/gui/ui-extensions-175295" target="_blank" rel="noopener">Unity Asset Store — uGUI</a></li>
          <!-- UI Toolkit Asset Store listing — live on publish; uncomment to reveal:
          <li><a href="https://assetstore.unity.com/packages/tools/gui/ui-toolkit-extensions-387946" target="_blank" rel="noopener">Unity Asset Store — UI Toolkit</a></li>
          -->
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-col-title">Docs &amp; project</p>
        <ul class="footer-links">
          <li><a href="{{ '/' | relative_url }}">Website &amp; docs</a></li>
          <li><a href="{{ '/changelog/' | relative_url }}">Changelog</a></li>
          <li><a href="https://github.com/Unity-UI-Extensions" target="_blank" rel="noopener">GitHub organisation</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-col-title">Community &amp; support</p>
        <ul class="footer-links">
          <li><a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/discussions" target="_blank" rel="noopener">GitHub Discussions</a></li>
          <li><a href="https://app.gitter.im/#/room/#Unity-UI-Extensions_Lobby:gitter.im" target="_blank" rel="noopener">Gitter Chat</a></li>
          <li><a href="{{ '/donate/' | relative_url }}">Support the project</a></li>
          <li><a href="https://github.com/sponsors/SimonDarksideJ" target="_blank" rel="noopener">GitHub Sponsors</a></li>
          <li><a href="https://www.patreon.com/UnityUIExtensions" target="_blank" rel="noopener">Patreon</a></li>
          <li><a href="https://ko-fi.com/uiextensions" target="_blank" rel="noopener">Ko-fi</a></li>
          <li><a href="https://paypal.me/unityuiextensions" target="_blank" rel="noopener">PayPal.me</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ─────────────────────────── CTA ─────────────────────────── -->
<section class="cta-band">
  <div class="cta-band-inner">
    <h2 class="cta-title">Two packages. One ecosystem.</h2>
    <p class="cta-sub">126 battle-tested controls. 34 example scenes. Free forever.</p>
    <div class="cta-actions">
      <a href="{{ '/ugui/' | relative_url }}" class="btn btn-u">Explore uGUI</a>
      <a href="{{ '/uitoolkit/' | relative_url }}" class="btn btn-t">Explore UI Toolkit</a>
    </div>
  </div>
</section>

<p style="text-align:center; color:var(--text-2,#dd88ff); font-size:.85rem; margin-top:2rem;">Unity UI Extensions is community-maintained and <strong>not affiliated with Unity Technologies</strong>. BSD-3-Clause (uGUI) &amp; MIT (UI Toolkit).</p>

</div>
