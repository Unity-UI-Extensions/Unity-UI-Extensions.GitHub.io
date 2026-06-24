---
layout: default
title: uGUI Examples — Unity UI Extensions
description: Browse the 22 playable uGUI example scenes and see which controls each one demonstrates.
permalink: /ugui/examples/
---

<section class="pkg-hero">
  <div class="pkg-hero-inner">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true">›</span>
      <a href="{{ '/ugui/' | relative_url }}">uGUI</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">Examples</span>
    </nav>
    <div class="pkg-hero-badge"><span class="badge-u">uGUI Package</span></div>
    <h1>uGUI Examples</h1>
    <p class="pkg-hero-lead">Playable sample scenes bundled with the package. Every example lists the controls it demonstrates — open one to see what it shows, how to run it, and what to expect.</p>
    <div class="pkg-hero-actions">
      <a href="{{ '/ugui/' | relative_url }}#controls" class="btn btn-u">Browse Controls</a>
      <a href="https://github.com/Unity-UI-Extensions/com.unity.uiextensions/tree/release/Examples~" class="btn btn-ghost" target="_blank" rel="noopener">Examples on GitHub</a>
    </div>
  </div>
</section>

<section id="examples" class="section controls-section" aria-labelledby="ugui-examples-heading">
  <div class="section-inner">
    <h2 id="ugui-examples-heading" class="section-title">All Examples</h2>

    <div class="controls-toolbar">
      <div class="search-wrap">
        <input id="control-search" type="search" placeholder="Search examples…" aria-label="Search examples">
      </div>

      <div class="filter-bar" role="group" aria-label="Filter by category">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="layout">Layout</button>
        <button class="filter-btn" data-filter="input">Input</button>
        <button class="filter-btn" data-filter="navigation">Navigation</button>
        <button class="filter-btn" data-filter="primitives">Primitives</button>
        <button class="filter-btn" data-filter="effects">Effects</button>
        <button class="filter-btn" data-filter="utilities">Utilities</button>
      </div>
    </div>

    <div class="controls-grid" aria-live="polite">
      {% for ex in site.data.ugui_examples %}
        <a href="{{ ex.permalink | relative_url }}"
           class="control-card"
           data-category="{{ ex.category | downcase }}"
           data-name="{{ ex.name | downcase }}"
           data-desc="{{ ex.description | downcase }}"
           data-tags="{{ ex.tags | join: ' ' | downcase }}"
           aria-label="{{ ex.name }} — {{ ex.description }}">

          <div class="control-card-img control-card-img--placeholder" aria-hidden="true">
            <span>{{ ex.name | truncate: 2, "" | upcase }}</span>
          </div>

          <div class="control-card-body">
            <div class="control-card-head">
              <h3 class="control-card-name">{{ ex.name }}</h3>
              <span class="badge-u control-card-cat">{{ ex.category }}</span>
            </div>
            <p class="control-card-desc">{{ ex.description }}</p>
            <div class="control-card-footer">
              <span class="tag tag--count">{{ ex.controls | size }} control{% if ex.controls.size != 1 %}s{% endif %}</span>
              {% for tag in ex.tags limit: 3 %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
        </a>
      {% endfor %}
    </div>

    <p id="no-results" class="no-results" style="display:none" role="status">
      No examples match your search. Try a different term or clear the filter.
    </p>
  </div>
</section>
