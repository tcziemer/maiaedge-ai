# MaiaEdge General Assistant — Enterprise Project Manifest

> Catch-all for strategic questions, GTM planning, pricing, partnerships, board narratives

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/general-assistant/upload/` (every context file + the branded-doc `assets/` tree). That built folder is the authoritative, complete file set; the lists below are a human reference and can lag the build. When in doubt, upload everything in `upload/`.

## Knowledge Files
Upload ALL skills and ALL context files. This is the kitchen-sink project.

### All Skills (upload as .md)
Every SKILL.md from skills/ directory

### All Context (upload as .md)
Every file from context/ directory (all subdirectories)

## Notes
- If hitting Project Knowledge capacity, prioritize context files over skill files
- Context = knowledge Claude can't infer; Skills = instructions that can be summarized

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; auto-discovers `context/segments/enterprise.md`, `context/segments/enterprise-use-cases.md`, `context/signals/enterprise-signals.md` via the find-all-md sweep)
