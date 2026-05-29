/* ============================================================
   Unity UI Extensions — Site JavaScript
   Handles: tabs, copy buttons, search/filter, scroll-spy,
   animated counters, mobile nav
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     Tabs
  ---------------------------------------------------------- */
  function initTabs() {
    document.querySelectorAll('[data-tabs]').forEach(function (tabGroup) {
      var btns = tabGroup.querySelectorAll('.tab-btn');
      var panels = tabGroup.querySelectorAll('.tab-panel');

      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var target = btn.dataset.tab;
          btns.forEach(function (b) { b.classList.remove('active'); });
          panels.forEach(function (p) { p.classList.remove('active'); });
          btn.classList.add('active');
          var panel = tabGroup.querySelector('.tab-panel[data-panel="' + target + '"]');
          if (panel) panel.classList.add('active');
        });
      });
    });
  }

  /* ----------------------------------------------------------
     Copy Buttons
  ---------------------------------------------------------- */
  function initCopyButtons() {
    document.querySelectorAll('.copy-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = btn.dataset.copy;
        var text = target
          ? (document.querySelector(target) || { textContent: '' }).textContent
          : btn.closest('.install-panel')
              ? btn.closest('.install-panel').querySelector('pre, code').textContent
              : '';

        if (!text) return;

        navigator.clipboard.writeText(text.trim()).then(function () {
          var orig = btn.textContent;
          btn.textContent = 'Copied!';
          btn.classList.add('copied');
          setTimeout(function () {
            btn.textContent = orig;
            btn.classList.remove('copied');
          }, 1800);
        });
      });
    });
  }

  /* ----------------------------------------------------------
     Control Search + Category Filter
  ---------------------------------------------------------- */
  function initControlFilter() {
    var searchInput = document.getElementById('control-search');
    var filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
    var cards = document.querySelectorAll('.control-card[data-category]');
    var noResults = document.getElementById('no-results');

    if (!searchInput && filterBtns.length === 0) return;

    var activeCategory = 'all';
    var searchQuery = '';

    function updateCards() {
      var visible = 0;
      cards.forEach(function (card) {
        var name = (card.dataset.name || card.querySelector('.control-card-name') && card.querySelector('.control-card-name').textContent || '').toLowerCase();
        var desc = (card.dataset.desc || card.querySelector('.control-card-desc') && card.querySelector('.control-card-desc').textContent || '').toLowerCase();
        var tags = (card.dataset.tags || '').toLowerCase();
        var cat = (card.dataset.category || '').toLowerCase();

        var matchesSearch = !searchQuery
          || name.includes(searchQuery)
          || desc.includes(searchQuery)
          || tags.includes(searchQuery);

        var matchesCat = activeCategory === 'all'
          || cat === activeCategory;

        var show = matchesSearch && matchesCat;
        card.style.display = show ? '' : 'none';
        if (show) visible++;
      });

      if (noResults) {
        noResults.style.display = visible === 0 ? '' : 'none';
      }
    }

    if (searchInput) {
      searchInput.addEventListener('input', function () {
        searchQuery = searchInput.value.trim().toLowerCase();
        updateCards();
      });
    }

    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        activeCategory = (btn.dataset.filter || 'all').toLowerCase();
        updateCards();
      });
    });
  }

  /* ----------------------------------------------------------
     Animated Counters
  ---------------------------------------------------------- */
  function initCounters() {
    var counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseInt(el.dataset.count, 10);
        var suffix = el.dataset.suffix || '';
        var duration = 1400;
        var start = performance.now();

        function step(now) {
          var elapsed = now - start;
          var progress = Math.min(elapsed / duration, 1);
          // Ease out cubic
          var ease = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(ease * target) + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
        observer.unobserve(el);
      });
    }, { threshold: 0.3 });

    counters.forEach(function (el) { observer.observe(el); });
  }

  /* ----------------------------------------------------------
     Scroll-spy sidebar
  ---------------------------------------------------------- */
  function initScrollSpy() {
    var sidebarLinks = document.querySelectorAll('.sidebar-link[href^="#"]');
    if (!sidebarLinks.length) return;

    var sections = Array.from(sidebarLinks).map(function (link) {
      var id = link.getAttribute('href').slice(1);
      return { link: link, el: document.getElementById(id) };
    }).filter(function (s) { return s.el; });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        sections.forEach(function (s) { s.link.classList.remove('active'); });
        var found = sections.find(function (s) { return s.el === entry.target; });
        if (found) found.link.classList.add('active');
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    sections.forEach(function (s) { observer.observe(s.el); });
  }

  /* ----------------------------------------------------------
     Mobile nav toggle
  ---------------------------------------------------------- */
  function initMobileNav() {
    var toggle = document.querySelector('.nav-mobile-toggle');
    var navLinks = document.querySelector('.nav-links');
    if (!toggle || !navLinks) return;

    toggle.addEventListener('click', function () {
      var open = navLinks.style.display === 'flex';
      navLinks.style.display = open ? '' : 'flex';
      navLinks.style.flexDirection = open ? '' : 'column';
      navLinks.style.position = open ? '' : 'absolute';
      navLinks.style.top = open ? '' : 'var(--nav-h)';
      navLinks.style.left = open ? '' : '0';
      navLinks.style.right = open ? '' : '0';
      navLinks.style.background = open ? '' : 'var(--bg-2)';
      navLinks.style.padding = open ? '' : '1rem 1.5rem';
      navLinks.style.borderBottom = open ? '' : '1px solid var(--border)';
      navLinks.style.zIndex = open ? '' : '899';
    });
  }

  /* ----------------------------------------------------------
     Sidebar toggle (mobile)
  ---------------------------------------------------------- */
  function initSidebarToggle() {
    var toggle = document.querySelector('.sidebar-toggle');
    var sidebar = document.querySelector('.sidebar');
    if (!toggle || !sidebar) return;

    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
    });

    document.addEventListener('click', function (e) {
      if (sidebar.classList.contains('open')
        && !sidebar.contains(e.target)
        && !toggle.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  /* ----------------------------------------------------------
     Initialise all
  ---------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', function () {
    initTabs();
    initCopyButtons();
    initControlFilter();
    initCounters();
    initScrollSpy();
    initMobileNav();
    initSidebarToggle();
  });

}());
