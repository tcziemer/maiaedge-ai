---
name: crm-guardian
description: "MaiaEdge CRM Guardian  -  autonomous CRM maintenance orchestrator, split into eleven independent routines (territory & hygiene, duplicate account audit, flagged-for-deletion consolidation, fresh enrichment, stale re-enrichment, contact duplicate flagging, persona gap fill, monthly account sourcing, quarterly job-change detection, monthly tier-audit, weekly edge-case-resolution) plus the sibling weekly-signal-scan. Writes corrections to HubSpot via MCP and manages contacts via Apollo MCP. Per-routine Slack DM is the audit trail. Use when asked to run CRM guardian, check CRM health, auto-fix CRM issues, run territory corrections, enrich new or stale accounts, audit accounts proposed for deletion, consolidate duplicate contacts, source new prospects, fill persona gaps, detect job changes, run tier-audit drift correction, resolve manual-review edge cases, or review the CRM change log."
---

# MaiaEdge CRM Guardian

## Purpose

CRM Guardian is the autonomous maintenance layer for MaiaEdge's HubSpot CRM. It writes back to HubSpot and creates contacts via Apollo under a three-tier safety system: most corrections are fully automatic (Tier 1), some are applied but flagged for Cooper's review (Tier 2), and high-risk changes require human approval (Tier 3).

**Architecture:** CRM Guardian is orchestration-only. It defines WHAT to run, WHEN, and at what safety tier. The sub-skills define HOW. Each sub-skill is the single source of truth for its domain logic. CRM Guardian never duplicates sub-skill logic  -  it references it.

**Execution model: 11 independent routines + 1 cross-routine drift sweep, scheduled separately.** The previous monolithic "run all jobs at 2 AM" master cycle has been split into eleven routines plus the weekly R-Tier-Audit drift sweep (R-Tier-Audit + D7 added 2026-05-14 as Phase 3 of the Account Tiering & Segmentation Overhaul; R-Tier-Audit cadence widened from monthly to weekly 2026-05-14 per Cooper). Each has its own schedule, scope, session budget, and report. Failures in one routine do not block the others. Each routine is defined by its own prompt file in `routines/claude-code/` (Claude Code), `cowork-scheduled-tasks/` (Cowork scheduled tasks - sibling of `routines/`), or `routines/cowork/` (Cowork manual-trigger tasks), with `trigger.md` / `task.md` sidecar metadata. The routines reference this SKILL.md for shared invariants, safety tiers, sub-skill domain logic, and the Cross-Routine Ledger - but the scheduling boundary is the routine, not the job.

| # | Routine | Cadence | Prompt file | Goal |
|---|---------|---------|-------------|------|
| 0 | Import Validator | Daily, 9:00 AM CT *(Cowork)* | `cowork-scheduled-tasks/r0-import-validator/prompt.md` | Validate name vs. domain on records imported in the last 24h; auto-rename mismatches, auto-flag hard-category junk (restaurants, apparel, churches, etc.) before enrichment wastes credits |
| 1 | Fresh Account Enrichment | Daily, 10:00 AM CT *(Cowork)* | `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` | Pre-score triage → enrich blank-segment ICP candidates (50/day Apollo cap), fast-classify non-ICP without Apollo. Inlines `context/account-tiering/tier-compute-spec.md` for the tier write at Stage 4. |
| 2 | Stale Account Re-Enrichment | Daily, 11:00 AM CT *(Cowork)* | `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` | Pre-score triage → full re-enrichment of ICP only; light-touch idempotency bump on Other / Partner Target / non-ICP records. Inlines `context/account-tiering/tier-compute-spec.md` for the tier write at Stage 4. |
| 3 | Duplicate Account Audit | Daily, 2:00 AM ET *(Claude Code)* | `routines/claude-code/r3-duplicate-accounts/prompt.md` | Detect company duplicates, reassociate contacts, flag losers |
| 4 | Flagged-for-Deletion Consolidation | Daily, 12:00 PM CT *(Cowork)* | `cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md` | Resolve contacts on flagged companies (preserve + reassociate, else flag) |
| 5 | Contact Duplicate Flagging | Weekly, Sun 1:00 AM ET *(Claude Code)* | `routines/claude-code/r5-contact-dedup/prompt.md` | Flag exact-email contact duplicates |
| 6 | Territory & Hygiene Sweep | Daily, 1:00 AM ET *(Claude Code)* | `routines/claude-code/r6-territory-hygiene/prompt.md` | Territory audit, enum migration, contact owner cascade, Mode 11 junk flags, **drain mode** for stale NEW leads (1000/run) + orphan contacts (300/run) + missing tier/sub-segment cascades (650/run combined). Tier corrections during cascades inline `context/account-tiering/tier-compute-spec.md`; `hs_is_target_account = true` records are skipped on the tier write. Step 5.5 also writes `signal_heat` alongside tier (heat is NOT frozen by the target-account flag). |
| 7 | Monthly New Account Sourcing | Monthly, 1st of month 9:00 AM ET *(Claude Code)* | `routines/claude-code/r7-monthly-sourcing/prompt.md` | account-sourcing CRM gap analysis + web search; surfaces Tier 3 candidates only (no auto-create) |
| 8 | Weekly Persona Gap Fill | Weekly, Fri 9:00 AM ET *(Claude Code)* | `routines/claude-code/r8-persona-fill/prompt.md` | Audit Tier 1+2 accounts for persona gaps; **auto-create via Apollo two-step (search → reveal → LinkedIn validate)** at Tier 2. Sort target accounts by `signal_heat` (`Hot` first - Title Case per HubSpot enum) for Apollo-budget priority. |
| 9 | Quarterly Job-Change Detection | Quarterly, 1st of Jan/Apr/Jul/Oct 9:00 AM ET *(Claude Code)* | `routines/claude-code/r9-quarterly-job-changes/prompt.md` | Apollo + LinkedIn cross-check on Tier 1+2 + open-deal contacts; surface departures, auto-create verified replacements at Tier 2 |
| 10 | R-Tier-Audit (Daily Drift Sweep) *- Cowork scheduled task* | Daily M-F 3:00 PM CT (cron `0 20 * * 1-5` UTC = 3pm CT during CDT; cadence widened to daily 2026-05-21 per Cooper) | `cowork-scheduled-tasks/r-tier-audit/prompt.md` (Cowork-only) | Cross-routine drift correction sweep over all ICP records. Recompute `account_tier` AND `signal_heat` per `context/account-tiering/tier-compute-spec.md` and surface drift > expected delta. **10% circuit breaker** (loosened 2026-05-21 from 5% for daily cadence). Apollo budget = 0 (HubSpot-only read + compute). `hs_is_target_account = true` records audited but tier write skipped (heat writes proceed). Daily cadence catches open-deal Hot transitions within 24h instead of 7 days; task is Apollo-free + idempotent (no-op when computed_tier == current_tier AND computed_heat == current_heat) so the cost is trivial. **Execution model: Cowork scheduled task (cron-fired, fire-and-forget, stateless across runs), not a Cowork routine.** |
| D7 | Edge Case Resolution (Weekly) *- Cowork scheduled task* | Weekly, Cooper-chosen day (suggested Wed 9am CT, cron `0 14 * * 3` UTC = Wed 9am CT during CDT) | `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md` (Cowork-only) | Deep-research targeted resolution queue. Entry criteria: (a) records on `manual_review_required` for >7 days, (b) records on `low_5069` confidence for >60 days, (c) Unknown / Other classifications with deal activity in last 30d, (d) crm-hygiene flagged records from its weekly audit (defense-in-depth feed). **Per-run cap 30 records; hard 14-day max wall-clock time on any single record before forced Cooper-escalation.** Apollo budget = 0 (deep web research + segment-classification only; if Apollo enrichment needed, defer to next R1 run). Complements R2 (broad re-enrichment cadence) and crm-hygiene (audit-only flagging). **Execution model: Cowork scheduled task (HubSpot is source of truth for the queue; no persistent task-local state across runs).** |

**Daily run order:** **0 (12:30 AM) → 6 (1 AM) → 3 (2 AM) → 4 (3 AM) → 1 (6 AM) → 2 (8 AM).** Import validation FIRST so the day's bad imports get killed before territory verifies them and before enrichment burns Apollo credits on them. Territory next so downstream routines see correct owners; dedup before enrichment so Apollo credits don't get burned on duplicates; flagged-cleanup before enrichment so contacts land on the correct primary; fresh + stale enrichment consume Apollo budget last. Routines 7, 8, 9 run at 9 AM ET on their own cadences (after the daily window closes); the sibling weekly-signal-scan was split 2026-05-28 into 6 per-ICP scans + 1 aggregator firing Mon 8:30am–2:30pm CT (see `cowork-scheduled-tasks/signal-scan-*`); R-Tier-Audit runs daily M-F 3pm CT (cadence widened from Sunday-weekly 2026-05-21 per Cooper; cron `0 20 * * 1-5` UTC); D7 runs once a week on Cooper's chosen day (no overlap constraint with daily routines - its 30-record cap keeps the runtime small).

