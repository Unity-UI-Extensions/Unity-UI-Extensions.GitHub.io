---
layout: default
title: UIToolkit Controls — Unity UIToolkit Extensions
description: 18 modern UI controls and manipulators for Unity's UI Toolkit framework. Navigation, forms, feedback, and more.
permalink: /uitoolkit/
---

<section class="pkg-hero uitk-context">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">UI Toolkit</span>
    </nav>
    <div class="pkg-hero-badge"><span class="badge-t">UI Toolkit Package</span></div>
    <h1>UIToolkit Extensions</h1>
    <p class="pkg-hero-lead">18 modern controls and manipulators for Unity's UI Toolkit framework. Built for runtime UI — ready for production.</p>
    <div class="pkg-hero-meta">
      <code class="pkg-id">com.unity.uitoolkitextensions</code>
      <span class="badge-ghost">MIT Licence</span>
      <span class="badge-ghost">Unity 2022.3+</span>
    </div>
    <div class="pkg-hero-actions">
      <a href="#controls" class="btn btn-t">Browse Controls</a>
      <a href="{{ '/uitoolkit/install/' | relative_url }}" class="btn btn-ghost">Installation Guide</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions" class="btn btn-ghost" target="_blank" rel="noopener">GitHub Repo</a>
      <a href="{{ '/assets/downloads/Unity-UI-Extensions-UIToolkit-Documentation.pdf' | relative_url }}" class="btn btn-ghost" download>Download PDF Docs</a>
    </div>
  </div>
</section>

<section class="section install-section uitk-context" aria-labelledby="uitk-install-heading">
  <div class="section-inner">
    <h2 id="uitk-install-heading" class="section-title">Installation</h2>

    <div class="install-tabs" data-tabs>
      <div class="tab-bar">
        <button class="tab-btn active" data-tab="openupm">OpenUPM</button>
        <button class="tab-btn" data-tab="giturl">Git URL</button>
        <button class="tab-btn" data-tab="manual">Manual</button>
      </div>

      <div class="tab-panel active" data-panel="openupm">
        <h3>Install via OpenUPM</h3>
        <div class="install-panel">
          <pre><code>openupm add com.unity.uitoolkitextensions</code></pre>
          <button class="copy-btn" aria-label="Copy command">Copy</button>
        </div>
        <p>Or add the scoped registry manually in <code>Edit → Project Settings → Package Manager</code>:</p>
        <div class="install-panel">
          <pre><code>Name: package.openupm.com
URL: https://package.openupm.com
Scope: com.unity.uitoolkitextensions</code></pre>
          <button class="copy-btn" aria-label="Copy registry settings">Copy</button>
        </div>
      </div>

      <div class="tab-panel" data-panel="giturl">
        <h3>Install via Git URL</h3>
        <p>Open the Package Manager (<code>Window → Package Manager</code>), click <strong>+</strong> → <strong>Add package from git URL</strong> and paste:</p>
        <div class="install-panel">
          <pre><code>https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git</code></pre>
          <button class="copy-btn" aria-label="Copy git URL">Copy</button>
        </div>
      </div>

      <div class="tab-panel" data-panel="manual">
        <h3>Manual / Embedded Package</h3>
        <ol>
          <li>Download the latest release from the <a href="https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions/releases" target="_blank" rel="noopener">Releases page</a></li>
          <li>Extract and place the folder in your project's <code>Packages/</code> directory</li>
          <li>Unity will automatically detect and import the package</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section id="controls" class="section controls-section uitk-context" aria-labelledby="uitk-controls-heading">
  <div class="section-inner">
    <h2 id="uitk-controls-heading" class="section-title">All Controls</h2>

    <div class="controls-toolbar">
      <div class="search-wrap">
        <input id="control-search" type="search" placeholder="Search controls…" aria-label="Search controls">
      </div>

      <div class="filter-bar" role="group" aria-label="Filter by category">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="navigation">Navigation</button>
        <button class="filter-btn" data-filter="forms">Forms</button>
        <button class="filter-btn" data-filter="feedback">Feedback</button>
        <button class="filter-btn" data-filter="primitives">Primitives</button>
        <button class="filter-btn" data-filter="utilities">Utilities</button>
      </div>
    </div>

    <div class="controls-grid" aria-live="polite">
      {% for ctrl in site.data.uitk_controls %}
        <a href="{{ ctrl.permalink | relative_url }}"
           class="control-card uitk-context"
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
            <div class="control-card-img control-card-img--placeholder control-card-img--uitk" aria-hidden="true">
              <span>{{ ctrl.name | truncate: 2, "" | upcase }}</span>
            </div>
          {% endif %}

          <div class="control-card-body">
            <div class="control-card-head">
              <h3 class="control-card-name">{{ ctrl.name }}</h3>
              <span class="badge-t control-card-cat">{{ ctrl.category }}</span>
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
