---
layout: default
title: uGUI Controls — Unity UI Extensions
description: 70+ battle-tested uGUI controls for Unity's legacy UI system. Sliders, graphs, effects, layouts, and more.
permalink: /ugui/
---

<section class="pkg-hero">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">uGUI</span>
    </nav>
    <div class="pkg-hero-badge"><span class="badge-u">uGUI Package</span></div>
    <h1>Unity UI Extensions</h1>
    <p class="pkg-hero-lead">70+ battle-tested controls for Unity's uGUI framework. The original community UI extension library — free, open source, and production-ready.</p>
    <div class="pkg-hero-meta">
      <code class="pkg-id">com.unity.uiextensions</code>
      <span class="badge-ghost">BSD 3-Clause</span>
      <span class="badge-ghost">Unity 2019.4+</span>
    </div>
    <div class="pkg-hero-actions">
      <a href="#controls" class="btn btn-u">Browse Controls</a>
      <a href="{{ '/ugui/install/' | relative_url }}" class="btn btn-ghost">Installation Guide</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions" class="btn btn-ghost" target="_blank" rel="noopener">GitHub Repo</a>
      <a href="{{ '/assets/downloads/Unity-UI-Extensions-uGUI-Documentation.pdf' | relative_url }}" class="btn btn-ghost" download>Download PDF Docs</a>
    </div>
  </div>
</section>

<section class="section install-section" aria-labelledby="ugui-install-heading">
  <div class="section-inner">
    <h2 id="ugui-install-heading" class="section-title">Installation</h2>

    <div class="install-tabs" data-tabs>
      <div class="tab-bar">
        <button class="tab-btn active" data-tab="openupm">OpenUPM</button>
        <button class="tab-btn" data-tab="giturl">Git URL</button>
        <button class="tab-btn" data-tab="upm">Package Manager</button>
      </div>

      <div class="tab-panel active" data-panel="openupm">
        <h3>Install via OpenUPM</h3>
        <div class="install-panel">
          <pre><code>openupm add com.unity.uiextensions</code></pre>
          <button class="copy-btn" aria-label="Copy command">Copy</button>
        </div>
        <p>Or add the scoped registry manually in <code>Edit → Project Settings → Package Manager</code>:</p>
        <div class="install-panel">
          <pre><code>Name: package.openupm.com
URL: https://package.openupm.com
Scope: com.unity.uiextensions</code></pre>
          <button class="copy-btn" aria-label="Copy registry settings">Copy</button>
        </div>
      </div>

      <div class="tab-panel" data-panel="giturl">
        <h3>Install via Git URL</h3>
        <p>Open the Package Manager (<code>Window → Package Manager</code>), click <strong>+</strong> → <strong>Add package from git URL</strong> and paste:</p>
        <div class="install-panel">
          <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git</code></pre>
          <button class="copy-btn" aria-label="Copy git URL">Copy</button>
        </div>
        <p>Pin to a specific release by appending <code>#2.3.2</code> (or desired tag) to the URL.</p>
      </div>

      <div class="tab-panel" data-panel="upm">
        <h3>Manual / Embedded Package</h3>
        <ol>
          <li>Download the latest <code>.zip</code> or <code>.unitypackage</code> from the <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/releases" target="_blank" rel="noopener">Releases page</a></li>
          <li>Extract and place the folder in your project's <code>Packages/</code> directory</li>
          <li>Unity will automatically detect and import the package</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section id="controls" class="section controls-section" aria-labelledby="controls-heading">
  <div class="section-inner">
    <h2 id="controls-heading" class="section-title">All Controls</h2>

    <div class="controls-toolbar">
      <div class="search-wrap">
        <input id="control-search" type="search" placeholder="Search controls…" aria-label="Search controls">
      </div>

      <div class="filter-bar" role="group" aria-label="Filter by category">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="layout">Layout</button>
        <button class="filter-btn" data-filter="input">Input</button>
        <button class="filter-btn" data-filter="primitives">Primitives</button>
        <button class="filter-btn" data-filter="effects">Effects</button>
        <button class="filter-btn" data-filter="utilities">Utilities</button>
        <button class="filter-btn" data-filter="navigation">Navigation</button>
      </div>
    </div>

    <div class="controls-grid" aria-live="polite">
      {% for ctrl in site.data.ugui_controls %}
        <a href="{{ ctrl.permalink | relative_url }}"
           class="control-card"
           data-category="{{ ctrl.category | downcase }}"
           data-name="{{ ctrl.name | downcase }}"
           data-desc="{{ ctrl.description | downcase }}"
           data-tags="{{ ctrl.tags | join: ' ' | downcase }}"
           aria-label="{{ ctrl.name }} — {{ ctrl.description }}">

          {% if ctrl.preview_image != "" %}
            <div class="control-card-img">
              <img src="{{ ctrl.preview_image }}" alt="{{ ctrl.name }} preview" loading="lazy">
            </div>
          {% else %}
            <div class="control-card-img control-card-img--placeholder" aria-hidden="true">
              <span>{{ ctrl.name | truncate: 2, "" | upcase }}</span>
            </div>
          {% endif %}

          <div class="control-card-body">
            <div class="control-card-head">
              <h3 class="control-card-name">{{ ctrl.name }}</h3>
              <span class="badge-ghost control-card-cat">{{ ctrl.category }}</span>
            </div>
            <p class="control-card-desc">{{ ctrl.description }}</p>
            <div class="control-card-footer">
              {% if ctrl.has_video %}<span class="tag tag--video">Video</span>{% endif %}
              {% for tag in ctrl.tags limit: 3 %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
        </a>
      {% endfor %}
    </div>

    <p id="no-results" class="no-results" style="display:none" role="status">
      No controls match your search. Try a different term or clear the filter.
    </p>
  </div>
</section>
