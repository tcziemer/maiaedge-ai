# Enterprise Project System Prompts

One file per Claude.ai Project. Paste the contents into the **Project Instructions** field in Claude.ai.

## Architecture

Skills live at the **Claude.ai instance level** (uploaded once from `builds/instance-skills/`). Every enterprise Project automatically has access to every skill by name — no skill files in Project knowledge. Each Project's `upload/` folder holds the **context files** (context/ `.md`s) that its skills need to operate reliably.

| File | Claude.ai Project | Context upload folder | Files | Skills assigned |
|------|-------------------|----------------------|------:|----------------:|
| [sales-outreach.md](sales-outreach.md) | MaiaEdge Sales Outreach | `enterprise/sales-outreach/upload/` | 32 | 10 |
| [founder-outreach.md](founder-outreach.md) | MaiaEdge Founder Outreach | `enterprise/founder-outreach/upload/` | 30 | 8 |
| [account-intelligence.md](account-intelligence.md) | MaiaEdge Account Intelligence | `enterprise/account-intelligence/upload/` | 52 | 12 |
| [call-intelligence.md](call-intelligence.md) | MaiaEdge Call Intelligence | `enterprise/call-intelligence/upload/` | 29 | 4 |
| [revenue-reporting.md](revenue-reporting.md) | MaiaEdge Revenue Reporting | `enterprise/revenue-reporting/upload/` | 21 | 4 |
| [crm-guardian.md](crm-guardian.md) | MaiaEdge CRM Guardian | `enterprise/crm-guardian/upload/` | 36 | 12 |
| [sales-docs.md](sales-docs.md) | MaiaEdge Sales Docs | `enterprise/sales-docs/upload/` | 35 | 4 |
| [general-assistant.md](general-assistant.md) | MaiaEdge General Assistant | `enterprise/general-assistant/upload/` | 56 | all 27 |

## Deployment workflow

1. **One-time:** upload every file in `builds/instance-skills/` to your Claude.ai instance as Skills. This is the single source of truth for skill logic across all Projects.
2. **Per Project:** upload the matching `enterprise/<project>/upload/` folder into Claude.ai Project knowledge (context files only).
3. **Per Project:** paste the matching prompt from this folder into the Project Instructions field.
4. **On skill update:** re-upload only the changed skill file(s) at the instance level — all Projects pick up the change automatically.
5. **On context update:** rebuild (`bash build.sh`) and re-upload the affected Project's `upload/` folder.

## What these prompts should do
- Orient Claude to the Project's purpose and the user's role
- Tell Claude which skills to use for which requests (skills resolve at instance level by name, e.g. `maiaedge-cold-outreach-writer`)
- Enforce cross-cutting rules (speed + ownership pairing, no em dashes, no competitor names in segment copy, tier inversion, etc. — see root `CLAUDE.md`)
- Point to the right context files by name when decisions depend on them
- Stay tight — Project Instructions run on every turn, so every paragraph costs tokens
