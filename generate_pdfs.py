#!/usr/bin/env python3
"""
generate_pdfs.py — Build documentation & press-kit PDFs via headless Chrome/Edge.

Renders on-brand ("Neon Arcade") HTML and prints it to PDF using a headless
Chromium browser (Google Chrome, Chromium, or Microsoft Edge).

Each package PDF is a full sales + technical document:
  cover (social banner) -> table of contents -> every control's doc page
  -> every example's doc page -> closing "find out more & support" page.

Control/example ordering and categories come from _data/*.yml; the rich page
bodies are pulled from the matching markdown docs (joined by `permalink`) and
rendered to HTML with the `markdown` library.

Outputs (assets/downloads/):
  Unity-UI-Extensions-PressKit.pdf
  Unity-UI-Extensions-uGUI-Documentation.pdf
  Unity-UI-Extensions-UIToolkit-Documentation.pdf

Usage:
  python generate_pdfs.py                  # all PDFs
  python generate_pdfs.py presskit         # one document
  python generate_pdfs.py ugui uitk        # several

Requires: a Chromium-based browser on PATH; PyYAML + Markdown for package docs.
  pip install pyyaml markdown
"""

import os
import re
import sys
import glob
import shutil
import tempfile
import datetime
import subprocess
import html as html_lib

try:
    import yaml
except ImportError:
    yaml = None
try:
    import markdown as _markdown
except ImportError:
    _markdown = None

# ── Paths ───────────────────────────────────────────────────────────────────
BASE      = os.path.dirname(os.path.abspath(__file__))
DATA      = os.path.join(BASE, "_data")
PRESSKIT  = os.path.join(BASE, "assets", "img", "presskit")
DOWNLOADS = os.path.join(BASE, "assets", "downloads")
os.makedirs(DOWNLOADS, exist_ok=True)
DATE = datetime.date.today().strftime("%B %Y")

# ── Brand palette ────────────────────────────────────────────────────────────
BG, BG2 = "#050508", "#08080e"
MAG, CYAN = "#ff0099", "#00ffee"
TEXT, T2, MUTED = "#ffffff", "#dd88ff", "#663388"

FONTS = ("https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800"
         "&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap")

LOGO = ('<svg width="60" height="60" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">'
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ff0099"/><stop offset="1" stop-color="#00ffee"/>'
        '</linearGradient></defs>'
        '<rect x="2" y="2" width="60" height="60" rx="12" fill="#0a0a14" stroke="#ff009955"/>'
        '<g fill="url(#g)"><rect x="16" y="14" width="9" height="28" rx="2"/>'
        '<rect x="39" y="14" width="9" height="28" rx="2"/>'
        '<rect x="16" y="35" width="32" height="9" rx="2"/></g></svg>')

# ── Package configuration ─────────────────────────────────────────────────────
UGUI_CFG = dict(
    title="Unity UI Extensions",
    subtitle="uGUI package — complete control & example reference",
    banner="social-banner-ugui-1200x630.svg", accent=MAG,
    version="3.0", license="BSD-3-Clause",
    controls_yml=os.path.join(DATA, "ugui_controls.yml"),
    examples_yml=os.path.join(DATA, "ugui_examples.yml"),
    controls_glob=os.path.join(BASE, "Controls", "*.md"),
    examples_glob=os.path.join(BASE, "ugui", "examples", "*", "index.md"),
    pkg_id="com.unity.uiextensions",
    repo="Unity-UI-Extensions/com.unity.uiextensions",
    filename="Unity-UI-Extensions-uGUI-Documentation.pdf",
)
UITK_CFG = dict(
    title="Unity UI Toolkit Extensions",
    subtitle="UI Toolkit package — complete control & example reference",
    banner="social-banner-uitoolkit-1200x630.svg", accent=CYAN,
    version="1.0", license="MIT",
    controls_yml=os.path.join(DATA, "uitk_controls.yml"),
    examples_yml=os.path.join(DATA, "uitk_examples.yml"),
    controls_glob=os.path.join(BASE, "uitoolkit", "controls", "*", "index.md"),
    examples_glob=os.path.join(BASE, "uitoolkit", "examples", "*", "index.md"),
    pkg_id="com.unity.uitoolkitextensions",
    repo="Unity-UI-Extensions/com.unity.uitoolkitextensions",
    filename="Unity-UI-Extensions-UIToolkit-Documentation.pdf",
)

