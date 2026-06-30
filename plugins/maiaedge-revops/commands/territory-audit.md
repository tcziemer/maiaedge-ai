---
description: Validate account territory assignments against the territory model
argument-hint: "[full | check [company] | distribution | corrections]"
---

Audit territory assignments in HubSpot.

Arguments provided: $ARGUMENTS

Invoke the territory-manager skill. If a specific mode is provided, run that check.

Modes:
- `full` — Audit all company records: find misassigned accounts, missing states, wrong owners
- `check [company]` — Check a single company's territory assignment
- `distribution` — Territory distribution report: account count per owner, segment mix, geographic heat map
- `corrections` — Generate a correction file for all misassigned accounts (HubSpot-ready import)
