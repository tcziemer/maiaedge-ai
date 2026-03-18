# MaiaEdge AI Toolkit — Cheat Sheet

## The Rule: Edit Once, Build Once, Deploy Everywhere

```
YOU EDIT HERE:              build.sh GENERATES:
──────────────              ────────────────────
context/                 →  enterprise/*/upload/     (flat .md files for each Cloud Project)
skills/                  →  builds/plugins-zipped/   (7 plugin zips for Cowork)
                            builds/skills-zipped/    (5 standalone skill zips)
```

You NEVER edit files in `enterprise/*/upload/` or `builds/` directly. They are generated output.

---

## Folder Structure

```
maiaedge-ai/
├── context/              ← EDIT HERE (single source of truth for all knowledge)
├── skills/               ← EDIT HERE (single source of truth for all skill logic)
├── plugins/              ← Plugin packaging configs (manifests + commands)
├── enterprise/
│   ├── sales-outreach/upload/        38 .md files → drag into Cloud Project
│   ├── founder-outreach/upload/      34 .md files → drag into Cloud Project
│   ├── account-intelligence/upload/  47 .md files → drag into Cloud Project
│   └── general-assistant/upload/     65 .md files → drag into Cloud Project
├── builds/
│   ├── plugins-zipped/               7 plugin zips → install in Cowork
│   └── skills-zipped/                5 standalone skill zips → install in Cowork
├── build.sh              ← Run this once, get everything
├── CLAUDE.md             ← Claude Code reads this automatically
└── CHANGELOG.md          ← Version history
```

---

## Daily Workflow

### Update a context file or skill:
```bash
# 1. Edit the source file
#    (in Claude Code, just tell Claude what to change)

# 2. Rebuild everything
bash build.sh

# 3. Deploy
#    Cowork:     install updated zip from builds/plugins-zipped/
#    Enterprise: upload updated .md files from enterprise/*/upload/

# 4. Commit
git add -A && git commit -m "what you changed and why"
```

### In Claude Code, you just talk:
```
> Update the neocloud strategy with the Q2 intel and rebuild
> Run bash build.sh
> Show me what changed
```

---

## What Goes Where

| I want to...                          | Edit this                          | Then...                              |
|---------------------------------------|------------------------------------|--------------------------------------|
| Update messaging rules                | `context/core/messaging-framework.md` | `bash build.sh` → redeploy        |
| Update a segment cheatsheet           | `context/segments/<segment>.md`    | `bash build.sh` → redeploy          |
| Fix a skill's behavior                | `skills/<name>/SKILL.md`           | `bash build.sh` → redeploy          |
| Add a new context file                | Create in `context/<category>/`    | Add to plugin manifests + `build.sh` |
| Add a new skill                       | Create `skills/<name>/SKILL.md`    | Add to plugin manifest or standalone |
| Change which files a plugin bundles   | `plugins/<name>/plugin-manifest.json` | `bash build.sh`                   |
| Change which files a Project gets     | Edit the project section in `build.sh` | `bash build.sh`                 |

---

## Enterprise Projects — What Each One Is For

| Project | Workflow | Users |
|---------|----------|-------|
| **Sales Outreach** | Raw name → enrich → CRM → classify → contacts → emails/LinkedIn → briefs | Tim L, Ken C, Cooper |
| **Founder Outreach** | Same as Sales Outreach but founder voice (Timothy Z / Abilash M) | Timothy, Abilash |
| **Account Intelligence** | CRM queries → lists → coverage → pipeline → territory → enrichment → imports | Cooper, team |
| **General Assistant** | Catch-all: strategy, GTM, pricing, partnerships, anything | Everyone |
| **Sales Docs** | Order Forms, MSAs, POCs, NDAs (self-contained, no local maintenance) | Tim L, Ken C |
