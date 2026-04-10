# Swiss Design System, PDF Implementation

This document maps the design principles (see PRINCIPLES.md) to concrete PDF generation using Python's reportlab canvas API.

## Technology

Use `reportlab.pdfgen.canvas.Canvas` directly, not Platypus flowables. The canvas API gives pixel-level control over the grid, which is essential for Swiss precision. Platypus fights you when you need exact placement.

## Absolute dimensions (A4)

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

W, H = A4  # 595.28 x 841.89 pt

LEFT      = 28 * mm
RIGHT     = W - 28 * mm
TOP       = H - 28 * mm
BOTTOM    = 28 * mm
COL_W     = RIGHT - LEFT
NUM_COL   = 26 * mm
TEXT_LEFT = LEFT + NUM_COL + 4 * mm
TEXT_W    = RIGHT - TEXT_LEFT
```

## Type scale (absolute)

| Element           | Font         | Size  | Leading |
|-------------------|-------------|-------|---------|
| Cover title       | Grotesk-Bold | 66pt  | .       |
| Section number    | Grotesk-Bold | 56pt  | .       |
| Section title     | Grotesk-Bold | 26pt  | 10mm    |
| Sub-heading       | Grotesk-Bold | 16pt  | 9mm     |
| Body              | Grotesk      | 11pt  | 17pt    |
| Box label         | Grotesk-Bold | 10.5pt| 14.5pt  |
| Box body          | Grotesk      | 10pt  | 14.5pt  |
| Footnote          | Grotesk      | 7.5pt | 10pt    |
| Running header    | Grotesk      | 7pt   | .       |
| Page number       | Grotesk      | 8pt   | .       |
| Numbered list num | Grotesk-Bold | 12pt  | .       |

## Font registration

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Grotesk', '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Grotesk-Bold', '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Grotesk-Italic', '/usr/share/fonts/truetype/liberation2/LiberationSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Grotesk-BoldItalic', '/usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf'))
```

Fallback: if Liberation Sans is not available, use "Helvetica" / "Helvetica-Bold" / "Helvetica-Oblique" (reportlab built-ins).

## Optical alignment notes (PDF-specific)

The section number (56pt bold) and section title (26pt bold) share a visual line. The number's bounding box is much taller than the title's. To make them appear aligned, the number is drawn with a downward offset (`y - 16` in the reference script). This shifts the number's optical center to match the title's x-height. Adjust this offset if the font changes.

For the cover title at 66pt, wrap_text handles line breaks, but if the first character is round or diagonal ("O", "D", "V"), consider a 1-2pt leftward nudge so the title appears flush with the margin.

## Reference implementation

`scripts/swiss_pdf.py` contains the `SwissPDF` class with all helpers. Read it and instantiate directly, or copy the relevant functions into your build script.

## Workflow

1. Read `scripts/swiss_pdf.py`
2. Plan content: sections, callouts, footnotes
3. Write a build script that uses SwissPDF
4. Generate the PDF
5. Visual QA: `pdftoppm -jpeg -r 150 output.pdf slide` then inspect images
6. Fix and regenerate

## QA checklist

- All text within 28mm margins
- Running header in margin zone, not overlapping content
- Page number on every page (bottom-right)
- Section numbers optically aligned with titles (not pixel-aligned)
- Callout boxes: background visible, no border, text aligned with body column
- No unicode rendering issues (no black boxes)
- Margin notes (left column) correspond to footnotes
- Body lines under 75 characters
- Generous whitespace, nothing cramped
