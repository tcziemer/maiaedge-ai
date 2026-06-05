# MaiaEdge Branded Doc Kit - Quickstart

Everything you need to generate partner-grade PDFs in the MaiaEdge brand system is in this skill.

## What's Inside

```
skills/branded-doc/
├── QUICKSTART.md           ← You are here
├── README.md               ← Detailed usage guide with common tasks
├── SKILL.md                ← The AI skill (Claude reads this to know how to build docs)
└── assets/
    ├── brand.css           ← Master stylesheet (colors, fonts, components)
    ├── build.py            ← Python script that converts markdown to branded PDF
    ├── cover-template.html ← Cover page scaffold with fill-in tokens
    ├── pattern-twotone.png ← Cover page pattern overlay
    ├── brand-reference.md  ← Full design system reference (colors, components, rules)
    ├── fonts/              ← 9 Tomorrow font weights (embedded in every PDF)
    ├── logos/              ← MaiaEdge logos (white + RGB SVG)
    ├── icons/              ← Segment cover icons (one per ICP segment)
    └── diagrams/           ← 3 production SVG diagrams (architecture, activation, cloud on-ramp)

Companion folders (elsewhere in the repo):
├── context/core/messaging-framework.md  ← Positioning rules (single source of truth, read by AI before writing any copy)
└── context/partner-assets/              ← The markdown source files used to build the existing partner docs
    ├── maiaedge-101.md
    ├── cheatsheet-colocation.md
    ├── cheatsheet-fiber-operator.md
    ├── cheatsheet-network-operator.md
    ├── cheatsheet-neocloud.md
    ├── cheatsheet-msp-aggregator.md
    └── product-quick-reference.md
```

## Option 1: Use with Claude.ai (Recommended for Non-Technical Users)

This is the easiest path. No Python, no installs, no command line.

1. Go to claude.ai and create a new **Project**.
2. Upload these files into the Project's knowledge base:
   - `SKILL.md`
   - `assets/brand-reference.md`
   - `context/core/messaging-framework.md` (from the repo)
   - Everything in `assets/fonts/`
   - Everything in `assets/logos/`
   - Everything in `assets/icons/`
   - Everything in `assets/diagrams/`
   - `assets/brand.css`
   - `assets/build.py`
   - `assets/cover-template.html`
   - `assets/pattern-twotone.png`
3. In the Project's **Custom Instructions**, paste this:

   > When the user asks for a branded doc, partner cheat sheet, battle card, playbook, or any PDF in the MaiaEdge brand system, follow the workflow in SKILL.md and produce a PDF that matches the partner cheat sheets visually. Use brand-reference.md for the full design system. Follow messaging-framework.md for all positioning and copy rules.

4. Start a conversation and say something like:
   - "Build me a branded cheat sheet about [topic]"
   - "Turn this markdown into a partner-style PDF"
   - "Make a battle card vs [competitor] in our brand system"

Claude will read the skill, follow the workflow, and produce a branded PDF.

## Option 2: Use with Cowork

If you have Cowork installed:

1. Zip the entire `skills/branded-doc/` folder.
2. Install via Cowork's plugin manager.
3. The skill auto-activates when you ask for branded docs.

## Option 3: Run the Build Script Directly

For batch-building all partner docs from their markdown sources:

**Prerequisites:**
- Python 3.8+
- Install dependencies: `pip install weasyprint markdown`
- WeasyPrint also needs system libraries. See: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

**Steps:**
1. Place your markdown source files in a folder.
2. Edit `assets/build.py` to point `MD_DIR` at your markdown folder and `OUT_DIR` at your desired output folder.
3. Run: `python3 assets/build.py`
4. PDFs appear in the output folder.

## Using the Assets Directly (Fonts, Logos, Diagrams)

Even without the AI skill, the assets in this kit are useful on their own:

- **Fonts** (`assets/fonts/`): Drop Tomorrow .ttf files into Word, Figma, Canva, Adobe, etc.
- **Brand CSS** (`assets/brand.css`): Reference for any custom HTML, Notion, or web work.
- **Diagrams** (`assets/diagrams/`): Drop SVGs into slides, decks, or web pages. They scale infinitely.
- **Logos** (`assets/logos/`): Official MaiaEdge logos in SVG format.
- **Icons** (`assets/icons/`): Segment-specific icons for covers and headers.

## Brand Rules (The Short Version)

- **Font:** Tomorrow only. Always.
- **Colors:** Gold #FFC200 (primary), Orange #FF9400 (accent), Heather #D4D0C9 (warm), Black #000000
- **No em dashes** in any customer-facing content. Ever. Use middle dot (·) for inline separators.
- **"Carrier infrastructure"** is the only acceptable way to describe what MaiaEdge is. Never IaaS, NaaS, or "platform."
- **Tagline:** Private paths. Any network. Instantly.

Full design system details are in `assets/brand-reference.md`.

## Example Markdown Sources

The `context/partner-assets/` folder (in the repo root, not inside this skill) contains the markdown files used to build the existing partner doc set: MaiaEdge 101, all 5 segment cheat sheets, and Product Quick Reference. Use these as templates when creating new docs.

## Questions?

Loop in Cooper Kennedy (RevOps) if you need to add new components to the brand system, change colors or fonts, or add new icons/diagrams.
