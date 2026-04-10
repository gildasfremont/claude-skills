---
name: grid-systems
description: >
  Apply Müller-Brockmann's grid system methodology to design documents, layouts, presentations,
  and visual communication artifacts. Use this skill whenever the user asks to design a document,
  layout a page, structure a report, create a magazine/brochure/catalogue grid, set up a
  presentation template, or organize text and images systematically. Also trigger for exhibition
  panels, corporate identity systems, or any task requiring consistent visual organization.
  The skill produces concrete, measurable grid specifications — column counts, field counts,
  typographic measurements, gutter widths — not vague aesthetic advice.
  Also use when the user asks to build a website layout, HTML/CSS grid, responsive design,
  or mentions the Raster CSS framework (rsms.me/raster). The skill covers both print grid
  theory (Müller-Brockmann) and its direct CSS implementation via Raster.
---

# Grid Systems in Graphic Design
*Based on Josef Müller-Brockmann, "Grid Systems in Graphic Design / Rastersysteme für die visuelle Gestaltung", Niggli, 1961.*

## Design philosophy

The grid is an ordering system, not a stylistic option. It expresses a constructivist approach: work must be clear, objective, functional and aesthetic — a contribution to culture, not decoration. Working with a grid means submitting to laws of universal validity. It implies: will to systematize, to clarify, to concentrate on essentials, to objectify rather than subjectify, to rationalize creative and technical production, to integrate form/color/material, to achieve architectural dominion over surface and space.

The result is measurable: information presented with clear, logically grouped titles, subtitles, texts, illustrations and captions is read faster, understood better, and retained in memory longer. This is empirically established.

## Typographic measurement system

All grid dimensions derive from typographic units, not metric or imperial.

| Unit | Metric equivalent |
|------|------------------|
| 1 point | 0.376 mm |
| 1 cicero | 12 points = 4.51 mm |
| 1 cm | ~2.66 ciceros |
| 1 m | 2660 points = 221⅔ ciceros |

**Consequences:** grid field heights must align to multiples of the leading (line-height). If running text is set at 10pt with 2pt leading (12pt leading total = 1 cicero), every field height must be a multiple of 1 cicero. Misalignment between grid and leading destroys the system.

**Type size selection by column width:** narrower column → smaller type. A column too narrow forces a typeface so small it becomes unreadable; too wide and the eye fatigues scanning across lines. As a rule, 7–10 words per line is optimal for body text.

## Grid construction sequence

**Step 1 — Study the problem.** Before sketching: clarify format, quantity of text vs. images, typeface, printing method, paper quality. These constrain the grid.

**Step 2 — Small sketches at final proportions.** Work at ~1:4 or 1:5 scale. Sketches must respect the final format ratio or problems multiply when going to full size.

**Step 3 — Choose column count.**

| Columns | Characteristics |
|---------|----------------|
| 1 | Text only; no image flexibility |
| 2 | Text in col 1, images in col 2; or both stacked; 2 cols → 4 by horizontal subdivision |
| 3 | More image variety; can subdivide to 6 |
| 4 | Ideal for image-heavy or statistics-heavy work; subdivides to 8, 16+ |

3 or 6-column layouts risk narrow columns requiring small type — evaluate against function.

**Step 4 — Determine type size and leading.** The leading value becomes the vertical module of the entire grid. Every field height, every gutter, every margin is a multiple of this value.

**Step 5 — Divide the type area into fields (rows).** A type area of 53 lines can divide into:
- 9 fields of 5 lines + 1 blank line between each field
- 6 fields of 8 lines + 1 blank line
- 4 fields of 11 lines + 1 blank line
- etc.

Fields must be separated by 1, 2, or more blank lines so that (a) images don't touch, and (b) captions fit below images.

**Step 6 — Set gutter widths (horizontal).** The gutter between columns equals the type size of the running text, plus the illustration gap. Typical: 1–2 ciceros for tight work, up to 3–4 for more open layouts.

**Step 7 — Draw the final grid in points/ciceros.** Annotate every column width, gutter, field height, and margin in typographic units. This is the production-ready specification.

## Field count and image sizing

The total number of fields = columns × rows. Common configurations:

| Total fields | Typical use |
|-------------|-------------|
| 4 (2×2) | Simple newsletter, exhibition panel |
| 6 (2×3 or 3×2) | Book, monograph |
| 8 (2×4 or 4×2) | Catalogue with mixed text/image |
| 9 (3×3) | Dense editorial |
| 12 (3×4 or 4×3) | Architectural/technical periodical (e.g., Casabella) |
| 18 (3×6) | Complex magazine |
| 65 (13×5) | High-flexibility periodical with constantly varying content (e.g., CCA Today) |

**Rule:** all illustrations are sized to 1, 2, 3 or N whole fields. Never crop to arbitrary sizes. Fewer distinct image sizes → quieter, more coherent design. The smallest illustration = 1 field; larger images span multiple contiguous fields.

## Case studies (from the book)

**Casabella (architectural periodical)**
- Format: 31 × 24.5 cm, upright
- Grid: 12 fields (3 cols × 4 rows), subdivided to 18 when needed (6 rows instead of 4)
- Text and images aligned; 2 blank lines between image and text
- Titles, text, captions in 3 type sizes only

**CCA Today (USA, general-interest magazine)**
- Format: 43.1 × 28 cm, upright
- Grid: 65 fields
- Risk identified by Müller-Brockmann: 65 fields risks obscuring clarity if the designer abuses flexibility; discipline remains required

**"Sport" exhibition (3D panels)**
- Panels of uniform size
- 4-field grid per panel
- Simple and extremely effective: viewer attention on content, not decoration

