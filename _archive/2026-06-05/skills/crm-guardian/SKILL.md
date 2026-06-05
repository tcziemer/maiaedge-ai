---
name: crm-guardian
description: "MaiaEdge CRM Guardian  -  autonomous CRM maintenance orchestrator, split into nine independent routines (territory & hygiene, duplicate account audit, flagged-for-deletion consolidation, fresh enrichment, stale re-enrichment, contact duplicate flagging, persona gap fill, monthly account sourcing, quarterly job-change detection) plus the sibling weekly-signal-scan. Writes corrections to HubSpot via MCP and manages contacts via Apollo MCP. Per-routine Slack DM is the audit trail. Use when asked to run CRM guardian, check CRM health, auto-fix CRM issues, run territory corrections, enrich new or stale accounts, audit accounts proposed for deletion, consolidate duplicate contacts, source new prospects, fill persona gaps, detect job changes, or review the CRM change log."
---

# MaiaEdge CRM Guardian

## Purpose

CRM Guardian is the autonomous maintenance layer for MaiaEdge's HubSpot CRM. It writes back to HubSpot and creates contacts via Apollo under a three-tier safety system: most corrections are fully automatic (Tier 1), some are applied but flagged for Cooper's review (Tier 2), and high-risk changes require human approval (Tier 3).

**Architecture:** CRM Guardian is orchestration-only. It defines WHAT to run, WHEN, and at what safety tier. The sub-skills define HOW. Each sub-skill is the single source of truth for its domain logic. CRM Guardian never duplicates sub-skill logic  -  it references it.

**Execution model: 10 independent routines, scheduled separately.** The previous monolithic "run all jobs at 2 AM" master cycle has been split into ten routines (Routine 0 added 2026-04-27), each with its own schedule, scope, session budget, and report. Failures in one routine do not block the others. Each routine is defined by its own prompt file in `Claude routine prompts/`. The routines reference this SKILL.md for shared invariants, safety tiers, sub-skill domain logic, and the Cross-Routine Ledger — but the scheduling boundary is the routine, not the job.

| # | Routine | Cadence | Prompt file | Goal |
|---|---------|---------|-------------|------|
| 0 | Import Validator | Daily, 12:30 AM ET | `crm-guardian-routine-0-import-validator.md` | Validate name vs. domain on records imported in the last 24h; auto-rename mismatches, auto-flag hard-category junk (restaurants, apparel, churches, etc.) before enrichment wastes credits |
| 1 | Fresh Account Enrichment | Daily, 6:00 AM ET | `crm-guardian-routine-1-fresh-enrichment.md` | Pre-score triage → enrich blank-segment ICP candidates (50/day Apollo cap), fast-classify non-ICP without Apollo |
| 2 | Stale Account Re-Enrichment | Daily, 8:00 AM ET | `crm-guardian-routine-2-stale-reenrichment.md` | Pre-score triage → full re-enrichment of ICP only; light-touch idempotency bump on Other / Partner Target / non-ICP records |
| 3 | Duplicate Account Audit | Daily, 2:00 AM ET | `crm-guardian-routine-3-duplicate-accounts.md` | Detect company duplicates, reassociate contacts, flag losers |
| 4 | Flagged-for-Deletion Consolidation | Daily, 3:00 AM ET | `crm-guardian-routine-4-flagged-consolidation.md` | Resolve contacts on flagged companies (preserve + reassociate, else flag) |
| 5 | Contact Duplicate Flagging | Weekly, Sun 1:00 AM ET | `crm-guardian-routine-5-contact-dedup.md` | Flag exact-email contact duplicates |
| 6 | Territory & Hygiene Sweep | Daily, 1:00 AM ET | `crm-guardian-routine-6-territory-hygiene.md` | Territory audit, enum migration, contact owner cascade, Mode 11 junk flags, **drain mode** for stale NEW leads (1000/run) + orphan contacts (300/run) + missing tier/sub-segment cascades (650/run combined) |
| 7 | Monthly New Account Sourcing | Monthly, 1st of month 9:00 AM ET | `crm-guardian-routine-7-monthly-sourcing.md` | account-sourcing CRM gap analysis + web search; surfaces Tier 3 candidates only (no auto-create) |
| 8 | Weekly Persona Gap Fill | Weekly, Fri 9:00 AM ET | `crm-guardian-routine-8-weekly-persona-fill.md` | Audit Tier 1+2 accounts for persona gaps; **auto-create via Apollo two-step (search → reveal → LinkedIn validate)** at Tier 2 |
| 9 | Quarterly Job-Change Detection | Quarterly, 1st of Jan/Apr/Jul/Oct 9:00 AM ET | `crm-guardian-routine-9-quarterly-job-changes.md` | Apollo + LinkedIn cross-check on Tier 1+2 + open-deal contacts; surface departures, auto-create verified replacements at Tier 2 |

