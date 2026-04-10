# Swiss Design System, PPTX Implementation

This document maps the design principles (see PRINCIPLES.md) to slide generation using Python's python-pptx library.

## Technology

Use `python-pptx` with blank slide layouts. Do not rely on PowerPoint templates or built-in themes, they conflict with the Swiss grid. Build every element from positioned text boxes and shapes, exactly like the PDF canvas approach.

## Slide dimensions

Widescreen 16:9, which is the default in python-pptx:

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu

prs = Presentation()
# Default: 13.333" x 7.5" (16:9)
SLIDE_W = prs.slide_width   # 12192000 EMU
SLIDE_H = prs.slide_height  #  6858000 EMU
```

## Grid mapping

The A4 grid (PRINCIPLES.md) maps to slides as follows:

```python
MARGIN    = Inches(0.6)           # ~5% of width (approx. 28mm equiv)
LEFT      = MARGIN
RIGHT     = SLIDE_W - MARGIN
TOP       = MARGIN
BOTTOM    = SLIDE_H - MARGIN
COL_W     = RIGHT - LEFT
NUM_COL   = Inches(1.2)          # left column for section numbers
TEXT_LEFT = LEFT + NUM_COL + Inches(0.15)
TEXT_W    = RIGHT - TEXT_LEFT
```

## Type scale (absolute, for projection)

Base unit is ~18pt (body text readable at projection distance).

| Element           | Font            | Size  | Color  |
|-------------------|-----------------|-------|--------|
| Cover title       | Liberation Sans Bold | 54pt  | BLACK  |
| Section number    | Liberation Sans Bold | 48pt  | ACCENT |
| Section title     | Liberation Sans Bold | 32pt  | BLACK  |
| Sub-heading       | Liberation Sans Bold | 24pt  | DARK   |
| Body              | Liberation Sans      | 18pt  | BODY   |
| Box label         | Liberation Sans Bold | 16pt  | DARK   |
| Box body          | Liberation Sans      | 16pt  | BODY   |
| Slide number      | Liberation Sans      | 12pt  | MUTED  |
| Caption / note    | Liberation Sans      | 14pt  | MUTED  |

## Slide types

### Title slide (slide 1)

Background white. Top accent bar, full-width rectangle at height ~0.08", ACCENT color. Title at 54pt bold, flush-left at LEFT, vertically centered upper-third. Subtitle at 20pt bold, MUTED, below a light rule. Author at 18pt regular, MUTED, below subtitle. Logo bottom-right, ~1" square, with transparency. Slide number bottom-right, small.

### Section slide

Running header in top margin zone, 10pt, LIGHT, document title left and subtitle right. Section number at 48pt bold, ACCENT, in left column. Section title at 32pt bold, BLACK, in main column. The number and title share the same perceived baseline (apply a descent offset to the number so it sits optically level with the title's x-height, not its ascender). Body text at 18pt regular, flush-left in main column. Slide number bottom-right.

### Content slide

Like section slide but without the large section number. Used for continuation within a section.

### Tip / Warning slide

Content slide with a callout box: full-width rectangle (within margins) with TIP_BG or WARN_BG fill, no border. Label text (bold) and body text (regular) aligned with the main column TEXT_LEFT. Box background extends 0.15" beyond text bounds on each side.

### Closing slide

Light rule across full column width. Italic message, 18pt, BODY. Contact info, 14pt, MUTED. Logo bottom-right if provided.

## One idea per slide

This is the most important mapping from Swiss PDF to Swiss PPTX. Each slide carries one thought: one section header with one short body paragraph, or one callout, or one numbered list. Never stack multiple sections on a single slide. The whitespace that remains is not waste, it is the design.

## Font handling

python-pptx does not register fonts like reportlab. It writes font names into the XML; PowerPoint resolves them at render time. Use "Liberation Sans" as the font family name. If the font is not installed on the viewer's machine, PowerPoint falls back to its default sans-serif (Calibri on Windows, Helvetica on macOS), which is acceptable.

```python
from pptx.util import Pt
from pptx.dml.color import RGBColor

def set_font(run, size, bold=False, italic=False, color_hex="#333333"):
    run.font.name = "Liberation Sans"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color_hex[1:])  # strip #
```

## Reference implementation

`scripts/swiss_pptx.py` contains the `SwissPPTX` class. It mirrors the SwissPDF API as closely as possible:

```python
from swiss_pptx import SwissPPTX

deck = SwissPPTX("output.pptx", title="My Deck", subtitle="March 2026", author="Name")
deck.title_slide(description="Optional short description.")
deck.section_slide(1, "Section Title", body="Body text for this section.")
deck.content_slide("More detail here.", tip=("Tip label", "Tip body."))
deck.closing_slide("Contact message.", "email@example.com")
deck.save()
```

## Workflow

1. Read `scripts/swiss_pptx.py`
2. Plan slide sequence: title, section slides, content slides, closing
3. Write a build script that uses SwissPPTX
4. Generate the .pptx
5. Open in a viewer or convert to images for QA
6. Fix and regenerate

## QA checklist

- All text within margins (0.6" on all sides)
- Title slide has accent bar, oversize title, rule, subtitle
- Section numbers optically aligned with titles (descent offset applied)
- One idea per slide, no slide has more than one section
- Callout boxes: background fill, no border, text aligned with body
- Slide numbers on every slide
- Font is Liberation Sans (or acceptable fallback)
- Generous whitespace, slides should feel airy, not packed