**Job-to-Routine mapping** (for context when reading the Job Definitions below):
- Routine 1 ↔ Job 2 (new-accounts half only)
- Routine 2 ↔ Job 2 (re-enrichment half only)
- Routine 3 ↔ half of Job 7 (company dedup + contact reassociation from duplicates)
- Routine 4 ↔ half of Job 7 (flagged-company contact consolidation)
- Routine 5 ↔ part of Job 1 Mode 11 + contact dedup logic
- Routine 6 ↔ Jobs 1 (most modes) + Job 3
- Routine 7 ↔ Job 4 (monthly account sourcing)
- Routine 8 ↔ Job 5 (weekly persona gap fill, Fridays)
- Routine 9 ↔ Job 6 (quarterly contact job-change detection)
- (Sibling routine, not numbered) ↔ Job 8 (weekly signal scan, Mondays - split 2026-05-28 into 7 Cowork scheduled tasks; monolithic `weekly-signal-scan-prompt.md` archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/`; production prompts: `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise,aggregator}/prompt.md`)

**All 8 jobs are now split into independent routines.** The legacy `crm-guardian-prompt.md` monolithic prompt is kept in the repo for manual "run everything at once" backfill scenarios but is no longer the production execution path. The Job Definitions section below remains the canonical domain-logic reference for all eight jobs; the routine prompts reference these definitions rather than redefining them.

## Reference Files

**HubSpot schemas:** `context/hubspot/property-schema.md`, `context/hubspot/hubspot-values.md`, `context/hubspot/contact-schema.md`, `context/hubspot/deals-schema.md`, `context/hubspot/territory-model.md`, `context/hubspot/poc-schema.md`

**Core:** `context/core/icp-playbook.md`, `context/core/segment-qualification.md`, `context/core/maiaedge-101.md`, **`context/account-tiering/tier-compute-spec.md`** (canonical tier function - read by R1, R2, R6, Signal Scan Stage 5b, R-Tier-Audit, and D7 for every `account_tier` write; honors `hs_is_target_account = true` by computing-then-skipping the write), **`context/account-tiering/sub-segment-qualification.md`** (canonical 30-value list of active `company_sub_segment` enums, case-sensitive - supersedes scattered enum lists; key new values: `Subsea cable operator` added 2026-05-14 as the 30th, `Greenfield` is a real sub-segment paired with Colo or NeoCloud parent, `Crypto to AI - Neoclouds` inclusive of operator AND landlord; 3 retired values archived 2026-05-13: `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, plus pre-Phase-1.7c.1 `Managed Network Services - Network Operator`), **`context/account-tiering/enrichment-protocols.md`** (research-first workflow + D1 disqualifier check + D5 v2 per-sub-segment protocols + §8-§9 verification queries used by crm-hygiene's weekly audit). The consolidated qualification reference also lives at `context/account-tiering/sub-segment-qualification-full.md` - file 06 is the canonical source if `sub-segment-qualification.md` and the upstream consolidated reference diverge.

**Segments:** `context/segments/colocation.md`, `context/segments/fiber-operator.md`, `context/segments/neocloud.md`, `context/segments/network-operator.md`, `context/segments/msp-aggregator.md`, **`context/segments/enterprise.md`** (Multi-DC ICP, 4 sub-segments only, anchor account Meijer), **`context/segments/enterprise-use-cases.md`** (8 priority Enterprise use cases x sub-segment x persona)

**Enrichment:** `context/enrichment/sourcing-reference-guide.md`, `context/enrichment/research-routes.md`, `context/enrichment/output-schemas.md`

**Classification gates (HIGH - read before any segment/eviction decision):**
- `context/account-tiering/d1-global-disqualifiers.md` - D1 global disqualifier list; every eviction decision must pass a D1 check before writing `Flagged for deletion`
- `context/signals/signal-framework.md` - 5-field signal engine spec; signal writes in R6/R-Tier-Audit/D7 must align with these semantics

**Classification disambiguation (MEDIUM):**
- `context/account-tiering/d2-wholesale-arm-policy.md` - wholesale-arm carveout; prevents false-positive evictions on ICP subsidiaries
- `context/account-tiering/d3-disambiguation-flowcharts.md` - tiebreaker flowcharts for borderline segment routing
- `context/account-tiering/icp-deep-dives/B-and-C-colocation.md` - anchor-based classification evidence for Colo
- `context/account-tiering/icp-deep-dives/B-and-C-fiber-operator.md` - anchor-based classification evidence for Fiber
- `context/account-tiering/icp-deep-dives/B-and-C-neocloud.md` - anchor-based classification evidence for NeoCloud
- `context/account-tiering/icp-deep-dives/B-and-C-network-op.md` - anchor-based classification evidence for Network Op
- `context/account-tiering/icp-deep-dives/B-and-C-msp-aggregator.md` - anchor-based classification evidence for MSP/Aggregator
- `context/account-tiering/icp-deep-dives/B-and-C-enterprise.md` - anchor-based classification evidence for Enterprise

**Terminology (LOW):**
- `context/core/terminology-glossary.md` - canonical term definitions for field values and category names

**Sub-skills (read these for domain logic  -  Guardian does not redefine their methodology):**
- **crm-hygiene**  -  Modes 2-11: duplicates, missing fields, stale records, completeness, deprecated enums, contact hygiene, stale leads, Cooper-owned detection, contact deletion flagging
- **company-enrichment**  -  Website-first adaptive enrichment (Stages 1-3), re-enrichment mode (Step 0C)
- **segment-classification**  -  Qualification gates, exclusion list, cascade rules for segment changes
- **territory-manager**  -  State-to-owner mapping, contact owner cascade, deal protection awareness
- **account-sourcing**  -  CRM gap analysis, search query generation, source evaluation
- **import-processor**  -  HubSpot value mapping transforms (segment, sub-segment, tier, confidence enums)
- **edge-case-researcher**  -  Second-pass investigation for excluded/uncertain accounts
- **contact-discovery**  -  Persona gap analysis (Mode 1), Apollo/LinkedIn hybrid fill (Mode 3), job change detection (Mode 4), bulk persona coverage (Mode 5)
- **pre-deletion-audit**  -  Duplicate detection, contact consolidation (reassociate to primary), 90-day activity preservation, `flagged_for_deletion` boolean writes on contacts, open-deal hard stop
- **weekly-signal-scan**  -  Job 8's core logic: 7-stage pipeline for weekly signal scraping, `recent_news_or_trigger_event` field updates, rep-email generation with Excel attachment

---

## Run-time Invariants

These rules apply to every job, every run. Violating any of them is a bug.

### Timezone

All date math uses **America/New_York** (US Eastern). "Today" = current Eastern calendar date at run start. "Within the last 90 days" = 90 calendar days back from that Eastern date. "1st of month" / "1st of Jan/Apr/Jul/Oct" = Eastern date. HubSpot stores timestamps in UTC; convert HubSpot timestamps to ET before comparing to the thresholds above. Mixing timezones silently shifts month boundaries and activity windows off-by-one  -  never acceptable.

### Skip already-flagged companies in non-Job-7 jobs

Any company with `customer_segment = "Flagged for deletion"` is NOT touched by Jobs 1, 2, 3, 4, 5, or 6. Do not enrich, re-territory, persona-fill, or otherwise operate on flagged accounts. Only Job 7 (pre-deletion audit) handles them  -  and only to validate/adjust the flag or resolve associated contacts. This prevents waste (re-enriching records destined for archival) and prevents surprise writes on records humans have marked for removal.

### Customer protection (company-level)

Any company with ANY deal where `hs_is_closed_won = true` or `dealstage = closedwon` is a past or present customer and is protected from:
- Flag-for-deletion in Job 7 (hard stop; see pre-deletion-audit Step 1a)
- Segment downgrade from ICP to non-ICP in Job 2 (escalate to Tier 3 instead  -  human decides)
- Contact reassociation in Job 7 Mode A (never reassociate contacts away from a customer company)

If a customer company was briefly reclassified as non-ICP by a recent enrichment pass, that's a signal to re-evaluate the classification, not to delete the record.

### Error containment

A failure on one record must not abort the job. For every sub-skill operation (enrichment, classification, territory lookup, Apollo call, HubSpot write):
- Wrap the operation in a per-record try/except
- On failure: log record ID + operation + error message + Apollo/HubSpot request ID (if available)
- Continue to the next record
- Surface ALL failures in the daily run report's "Errors / API failures" section with enough detail to diagnose

Exceptions that DO abort the current job (not the whole run): Apollo plan exhausted (stop Apollo calls for the day), HubSpot auth token revoked (stop HubSpot calls), MCP connector disconnected. In those cases, write partial progress, move to the next job if it doesn't share the failed connector, and surface the connector failure prominently in the report.

### Default to Tier 3 when uncertain

When a decision involves ambiguous data  -  segment confidence = LOW or MANUAL_REVIEW, fuzzy dedup match below HIGH threshold, unclear activity signal (e.g., `notes_last_contacted` is exactly at the 90-day boundary), conflicting data sources (e.g., Apollo says one state, website says another)  -  default to Tier 3. Do not write. Surface for human review. "When in doubt, don't" is the rule.

### Idempotency

The routine is safe to run multiple times per day (manual test + scheduled, or re-run after partial failure). All writes must be deterministic based on current field state + input data. Never maintain in-memory state that affects outcomes across records. If run twice on the same day, the second run should produce a report that is mostly "All clean" because the first run already did the work.

### MaiaEdge-specific gotchas

These are repo-level conventions that do not match intuition. Skills reference them, but the orchestrator must respect them:

- **`account_tier` is INVERTED.** Tier 1 = highest priority, Tier 5 = lowest. When logic says "upgrade to Tier 1," it means make it MORE important (higher priority), not numerically higher.
- **MSP/Aggregator and Enterprise are BOTH ICP segments now.** `customer_segment = "MSP/Aggregator"` is the operator-segment ICP (telecom aggregators / TSDs / NaaS platform operators). `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is the **6th ICP segment as of 2026-05-11** - Multi-DC enterprises in financial services / healthcare systems / retail and distribution / outsourcing services with $1B+ revenue + in-house network engineering. Do not confuse the two. (Pre-2026-05-07 the MSP value was `Enterprise` - any stale reference to that should now be `MSP/Aggregator`. Pre-2026-05-11 `Enterprise-CustomerSegment` was non-ICP - any stale reference to that framing should now be ICP.)
- **AI Colo accounts** use `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. The old value `AI - Colocation Operator` is DEPRECATED and auto-migrated by Job 1 Mode 7.
- **No em dashes in customer-facing field values.** When writing `account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event` - use hyphens or restructure sentences. Never `-`. (`maiaedge_value_proposition` is retired 2026-05-26 - do not write it.)
- **Category descriptor: "Carrier infrastructure" only.** Never "IaaS," "NaaS," "platform," or any other term in customer-facing fields.

---

## Safety Tier System

Every auto-correction operates under one of three safety tiers.

### TIER 1  -  AUTO-FIX
Apply immediately. No HubSpot note is created  -  the field value change itself is the evidence, and the daily email report captures the full change log (see Change Log Format below).

- Fill missing `customer_segment` on unambiguous accounts (HIGH confidence from enrichment)
- Correct `hubspot_owner_id` based on HQ state mapping per territory-model.md (including Cooper-owned accounts with known state)
- Fill missing `company_sub_segment` when segment is known (per sub-segment assignment rules in hubspot-values.md)
- Set `last_enriched_date` after enrichment completes
- Normalize state abbreviations
- Fill `geographic_focus` from research
- Migrate deprecated `AI - Colocation Operator` → `Data Center Colo Provider` + `AI Signals - colo`
- Cascade contact `hubspot_owner_id` to match corrected company owner (per territory-manager Contact Owner Cascade)
- Sync contact `customer_segment` from company record
- Set contact `flagged_for_deletion = true` when pre-deletion-audit confirms: non-ICP company, zero activity in 90 days, no open-deal association
- Set contact `flagged_for_deletion = true` on clear-cut junk contacts via crm-hygiene Mode 11: hard-bounced emails (`hs_email_hard_bounce_reason_enum` populated), generic spam addresses (`noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@`), test/placeholder addresses (`test@test`, `@example.com`, `@yourdomain`, firstname+lastname both "test"), and contacts associated ONLY to `Flagged for deletion` companies with zero open deals
- Clear contact `flagged_for_deletion = false` when a previously flagged contact shows activity within 90 days
- Set company `customer_segment = "Flagged for deletion"` ONLY after pre-deletion-audit has fully resolved all associated contacts (reassociated, preserved, or flagged). The SAME write MUST also set `flagged_for_deletion_reason` (leading with a canonical reason code + colon + evidence sentence) per the Non-ICP Eviction Rule's "`flagged_for_deletion_reason` companion write" table below
- Clear company `flagged_for_deletion_reason` to empty whenever a company is moved OFF `Flagged for deletion` back into an active segment (reason code must never linger on an unflagged record)

### TIER 2  -  AUTO-FIX WITH FLAG
Apply the correction AND flag it in the run report for Cooper's review.

- Change `customer_segment` on accounts with NO open deals
- Enrich accounts with MEDIUM confidence classification
- Fill enrichment fields (`infrastructure_profile`, `fabric_provisioning_approach`, `account_tier`) from research
- Auto-create contacts from Apollo (verified email, LinkedIn validated per contact-discovery Mode 3)
- Auto-create replacement contacts for detected job changes (per contact-discovery Mode 4)
- Reassociate contacts from a duplicate company to the ICP primary (pre-deletion-audit Mode A) on HIGH confidence dedup match (exact domain or normalized-name exact match)
- Set contact `flagged_for_deletion = true` on heuristic-match junk via crm-hygiene Mode 11: contacts with no email/phone/mobilephone/company AND `createdate` > 180 days AND lifecycle in {blank, subscriber, lead} AND zero deals AND no sales-activity timestamp; duplicate-email records where a fresher sibling is retained

### TIER 3  -  HUMAN REVIEW ONLY
Do NOT auto-fix. Log as a pending action in the run report for Cooper.

- Merge duplicate records (never auto-merge companies themselves; pre-deletion-audit reassociates contacts only)
- Change `customer_segment`, `account_tier`, or create/modify contacts on accounts WITH open deals (deal protection  -  see below)
- Delete or archive any record (the Guardian never archives  -  it only writes flag fields; humans finalize archival)
- Override strategic/leadership-assigned owners (per territory-manager strategic exception detection)
- Create net-new company records from sourcing job (always hold for review)
- Any change where `segmentation_confidence` = LOW or MANUAL_REVIEW
- Contact creation from Apollo with unverified emails
- Pre-deletion-audit MEDIUM confidence dedup matches (fuzzy name match without domain match)  -  surface as merge suggestion
- Pre-deletion-audit Mode B edge case: non-ICP company with preserved active contacts and no ICP primary available for reassociation

### Deal Protection Rule

If an account has any open deal (dealstage is not `closedwon` or `closedlost`):
- **Segment changes, tier changes, and contact modifications** escalate from their normal tier → Tier 3
- **Owner/territory corrections remain Tier 1**  -  reps need correct routing regardless of deal status
- The deal's own `hubspot_owner_id` is NOT changed by Guardian corrections

All sub-skills reference this rule. When a sub-skill says "When running under CRM Guardian," it means these safety tiers and deal protection apply.

---

## Cascade Logic

When `customer_segment` changes (fill, correction, re-enrichment, or deprecated enum migration), execute the cascade defined in **segment-classification → Segment Change Cascade Rules**. That section is the single source of truth for cascade behavior.

Summary: re-derive sub-segment → tier → confidence → infrastructure_profile (if new research) → update last_enriched_date → sync segment to contacts. Cascade steps inherit the safety tier of the original segment change. Contact sync is always Tier 1.

---

## Model Selection per Routine

**Per Cooper directive 2026-04-28: all routines run on the current top Opus tier with the 1M context window (currently `claude-opus-4-8[1m]`).** The CRM is the single source of truth for the entire MaiaEdge GTM motion - every downstream output (cold emails, signal-scan rep DMs, persona fills, MEDDPICC writes, weekly call recap) cascades off the data quality these routines produce. The cost difference between Sonnet and Opus is dwarfed by the cost of a bad classification reaching production. The 1M context variant adds zero cost on small runs (you only pay for tokens used) but eliminates context-overflow risk on heavy runs (big import weeks for Routine 0, large transcript bundles for Weekly Call Recap, M&A-rich weeks for Weekly Signal Scan, full table scans for Routine 6). Opus 1M across the board.

| Routine | Model | Why Opus matters here |
|---|---|---|
| 0  -  Import Validator | **Opus 4.8** | Semantic name-vs-domain matching, 18-category hard-flag judgment, PARTNER_KEEP carveout - all reasoning-intensive |
| 1  -  Fresh Enrichment | **Opus 4.8** | Multi-page company research, segment qualification gates, edge-case detection, eviction-rule decision tree. Sonnet drops accuracy on borderline ICP cases (AI Colo vs standard, Network Op Track A vs B, NeoCloud vs Cloud GPU Reseller) |
| 2  -  Stale Re-Enrichment | **Opus 4.8** | Same depth as Routine 1 plus diff-detection and trigger-event recognition (M&A, funding, leadership changes). Eviction-rule path also requires nuanced PARTNER_KEEP decisions on existing `Other` records |
| 3  -  Duplicate Account Audit | **Opus 4.8** | Mostly mechanical pattern matching, but the divergent-name disambiguation (Wholesale vs AI Cloud vs Business unit) and customer-history-conflict adjudication benefit from deeper reasoning |
| 4  -  Flagged Consolidation | **Opus 4.8** | pre-deletion-audit Mode A consolidation requires identifying the correct ICP primary across the CRM - entity-resolution reasoning that Sonnet handles less reliably on edge cases |
| 5  -  Contact Dedup (Weekly) | **Opus 4.8** | Mode 11 protection filters and lifecycle-stage rules need careful reasoning to avoid false positives - Cooper would rather pay Opus than have a wrongly-flagged contact reach archival |
| 6  -  Territory & Hygiene | **Opus 4.8** | Field Resolution Ladder + drain-mode auto-fill cascades + Mode 11 contact flagging - multiple judgment calls per record, some with reversible/irreversible consequences |
| 7  -  Monthly Sourcing | **Opus 4.8** | Web-search candidate evaluation against ICP gates, dedup against existing CRM, segment routing |
| 8  -  Persona Fill (Weekly) | **Opus 4.8** | Apollo persona search + LinkedIn validation + suppression check + Tier 2 auto-create - quality of contact creates is high-stakes |
| 9  -  Job Changes (Quarterly) | **Opus 4.8** | Apollo + LinkedIn cross-check, departure detection, replacement persona routing |
| weekly-signal-scan | **Opus 4.8 (1M context)** | 7-stage pipeline with 5 parallel per-segment sub-stages, multi-source signal scoring with cross-source validation, segment cascade, account brief regeneration. Reads ~30+ catalog/skill/segment files per run - 1M context variant gives headroom |
| weekly-call-recap | **Opus 4.8** | Per-call MEDDPICC extraction with material-update guard, drift detection, deal-trajectory reads, PMF signal synthesis |
| weekly-market-news | **Opus 4.8** | Disabled by default; when enabled, multi-source synthesis with brand-voice constraint |

When the routine platform schedules a routine, the model setting in the platform takes precedence over this table - but the routine prompt includes a Model directive at the top to make the requirement visible to whoever configures it.

---

## Non-ICP Eviction Rule

**Goal:** Every record entering or refreshed by the enrichment pipeline must have its **actual domain fetched and verified**. Records confirmed as non-ICP that don't qualify as strategic Partner Target keepers get **flagged for deletion**, not classified as low-tier `Other` and left in the CRM. This stops outreach pollution at the source - a CRM full of "Tier 5 Other" records dilutes rep dashboards, persona-fill candidate pools, and signal-scan prioritization.

This is the canonical rule referenced by Routines 0, 1, 2, and any other routine that touches segment classification. Do not duplicate the logic - reference this section.

### Mandatory domain fetch

Every candidate record (fresh import, re-enrichment candidate, edge-case sweep) MUST have its domain root fetched (`web_fetch` on `https://[domain]`) before classification is finalized. Apollo data alone, name-only heuristics alone, or pre-score triage alone are NOT sufficient grounds for any classification write. Pre-score triage is a routing helper that decides depth-of-research; it does not substitute for actually verifying the domain content.

If `web_fetch` fails (DNS error, 5xx, parked page, dead domain) → route per the DEAD_DOMAIN bucket below.

### Decision tree (run after the domain fetch)

For each record, after fetching the domain root + (if needed) `/about` + `/contact`, classify into ONE of these buckets:

| Bucket | Definition | Action | Tier |
|---|---|---|---|
| **ICP** | Domain confirms a Colocation Operator, Fiber Operator, NeoCloud, Network Operator (Tier 1 / VNO), MSP/Aggregator, **OR Multi-DC Enterprise (4 sub-segments per `context/segments/enterprise.md`)** per the segment cheatsheets in `context/segments/`. Enterprise verdicts MUST pass the hard scale gate ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng + vertical match to Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services) - segment-classification owns the gate logic | Run full company-enrichment pipeline (Stages 1-3) → segment-classification → write enrichment fields | Tier 1 / 2 / 3 per confidence |
| **PARTNER_KEEP** | Domain confirms a strategic partner candidate per the keep-list below | Write `customer_segment = "Other"`, `account_tier = TIER_5`, populate `account_brief` with one line: `Partner Target keep: [reason] (eviction-rule applied [date])` | Tier 1 |
| **HARD_DELETE** | Domain confirms one of the hard-flag categories listed below | Write `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Hard junk / non-business: [discovered entity + category]"` (or `D1 disqualified (no reference value): ...` if the category is a D1 disqualifier with no reference value); populate `account_brief` with the discovered entity + category | Tier 2 (auto-flag + surface in Slack DM) |
| **DEAD_DOMAIN** | Domain returns parked/for-sale/no content/DNS-fail across all fetch attempts | Write `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Dead domain: [domain] returns parked/for-sale/no-content/DNS-fail (NOT a proxy block)"`, `account_brief = "Dead/parked domain ([domain]) - eviction-rule applied [date]"` | Tier 2 |
| **AMBIGUOUS** | Domain content unclear, partial business signals, or borderline category | Hold. Write nothing. Surface to Cooper's Slack DM + ledger | Tier 3 |