# ── Small helpers ──────────────────────────────────────────────────────────────
def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""

def fm_field(text, field):
    m = re.search(rf'(?mi)^{field}:\s*"?([^"\n]+?)"?\s*$', text)
    return m.group(1).strip() if m else ""

def esc(s):
    return html_lib.escape(s or "")

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")

def file_uri(path):
    return "file:///" + os.path.abspath(path).replace("\\", "/")

def inline_svg(path):
    s = read(path).strip()
    return s if s.startswith("<svg") else ""

def load_yaml(path):
    data = yaml.safe_load(read(path))
    return data if isinstance(data, list) else []

# ── Markdown rendering ─────────────────────────────────────────────────────────
_MD = _markdown.Markdown(extensions=["extra", "sane_lists"],
                         output_format="html5") if _markdown else None

def split_front_matter(raw):
    m = re.match(r"(?s)\A---\n.*?\n---\n?(.*)\Z", raw)
    return m.group(1) if m else raw

def clean_md_body(body):
    body = body.lstrip("\n")
    # Drop a single leading H1 — we render our own control/example title.
    body = re.sub(r"\A#\s+[^\n]*\n", "", body)
    # Drop the legacy per-control "## Contents" mini-TOC (the PDF has its own TOC).
    body = re.sub(r"(?ms)^##\s+Contents\b.*?\n-{3,}[ \t]*\n", "", body)
    return body.strip()

def demote_headings(html, by=2):
    def repl(m):
        return f"<{m.group(1)}h{min(int(m.group(2)) + by, 6)}"
    return re.sub(r"<(/?)h([1-6])\b", repl, html)

def process_images(html):
    """Rewrite root-absolute image src to file:// URIs; drop missing/video images."""
    def repl(m):
        tag, src = m.group(0), m.group(1)
        if not src.startswith("/"):
            return tag
        clean = src.split("?")[0].split("#")[0]
        if clean.lower().endswith((".mp4", ".webm", ".mov", ".avi")):
            return ""  # video can't embed in a PDF
        local = os.path.join(BASE, clean.lstrip("/").replace("/", os.sep))
        if not os.path.exists(local):
            return ""  # drop broken images rather than show a placeholder
        return tag.replace(f'src="{src}"', f'src="{file_uri(local)}"')
    return re.sub(r'<img\b[^>]*\bsrc="([^"]*)"[^>]*>', repl, html)

def render_body(filepath):
    """Markdown doc file -> branded HTML body (or None if no file)."""
    if not filepath:
        return None
    body = clean_md_body(split_front_matter(read(filepath)))
    if not body:
        return None
    _MD.reset()
    return process_images(demote_headings(_MD.convert(body)))

def build_permalink_index(pattern):
    """Map normalised permalink -> markdown file, by scanning front matter."""
    idx = {}
    for p in glob.glob(pattern):
        pl = fm_field(read(p), "permalink")
        if pl:
            idx[pl.rstrip("/") + "/"] = p
    return idx

def group_by_category(items):
    order, buckets = [], {}
    for it in items:
        cat = (it.get("category") or "Other").strip()
        if cat not in buckets:
            buckets[cat] = []
            order.append(cat)
        buckets[cat].append(it)
    return [(cat, buckets[cat]) for cat in order]

