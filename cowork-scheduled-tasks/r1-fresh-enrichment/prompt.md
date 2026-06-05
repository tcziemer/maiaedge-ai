# CRM Guardian - Fresh Enrichment (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget; HubSpot is the source of truth for the candidate pool, the Apollo budget tracker lives in `weekly-reports/apollo-budget.json`, and the Tier 3 hold canvas (`F0B0AFSB9LN`) holds cross-task state. Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Daily, 10:00 AM CT, Monday-Friday. Cron: `0 10 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**

Runs SECOND in the daily Cowork cycle (after Import Validator). Drives every HubSpot company in the active candidate pool to a **definitive segment + tier + brief** at known freshness - newest-first, three routing paths, no silent backlog growth. Does NOT touch any other maintenance work - that's split across R2-R6.

**Throughput mandate:** This task MUST drain its full daily candidate batch (dynamic 100-150 records per Edit 5). Deferring records is the symptom of a misrouted query - every other CRM Guardian task, the weekly signal scan, the persona fill, the call recap, and rep prospecting workflows cascade off accurate segmentation. The new 4-filter-group trigger query (Edit 1) eliminates the noisy ~84/100 daily Other/Partner-Target reappearances, and the three-path workflow (Edit 2) routes each record to the right depth-of-research without burning Apollo credits on non-ICP records.

**CRM scale baseline:** 3,489 companies total. Active candidate pool (4-group trigger): ~100 records steady state, dropping toward zero as the pool drains. Import spikes can push to 200-400; dynamic cap (Edit 5) flexes 125/run at 200-400 and 150/run above 400 with a hero flag. Sort order guarantees newest imports get correct segmentation first so reps see the right tier on accounts they're actively working.

**Convergence target:** every record in the active pool gets a definitive `customer_segment + account_tier + account_brief` (or an explicit Tier 3 hold) at a known freshness within ~120 days. "Unknown" is a **forbidden output** of this routine - if research can't resolve it, the record gets `segmentation_confidence = manual_review_required` + Tier 3 hold instead.

---

## Connected Tools (Cowork)

- **HubSpot MCP** - read/write companies + contacts; territory owner re-derive
- **Apollo MCP** - `apollo_users_api_profile` (budget pre-flight), `apollo_organizations_enrich` (firmographics on LIKELY_ICP only)
- **Slack MCP** - `slack_send_message` to Cooper (hard-failure ping ONLY), `slack_read_canvas` + `slack_update_canvas`
- **`web_search`** - PRIMARY research path
- **`web_fetch`** - opportunistic enhancement (skip on 4xx/5xx/timeout - proceed on web_search alone, no penalty)

---

## Delivery - quiet on success, ping only on hard failure

