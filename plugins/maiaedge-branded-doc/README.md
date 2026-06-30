# MaiaEdge Branded Doc Plugin

Generate partner-grade PDFs in the MaiaEdge design system — visually consistent with the partner cheat sheets and MaiaEdge 101. Tomorrow font embedded, gold/orange/black palette, doc-style covers, eyebrow-numbered sections, branded tables, and component cards.

## Skills

- `branded-doc` — Authors markdown and renders it to a branded PDF via the bundled renderer (`assets/build.py`, WeasyPrint). Also ships the locked-template one-pager solution-brief system under `assets/onepager/`.

## What's bundled

The skill carries its full runtime payload under `skills/branded-doc/assets/`:

| Asset | Purpose |
|-------|---------|
| `brand.css` + `fonts/Tomorrow-*.ttf` (9 weights) | Brand stylesheet with embedded `@font-face` |
| `build.py` | The renderer (markdown → branded HTML → PDF) |
| `cover-template.html` | Full-bleed doc-style cover wrapper |
| `brand-reference.md` | Full brand system: colors, components, lessons, gotchas |
| `logos/`, `icons/`, `pattern-twotone.png` | Cover + section art |
| `diagrams/*.svg` | Production architecture / activation-flow / cloud-onramp diagrams |
| `onepager/` | Locked, QA-gated single-page Solution Brief renderer (`render.py`, `qa.py`, schema, worked examples, vendored fonts) |

## Context

- `core/messaging-framework.md` — positioning rules the skill reads before authoring copy.

## Use when

- New segment cheat sheet, battle card, playbook, one-pager, or technical brief
- Any markdown content that should ship as a branded partner-facing PDF

**Don't use for:** legal docs (use `sales-docs`), short copy/emails (use the outreach skills).

## Default output

Branded PDF (primary). Requires WeasyPrint with pango/cairo for rendering; see `skills/branded-doc/QUICKSTART.md`.