### `flagged_for_deletion_reason` companion write (MANDATORY on every eviction)

Every time any routine inheriting this rule sets `customer_segment = "Flagged for deletion"`, the SAME HubSpot `updateRequest` MUST also set `flagged_for_deletion_reason` (multi-line text on the Company object). The value leads with ONE of the 7 canonical reason codes, then a colon and one concrete sentence of evidence. **No em dashes - use a colon.** The scannable code lives in `flagged_for_deletion_reason`; the 2-4 sentence prose rationale stays in `account_brief` (unchanged - see "account_brief is pure prose" below). This is the canonical companion-write rule referenced by Routines 0, 1, 2, 4 and pre-deletion-audit - do not duplicate the code list elsewhere; reference this table.

| Reason code | When it applies |
|---|---|
| `Dead domain` | DNS NXDOMAIN / parked / for-sale / persistent destination 4xx-5xx (NOT a proxy block). Maps to the DEAD_DOMAIN bucket. |
| `Hard junk / non-business` | Non-business / hard-flag category (restaurant, church, school, personal site), junk TLD, spoofed-brand or test record. Maps to the HARD_DELETE bucket (non-business categories). |
| `D1 disqualified (no reference value)` | Matched a D1 global disqualifier (gov / academic / pure-SaaS / logistics / equipment-vendor, etc.) with NO competitive/partner reference value. |
| `No ICP fit` | Researched; no positive evidence for any of the 6 ICP sub-segments; not a partner/competitor reference. |
| `Duplicate (merged)` | Duplicate of an existing record; contacts reassociated to primary (cite primary name + record ID). pre-deletion-audit Mode A. |
| `Defunct / out of business` | Confirmed defunct / ceased ops / absorbed post-acquisition (cite the event). |
| `Stalled greenfield` | Greenfield record with no construction progress or signal in 18+ months; web-verified stalled. |

