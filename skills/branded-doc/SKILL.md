---
name: maiaedge-branded-doc
description: "Generate partner-grade PDFs in the MaiaEdge brand system. Tomorrow font (embedded), gold/orange/black palette, doc-style cover, eyebrow-numbered sections, branded tables, component cards. Use for partner cheat sheets, MaiaEdge 101-style briefs, battle cards, playbooks, one-pagers, technical references — any partner-facing PDF that should look like the existing partner doc set. Triggers: 'branded doc about X', 'partner PDF for X', 'cheat sheet / battle card / playbook in our brand system', 'turn this markdown into a branded PDF'."
---

# MaiaEdge Branded Doc Generator

Produces partner-grade PDFs in the MaiaEdge design system — visually consistent with the partner cheat sheets and MaiaEdge 101.

## Use when

- New segment cheat sheet, battle card, playbook, one-pager, or technical brief
- Any markdown content that should ship as a branded partner-facing PDF

**Don't use for:** legal docs (use `sales-docs`), short copy/emails (use outreach skills).

## Workflow

1. **Read** `assets/brand-reference.md` (full brand system: colors, components, lessons learned, gotchas). Also read `context/core/messaging-framework.md` for positioning rules.

2. **Stage assets** — copy from this skill's `assets/` into the working directory:
   - `brand.css` (with `@font-face` for Tomorrow)
   - `fonts/Tomorrow-*.ttf` (9 weights)
   - `logos/logo-white.svg`
   - `pattern-twotone.png`
   - `icons/<segment>.svg` (cover icon — see mapping in brand-reference.md)
   - `cover-template.html`
   - `build.py` (the renderer)

3. **Author markdown.** Standard markdown. `## Title` for sections, `### Title` for sub-sections. Tables → branded tables. `> Blockquotes` → pain-quote panels (or callouts if a single quote starts with `**Label:**`).

4. **Build** — run `python3 assets/build.py` (or call the equivalent steps inline). It strips the H1, pre-processes lists, renders HTML, post-processes (auto-numbered eyebrows, pain-quote grouping, Q&A table tagging), wraps in cover, and renders PDF via WeasyPrint.

5. **Cover** — fill `cover-template.html` tokens: `title`, `title_accent`, `segment_tag`, `segment_sub`, `subtitle`, `icon_path`.

6. **Diagram swaps** — for ASCII diagrams in fenced code blocks, replace with one of the production SVGs in `assets/diagrams/` (architecture, activation-flow, cloud-onramp). New diagrams: build as SVG with brand colors at 1600×1100 viewBox.

7. **Render PDF** — `HTML(filename="doc.html", base_url=".").write_pdf("Doc.pdf")`. The `base_url` must resolve `@font-face` URLs.

8. **QA pass:**
   - `pdffonts Doc.pdf` confirms Tomorrow is embedded
   - Render every page to PNG: `pdftoppm -r 80 -png Doc.pdf qa/p` and visually verify
   - No table row split mid-cell, no page > 30% whitespace at the bottom, no em dashes anywhere

9. **Output** — save to `partner docs/final/`. Filename: `<DocType>-<Topic>.pdf` (e.g., `Cheat-Sheet-Colocation.pdf`, `Battle-Card-Cisco.pdf`).

## Brand system at a glance

- **Colors:** Gold `#FFC200` (primary), Orange `#FF9400` (accent), Heather `#D4D0C9` (warm), Black, Heather Tint `#F4F2EE`
- **Font:** Tomorrow only, embedded via `@font-face`
- **No em dashes** — use `·` for inline caps separators
- **"Carrier infrastructure"** is the only acceptable category descriptor

Full reference: `assets/brand-reference.md`.

## Reference examples

Open these to see "branded" in practice:
- `partner docs/final/MaiaEdge-101.pdf` (11-page flagship brief)
- `partner docs/final/Cheat-Sheet-Colocation.pdf` (6-page segment cheat sheet)
- `partner docs/final/Product-Quick-Reference.pdf` (12-page technical reference)

Anything new should match these visually.
