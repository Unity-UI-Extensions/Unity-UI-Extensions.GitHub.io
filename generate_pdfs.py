#!/usr/bin/env python3
"""
generate_pdfs.py — Build package documentation PDFs.

Produces:
  Unity-UI-Extensions-uGUI-Documentation.pdf
  Unity-UI-Extensions-UIToolkit-Documentation.pdf

Usage:
  python generate_pdfs.py

Requires: fpdf2, markdown  (pip install fpdf2 markdown)
"""

import os
import re
import glob
import datetime
import html as html_lib
import markdown
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ── Paths ─────────────────────────────────────────────────────────────────────

BASE         = os.path.dirname(os.path.abspath(__file__))
CONTROLS_DIR = os.path.join(BASE, "Controls")
UITK_DIR     = os.path.join(BASE, "uitoolkit", "controls")
MISSING      = os.path.join(BASE, "MISSING_CONTENT.md")
DOWNLOADS    = os.path.join(BASE, "assets", "downloads")
os.makedirs(DOWNLOADS, exist_ok=True)

VERSION_DATE = datetime.date.today().strftime("%B %Y")

# ── Colours ───────────────────────────────────────────────────────────────────

UGUI_ACCENT  = (255, 0, 153)   # #ff0099
UITK_ACCENT  = (0, 200, 160)   # #00c8a0
TEXT_DARK    = (26, 26, 46)    # #1a1a2e
TEXT_MUTED   = (120, 120, 120)
BG_CODE      = (244, 244, 248)
BG_TABLE_HDR = None            # set per PDF
WHITE        = (255, 255, 255)
RULE_GREY    = (220, 220, 220)

MARGIN = 18
PAGE_W = 210 - MARGIN * 2   # usable mm on A4

# ── Front-matter helpers ───────────────────────────────────────────────────────

FM_RE     = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
LIQUID_RE = re.compile(r"\{[{%].*?[}%]\}", re.DOTALL)
FENCE_RE  = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
HEADER_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
TABLE_RE  = re.compile(r"(\|[^\n]+\|\n)+", re.MULTILINE)


def strip_front_matter(text):
    return FM_RE.sub("", text, count=1).lstrip()


def strip_liquid(text):
    return LIQUID_RE.sub("", text)