**Daily run order:** **0 (12:30 AM) → 6 (1 AM) → 3 (2 AM) → 4 (3 AM) → 1 (6 AM) → 2 (8 AM).** Import validation FIRST so the day's bad imports get killed before territory verifies them and before enrichment burns Apollo credits on them. Territory next so downstream routines see correct owners; dedup before enrichment so Apollo credits don't get burned on duplicates; flagged-cleanup before enrichment so contacts land on the correct primary; fresh + stale enrichment consume Apollo budget last. Routines 7, 8, 9 run at 9 AM ET on their own cadences (after the daily window closes), and the sibling weekly-signal-scan runs Mon 10 UTC.

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
- (Sibling routine, not numbered) ↔ Job 8 (weekly signal scan, Mondays — its own prompt file `weekly-signal-scan-prompt.md`)

**All 8 jobs are now split into independent routines.** The legacy `crm-guardian-prompt.md` monolithic prompt is kept in the repo for manual "run everything at once" backfill scenarios but is no longer the production execution path. The Job Definitions section below remains the canonical domain-logic reference for all eight jobs; the routine prompts reference these definitions rather than redefining them.

## Reference Files

**HubSpot schemas:** property-schema.md, hubspot-values.md, contact-schema.md, deals-schema.md, territory-model.md, poc-schema.md

**Core:** icp-playbook.md, segment-qualification.md, maiaedge-101.md

**Segments:** colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md

