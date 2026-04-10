# Swiss Design System, Principles

This document defines the design system independently of any output format. It applies identically to PDF, PPTX, HTML, or any other medium. Format-specific implementation details live in PDF.md and PPTX.md.

## Philosophy

The International Typographic Style rests on three structural ideas: the grid as skeleton, typography as the primary visual signal, and whitespace used deliberately as a design element. Every element on the surface earns its place, nothing decorative, everything functional. Hierarchy comes from size contrast and weight, not from color or ornament.

## Palette, grayscale

The entire document uses grayscale by default. This forces the hierarchy to emerge from size, weight, and spacing rather than hue.

| Token   | Hex       | Role                                       |
|---------|-----------|---------------------------------------------|
| BLACK   | `#1A1A1A` | Titles, primary emphasis                    |
| DARK    | `#2D2D2D` | Sub-headings, box labels                    |
| BODY    | `#333333` | Running text                                |
| MUTED   | `#777777` | Secondary text, footnotes, captions         |
| LIGHT   | `#BBBBBB` | Very subtle elements (running header)       |
| ACCENT  | `#444444` | Section numbers, structural markers         |
| RULE    | `#D0D0D0` | Thin separators                             |
| TIP_BG  | `#F0F0F0` | Callout box background (tips)               |
| WARN_BG | `#E8E8E8` | Callout box background (warnings/errata)    |

If the user explicitly asks for color, replace ACCENT with one single hue and derive TIP_BG / WARN_BG as tints of that hue. Never more than one accent color.

## Typography

Use a grotesk (sans-serif neo-grotesque) typeface. The reference font is Liberation Sans (metrically identical to Helvetica, available as TTF). Four weights are required: Regular, Bold, Italic, Bold Italic.

Fallback chain: Liberation Sans > Helvetica > Arial > system sans-serif.

### Scale ratios

The design system defines a type scale by function, not by absolute point sizes (which depend on the medium). The key constraint is the contrast ratio between the largest and smallest functional elements:

| Element           | Weight    | Relative size | Color  |
|-------------------|-----------|---------------|--------|
| Cover title       | Bold      | 6x            | BLACK  |
| Section number    | Bold      | 5x            | ACCENT |
| Section title     | Bold      | 2.4x          | BLACK  |
| Sub-heading       | Bold      | 1.5x          | DARK   |
| Body              | Regular   | 1x (base)     | BODY   |
| Box label         | Bold      | 0.95x         | DARK   |
| Box body          | Regular   | 0.9x          | BODY   |
| Footnote / caption| Regular   | 0.7x          | MUTED  |
| Running header    | Regular   | 0.6x          | LIGHT  |
| Page / slide num  | Regular   | 0.7x          | MUTED  |

The base unit depends on format: ~11pt for A4 PDF, ~18pt for 16:9 PPTX projected at 1920px.

### Weight usage

Bold is a structural signal, not emphasis. Use bold for: titles, section numbers, sub-headings, box labels, numbered list markers. Body text stays regular. If a sentence inside body text needs emphasis, use italic, not bold.

### Line length (measure)

A line of body text should contain between 45 and 75 characters, ideally around 60. This is the typographic "measure" and it controls readability more than font size does. If the available column is too wide for the body size, either increase the font size or split the column. Never let a line run beyond 80 characters; the reader's eye loses its way back to the next line.

For titles, the constraint is different: a title can span the full width because the reader processes it as a single visual block, not as running text.

### Paragraph density

Keep body paragraphs short, three to five lines in PDF, two to three lines on slides. Dense walls of text defeat the purpose of the design. If a paragraph needs to be longer, it probably contains two ideas and should be split.

## Grid

### Technical grid vs. aesthetic grid

The technical grid is the coordinate system: margins at fixed offsets, column boundaries at known positions, baseline increments. It is the scaffold.