def fm_field(text, field):
    m = re.search(rf'^{field}:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


# ── Markdown → structured blocks ──────────────────────────────────────────────
# We parse Markdown into simple blocks the FPDF renderer can handle cleanly.

def parse_blocks(md_text):
    """Return list of (type, content) tuples from Markdown source."""
    text = strip_liquid(md_text)
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append(("code", "\n".join(code_lines)))

        # Heading
        elif line.startswith("#"):
            m = re.match(r"^(#{1,6})\s+(.+)$", line)
            if m:
                level = len(m.group(1))
                blocks.append((f"h{level}", m.group(2).strip()))

        # Table — collect while rows look like | ... |
        elif "|" in line and line.strip().startswith("|"):
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            # filter separator rows (|---|---| etc.)
            data = [r for r in rows if not re.match(r"^\s*\|[\s\-|:]+\|\s*$", r)]
            parsed = []
            for r in data:
                cells = [c.strip() for c in r.strip("|").split("|")]
                parsed.append(cells)
            blocks.append(("table", parsed))
            continue

        # Blank line — paragraph break
        elif line.strip() == "":
            pass

        # List item
        elif re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*+]\s+", "", lines[i]))
                i += 1
            blocks.append(("ul", items))
            continue

        # Ordered list
        elif re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            blocks.append(("ol", items))
            continue

        # Image — skip (PDFs are text reference; images need file paths)
        elif re.match(r"^!\[", line):
            pass  # omit broken local image refs

        # Normal paragraph text
        else:
            para_lines = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") \
                    and not lines[i].startswith("```") and "|" not in lines[i] \
                    and not re.match(r"^\s*[-*+\d]", lines[i]):
                para_lines.append(lines[i])
                i += 1
            text_block = " ".join(para_lines).strip()
            if text_block:
                blocks.append(("p", text_block))
            continue

        i += 1

    return blocks


_UNICODE_MAP = {
    "\u2014": "--",   # em dash
    "\u2013": "-",    # en dash
    "\u2018": "'", "\u2019": "'",   # smart quotes
    "\u201c": '"', "\u201d": '"',
    "\u2022": "-",    # bullet
    "\u2026": "...",  # ellipsis
    "\u00b7": ".",    # middle dot
    "\u2192": "->",   # arrow
    "\u2190": "<-",
    "\u00a0": " ",    # non-breaking space
}


def to_latin1(text: str) -> str:
    """Replace common unicode chars with ASCII equivalents; drop the rest."""
    for char, repl in _UNICODE_MAP.items():
        text = text.replace(char, repl)
    return text.encode("latin-1", errors="replace").decode("latin-1")


def inline_clean(text):
    """Strip inline Markdown formatting for plain text output."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    return to_latin1(text.strip())


# ── PDF class ─────────────────────────────────────────────────────────────────

class DocPDF(FPDF):
    def __init__(self, title, accent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doc_title = title
        self.accent = accent           # (R, G, B)
        self.set_margins(MARGIN, 16, MARGIN)
        self.set_auto_page_break(auto=True, margin=14)

    # ── Header / Footer ───────────────────────────────────────────────────────

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*TEXT_MUTED)
        self.cell(0, 6, to_latin1(self.doc_title), align="L",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*RULE_GREY)
        self.line(MARGIN, self.get_y(), 210 - MARGIN, self.get_y())
        self.ln(2)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*TEXT_MUTED)
        self.cell(0, 6, f"Page {self.page_no()}", align="C")

    # ── Cover page ────────────────────────────────────────────────────────────

    def cover(self, package_name, subtitle):
        self.add_page()
        self.ln(50)
        # coloured banner
        r, g, b = self.accent
        self.set_fill_color(r, g, b)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 34)
        self.cell(0, 20, "  U  ", align="C", fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)
        self.set_text_color(*TEXT_DARK)
        self.set_font("Helvetica", "B", 20)
        self.cell(0, 10, to_latin1(package_name), align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(*TEXT_MUTED)
        self.cell(0, 8, to_latin1(subtitle), align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(20)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 6, to_latin1(f"Generated {VERSION_DATE}  -  BSD 3-Clause Licensed  -  Not affiliated with Unity Technologies"),
                  align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ── Section heading ───────────────────────────────────────────────────────

    def section_heading(self, text):
        self.add_page()
        self.ln(4)
        r, g, b = self.accent
        self.set_fill_color(r, g, b)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, to_latin1(f"  {text}"), fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*TEXT_DARK)
        self.ln(4)

    # ── Control title ─────────────────────────────────────────────────────────

    def control_title(self, name, category, description):
        self.ln(4)
        r, g, b = self.accent
        self.set_draw_color(r, g, b)
        self.set_line_width(0.8)
        self.line(MARGIN, self.get_y(), MARGIN + 60, self.get_y())
        self.set_line_width(0.2)
        self.ln(2)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*TEXT_DARK)
        self.cell(0, 7, to_latin1(name), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(*TEXT_MUTED)
        self.cell(0, 5, to_latin1(f"{category}  -  {description}"),
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*TEXT_DARK)
        self.ln(2)

    # ── Render blocks ─────────────────────────────────────────────────────────

    def render_blocks(self, blocks):
        for btype, content in blocks:
            if btype == "h2":
                self.ln(3)
                r, g, b = self.accent
                self.set_text_color(r, g, b)
                self.set_font("Helvetica", "B", 11)
                self.multi_cell(0, 6, inline_clean(content),
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.set_text_color(*TEXT_DARK)
            elif btype == "h3":
                self.ln(2)
                self.set_font("Helvetica", "B", 10)
                self.multi_cell(0, 6, inline_clean(content),
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            elif btype in ("h4", "h5", "h6"):
                self.ln(1)
                self.set_font("Helvetica", "BI", 9.5)
                self.multi_cell(0, 5, inline_clean(content),
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            elif btype == "p":
                self.set_font("Helvetica", "", 10)
                self.multi_cell(0, 5.5, inline_clean(content),
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.ln(1)
            elif btype == "code":
                self.set_fill_color(*BG_CODE)
                self.set_font("Courier", "", 8)
                lines = content.split("\n")
                for ln in lines:
                    ln = to_latin1(ln)
                    while len(ln) > 95:
                        self.cell(0, 4.5, ln[:95], fill=True,
                                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                        ln = "  " + ln[95:]
                    self.cell(0, 4.5, ln, fill=True,
                              new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.set_fill_color(*WHITE)
                self.ln(2)
            elif btype == "ul":
                self.set_font("Helvetica", "", 9.5)
                for item in content:
                    self.cell(6, 5.5, chr(149), new_x=XPos.RIGHT, new_y=YPos.TOP)
                    self.multi_cell(0, 5.5, inline_clean(item),
                                    new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.ln(1)
            elif btype == "ol":
                self.set_font("Helvetica", "", 9.5)
                for n, item in enumerate(content, 1):
                    self.cell(7, 5.5, f"{n}.", new_x=XPos.RIGHT, new_y=YPos.TOP)
                    self.multi_cell(0, 5.5, inline_clean(item),
                                    new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.ln(1)
            elif btype == "table":
                self._render_table(content)

    def _render_table(self, rows):
        if not rows:
            return
        r, g, b = self.accent
        col_w = PAGE_W / max(len(rows[0]), 1)
        col_w = min(col_w, 55)

        for idx, row in enumerate(rows):
            if idx == 0:
                self.set_fill_color(r, g, b)
                self.set_text_color(*WHITE)
                self.set_font("Helvetica", "B", 8.5)
            else:
                fill = idx % 2 == 0
                self.set_fill_color(245, 245, 250) if fill else self.set_fill_color(*WHITE)
                self.set_text_color(*TEXT_DARK)
                self.set_font("Helvetica", "", 8.5)
            for cell in row:
                self.cell(col_w, 5.5, inline_clean(str(cell))[:40],
                          border=1, fill=(idx == 0 or idx % 2 == 0),
                          new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.ln()

        self.set_fill_color(*WHITE)
        self.set_text_color(*TEXT_DARK)
        self.ln(2)

    # ── TOC page ──────────────────────────────────────────────────────────────

    def toc_page(self, controls, package_label):
        self.add_page()
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*TEXT_DARK)
        self.cell(0, 9, to_latin1(f"{package_label} - {len(controls)} Controls"),
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*RULE_GREY)
        self.line(MARGIN, self.get_y(), 210 - MARGIN, self.get_y())
        self.ln(3)

        cats = sorted({c["category"] for c in controls})
        for cat in cats:
            self.set_font("Helvetica", "B", 10)
            r, g, b = self.accent
            self.set_text_color(r, g, b)
            self.cell(0, 7, cat, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(*TEXT_DARK)
            self.set_font("Helvetica", "", 9.5)
            for c in controls:
                if c["category"] != cat:
                    continue
                self.cell(6, 5.5, chr(149), new_x=XPos.RIGHT, new_y=YPos.TOP)
                self.cell(0, 5.5, to_latin1(c["title"]),
                          new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(1)


# ── Control loaders ───────────────────────────────────────────────────────────

def get_ugui_controls():
    controls = []
    for path in sorted(glob.glob(os.path.join(CONTROLS_DIR, "*.md"))):
        raw = read_file(path)
        if not raw.startswith("---"):
            continue
        controls.append({
            "title":       fm_field(raw, "title") or os.path.basename(path),
            "category":    fm_field(raw, "category") or "Other",
            "description": fm_field(raw, "description") or "",
            "body":        strip_front_matter(raw),
        })
    return controls


def get_uitk_controls():
    controls = []
    for path in sorted(glob.glob(os.path.join(UITK_DIR, "*", "index.md"))):
        raw = read_file(path)
        if not raw.startswith("---"):
            continue
        controls.append({
            "title":       fm_field(raw, "title") or "",
            "category":    fm_field(raw, "category") or "Other",
            "description": fm_field(raw, "description") or "",
            "body":        strip_front_matter(raw),
        })
    return controls


# ── PDF builders ──────────────────────────────────────────────────────────────

def build_pdf(controls, package_name, subtitle, doc_title, accent, output_path):
    pdf = DocPDF(doc_title, accent, "P", "mm", "A4")
    pdf.set_author("Unity UI Extensions Community")
    pdf.set_creator("generate_pdfs.py")
    pdf.set_title(doc_title)

    pdf.cover(package_name, subtitle)
    pdf.toc_page(controls, package_name)

    cats = sorted({c["category"] for c in controls})
    for cat in cats:
        cat_controls = [c for c in controls if c["category"] == cat]
        pdf.section_heading(cat)
        for ctrl in cat_controls:
            pdf.control_title(ctrl["title"], ctrl["category"], ctrl["description"])
            blocks = parse_blocks(ctrl["body"])
            pdf.render_blocks(blocks)

    pdf.output(output_path)
    size_kb = os.path.getsize(output_path) // 1024
    print(f"  Written: {os.path.basename(output_path)}  ({size_kb} KB,  pages: {pdf.page_no()})")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating PDFs…")

    ugui = get_ugui_controls()
    print(f"  uGUI controls found: {len(ugui)}")
    build_pdf(
        controls     = ugui,
        package_name = "Unity UI Extensions",
        subtitle     = f"uGUI Package — complete control reference  •  {len(ugui)} controls",
        doc_title    = "Unity UI Extensions — uGUI Reference",
        accent       = UGUI_ACCENT,
        output_path  = os.path.join(DOWNLOADS, "Unity-UI-Extensions-uGUI-Documentation.pdf"),
    )

    uitk = get_uitk_controls()
    print(f"  UIToolkit controls found: {len(uitk)}")
    build_pdf(
        controls     = uitk,
        package_name = "Unity UI Extensions",
        subtitle     = f"UI Toolkit Package — complete control reference  •  {len(uitk)} controls",
        doc_title    = "Unity UI Extensions — UI Toolkit Reference",
        accent       = UITK_ACCENT,
        output_path  = os.path.join(DOWNLOADS, "Unity-UI-Extensions-UIToolkit-Documentation.pdf"),
    )

    print("Done.")