# ── HTML shell with print CSS (dark, on-brand, A4) ────────────────────────────
_CSS = """
@page { size: A4; margin: 14mm 15mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html, body { margin: 0; }
body { background: __BG__; color: __TEXT__; font-family: 'Inter', system-ui, sans-serif;
       font-size: 10.5pt; line-height: 1.5; }
h1, h2, h3, h4, h5, h6 { font-family: 'Orbitron', 'Space Grotesk', system-ui, sans-serif; color: #fff; line-height: 1.2; }
h1 { font-size: 30pt; letter-spacing: 1px; margin: 0 0 4pt; }
h2 { font-size: 16pt; color: __ACCENT__; border-bottom: 1px solid __ACCENT__55; padding-bottom: 4pt; margin: 22pt 0 10pt; }
h3 { font-size: 13pt; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 4pt 0; }
a { color: __ACCENT__; text-decoration: none; }
code, .mono { font-family: 'JetBrains Mono', monospace; font-size: 9pt; color: __CYAN__; }
.muted { color: __T2__; }
.lead { color: __T2__; font-size: 13pt; margin: 6pt 0; }
.badge { display: inline-block; width: fit-content; font-family: 'JetBrains Mono', monospace; font-size: 8pt;
         padding: 3pt 8pt; border: 1px solid __ACCENT__; color: __ACCENT__; border-radius: 3px; margin: 10pt 0; letter-spacing: 1px; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0; }
th, td { text-align: left; vertical-align: top; padding: 5pt 8pt; border-bottom: 1px solid #ffffff14; font-size: 10pt; }
th { color: __T2__; font-family: 'JetBrains Mono', monospace; font-weight: 600; }
pre { background: __BG2__; border: 1px solid __ACCENT__33; border-radius: 4px; padding: 8pt 10pt;
      font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; color: __CYAN__; white-space: pre-wrap;
      break-inside: avoid; }
ul, ol { margin: 4pt 0; padding-left: 18pt; } li { margin: 2pt 0; }
.foot { margin-top: 20pt; padding-top: 8pt; border-top: 1px solid #ffffff22; color: __MUTED__; font-size: 8.5pt; }
.pagebreak { break-before: page; }
.u { color: __MAG_LIT__; } .t { color: __CYAN__; }

/* press-kit factsheet table (key/value) */
.facts th { width: 30%; white-space: nowrap; }

/* stat row */
.statrow { display: flex; gap: 10pt; margin: 12pt 0; }
.stat { flex: 1; border: 1px solid __ACCENT__44; border-radius: 4px; padding: 9pt 11pt; background: __ACCENT__0d; }
.stat b { font-family: 'Orbitron', sans-serif; font-size: 18pt; color: __ACCENT__; display: block; line-height: 1; }
.stat span { font-size: 8.5pt; color: __T2__; }

/* package cover */
.pcover { break-after: page; }
.cover-banner { width: 100%; margin: 0 0 14pt; border-radius: 6px; overflow: hidden; border: 1px solid __ACCENT__44; }
.cover-banner svg { display: block; width: 100%; height: auto; }

/* press-kit cover (centred) */
.cover { min-height: 52vh; display: flex; flex-direction: column; justify-content: center; }

/* table of contents */
.toc { font-size: 10pt; }
.toc-h { font-family: 'Orbitron', sans-serif; color: __ACCENT__; font-size: 12pt; margin: 14pt 0 4pt; }
.toc-cat { color: __T2__; font-weight: 600; margin: 8pt 0 1pt; font-size: 9pt; text-transform: uppercase; letter-spacing: .5px; }
.toc-list { margin: 0 0 4pt; line-height: 1.7; color: __MUTED__; }
.toc-list a { color: #fff; }

/* section heads + entries */
.section-h { break-before: page; }
.cat { color: __ACCENT__; font-family: 'Orbitron', sans-serif; font-size: 12pt; margin: 18pt 0 4pt; break-after: avoid; }
.entry { margin: 0 0 8pt; padding-top: 8pt; }
.entry + .entry { border-top: 1px solid __ACCENT__22; }
h3 .tag { font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: __ACCENT__;
          border: 1px solid __ACCENT__55; border-radius: 3px; padding: 1pt 5pt; margin-left: 7pt;
          vertical-align: middle; letter-spacing: .5px; }
.lead-desc { color: __T2__; font-size: 10.5pt; margin: 2pt 0 6pt; }

/* rendered markdown doc body */
.doc { font-size: 10pt; }
.doc h4 { color: __ACCENT__; font-size: 11pt; margin: 11pt 0 3pt; break-after: avoid; }
.doc h5 { color: __T2__; font-size: 10pt; margin: 8pt 0 2pt; break-after: avoid; }
.doc h6 { color: __T2__; font-size: 9.5pt; margin: 6pt 0 2pt; }
.doc img { display: block; max-width: 80%; max-height: 105mm; width: auto; margin: 8pt auto;
           border: 1px solid __ACCENT__33; border-radius: 4px; break-inside: avoid; }
.doc th { color: __ACCENT__; }
.doc td code, .doc th code { white-space: pre-wrap; }
.doc blockquote { border-left: 2px solid __ACCENT__55; margin: 6pt 0; padding: 2pt 0 2pt 10pt; color: __T2__; }
.doc hr { border: none; border-top: 1px solid #ffffff14; margin: 10pt 0; }

/* support call-to-action */
.cta { border: 1px solid __ACCENT__; background: __ACCENT__0d; border-radius: 6px; padding: 12pt 14pt; margin: 12pt 0; }
.cta b { color: __ACCENT__; font-family: 'Orbitron', sans-serif; }
"""

