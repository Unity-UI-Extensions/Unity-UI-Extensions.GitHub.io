---
layout: default
title: Install Unity UI Extensions (uGUI) — Unity UI Extensions
description: Step-by-step installation guide for the Unity UI Extensions uGUI package. OpenUPM, Git URL, and manual installation methods.
permalink: /ugui/install/
---

<section class="pkg-hero">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <a href="{{ '/ugui/' | relative_url }}">uGUI</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">Installation</span>
    </nav>
    <div class="pkg-hero-badge"><span class="badge-u">uGUI Package</span></div>
    <h1>Installing Unity UI Extensions</h1>
    <p class="pkg-hero-lead">Three ways to add <code>com.unity.uiextensions</code> to your Unity project. OpenUPM is the recommended approach.</p>
    <div class="pkg-hero-meta">
      <code class="pkg-id">com.unity.uiextensions</code>
      <span class="badge-ghost">BSD 3-Clause</span>
      <span class="badge-ghost">Unity 2019.4+</span>
    </div>
  </div>
</section>

<section class="section install-detail-section" aria-labelledby="install-openupm">
  <div class="section-inner">

    <h2 id="install-openupm" class="section-title">Method 1 — OpenUPM (Recommended)</h2>
    <p>OpenUPM is the fastest and most reliable installation method. It supports automatic dependency resolution and version management.</p>

    <h3>Option A: OpenUPM CLI</h3>
    <p>If you have the <a href="https://openupm.com/docs/getting-started.html" target="_blank" rel="noopener">OpenUPM CLI</a> installed, run:</p>
    <div class="install-panel">
      <pre><code>openupm add com.unity.uiextensions</code></pre>
      <button class="copy-btn" aria-label="Copy command">Copy</button>
    </div>

    <h3>Option B: Scoped Registry (manual)</h3>
    <p>Open <strong>Edit → Project Settings → Package Manager</strong> and add the following scoped registry:</p>
    <div class="install-panel">
      <pre><code>Name: package.openupm.com
URL:  https://package.openupm.com
Scope: com.unity.uiextensions</code></pre>
      <button class="copy-btn" aria-label="Copy registry settings">Copy</button>
    </div>
    <p>Then open <strong>Window → Package Manager</strong>, switch the dropdown to <strong>My Registries</strong>, find <strong>Unity UI Extensions</strong>, and click <strong>Install</strong>.</p>

  </div>
</section>

<section class="section install-detail-section" aria-labelledby="install-giturl">
  <div class="section-inner">

    <h2 id="install-giturl" class="section-title">Method 2 — Git URL</h2>
    <p>Requires Git to be installed on your machine and accessible on the system path.</p>
    <ol>
      <li>Open <strong>Window → Package Manager</strong></li>
      <li>Click <strong>+</strong> and select <strong>Add package from git URL…</strong></li>
      <li>Paste the URL below and click <strong>Add</strong>:</li>
    </ol>
    <div class="install-panel">
      <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git</code></pre>
      <button class="copy-btn" aria-label="Copy git URL">Copy</button>
    </div>
    <p>To pin to a specific release, append the tag to the URL:</p>
    <div class="install-panel">
      <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git#2.3.2</code></pre>
      <button class="copy-btn" aria-label="Copy versioned git URL">Copy</button>
    </div>
    <p>Check the <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases" target="_blank" rel="noopener">Releases page</a> for all available version tags.</p>

  </div>
</section>

<section class="section install-detail-section" aria-labelledby="install-manual">
  <div class="section-inner">

    <h2 id="install-manual" class="section-title">Method 3 — Manual / Embedded Package</h2>
    <p>Use this when you need full local control over the package source, or when you're working offline.</p>
    <ol>
      <li>Go to the <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases/latest" target="_blank" rel="noopener">latest release</a> and download the <code>.zip</code> or <code>.unitypackage</code></li>
      <li>Extract the archive so you have a folder named <code>com.unity.uiextensions</code></li>
      <li>Move that folder into your project's <code>Packages/</code> directory (alongside <code>manifest.json</code>)</li>
      <li>Unity will detect and import the package automatically — no changes to <code>manifest.json</code> are required</li>
    </ol>
    <p>To later update the package, replace the folder contents with the newer version.</p>

  </div>
</section>

<section class="section install-detail-section" aria-labelledby="install-verify">
  <div class="section-inner">

    <h2 id="install-verify" class="section-title">Verifying the Installation</h2>
    <p>After installation you should see the package listed in <strong>Window → Package Manager</strong> under <em>In Project</em>. The package adds the following to your project:</p>
    <ul>
      <li><strong>Scripts</strong> — All control scripts are available via the <code>UnityEngine.UI.Extensions</code> namespace</li>
      <li><strong>Prefabs</strong> — Ready-to-use prefabs are available under <code>Assets/UI Extensions/Prefabs/</code> (if sample content was imported)</li>
      <li><strong>Samples</strong> — Optional sample scenes can be imported via the Package Manager's <em>Samples</em> tab</li>
    </ul>
    <p>Add any control component to a GameObject via <strong>Add Component → UI → Extensions → [Control Name]</strong>.</p>

  </div>
</section>

<section class="section install-detail-section" aria-labelledby="install-requirements">
  <div class="section-inner">

    <h2 id="install-requirements" class="section-title">Requirements</h2>
    <ul>
      <li>Unity <strong>2019.4 LTS</strong> or later</li>
      <li>Unity's built-in <strong>UI (uGUI)</strong> module — installed by default in all Unity projects</li>
      <li>No additional dependencies required</li>
    </ul>

    <div class="callout callout--note">
      <strong>Unity 6</strong> — All controls are supported. Some older controls that relied on legacy input may behave differently with the new Input System. Check individual control pages for notes.
    </div>

  </div>
</section>

<section class="cta-band" aria-labelledby="cta-browse">
  <div class="cta-band-inner">
    <h2 id="cta-browse">Ready to explore the controls?</h2>
    <p>Browse all 101 uGUI controls with descriptions, properties, and examples.</p>
    <div class="cta-actions">
      <a href="{{ '/ugui/' | relative_url }}" class="btn btn-u">Browse uGUI Controls</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/issues" class="btn btn-ghost" target="_blank" rel="noopener">Report an Issue</a>
    </div>
  </div>
</section>
