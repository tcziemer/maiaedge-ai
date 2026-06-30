# MaiaEdge Brand Reference

Detailed reference for the branded-doc skill. Read this **after** SKILL.md when building any branded PDF.

## Color palette

| Color | Hex | PMS | Role |
|---|---|---|---|
| Gold | `#FFC200` | 7548C | Primary brand accent |
| Orange | `#FF9400` | 2013C | Secondary accent (eyebrows, anti-position bars) |
| Heather | `#D4D0C9` | Warm Gray 1C | Warm neutral |
| Heather Tint | `#F4F2EE` | - | Soft section background |
| Black | `#000000` | Process Black C | Type, dark sections |
| Ink | `#1A1A1A` | - | Body text |
| Ink-2 | `#4A4A4A` | - | Secondary text |
| Rule | `#E5E1DA` | - | Hairline borders |

## Typography rules

Tomorrow only. Always embed via `@font-face`.

| Role | Weight | Size |
|---|---|---|
| Body | 400 | 9pt |
| Sub-titles | 700 | 12.5pt |
| Section titles | 800 | 20pt + gold underline |
| Eyebrows | 600/700 caps | 7.5pt with letter-spacing 0.22–0.32em |

**Identity rules (non-negotiable):**
- Never em dashes. Use `·` (middle dot) for inline caps separators.
- Always "carrier infrastructure" as our category - never IaaS / NaaS / "platform".
- Pillar cards rotate top borders: Gold / Orange / Black.
- Anti-position cards always Orange left bar; component cards always Gold.
- Status-Quo hero always Black with Gold accents.

## Component library

All defined in `brand.css`:

