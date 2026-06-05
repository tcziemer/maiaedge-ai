# MaiaEdge Branded-Doc Skill

A complete kit for generating partner-grade PDFs in the MaiaEdge brand system.

## What's in this folder

```
SKILL.md                            ← The skill itself: design system, workflow, QA bar
assets/
├── brand.css                       Canonical stylesheet (Tomorrow + brand palette)
├── build.py                        Python builder: markdown → branded PDF
├── cover-template.html             Cover page scaffold with {{tokens}}
├── pattern-twotone.png             Cover pattern wash
├── fonts/                          9 Tomorrow weights (embedded in every PDF)
├── logos/                          MaiaEdge logos (white + RGB)
├── icons/                          Segment cover icons
└── diagrams/                       3 production SVG diagrams (architecture, activation flow, cloud on-ramp)
```

## How to use it

### Option 1 — Drop into a Claude.ai Project

1. Create or open a Project at claude.ai.
2. Upload `SKILL.md` plus everything in `assets/` into the Project's knowledge base.
3. In the Project's custom instructions, paste:
   > "When the user asks for a branded doc, partner cheat sheet, battle card, playbook, or any PDF deliverable in the MaiaEdge brand system, follow the workflow in SKILL.md and produce a PDF that matches the partner cheat sheets visually."
4. Then in any chat, say: *"Build me a branded doc about [topic]"* — Claude will follow the skill.

### Option 2 — Add as a Cowork plugin

This skill folder is structured to work as a Cowork plugin. Zip the whole `branded-doc/` folder, install via Cowork's plugin manager.

### Option 3 — Use the assets directly

If you just need the source files (Tomorrow fonts, logos, the brand stylesheet, the architecture diagrams):
- `assets/fonts/` — drop into Word, Figma, Adobe, etc.
- `assets/brand.css` — reference for any custom HTML / Notion / web work.
- `assets/diagrams/` — drop into slides, decks, web pages as-is. They're SVG so they scale infinitely.
- `assets/logos/` — official MaiaEdge logos.

## What "branded" means here

Every doc produced with this skill has:

- **Tomorrow font** embedded directly in the PDF (no font dependency on the recipient's machine).
- **Brand palette**: Gold `#FFC200` (primary), Orange `#FF9400` (accent), Heather `#D4D0C9` (warm neutral), Black `#000000`.
- **Black-hero cover page** with logo, segment icon, oversized title, and a gold tagline plate at the bottom.
- **Eyebrow-numbered sections** (`01 / FOUNDATION`, `02 / WHO BUYS MAIAEDGE`...) with gold rule under each title.
- **Component library**: pull quotes, pain quotes, callouts, anti-position cards, status-quo hero blocks, pillar cards, segment cards, brand-styled tables.
- **No em dashes** anywhere in customer-facing copy (this is a MaiaEdge identity rule).
- **Page footer** on every body page: `MAIAEDGE / PARTNER EDITION` left, `X / N` right.

## Examples in production

Open the partner docs final folder (`partner docs/final/` on Cooper's machine) for reference:
- `MaiaEdge-101.pdf` — flagship 101 brief, 11 pages
- `Cheat-Sheet-Colocation.pdf`
- `Cheat-Sheet-Fiber-Operator.pdf`
- `Cheat-Sheet-Network-Operator.pdf`
- `Cheat-Sheet-Neocloud.pdf`
- `Cheat-Sheet-MSP-Aggregator.pdf`
- `Product-Quick-Reference.pdf` — 12 pages, 3 embedded diagrams

Any new doc you build with this skill should look visually consistent with these.

## Common tasks

| You want | Say to Claude |
|---|---|
| New segment cheat sheet | "Build a cheat sheet for [segment]" |
| Battle card vs a competitor | "Make a battle card vs [competitor] in our brand system" |
| Internal playbook | "Turn this markdown into a partner-style playbook PDF" |
| Webinar one-pager | "Branded one-pager for [event/topic]" |
| Architecture brief | "Build a technical brief on [topic] using the architecture diagram" |

## Questions / changes

Loop in Cooper if you need to:
- Add a new component to the brand system
- Change a brand color or font
- Add a new icon or diagram to the asset library

The `SKILL.md` is the source of truth. If you find something useful and want to add it (a new component, a new lesson learned, a new icon), update SKILL.md and re-share.
