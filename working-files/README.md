# working-files/

Operational files used by the MaiaEdge sales team. Not part of the AI toolkit codebase — `build.sh` does not read from here.

| Sub-folder | Contents | When to use |
|------------|----------|-------------|
| `brand/` | Canonical MaiaEdge logo set (Blk, RGB, RevWhite). One copy lives here; embed from this path when building docs. | Use as the source of truth for any logo asset. |
| `comp-plans/` | Sales compensation plans for Tim Lieto and Ken Cunningham | Reference when answering comp questions or modeling commission. |
| `enablement/` | Partner enablement deck and the Toolkit Cheatsheet PPTX | Reference when onboarding a partner or new rep. |
| `intro-briefings/` | Personalized intro briefings prepared for specific contacts (Andre van Zijl, Dario, future names) | Reference when preparing similar briefings; pattern-match on tone and structure. |
| `outreach-samples/` | Historical outreach campaign artifacts: ITW 2026 Smartlead CSVs, segment-specific outreach XLSX, LinkedIn target lists | Reference when running a new campaign — these are exemplar outputs, not active campaigns. |
| `pricing/` | Founding customer agreement + term sheet (HDCO), Movi pricing model, working pricing visuals | Reference when scoping or proposing pricing. |
| `sales-metrics/` | Pipeline dashboards, pipeline tracker decks, periodic call notes | Reference when reporting on pipeline state at a point in time. |
| `strategic/` | Internal strategy projects (LMaaS, Neocloud) — business cases, briefs, sensitivity models | Reference when doing strategic planning or extending these initiatives. |

## What does NOT belong here

- Active deal artifacts (those go in top-level `Nexus/`, `Quotes/`, or a new top-level account folder).
- Skill or context source files (those belong in `skills/` or `context/`).
- Anything `build.sh` should pick up (that goes in `context/`).

## Naming conventions

- Subfolders are kebab-case (`comp-plans`, `intro-briefings`, `sales-metrics`).
- File names use underscores rather than spaces where possible (helps Python/pandas/CLI workflows). Pre-existing files with spaces are left alone unless renaming would be low-risk.