- `.cover` - full-bleed black + gold tagline plate (`@page cover { margin: 0 }`)
- `h1.section-title` - bold with 2pt gold underline rule
- `.eyebrow` - orange numbered caps label above section titles
- `.pullquote` - black bg, gold left bar, serif quote glyph
- `.pain-grid` / `.pain-quote` - heather-tint with gold left bar
- `.callout` - heather-tint with orange left bar
- `.chips` - compact label-value tile row
- `.component` - black header with gold icon plate
- `.pillar` - 3-up grid with rotating top borders
- `.anti-card` - orange left bar (competitive)
- `.status-quo` - black hero block (#1 Competitor)
- `table` / `table.qa` - black header + gold caps text + alternating tints
- `.steps` - numbered process steps
- `.diagram` - wrapper for embedded SVG diagrams

## Cover icon mapping

| Topic | Icon file in `assets/icons/` |
|---|---|
| Colocation (standard / AI) | `DC Cabinet.svg` |
| Fiber Operator | `Topology.svg` |
| Network Operator | `Router.svg` |
| Neocloud / GPU cloud | `Lab Server.svg` |
| MSP / Aggregator / TSD | `Customers.svg` |
| Product / hardware reference | `MaiaEdgeBox_black and yellow.svg` |
| Battle card / playbook | Closest segment match |

## Icon library (for diagrams + component cards)

Beyond the cover icons above, the full MaiaEdge brand icon set (40 SVGs, already on-palette) lives in `assets/icons/library/`. Use these inside diagrams, component cards, and benefit rows - reference by filename, do NOT restyle them.

- **Product:** `PBC.svg`, `PBC Extended.svg`, `PCE_Icon_black.svg`, `Port Extender.svg`, `MaiaEdgeBox_black and yellow.svg`, `ColoBox_black.svg`, `Systems box_black.svg`
- **Network / infrastructure:** `Cloud Onramp.svg`, `Cross-Connect.svg`, `Paths.svg`, `Links.svg`, `Topology.svg`, `Router.svg`, `EthernetW_black.svg`, `MultiCloud_black.svg`, `Server NICs.svg`, `DC Cabinet.svg`, `Building.svg`, `Traffic Management.svg`
- **Value props / benefits:** `Deterministic_black.svg`, `FasterRevenue_black.svg`, `IncreaseRevenue_black.svg`, `SaveCost_black.svg`, `HighBandwidth_black.svg`, `HighVelocity_black.svg`, `OnDemand_black.svg`, `PathDriven_black.svg`, `PlugandPlay_black.svg`, `PushButton_black.svg`, `FutureReady_black.svg`, `Marketplace.svg`
- **Ops / lifecycle:** `Dashboard.svg`, `Alarms.svg`, `Events.svg`, `Inventory.svg`, `Lifecycle.svg`, `POC Deployment.svg`, `Customers.svg`, `Users.svg`

The cover icons in the mapping above are the same set; they also live at `assets/icons/` (one level up) and must stay there for the cover build.

## Product images (for hardware / datasheet docs)

Real product photography lives in `assets/product-images/` - use for product/hardware references, datasheets, and one-pagers where a device shot helps:
- **PBC:** `product-images/PBC/` - bezel front + perspective, ambient-light hero, packaging, icon.
- **Port Extender (MPP):** `product-images/Port-Extender/` - front + side.

Place on a light (`#F4F2EE`) or black block; constrain by width and let height scale, do not stretch.

## Diagram library

In `assets/diagrams/` (use SVG, not PNG):
- `architecture-diagram.svg` - system architecture (Customer Layer / Control Plane / Data Plane)
- `activation-flow-diagram.svg` - 8-step path activation timeline
- `cloud-onramp-diagram.svg` - frontstage / backstage / destination cloud on-ramp pipeline

If you need a NEW diagram, build as SVG: 1600×1100 viewBox, brand colors, layer labels in orange caps on the left, components as cards with gold left bars or full black hero blocks, Tomorrow font.

## Build pipeline detail

`assets/build.py`:

1. Strips H1 + intro lines
2. Pre-processes markdown to insert blank lines before lists (so they parse as lists)
3. Renders to HTML with `markdown` + `tables`, `fenced_code`, `sane_lists` extensions
4. Post-processes HTML:
   - Wraps each `<h2>` in a `<section>` with auto-numbered eyebrow
   - Maps title to short eyebrow label (FOUNDATION, OBJECTIONS, COMPETITIVE...)
   - Converts `<h3>` to `<h2 class="sub-title">`
   - Groups consecutive blockquotes into `.pain-grid`, or detects `**Label:**` → `.callout`
   - Tags Q&A-style tables with `class="qa"`
5. Wraps body in `<div class="md">` + cover template
6. Renders to PDF via WeasyPrint

## Cover template tokens

In `assets/cover-template.html`:

| Token | Example value |
|---|---|
| `{{title}}` | "Colocation" |
| `{{title_accent}}` | "Cheat Sheet." |
| `{{segment_tag}}` | "Partner Cheat Sheet" |
| `{{segment_sub}}` | "MaiaEdge for Colocation Operators" |
| `{{subtitle}}` | "Use this when you're calling on..." |
| `{{icon_path}}` | "assets/icons/DC Cabinet.svg" |

**Don't change** the pattern-band positioning (`top: 5.7in, height: 3.4in, opacity: 0.42`). Cooper has reviewed and approved this exact placement.

## Lessons learned

1. **Always embed Tomorrow** in the inline `<style>` of any standalone HTML file (the `@font-face` block from `brand.css` must be present). Verify with `pdffonts <pdf>`.

2. **Don't force page breaks.** Content should flow continuously. Use:
   - `.eyebrow { page-break-after: avoid }`
   - `h1.section-title, h2.sub-title { page-break-after: avoid }`
   - `tr { page-break-inside: avoid }`
   - `.component-head { page-break-after: avoid }`

3. **Closer blocks orphan easily.** For cheat sheets, omit the closing tagline block - the cover and footer already establish the tagline. For longer docs (MaiaEdge 101) the closer is OK because it lands with substantial prior content.

4. **Tomorrow has wider metrics** than system fallbacks. When swapping from system-fallback → Tomorrow: body 9.5pt → 9pt, line-height 1.5 → 1.4, table cell padding `7pt 10pt` → `5pt 9pt`. Re-verify page counts.

5. **SVG > PNG** for embedded diagrams. WeasyPrint scales SVG perfectly; PNGs at 200 DPI render at unwanted natural pixel size.

6. **Pre-process markdown lists** with this regex (markdown libs fail if no blank line before list):
   ```python
   text = re.sub(
       r"(?m)^(?!\s*$)(?![\-\*\+]\s)(?!\d+\.\s)(?!#)(?!\>)(.+)\n(\s*\d+\.\s)",
       r"\1\n\n\2", text,
   )
   ```

7. **Page footer** on every body page - `MAIAEDGE / PARTNER EDITION` left, `X / N` right. Configured in `brand.css` via `@page { @bottom-left { content: ... } @bottom-right { content: counter(page) ... } }`.

8. **Cover uses separate `@page cover` rule.** Margins 0 for full bleed, footer suppressed. Apply via `.cover { page: cover; page-break-after: always; }`.

## Quality checklist

- ☐ Tomorrow embedded (`pdffonts` confirms)
- ☐ Cover: gold tagline plate at bottom + pattern band above it
- ☐ Every section title has gold underline
- ☐ No table row split mid-cell across pages
- ☐ No page > 30% whitespace at the bottom
- ☐ No em dashes in customer-facing copy
- ☐ File size sensible (< 1MB cheat sheet, < 1.5MB with embedded diagrams)
- ☐ Filename: `<DocType>-<Topic>.pdf`

## Reference examples

The canonical docs are built by `build.py` from their markdown sources in `context/partner-assets/`. Those sources are always current - read the matching one for structure, depth, and section order:
- `maiaedge-101.md` -> the 11-page flagship 101 brief
- `cheatsheet-<segment>.md` (6 segments) -> the segment cheat sheets (typical structure; the neocloud one carries an extra "Sub-Segment Cheat Codes" section)
- `product-quick-reference.md` -> the 12-page technical reference with 3 embedded diagrams

For a VISUAL match, open whatever approved PDFs are currently in `partner docs/final/`. If the generated set (`MaiaEdge-101.pdf`, the cheat sheets, `Product-Quick-Reference.pdf`) is not present, regenerate it with `python3 build.py`. Anything new should match these in look and structure.
