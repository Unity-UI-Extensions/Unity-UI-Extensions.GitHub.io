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
     Visitor counter (homepage)
     Pulls rolling-month and all-time visit counts from the
     GoatCounter public counter API. Counts are served formatted
     (locale separators), so digits are extracted and re-formatted.
     The element stays hidden if the API is unreachable or the
     "visitor counts" setting is disabled on the dashboard.
  ---------------------------------------------------------- */
  function initVisitorCounter() {
    var el = document.querySelector('.visitor-counter');
    if (!el || !window.fetch) return;

    var base = 'https://unity-ui-extensions.goatcounter.com/counter/TOTAL.json';

    function getCount(url) {
      return fetch(url).then(function (res) {
        if (!res.ok) throw new Error('counter unavailable');
        return res.json();
      }).then(function (data) {
        var digits = String(data.count).replace(/[^0-9]/g, '');
        if (!digits) throw new Error('no count');
        return parseInt(digits, 10);
      });
    }

    Promise.all([
      getCount(base + '?start=month'),
      getCount(base)
    ]).then(function (counts) {
      el.querySelector('.vc-month').textContent = counts[0].toLocaleString('en');
      el.querySelector('.vc-total').textContent = counts[1].toLocaleString('en');
      el.hidden = false;
    }).catch(function () { /* leave hidden — counter is decorative */ });
  }

  /* ----------------------------------------------------------
     Donate nudge toast
     Counts distinct visit DAYS in localStorage (nothing leaves
     the browser — the site's no-cookies/no-personal-data stance
     is unchanged). After 5 visit days a toast slides in inviting
     a donation. Shown at most once per 14 days; "Maybe later"
     or close snoozes 90 days; clicking Donate retires it.
     Local testing (never counts or persists anything):
       #donate-toast        — force-show the toast
       #donate-toast-reset  — clear stored nudge state
  ---------------------------------------------------------- */
  function initDonateNudge() {
    var KEY = 'uiext-donate-nudge';
    var DAYS_NEEDED = 5;
    var SHOW_DELAY = 2500;   // ms after load before sliding in
    var SNOOZE_SHOWN = 14, SNOOZE_DISMISS = 90;  // days

    var testMode = location.hash === '#donate-toast';

    var state = {};
    var store = function () {
      try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
    };
    try {
      if (location.hash === '#donate-toast-reset') {
        localStorage.removeItem(KEY);
        console.info('donate-nudge: stored state cleared');
        return;
      }
      state = JSON.parse(localStorage.getItem(KEY)) || {};
    } catch (e) {
      if (!testMode) return;  // no storage (private mode) — skip silently
    }
    state.days = state.days || 0;

    if (!testMode) {
      if (state.off) return;

      var today = new Date().toISOString().slice(0, 10);
      if (state.last !== today) {
        state.days += 1;
        state.last = today;
        store();
      }

      if (state.days < DAYS_NEEDED) return;
      if (state.snoozeUntil && Date.now() < state.snoozeUntil) return;
    }

    var track = function (name) {
      if (testMode) return;  // keep test runs out of the stats
      if (window.goatcounter && goatcounter.count)
        goatcounter.count({ event: true, path: 'donate-toast-' + name });
    };

    var toast = document.createElement('div');
    toast.className = 'donate-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.innerHTML =
      '<button class="donate-toast-close" aria-label="Dismiss">✕</button>' +
      '<p class="donate-toast-eyebrow">✦ Achievement unlocked — visit ' + Math.max(state.days, DAYS_NEEDED) + '</p>' +
      '<p class="donate-toast-msg">Looks like you are enjoying UI Extensions.<br>Would you consider donating to support the project?</p>' +
      '<div class="donate-toast-actions">' +
      '  <a href="/donate/#ways-to-give" class="btn btn-u">❤️ Support the project</a>' +
      '  <button class="donate-toast-later">Maybe later</button>' +
      '</div>';

    var hide = function (snoozeDays) {
      if (!testMode && snoozeDays) {
        state.snoozeUntil = Date.now() + snoozeDays * 864e5;
        store();
      }
      toast.classList.remove('show');
      setTimeout(function () { if (toast.parentNode) toast.parentNode.removeChild(toast); }, 500);
      document.removeEventListener('keydown', onKey);
    };

    var onKey = function (e) { if (e.key === 'Escape') { track('dismissed'); hide(SNOOZE_DISMISS); } };

    toast.querySelector('.donate-toast-close').addEventListener('click', function () {
      track('dismissed');
      hide(SNOOZE_DISMISS);
    });
    toast.querySelector('.donate-toast-later').addEventListener('click', function () {
      track('later');
      hide(SNOOZE_DISMISS);
    });
    toast.querySelector('a.btn').addEventListener('click', function () {
      track('donate-click');
      if (!testMode) { state.off = true; store(); }
      // Navigation proceeds normally.
    });

    setTimeout(function () {
      document.body.appendChild(toast);
      track('shown');
      if (!testMode) {
        state.snoozeUntil = Date.now() + SNOOZE_SHOWN * 864e5;
        store();
      }
      document.addEventListener('keydown', onKey);
      requestAnimationFrame(function () {
        requestAnimationFrame(function () { toast.classList.add('show'); });
      });
    }, SHOW_DELAY);
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
    initVisitorCounter();
    initDonateNudge();
  });

}());