def _css(accent):
    return (_CSS.replace("__BG2__", BG2).replace("__BG__", BG).replace("__TEXT__", TEXT)
            .replace("__ACCENT__", accent).replace("__CYAN__", CYAN)
            .replace("__T2__", T2).replace("__MUTED__", MUTED).replace("__MAG_LIT__", MAG))

def shell(title, accent, inner):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet"><style>{_css(accent)}</style></head><body>{inner}
<div class="foot">Generated {DATE} &middot; unity-ui-extensions.github.io &middot; BSD-3-Clause (uGUI) &amp; MIT (UI Toolkit) &middot; Not affiliated with Unity Technologies</div>
</body></html>"""

# ── Package document (cover -> TOC -> controls -> examples -> support) ──────────
def _entry(item, index, prefix):
    slug = item.get("slug") or slugify(item.get("name", ""))
    anchor = f"{prefix}-{slug}"
    name, cat = esc(item.get("name", "")), esc((item.get("category") or "Other").strip())
    desc = esc(item.get("description", ""))
    head = f'<h3 id="{anchor}">{name} <span class="tag">{cat}</span></h3>'
    lead = f'<p class="lead-desc">{desc}</p>' if desc else ""
    permalink = (item.get("permalink") or "").rstrip("/") + "/"
    body = render_body(index.get(permalink))
    if body:
        return f'<div class="entry">{head}{lead}<div class="doc">{body}</div></div>'
    # Fallback when no doc body exists: preview image (if any) + pointer to the site.
    img = process_images(f'<img src="{esc(item.get("preview_image",""))}">') if item.get("preview_image") else ""
    return (f'<div class="entry">{head}{lead}<div class="doc">{img}'
            f'<p class="muted">Full write-up and demo media on the website.</p></div></div>')

def _entries(grouped, index, prefix):
    out = []
    for cat, items in grouped:
        out.append(f'<div class="cat">{esc(cat)}</div>')
        out += [_entry(it, index, prefix) for it in items]
    return "".join(out)

def _toc(grouped_controls, grouped_examples):
    parts = ['<h2>Table of Contents</h2>', '<div class="toc">', '<div class="toc-h">Controls</div>']
    for label, grouped, prefix in (("", grouped_controls, "ctrl"),):
        for cat, items in grouped:
            links = " &middot; ".join(
                f'<a href="#{prefix}-{it.get("slug") or slugify(it["name"])}">{esc(it["name"])}</a>'
                for it in items)
            parts.append(f'<div class="toc-cat">{esc(cat)}</div><div class="toc-list">{links}</div>')
    parts.append('<div class="toc-h">Examples</div>')
    for cat, items in grouped_examples:
        links = " &middot; ".join(
            f'<a href="#ex-{it.get("slug") or slugify(it["name"])}">{esc(it["name"])}</a>'
            for it in items)
        parts.append(f'<div class="toc-cat">{esc(cat)}</div><div class="toc-list">{links}</div>')
    parts.append("</div>")
    return "".join(parts)

def _cover(cfg, n_controls, n_examples):
    return f"""
<div class="pcover">
  <div class="cover-banner">{inline_svg(os.path.join(PRESSKIT, cfg['banner']))}</div>
  <span class="badge">CONTROL &amp; EXAMPLE REFERENCE &middot; v{cfg['version']}</span>
  <h1>{esc(cfg['title'])}</h1>
  <p class="lead">{esc(cfg['subtitle'])}</p>
  <div class="statrow">
    <div class="stat"><b>{n_controls}</b><span>controls</span></div>
    <div class="stat"><b>{n_examples}</b><span>example scenes</span></div>
    <div class="stat"><b>{esc(cfg['license'])}</b><span>licensed</span></div>
    <div class="stat"><b>Unity&nbsp;6</b><span>6000.0+</span></div>
  </div>
</div>"""

def _closing(cfg):
    return f"""
<h2 class="section-h">Find Out More &amp; Support</h2>
<p>Unity UI Extensions is free and 100% open source, built and maintained by a global community since 2015.
Here is where to go next &mdash; and how to help keep it growing.</p>

