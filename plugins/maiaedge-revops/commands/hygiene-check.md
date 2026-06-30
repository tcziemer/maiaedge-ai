---
description: Audit CRM data quality and find issues
argument-hint: "[full | duplicates | missing-fields | stale | enrichment | scorecard]"
---

Run a CRM hygiene check on MaiaEdge HubSpot data.

Arguments provided: $ARGUMENTS

Invoke the crm-hygiene skill. If a specific mode is provided, run that check. If no mode specified, run a full health check (all modes).

Modes:
- `full` — Run all checks, produce consolidated health report with 0-100 score
- `duplicates` — Find duplicate companies by domain and name similarity
- `missing-fields` — Find records missing critical fields (segment, state, owner, domain)
- `stale` — Find accounts with no activity in 90+ days
- `enrichment` — Find records that were imported but never fully enriched
- `scorecard` — Data completeness scorecard by segment