**Enrichment:** sourcing-reference-guide.md, research-routes.md, output-schemas.md

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
- **`customer_segment` value `Enterprise` is legacy naming for MSP/Aggregator**, NOT enterprise consumer. Enterprise consumers use `Enterprise-CustomerSegment` (which is non-ICP). Do not re-classify MSPs as something else to "fix" the naming.
- **AI Colo accounts** use `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. The old value `AI - Colocation Operator` is DEPRECATED and auto-migrated by Job 1 Mode 7.
- **No em dashes in customer-facing field values.** When writing `account_brief`, `maiaedge_value_proposition`, `provisioning_landscape`, `recent_news_or_trigger_event`  -  use hyphens or restructure sentences. Never `—`.
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
- Set company `customer_segment = "Flagged for deletion"` ONLY after pre-deletion-audit has fully resolved all associated contacts (reassociated, preserved, or flagged)

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

**Per Cooper directive 2026-04-28: All routines run on Opus 4.7 with 1M context window (`claude-opus-4-7[1m]`).** The CRM is the single source of truth for the entire MaiaEdge GTM motion — every downstream output (cold emails, signal-scan rep DMs, persona fills, MEDDPICC writes, weekly call recap) cascades off the data quality these routines produce. The cost difference between Sonnet and Opus is dwarfed by the cost of a bad classification reaching production. The 1M context variant adds zero cost on small runs (you only pay for tokens used) but eliminates context-overflow risk on heavy runs (big import weeks for Routine 0, large transcript bundles for Weekly Call Recap, M&A-rich weeks for Weekly Signal Scan, full table scans for Routine 6). Opus 1M across the board.

| Routine | Model | Why Opus matters here |
|---|---|---|
| 0  -  Import Validator | **Opus 4.7** | Semantic name-vs-domain matching, 18-category hard-flag judgment, PARTNER_KEEP carveout — all reasoning-intensive |
| 1  -  Fresh Enrichment | **Opus 4.7** | Multi-page company research, segment qualification gates, edge-case detection, eviction-rule decision tree. Sonnet drops accuracy on borderline ICP cases (AI Colo vs standard, Network Op Track A vs B, NeoCloud vs Cloud GPU Reseller) |
| 2  -  Stale Re-Enrichment | **Opus 4.7** | Same depth as Routine 1 plus diff-detection and trigger-event recognition (M&A, funding, leadership changes). Eviction-rule path also requires nuanced PARTNER_KEEP decisions on existing `Other` records |
| 3  -  Duplicate Account Audit | **Opus 4.7** | Mostly mechanical pattern matching, but the divergent-name disambiguation (Wholesale vs AI Cloud vs Business unit) and customer-history-conflict adjudication benefit from deeper reasoning |
| 4  -  Flagged Consolidation | **Opus 4.7** | pre-deletion-audit Mode A consolidation requires identifying the correct ICP primary across the CRM — entity-resolution reasoning that Sonnet handles less reliably on edge cases |
| 5  -  Contact Dedup (Weekly) | **Opus 4.7** | Mode 11 protection filters and lifecycle-stage rules need careful reasoning to avoid false positives — Cooper would rather pay Opus than have a wrongly-flagged contact reach archival |
| 6  -  Territory & Hygiene | **Opus 4.7** | Field Resolution Ladder + drain-mode auto-fill cascades + Mode 11 contact flagging — multiple judgment calls per record, some with reversible/irreversible consequences |
| 7  -  Monthly Sourcing | **Opus 4.7** | Web-search candidate evaluation against ICP gates, dedup against existing CRM, segment routing |
| 8  -  Persona Fill (Weekly) | **Opus 4.7** | Apollo persona search + LinkedIn validation + suppression check + Tier 2 auto-create — quality of contact creates is high-stakes |
| 9  -  Job Changes (Quarterly) | **Opus 4.7** | Apollo + LinkedIn cross-check, departure detection, replacement persona routing |
| weekly-signal-scan | **Opus 4.7 (1M context)** | 7-stage pipeline with 5 parallel per-segment sub-stages, multi-source signal scoring with cross-source validation, segment cascade, account brief regeneration. Reads ~30+ catalog/skill/segment files per run — 1M context variant gives headroom |
| weekly-call-recap | **Opus 4.7** | Per-call MEDDPICC extraction with material-update guard, drift detection, deal-trajectory reads, PMF signal synthesis |
| weekly-market-news | **Opus 4.7** | Disabled by default; when enabled, multi-source synthesis with brand-voice constraint |

When the routine platform schedules a routine, the model setting in the platform takes precedence over this table — but the routine prompt includes a Model directive at the top to make the requirement visible to whoever configures it.

---

## Non-ICP Eviction Rule

**Goal:** Every record entering or refreshed by the enrichment pipeline must have its **actual domain fetched and verified**. Records confirmed as non-ICP that don't qualify as strategic Partner Target keepers get **flagged for deletion**, not classified as low-tier `Other` and left in the CRM. This stops outreach pollution at the source — a CRM full of "Tier 5 Other" records dilutes rep dashboards, persona-fill candidate pools, and signal-scan prioritization.

This is the canonical rule referenced by Routines 0, 1, 2, and any other routine that touches segment classification. Do not duplicate the logic — reference this section.

### Mandatory domain fetch

Every candidate record (fresh import, re-enrichment candidate, edge-case sweep) MUST have its domain root fetched (`web_fetch` on `https://[domain]`) before classification is finalized. Apollo data alone, name-only heuristics alone, or pre-score triage alone are NOT sufficient grounds for any classification write. Pre-score triage is a routing helper that decides depth-of-research; it does not substitute for actually verifying the domain content.

If `web_fetch` fails (DNS error, 5xx, parked page, dead domain) → route per the DEAD_DOMAIN bucket below.

### Decision tree (run after the domain fetch)

For each record, after fetching the domain root + (if needed) `/about` + `/contact`, classify into ONE of these buckets:

| Bucket | Definition | Action | Tier |
|---|---|---|---|
| **ICP** | Domain confirms a Colocation Operator, Fiber Operator, NeoCloud, Network Operator (Tier 1 / VNO), or MSP/Aggregator per the segment cheatsheets in `context/segments/` | Run full company-enrichment pipeline (Stages 1-3) → segment-classification → write enrichment fields | Tier 1 / 2 / 3 per confidence |
| **PARTNER_KEEP** | Domain confirms a strategic partner candidate per the keep-list below | Write `customer_segment = "Other"`, `account_tier = TIER_5`, populate `account_brief` with one line: `Partner Target keep: [reason] (eviction-rule applied [date])` | Tier 1 |
| **HARD_DELETE** | Domain confirms one of the hard-flag categories listed below | Write `customer_segment = "Flagged for deletion"`, populate `account_brief` with the discovered entity + category | Tier 2 (auto-flag + surface in Slack DM) |
| **DEAD_DOMAIN** | Domain returns parked/for-sale/no content/DNS-fail across all fetch attempts | Write `customer_segment = "Flagged for deletion"`, `account_brief = "Dead/parked domain ([domain]) — eviction-rule applied [date]"` | Tier 2 |
| **AMBIGUOUS** | Domain content unclear, partial business signals, or borderline category | Hold. Write nothing. Surface to Cooper's Slack DM + ledger | Tier 3 |