<h3>Install</h3>
<p class="muted">Via OpenUPM:</p>
<pre>openupm add {cfg['pkg_id']}</pre>
<p class="muted">Via git URL (Unity Package Manager &rarr; Add package from git URL):</p>
<pre>https://github.com/{cfg['repo']}.git</pre>

<h3>Documentation &amp; source</h3>
<ul>
  <li>Website &amp; full docs: <b>unity-ui-extensions.github.io</b></li>
  <li>Source &amp; issues: github.com/{cfg['repo']}</li>
  <li>GitHub organisation: github.com/Unity-UI-Extensions</li>
  <li>Itch.io: unityuiextensions.itch.io/uiextensions2-0</li>
</ul>

<h3>Community</h3>
<ul>
  <li>Gitter chat &amp; GitHub Discussions &mdash; ask questions, share what you build</li>
  <li>Contributions welcome &mdash; {esc(cfg['license'])} licensed, every contributor credited</li>
</ul>

<div class="cta">
  <b>Support the project &#9829;</b>
  <p>This project is free and always will be. If it saves you time, please consider supporting ongoing
  development, new controls and documentation:</p>
  <ul>
    <li><b>Patreon:</b> patreon.com/UnityUIExtensions</li>
    <li><b>Sponsor / one-off:</b> via the links on unity-ui-extensions.github.io</li>
  </ul>
  <p class="muted">Every contribution funds new controls, examples, fixes and documentation.</p>
</div>

<p class="muted" style="margin-top:14pt;">Press &amp; partnerships: uiextensions@zenithmoon.com &middot;
Maintainer: Simon &ldquo;darkside&rdquo; Jackson (@SimonDarksideJ)</p>"""

def package_html(cfg):
    controls = load_yaml(cfg["controls_yml"])
    examples = load_yaml(cfg["examples_yml"])
    gc, ge = group_by_category(controls), group_by_category(examples)
    cidx = build_permalink_index(cfg["controls_glob"])
    eidx = build_permalink_index(cfg["examples_glob"])
    print(f"  {len(controls)} controls ({sum(1 for c in controls if (c.get('permalink','').rstrip('/')+'/') in cidx)} with doc bodies), "
          f"{len(examples)} examples ({sum(1 for e in examples if (e.get('permalink','').rstrip('/')+'/') in eidx)} with doc bodies)")
    inner = (_cover(cfg, len(controls), len(examples))
             + _toc(gc, ge)
             + '<h2 class="section-h">Controls</h2>' + _entries(gc, cidx, "ctrl")
             + '<h2 class="section-h">Examples</h2>' + _entries(ge, eidx, "ex")
             + _closing(cfg))
    return shell(f"{cfg['title']} — Documentation", cfg["accent"], inner)

# ── Press kit document ─────────────────────────────────────────────────────────
def presskit_html():
    banner = inline_svg(os.path.join(PRESSKIT, "social-banner-og-1200x630.svg"))
    inner = f"""
<div class="cover">
  <div class="cover-banner">{banner}</div>
  <span class="badge">PRESS KIT &middot; VERSION 3.0</span>
  <h1>Unity UI Extensions</h1>
  <p class="muted" style="font-size:13pt;">Two packages. One ecosystem.</p>
  <div class="statrow">
    <div class="stat"><b>126</b><span>UI controls</span></div>
    <div class="stat"><b>34</b><span>example scenes</span></div>
    <div class="stat"><b>2</b><span>packages</span></div>
    <div class="stat"><b>2015</b><span>community since</span></div>
  </div>
</div>

