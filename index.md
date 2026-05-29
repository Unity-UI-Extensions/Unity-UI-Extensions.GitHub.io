---
layout: home
title: Unity UI Extensions — Community UI Controls for Unity
description: 80+ battle-tested UI controls for Unity's uGUI and UI Toolkit frameworks. Free forever, open source, community maintained.
permalink: /
---

<section class="hero">
  <div class="container">
    <p class="hero-eyebrow">Community Open Source — Free Forever</p>
    <h1 class="hero-title">
      Unity UI <span class="hl-u">Extensions</span>
    </h1>
    <p class="hero-sub">
      80+ battle-tested UI controls for Unity's <strong>uGUI</strong> and <strong>UI Toolkit</strong> frameworks.
      Drop in. Build faster. Ship sooner.
    </p>
    <div class="hero-ctas">
      <a href="/ugui/" class="btn btn-u">Explore uGUI Controls</a>
      <a href="/uitoolkit/" class="btn btn-t">Explore UI Toolkit Controls</a>
    </div>
  </div>
</section>

<section class="stats-band" aria-label="Project statistics">
  <div class="stats-band-inner">
    <div class="stat-item">
      <span class="stat-number" data-count="70" data-suffix="+">0+</span>
      <span class="stat-label">uGUI Controls</span>
    </div>
    <div class="stat-item">
      <span class="stat-number" data-count="18">0</span>
      <span class="stat-label">UIToolkit Controls</span>
    </div>
    <div class="stat-item">
      <span class="stat-number" data-count="2">0</span>
      <span class="stat-label">Packages</span>
    </div>
    <div class="stat-item">
      <span class="stat-number" data-count="100" data-suffix="%">0%</span>
      <span class="stat-label">Free &amp; Open Source</span>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="packages-heading">
  <div class="container">
    <div class="section-head">
      <h2 id="packages-heading" class="section-title">Two Packages, One Community</h2>
      <p class="section-sub">Choose the package that matches your Unity UI framework — or use both.</p>
    </div>

    <div class="grid-2 packages-grid">
      <article class="package-card package-card--u">
        <div class="package-card-top">
          <span class="badge badge-u">uGUI</span>
          <h3 class="package-card-name">Unity UI Extensions</h3>
          <p class="package-id"><code>com.unity.uiextensions</code></p>
          <p class="package-card-desc">The original and largest collection. 70+ production-ready controls built on Unity's legacy uGUI system — sliders, graphs, scrollers, effects, and more.</p>
        </div>
        <ul class="package-features">
          <li>70+ controls across 6 categories</li>
          <li>BSD 3-Clause licence — use in commercial projects</li>
          <li>OpenUPM, Git URL, and Unity Package Manager</li>
          <li>Works in Unity 2019.4+</li>
        </ul>
        <div class="package-card-actions">
          <a href="/ugui/" class="btn btn-u">Browse Controls</a>
          <a href="/ugui/install/" class="btn btn-ghost-u">Install Guide</a>
        </div>
      </article>

      <article class="package-card package-card--t">
        <div class="package-card-top">
          <span class="badge badge-t">UI Toolkit</span>
          <h3 class="package-card-name">UIToolkit Extensions</h3>
          <p class="package-id"><code>com.unity.uitoolkitextensions</code></p>
          <p class="package-card-desc">A modern, growing library of custom controls and manipulators for Unity's UI Toolkit — built for runtime UI, designed for productivity.</p>
        </div>
        <ul class="package-features">
          <li>18 controls for navigation, forms, and feedback</li>
          <li>MIT licence — maximum flexibility</li>
          <li>OpenUPM and Git URL installation</li>
          <li>Requires Unity 2022.3+</li>
        </ul>
        <div class="package-card-actions">
          <a href="/uitoolkit/" class="btn btn-t">Browse Controls</a>
          <a href="/uitoolkit/install/" class="btn btn-ghost-t">Install Guide</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="install-heading">
  <div class="container">
    <div class="section-head">
      <h2 id="install-heading" class="section-title">Get Started in Seconds</h2>
    </div>

    <div class="install-tabs" data-tabs>
      <div class="tabs">
        <button class="tab-btn active" data-tab="openupm">OpenUPM</button>
        <button class="tab-btn" data-tab="giturl">Git URL</button>
        <button class="tab-btn" data-tab="manual">Manual</button>
      </div>

      <div class="tab-panel active" data-panel="openupm">
        <h3>Install via OpenUPM <span class="badge badge-n">Recommended</span></h3>
        <p>The fastest way — use the OpenUPM CLI or add the scoped registry manually.</p>

        <h4>uGUI Package</h4>
        <div class="install-panel">
          <pre><code>openupm add com.unity.uiextensions</code></pre>
          <button class="copy-btn" aria-label="Copy install command">Copy</button>
        </div>

        <h4>UIToolkit Package</h4>
        <div class="install-panel">
          <pre><code>openupm add com.unity.uitoolkitextensions</code></pre>
          <button class="copy-btn" aria-label="Copy install command">Copy</button>
        </div>
      </div>

      <div class="tab-panel" data-panel="giturl">
        <h3>Install via Git URL</h3>
        <p>In Unity: <strong>Window → Package Manager → + → Add package from git URL</strong></p>

        <h4>uGUI Package</h4>
        <div class="install-panel">
          <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git</code></pre>
          <button class="copy-btn" aria-label="Copy git URL">Copy</button>
        </div>

        <h4>UIToolkit Package</h4>
        <div class="install-panel">
          <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git</code></pre>
          <button class="copy-btn" aria-label="Copy git URL">Copy</button>
        </div>
      </div>

      <div class="tab-panel" data-panel="manual">
        <h3>Manual Installation</h3>
        <p>Download the latest release and extract to your project's <code>Packages/</code> folder.</p>
        <div class="hero-ctas" style="justify-content:flex-start;margin-top:1.5rem;">
          <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases/latest" class="btn btn-u" target="_blank" rel="noopener">Download uGUI Release</a>
          <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/releases/latest" class="btn btn-t" target="_blank" rel="noopener">Download UIToolkit Release</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="features-heading">
  <div class="container">
    <div class="section-head">
      <h2 id="features-heading" class="section-title">Why UI Extensions?</h2>
    </div>
    <div class="grid-3 features-grid">
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#9889;</div>
        <p class="feature-title">Drop-In Ready</p>
        <p class="feature-desc">Every control is self-contained. Add a component, tweak inspector properties, done. No configuration files, no setup ceremonies.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#128275;</div>
        <p class="feature-title">Open source</p>
        <p class="feature-desc">BSD 3-Clause and MIT licences. Use in commercial games, apps, and tools — forever. No subscriptions, no royalties, no catch.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#127757;</div>
        <p class="feature-title">Community Driven</p>
        <p class="feature-desc">Built and maintained by Unity developers for Unity developers. Every control has been battle-tested in real projects by the community.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#128230;</div>
        <p class="feature-title">UPM Native</p>
        <p class="feature-desc">Full Unity Package Manager support. Install in one click via OpenUPM, reference via git URL, or embed locally — your choice.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#127912;</div>
        <p class="feature-title">Both UI Frameworks</p>
        <p class="feature-desc">Controls for both uGUI (legacy) and UI Toolkit (modern). Whether you're maintaining an existing project or building something new, we've got you covered.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon" aria-hidden="true">&#128216;</div>
        <p class="feature-title">Well Documented</p>
        <p class="feature-desc">Every control ships with property references, usage examples, and where available — video demos and sample scenes to learn from.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band" aria-labelledby="cta-heading">
  <div class="container">
    <h2 id="cta-heading" class="cta-title">Ready to build something?</h2>
    <p class="cta-sub">Join thousands of Unity developers using UI Extensions every day.</p>
    <div class="cta-packages-grid">
      <p class="cta-package-label cta-package-label--u">uGUI Package</p>
      <p class="cta-package-label cta-package-label--t">UI Toolkit Package</p>
      <a href="/ugui/controls/" class="btn btn-u">Browse All uGUI Controls</a>
      <a href="/uitoolkit/controls/" class="btn btn-t">Browse UIToolkit Controls</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions" class="btn btn-ghost" target="_blank" rel="noopener">View on GitHub</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions" class="btn btn-ghost" target="_blank" rel="noopener">View on GitHub</a>
    </div>
  </div>
</section>
