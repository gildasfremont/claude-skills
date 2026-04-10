---
name: swiss-designer
description: "Generate documents in International Typographic Style (Swiss design), supports PDF and PPTX. Use this skill whenever the user asks for a document with clean, modern, editorial design: Swiss style, grotesk, Müller-Brockmann-inspired, oversize titles, grid layout, or simply a professional minimal layout. Triggers for both PDF (reportlab canvas) and slide decks (python-pptx). MANDATORY TRIGGERS: Swiss design, grotesk, typographic, editorial PDF, clean PDF layout, designed PDF, professional slides, minimal deck, editorial presentation."
---

# Swiss Designer

Generate documents in the International Typographic Style. This skill covers PDF and PPTX output, sharing a single design system across both formats.

## Architecture

The skill is split into three layers:

1. **Principles** (`docs/PRINCIPLES.md`): the design system itself, covering palette, typography scale, grid ratios, element vocabulary, spacing rules, and optical alignment. Format-agnostic. Read this first for every task.

2. **Format-specific guides**, which map the principles to a concrete rendering engine:
   - `docs/PDF.md`: reportlab canvas, A4 dimensions, absolute pt sizes. Reference: `scripts/swiss_pdf.py`
   - `docs/PPTX.md`: python-pptx, 16:9 widescreen, projection-friendly sizes. Reference: `scripts/swiss_pptx.py`

3. **Scripts**, ready-to-use Python modules:
   - `scripts/swiss_pdf.py` > `SwissPDF` class
   - `scripts/swiss_pptx.py` > `SwissPPTX` class

## When to use this skill

Whenever the user wants a document (PDF or slide deck) that looks designed rather than generated. Typical use cases: course recaps, didactic documents, one-pagers, training materials, reports, presentations with modern editorial feel.

## Routing

| User wants...              | Read in order                             | Use script     |
|----------------------------|-------------------------------------------|----------------|
| A designed PDF             | PRINCIPLES.md > PDF.md > swiss_pdf.py     | `SwissPDF`     |
| A designed slide deck      | PRINCIPLES.md > PPTX.md > swiss_pptx.py  | `SwissPPTX`    |
| Both (e.g. recap + slides) | PRINCIPLES.md > both format docs          | Both classes   |

## Quick start

### PDF
```python
from swiss_pdf import SwissPDF
pdf = SwissPDF("output.pdf", title="Document", subtitle="Date", author="Name", logo_path="logo.png")
pdf.title_page(description="A short intro.")
y = pdf.new_content_page()
y = pdf.section(1, "First Section", y)
y = pdf.body("Paragraph text.", y)
y = pdf.tip("Tip title", "Tip body.", y)
y = pdf.end_page()
pdf.save()
```

### PPTX
```python
from swiss_pptx import SwissPPTX
deck = SwissPPTX("output.pptx", title="Deck", subtitle="Date", author="Name", logo_path="logo.png")
deck.title_slide(description="A short intro.")
deck.section_slide(1, "First Section", body="Paragraph text.")
deck.tip_slide("Tip title", "Tip body.")
deck.closing_slide("Contact message.", "email@example.com")
deck.save()
```

## Assets

`assets/claude-logo.png`: Claude AI logo, 400x400 PNG with transparency. Replace with any logo relevant to the document.