The aesthetic grid is what the viewer perceives. It does not always coincide with the technical grid. A round glyph like "O" or "0" extends slightly beyond the cap height and baseline (overshoots); a section number "01" in bold at 56pt has a visual mass that sits lower than its bounding box. A callout box with a light background has a visual edge inside its fill, not at the fill boundary. The ragged right margin of a flush-left paragraph does not end at a pixel; it ends at a mean line that the eye averages over several lines.

The rule is: align on what the eye sees, not on what the coordinate system computes.

Concretely:
- When a section number and a section title sit on the same visual line, the number (which is much larger) must be shifted down from the technical baseline so that its optical center aligns with the title's x-height, not its ascender. A large bold "01" next to a smaller bold title needs a descent correction, typically 15-20% of the size difference.
- A callout box background should extend slightly beyond the text bounds (4mm or ~0.15") so the text appears to float inside it, not to touch its edges. But the text itself aligns exactly on the body column left edge, because that is what the eye tracks.
- The ragged right edge of body text can optionally exceed the technical right margin on individual lines if the mean line length stays within the column. This is a deliberate choice, not an accident.
- Flush-left titles have optical overshoot: letters like "T", "V", "W" with diagonal stems appear indented relative to straight stems like "H", "N". At very large sizes (>40pt), consider nudging the title left by 1-2pt when it starts with a diagonal or round letter.

### Proportions

Every format uses a margin-grid-column system. The proportions are:

- Margins: ~5% of the surface width on each side (approx. 28mm on A4, 0.5" on 16:9)
- Left column: ~17% of the text area width, reserved for section numbers and margin annotations
- Main column: remaining width, carries all body content
- Vertical rhythm: consistent spacing between elements, with generous gaps between sections

### Columns and breathing

The left column is not a decoration. It creates a clear gutter between the structural markers (section numbers, margin notes) and the reading flow. That gutter is part of the whitespace budget. If the content requires it (for instance a two-column layout within the main column for a comparison), use sub-columns with their own internal gutter, but never eliminate the outer margins.

Around every content block (paragraph, callout, list), there must be enough whitespace for the block to be perceived as a distinct unit. The minimum is one full line height above and below. For section transitions, double that.

## Element vocabulary

The design system defines a fixed set of content elements. Every document is composed exclusively from these:

**Structural**: title page, section header (number + title), sub-heading, page/slide break, light rule, running header, page/slide number.

**Content**: body paragraph, bold body, tip callout, warning callout, numbered list, margin note.

**Closing**: footnotes block, closing message with contact, logo placement.

Each element has a clear role and cannot be repurposed. A tip is never used for a warning; a sub-heading never replaces a section title.

## Spacing

Whitespace is not empty, it is the structure. Key rules:

- One major topic per page/slide. If two short sections share a surface, separate them with a light rule and generous spacing.
- After a section title: leave a gap before the first paragraph (~1.5x leading).
- Between paragraphs: ~0.5x leading.
- Between a paragraph and a callout box: ~1x leading.
- Inside callout boxes: the text aligns with the body column (same left edge). The background extends slightly beyond the text bounds to create visual padding without misaligning the text.
- Callout boxes have no visible border. They rely on the background fill alone for differentiation.

## Logo

If a logo is present (PNG, transparency preserved), it sits in the bottom-right of the title page at ~5% of the surface width. It can optionally repeat smaller on the closing page. The logo should never dominate.

## What to avoid

- Color (unless explicitly requested).
- Em dashes. Use commas, colons, or sentence restructuring instead.
- Centered text (everything flush-left, except page numbers which are right-aligned).
- Decorative elements: no borders, shadows, gradients, rounded corners.
- Multiple fonts: one typeface, four weights.
- Tight spacing: when in doubt, add more whitespace.
- Unicode superscripts (U+2074, U+2075, etc.): rendering is unreliable across engines. Use margin notes or explicit callouts instead.
- Lines longer than 75 characters in body text. Shorten the column or increase the font size.