## Grid and corporate identity

The grid system extends to all visual media of a firm: visiting card to exhibition stand, all printed forms, advertising matter, vehicles, name-plates, building lettering. Uniform paper sizes (DIN A-series) are part of this system — DIN-standardized formats are stocked by printers, fit envelopes, file in folders, and scale by factor 2 between sizes.

## Historical grounding

The mathematical ordering of visual space is not a 20th-century invention. Renaissance painters (Mantegna, Raphael, Piero della Francesca, Leonardo, Dürer) worked with strict proportional rules derived from the Golden Section. Mondrian's "Broadway Boogie-Woogie" (1942) has a documented proportion diagram showing the grid underlying its composition. The Swiss constructivist approach connects directly to this tradition.

## Failure modes

- **Grid not derived from leading:** fields that don't align to text lines create misregistration; text and image edges don't coincide.
- **Too many image sizes:** defeats the unifying function of the grid; creates visual noise.
- **Column count chosen aesthetically:** should be determined by content volume and image-to-text ratio, not by what looks balanced.
- **Gutter too narrow:** images touch; captions can't be placed; illusion of order collapses.
- **Sketches not at final proportions:** problems discovered only at full scale, when reverting is costly.
- **Excessive field count without discipline:** a 65-field grid with arbitrary image placement is worse than a 4-field grid used rigorously.

## Applying this skill

When asked to design or specify a layout, output:
1. Format (width × height in mm or cm)
2. Column count and rationale
3. Type size and leading (in points), with derived cicero module
4. Number of rows/fields and their height in lines of text
5. Gutter widths (horizontal and vertical) in ciceros
6. Total field count
7. Image sizing rule for this grid
8. Any DIN paper size considerations

---

## Raster — CSS implementation of grid systems

*Source: rsms.me/raster — pure CSS, no JavaScript, open source (GitHub: rsms/raster)*

Raster is the direct translation of Müller-Brockmann's grid logic into HTML/CSS. It uses custom HTML elements (`<r-grid>`, `<r-cell>`) rather than utility classes, which keeps the structure descriptive and readable. The underlying principle is identical: a fixed column count, cells that span explicit ranges, and a typographic baseline that governs all vertical spacing.

### Core syntax

```html
<!-- Define a grid with N columns -->
<r-grid columns=8>
  <r-cell></r-cell>           <!-- next available col, span 1 -->
  <r-cell span=3></r-cell>    <!-- next col, span 3 -->
  <r-cell span=2-5></r-cell>  <!-- col 2 to col 5 -->
  <r-cell span=6..></r-cell>  <!-- col 6 to end of row -->
  <r-cell span=2+3></r-cell>  <!-- col 2, span 3 cols -->
  <r-cell span=row></r-cell>  <!-- full row -->
</r-grid>
```

### span= syntax reference

| Value | Meaning |
|-------|---------|
| `2-5` | start col 2, end col 5 |
| `2+3` | start col 2, span 3 columns |
| `2..` | start col 2, span to end of row |
| `3` | next available col, span 3 columns |
| `row` | full row |

### Responsive breakpoints

Two breakpoints, controlled via attributes on `<r-grid>` and `<r-cell>`:

```html
<r-grid columns=6 columns-s=3>
  <r-cell span=2 span-s=row>
  <r-cell span=3-6 span-s=row>
</r-grid>
```

| Attribute | Applies at |
|-----------|-----------|
| `columns` / `span` | default (large) |
| `columns-s` / `span-s` | small screens (≤ 600dp) |
| `columns-l` / `span-l` | very large screens |

The `columns-s` attribute alone often suffices — changing the column count reflows all cells without needing individual `span-s` overrides.

### Typography and baseline

The full framework (`raster2.css`) provides:
- Baseline grid derived from `--lineHeight` — all spacing in the system is a multiple of this variable, exactly like the cicero module in print
- `--fontSize` scales the entire typographic system proportionally
- Heading hierarchy (h1–h5) with scale harmony out of the box
- Monospace via `--fontMono`
- Image sizing respects fill/contain/align via CSS classes

Only the grid (`raster.grid.css`, ~5 kB gzipped) can be used standalone if typography is handled separately.

### CSS customization

```css
:root {
  --fontSize: 16px;       /* scales entire system */
  --lineHeight: 1.5;      /* baseline unit, governs all spacing */
  --fontMono: monospace;
}
```

### Common column configs (from examples)

| `columns=` | Typical use |
|-----------|-------------|
| 3 | Simple landing page, narrow content |
| 6 | Standard web layout, sidebar + content |
| 8 | Editorial, magazine-style |
| 9 | Asymmetric compositions |
| 16 | Dense dashboard, data tables |

### Poster/print application

The poster example at rsms.me/raster/examples/poster.html demonstrates Raster applied to a Swiss-style typographic poster (explicit Swiss Style reference, with Akzidenz Grotesk / Univers / Helvetica as canonical typefaces). A 4-column grid underlies the composition. This confirms Raster's design intent: it is not just a web utility, but a direct continuation of the Müller-Brockmann tradition for screen.

### Difference from print grids

| Dimension | Print (MBr) | Raster (web) |
|-----------|------------|--------------|
| Unit | points, ciceros | dp (device pixels), rem |
| Vertical module | leading in pt | `--lineHeight` in rem |
| Field height | fixed in lines of type | determined by content + CSS |
| Column width | computed from format | computed from viewport |
| Responsive | N/A | `columns-s`, `span-s` |
| Image sizing | whole fields only | CSS fill/contain/align |

The invariant across both: column count is explicit, cell placement is explicit, the vertical rhythm derives from a single typographic unit, and all other measurements are multiples of that unit.