Do NOT DM Cooper a per-run debrief. On a clean or partial-but-recoverable run (including zero-record runs and partial-gate runs where some records carry to next run), the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r1-fresh-enrichment/...` (the report body structured in the Output section below becomes the on-disk report, NOT a DM), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack/Apollo MCP unreachable, an abort, or zero records processed against a non-empty candidate queue - as ONE line:

`:red_circle: CRM Guardian - Fresh Enrichment [FAILED/ABORTED] - [one-clause reason].`

Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk report + Run-log row are the fallback.

---

## Reference Files (read at run start)

These exist in the repo and define the canonical decision logic. Read them once at run start to ensure you apply the current rules:

### Phase 3 canonical references (READ FIRST - 2026-05-14)

- `context/account-tiering/tier-compute-spec.md` - canonical `compute_tier(segment, sub_segment, hs_is_target_account)` algorithm. Called at Stage 4 of the 5-stage workflow. Defines named-account override, segment null fallback for unknown (segment, sub-segment) pairs, and the segment-priority defaults.
- `context/account-tiering/sub-segment-qualification.md` - pointer to file 06, the primary source of truth for the 30 active sub-segment values, their parent segments, D5 protocol questions, and anchor-account references.
- `context/account-tiering/enrichment-protocols.md` - operational D5 v2 protocols. Defines the 5-stage research-first workflow, per-sub-segment evidence questions, confidence-scoring rules, and Cooper conciseness rule (2-4 sentence cap on enriched fields).
- File 06 path (primary source of sub-segment classification): `context/account-tiering/sub-segment-qualification-full.md`

### Skill + supporting context references

- `skills/crm-guardian/SKILL.md` (Non-ICP Eviction Rule + safety tiers + Cross-Routine Ledger)
- `routines/_shared/apollo-weekly-budget-spec.md` (850/week Apollo cap as of 2026-05-06; R1 sub-cap 30/run as of 2026-05-21; tracker file format, pre-flight + post-run logic)
- `skills/company-enrichment/SKILL.md` (Stages 1-3 + Field Resolution Ladder + Completeness Gate Mandatory Fields)
- `skills/segment-classification/SKILL.md` (qualification gates, cascade rules, EXCLUDE verdict routing)
- `skills/import-processor/SKILL.md` (HubSpot enum value mapping)
- `skills/edge-case-researcher/SKILL.md` (second-pass for uncertain classifications)
- `context/hubspot/property-schema.md` + `context/hubspot/hubspot-values.md` (ESPECIALLY the **Enum Case-Sensitivity Reference** appendix - enum writes use the `value` not the `label`)
- `context/hubspot/territory-model.md` (state -> owner mapping)
- `context/core/icp-playbook.md` + `context/core/segment-qualification.md`
- `context/segments/` (all 6 segment cheatsheets - Colocation, Fiber, NeoCloud, Network Operator, MSP/Aggregator, **Enterprise** [Multi-DC ICP added 2026-05-11; reads `enterprise.md` for sub-segment Insider Language Banks + scale gate, plus `enterprise-use-cases.md` for the 8 priority Enterprise use cases])

---

## 5-Stage Research-First Workflow (Phase 3, 2026-05-14)

Per Cooper's 2026-05-14 directive, the Path α full enrichment workflow is structured as **5 discrete stages**. This order is mandatory: D1 quick-check fires BEFORE deep research to avoid wasted cycles on obvious disqualifiers, deep research fires BEFORE segment routing so classification is grounded in evidence (not name/domain guesses), and tier computation fires AFTER classification so the algorithm in `context/account-tiering/tier-compute-spec.md` has its inputs.

### Stage 0: Identity resolution
- Verify domain reachability + canonicalization
- Apply D2 wholesale-arm parent policy (`context/account-tiering/enrichment-protocols.md` D2) - wholly-owned wholesale arms of a parent operator inherit the parent's segment if the parent itself qualifies
- Dedup check (does this name/domain already exist as a different HubSpot company ID)

### Stage 1a: D1 quick check (cheap domain/website disqualifiers)
- Apply D1 quick disqualifiers from `context/account-tiering/enrichment-protocols.md` D1 (TLD-based, keyword-based, parked-domain checks)
- MATCH -> write `customer_segment = "Other"` (vetted non-ICP) OR `customer_segment = "Flagged for deletion"` (junk / dead) and SKIP deep research. On a `Flagged for deletion` write, ALSO set `flagged_for_deletion_reason` in the same update, leading with the canonical reason code that matches the D1 cause: `D1 disqualified (no reference value)` when the record matched a D1 global disqualifier with no competitive/partner reference value; `Dead domain` for parked/NXDOMAIN/dead destinations; `Hard junk / non-business` for junk TLD / non-business / spoofed-brand. Format: `"<Reason code>: <one concrete sentence of evidence>"` (no em dashes; see property-schema §2.1).
- Cite the specific D1 rule in `account_brief` and the audit log

### Stage 1b: Deep research -> populate 7 enriched fields
Apply the Cooper conciseness rule: **2-4 sentence cap per field**. No padding. The 7 fields populated at this stage:

1. `account_brief`
2. `geographic_focus`
3. `infrastructure_profile` (multi-select bands - **PRIMARY structured signal for classification**)
4. `hyperscaler_proximity`
5. `fabric_provisioning_approach` (Track A vs Track B detector)
6. `provisioning_landscape`
7. `recent_news_or_trigger_event`

**NOT populated at this stage:** `maiaedge_value_proposition`. The outreach skills (cold-email, linkedin-outreach, prospect-research) generate value-prop language at outreach time against the freshest version of the account's enriched profile. R1 does not pre-write value-prop.

### Stage 1c: D1 deep check (disqualifiers surfaced by research)
- Re-apply D1 rules now that deep research has surfaced industry, revenue, ownership signals
- Catches the records that passed the cheap domain check but reveal as non-ICP after research (e.g., a `.com` domain that turns out to be a regional dental chain)

### Stage 2: Segment routing
- Read the enriched profile -> run the D3 flowchart pre-gate from `context/account-tiering/enrichment-protocols.md` D3
- Fail the pre-gate -> `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` (same update) with D1/D3 rule citation in audit log. Lead the reason with `D1 disqualified (no reference value)` if the pre-gate fail is a D1 disqualifier match, otherwise `No ICP fit` (researched, no positive evidence for any ICP sub-segment). Format: `"<Reason code>: <one concrete sentence of evidence>"` (no em dashes; see property-schema §2.1).
- Pass -> continue to Stage 3

### Stage 3: D3 flowchart traversal -> D5 protocol questions
- Walk the D3 flowchart to identify candidate sub-segment(s)
- For each candidate, run the per-sub-segment D5 evidence questions from `context/account-tiering/enrichment-protocols.md` and `context/account-tiering/sub-segment-qualification.md` (file 06)
- Compute confidence + apply tiebreaker for best-fit when multiple candidates pass evidence
- **No-default-manual-review** - best-fit wins, `manual_review_required` is reserved for genuine multi-classification ambiguity (see "No-Default-Manual-Review Principle" section below)

### Stage 4: Tier computation
- Call `compute_tier(segment, sub_segment, hs_is_target_account)` per `context/account-tiering/tier-compute-spec.md`
- **Honor `hs_is_target_account = true`:** skip the tier write only (the named-account flag drives tier in HubSpot's calc-property layer); segment, sub-segment, signal fields, and enriched fields write normally
- Unknown (segment, sub-segment) pair -> segment null fallback per spec; log warning to the run report and audit log. Example records that historically hit this fallback: the 5 MSP/colo mismatched records (Mapletree, Montera, PTS, Lonestar, LS Power).

### Stage 5: HubSpot write + audit
- Write the 8 enriched fields (the 7 from Stage 1b + audit) and classification fields (segment, sub-segment, tier unless `hs_is_target_account = true`, confidence)
- **Path α (new accounts) default-write `signal_heat = Cold`** - no signal history yet. Heat will be recomputed by Weekly Signal Scan / R-Tier-Audit once signals start arriving on this account. This is a default assignment, NOT a classification - the enrichment bot does not compute heat from research findings.
- Audit log entry cites the specific D1 / D2 / D3 / D5 rules applied
- **NO `maiaedge_value_proposition` write** (outreach skills own this field at outreach time)

### Path behaviors

- **Path α full enrichment** runs ALL 5 stages. New accounts get `signal_heat = Cold` written at Stage 5.
- **Path β re-research** runs Stage 1b refresh (deep research on the existing record to update the 7 enriched fields) + Stages 2-5 IF classification shifts. If Stage 1b confirms the existing classification with no shift, only the enriched fields get refreshed (no segment/sub-segment/tier rewrite). **Path β does NOT touch `signal_heat`** - Signal Scan + R-Tier-Audit own heat for existing records.
- **Path γ eviction** writes `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` (same update) with the D1 rule citation in `account_brief` and the audit log. Reason code by cause: `No ICP fit` for LIKELY_NON_ICP (researched, no positive evidence for any ICP sub-segment, not a partner/competitor reference); `Hard junk / non-business` for LIKELY_JUNK (junk TLD / spoofed brand / non-business); `D1 disqualified (no reference value)` for a D1 disqualifier match with no reference value; `Dead domain` for DEAD_DOMAIN. Format: `"<Reason code>: <one concrete sentence of evidence>"` (no em dashes; see property-schema §2.1). No Stage 2-4 traversal needed: D1 is the gate. **Path γ does NOT touch `signal_heat`** - eviction supersedes.

### End-of-pipeline verification queries (D5 §9 / 4 self-checks)

R1 self-runs these 4 checks at end of pipeline BEFORE the run report is finalized. Any failure surfaces in the run report's "What needs Cooper's attention" section as a remediation item (and, if a check failure constitutes a hard failure, in the failure ping per the Delivery rule).

1. **Sub-segment nullness check.** For every record this run wrote `customer_segment` to an ICP value, confirm `company_sub_segment` is populated. If `company_sub_segment` is null on an ICP record, confirm `segmentation_confidence = manual_review_required` AND `account_brief` contains named reasoning for why sub-segment was not assigned. Otherwise flag as a bug.
2. **Confidence-evidence alignment check.** For every record this run wrote `segmentation_confidence = high_90`, confirm the audit log cites either a named D5 question-count threshold (e.g., "3 of 4 D5 questions passed") OR an anchor account match (e.g., "matches Meijer Enterprise Retail anchor profile"). high_90 without named evidence is a bug.
3. **Disqualifier audit check.** For every record this run wrote `customer_segment = "Other"` via eviction (Path γ PARTNER_KEEP) or Stage 1a/1c D1 MATCH, confirm the audit log cites the specific D1 rule that disqualified it. Generic "non-ICP" with no rule citation is a bug.
4. **Catch-all guard check.** For every record this run classified as `Regional CLEC`, `Standard - colo`, or `Telecom Aggregator` (the three catch-all sub-segments that historically over-collect manual_review_required records), confirm the audit log cites positive-evidence D5 questions (not just negative exclusion from other sub-segments). These three sub-segments require POSITIVE evidence to assign - exclusion-by-default is a bug.

---

## No-Default-Manual-Review Principle (Cooper 2026-05-14)

`manual_review_required` is NOT the default escape hatch. Best-fit classification with calibrated confidence is the default. Three explicit categories:

- **Best-fit classification with calibrated confidence.** When research surfaces positive evidence for one sub-segment more than others, assign that sub-segment with the appropriate confidence band (`low_5069` / `medium_7089` / `high_90` per D5 question pass-count). The tiebreaker rules in `context/account-tiering/sub-segment-qualification.md` resolve close calls.
- **`Flagged for deletion`** for records with no positive evidence for ANY ICP sub-segment (D1 MATCH or D3 pre-gate fail).
- **`manual_review_required`** reserved for genuine multi-classification ambiguity: 2+ sub-segments both have clear positive evidence AND the tiebreaker fails to pick one. This should be RARE.

**Target population:** `segmentation_confidence = manual_review_required` writes <5% of records per run. If a run exceeds 5%, the routine is over-applying manual_review_required and the next run should investigate (likely cause: a sub-segment's D5 evidence questions are too strict or the tiebreaker isn't firing).

---

## Multi-Marker Classification (Cooper 2026-05-14)

`infrastructure_profile` is the **PRIMARY structured signal** for classification. Multi-select bands populated at Stage 1b are the highest-weighted input to Stage 3 D5 evidence questions.

**Tie-breaker rule:** when `annualrevenue` conflicts with `infrastructure_profile`, `infrastructure_profile` wins. Revenue data is dirty more often than infrastructure (stale Apollo pulls, parent-vs-subsidiary attribution errors, currency mismatches). Infrastructure signals are anchored in the company's actual buildout and don't drift the same way.

This rule applies specifically to the Enterprise scale gate ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR in-house net eng) and to Tier 1 vs Tier 2 carrier disambiguation in Network Operator. When in doubt, trust the infrastructure footprint.

---

## Active Sub-Segment Values (30 active values, 2026-05-14)

Authoritative list lives in `context/account-tiering/sub-segment-qualification.md`. Phase 3 notes:

- **`Tier 1 Carrier - Network Op`** replaces any legacy "Tier 1 Global Incumbent" references in older docs. Use the new name.
- **`Subsea cable operator`** is the 30th sub-segment, added 2026-05-14. Pairs with the Network Operator parent segment.
- **`Crypto to AI - Neoclouds`** is INCLUSIVE of both the operator AND the landlord (data center owner repurposing for AI compute). Both fit this sub-segment per Cooper 2026-05-14: do not split.
- **`Greenfield`** is a REAL sub-segment, not deprecated. It pairs with EITHER the Colocation OR the NeoCloud parent segment depending on the operator's go-to-market posture (colo greenfield = traditional retail/wholesale buildout; neocloud greenfield = GPU-first / AI compute buildout from scratch).

---

## Run-Time Invariants

### A. Timezone
All date math in America/New_York. "Today" = current Eastern calendar date at run start. HubSpot timestamps are UTC - convert to ET before comparing.

### B. Skip Already-Flagged
Companies with `customer_segment = "Flagged for deletion"` are out of scope. Exclude from candidate query.

### C. Customer Protection
Any company with ANY closed-won deal is protected. Never segment-downgrade from ICP to non-ICP - Tier 3 escalation instead.

### D. Default to Tier 3 When Uncertain
LOW / MANUAL_REVIEW segmentation confidence, conflicting sources, ambiguous data → do not write. Hold for Cooper.

### E. Idempotency + Completeness Gate
After successful enrichment AND completeness-gate pass, set `last_enriched_date = today (ET)`. **`last_enriched_date` is the LAST field written and is ONLY written if the gate passes.** A failed gate means partial enrichment - write whatever fields ARE available, but DO NOT bump `last_enriched_date`. Record stays in stale pool for next-run retry.

**Why this matters:** historical bug pattern was bumping `last_enriched_date` while leaving infrastructure_profile / fabric_provisioning_approach / value_prop blank. That removed records from the stale pool for 120 days while they were actually still unenriched. The gate prevents that.

### F. MaiaEdge Gotchas
- `account_tier` is INVERTED. Tier 1 = highest priority.
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed 2026-05-07 from the deleted legacy value `Enterprise`).
- `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is now an **ICP segment as of 2026-05-11** with four sub-segments: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Hard gate: $1B+ revenue AND (3+ DCs OR direct Equinix Fabric / Megaport port OR confirmed in-house net eng) AND vertical match. Anchor account: Meijer.
- AI Colo: `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`.
- No em dashes in customer-facing fields (`account_brief`, `maiaedge_value_proposition`, etc.). Use hyphens.
- Category descriptor: "Carrier infrastructure" only. Never "IaaS," "NaaS," "platform."

