# MaiaEdge Outreach Plugin

A cold email and LinkedIn outreach plugin for MaiaEdge, primarily designed for Cowork. Research prospects, classify segments, and write personalized outreach that sounds like a smart industry peer, not a sequence tool.

## What It Does

- **Researches** companies with mandatory web searches before writing anything
- **Classifies** prospects into qualified segments (fiber operators, colocation, AI colo, neoclouds, network operators, MSPs) or flags exclusions
- **Writes cold emails** with peer-to-peer tone, segment-specific messaging, and role-based pain points
- **Writes LinkedIn connection requests** under 300 characters with credibility anchors
- **Checks AI signals** for colocation operators to apply AI-specific messaging when warranted

## Commands

| Command | What It Does |
|---------|-------------|
| `/maiaedge-outreach:write-email` | Full workflow: research + classify + email + LinkedIn for a single prospect |
| `/maiaedge-outreach:research-prospect` | Research and classify a company without writing the email |
| `/maiaedge-outreach:batch-outreach` | Process multiple contacts with individual research for each |

## Skills (Auto-Activated)

| Skill | When It Fires |
|-------|---------------|
| `cold-email` | Writing cold emails, outreach, prospecting emails |
| `linkedin-outreach` | Writing LinkedIn connection requests or messages |
| `prospect-research` | Researching companies and contacts for outreach |
| `segment-classification` | Classifying companies into segments, applying messaging |

## Senders

Emails are written as one of two senders:

- **Tim Lieto** — AVP, North America Sales (default if unspecified)
- **Ken Cunningham** — Sales, East Region

## Connectors

The plugin connects to HubSpot CRM via MCP for contact management and task creation. Configure in `.mcp.json`.

## Customization

### Adding Reference Materials

Drop additional reference files (cheatsheets, messaging frameworks, competitive intel) into `skills/cold-email/references/`. The plugin will draw on them when relevant.

### Adjusting Messaging

Edit the segment messaging in `skills/segment-classification/SKILL.md` to update pain points, angles, or positioning as the product evolves.

### Adding Senders

Add new senders to the sender table in `skills/cold-email/SKILL.md`.

## Installation

### From Cowork UI
Upload the plugin folder through the Cowork plugin manager.

### From CLI
```bash
# If hosted in a Git repo
claude plugin install maiaedge-outreach

# Or install from local path
claude plugin install /path/to/maiaedge-outreach
```

## File Structure

```
maiaedge-outreach/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── .mcp.json                    # HubSpot MCP connector
├── README.md                    # This file
├── commands/
│   ├── write-email.md           # /maiaedge-outreach:write-email
│   ├── research-prospect.md     # /maiaedge-outreach:research-prospect
│   └── batch-outreach.md        # /maiaedge-outreach:batch-outreach
└── skills/
    ├── cold-email/
    │   ├── SKILL.md             # Email tone, structure, rules, quality
    │   └── references/          # Drop cheatsheets and reference docs here
    ├── linkedin-outreach/
    │   └── SKILL.md             # LinkedIn connection requests
    ├── prospect-research/
    │   └── SKILL.md             # Mandatory research process
    └── segment-classification/
        └── SKILL.md             # Segments, exclusions, messaging
```
