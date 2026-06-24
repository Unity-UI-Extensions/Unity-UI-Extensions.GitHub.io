---
layout: default
title: Install UIToolkit Extensions — Unity UIToolkit Extensions
description: Step-by-step installation guide for the UIToolkit Extensions package. OpenUPM and Git URL installation methods.
permalink: /uitoolkit/install/
---

<section class="pkg-hero uitk-context">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <a href="{{ '/uitoolkit/' | relative_url }}">UI Toolkit</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">Installation</span>
    </nav>
    <div class="pkg-hero-badge"><span class="badge-t">UI Toolkit Package</span></div>
    <h1>Installing UIToolkit Extensions</h1>
    <p class="pkg-hero-lead">Two ways to add <code>com.unity.uitoolkitextensions</code> to your Unity project. OpenUPM is the recommended approach.</p>
    <div class="pkg-hero-meta">
      <code class="pkg-id">com.unity.uitoolkitextensions</code>
      <span class="badge-ghost">MIT Licence</span>
      <span class="badge-ghost">Unity 6000.0+</span>
    </div>
  </div>
</section>

<section class="section install-detail-section uitk-context" aria-labelledby="install-openupm">
  <div class="section-inner">

    <h2 id="install-openupm" class="section-title">Method 1 — OpenUPM (Recommended)</h2>
    <p>OpenUPM is the fastest and most reliable installation method. It supports automatic dependency resolution and version management.</p>

    <h3>Option A: OpenUPM CLI</h3>
    <p>If you have the <a href="https://openupm.com/docs/getting-started.html" target="_blank" rel="noopener">OpenUPM CLI</a> installed, run:</p>
    <div class="install-panel">
      <pre><code>openupm add com.unity.uitoolkitextensions</code></pre>
      <button class="copy-btn" aria-label="Copy command">Copy</button>
    </div>

    <h3>Option B: Scoped Registry (manual)</h3>
    <p>Open <strong>Edit → Project Settings → Package Manager</strong> and add the following scoped registry:</p>
    <div class="install-panel">
      <pre><code>Name: package.openupm.com
URL:  https://package.openupm.com
Scope: com.unity.uitoolkitextensions</code></pre>
      <button class="copy-btn" aria-label="Copy registry settings">Copy</button>
    </div>
    <p>Then open <strong>Window → Package Manager</strong>, switch the dropdown to <strong>My Registries</strong>, find <strong>UIToolkit Extensions</strong>, and click <strong>Install</strong>.</p>

  </div>
</section>

<section class="section install-detail-section uitk-context" aria-labelledby="install-giturl">
  <div class="section-inner">

    <h2 id="install-giturl" class="section-title">Method 2 — Git URL</h2>
    <p>Requires Git to be installed on your machine and accessible on the system path.</p>
    <ol>
      <li>Open <strong>Window → Package Manager</strong></li>
      <li>Click <strong>+</strong> and select <strong>Add package from git URL…</strong></li>
      <li>Paste the URL below and click <strong>Add</strong>:</li>
    </ol>
    <div class="install-panel">
      <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git</code></pre>
      <button class="copy-btn" aria-label="Copy git URL">Copy</button>
    </div>
    <p>Check the <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/releases" target="_blank" rel="noopener">Releases page</a> for all available version tags. Append a tag to pin a specific version, for example:</p>
    <div class="install-panel">
      <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git#1.0.0</code></pre>
      <button class="copy-btn" aria-label="Copy versioned git URL">Copy</button>
    </div>

  </div>
</section>

<section class="section install-detail-section uitk-context" aria-labelledby="install-manual">
  <div class="section-inner">

    <h2 id="install-manual" class="section-title">Method 3 — Manual / Embedded Package</h2>
    <p>Use this when you need full local control over the package source, or when you're working offline.</p>
    <ol>
      <li>Go to the <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/releases/latest" target="_blank" rel="noopener">latest release</a> and download the source archive</li>
      <li>Extract so you have a folder named <code>com.unity.uitoolkitextensions</code></li>
      <li>Move that folder into your project's <code>Packages/</code> directory (alongside <code>manifest.json</code>)</li>
      <li>Unity will detect and import the package automatically</li>
    </ol>

  </div>
</section>

<section class="section install-detail-section uitk-context" aria-labelledby="install-verify">
  <div class="section-inner">

    <h2 id="install-verify" class="section-title">Verifying the Installation</h2>
    <p>After installation you should see the package listed in <strong>Window → Package Manager</strong> under <em>In Project</em>. All controls are available under the <code>UnityUIToolkit.Extensions</code> namespace.</p>
    <p>Controls can be instantiated in C# or declared in UXML:</p>
    <div class="install-panel">
      <pre><code>// C#
using UnityUIToolkit.Extensions;
var toggle = new ToggleButton();
root.Add(toggle);</code></pre>
      <button class="copy-btn" aria-label="Copy code">Copy</button>
    </div>
    <div class="install-panel">
      <pre><code>&lt;!-- UXML --&gt;
&lt;UnityUIToolkit.Extensions.ToggleButton /&gt;</code></pre>
      <button class="copy-btn" aria-label="Copy UXML">Copy</button>
    </div>

  </div>
</section>

<section class="section install-detail-section uitk-context" aria-labelledby="install-requirements">
  <div class="section-inner">

    <h2 id="install-requirements" class="section-title">Requirements</h2>
    <ul>
      <li>Unity <strong>6 LTS</strong> or later</li>
      <li>Unity's <strong>UI Toolkit</strong> module (included by default in Unity 6)</li>
      <li>No additional dependencies required</li>
    </ul>

    <div class="callout callout--note">
      <strong>Runtime vs Editor UI</strong> — All controls target runtime UI Toolkit panels. Editor-window usage is possible but some controls (particularly gesture-based ones) may behave differently outside a game view context.
    </div>

  </div>
</section>

<section class="cta-band uitk-context" aria-labelledby="cta-browse">
  <div class="cta-band-inner">
    <h2 id="cta-browse">Ready to explore the controls?</h2>
    <p>Browse all 25 UIToolkit controls with full API reference and code examples.</p>
    <div class="cta-actions">
      <a href="{{ '/uitoolkit/' | relative_url }}" class="btn btn-t">Browse UIToolkit Controls</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/issues" class="btn btn-ghost" target="_blank" rel="noopener">Report an Issue</a>
    </div>
  </div>
</section>