### PARTNER_KEEP — strategic partner-target keep-list

A record is PARTNER_KEEP only if it falls into one of these specific categories AND the domain confirms it. When in doubt, route to AMBIGUOUS (Tier 3 hold), not PARTNER_KEEP — Cooper would rather review borderline cases than lose a potential partner.

| Category | Examples | Why kept |
|---|---|---|
| **Hyperscalers** | AWS, Microsoft Azure, Google Cloud, IBM Cloud, Oracle Cloud, Alibaba Cloud | Signal source + cloud on-ramp partners |
| **Major IT/Network OEMs** | Cisco, Juniper, Arista, Dell, HPE, Lenovo, Supermicro, NVIDIA, Broadcom | Equipment sold to telecoms; often joint-account opportunities |
| **Major SI / consulting firms** | Accenture, Deloitte, Capgemini, Infosys, TCS, Wipro, KPMG, IBM Services | Channel + co-sell opportunities into telecoms |
| **Major analyst / research firms** | Gartner, Forrester, IDC, TeleGeography, Omdia, Synergy Research | Research source + signal feed |
| **Cloud orchestration / interconnection partners** | Megaport, PacketFabric, Equinix Fabric, Console Connect, Aviatrix | Co-existence partners (channel routing per `context/sales/` notes) |
| **Named channel partners** | Datum (per `context/sales/` neocloud strategy), and any partner explicitly listed in MaiaEdge's partner ecosystem | Channel routing |

**Not on the keep-list = not PARTNER_KEEP.** Software vendors, IT MSPs that don't aggregate carriers, generic consulting firms, manufacturing companies, vendor/contractor businesses (fiber construction, ISP installer crews), and similar companies are NOT partner targets just because they're "tech-adjacent" — they go to HARD_DELETE.

### HARD_DELETE — confirmed non-ICP, non-partner categories

