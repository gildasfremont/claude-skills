#!/usr/bin/env python3
"""
Swiss PDF: helper library for International Typographic Style PDFs.

Usage:
    from swiss_pdf import SwissPDF

    pdf = SwissPDF("output.pdf", title="My Document", subtitle="A subtitle", author="Name")
    pdf.title_page(description="A short description of this document.")

    y = pdf.new_content_page()
    y = pdf.section(1, "Section Title", y)
    y = pdf.body("Body text here.", y)
    y = pdf.tip("Tip label", "Tip body text.", y)
    y = pdf.margin_note(1, y)
    y = pdf.light_rule(y)
    y = pdf.warn_box("Warning label", "Warning text.", y)

    pdf.footnotes_section([
        ("1", "First footnote text."),
        ("2", "Second footnote text."),
    ], y)

    pdf.closing("Contact line or sign-off.", "email@example.com", y_after_footnotes)
    pdf.save()
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

W, H = A4

# Try to register Liberation Sans; fall back to Helvetica
_FONT_REGISTERED = False
try:
    pdfmetrics.registerFont(TTFont('Grotesk', '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Grotesk-Bold', '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Grotesk-Italic', '/usr/share/fonts/truetype/liberation2/LiberationSans-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Grotesk-BoldItalic', '/usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf'))
    _FONT_REGISTERED = True
except Exception:
    pass

FONT = "Grotesk" if _FONT_REGISTERED else "Helvetica"
FONT_BOLD = "Grotesk-Bold" if _FONT_REGISTERED else "Helvetica-Bold"
FONT_ITALIC = "Grotesk-Italic" if _FONT_REGISTERED else "Helvetica-Oblique"
FONT_BOLD_ITALIC = "Grotesk-BoldItalic" if _FONT_REGISTERED else "Helvetica-BoldOblique"

#Colors (grayscale)BLACK   = HexColor("#1A1A1A")
DARK    = HexColor("#2D2D2D")
BODY    = HexColor("#333333")
MUTED   = HexColor("#777777")
LIGHT   = HexColor("#BBBBBB")
ACCENT  = HexColor("#444444")
RULE    = HexColor("#D0D0D0")
TIP_BG  = HexColor("#F0F0F0")
WARN_BG = HexColor("#E8E8E8")

#GridLEFT      = 28 * mm
RIGHT     = W - 28 * mm
TOP       = H - 28 * mm
BOTTOM    = 28 * mm
COL_W     = RIGHT - LEFT
NUM_COL   = 26 * mm
TEXT_LEFT = LEFT + NUM_COL + 4 * mm
TEXT_W    = RIGHT - TEXT_LEFT


def wrap_text(text, font, size, max_width):
    """Word-wrap text to fit within max_width. Returns list of strings."""
    lines = []
    for paragraph in text.split('\n'):
        if not paragraph.strip():
            lines.append('')
            continue
        words = paragraph.split()
        current_line = ''
        for word in words:
            test = current_line + (' ' if current_line else '') + word
            tw = pdfmetrics.stringWidth(test, font, size)
            if tw > max_width and current_line:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test
        if current_line:
            lines.append(current_line)
    return lines


class SwissPDF:
    """High-level API for building Swiss-style PDFs."""

    def __init__(self, outpath, title="Document", subtitle="", author="",
                 logo_path=None):
        self.outpath = outpath
        self.title_text = title
        self.subtitle_text = subtitle
        self.author = author
        self.logo_path = logo_path
        self.c = canvas.Canvas(outpath, pagesize=A4)
        self.c.setTitle(title)
        if author:
            self.c.setAuthor(author)
        self.page_num = 0

    #Low-level drawing
    def _draw_page_number(self):
        self.c.setFont(FONT, 8)
        self.c.setFillColor(MUTED)
        self.c.drawRightString(RIGHT, BOTTOM - 12 * mm, str(self.page_num))

    def _draw_running_header(self):
        self.c.setFont(FONT, 7)
        self.c.setFillColor(LIGHT)
        self.c.drawString(LEFT, TOP + 10 * mm, self.title_text)
        if self.subtitle_text:
            self.c.drawRightString(RIGHT, TOP + 10 * mm, self.subtitle_text)

    #Page management
    def title_page(self, description="", logo_path=None):
        """Draw the title/cover page. Call this first."""
        self.page_num = 1
        c = self.c
        lp = logo_path or self.logo_path

        # Top accent bar
        c.setFillColor(ACCENT)
        c.rect(0, H - 5, W, 5, stroke=0, fill=1)

        y = TOP - 20 * mm

        # Oversize title, wrap to fit within margins
        c.setFont(FONT_BOLD, 66)
        c.setFillColor(BLACK)
        title_lines = wrap_text(self.title_text, FONT_BOLD, 66, COL_W)
        for tl in title_lines:
            c.drawString(LEFT, y, tl)
            y -= 22 * mm
        c.setStrokeColor(RULE)
        c.setLineWidth(0.3)
        c.line(LEFT, y, RIGHT, y)
        y -= 10 * mm

        if self.subtitle_text:
            c.setFont(FONT_BOLD, 16)
            c.setFillColor(MUTED)
            c.drawString(LEFT, y, self.subtitle_text)
            y -= 9 * mm

        if self.author:
            c.setFont(FONT, 13)
            c.setFillColor(MUTED)
            c.drawString(LEFT, y, self.author)
            y -= 25 * mm

        if description:
            self.body(description, y, x=LEFT, w=COL_W, color=MUTED)

        # Logo bottom-right
        if lp and os.path.exists(lp):
            logo_size = 28 * mm
            c.drawImage(lp, RIGHT - logo_size, BOTTOM - 5 * mm,
                        width=logo_size, height=logo_size,
                        preserveAspectRatio=True, mask='auto')

        # Author footer
        if self.author:
            c.setFont(FONT, 8)
            c.setFillColor(LIGHT)
            c.drawString(LEFT, BOTTOM - 5 * mm, self.author)

        self._draw_page_number()
        c.showPage()

    def new_content_page(self):
        """Start a new content page with running header. Returns y cursor."""
        self.page_num += 1
        self._draw_running_header()
        return TOP - 5 * mm

    def end_page(self):
        """Finalize current page (page number) and start a new one."""
        self._draw_page_number()
        self.c.showPage()
        return self.new_content_page()

    #Content elements
    def section(self, num, title, y):
        """Draw section number + title. Returns y after title."""
        c = self.c
        # Number in left column
        c.setFont(FONT_BOLD, 56)
        c.setFillColor(ACCENT)
        c.drawString(LEFT, y - 16, f"{num:02d}")
        # Title in main column
        c.setFont(FONT_BOLD, 26)
        c.setFillColor(BLACK)
        lines = wrap_text(title, FONT_BOLD, 26, TEXT_W)
        for line in lines:
            c.drawString(TEXT_LEFT, y, line)
            y -= 10 * mm
        return y - 3 * mm

    def sub_heading(self, text, y):
        """Draw a sub-heading at 16pt bold."""
        self.c.setFont(FONT_BOLD, 16)
        self.c.setFillColor(DARK)
        self.c.drawString(TEXT_LEFT, y, text)
        return y - 9 * mm

    def body(self, text, y, font=None, size=11, leading=17, color=None,
             x=None, w=None):
        """Draw wrapped body text. Returns y after text."""
        f = font or FONT
        col = color or BODY
        _x = x if x is not None else TEXT_LEFT
        _w = w if w is not None else TEXT_W
        self.c.setFont(f, size)
        self.c.setFillColor(col)
        lines = wrap_text(text, f, size, _w)
        for line in lines:
            if y < BOTTOM + 5 * mm:
                return y
            self.c.drawString(_x, y, line)
            y -= leading
        return y

    def body_bold(self, text, y, **kwargs):
        """Draw bold body text."""
        return self.body(text, y, font=FONT_BOLD, **kwargs)

    def tip(self, label, text, y, x=None, w=None):
        """Draw a tip callout box with left accent border."""
        return self._draw_box(label, text, y, TIP_BG, ACCENT, x, w)

    def warn_box(self, label, text, y, x=None, w=None):
        """Draw a warning/correction box with left black border."""
        return self._draw_box(label, text, y, WARN_BG, BLACK, x, w)

    def _draw_box(self, label, text, y, bg_color, border_color, x=None, w=None):
        _x = x if x is not None else TEXT_LEFT
        _w = w if w is not None else TEXT_W
        c = self.c

        pad_x = 4 * mm   # horizontal padding around text
        pad_y = 4 * mm   # vertical padding top & bottom

        lines_label = wrap_text(label, FONT_BOLD, 10.5, _w)
        lines_text = wrap_text(text, FONT, 10, _w)
        content_h = (len(lines_label) + len(lines_text)) * 14.5 + 2 * mm
        box_h = content_h + 2 * pad_y

        # Background extends slightly beyond text column
        box_x = _x - pad_x
        box_w = _w + 2 * pad_x
        c.setFillColor(bg_color)
        c.rect(box_x, y - box_h + pad_y, box_w, box_h, stroke=0, fill=1)

        # Text aligned with body paragraphs (TEXT_LEFT)
        cy = y - 1 * mm
        c.setFont(FONT_BOLD, 10.5)
        c.setFillColor(DARK)
        for line in lines_label:
            c.drawString(_x, cy, line)
            cy -= 14.5
        cy -= 1.5 * mm
        c.setFont(FONT, 10)
        c.setFillColor(BODY)
        for line in lines_text:
            c.drawString(_x, cy, line)
            cy -= 14.5

        return y - box_h - 2 * mm

    def margin_note(self, num, y):
        """Draw a small footnote reference number in the left margin."""
        self.c.setFont(FONT_BOLD, 7.5)
        self.c.setFillColor(ACCENT)
        self.c.drawString(LEFT, y + 16, str(num))
        return y

    def light_rule(self, y):
        """Draw a light horizontal separator."""
        self.c.setStrokeColor(RULE)
        self.c.setLineWidth(0.3)
        self.c.line(LEFT, y, RIGHT, y)
        return y

    def section_break(self, y, gap_before=12, gap_after=10):
        """Light rule with spacing, for separating sections on the same page."""
        y -= gap_before * mm
        self.light_rule(y)
        return y - gap_after * mm

    def numbered_list(self, items, y):
        """Draw a numbered list of items."""
        for i, item in enumerate(items):
            self.c.setFont(FONT_BOLD, 12)
            self.c.setFillColor(ACCENT)
            self.c.drawString(TEXT_LEFT, y, str(i + 1))
            y = self.body(item, y, x=TEXT_LEFT + 7 * mm, w=TEXT_W - 7 * mm)
            y -= 3.5 * mm
        return y

    def footnotes_section(self, footnotes, y):
        """
        Draw the footnotes block.
        footnotes: list of (number_str, text) tuples.
        Returns y after all footnotes.
        """
        c = self.c
        y -= 12 * mm
        c.setStrokeColor(BLACK)
        c.setLineWidth(0.6)
        c.line(LEFT, y, LEFT + 35 * mm, y)
        y -= 7 * mm

        c.setFont(FONT_BOLD, 8)
        c.setFillColor(MUTED)
        c.drawString(LEFT, y, "Notes")
        y -= 7 * mm

        for num, text in footnotes:
            c.setFont(FONT_BOLD, 7.5)
            c.setFillColor(ACCENT)
            c.drawString(LEFT, y, num)
            c.setFont(FONT, 7.5)
            c.setFillColor(MUTED)
            lines = wrap_text(text, FONT, 7.5, COL_W - 6 * mm)
            for line in lines:
                c.drawString(LEFT + 5 * mm, y, line)
                y -= 10
            y -= 3 * mm

        return y

    def closing(self, message, contact, y):
        """Draw the closing italic message and contact info."""
        c = self.c
        y -= 8 * mm
        self.light_rule(y)
        y -= 8 * mm

        c.setFont(FONT_ITALIC, 10.5)
        c.setFillColor(BODY)
        lines = wrap_text(message, FONT_ITALIC, 10.5, COL_W)
        for line in lines:
            c.drawString(LEFT, y, line)
            y -= 16

        y -= 5 * mm
        c.setFont(FONT, 9)
        c.setFillColor(MUTED)
        c.drawString(LEFT, y, contact)

        return y

    def add_logo(self, logo_path, size_mm=18):
        """Add logo to bottom-right of current page."""
        if logo_path and os.path.exists(logo_path):
            s = size_mm * mm
            self.c.drawImage(logo_path, RIGHT - s, BOTTOM - 5 * mm,
                             width=s, height=s,
                             preserveAspectRatio=True, mask='auto')

    def save(self):
        """Finalize and write the PDF."""
        self._draw_page_number()
        self.c.save()
        print(f"OK: {self.outpath}")


#Standalone helpers for direct canvas usage
def sp(mm_val):
    """Spacer: returns mm value for use in y calculations."""
    return mm_val * mm