<h2 class="pagebreak">Factsheet</h2>
<table class="facts">
  <tr><th>Project</th><td>Unity UI Extensions</td></tr>
  <tr><th>Release</th><td>Version 3.0 &mdash; a two-package ecosystem relaunch</td></tr>
  <tr><th>Maintainer</th><td>Simon &ldquo;darkside&rdquo; Jackson (@SimonDarksideJ) &amp; a global community of contributors</td></tr>
  <tr><th>Community since</th><td>2015</td></tr>
  <tr><th>Packages</th><td>uGUI &mdash; <code>com.unity.uiextensions</code> (v3.0.0, BSD-3-Clause)<br>UI Toolkit &mdash; <code>com.unity.uitoolkitextensions</code> (v1.0.0, MIT)</td></tr>
  <tr><th>Engine</th><td>Unity 6 (6000.0+); the established 2.x line remains for older Unity versions</td></tr>
  <tr><th>Controls</th><td><b>126</b> total &mdash; 101 uGUI &middot; 25 UI Toolkit</td></tr>
  <tr><th>Examples</th><td><b>34</b> playable example scenes (22 uGUI &middot; 12 UI Toolkit)</td></tr>
  <tr><th>Price</th><td>Free &mdash; 100% open source, no lock-in</td></tr>
  <tr><th>Distribution</th><td>Unity Package Manager (OpenUPM &amp; git URL) &middot; Itch.io &middot; Unity Asset Store (uGUI; UI Toolkit listing coming soon)</td></tr>
  <tr><th>Website</th><td>unity-ui-extensions.github.io</td></tr>
  <tr><th>Source</th><td>uGUI &mdash; github.com/Unity-UI-Extensions/com.unity.uiextensions<br>UI Toolkit &mdash; github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions</td></tr>
  <tr><th>Community</th><td>Gitter &middot; GitHub Discussions</td></tr>
  <tr><th>Support</th><td>patreon.com/UnityUIExtensions</td></tr>
  <tr><th>Press contact</th><td>uiextensions@zenithmoon.com &middot; maintainer via GitHub / Patreon</td></tr>
</table>

<h2>About</h2>
<p><b>Stop rebuilding UI from scratch.</b> Unity UI Extensions is the flagship open-source UI control
collection for Unity &mdash; 126 battle-tested controls for both uGUI and UI Toolkit. The controls
you would build anyway are already here, polished and edge-case handled.</p>
<p>Community-driven since 2015, the project is 100% free and open source, distributed UPM-first via OpenUPM
and git URL, and licensed under BSD-3-Clause (uGUI) and MIT (UI Toolkit). Maintained by Simon &ldquo;darkside&rdquo;
Jackson and a global community of contributors.</p>

<h2>The two-package ecosystem</h2>
<h3 class="u">uGUI &mdash; Unity UI Extensions</h3>
<p>The original and largest collection &mdash; 101 production-ready controls for Unity's uGUI system,
refined over a decade of community use. This is the V3 release.</p>
<ul>
  <li>Package id <code>com.unity.uiextensions</code> &middot; v3.0.0 &middot; Unity 6000.0+ &middot; BSD-3-Clause</li>
  <li>101 controls &middot; ~195 runtime scripts &middot; 22 example scenes</li>
</ul>
<h3 class="t">UI Toolkit &mdash; Unity UI Toolkit Extensions</h3>
<p>The modern companion &mdash; 25 USS-themable, data-driven controls built from the ground up for
Unity 6's UI Toolkit runtime.</p>
<ul>
  <li>Package id <code>com.unity.uitoolkitextensions</code> &middot; v1.0.0 &middot; Unity 6000.0+ &middot; MIT</li>
  <li>25 controls &middot; ~21 runtime scripts &middot; 12 example scenes</li>
</ul>

<h2>Key features</h2>
<ul>
  <li><b>Ship weeks faster</b> &mdash; the controls you would build anyway, polished and edge-case handled.</li>
  <li><b>Production battle-tested</b> &mdash; a decade of community use, bug reports and fixes since 2015.</li>
  <li><b>UPM-first distribution</b> &mdash; OpenUPM or git URL, clean dependency management.</li>
  <li><b>Fully customisable</b> &mdash; Inspector-exposed for uGUI, USS-themable for UI Toolkit.</li>
  <li><b>Examples included</b> &mdash; 34 playable example scenes across both packages.</li>
  <li><b>Open contribution</b> &mdash; BSD-3 &amp; MIT, PRs welcome, every contributor credited.</li>
</ul>

<h2>Quote</h2>
<p>&ldquo;Two packages, one ecosystem &mdash; that is the whole story of 3.0. For ten years the community has built
the controls you would build anyway, polished them, and handled the edge cases so you do not have to. Ship faster.
Build better.&rdquo;<br>
<b>&mdash; Simon &ldquo;darkside&rdquo; Jackson, project maintainer</b></p>

<div class="cta">
  <b>Support the project &#9829;</b>
  <p>Free and open source, funded by the community. Support development at
  <b>patreon.com/UnityUIExtensions</b>.</p>