Auto-flag these for deletion at HIGH confidence (Tier 2 — applied + surfaced):

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
- IT MSPs that fail the IT MSP Test (don't aggregate carrier circuits) — see `context/segments/msp-aggregator.md`
- Network construction contractors (texasfiberdesigngroup.com, GAC Enterprises) — they build infrastructure but don't operate it
- Generic consulting firms with no telecom/network practice
- Manufacturing companies with no telecom operations
- Media companies / broadcasters / publishers (FreeWheel ad-tech, Endeavor Business Media, Telemetro Reporta TV)
- Insurance / financial services consumers (BT Insurance Korea, GEICO when not procurement-side)

### Why the rule writes to Tier 2, not Tier 1

Auto-flag-for-deletion is reversible (Cooper can clear `customer_segment` back to empty in HubSpot if a flag was wrong) but consequential (the record drops out of all active routines). Tier 2 (applied + surfaced in Slack DM) is the right safety setting. Cooper sees every eviction in the daily routine reports and can spot-revert before bulk-archival.

### Idempotency

A record that has been HARD_DELETE'd in a prior run is `customer_segment = "Flagged for deletion"` already and is excluded from Routines 1, 2, and 6 by their trigger queries. Routine 4 owns the contact-consolidation work on flagged records. So the eviction rule is idempotent: a record can only be evicted once.

### Routine attribution in account_brief

Every eviction (HARD_DELETE or DEAD_DOMAIN) MUST write the `account_brief` field with a one-line attribution: `[Routine N] [YYYY-MM-DD]: Eviction rule applied — [discovered_entity / dead-domain] — [category if applicable]`. This is the audit trail Cooper uses when reviewing flags.

---

## Cross-Routine Ledger

A single Slack canvas — `CRM Guardian — Open Items Ledger` — held in Cooper's self-DM is the shared accountability surface across all routines. The pre-split routines surfaced unactioned items (47 unmerged dupes, 9 hard-delete records, 5 Apollo persona candidates) in successive reports without a closure path. The ledger fixes that: each routine reads the canvas at start, drains its own previously-surfaced items first, then appends new Tier 3 holds at end.

### Canvas structure

```
# CRM Guardian Open Items — Updated [timestamp]

## Tier 3 Holds (need Cooper)
- [routine] [date_first_surfaced] [record_id] — [reason]
- ...

## Apollo Reveals Pending (Routine 8)
- [account] [persona_slot] [apollo_id] [date_first_surfaced]
- ...

## Hard-Delete Recommendations (Routine 0)
- [record_id] [domain] [discovered_entity] [date_first_surfaced]
- ...

## Cooper-Decided Divergent Dupes (Routine 3)
- [primary_id] vs [other_id] — [domain] — [recommendation] [date_first_surfaced]
- ...

## Stale (>30 days, Cooper decide or close)
- [...everything older than 30 days demoted here automatically]
```

### Routine contract (every routine, 0-9 + weekly-signal-scan)

1. **At run start (after the trigger query, before any writes):**
   - Call `slack_read_canvas` on the ledger canvas ID.
   - Filter to items belonging to THIS routine.
   - For each item: re-evaluate against current HubSpot state. If the underlying issue is now resolved (Cooper acted manually, the record was deleted, etc.), mark for removal from the ledger. If still open, mark as priority work for THIS run — these are the routine's first work items, ahead of new candidates.
2. **At run end (after writes complete):**
   - For every Tier 3 hold this routine produced this run: append to the ledger under the appropriate section with `[YYYY-MM-DD]` as `date_first_surfaced` (only for new items — items already in the ledger keep their original surface date).
   - Items the routine resolved this run: remove from the ledger.
   - Auto-cleanup: any item whose `date_first_surfaced` is more than 30 days old gets demoted to the "Stale" section. Don't delete — Cooper still needs visibility on long-tail holds, but they shouldn't clog the active sections.
   - Call `slack_update_canvas` to persist.

### Canvas ID

**Canvas ID: `F0B0AFSB9LN`** (seeded 2026-04-28 by Cooper).
**URL:** `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`

Canvas structure (as scaffolded):
- **Active routines table** — one row per routine, with `_name TBD_` placeholders for routines not yet named.
- **Status emoji conventions** — single source of truth for what each emoji means (`:large_green_circle:` HEALTHY, `:large_yellow_circle:` DEGRADED, `:red_circle:` BLOCKED, etc.). Routines must read this section and use the existing emojis — do NOT invent new ones.
- **Tier 3 open items** — append-only across runs, organized by routine and `date_first_surfaced`.
- **Run log** (append-only, one row per run): `| YYYY-MM-DD | <routine name> | <status emoji> | <one-sentence summary> | <artifact links> |`

Run-time contract for every routine that reads/writes the canvas:
1. **At run start** — call `slack_read_canvas(canvas_id="F0B0AFSB9LN")`. Read the Active routines table, the status emoji conventions, and any Tier 3 items belonging to this routine. Drain prior holds: re-evaluate against current HubSpot state, resolve where Cooper acted manually since the prior run.
2. **At run end** — call `slack_update_canvas(canvas_id="F0B0AFSB9LN", ...)`. Append new Tier 3 holds from THIS run with `[YYYY-MM-DD]` as `date_first_surfaced`. Append exactly ONE row to the Run log table.
3. **Failure handling** — if `slack_read_canvas` returns an error (canvas archived, MCP disconnected, transient network failure), log the error in the routine's Slack DM Errors section and continue without ledger reads/writes. Do NOT abort the routine — the canvas is observability, not a hard dependency.

### Why a Slack canvas (not HubSpot custom object, not repo file)

- **Persistent + editable via MCP** (`slack_read_canvas`, `slack_update_canvas`) — fits the routines' write-only-via-MCP model.
- **Visible to Cooper** in the same Slack DM thread where routine reports already land — no context switch.
- **No new HubSpot schema** — adding a custom object would require schema management.
- **Searchable** by Slack search like the routine DMs themselves.

---

## Change Log Format

**Per-record HubSpot notes are NOT created by CRM Guardian.** The routine deliberately avoids writing notes to keep HubSpot activity feeds clean  -  especially on accounts where reps are actively working. Evidence of Guardian activity is visible without notes:

- **Job 2 touched this account:** `last_enriched_date` equals the run date (or recent).
- **Job 3 changed the owner:** `hubspot_owner_id` reflects the new owner; the state-to-owner mapping makes the correctness self-evident.
- **Job 1 migrated or filled a field:** Current field value speaks for itself (e.g., `customer_segment` is now `Data Center Colo Provider` instead of the deprecated `AI - Colocation Operator`).
- **Job 7 flagged a contact or consolidated a company:** `flagged_for_deletion = true` on the contact OR `customer_segment = "Flagged for deletion"` on the company tells the story.

The **single source of audit truth** is the daily consolidated email report (see Email Delivery below). Every Tier 1, Tier 2, and Tier 3 item across all jobs is listed there with record IDs, old/new values, and reasons. Keep the email archive  -  that's your history.

### Report Delivery — Slack DM (end of every routine run)

Each routine produces its own report and delivers it as a self-DM to Cooper via the Slack MCP. The previous Microsoft 365 / Outlook path is deprecated — no email delivery is wired up.

**Transport:** Slack MCP `slack_send_message` tool. Workspace: `maia-edge.slack.com`.

**Recipient:** `U0A24D9RJLS` (Cooper Kennedy's Slack user ID — DM to self). Pass this as `channel_id` to `slack_send_message`; Slack treats self-DMs as a normal DM channel.

**First line of message (acts as subject — use for consistent grouping):**
```
:emoji: *CRM Guardian — [routine name]* — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held
```
If both N and M are zero, use `All clean` in place of the counts. Per-routine emoji + prefix:
- `:warning: *CRM Guardian — Import Validator*` (Routine 0, 12:30 AM)
- `:broom: *CRM Guardian — Territory & Hygiene*` (Routine 6, 1 AM)
- `:busts_in_silhouette: *CRM Guardian — Duplicate Accounts*` (Routine 3, 2 AM)
- `:wastebasket: *CRM Guardian — Flagged Consolidation*` (Routine 4, 3 AM)
- `:wrench: *CRM Guardian — Fresh Enrichment*` (Routine 1, 6 AM)
- `:arrows_counterclockwise: *CRM Guardian — Stale Re-Enrichment*` (Routine 2, 8 AM)
- `:mag: *CRM Guardian — Contact Dedup (Weekly)*` (Routine 5, Sun 1 AM)

Slack search on the prefix groups all runs of a given routine into a single stream.

**Body format:** Slack mrkdwn. Use `**bold**` for section headings, `_italic_` for emphasis, `>` for blockquotes / callouts, triple-backtick fenced code blocks for tables (monospace preserves column alignment). Avoid HTML — Slack renders it as plain text.

**Body structure:**
1. Hero: routine-specific counters (records scanned, Tier 1/2/3 counts, Apollo credits if any, health score if applicable)
2. Needs your attention (Tier 2 + Tier 3, grouped, tables in code blocks)
3. Auto-fixed (Tier 1 summary counts)
4. Per-routine highlights (e.g., Mode A / Mode B for Routine 4)
5. Errors / API failures (if any)

**Size & threading:** 5,000-character limit per text element. If the report exceeds this (common on Routine 4 first-run drain), split into a hero + threaded replies (one thread per table) using `thread_ts` from the hero message. Overflow inside a thread keeps the DM clean.

**Failure handling:** on `slack_send_message` error, retry once with exponential backoff (1s → 2s). If still failing, log in the report's Errors section and rely on the routine-platform's fallback notification. No email fallback exists.

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

Each routine produces its own report and delivers it as a self-DM to Cooper via Slack with a distinct subject prefix so Slack search groups runs independently:
- `CRM Guardian — Import Validator —` (Routine 0)
- `CRM Guardian — Territory & Hygiene —` (Routine 6)
- `CRM Guardian — Duplicate Accounts —` (Routine 3)
- `CRM Guardian — Flagged Consolidation —` (Routine 4)
- `CRM Guardian — Fresh Enrichment —` (Routine 1)
- `CRM Guardian — Stale Re-Enrichment —` (Routine 2)
- `CRM Guardian — Contact Dedup (Weekly) —` (Routine 5)
- `CRM Guardian — Persona Fill (Weekly) —` (Routine 8)
- `CRM Guardian — Monthly Sourcing —` (Routine 7)
- `CRM Guardian — Job Changes (Quarterly) —` (Routine 9)

### Sibling routine on its own dedicated prompt

| Routine | Cadence | Runs On | Prompt file |
|-----|---------|---------|-------------|
| Weekly Signal Scan (Job 8) | Weekly | Mondays, 10:00 UTC (~5-6 AM ET) | `weekly-signal-scan-prompt.md` |

This is conceptually Job 8 from the Job Definitions section but lives outside the numbered Routines 1-9 series because its skill (`weekly-signal-scan`) is a full standalone skill rather than a thin orchestrator over crm-hygiene/territory-manager modes. It still emits its own per-rep Slack DMs + Cooper audit DM and respects all the same safety tiers and invariants.

**Note on Job 8 timing:** weekly-signal-scan must complete by Monday 7:00 AM ET for rep delivery. Since the daily routines 6/3/4 finish by ~3 AM, Job 8 has a clear 3-7 AM window. On a delayed Monday run, Slack delivery may slip — the routine surfaces this in its Cooper run report.

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
9. Run crm-hygiene **Mode 11** (Contact Deletion Flagging). Populate `flagged_for_deletion = true` on Contact records that meet clear-cut junk criteria so Cooper can bulk-delete from the HubSpot UI after reviewing the daily email report. Tier 1 auto-flag: hard bounces, generic spam patterns, test/placeholder addresses, contacts orphaned to flagged companies with zero open deals. Tier 2 auto-flag + review: no-contact-info aged-inactive contacts, duplicate-email siblings (keep freshest). Never-flag safety: any `hs_email_optout = true`, customer/opportunity lifecycle, any open-deal association, contacts < 30 days old with no contact info (Apollo-enrichment pipeline candidates — route to Job 5 instead). Full criteria per crm-hygiene Mode 11; Guardian only orchestrates + applies tiers.
10. Run crm-hygiene **Mode 6** (Data Completeness Analysis). Calculate health score.
11. Produce run report. Include a **"Contacts Flagged for Deletion"** section with Tier 1 count, Tier 2 count, and bulk-delete instruction pointer.

---

### JOB 2: NEW ACCOUNT ENRICHMENT + RE-ENRICHMENT
**Cadence:** Daily
**Executes:** company-enrichment (Stages 1-3 + Step 0C), segment-classification, import-processor value mappings, edge-case-researcher

1. **New accounts:** Query HubSpot for companies where `createdate` is within the last 24 hours AND (`customer_segment` is blank OR `company_sub_segment` is blank OR `account_tier` is blank). Daily cadence means the window is always "since last run" rather than the prior 14 days.
2. **Re-enrichment candidates:** The ONLY trigger for re-enrichment is the company-level property `last_enriched_date`. Query HubSpot for companies where `last_enriched_date < [today - 120 days]` OR (`last_enriched_date` IS EMPTY AND `customer_segment` is populated). Do not use `hs_lastmodifieddate`, `createdate`, or any other recency signal as a proxy  -  `last_enriched_date` is the authoritative field and it is set to today (YYYY-MM-DD) at the end of every enrichment run so the next rotation is predictable. Process in batches of 50 per day to keep the daily cycle bounded  -  tune the batch size based on total CRM account volume so the full stale pool rotates within the 120-day window (rough sizing: `daily_batch >= active_accounts / 120`). Apollo organization enrichment is the authoritative source for refreshed `state`, `country`, and firmographic data on every re-enrichment; territory owner is re-derived from the new state value.
3. For each company: execute company-enrichment full pipeline (Step 0C skips for re-enrichment, then Stages 1-3). Classify per segment-classification qualification gates. Map values per import-processor. Write all enrichment fields to HubSpot. Set `last_enriched_date` to today. Execute segment-classification cascade rules if segment changed. Sync to contacts.
4. Safety tiers by confidence: HIGH → Tier 1, MEDIUM → Tier 2, LOW/MANUAL_REVIEW → Tier 3
5. Deal protection applies per the rule above.
6. Run edge-case-researcher on any excluded/uncertain accounts.
7. Produce run report.

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
   - Stage 3 new-account creation: HIGH confidence → Tier 1 auto-create; MEDIUM → Tier 2 auto-create + flag; LOW / MANUAL_REVIEW → Tier 3 hold (surface in rep report's "possible new accounts — review needed" section, NOT auto-created).
   - Stage 5 field updates on deal-protected accounts (any open deal) → Tier 2 (applied + flagged).
   - Stage 5 LOW-confidence signals on Tier 1 accounts → Tier 3 hold, not written.
3. Apollo credit soft floor: if remaining credits < 20% of monthly allocation at Stage 3 entry, pause new-account enrichment for the run and defer to next Monday. Surface in Cooper's run report. Matched accounts (already in HubSpot) still get enriched since they're priority spend.
4. Account brief regeneration: the skill regenerates `account_brief` via the `account-brief` skill whenever either (a) brief is >30 days old, or (b) fresh research materially diverges from the existing brief. Apply Tier 1 (auto-write) on accounts without open deals, Tier 2 (auto-write + flag) on deal-protected accounts.
5. Delivery: 3 rep emails (Tim Lieto / Ken Cunningham / Tim Ziemer) + Cooper CC. Cooper also receives a consolidated run report folded into the daily Guardian email.
6. Idempotency: Job 8 is safe to re-trigger manually (e.g., for testing) but will NOT re-send rep emails outside the scheduled Monday AM run — manual triggers return report content only.

---

### JOB 7: PRE-DELETION AUDIT & CONTACT CONSOLIDATION
**Cadence:** Daily
**Executes:** pre-deletion-audit (full workflow)

This job is the single choke point through which every "mark this non-fit for deletion" decision must pass. It catches non-ICP accounts before they are flagged, reassociates salvageable contacts to ICP primaries when duplicates exist, and preserves any contact with activity in the last 90 days or an association to an open deal.

1. **Build the candidate set** by pulling companies that are:
   - Newly classified as non-ICP in the last 24h (Job 2 or segment-classification output where verdict was EXCLUDE)
   - Already `customer_segment = "Flagged for deletion"` but still have associated contacts unresolved (safety sweep for records that were flagged manually without the audit running)
   - Any company where `customer_segment` is in: `Dark Fiber - Commercial Enterprise`, `Enterprise-CustomerSegment`, `Partner Target`, `Other`, `Unknown` AND `last_enriched_date` > 30 days ago (periodic re-evaluation pool, batch of 25/day to keep the daily cycle bounded)
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

### Apollo monthly budget — HARD CAP 6,000 credits/month

**Effective 2026-04-26: total Apollo consumption across ALL routines is capped at 6,000 credits per calendar month.** The cap is enforced at the routine level via per-routine sub-caps that mathematically sum below 6,000/month at full hit rate, plus a pre-flight budget check that every Apollo-consuming routine performs at run start.

**Per-routine sub-caps (ALL routines must respect these — see each routine's Caps & Budgets section):**

| Routine | Sub-cap | Monthly max | Steady-state burn |
|---|---|---|---|
| Routine 0 (Import Validator) | 0 (Apollo-free, website-only) | 0 | 0 |
| Routine 1 (Fresh Enrichment) | 100 accounts/day, ICP-only via pre-score (~40% Apollo hit rate) | 1,500 | ~600 |
| Routine 2 (Stale Re-Enrichment) | 100 accounts/day, ICP+reclassify-only via pre-score (~40% Apollo hit rate) | 1,500 | ~750 |
| Routine 6 (Territory & Hygiene) | 25 Apollo state-verifications/day | 750 | ~300 |
| Routine 8 (Persona Fill, Fri) | 250 credits/week | 1,075 | ~1,000 |
| Routine 9 (Job Changes, quarterly) | 750 credits/quarter | 250 | 250 |
| weekly-signal-scan (Mon) | 200 credits/week | 860 | ~215 |
| **Combined cap** | | **5,935** | **3,115** |

The cap leaves ~65 credits/month of buffer at full hit and runs at ~52% of budget in steady state. **The 100/day record cap on Routines 1+2 is the throughput lever** — paired with pre-score triage that routes ~60% of records to no-Apollo paths, the effective Apollo cost per record drops to ~0.4 credits, so doubling the daily record throughput only modestly raises monthly Apollo burn (from ~2,240 at 50/day to ~3,115 at 100/day). The cap enables draining 500-record import spikes in 5 days instead of 10 and keeps fresh enrichment from starving downstream routines (signal-scan, persona fill, call recap, rep prospecting all cascade off accurate `customer_segment` + `account_tier`).

**Pre-flight monthly budget check (mandatory for every Apollo-consuming routine):**

At run start, before any Apollo call, every routine MUST:

1. Call `apollo_users_api_profile` (or equivalent budget-introspection endpoint) to fetch the current month's credit consumption.
2. Compute `remaining = 6000 - consumed_this_month`.
3. Compute `planned_for_this_run` (the routine's worst-case Apollo burn for this run, e.g. 50 credits for Routine 1 at full cap, 250 for Routine 8 first-run, etc.).
4. If `planned_for_this_run > remaining`: scale down the run to `remaining` credits worth of work, prioritized per the routine's priority rules, and surface in the Slack DM as "Apollo monthly budget cap reached — N items deferred to next month / next run."
5. If `remaining <= 50` (near zero): defer the entire run with a one-line Slack DM "Apollo monthly budget exhausted — routine deferred until next billing cycle."

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
- *(not used — per-record notes are intentionally skipped; see Change Log Format)*
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