**Clear-on-exit:** if any path moves a record OFF `Flagged for deletion` back into an active segment, clear `flagged_for_deletion_reason` to empty in the same write. The reason code must never linger on a record that is no longer flagged. Full canonical spec: `context/hubspot/property-schema.md` §2.1.

### PARTNER_KEEP - strategic partner-target keep-list

A record is PARTNER_KEEP only if it falls into one of these specific categories AND the domain confirms it. When in doubt, route to AMBIGUOUS (Tier 3 hold), not PARTNER_KEEP - Cooper would rather review borderline cases than lose a potential partner.

| Category | Examples | Why kept |
|---|---|---|
| **Hyperscalers** | AWS, Microsoft Azure, Google Cloud, IBM Cloud, Oracle Cloud, Alibaba Cloud | Signal source + cloud on-ramp partners |
| **Major IT/Network OEMs** | Cisco, Juniper, Arista, Dell, HPE, Lenovo, Supermicro, NVIDIA, Broadcom | Equipment sold to telecoms; often joint-account opportunities |
| **Major SI / consulting firms** | Accenture, Deloitte, Capgemini, Infosys, TCS, Wipro, KPMG, IBM Services | Channel + co-sell opportunities into telecoms |
| **Major analyst / research firms** | Gartner, Forrester, IDC, TeleGeography, Omdia, Synergy Research | Research source + signal feed |
| **Cloud orchestration / interconnection partners** | Megaport, PacketFabric, Equinix Fabric, Console Connect, Aviatrix | Co-existence partners (channel routing per `context/sales/` notes) |
| **Named channel partners** | Datum (per `context/sales/` neocloud strategy), and any partner explicitly listed in MaiaEdge's partner ecosystem | Channel routing |

**Not on the keep-list = not PARTNER_KEEP.** Software vendors, IT MSPs that don't aggregate carriers, generic consulting firms, manufacturing companies, vendor/contractor businesses (fiber construction, ISP installer crews), and similar companies are NOT partner targets just because they're "tech-adjacent" - they go to HARD_DELETE.

### HARD_DELETE - confirmed non-ICP, non-partner categories

Auto-flag these for deletion at HIGH confidence (Tier 2 - applied + surfaced):

