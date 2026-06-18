#!/usr/bin/env python3
"""
generate_pdfs.py — Build documentation & press-kit PDFs via headless Chrome/Edge.

This replaces the previous fpdf2-based routine (which could hang on large control
sets). It renders on-brand HTML and prints it to PDF using a headless Chromium
browser (Google Chrome, Chromium, or Microsoft Edge), so the output matches the
website's "Neon Arcade" identity exactly and never blocks on content quirks.

Outputs (assets/downloads/):
  Unity-UI-Extensions-PressKit.pdf
  Unity-UI-Extensions-uGUI-Documentation.pdf
  Unity-UI-Extensions-UIToolkit-Documentation.pdf

Usage:
  python generate_pdfs.py              # all PDFs
  python generate_pdfs.py --presskit   # press kit only (fast)

Requires: a Chromium-based browser on PATH or in a standard location.
No Python PDF dependencies. (In CI, install Chrome e.g. browser-actions/setup-chrome.)
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

# ── Paths ───────────────────────────────────────────────────────────────────
BASE         = os.path.dirname(os.path.abspath(__file__))
CONTROLS_DIR = os.path.join(BASE, "Controls")
UITK_DIR     = os.path.join(BASE, "uitoolkit", "controls")
DOWNLOADS    = os.path.join(BASE, "assets", "downloads")
os.makedirs(DOWNLOADS, exist_ok=True)
DATE = datetime.date.today().strftime("%B %Y")

# ── Honest counts (the project's documented control totals) ──────────────────
# uGUI: 64 controls with live demos + 37 documented (pending demo media) = 101
# (see _data/ugui_controls.yml and MISSING_CONTENT.md). UI Toolkit: 20.
UGUI_CONTROLS, UITK_CONTROLS, TOTAL_CONTROLS = 101, 20, 121
UGUI_EXAMPLES, UITK_EXAMPLES, TOTAL_EXAMPLES = 21, 8, 29

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

# ── Front-matter helpers ──────────────────────────────────────────────────────
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

def get_controls(glob_pattern):
    """Return [{title, category, description}] from markdown files with front matter."""
    items = []
    for p in sorted(glob.glob(glob_pattern)):
        raw = read(p)
        if not raw.startswith("---"):
            continue
        title = fm_field(raw, "title")
        if not title:
            continue
        items.append({
            "title": title,
            "category": fm_field(raw, "category") or "Other",
            "description": fm_field(raw, "description") or "",
        })
    return items

# ── HTML shell with print CSS (dark, on-brand, A4) ────────────────────────────
_CSS = """
@page { size: A4; margin: 0; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html, body { margin: 0; }
body { background: __BG__; color: __TEXT__; font-family: 'Inter', system-ui, sans-serif;
       font-size: 10.5pt; line-height: 1.5; padding: 14mm 15mm; }
h1, h2, h3, h4 { font-family: 'Orbitron', 'Space Grotesk', system-ui, sans-serif; color: #fff; line-height: 1.2; }
h1 { font-size: 30pt; letter-spacing: 1px; margin: 0 0 4pt; }
h2 { font-size: 15pt; color: __ACCENT__; border-bottom: 1px solid __ACCENT__55; padding-bottom: 4pt; margin: 22pt 0 8pt; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; }
p { margin: 4pt 0; }
a { color: __ACCENT__; text-decoration: none; }
code, .mono { font-family: 'JetBrains Mono', monospace; font-size: 9pt; color: __CYAN__; }
.muted { color: __T2__; }
.cover { min-height: 56vh; display: flex; flex-direction: column; justify-content: center; }
.badge { display: inline-block; width: fit-content; font-family: 'JetBrains Mono', monospace; font-size: 8pt;
         padding: 3pt 8pt; border: 1px solid __ACCENT__; color: __ACCENT__; border-radius: 3px; margin: 10pt 0; letter-spacing: 1px; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0; }
th, td { text-align: left; vertical-align: top; padding: 5pt 8pt; border-bottom: 1px solid #ffffff14; font-size: 10pt; }
th { width: 30%; color: __T2__; font-family: 'JetBrains Mono', monospace; font-weight: 600; white-space: nowrap; }
.statrow { display: flex; gap: 10pt; margin: 12pt 0; }
.stat { flex: 1; border: 1px solid __ACCENT__44; border-radius: 4px; padding: 9pt 11pt; background: __ACCENT__0d; }
.stat b { font-family: 'Orbitron', sans-serif; font-size: 20pt; color: __ACCENT__; display: block; line-height: 1; }
.stat span { font-size: 8.5pt; color: __T2__; }
.cat { color: __ACCENT__; font-family: 'Orbitron', sans-serif; font-size: 11pt; margin: 16pt 0 5pt; }
.ctrl { padding: 4pt 0; border-bottom: 1px solid #ffffff10; break-inside: avoid; }
.ctrl b { color: #fff; }
.ctrl .d { color: __T2__; font-size: 9.5pt; }
pre { background: __BG2__; border: 1px solid __ACCENT__33; border-radius: 4px; padding: 8pt 10pt;
      font-family: 'JetBrains Mono', monospace; font-size: 9pt; color: __CYAN__; white-space: pre-wrap; }
ul { margin: 4pt 0; padding-left: 16pt; } li { margin: 2pt 0; }
.foot { margin-top: 20pt; padding-top: 8pt; border-top: 1px solid #ffffff22; color: __MUTED__; font-size: 8.5pt; }
.pagebreak { break-before: page; }
.u { color: __MAG_LIT__; } .t { color: __CYAN__; }
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

# ── Press kit document ─────────────────────────────────────────────────────────
def presskit_html():
    inner = f"""
<div class="cover">{LOGO}
  <span class="badge">PRESS KIT &middot; VERSION 3.0</span>
  <h1>Unity UI Extensions</h1>
  <p class="muted" style="font-size:13pt;">Two packages. One ecosystem.</p>
  <div class="statrow">
    <div class="stat"><b>{TOTAL_CONTROLS}</b><span>UI controls</span></div>
    <div class="stat"><b>{TOTAL_EXAMPLES}</b><span>example scenes</span></div>
    <div class="stat"><b>2</b><span>packages</span></div>
    <div class="stat"><b>2015</b><span>community since</span></div>
  </div>
</div>

<h2 class="pagebreak">Factsheet</h2>
<table>
  <tr><th>Project</th><td>Unity UI Extensions</td></tr>
  <tr><th>Release</th><td>Version 3.0 &mdash; a two-package ecosystem relaunch</td></tr>
  <tr><th>Maintainer</th><td>Simon &ldquo;darkside&rdquo; Jackson (@SimonDarksideJ) &amp; a global community of contributors</td></tr>
  <tr><th>Community since</th><td>2015</td></tr>
  <tr><th>Packages</th><td>uGUI &mdash; <code>com.unity.uiextensions</code> (v3.0.0-pre.1, BSD-3-Clause)<br>UI Toolkit &mdash; <code>com.unity.uitoolkitextensions</code> (v1.0.0-pre.1, MIT)</td></tr>
  <tr><th>Engine</th><td>Unity 6 (6000.0+); the established 2.x line remains for older Unity versions</td></tr>
  <tr><th>Controls</th><td><b>{TOTAL_CONTROLS}</b> total &mdash; {UGUI_CONTROLS} uGUI &middot; {UITK_CONTROLS} UI Toolkit</td></tr>
  <tr><th>Examples</th><td><b>{TOTAL_EXAMPLES}</b> playable example scenes ({UGUI_EXAMPLES} uGUI &middot; {UITK_EXAMPLES} UI Toolkit)</td></tr>
  <tr><th>Price</th><td>Free &mdash; 100% open source, no lock-in</td></tr>
  <tr><th>Distribution</th><td>Unity Package Manager (OpenUPM &amp; git URL) &middot; Itch.io &middot; Unity Asset Store (planned)</td></tr>
  <tr><th>Website</th><td>unity-ui-extensions.github.io</td></tr>
  <tr><th>Source</th><td>github.com/Unity-UI-Extensions</td></tr>
  <tr><th>Community</th><td>Discord &middot; Gitter &middot; Unity Discussions</td></tr>
  <tr><th>Support</th><td>patreon.com/simonDarksideJ</td></tr>
  <tr><th>Press contact</th><td>uiextensions@zenithmoon.com &middot; maintainer via GitHub / Patreon</td></tr>
</table>

<h2>About</h2>
<p><b>Stop rebuilding UI from scratch.</b> Unity UI Extensions is the flagship open-source UI control
collection for Unity &mdash; {TOTAL_CONTROLS} battle-tested controls for both uGUI and UI Toolkit. The controls
you would build anyway are already here, polished and edge-case handled.</p>
<p>Community-driven since 2015, the project is 100% free and open source, distributed UPM-first via OpenUPM
and git URL, and licensed under BSD-3-Clause (uGUI) and MIT (UI Toolkit). Maintained by Simon &ldquo;darkside&rdquo;
Jackson and a global community of contributors.</p>

<h2>The two-package ecosystem</h2>
<h3 class="u">uGUI &mdash; Unity UI Extensions</h3>
<p>The original and largest collection &mdash; {UGUI_CONTROLS} production-ready controls for Unity's uGUI system,
refined over a decade of community use. This is the V3 release.</p>
<ul>
  <li>Package id <code>com.unity.uiextensions</code> &middot; v3.0.0-pre.1 &middot; Unity 6000.0+ &middot; BSD-3-Clause</li>
  <li>{UGUI_CONTROLS} controls &middot; ~195 runtime scripts &middot; {UGUI_EXAMPLES} example scenes</li>
  <li>Categories: Controls, Primitives, Layouts, Effects &amp; Utilities</li>
</ul>
<h3 class="t">UI Toolkit &mdash; Unity UI Toolkit Extensions</h3>
<p>The modern companion &mdash; {UITK_CONTROLS} USS-themable, data-driven controls built from the ground up for
Unity 6's UI Toolkit runtime.</p>
<ul>
  <li>Package id <code>com.unity.uitoolkitextensions</code> &middot; v1.0.0-pre.1 &middot; Unity 6000.0+ &middot; MIT</li>
  <li>{UITK_CONTROLS} controls &middot; ~21 runtime scripts &middot; {UITK_EXAMPLES} example scenes</li>
  <li>Built with USS &middot; fully themable &middot; data-driven UI</li>
</ul>

<h2>Key features</h2>
<ul>
  <li><b>Ship weeks faster</b> &mdash; the controls you would build anyway, polished and edge-case handled.</li>
  <li><b>Production battle-tested</b> &mdash; a decade of community use, bug reports and fixes since 2015.</li>
  <li><b>UPM-first distribution</b> &mdash; OpenUPM or git URL, clean dependency management.</li>
  <li><b>Fully customisable</b> &mdash; Inspector-exposed for uGUI, USS-themable for UI Toolkit.</li>
  <li><b>Examples included</b> &mdash; {TOTAL_EXAMPLES} playable example scenes across both packages.</li>
  <li><b>Open contribution</b> &mdash; BSD-3 &amp; MIT, PRs welcome, every contributor credited.</li>
</ul>

<h2>Install</h2>
<p class="muted">uGUI &mdash; via OpenUPM:</p>
<pre>openupm add com.unity.uiextensions</pre>
<p class="muted">uGUI &mdash; via git URL:</p>
<pre>https://github.com/Unity-UI-Extensions/com.unity.uiextensions.git</pre>
<p class="muted">UI Toolkit &mdash; via git URL:</p>
<pre>https://github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions.git</pre>

<h2>Quote</h2>
<p>&ldquo;Two packages, one ecosystem &mdash; that is the whole story of 3.0. For ten years the community has built
the controls you would build anyway, polished them, and handled the edge cases so you do not have to. The controls
you would build anyway are already here. Ship faster. Build better.&rdquo;<br>
<b>&mdash; Simon &ldquo;darkside&rdquo; Jackson, project maintainer</b></p>

<h2>Links &amp; contact</h2>
<ul>
  <li>Website &amp; docs: unity-ui-extensions.github.io</li>
  <li>GitHub organisation: github.com/Unity-UI-Extensions</li>
  <li>uGUI repo: github.com/Unity-UI-Extensions/com.unity.uiextensions</li>
  <li>UI Toolkit repo: github.com/Unity-UI-Extensions/com.unity.uitoolkitextensions</li>
  <li>Itch.io (uGUI): unityuiextensions.itch.io/uiextensions2-0</li>
  <li>Support (Patreon): patreon.com/simonDarksideJ</li>
  <li>Maintainer: Simon &ldquo;darkside&rdquo; Jackson (@SimonDarksideJ)</li>
</ul>
"""
    return shell("Unity UI Extensions — Press Kit", MAG, inner)

# ── Per-package control reference ──────────────────────────────────────────────
def reference_html(controls, package_name, accent, subtitle, total_in_pack=None):
    cats = sorted({c["category"] for c in controls})
    rows = []
    for cat in cats:
        rows.append(f'<div class="cat">{esc(cat)}</div>')
        for c in controls:
            if c["category"] != cat:
                continue
            desc = f'<div class="d">{esc(c["description"])}</div>' if c["description"] else ""
            rows.append(f'<div class="ctrl"><b>{esc(c["title"])}</b>{desc}</div>')
    n = len(controls)
    total = total_in_pack or n
    span = f"of {total} controls" if total > n else "controls documented"
    note = (f'<p class="muted">This package includes <b>{total}</b> controls in total. '
            f'This reference lists the <b>{n}</b> with full text documentation; a further '
            f'<b>{total - n}</b> have documentation with demo media pending (see the website).</p>'
            ) if total > n else ""
    heading = f"{n} of {total}" if total > n else f"{n}"
    inner = f"""
<div class="cover">{LOGO}
  <span class="badge">CONTROL REFERENCE &middot; VERSION 3.0</span>
  <h1>{esc(package_name)}</h1>
  <p class="muted" style="font-size:12pt;">{esc(subtitle)}</p>
  <div class="statrow"><div class="stat"><b>{n}</b><span>{span}</span></div></div>
  {note}
</div>
<h2 class="pagebreak">Controls ({heading})</h2>
{''.join(rows)}
"""
    return shell(f"{package_name} — Reference", accent, inner)

# ── Headless-browser rendering ─────────────────────────────────────────────────
def find_browser():
    # Explicit override (set by CI from the setup-chrome action output).
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
        base = [browser, "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                f"--user-data-dir={profile}", "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=10000", f"--print-to-pdf={output_path}"]
        for headless in ("--headless=new", "--headless"):
            try:
                subprocess.run([browser, headless] + base[1:] + [uri],
                               capture_output=True, text=True, timeout=120)
            except subprocess.TimeoutExpired:
                pass
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                return True
        return False

def emit(html_str, filename, browser):
    out = os.path.join(DOWNLOADS, filename)
    ok = html_to_pdf(html_str, out, browser)
    if ok:
        print(f"  OK   {filename}  ({os.path.getsize(out)//1024} KB)")
    else:
        print(f"  FAIL {filename}")
    return ok

# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    only_presskit = ("--presskit" in sys.argv) or ("presskit" in sys.argv)

    browser = find_browser()
    if not browser:
        print("ERROR: No Chromium-based browser (Chrome / Chromium / Edge) found.")
        print("Install one, or in CI add e.g. `browser-actions/setup-chrome`.")
        sys.exit(1)
    print(f"Using browser: {browser}")
    print("Generating PDFs...")

    # Press kit first — self-contained, always produced.
    ok = emit(presskit_html(), "Unity-UI-Extensions-PressKit.pdf", browser)
    if only_presskit:
        print("Done (press kit only).")
        sys.exit(0 if ok else 1)

    ugui = get_controls(os.path.join(CONTROLS_DIR, "*.md"))
    print(f"  uGUI controls parsed: {len(ugui)}")
    emit(reference_html(ugui, "Unity UI Extensions",
                        MAG, "uGUI package — control reference", total_in_pack=UGUI_CONTROLS),
         "Unity-UI-Extensions-uGUI-Documentation.pdf", browser)

    uitk = get_controls(os.path.join(UITK_DIR, "*", "index.md"))
    print(f"  UI Toolkit controls parsed: {len(uitk)}")
    emit(reference_html(uitk, "Unity UI Toolkit Extensions",
                        CYAN, "UI Toolkit package — complete control reference"),
         "Unity-UI-Extensions-UIToolkit-Documentation.pdf", browser)

    print("Done.")
