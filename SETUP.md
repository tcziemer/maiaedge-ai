# MaiaEdge AI Toolkit -- Setup Guide

This folder is your personal AI knowledge base. It contains skills (workflows Claude follows), context (company knowledge), and a build system that packages everything into Cowork plugins and Claude.ai Project uploads.

**New here?** Follow the steps below. Once set up, see [CHEATSHEET.md](CHEATSHEET.md) for daily use.

---

## Before You Start

Do these before sitting down at the computer:

1. Download the maiaedge-ai folder from SharePoint
2. Create a GitHub account (or use an existing one) at https://github.com
3. Create a new **empty** repository on GitHub called `maiaedge-ai` (no README, no .gitignore, no license -- leave everything blank)
4. Copy the repo URL -- it will look like: `https://github.com/YOUR-USERNAME/maiaedge-ai.git`

---

## Computer 1

### Step 1: Install Prerequisites

Install these four things. Accept all defaults unless noted.

**1a. Git for Windows**
- Download: https://git-scm.com/download/win
- Run installer, click Next through everything, accept all defaults
- Verify: open a terminal and run `git --version`

**1b. Node.js 18+**
- Download: https://nodejs.org (click the LTS button)
- Run installer, accept all defaults
- Verify: open a terminal and run `node --version`

**1c. Python 3**
- Download: https://www.python.org/downloads/
- Run installer -- **CHECK the box that says "Add Python to PATH"** (this is important)
- Accept all other defaults
- Verify: open a terminal and run `python --version`

**1d. Claude Code**
- Open Git Bash (search "Git Bash" in Start menu)
- Paste this command:

```bash
npm install -g @anthropic-ai/claude-code
```

### Step 2: Set Up the Folder

**Important:** Do NOT put this folder inside OneDrive, Dropbox, or any cloud sync folder. Cloud sync and git do not play well together.

Open Git Bash and paste these commands one at a time:

```bash
# Create a repos folder on your C: drive
mkdir -p /c/repos

# Copy the downloaded folder into repos (adjust source path as needed)
cp -r "/c/Users/$USER/Downloads/maiaedge-ai" /c/repos/maiaedge-ai

# Go into the folder
cd /c/repos/maiaedge-ai
```

### Step 3: Initialize Git and Push to GitHub

Still in Git Bash, in the maiaedge-ai folder. Paste these commands one at a time.

Replace `YOUR-USERNAME` with the actual GitHub username:

```bash
git init
git add -A
git commit -m "Initial toolkit"
git remote add origin https://github.com/YOUR-USERNAME/maiaedge-ai.git
git branch -M main
git push -u origin main
```

When prompted, sign in with your GitHub account in the browser window that opens.

### Step 4: Verify Everything Works

Still in Git Bash, in the maiaedge-ai folder:

```bash
# Start Claude Code (type /exit to quit)
claude

# Build all plugins and enterprise uploads
bash build.sh
```

After `bash build.sh` completes, you should see:
- "Build Complete" with plugin and skill counts
- `builds/plugins-zipped/` should contain 7 .zip files
- `enterprise/general-assistant/upload/` should contain .md files

### Step 5: Set Up Cowork

1. Open Cowork
2. Go to plugin management
3. Install each plugin zip from `C:\repos\maiaedge-ai\builds\plugins-zipped\`:

| Plugin | What It Does |
|--------|-------------|
| maiaedge-outreach | Cold emails, LinkedIn, prospect research, segment classification |
| maiaedge-enrichment-pipeline | Company research, enrichment, import processing |
| maiaedge-revops | Contact discovery, CRM hygiene, pipeline analytics, territory |
| maiaedge-sdr-pipeline | End-to-end batch: company list to 3-email sequences |
| maiaedge-sales-docs | Order forms, MSAs, POC agreements, NDAs |
| maiaedge-events | Conference prep, attendee processing, follow-up |
| linkedin-network-builder | LinkedIn networking automation |

### Step 6: Set Up Claude.ai Projects (optional)

1. Go to https://claude.ai
2. Create a new Project (e.g., "Founder Outreach")
3. Open the Project Knowledge section
4. Open the folder `C:\repos\maiaedge-ai\enterprise\founder-outreach\upload\` on your computer
5. Select all .md files and drag them into Project Knowledge
6. Repeat for any other projects you want:

| Project | What It Does | Upload From |
|---------|-------------|-------------|
| Founder Outreach | Cold emails + research in founder voice | `enterprise/founder-outreach/upload/` |
| General Assistant | Everything -- strategy, GTM, pricing, any question | `enterprise/general-assistant/upload/` |
| Sales Outreach | Full outreach workflow (enrichment to sequences) | `enterprise/sales-outreach/upload/` |
| Account Intelligence | CRM reports, pipeline, territory, enrichment | `enterprise/account-intelligence/upload/` |
| Call Intelligence | Call analysis, pipeline boards, dashboards | `enterprise/call-intelligence/upload/` |

---

## Computer 2

### Step 1: Install Prerequisites

Same four installs as Computer 1:

1. **Git for Windows** -- https://git-scm.com/download/win (accept defaults)
2. **Node.js 18+** -- https://nodejs.org (LTS, accept defaults)
3. **Python 3** -- https://www.python.org/downloads/ (**check "Add Python to PATH"**)
4. **Claude Code** -- open Git Bash, run: `npm install -g @anthropic-ai/claude-code`

### Step 2: Clone Your Repo

Open Git Bash and paste these commands. Replace `YOUR-USERNAME`:

```bash
mkdir -p /c/repos
cd /c/repos
git clone https://github.com/YOUR-USERNAME/maiaedge-ai.git
cd maiaedge-ai
```

### Step 3: Verify

```bash
# Start Claude Code (type /exit to quit)
claude

# Build everything
bash build.sh
```

### Step 4: Set Up Cowork + Projects

Same as Computer 1 Steps 5 and 6. Install plugin zips from `builds/plugins-zipped/` and optionally upload enterprise project files.

---

## Daily Use

### Using Claude Code
```bash
cd /c/repos/maiaedge-ai
claude
```
Then just talk:
- "Create a skill for board reporting"
- "Update the neocloud strategy with this new intel"
- "Research Equinix and draft a cold email for Tim Lieto"

### After Making Changes
```bash
# Rebuild plugins and enterprise uploads
bash build.sh

# Install updated plugin zips in Cowork
# Upload updated files to Claude.ai Projects (if using)
```

### Saving and Syncing
```bash
# Save your work
git add -A
git commit -m "what you changed and why"
git push

# On the other computer, get latest changes
git pull
```

---

## Quick Reference

See [CHEATSHEET.md](CHEATSHEET.md) for the full edit/build/deploy workflow table.

See [CLAUDE.md](CLAUDE.md) for skill descriptions, key rules, and how to create new content.