</div>
"""
    return shell("Unity UI Extensions — Press Kit", MAG, inner)

# ── Headless-browser rendering ─────────────────────────────────────────────────
def find_browser():
    env = os.environ.get("CHROME_BIN") or os.environ.get("CHROME_PATH") or os.environ.get("BROWSER")
    if env and os.path.exists(env):
        return env
    names = ["chrome", "google-chrome", "google-chrome-stable", "chromium",
             "chromium-browser", "msedge", "microsoft-edge", "microsoft-edge-stable"]
    for n in names:
        p = shutil.which(n)
        if p:
            return p
    pf  = os.environ.get("ProgramFiles", r"C:\Program Files")
    pfx = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
    la  = os.environ.get("LOCALAPPDATA", "")
    candidates = [
        os.path.join(pf,  "Google", "Chrome", "Application", "chrome.exe"),
        os.path.join(pfx, "Google", "Chrome", "Application", "chrome.exe"),
        os.path.join(la,  "Google", "Chrome", "Application", "chrome.exe"),
        os.path.join(pfx, "Microsoft", "Edge", "Application", "msedge.exe"),
        os.path.join(pf,  "Microsoft", "Edge", "Application", "msedge.exe"),
        "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def html_to_pdf(html_str, output_path, browser):
    if os.path.exists(output_path):
        os.remove(output_path)
    with tempfile.TemporaryDirectory() as td:
        htmlfile = os.path.join(td, "doc.html")
        with open(htmlfile, "w", encoding="utf-8") as f:
            f.write(html_str)
        uri = "file:///" + htmlfile.replace("\\", "/")
        profile = os.path.join(td, "profile")
        # --disable-dev-shm-usage and --no-zygote harden against the headless-Chrome
        # hangs/crashes that are common on CI runners (tiny /dev/shm, sandboxing).
        base = [browser, "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage",
                "--no-zygote", "--no-pdf-header-footer", f"--user-data-dir={profile}",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=15000", f"--print-to-pdf={output_path}"]
        for headless in ("--headless=new", "--headless"):
            try:
                # Do NOT capture output. Headless Chrome forks child processes that
                # inherit the stdout/stderr pipes and keep them open; with
                # capture_output the timeout fires but subprocess.run then blocks
                # forever draining the pipe (this was the indefinite CI hang).
                # Redirecting to DEVNULL removes the pipe so the timeout works.
                subprocess.run([browser, headless] + base[1:] + [uri],
                               stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=120)
            except subprocess.TimeoutExpired:
                pass
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                return True
        return False

def emit(html_str, filename, browser):
    out = os.path.join(DOWNLOADS, filename)
    ok = html_to_pdf(html_str, out, browser)
    print(f"  {'OK  ' if ok else 'FAIL'} {filename}" + (f"  ({os.path.getsize(out)//1024} KB)" if ok else ""))
    return ok

# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Select which document(s) to build. With no args, build all; otherwise name
    # one or more targets — CI builds one PDF per parallel job:
    #   python generate_pdfs.py presskit | ugui | uitk
    ALIASES = {"presskit": "presskit", "ugui": "ugui", "uitk": "uitk", "uitoolkit": "uitk"}
    requested = {ALIASES[a] for a in (x.lstrip("-").lower() for x in sys.argv[1:]) if a in ALIASES}
    want = (lambda name: True) if not requested else (lambda name: name in requested)

    if (want("ugui") or want("uitk")) and (yaml is None or _markdown is None):
        print("ERROR: package docs need PyYAML and Markdown.  pip install pyyaml markdown")
        sys.exit(1)

    browser = find_browser()
    if not browser:
        print("ERROR: No Chromium-based browser (Chrome / Chromium / Edge) found.")
        print("Install one, or in CI add e.g. `browser-actions/setup-chrome`.")
        sys.exit(1)
    print(f"Using browser: {browser}")
    print(f"Generating PDFs: {', '.join(sorted(requested)) or 'all'}")

    results = []
    if want("presskit"):
        results.append(emit(presskit_html(), "Unity-UI-Extensions-PressKit.pdf", browser))
    if want("ugui"):
        print("uGUI document:")
        results.append(emit(package_html(UGUI_CFG), UGUI_CFG["filename"], browser))
    if want("uitk"):
        print("UI Toolkit document:")
        results.append(emit(package_html(UITK_CFG), UITK_CFG["filename"], browser))

    print("Done." if all(results) else "Done with errors.")
    sys.exit(0 if results and all(results) else 1)