### G. Write Authorization
Every `manage_crm_objects` call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:** `customer_segment` (including "Flagged for deletion" via Path γ / Stage 1a / Stage 2 pre-gate fail), `flagged_for_deletion_reason` (scannable reason code + one sentence of evidence; written in the SAME update as any `customer_segment = "Flagged for deletion"` write; lead with the canonical reason code per property-schema §2.1), `company_sub_segment`, `account_tier`, `signal_heat` (Path α new-account default `Cold` only — Title Case per HubSpot enum), `segmentation_confidence`, `last_enriched_date`, `hubspot_owner_id`, `state`, `country`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event` (pure narrative — no date prefix; if Stage 1b research surfaces a fresh signal-grade event with a known event date, also write `last_signal_date` to the event date), `domain` (MISDOMAIN auto-correct only - Tier 1 HIGH / Tier 2 MEDIUM). **NOT pre-authorized:** `maiaedge_value_proposition` (outreach concern, not enrichment - owned by cold-email / linkedin-outreach / prospect-research / sdr-pipeline). **Heat on existing accounts** is owned by Signal Scan Stage 5b and R-Tier-Audit, not R1 - Paths β and γ do not touch `signal_heat`.

**Hard stops:** MaiaEdge own (124293230301). Any open deal at `contractsent` or later.

---

## Pre-flight - Tier 3 Hold Exclusion (NEW, runs BEFORE the trigger query)

At run start, BEFORE issuing the HubSpot search:

1. `slack_read_canvas` on `F0B0AFSB9LN` (the cross-routine ledger).
2. Parse every Tier 3 hold table. Section header pattern:
   - `### R0 Import Validator YYYY-MM-DD - Tier 3 holds added`
   - `### R2 Stale Re-Enrichment YYYY-MM-DD - Tier 3 holds added`
   - `### R4 Flagged Consolidation YYYY-MM-DD - Tier 3 holds added`
   - `### R1 Fresh Enrichment YYYY-MM-DD - Tier 3 holds added` (this routine's own prior-run holds)
3. Each table uses columns `Date | Routine | Account | HubSpot ID | Reason | Action`. Extract every value from the **HubSpot ID** column across all parsed sections.
4. Build `TIER_3_EXCLUDE_SET` (deduplicated set of HubSpot company IDs).
5. Apply as a CLIENT-SIDE filter on the trigger query result - drop any candidate whose `hs_object_id` is in the set. (HubSpot's filterGroups max is 5; the exclude set can grow large enough that listing it inside the query is infeasible - client-side is the cleaner path.)

**Why this matters:** prevents the 2026-05-06 g.softbank.co.jp pattern, where R0 holds a record at 9 AM and R1 incorrectly classifies it at 10 AM because it didn't see the hold.

---

## Trigger Query

HubSpot `search_crm_objects` on COMPANY. **Four logical filter groups** (Edit 1, 2026-05-06 redesign), implemented as **five filterGroups** because HubSpot AND-combines filters within a group and Filter Group B's "at least one of sub_segment / tier blank" must be split into two OR'd sub-groups. HubSpot's filterGroups limit is 5 - this is exactly at the limit.

### Filter Group A - Blank primary segmentation
- `customer_segment` operator `NOT_HAS_PROPERTY`
- `hs_object_id` operator `NEQ` value `124293230301`

### Filter Group B - ICP partial-fill (true gap)
Split into **B1** and **B2** because HubSpot AND-combines within a group and we need OR between "sub_segment blank" and "tier blank":

**B1:**
- `customer_segment` operator `IN` values `["Data Center Colo Provider", "Fiber Operator", "Network Operator(Tier 1 / VNO)", "NeoCloud", "MSP/Aggregator", "Enterprise-CustomerSegment"]`
- `company_sub_segment` operator `NOT_HAS_PROPERTY`
- `hs_object_id` operator `NEQ` value `124293230301`

**B2:**
- `customer_segment` operator `IN` (same 6 values as B1)
- `account_tier` operator `NOT_HAS_PROPERTY`
- `hs_object_id` operator `NEQ` value `124293230301`

### Filter Group C - Unknown segment (any confidence - must be resolved)
- `customer_segment` operator `EQ` value `Unknown`
- `hs_object_id` operator `NEQ` value `124293230301`

### Filter Group D - Low-confidence non-ICP (needs verification)
- `customer_segment` operator `IN` values `["Other", "Partner Target"]`
- `segmentation_confidence` operator `IN` values `["low_5069", "manual_review_required"]`
- `hs_object_id` operator `NEQ` value `124293230301`

### Explicitly excluded (these stop reappearing in the daily pool)
- `customer_segment IN ["Other", "Partner Target"]` AND `segmentation_confidence EQ "high_90"` - these are deliberate, vetted classifications. Do not touch them. Re-evaluation belongs in R2's 120-day stale rotation, not here.
- Any `customer_segment = "Flagged for deletion"` - out of scope.
- MaiaEdge own (`hs_object_id = 124293230301`) - hard stop.
- `last_enriched_date IS EMPTY` records with populated ICP segment + populated sub_segment + populated tier - that's R2's stale pool, not R1.

### Sort + cap
- **Sort:** `createdate DESCENDING` (newest first).
- **Cap:** dynamic per Edit 5 (100/125/150 based on total pool size).

### Dry-test baseline (2026-05-06)
- Old 2-filter-group query: **391 candidates**.
- New 5-filter-group query: **97 candidates** at run-time of design dry-test. Validate against this benchmark - if a future query returns >200 the trigger logic has drifted and needs investigation.

---

## Workflow - Three Processing Paths (Edit 2, 2026-05-06 redesign)

Every candidate enters one of three paths based on which trigger filter group it came from + a name/domain pre-score. Every path ends with a definitive resolution - enrichment write, eviction write, or explicit Tier 3 hold (with `segmentation_confidence = manual_review_required`). **"Unknown" is a forbidden output of this routine.**

### Pre-score keywords (used to route filter groups A and B's pool)

| Pre-score | Heuristic |
|---|---|
| **LIKELY_ICP - operator** | Name/domain suggests an operator (contains `fiber`, `network`, `telecom`, `wholesale`, `colo`, `data center`, `cloud`, `interconnect`, `cdn`, `transport`, `wavelength`, `gpu`, `compute`, `infrastructure`, `mso`, or matches an ICP segment cheatsheet) |
| **LIKELY_ICP - Enterprise candidate** | Name/domain suggests one of the four Enterprise ICP sub-segments AND scale signal present. Heuristics: known Fortune 500/1000 financial services / healthcare system / multi-DC retailer / BPO operator (matches name in `context/segments/enterprise.md` example list - JPMorgan, HCA, Meijer, Kroger, Cognizant, Genpact, etc.); domain contains `.com` for a vertical-keyword hit (`bank`, `bancorp`, `health`, `hospital`, `medical`, `retail`, `grocery`, `bpo`); LinkedIn / Apollo signals enterprise of $1B+ revenue. Routes to Path α - full enrichment will run the Enterprise scale gate via segment-classification |
| **LIKELY_NON_ICP** | TLDs `.gov`/`.edu`/`.mil`; `.org` for non-telecom non-profits; keywords `church`/`school`/`clinic`/`dental`/`realestate`/`restaurant`/`apparel`/`consulting`/`lawfirm`/`staffing`/`hair`/`beauty`/`farm`/`agriculture`/`bath`/`auto`/`truck`/`manufacturing`/`media` (unless `manufacturing` paired with $1B+ enterprise IT footprint that surfaces as Watch List in segment-classification - surface as Tier 3) /`crypto` (unless paired with `cloud`/`gpu`/`compute`). Note: `health` and `clinic` alone do NOT auto-disqualify - small clinics are LIKELY_NON_ICP, but multi-hospital IDNs are LIKELY_ICP - Enterprise candidate. Use scale + footprint to disambiguate, route ambiguous cases to Path α (segment-classification handles the gate). |
| **LIKELY_JUNK** | TLDs `.tk`/`.ml`/`.ga`; spoofed brand domains; dead-on-arrival lookups |

### Routing matrix

| Filter group source | Pre-score | Path |
|---|---|---|
| A (blank segment) | LIKELY_ICP - operator | **α - Full enrichment** |
| A (blank segment) | LIKELY_ICP - Enterprise candidate | **α - Full enrichment** (segment-classification runs the Enterprise scale gate; if it fails, segment-classification returns Other / Watch List → re-routes to Path γ) |
| A (blank segment) | LIKELY_NON_ICP / LIKELY_JUNK | **γ - Eviction-decision** |
| B (ICP partial-fill, sub_segment OR tier blank) | LIKELY_ICP keyword match (operator OR Enterprise) | **α - Full enrichment** (gap fill) |
| B (ICP partial-fill, including `Enterprise-CustomerSegment` records) | No LIKELY_ICP keyword match | **β - Re-research** (Enterprise records that fall here keep their ICP segment; β re-research fills sub_segment + tier per segment-classification's Enterprise sub-segment assignment rules) |
| C (Unknown segment) | any | **β - Re-research** |
| D (Other / Partner Target + low_5069 / manual_review_required) | any | **β - Re-research** |

---

### Path α - Full enrichment

**Source:** Filter Group A's LIKELY_ICP pool, plus Filter Group B's LIKELY_ICP partial-fills.
**Workflow:** web_search + optional web_fetch → company-enrichment Stages 1-3 → Apollo enrich → segment-classification → ICP Gate → write.
**Apollo cost:** ~1 credit per record.
**Cap:** **30 records/run** (Apollo budget-bound at 30 credits - see Caps & Budgets).

For each candidate:
1. **`web_search` `"<domain>"` site identification** + **`web_search` `"<company name>" "<domain>"`** - primary research path.
2. **OPTIONAL `web_fetch` enhancement** - `https://[domain]` + `/about` + `/contact` if reachable. If web_fetch returns 4xx/5xx/timeout, **proceed on web_search alone** - no penalty.
3. Run `skills/company-enrichment/SKILL.md` **Stages 1-3** (web-search-driven adaptive enrichment).
4. Run **Apollo `apollo_organizations_enrich`** - authoritative for `state`, `country`, industry, employee count, revenue, funding. Apollo wins when it disagrees with HubSpot.
5. Run `skills/segment-classification/SKILL.md` qualification gates → verdict + confidence.
6. Apply Non-ICP Eviction Rule decision tree (`skills/crm-guardian/SKILL.md`):
   - **ICP verdict** → continue to step 7.
   - **Non-ICP, PARTNER_KEEP keep-list** → re-route to Path γ (eviction Other-write).
   - **Non-ICP, NOT PARTNER_KEEP** → re-route to Path γ (eviction Flagged-write).
   - **AMBIGUOUS / LOW / MANUAL_REVIEW** → run `skills/edge-case-researcher/SKILL.md`; if still uncertain → Tier 3 Hold Gate (NEVER output "Unknown").
7. Apply `skills/import-processor/SKILL.md` enum mapping. **Critical: enum writes use `value` not `label` - see `context/hubspot/property-schema.md` Enum Case-Sensitivity appendix.**
8. **Field Resolution Ladder for state/country.** If Apollo returned null, walk: Apollo → website → LinkedIn About → WHOIS, per `skills/company-enrichment/SKILL.md`. Tier 1 at HIGH (steps 1-2), Tier 2 at MEDIUM (step 3), Tier 3 hold only if all four steps return null.
9. **ICP Completeness Gate** (see "Differentiated Completeness Gates" section).
10. Re-derive `hubspot_owner_id` from HQ `state` per `context/hubspot/territory-model.md`.
11. If `customer_segment` was filled or changed: execute Segment Change Cascade Rules - re-derive sub-segment, tier, confidence, infrastructure_profile; sync `customer_segment` to all associated contacts (Tier 1).

---

### Path β - Re-research

**Source:** Filter Group C (`Unknown`), Filter Group D (Other / Partner Target with low confidence), and Filter Group B partial-fills WITHOUT LIKELY_ICP keyword match.
**Workflow:** web_search-only re-classification (no Apollo unless promoted to LIKELY_ICP mid-research; if promoted AND Apollo budget remains, pull into Path α and consume Apollo credit - that promotion COUNTS AGAINST PATH α'S CAP, not Path β's).
**Apollo cost:** 0 credits in steady state.
**Output domain:** ICP / Other / Partner Target / Flagged for deletion / explicit Tier 3 hold. **NEVER "Unknown".**
**Cap:** **50 records/run.**

For each candidate:
1. **`web_search` `"<domain>"`** + **`web_search` `"<company name>" "<domain>"`** - primary identification.
2. **OPTIONAL `web_fetch`** `https://[domain]` + `/about` if reachable.
3. **MISDOMAIN check (BEFORE classification).** If the entity at the domain differs from HubSpot `name` AND the HubSpot name searches cleanly to its own canonical domain → MISDOMAIN. Run domain-correction discovery; on HIGH: write `domain = <discovered>` Tier 1, account_brief, re-route to Path α. On MEDIUM: same Tier 2. On LOW: skip MISDOMAIN, continue.
4. Mid-research promotion check: if research turns up clear ICP signals (operator language, NaaS/colo/fiber buildout, Tier 1+ scale evidence) AND Path α has remaining capacity AND Apollo budget remains → promote to Path α step 3 onward. Counts against Path α cap.
5. Apply segment-classification gates:
   - **ICP verdict** → ICP Completeness Gate (full ICP write path).
   - **Other / Partner Target with high confidence resolution** → Non-ICP Completeness Gate (write segment + tier_5 + brief + high_90 confidence).
   - **HARD_DELETE / DEAD_DOMAIN** → Eviction Completeness Gate (write Flagged for deletion).
   - **Still uncertain after research** → **Tier 3 Hold Gate** with `segmentation_confidence = manual_review_required`. Add HubSpot ID to canvas Tier 3 table. Do NOT bump `last_enriched_date`.

**Critical for Filter Group C (`Unknown`) records:** "Unknown" with prior `segmentation_confidence = high_90` is treated as RE-RESEARCHABLE, NOT a deliberate Cooper-set final state (Cooper has confirmed he never deliberately writes Unknown + high_90). On re-research, if still uncertain → write segmentation_confidence = manual_review_required AND Tier 3 hold. The high_90 stamp gets DOWNGRADED - that's intentional. Better to surface real ambiguity than perpetuate a stale confidence stamp.

---

### Path γ - Eviction-decision

**Source:** Filter Group A's LIKELY_NON_ICP and LIKELY_JUNK pools, plus Path α/β re-routes.
**Workflow:** web_search + optional web_fetch → MISDOMAIN check → eviction decision per Non-ICP Eviction Rule.
**Apollo cost:** 0 credits.
**Cap:** **50 records/run.**

For each candidate:
1. **`web_search`** for entity identification + **OPTIONAL `web_fetch`** for confirmation.
2. **MISDOMAIN check (BEFORE applying eviction rule).** Same logic as Path β step 3. On MISDOMAIN HIGH/MEDIUM → re-route to Path α.
3. Apply Non-ICP Eviction Rule decision tree:
   - **PARTNER_KEEP** → Non-ICP Completeness Gate (`customer_segment = "Other"`, `account_tier = "tier_5"`, brief, `segmentation_confidence = "high_90"`).
   - **HARD_DELETE** → Eviction Completeness Gate (`customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Hard junk / non-business: <one concrete sentence>"`, brief explaining reason).
   - **DEAD_DOMAIN** (real DNS NXDOMAIN / parked / persistent 4xx-5xx - NOT proxy block) → Eviction Completeness Gate (`flagged_for_deletion_reason = "Dead domain: <one concrete sentence>"`).
   - **AMBIGUOUS** → Tier 3 Hold Gate.
   - **Surprise ICP** → re-route to Path α.

---

### Cap-aware slot rebalancing

Total slots = dynamic per-run cap (Edit 5). Default slot allocation: 50 / 50 / 50 = 150 (at the high backlog cap). At lower caps, scale proportionally (33/33/34 at 100, 42/42/41 at 125).

If Path α candidates < its allocated slots → roll unused slots to Path β (the highest-volume path on the new query).
If Path γ candidates < its allocated slots → roll unused slots to Path β.
If Path β candidates < its allocated slots → roll to Path α (Apollo permitting), then Path γ.

This guarantees the dynamic cap is the ACTUAL drain rate every run, not an aspirational ceiling.

**No record gets deferred unprocessed.** Every record gets a definitive write (enrichment, Other, Flagged for deletion) or an explicit Tier 3 hold with `manual_review_required` confidence. The dynamic batch drains every run.

---

## Differentiated Completeness Gates (Edit 4, 2026-05-06)

Each path lands at a different gate based on the classification outcome. The gate determines what's required before the routine writes anything AND whether `last_enriched_date` gets stamped (the field that gates R2's 120-day rotation).

### ICP Gate (Path α + Path β LIKELY_ICP-promoted partial-fill)
**Required fields, ALL must be populated:**
- `customer_segment` (one of the 7 ICP values)
- `company_sub_segment`
- `account_tier`
- `segmentation_confidence` ≥ `medium_7089`
- `state`
- `country`
- `hubspot_owner_id`
- `infrastructure_profile`
- `account_brief`

`maiaedge_value_proposition` is intentionally NOT in this gate. Per CLAUDE.md Operating Principle #6 (Cooper 2026-05-14): outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) populate that field on-demand at outreach time using the customer_segment-specific template. R1 does not write it.

**Pass:** write all fields + stamp `last_enriched_date = today (ET)`.
**Fail:** partial write of resolved fields ONLY; `last_enriched_date` stays at prior value (blank for fresh records). Surface in the run report under "Partial Enrichment - held for next run."

### Non-ICP Gate (Path γ Other / Partner Target; Path β resolving to Other)
**Required fields, ALL must be populated:**
- `customer_segment` (Other or Partner Target)
- `account_tier = "tier_5"`
- `segmentation_confidence = "high_90"`
- `infrastructure_profile = "None Identified"`
- `account_brief` (must explain why Other / why kept as Partner Target)
- `hubspot_owner_id`

**Pass:** write all fields + stamp `last_enriched_date = today (ET)` so the record stops reappearing in the daily pool.
**Fail:** partial write of resolved fields; `last_enriched_date` stays at prior value.

### Eviction Gate (Path γ Flagged for deletion; Stage 1a / Stage 2 pre-gate fail Flagged writes)
**Required fields:**
- `customer_segment = "Flagged for deletion"`
- `flagged_for_deletion_reason` — written in the SAME update, leading with the canonical reason code per property-schema §2.1, then a colon and one concrete sentence of evidence. Code by cause: `No ICP fit` (researched, no positive evidence for any ICP sub-segment), `Hard junk / non-business` (HARD_DELETE / LIKELY_JUNK), `Dead domain` (DEAD_DOMAIN), `D1 disqualified (no reference value)` (D1 disqualifier match, no reference value). No em dashes in the reason string.
- `account_brief` explaining HARD_DELETE / DEAD_DOMAIN / No-ICP rationale (cite discovered category)
- `segmentation_confidence = "high_90"`

**Pass:** write all fields + stamp `last_enriched_date = today (ET)`.
**Fail:** treat as Tier 3 hold (don't write Flagged for deletion without high confidence).

### Tier 3 Hold Gate (Path β unresolved; Path α step 6 fall-through; Path γ AMBIGUOUS)
**This is a NON-WRITE gate.** No write to `customer_segment` / `company_sub_segment` / `account_tier`.
- `segmentation_confidence = "manual_review_required"` (Tier 1 write - explicitly DOWNGRADES prior high_90 stamps on Filter Group C `Unknown` records)
- `account_brief` explains the ambiguity: what was checked, what's still unclear, what needs Cooper's eye
- `last_enriched_date` is NOT bumped - record stays in the active pool for next run
- HubSpot ID added to canvas Tier 3 table (`### R1 Fresh Enrichment YYYY-MM-DD - Tier 3 holds added`) per the Cross-routine Ledger section

**Why this gate matters:** Cooper's hard rule - if a record can't be definitively classified, surface it explicitly rather than leave a silent "Unknown" or stale high_90. Tier 3 hold + manual_review_required is the routine's escape hatch; "Unknown" output is forbidden.

---

## Safety Tiers

| Confidence | Segment/fields write | Contact cascade |
|-----|-----|-----|
| HIGH | Tier 1 auto-write | Tier 1 sync |
| MEDIUM | Tier 2 auto-write + flag | Tier 1 sync |
| LOW / MANUAL_REVIEW | Tier 3 hold (no write) | - |

**Deal protection:** if any open deal exists, segment and tier writes escalate to Tier 3. Owner corrections stay Tier 1.

---

## Caps & Budgets

### Dynamic per-run record cap (Edit 5)

After the trigger query + Tier 3 exclusion, count `total_candidates`:

| total_candidates | Per-run cap | Notes |
|---|---|---|
| ≤ 200 | **100 records/run** | Steady state |
| 201 – 400 | **125 records/run** | Elevated |
| > 400 | **150 records/run** | Backlog elevated - run report header flags `BACKLOG ELEVATED - inflow > drain rate, consider trigger refinement or routine frequency increase` |

The cap caps records, NOT paths. Within the cap, slots distribute across the three paths per the Routing matrix and Cap-aware slot rebalancing.

### Apollo credits (changed 2026-05-06, supersedes 2026-05-03 spec)

- **Weekly cap (primary):** per `routines/_shared/apollo-weekly-budget-spec.md`. Global weekly cap **850 credits** (unchanged). Read `weekly-reports/apollo-budget.json` at run start. **R1's sub-cap is 30 credits per run** (raised 30 → 50 on 2026-05-06, returned to 30 on 2026-05-21 - see footnote below). 5 runs/week × 30 = 150/week (18% of the 850/week global cap).
- If `consumed >= 850`: skip Apollo entirely - process Path β and Path γ only (both 0 credits), surface deferred Path α records in the run report header.
- If `available < 30`: scale R1's budget down to `available`, prioritize Path α LIKELY_ICP records first.
- **Monthly cap (kept, secondary):** call `apollo_users_api_profile`. Confirm `(monthly_consumed + R1_budget) <= 6000`. If monthly is depleted, skip Apollo regardless of weekly state.
- **R1 monthly draw:** ~650 against Apollo's 6,000/month allocation (5 runs × 30 credits × ~4.3 weeks).
- Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded` error.

> **2026-05-21:** R1 sub-cap reduced from 50 → 30 cr/run to free 100 cr/wk for R2's 5,000-record rotation headroom. Recent R1 daily Apollo consumption averaged 5-10 cr with peak of 22 (2026-05-12) - 30/day remains 36% over peak.

### Apollo budget post-run write (Edit 7 - best-effort git)

After the routine completes:

1. **Required:** write updated `weekly-reports/apollo-budget.json` to disk - increment `consumed`, increment `by_routine.fresh-enrichment`, append history entry, trim history to last 14 days.
2. **Best-effort git:** attempt one `git add` + `git commit` + `git push` with a 10-second timeout per command.
   - If `.git/index.lock` is present (concurrent routine holding the lock) OR any git command exits non-zero → log a single line in the run report: `Git commit deferred (concurrent routine); JSON updated locally`. Do NOT treat as a run failure.
   - The local JSON update is the source of truth. The next routine that successfully commits will sweep this run's update into git history.
3. **The on-disk run report is the audit trail of record.** Apollo consumption is recorded in every run's report body regardless of git status (see Output section). The CRM Ops Daily Digest reads it from there.

### HubSpot writes
**Batch cap 10 `objects` per `manage_crm_objects` call.** Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch after 3 consecutive 429s.

### Web tooling
- **web_search:** ~3-5 per Path α record (multi-search for Stages 1-3), ~2-3 per Path β record, 1-2 per Path γ record. ≥1s between searches.
- **web_fetch:** opportunistic only. ≥0.5s between fetches per host.
- **Session pacing:** 100 records/page on HubSpot reads, ≥1s between pages.

---

## On-disk run report (structure - Edit 8, 2026-05-06)

Write this report to `weekly-reports/YYYY-MM-DD/r1-fresh-enrichment/run-report.md`. This is the durable record the CRM Ops Daily Digest reads from - it is NOT sent as a DM. Keep the structure intact.

**Header:**
```
CRM Guardian - Fresh Enrichment - [YYYY-MM-DD] - [X]/[cap] processed · [N] Tier 3 held
```

**Body:**
```
*Pool:* [total_candidates] candidates · cap [100/125/150] · drain projection: [days_to_drain] days at current rate
[If total_candidates > 400] :warning: BACKLOG ELEVATED - inflow > drain rate, consider trigger refinement or routine frequency increase

*Path counts (this run):*
- Path α full enrichment: [Nα] processed → [Iα] ICP writes, [Eα] re-routed to γ
- Path β re-research: [Nβ] processed → [Bβ] reclassified, [Tβ] Tier 3 holds
- Path γ eviction: [Nγ] processed → [Pγ] Partner Target keeps, [Fγ] Flagged for deletion, [Mγ] MISDOMAIN re-routes to α

*Apollo:* [credits used] credits this run · [weekly_consumed]/850 weekly · [available] remaining for week
*Git:* [committed | deferred (concurrent routine); JSON updated locally]

*Path α - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Colocation / Fiber / NeoCloud / Network Op / MSP-Aggregator):
  - [Company name] ([segment] / [sub_segment] / tier_[N])
- Enterprise ICP (Multi-DC, 4 sub-segments - promoted 2026-05-11):
  - [Company name] ([Enterprise-CustomerSegment] / [Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services - Enterprise] / tier_[N])
  - Note: Cooper should spot-check Enterprise classifications in early runs - verify scale gate ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR in-house net eng) was actually applied.
- Enterprise scale-gate failures routed to Path γ (Other / Watch List):
  - [Company name] (failed scale gate; vertical OK but [missing scale signal])

*Path β - Top 5 reclassifications:*
- [Company]: was [old_segment]/[old_conf] → became [new_segment]/[new_conf]
- [...]

*Path γ - Eviction summary:*
- [Pγ] Partner Target keeps · [Fγ] Flagged for deletion ([breakdown by reason: HARD_DELETE / DEAD_DOMAIN])

*What needs Cooper's attention:*
- [If Tier 3 > 0] [N] Tier 3 holds - see canvas F0B0AFSB9LN section "R1 Fresh Enrichment [YYYY-MM-DD]" + the per-path tables below
- [If Flagged for deletion > 0] [F] hard-flagged companies in HubSpot Companies filter `customer_segment = "Flagged for deletion"`
- [If partial gate failures > 0] [P] records partial-enriched (gate failed); will retry next run

*Run health:* [GREEN / YELLOW / RED]
- GREEN: full cap processed, 0 errors, gate-pass rate >80%, no Apollo cap pressure
- YELLOW: completed but Tier 3 holds OR gate-pass rate 50-80% OR Apollo budget tight OR backlog elevated
- RED: aborted, Apollo exhausted, or gate-pass rate <50%

*Errors:* [None | description]
```

**Per-path tables (append to the report, always):**
- Path α full ICP write table (Account | HubSpot ID | Segment | Sub-segment | Tier | Confidence)
- Path β reclassification table (Account | HubSpot ID | Was → Became | Confidence delta)
- Path γ eviction table (Account | HubSpot ID | Outcome | Reason)
- Tier 3 hold table (Account | HubSpot ID | Path | Ambiguity)
- Partial gate failure table (Account | HubSpot ID | Path | Missing fields)

Use triple-backtick code blocks for tables.

**Zero-record run:** report `All clean - no candidates today. Pool drained. Run health: GREEN.` + the ✅ Run-log row. No DM.

**Hard failure (abort / MCP unreachable / zero processed against a non-empty queue):** write the report with `Run health: RED` (`RUN ABORTED at Path [α/β/γ] step [X]. [error]. Records processed before abort: [N].`), write the ❌ Run-log row, AND send the one-line failure ping per the Delivery rule at the top of this prompt.

---

## Cross-routine ledger

- **At run start (Pre-flight Tier 3 Hold Exclusion, Edit 3):** read canvas `F0B0AFSB9LN` via `slack_read_canvas`. Parse Tier 3 hold tables for **R0, R1, R2, R4** (sections named `### Rn <Routine name> YYYY-MM-DD - Tier 3 holds added`). Build `TIER_3_EXCLUDE_SET` from the HubSpot ID column across all parsed sections. Apply as a client-side filter on the trigger-query result before any classification work begins. This prevents cross-routine same-day collisions (the 2026-05-06 g.softbank.co.jp pattern).
- **At run end:** append NEW Tier 3 holds added by THIS run to a section titled `### R1 Fresh Enrichment YYYY-MM-DD - Tier 3 holds added`. Match the column format used by the existing R0/R2/R4 tables: `|Date|Routine|Account|HubSpot ID|Reason|Action|`. Create the section if it does not yet exist for today's date. Remove R1 items that were resolved this run (i.e., the underlying record now has a definitive ICP / Other / Flagged classification with a passing gate).
- Append ONE row to canvas's "Run log" table:
  `| YYYY-MM-DD | CRM Guardian - Fresh Enrichment | <status emoji> | <summary> | <links> |`
  Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped.

---

## Delivery

See the "Delivery - quiet on success, ping only on hard failure" rule near the top of this prompt. Summary:

- **Success / partial-recoverable runs:** NO DM. Write the on-disk run report (structure in the "On-disk run report" section) + append the Run-log row to canvas `F0B0AFSB9LN`.
- **Hard failure only** (HubSpot/Slack/Apollo MCP unreachable, abort, or zero processed against a non-empty queue): one-line `:red_circle:` ping to `slack_send_message` channel_id `U0A24D9RJLS` (Cooper's self-DM). Retry the ping once (1s → 2s); if it still fails, the disk report + ❌ Run-log row are the fallback.
- **Body format:** Slack mrkdwn for the failure ping; the on-disk report uses plain markdown with tables in triple-backtick code blocks.

---

## Cross-routine coordination

- **Runs AFTER Routine 0 (9:00 AM CT Import Validator):** R1 sees a smaller, cleaner candidate set.
- **Runs BEFORE Routine 2 (11:00 AM CT Stale Re-Enrichment):** R1's writes update `last_enriched_date`, removing records from R2's stale pool.
- **Pre-score `LIKELY_JUNK` bucket** routes records to Routine 0 for re-investigation if they slipped past the 24-hour window.