**Clear non-business categories** (also covered by Routine 0 first-pass):
- Restaurants / food service / hospitality
- Apparel / fashion / retail
- Churches / religious organizations / faith-based AV
- Schools / universities / educational institutions (unless verified research-network operator)
- Government tribal organizations / cultural orgs (unless they operate carrier infrastructure)
- Real estate / property management / brokerages
- Automotive manufacturers / trucking companies
- Consumer electronics distributors / retailers
- Blockchain / crypto / NFT projects (unless explicit NeoCloud Crypto-to-AI Pivot per `context/segments/neocloud.md`)
- Agriculture / farming / livestock
- Healthcare clinics / dental / medical practices
- Law firms / legal services
- Staffing / recruiting / certification orgs
- AV / intercom / production-AV vendors
- Construction / infrastructure CONTRACTORS (build for operators but don't operate)
- Personal services (hair, beauty, fitness)
- Spoofed brand domains
- Bathroom / plumbing fixtures

**Tech-adjacent but not partner-target categories:**
- Software / SaaS vendors not in the carrier-infrastructure space (e.g., Aegis Mobile compliance software, MNJ IT, Open Systems IT, Aristotle Unified Comms when it's helpdesk-MSP not telecom-aggregator)
- IT MSPs that fail the IT MSP Test (don't aggregate carrier circuits) - see `context/segments/msp-aggregator.md`
- Network construction contractors (texasfiberdesigngroup.com, GAC Enterprises) - they build infrastructure but don't operate it
- Generic consulting firms with no telecom/network practice
- Manufacturing companies with no telecom operations
- Media companies / broadcasters / publishers (FreeWheel ad-tech, Endeavor Business Media, Telemetro Reporta TV)
- Insurance / financial services consumers (BT Insurance Korea, GEICO when not procurement-side)

### Why the rule writes to Tier 2, not Tier 1

Auto-flag-for-deletion is reversible (Cooper can clear `customer_segment` back to empty in HubSpot if a flag was wrong) but consequential (the record drops out of all active routines). Tier 2 (applied + surfaced in Slack DM) is the right safety setting. Cooper sees every eviction in the daily routine reports and can spot-revert before bulk-archival.

### Idempotency

A record that has been HARD_DELETE'd in a prior run is `customer_segment = "Flagged for deletion"` already and is excluded from Routines 1, 2, and 6 by their trigger queries. Routine 4 owns the contact-consolidation work on flagged records. So the eviction rule is idempotent: a record can only be evicted once.

### account_brief is pure prose - NO routine attribution prefix

`account_brief` (and every other enriched narrative field - `recent_news_or_trigger_event`, `provisioning_landscape`) is pure prose describing what the entity IS. NO leading `[Routine N]` tag, NO leading `[YYYY-MM-DD]:` date prefix, NO bracketed metadata of any kind. The routine identity that wrote the field is recoverable from `last_enriched_date` + the on-disk per-run report + git history; the date is already structured in `last_enriched_date`. Tagging breaks rep-facing readability and bloats the field with audit metadata that has its own home.

On eviction paths (HARD_DELETE / DEAD_DOMAIN), the brief should describe the actual entity at the domain - what it does, scale if visible, why it falls in the [category] - followed by a single trailing clause noting that the record was flagged for deletion. The flag itself is structured by `customer_segment = "Flagged for deletion"`; the brief explains the WHO, not the routine machinery.

Audit trail of which routine touched what lives in the on-disk run report under `weekly-reports/YYYY-MM-DD/` + the per-run Slack DM, NOT inside `account_brief`.

---

## Cross-Routine Ledger

A single Slack canvas - `CRM Guardian - Open Items Ledger` - held in Cooper's self-DM is the shared accountability surface across all routines. The pre-split routines surfaced unactioned items (47 unmerged dupes, 9 hard-delete records, 5 Apollo persona candidates) in successive reports without a closure path. The ledger fixes that: each routine reads the canvas at start, drains its own previously-surfaced items first, then appends new Tier 3 holds at end.

### Canvas structure

```
# CRM Guardian Open Items - Updated [timestamp]

## Tier 3 Holds (need Cooper)
- [routine] [date_first_surfaced] [record_id] - [reason]
- ...

## Apollo Reveals Pending (Routine 8)
- [account] [persona_slot] [apollo_id] [date_first_surfaced]
- ...

## Hard-Delete Recommendations (Routine 0)
- [record_id] [domain] [discovered_entity] [date_first_surfaced]
- ...

## Cooper-Decided Divergent Dupes (Routine 3)
- [primary_id] vs [other_id] - [domain] - [recommendation] [date_first_surfaced]
- ...

## Stale (>30 days, Cooper decide or close)
- [...everything older than 30 days demoted here automatically]
```

### Routine contract (every routine, 0-9 + weekly-signal-scan)

1. **At run start (after the trigger query, before any writes):**
   - Call `slack_read_canvas` on the ledger canvas ID.
   - Filter to items belonging to THIS routine.
   - For each item: re-evaluate against current HubSpot state. If the underlying issue is now resolved (Cooper acted manually, the record was deleted, etc.), mark for removal from the ledger. If still open, mark as priority work for THIS run - these are the routine's first work items, ahead of new candidates.
2. **At run end (after writes complete):**
   - For every Tier 3 hold this routine produced this run: append to the ledger under the appropriate section with `[YYYY-MM-DD]` as `date_first_surfaced` (only for new items - items already in the ledger keep their original surface date).
   - Items the routine resolved this run: remove from the ledger.
   - Auto-cleanup: any item whose `date_first_surfaced` is more than 30 days old gets demoted to the "Stale" section. Don't delete - Cooper still needs visibility on long-tail holds, but they shouldn't clog the active sections.
   - Call `slack_update_canvas` to persist.

### Canvas ID

**Canvas ID: `F0B0AFSB9LN`** (seeded 2026-04-28 by Cooper).
**URL:** `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`

Canvas structure (as scaffolded):
- **Active routines table** - one row per routine, with `_name TBD_` placeholders for routines not yet named.
- **Status emoji conventions** - single source of truth for what each emoji means (`:large_green_circle:` HEALTHY, `:large_yellow_circle:` DEGRADED, `:red_circle:` BLOCKED, etc.). Routines must read this section and use the existing emojis - do NOT invent new ones.
- **Tier 3 open items** - append-only across runs, organized by routine and `date_first_surfaced`.
- **Run log** (append-only, one row per run): `| YYYY-MM-DD | <routine name> | <status emoji> | <one-sentence summary> | <artifact links> |`

Run-time contract for every routine that reads/writes the canvas:
1. **At run start** - call `slack_read_canvas(canvas_id="F0B0AFSB9LN")`. Read the Active routines table, the status emoji conventions, and any Tier 3 items belonging to this routine. Drain prior holds: re-evaluate against current HubSpot state, resolve where Cooper acted manually since the prior run.
2. **At run end** - call `slack_update_canvas(canvas_id="F0B0AFSB9LN", ...)`. Append new Tier 3 holds from THIS run with `[YYYY-MM-DD]` as `date_first_surfaced`. Append exactly ONE row to the Run log table.
3. **Failure handling** - if `slack_read_canvas` returns an error (canvas archived, MCP disconnected, transient network failure), log the error in the routine's Slack DM Errors section and continue without ledger reads/writes. Do NOT abort the routine - the canvas is observability, not a hard dependency.

### Why a Slack canvas (not HubSpot custom object, not repo file)

- **Persistent + editable via MCP** (`slack_read_canvas`, `slack_update_canvas`) - fits the routines' write-only-via-MCP model.
- **Visible to Cooper** in the same Slack DM thread where routine reports already land - no context switch.
- **No new HubSpot schema** - adding a custom object would require schema management.
- **Searchable** by Slack search like the routine DMs themselves.

---

## Change Log Format

**Per-record HubSpot notes are NOT created by CRM Guardian.** The routine deliberately avoids writing notes to keep HubSpot activity feeds clean  -  especially on accounts where reps are actively working. Evidence of Guardian activity is visible without notes:

- **Job 2 touched this account:** `last_enriched_date` equals the run date (or recent).
- **Job 3 changed the owner:** `hubspot_owner_id` reflects the new owner; the state-to-owner mapping makes the correctness self-evident.
- **Job 1 migrated or filled a field:** Current field value speaks for itself (e.g., `customer_segment` is now `Data Center Colo Provider` instead of the deprecated `AI - Colocation Operator`).
- **Job 7 flagged a contact or consolidated a company:** `flagged_for_deletion = true` on the contact OR `customer_segment = "Flagged for deletion"` on the company tells the story.

### Report Delivery - quiet on success, ping only on hard failure

Routines do NOT DM Cooper a per-run debrief. The single ops surface is the **CRM Ops Daily Digest** (`cowork-scheduled-tasks/crm-ops-daily-digest/`, M-F 4:45pm CT), which reads HubSpot + the working-ledger canvas `F0B0AFSB9LN` and renders the whole fleet's day on a dashboard canvas + one short DM. Per-run self-DMs are therefore redundant and are removed.

Every routine's run record is:
1. **On-disk run report** at `weekly-reports/YYYY-MM-DD/<routine>/run-report.md` (or `audit.md`) - the structure below.
2. **One Run-log row** appended to canvas `F0B0AFSB9LN` with a status emoji from the canvas conventions.

**Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure** - HubSpot/Slack/Apollo MCP unreachable, an abort, a circuit-breaker pause, or zero records processed against a non-empty queue. Keep it to ONE line and still write the matching ❌/⚠️ Run-log row:
```
:red_circle: [Routine name] [FAILED / ABORTED / PAUSED] - [one-clause reason].
```
On a clean or partial-but-recoverable run, send nothing to Cooper - the disk report + Run-log row are the full record, and the digest surfaces the work.

**On-disk run report structure** (Slack mrkdwn or plain markdown; tables in fenced code blocks):
1. Hero: routine-specific counters (records scanned, Tier 1/2/3 counts, Apollo credits if any, health score if applicable)
2. Tier 2 + Tier 3 items, grouped, with record IDs / old→new values / reasons
3. Auto-fixed (Tier 1 summary counts)
4. Per-routine highlights (e.g., Mode A / Mode B for Routine 4)
5. Errors / API failures (if any)

**Failure-ping handling:** on `slack_send_message` error for the hard-failure ping, retry once (1s → 2s); if still failing, the on-disk report + the ❌ Run-log row are the fallback record.

### Per-Run: Summary Report
```
CRM GUARDIAN RUN REPORT  -  [Date] [Time]
==========================================
Job: [job name]
Records scanned: [N]
Issues found: [N]
Auto-fixed (Tier 1): [N]
Auto-fixed + flagged (Tier 2): [N]
Pending human review (Tier 3): [N]

TIER 1 CORRECTIONS (applied):
| Record | Field | Old Value | New Value | Reason |
|--------|-------|-----------|-----------|--------|

TIER 2 CORRECTIONS (applied + flagged for review):
| Record | Field | Old Value | New Value | Reason | Review Note |
|--------|-------|-----------|-----------|--------|-------------|

TIER 3 ESCALATIONS (NOT applied  -  needs Cooper):
| Record | Issue | Recommended Action | Reason |
|--------|-------|--------------------|--------|

HEALTH SCORE: [X]/100
```

---

## Master Cadence

CRM Guardian no longer runs as a single 2 AM master cycle. As of 2026-04-24 the work is split across **six independent routines** (daily maintenance) plus four retained jobs on their own schedules (weekly/monthly/quarterly).

### Core daily + weekly + monthly + quarterly routines (see Execution Model table above for prompt files)

| Routine | Time (ET) | Cadence | Days |
|---------|-----------|---------|------|
| 0  -  Import Validator | 12:30 AM | Daily | Every day |
| 6  -  Territory & Hygiene Sweep | 1:00 AM | Daily | Every day |
| 3  -  Duplicate Account Audit | 2:00 AM | Daily | Every day |
| 4  -  Flagged-for-Deletion Consolidation | 3:00 AM | Daily | Every day |
| 1  -  Fresh Account Enrichment | 6:00 AM | Daily | Every day |
| 2  -  Stale Account Re-Enrichment | 8:00 AM | Daily | Every day |
| 5  -  Contact Duplicate Flagging | 1:00 AM | Weekly | Sundays |
| 8  -  Weekly Persona Gap Fill | 9:00 AM | Weekly | Fridays |
| 7  -  Monthly New Account Sourcing | 9:00 AM | Monthly | 1st of each month |
| 9  -  Quarterly Job-Change Detection | 9:00 AM | Quarterly | 1st of Jan / Apr / Jul / Oct |
| 10 -  R-Tier-Audit (Drift Sweep) | 3:00 PM CT | Daily | M-F (Cowork-only; Apollo budget 0; 10% circuit breaker; widened to daily M-F 2026-05-21 per Cooper) |
| D7 -  Edge Case Resolution | Cooper-chosen | Weekly | Cooper-chosen day (Cowork-only; Apollo budget 0; per-run cap 30; 14-day max wall-clock per record) |

Each routine produces its own report and delivers it as a self-DM to Cooper via Slack with a distinct subject prefix so Slack search groups runs independently:
- `CRM Guardian - Import Validator -` (Routine 0)
- `CRM Guardian - Territory & Hygiene -` (Routine 6)
- `CRM Guardian - Duplicate Accounts -` (Routine 3)
- `CRM Guardian - Flagged Consolidation -` (Routine 4)
- `CRM Guardian - Fresh Enrichment -` (Routine 1)
- `CRM Guardian - Stale Re-Enrichment -` (Routine 2)
- `CRM Guardian - Contact Dedup (Weekly) -` (Routine 5)
- `CRM Guardian - Persona Fill (Weekly) -` (Routine 8)
- `CRM Guardian - Monthly Sourcing -` (Routine 7)
- `CRM Guardian - Job Changes (Quarterly) -` (Routine 9)

### Sibling routine on its own dedicated prompt

| Routine | Cadence | Runs On | Prompt file |
|-----|---------|---------|-------------|
| Weekly Signal Scan (Job 8) | Weekly | Mondays, staggered 8:30 AM - 2:30 PM CT *(Cowork)* | 7 tasks: `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise,aggregator}/prompt.md` (monolithic archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/`) |

This is conceptually Job 8 from the Job Definitions section but lives outside the numbered Routines 1-9 series because its skill (`weekly-signal-scan`) is a full standalone skill rather than a thin orchestrator over crm-hygiene/territory-manager modes. It was split 2026-05-28 into 6 per-segment Cowork tasks + 1 aggregator task (see CLAUDE.md "weekly-signal-scan" entry for full schedule). It still emits per-rep Slack DMs + Cooper audit DM and respects all the same safety tiers and invariants.

### Why the split

- **Fault isolation:** Apollo exhaustion in Routine 1 no longer halts Territory & Hygiene.
- **Independent scheduling:** routines can be rebalanced (e.g., move dedup earlier) without rewriting one monolithic prompt.
- **Session budgets:** each routine owns its own token / Apollo / HubSpot write caps.
- **Readable reports:** nine threaded Slack DM conversations instead of one omnibus daily digest.
- **Cadence-correct deployment:** Routines 7/8/9 fire only on their actual cadence (1st of month / Friday / quarter-start), instead of a daily prompt that internally cadence-gates and burns context every day.

The legacy `crm-guardian-prompt.md` is retained for manual "run everything at once" scenarios (e.g., post-incident backfills) and is NOT the production execution path. All scheduled CRM Guardian work flows through the nine numbered routines + the weekly-signal-scan sibling.

---

## Job Definitions

### JOB 1: DATA HYGIENE & GAP FILLING
**Cadence:** Daily
**Executes:** crm-hygiene Modes 2-10 in sequence, with Guardian safety tiers applied

1. Run crm-hygiene **Mode 2** (Duplicate Detection). All duplicates → Tier 3.
2. Run crm-hygiene **Mode 3** (Missing Critical Fields). For missing `customer_segment` with a domain: run company-enrichment Phase 1 to classify, then apply safety tier by confidence level. When segment fills, execute segment-classification cascade rules. For missing `state`: research via domain. For missing `hubspot_owner_id`: apply territory mapping if state known.
3. Run crm-hygiene **Mode 7** (Deprecated Enum Detection). Auto-migrate `AI - Colocation Operator`. Tier 1. Execute cascade.
4. Run crm-hygiene **Mode 10** (Cooper-Owned Account Detection). Auto-route routeable accounts per territory-model.md. Tier 1 if state known, Tier 3 if not. Cascade contact owners per territory-manager.
5. Run crm-hygiene **Mode 4** (Stale Record Identification). Report only.
6. Run crm-hygiene **Mode 5** (Incomplete Enrichment Tracking). Feed stale enrichment candidates into Job 2's re-enrichment pool.
7. Run crm-hygiene **Mode 9** (Stale Lead Detection). Report only.
8. Run crm-hygiene **Mode 8** (Contact-Level Hygiene). Auto-sync owner and segment mismatches. Tier 1. Orphaned contacts and missing emails → report only.
9. Run crm-hygiene **Mode 11** (Contact Deletion Flagging). Populate `flagged_for_deletion = true` on Contact records that meet clear-cut junk criteria so Cooper can bulk-delete from the HubSpot UI after reviewing the daily email report. Tier 1 auto-flag: hard bounces, generic spam patterns, test/placeholder addresses, contacts orphaned to flagged companies with zero open deals. Tier 2 auto-flag + review: no-contact-info aged-inactive contacts, duplicate-email siblings (keep freshest). Never-flag safety: any `hs_email_optout = true`, customer/opportunity lifecycle, any open-deal association, contacts < 30 days old with no contact info (Apollo-enrichment pipeline candidates - route to Job 5 instead). Full criteria per crm-hygiene Mode 11; Guardian only orchestrates + applies tiers.
10. Run crm-hygiene **Mode 6** (Data Completeness Analysis). Calculate health score.
11. Produce run report. Include a **"Contacts Flagged for Deletion"** section with Tier 1 count, Tier 2 count, and bulk-delete instruction pointer.

---

### JOB 2: NEW ACCOUNT ENRICHMENT + RE-ENRICHMENT
**Cadence:** Daily
**Executes:** company-enrichment (Stages 1-3 + Step 0C), segment-classification, import-processor value mappings, edge-case-researcher

**Routine 1 (Fresh Enrichment) covers the new-account half. Routine 2 (Stale Re-Enrichment) covers the re-enrichment half.** Both routines run on Cowork (per "Scheduled Routines - Platform Split" in CLAUDE.md). The canonical, current-state spec for R1 is `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` (redesigned 2026-05-06 - three-path workflow + 4-filter-group trigger query).

1. **New accounts (Routine 1, redesigned 2026-05-06):** Trigger query is FOUR logical filter groups (split as 5 HubSpot filterGroups because B's "at least one of sub_segment/tier blank" must be OR'd):
   - **A** - `customer_segment NOT_HAS_PROPERTY` (and not MaiaEdge own).
   - **B** - `customer_segment` IN one of 7 ICP values AND (`company_sub_segment NOT_HAS_PROPERTY` OR `account_tier NOT_HAS_PROPERTY`). Catches partial-fills.
   - **C** - `customer_segment EQ "Unknown"` (any confidence). "Unknown" is NEVER a deliberate Cooper-set state; routine resolves it.
   - **D** - `customer_segment IN ["Other", "Partner Target"]` AND `segmentation_confidence IN ["low_5069", "manual_review_required"]`. Re-evaluates low-confidence non-ICP records.
   - **Excluded:** `Other`/`Partner Target` with `high_90` confidence (deliberate, vetted - out of scope until R2's stale rotation).
   - **Pre-flight:** read canvas `F0B0AFSB9LN` for cross-routine Tier 3 holds (R0/R1/R2/R4) and exclude those HubSpot IDs client-side. Prevents same-day routine collisions.
   - **Cap:** dynamic - 100/run at ≤200 candidates, 125/run at 201-400, 150/run above 400 (with backlog-elevated DM hero flag).
   - **Three paths:**
     - **α - Full enrichment** (LIKELY_ICP keyword match in name/domain): web_search + web_fetch → company-enrichment Stages 1-3 → Apollo enrich → segment-classification → ICP Completeness Gate. Apollo cost ~1 credit/record. Cap 50/run (Apollo budget-bound).
     - **β - Re-research** (Filter Groups C, D, and B without LIKELY_ICP keywords): web_search-only re-classification, no Apollo unless mid-research promotion to LIKELY_ICP. Output domain ICP / Other / Partner Target / Flagged for deletion / explicit Tier 3 hold. NEVER outputs "Unknown". Cap 50/run.
     - **γ - Eviction-decision** (Filter Group A's LIKELY_NON_ICP and LIKELY_JUNK pools): web_search + MISDOMAIN check + Non-ICP Eviction Rule. No Apollo. Cap 50/run.
   - **Slot rebalancing:** if any path's pool < its allocated slots, roll unused slots to Path β (the highest-volume path on the new query).

2. **Re-enrichment candidates (Routine 2):** The ONLY trigger for re-enrichment is the company-level property `last_enriched_date`. Query HubSpot for companies where `last_enriched_date < [today - 120 days]` OR (`last_enriched_date` IS EMPTY AND `customer_segment` is populated). Do not use `hs_lastmodifieddate`, `createdate`, or any other recency signal as a proxy  -  `last_enriched_date` is the authoritative field and it is set to today (YYYY-MM-DD) at the end of every enrichment run that passes its Completeness Gate so the next rotation is predictable. Process in batches of 100 per day to keep the daily cycle bounded  -  tune the batch size based on total CRM account volume so the full stale pool rotates within the 120-day window (rough sizing: `daily_batch >= active_accounts / 120`). Apollo organization enrichment is the authoritative source for refreshed `state`, `country`, and firmographic data on every re-enrichment; territory owner is re-derived from the new state value.

3. For each company: execute company-enrichment full pipeline (Step 0C skips for re-enrichment, then Stages 1-3). Classify per segment-classification qualification gates. Map values per import-processor. **Differentiated Completeness Gates by classification outcome:** ICP Gate (full ICP write - segment + sub_segment + tier ≥ medium_7089 + state + country + owner + infra_profile + brief + value_prop), Non-ICP Gate (Other/Partner Target - tier_5 + high_90 + None Identified infra + brief), Eviction Gate (Flagged for deletion - high_90 + brief explaining reason), Tier 3 Hold Gate (NO segment/tier write; segmentation_confidence = manual_review_required + brief + canvas hold). `last_enriched_date` stamps ONLY on a passing ICP / Non-ICP / Eviction gate; Tier 3 holds keep the prior `last_enriched_date` so the record stays in the active pool.

4. Safety tiers by confidence: HIGH → Tier 1, MEDIUM → Tier 2, LOW/MANUAL_REVIEW → Tier 3 Hold Gate.
5. Deal protection applies per the rule above.
6. Run edge-case-researcher on any excluded/uncertain accounts before falling through to Tier 3.
7. **Apollo budget post-run (R1+R2):** required local write to `weekly-reports/apollo-budget.json`; `git commit/push` is **best-effort** with a 10s timeout. If `.git/index.lock` is held by a concurrent routine OR git exits non-zero, log "Git commit deferred (concurrent routine); JSON updated locally" in the Slack DM and continue. The Slack DM is the audit trail of record.
8. Produce run report.

---

### JOB 3: TERRITORY & OWNER VALIDATION
**Cadence:** Daily
**Executes:** territory-manager Mode 1 (Full Territory Audit) with Apollo state verification enabled

1. Execute territory-manager Mode 1 with Guardian safety tiers applied:
   - Mismatches with known state → Tier 1 auto-fix
   - Cooper-owned with known state → Tier 1 auto-fix
   - Strategic exceptions (per territory-manager detection rules) → skip
   - State blank OR HubSpot state stale (last_enriched_date 120+ days or blank) → Apollo state verification (step 6 of territory-manager Mode 1). Apollo is the authoritative source for `state` and `country`. HubSpot values are treated as cached copies  -  when they disagree with Apollo AND the account has not been enriched recently, Apollo wins.
   - State still blank after Apollo → Tier 3 hold
2. Execute territory-manager Contact Owner Cascade for every correction.
3. Deal protection: owner corrections on accounts with open deals remain Tier 1 (per territory-manager Deal Protection Awareness). State overwrites on deal-protected accounts become Tier 2 (applied + flagged).
4. Produce run report.

---

### JOB 4: NEW ACCOUNT SOURCING
**Cadence:** Monthly (1st of month only)
**Executes:** account-sourcing Mode 4 (CRM Gap Analysis) + Mode 2 (Search Query Generation), company-enrichment Phase 1 (quick check), segment-classification

1. Run account-sourcing Mode 4: CRM gap analysis focused on `Data Center Colo Provider` (AI Signals sub-segment) and `NeoCloud`.
2. Run account-sourcing Mode 2: generate search queries for priority segments.
3. `web_search` for candidate companies.
4. For each candidate: quick enrichment check (company-enrichment Phase 1 website read only), classify per segment-classification, dedup against HubSpot by domain.
5. Produce sourcing report with candidates. **Do NOT auto-create records.** All → Tier 3 (hold for Cooper's review).
6. Produce run report.

---

### JOB 5: CONTACT PERSONA GAP ANALYSIS + APOLLO/LINKEDIN HYBRID FILL
**Cadence:** Weekly (Fridays only)
**Executes:** contact-discovery Mode 1 (HubSpot audit) + Mode 3 (Apollo/LinkedIn Hybrid Fill)

1. Pull Tier 1 and Tier 2 companies from HubSpot.
2. For each company: run contact-discovery Mode 1 to identify persona gaps.
3. For each persona gap: execute contact-discovery Mode 3 (Apollo search → LinkedIn validation → create or flag for rep). All methodology per Mode 3  -  Guardian does not override the process, only applies safety tiers.
4. Created contacts → Tier 2. Deal-protected accounts → Tier 3. Remaining gaps → flag for reps per Mode 3's rep action format.
5. Produce run report per contact-discovery Mode 3 output format.

---

### JOB 6: CONTACT JOB CHANGE DETECTION
**Cadence:** Quarterly (1st of Jan / Apr / Jul / Oct)
**Executes:** contact-discovery Mode 4 (Job Change Detection)

1. Execute contact-discovery Mode 4 on contacts at Tier 1/2 accounts and accounts with open deals. All methodology per Mode 4  -  Guardian does not override the process, only applies safety tiers.
2. Departures → flagged in the daily email report (no HubSpot note). Replacements → Tier 2 auto-create with `hs_marketable_status = "false"`. Deal-protected accounts → Tier 3. Remaining gaps → flag for reps per Mode 4's rep action format.
3. Produce run report per contact-discovery Mode 4 output format.

---

### JOB 8: WEEKLY SIGNAL SCAN
**Cadence:** Weekly (Mondays only)
**Executes:** weekly-signal-scan (full 7-stage pipeline), with sub-skill calls to company-enrichment, territory-manager, account-brief, account-sourcing

1. Invoke `weekly-signal-scan` skill with full pipeline (Stages 1-7 per its SKILL.md).
2. Safety tier integration:
   - Stage 3 new-account creation: HIGH confidence → Tier 1 auto-create; MEDIUM → Tier 2 auto-create + flag; LOW / MANUAL_REVIEW → Tier 3 hold (surface in rep report's "possible new accounts - review needed" section, NOT auto-created).
   - Stage 5 field updates on deal-protected accounts (any open deal) → Tier 2 (applied + flagged).
   - Stage 5 LOW-confidence signals on Tier 1 accounts → Tier 3 hold, not written.
3. Apollo credit soft floor: if remaining credits < 20% of monthly allocation at Stage 3 entry, pause new-account enrichment for the run and defer to next Monday. Surface in Cooper's run report. Matched accounts (already in HubSpot) still get enriched since they're priority spend.
4. Account brief regeneration: the skill regenerates `account_brief` via the `account-brief` skill whenever either (a) brief is >30 days old, or (b) fresh research materially diverges from the existing brief. Apply Tier 1 (auto-write) on accounts without open deals, Tier 2 (auto-write + flag) on deal-protected accounts.
5. Delivery: 3 rep emails (Tim Lieto / Ken Cunningham / Tim Ziemer) + Cooper CC. Cooper also receives a consolidated run report folded into the daily Guardian email.
6. Idempotency: Job 8 is safe to re-trigger manually (e.g., for testing) but will NOT re-send rep emails outside the scheduled Monday AM run - manual triggers return report content only.

---

### JOB 7: PRE-DELETION AUDIT & CONTACT CONSOLIDATION
**Cadence:** Daily
**Executes:** pre-deletion-audit (full workflow)

This job is the single choke point through which every "mark this non-fit for deletion" decision must pass. It catches non-ICP accounts before they are flagged, reassociates salvageable contacts to ICP primaries when duplicates exist, and preserves any contact with activity in the last 90 days or an association to an open deal.

1. **Build the candidate set** by pulling companies that are:
   - Newly classified as non-ICP in the last 24h (Job 2 or segment-classification output where verdict was EXCLUDE)
   - Already `customer_segment = "Flagged for deletion"` but still have associated contacts unresolved (safety sweep for records that were flagged manually without the audit running)
   - Any company where `customer_segment` is in: `Enterprise-CustomerSegment`, `Partner Target`, `Other`, `Unknown` AND `last_enriched_date` > 30 days ago (periodic re-evaluation pool, batch of 25/day to keep the daily cycle bounded)
2. **Execute pre-deletion-audit** workflow Steps 0-5 on each candidate. All methodology per pre-deletion-audit SKILL.md  -  Guardian does not override the process, only applies safety tiers.
3. Open-deal hard stop → Tier 3. Mode A consolidation → Tier 1 field writes + Tier 2 reassociations. Mode B standalone flag with all-contacts-inactive → Tier 1. Mode B with preserved active contacts → Tier 3.
4. Every contact flag, reassociation, and company segment change is captured in the daily email report. No per-record HubSpot notes are created.
5. Produce run report per pre-deletion-audit output format; fold into the daily consolidated run report.

---

## Task Routing

| Trigger | Routine / Job |
|---------|---------------|
| "Run territory audit" / "Fix owners" / "Run hygiene" / "Clean the CRM" / "Health check" | Routine 6 (territory & hygiene sweep) |
| "Run duplicate audit" / "Check for duplicate accounts" / "Merge duplicates" | Routine 3 (duplicate account audit) |
| "Consolidate flagged contacts" / "Audit flagged accounts" / "Clean up flagged-for-deletion" | Routine 4 (flagged-for-deletion consolidation) |
| "Enrich new accounts" / "Enrich today's new companies" / "Fresh enrichment" | Routine 1 (fresh account enrichment) |
| "Re-enrich stale accounts" / "Run re-enrichment" / "Refresh the CRM" | Routine 2 (stale account re-enrichment) |
| "Flag duplicate contacts" / "Contact dedup" / "Weekly contact audit" | Routine 5 (contact duplicate flagging, weekly) |
| "Run CRM Guardian" / "Guardian run" / "Run everything" | Trigger ALL six daily routines in order (6 → 3 → 4 → 1 → 2) plus Routine 5 if Sunday; also run retained jobs whose cadence is due today |
| "Source new accounts" / "Find prospects" / "Sourcing report" | Job 4 (retained, monthly) |
| "Check persona gaps" / "Find contacts" / "Fill gaps" | Job 5 (retained, Fridays) |
| "Check job changes" / "Contact audit" / "Who left?" | Job 6 (retained, quarterly) |
| "Run weekly signal scan" / "Monday brief" / "Refresh news fields" / "Weekly prospect list" | Job 8 (retained, Mondays; preview-only outside the scheduled window) |
| "Show change log" / "What did Guardian do?" | Summarize the most recent routine emails (pull from the email archive  -  no per-record notes exist) |
| "Guardian status" | Report: per-routine last run date, pending Tier 3 items count, Apollo budget consumption trend |

---

## Operational Limits and Failure Handling

Real production routines hit API limits. The master cycle must degrade gracefully, not silently drop data.

### Apollo monthly budget - HARD CAP 6,000 credits/month

**Effective 2026-04-26: total Apollo consumption across ALL routines is capped at 6,000 credits per calendar month.** The cap is enforced at the routine level via per-routine sub-caps that mathematically sum below 6,000/month at full hit rate, plus a pre-flight budget check that every Apollo-consuming routine performs at run start.

**Per-routine sub-caps (ALL routines must respect these - see each routine's Caps & Budgets section):**

| Routine | Sub-cap | Monthly max | Steady-state burn |
|---|---|---|---|
| Routine 0 (Import Validator) | 0 (Apollo-free, website-only) | 0 | 0 |
| Routine 1 (Fresh Enrichment) | 50 credits/run × 5 runs/week (Path α only; β and γ are Apollo-free) | ~1,000 | ~1,000 |
| Routine 2 (Stale Re-Enrichment) | 30 credits/run × 5 runs/week, ICP+reclassify-only via pre-score | ~600 | ~600 |
| Routine 6 (Territory & Hygiene) | 5 Apollo state-verifications/run × 5 runs/week | ~100 | ~100 |
| Routine 8 (Persona Fill, Fri) | 175 credits/week | ~750 | ~750 |
| Routine 9 (Job Changes, quarterly) | spare-capacity (up to 750/quarter) | 250 | 250 |
| weekly-signal-scan (Mon) | 250 credits/week | ~1,075 | ~1,075 |
| **Steady-state weekly draw (R1+R2+R6+R8+SS)** | **850 credits/week** | **~3,650/month** | **~3,650** |

The 6,000/month ceiling leaves ~2,350 credits/month of headroom for ad-hoc enrichment, conference prep, and surge weeks. **The 850-credit weekly hard cap on routines is the throughput lever** - enforced via `weekly-reports/apollo-budget.json` per `routines/_shared/apollo-weekly-budget-spec.md`. R1's 50/run sub-cap (raised from 30/run on 2026-05-06 alongside the trigger-query redesign) lets Path α process up to 50 LIKELY_ICP records per run while Path β and Path γ (re-research and eviction) consume zero Apollo and run uncapped within the dynamic record cap. The combined design enables draining 500-record import spikes in ~3-4 days at the 150/run elevated cap.

**Pre-flight monthly budget check (mandatory for every Apollo-consuming routine):**

At run start, before any Apollo call, every routine MUST:

1. Call `apollo_users_api_profile` (or equivalent budget-introspection endpoint) to fetch the current month's credit consumption.
2. Compute `remaining = 6000 - consumed_this_month`.
3. Compute `planned_for_this_run` (the routine's worst-case Apollo burn for this run, e.g. 50 credits for Routine 1 at full cap, 250 for Routine 8 first-run, etc.).
4. If `planned_for_this_run > remaining`: scale down the run to `remaining` credits worth of work, prioritized per the routine's priority rules, and surface in the Slack DM as "Apollo monthly budget cap reached - N items deferred to next month / next run."
5. If `remaining <= 50` (near zero): defer the entire run with a one-line Slack DM "Apollo monthly budget exhausted - routine deferred until next billing cycle."

**Priority ordering on capped scans (Routines 8, 9):**
- Routine 9: open-deal contacts always covered first; then Tier 1 contacts; then Tier 2 round-robin (oldest-Apollo-checked first). Full base cycles in ~5 quarters at the 750-credits/quarter cap.
- Routine 8: Tier 1 accounts before Tier 2; within each tier, oldest-persona-audited first.

**Why 6,000/month:** matches the user's Apollo plan tier ceiling. Going above triggers overage charges; this cap keeps spend deterministic.

### Apollo per-run credit exhaustion (within-month rate limits)

- **Per-run rate limits:** Apollo returns HTTP 429 or an error message containing `rate_limit`, `credit_exhausted`, `quota_exceeded`, or `insufficient_credits`. If any of these appear:
  1. Stop calling Apollo for the remainder of this run. Do not retry.
  2. Write whatever has been enriched so far to HubSpot (partial-run completion is fine  -  the daily cadence will resume tomorrow).
  3. Mark the remaining Job 2 re-enrichment batch as "deferred  -  Apollo credits exhausted; will retry next run."
  4. Include an explicit section in the run report:
     ```
     ⚠ APOLLO CREDITS EXHAUSTED
     Completed: [N] of [M] planned enrichments
     Deferred: [M - N] companies (will process next run)
     Recommendation: Check Apollo plan tier or reduce daily_batch in SKILL.md
     ```
- **Plan-aware batching:** If Cooper reports Apollo credits are regularly hitting the ceiling, reduce the Job 2 `daily_batch` value in the SKILL so the routine stays under budget even at worst-case overhead. Document the actual ceiling in the run report.

### HubSpot API rate limits

HubSpot's standard rate limits: 100 requests per 10 seconds, 250,000 requests per day (Professional) or 500,000 (Enterprise). A full-day Guardian run on a 6000-account CRM reaches ~2,000-3,000 requests (pagination + per-record writes  -  per-record notes are NOT created). Comfortable under the daily limit, but the burst limit (100/10s) is easy to hit during pagination.

- **Batching + backoff required:** When paginating through companies or contacts, respect the page-per-second rhythm (100 records per page, one page per second minimum). When writing (updates, notes), batch no more than 10 writes per second and add exponential backoff (1s → 2s → 4s) on any HTTP 429 response.
- **Bulk operations preferred:** Where HubSpot MCP exposes batch endpoints (e.g., batch update, batch note create), prefer them over sequential writes. Reduces request count 10x.
- **429 handling:** On rate-limit response, pause 10 seconds and retry the same request. If three consecutive 429s on the same operation → log as a transient failure, skip to next operation, include in run report.
- **Dead-letter surface:** Any write that fails after retries lands in a "HubSpot write failures" section of the run report with `record_id, operation, error`. Cooper can manually re-apply or investigate.

### Partial-run safety

A run that fails halfway through must not leave the CRM in an inconsistent state. Every write is standalone  -  no transactions across records. If Job 2 halts after enriching 37 of 50 companies, those 37 have their `last_enriched_date` set to today and won't reappear in tomorrow's pool. The unprocessed 13 stay at their prior `last_enriched_date` and will be the first picked up tomorrow.

Never skip writing `last_enriched_date` after a successful enrichment  -  it's the idempotency key for the whole re-enrichment cadence.

---

## MCP Requirements

### HubSpot MCP
- `search_crm_objects`  -  search companies, contacts, deals by property filters
- `get_object`  -  read individual records with all properties
- `update_object`  -  write field corrections to company/contact records
- `create_object`  -  create new contact records from Apollo data
- *(not used - per-record notes are intentionally skipped; see Change Log Format)*
- `get_associations`  -  get contacts associated with a company, deals associated with a company

### Apollo MCP
- `apollo_organizations_enrich`  -  authoritative source for HQ `state`, `country`, industry, employee count, revenue, founded year, funding. Called on every new-account enrichment (Job 2), every re-enrichment (Job 2), and every territory state verification (Job 3) where the HubSpot value is blank or stale.
- Search people by company + title + seniority (Job 5 persona fill)
- Search people by email (Job 6 job change detection)
- Filter by email verification status (verified only)
- Read contact details: name, title, email, phone, LinkedIn URL

### Web Tools
- `web_search`  -  enrichment research, sourcing candidate discovery
- `web_fetch`  -  company website reads, LinkedIn profile validation

### Slack MCP (report delivery)
- `slack_send_message`  -  post the routine report as a self-DM to `channel_id = U0A24D9RJLS` (Cooper's Slack user ID). Workspace `maia-edge.slack.com`.
- `slack_send_message` with `thread_ts`  -  threaded overflow replies for reports that exceed Slack's 5,000-char-per-text-element limit (Routine 4 first-run drain is the likely case).
- Other Slack MCP tools (search, read) are not used by CRM Guardian  -  delivery is write-only.

---

## Skill Chain

- **Triggers:** company-enrichment (re-enrichment of stale accounts), contact-discovery (persona gap fills), territory-manager (owner corrections), segment-classification (segment cascades)
- **References:** crm-hygiene (audit logic), import-processor (HubSpot enum values)
