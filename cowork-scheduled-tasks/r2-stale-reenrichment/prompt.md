# CRM Guardian - Stale Re-Enrichment (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget; HubSpot is the source of truth for the stale pool, the Apollo budget tracker lives in `weekly-reports/apollo-budget.json`, and the Tier 3 hold canvas (`F0B0AFSB9LN`) holds cross-task state. Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Daily, 11:00 AM CT, Monday-Friday. Cron: `0 11 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**

Runs THIRD in the daily Cowork cycle (after Import Validator + Fresh Enrichment). Drains the stale-enrichment backlog - companies whose `last_enriched_date` is older than 120 days OR blank (with segment already populated) - so the full CRM rotates through re-enrichment on a 120-day cycle. Does NOT touch fresh accounts (blank segment → R1 Fresh Enrichment) or any other maintenance work.

**Throughput mandate:** This task MUST drain its full daily candidate batch (up to 100 records). Re-enrichment is the ONLY mechanism that catches accounts whose classification has shifted (colo → NeoCloud pivots, fiber op M&A, leadership changes, AI signal upgrades). Failing to process them means stale segment/tier/owner assignments propagate forward, breaking territory routing and signal-scan account prioritization.

**CRM scale baseline:** 3,489 companies total. After excluding ~379 flagged-for-deletion, ~3,110 active. At 120-day rotation = **26 accounts/day steady state**. Initial backlog drains at 100/day cap in ~2 days, then most runs have <30 candidates.

---

## Connected Tools (Cowork)

- **HubSpot MCP** - read/write companies + contacts (incl. `customer_segment`, `flagged_for_deletion_reason`, `account_brief`); territory owner re-derive
- **Apollo MCP** - `apollo_users_api_profile` (budget pre-flight), `apollo_organizations_enrich` (RE_ENRICH_FULL only)
- **Slack MCP** - `slack_send_message` to Cooper (hard-failure ping ONLY), `slack_read_canvas` + `slack_update_canvas`
- **`web_search`** - PRIMARY research path
- **`web_fetch`** - opportunistic enhancement (skip on failure, no penalty)

---

## Delivery - quiet on success, ping only on hard failure

Do NOT DM Cooper a per-run debrief. On a clean or partial-but-recoverable run (including zero-candidate "CRM freshness GREEN" runs and partial runs where records are held for Apollo budget / gate failures), the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r2-stale-reenrichment/...` (the report body structured in the Output section below becomes the on-disk report, NOT a DM), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack/Apollo MCP unreachable, an abort, or zero records processed against a non-empty stale queue - as ONE line:

`:red_circle: CRM Guardian - Stale Re-Enrichment [FAILED/ABORTED] - [one-clause reason].`

Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk report + Run-log row are the fallback. (Historical note: R2 once went silent for 3+ days after April 27. The disk report + Run-log row + digest are now the always-on diagnostic; a true abort still fires the failure ping.)

---

## Reference Files (read at run start)

**Phase 3 primary references (Account Tiering & Segmentation Overhaul - read FIRST):**
- `context/account-tiering/tier-compute-spec.md` - called at Stage 4 of the workflow. Tier is COMPUTED, not assigned. Recompute on every FULL pass regardless of whether sub-segment changed (signal modifiers + open-deal state may have shifted since last run).
- `context/account-tiering/sub-segment-qualification.md` - file 06 source: `context/account-tiering/sub-segment-qualification-full.md`. The 30 active sub-segment values + D3 decision flowchart + D5 v2 protocol questions.
- `context/account-tiering/enrichment-protocols.md` - D5 v2 protocols invoked at Stage 3 to upgrade or downgrade confidence.

**Existing references:**
- `skills/crm-guardian/SKILL.md` (Non-ICP Eviction Rule + safety tiers + Cross-Routine Ledger)
- `routines/_shared/apollo-weekly-budget-spec.md` (850/week Apollo cap, tracker file format, pre-flight + post-run logic - added 2026-05-03, raised 2026-05-06)
- `skills/company-enrichment/SKILL.md` (Step 0C re-enrichment mode, Stages 1-3, Field Resolution Ladder, Completeness Gate Mandatory Fields)
- `skills/segment-classification/SKILL.md`
- `skills/import-processor/SKILL.md`
- `skills/territory-manager/SKILL.md`
- `skills/edge-case-researcher/SKILL.md`
- `context/hubspot/property-schema.md` + `context/hubspot/hubspot-values.md` + `context/hubspot/territory-model.md`
- `context/core/icp-playbook.md` + `context/core/segment-qualification.md`
- `context/segments/` (all 6 segment cheatsheets - Colocation, Fiber, NeoCloud, Network Operator, MSP/Aggregator, **Enterprise** [Multi-DC ICP added 2026-05-11; `enterprise.md` + `enterprise-use-cases.md` for sub-segment classification, scale gate, and lead-angle templates])

---

## 5-Stage Research-First Workflow (Phase 3 reference - RE_ENRICH_FULL path runs all 5)

The RE_ENRICH_FULL path is the same research-first pipeline R1 uses. Each stage is defined in the linked SKILL.md / context files; this section is the at-a-glance map.

- **Stage 0: Identity resolution.** Confirm the entity at the current `domain` is the entity in HubSpot `name` (MISDOMAIN check, Step 0B below).
- **Stage 1a: D1 quick check.** Fast disqualification scan - obvious non-ICP / non-business / dead-domain bail-outs before deep research spend.
- **Stage 1b: Deep research re-populates 7 enriched fields (2-4 sentence cap each per Cooper conciseness rule):**
  - `account_brief`
  - `geographic_focus`
  - `infrastructure_profile` (PRIMARY structured signal for sub-segment classification)
  - `hyperscaler_proximity`
  - `fabric_provisioning_approach`
  - `provisioning_landscape`
  - `recent_news_or_trigger_event` (subject to staleness clearing - see Step 14)
- **Stage 1c: D1 deep check.** Post-research disqualification re-test; catches entities that looked plausibly ICP at Stage 1a but research disconfirms.
- **Stage 2: Segment routing.** Map to one of the 6 customer_segment values (5 operator ICPs + Enterprise + Other / Flagged-for-deletion outcomes).
- **Stage 3: D3 flowchart traversal + D5 protocol questions** per `context/account-tiering/sub-segment-qualification.md` + `context/account-tiering/enrichment-protocols.md`. **May upgrade or downgrade confidence** - D5 v2 protocols are the calibrated-confidence layer that pushes records out of `manual_review_required` whenever positive evidence is unambiguous.
- **Stage 4: Tier computation + signal-heat recomputation** per `context/account-tiering/tier-compute-spec.md`. **Always runs** on every FULL pass, regardless of whether sub-segment changed - modifiers may have shifted (new signals, deal state changes, hs_is_target_account flips, etc.). Heat compute runs alongside tier compute using the same signal-field inputs; heat is NOT frozen by `hs_is_target_account`.
- **Stage 5: HubSpot write + audit.** Completeness Gate → batch write → `last_enriched_date` stamp. Includes `account_tier` (unless `hs_is_target_account = true`) AND `signal_heat` (regardless of `hs_is_target_account`). **NO `maiaedge_value_proposition` write - that field is an outreach concern owned by outreach routines, not enrichment.**

---

## Run-Time Invariants

### A. Timezone
America/New_York for all date math. `last_enriched_date` comparisons use ET calendar dates.

### B. Skip Already-Flagged
Exclude `customer_segment = "Flagged for deletion"` from candidate pool.

### C. Customer Protection
Companies with any closed-won deal are protected. If re-enrichment proposes a downgrade from ICP to non-ICP → escalate to Tier 3, do NOT auto-write the downgrade. A customer record briefly reclassifying as non-ICP is a re-evaluation signal, not a delete signal.

### D. Default to Tier 3 When Uncertain
LOW / MANUAL_REVIEW confidence, conflicting Apollo vs. website data, boundary cases → no write, hold for Cooper.

### E. Idempotency + Date-Bump Discipline
**`last_enriched_date = today (ET)` is the LAST field written and is ONLY written when the gate passes.** Critical scenarios:

| Outcome | Bump `last_enriched_date`? |
|---|---|
| Full re-enrichment, gate passes | YES |
| RE_ENRICH_LIGHT → PARTNER_KEEP confirmed (web_search succeeded) | YES |
| RE_ENRICH_LIGHT → HARD_DELETE / DEAD_DOMAIN (eviction is the resolution) | YES |
| Partial enrichment (gate failed) | NO - stays in stale pool |
| AMBIGUOUS / Tier 3 hold | NO |
| web_search inconclusive AND web_fetch unavailable | NO - record needs another shot |

**Why this matters:** historical bug pattern was bumping the date while leaving fields blank, hiding records from the rotation for 120 days. Don't repeat it.

### F. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest). Tier is COMPUTED at Stage 4 per `context/account-tiering/tier-compute-spec.md`, never assigned ad hoc.
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07).
- `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is now an **ICP segment as of 2026-05-11**. Four sub-segments only: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Hard gate: $1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR in-house net eng + vertical match. Records currently tagged `Enterprise-CustomerSegment` get the same 120-day rotation as other ICP segments (RE_ENRICH_FULL bucket - see Step 0 below).
- AI Colo: `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. Auto-migrate the deprecated `AI - Colocation Operator` value if encountered.
- No em dashes in customer-facing fields. Use hyphens.
- Category descriptor: "Carrier infrastructure" only.

### F.1. Sub-segment value hygiene (Phase 3)

R2 writes ONLY the 30 active sub-segment values defined in `context/account-tiering/sub-segment-qualification.md`. Replace any stale legacy values encountered on read:

- **Network Operator parent:** use `Tier 1 Carrier - Network Op` (NOT the legacy "Tier 1 Global Incumbent"). Auto-migrate on read.
- **NEW 2026-05-14:** `Subsea cable operator` is a real Network Operator sub-segment.
- **NeoCloud parent:** `Crypto to AI - Neoclouds` is INCLUSIVE of both the operator and the landlord business models (Cooper 2026-05-14 clarification). Both pivot types route here.
- **Greenfield is a real sub-segment** under either Data Center Colo Provider or NeoCloud parents - subject to auto-migration on operational milestone (see Greenfield Auto-Migration Rule below).
- **MSP/Aggregator parent:** `Managed Network Services - MSP` (the `- MSP` suffix is the canonical form post-Phase 1.7c.1; the legacy `- Network Operator` suffix is archived). Auto-migrate on read.

**Unknown (segment, sub-segment) pair handling:** if D3 traversal yields a pair not in the 30-value table, fall back to `customer_segment = null` (do NOT write a fabricated parent), set `segmentation_confidence = manual_review_required`, log a warning to the run report ("Unknown sub-segment pair: [segment]/[sub_segment] on [companyId]"), Tier 3 hold.

### F.2. Greenfield Auto-Migration Rule (NEW Phase 3)

When a record currently has `company_sub_segment = "Greenfield"` (under either `Data Center Colo Provider` or `NeoCloud` parent), R2 checks `recent_news_or_trigger_event` and the broader signal corpus for operational state transitions. The pattern catalog R2 matches against is in `context/account-tiering/enrichment-protocols.md` §7 (4-tier catalog: Tier 1 operational milestone -> 20+ phrases including "first site operational" / "ribbon cutting" / "first customer live" / first MW energized; Tier 2 abandonment -> 13 phrases including "abandoned project" / "funding pulled" / "bankruptcy"; Tier 3 construction-progress -> 11 phrases that keep the record in Greenfield; Tier 4 stalled -> 18+ months without progress -> D7 fallback). The summary table below covers the action matrix:

| Detected signal | Action |
|---|---|
| "first site operational" / "ribbon cutting" / "first customer live" / first revenue milestone / first MW energized | **Reclassify into the operational sub-segment** that best fits the now-operational entity (e.g. `AI Signals - colo`, `Modular colo`, `Hyperscale Wholesale`, `Large Scale GPU Neocloud`, etc. - pick via D3 traversal). Write a HubSpot company-level **note** (NOT into `account_brief`) documenting the migration: `"Greenfield → [new sub-segment] auto-migration on operational milestone: [signal text]."` Recompute tier at Stage 4. |
| "abandoned project" / "funding pulled" / "bankruptcy" | Migrate to `customer_segment = "Flagged for deletion"` + set `flagged_for_deletion_reason = "Defunct / out of business: <cite the abandonment/bankruptcy event>"` in the same update (lead with the canonical code per property-schema §2.1; no em dashes). Same note pattern. |
| 18+ months since last Greenfield-relevant signal AND no construction progress (stalled greenfield) | Migrate to `customer_segment = "Flagged for deletion"` + set `flagged_for_deletion_reason = "Stalled greenfield: <cite the 18+ month gap / web-verified stall>"` in the same update (lead with the canonical code per property-schema §2.1; no em dashes). Same note pattern citing staleness. |

Greenfield migrations are Tier 1 writes when the signal evidence is HIGH-confidence, Tier 2 at MEDIUM, Tier 3 hold at LOW.

### F.3. Multi-Marker Classification + No-Default-Manual-Review (Phase 3, Cooper 2026-05-14)

R2 must produce a **best-fit classification with calibrated confidence** on every re-enrichment that completes Stage 1b research. Default-to-manual-review is now a anti-pattern - target `manual_review_required` population <5% of records per run.

- `manual_review_required` fires ONLY when **2+ sub-segments have clear positive evidence AND the D5 v2 tiebreaker protocol fails**. Single-marker ambiguity is NOT enough to hold for manual review - assign best-fit with `medium_7089` confidence and continue.
- **`infrastructure_profile` is the PRIMARY structured signal** for sub-segment classification. When `annualrevenue` (Apollo) conflicts with `infrastructure_profile` (research), **`infrastructure_profile` wins.** Apollo is authoritative for state/country/employee count/funding but NOT for sub-segment routing.

### F.4. hs_is_target_account Handling (Phase 3)

If `hs_is_target_account = true` on a record:
- **Skip the tier write only.** Cooper has manually pinned tier; R2 does not overwrite.
- All other writes proceed normally: segment, sub-segment, signal fields, the 7 enriched fields, owner re-derive, account_brief regeneration, recent_news staleness clearing.
- Log "tier write skipped - hs_is_target_account = true" in run report.

### G. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"` on every `manage_crm_objects` call.

**Pre-authorized writes:** same as Routine 1 - `customer_segment` (including "Flagged for deletion" via eviction / greenfield-abandonment / 18-mo-stall paths), `flagged_for_deletion_reason` (scannable reason code + one sentence of evidence; written in the SAME update as any `customer_segment = "Flagged for deletion"` write, and CLEARED to empty in the same update on any re-upgrade back to an active segment; lead with the canonical reason code per property-schema §2.1), `company_sub_segment`, `account_tier`, `segmentation_confidence`, `last_enriched_date`, `hubspot_owner_id`, `state`, `country`, all 7 enrichment narrative fields (`account_brief`, `infrastructure_profile`, `geographic_focus`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`), plus `domain` (MISDOMAIN auto-correct path only - Tier 1 HIGH / Tier 2 MEDIUM, per the MISDOMAIN check in the RE_ENRICH_LIGHT path). **NOT pre-authorized:** `maiaedge_value_proposition` (outreach concern, not enrichment - owned by cold-email / linkedin-outreach / prospect-research / sdr-pipeline per Cooper 2026-05-14).

**Clear-on-exit:** When any path moves a record OFF `customer_segment = "Flagged for deletion"` back into an active segment (e.g. RE_ENRICH_LIGHT "Surprise ICP" re-route, or a re-classification that reverses a prior flag), clear `flagged_for_deletion_reason` to empty in the SAME HubSpot update that writes the new active segment. A previously-flagged record promoted back to ICP/Other/Partner Target must not retain a stale deletion reason.

**Hard stops:** MaiaEdge own (124293230301). Open deals at `contractsent` or later. `hs_is_target_account = true` blocks tier writes only (other writes proceed).

---

## Trigger Query

HubSpot `search_crm_objects` on COMPANY, two filter groups OR-combined:

**Filter group A - stale enrichment (120+ days old):**
- `last_enriched_date` operator `LT` value = `today(ET) - 120 days`, formatted `YYYY-MM-DD`
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`

**Filter group B - never enriched but segment populated:**
- `last_enriched_date` operator `NOT_HAS_PROPERTY`
- `customer_segment` operator `HAS_PROPERTY`
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`

**Filter group C - rotation pre-spread (load-smoothing; added 2026-06-04):**
Fires ONLY when Filter A + Filter B together return fewer than **40** candidates (the current steady state - the entire active pool was enriched in the compressed May migration window, so ~3,000 records would otherwise all cross 120 days together in late September and overwhelm the 100/day cap). When the stale pool is short, top the daily batch up to 40 records by pulling the OLDEST-enriched active records that are NOT yet 120 days stale:
- `last_enriched_date` operator `HAS_PROPERTY` AND operator `GTE` value `today(ET) - 120 days` (i.e. not already caught by Filter A)
- `customer_segment` operator `HAS_PROPERTY` AND `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`
- Sort `last_enriched_date ASCENDING`; take only enough to bring the run's total candidate count to 40.

Re-enriching these early re-stamps `last_enriched_date` to today, staggering their NEXT due-date across the months ahead instead of bunching in September. Pre-spread YIELDS to genuine stale (A/B) candidates, respects the Apollo sub-cap (50/run) and the 100-record hard cap, and defers any remainder to tomorrow. It runs the normal RE_ENRICH_FULL pipeline (bumps `last_enriched_date` on gate pass) and becomes a natural no-op once the population is evenly distributed across the 120-day window.

**Explicitly NOT in scope** (belongs to Routine 1): records where `customer_segment IS EMPTY`.

**Sort:** `last_enriched_date ASCENDING` (oldest first; null sorts earliest in HubSpot search).

**Cap:** 100 records (full daily batch).

---

## Workflow

### Step 0 - Pre-score triage

Re-enrichment is the highest-volume Apollo consumer in steady state. Pre-score routes records by depth-of-research; **every record still gets its domain investigated** before any classification write.

| Bucket | Definition | Step 1 path |
|---|---|---|
| **RE_ENRICH_FULL** | Already classified as ICP (Colocation / Fiber / NeoCloud / Network Operator / MSP-Aggregator / **Enterprise-CustomerSegment**) AT ANY TIER, OR `customer_segment IS EMPTY` with usable domain | Full pipeline (Stages 1-3 + Apollo) |
| **RE_ENRICH_LIGHT** | Already classified as `Other` or `Unknown`, AND `account_tier` in {TIER_4, TIER_5, UNRANKED} | Eviction-decision path (no Apollo) |
| **RE_ENRICH_LIGHT - Enterprise scale-gate recheck** | Currently tagged `Enterprise-CustomerSegment` BUT account_tier is TIER_5 OR `segmentation_confidence` is `low_5069`/`manual_review_required` OR `account_brief` predates the 2026-05-11 ICP promotion (no mention of Enterprise sub-segment / scale gate / Meijer-style framing). These records were tagged Enterprise under the **old non-ICP framing** and need a scale-gate recheck before they get protected by the 120-day rotation. | Promote to RE_ENRICH_FULL - rerun segment-classification's Enterprise scale gate. If it passes → re-classify with proper sub-segment + tier. If it fails → re-classify as `Other` Tier 5 PARTNER_KEEP (scale-gate failure for an already-CRM'd record is a Tier 2 segment downgrade, NOT eviction - the data is real, the prior framing was wrong). |
| **MAYBE_RECLASSIFY** | Classified as non-ICP but Cooper or recent runs flagged as questionable, OR domain looks ICP but record is stale | Full pipeline (treat like RE_ENRICH_FULL) |
| **RE_ENRICH_DEFER** | `Flagged for deletion` (defensive - shouldn't reach this routine) | Skip |

Surface bucket distribution in the run report header. The RE_ENRICH_LIGHT path is the throughput lever AND the eviction lever - drains rotation pool with 0 Apollo while actively removing confirmed non-partner non-ICP Tier 5 records.

### Step 1 - Path execution

#### RE_ENRICH_FULL + MAYBE_RECLASSIFY records - full re-enrichment

For each candidate (no separate cap):

0. **Step 0B MISDOMAIN check (added 2026-05-03 - runs BEFORE diff check + before any Apollo spend).** Old ICP records can carry longstanding wrong domains (typos, M&A renames, parent-vs-subsidiary confusion) that R0's 24-hour window never caught. Check before re-enriching the wrong entity.
   - **`web_search` `"<domain>"` site identification** - what entity does the domain serve right now? Look for business directory, LinkedIn company page, Wikipedia, news mentions.
   - **OPTIONAL `web_fetch` `https://[domain]`** for confirmation. If 4xx/5xx/timeout, proceed on web_search alone.
   - Compare to HubSpot `name`. Three outcomes:
     - **MATCH** (entity at domain plausibly = HubSpot name, including case/abbreviation/parent-subsidiary differences) → continue to Step 0C diff check normally.
     - **MISDOMAIN** (entity at domain ≠ HubSpot name AND HubSpot name searches cleanly to its own canonical domain `<X>`) → run domain-correction discovery: `web_search "<HubSpot name>" official website` + optional validation `web_fetch` on the candidate URL. On HIGH confidence: write `domain = <X>` (Tier 1). Continue Stage 1-3 enrichment using the CORRECTED domain - the Stage 1b research-driven rewrite of `account_brief` will land pure-prose company description (no routine tag, no leading date); the domain-correction event itself is logged in the on-disk run report, NOT inside `account_brief`. On MEDIUM: same writes Tier 2. On LOW: skip MISDOMAIN, continue.
     - **DEAD-DOMAIN MISDOMAIN** (current domain returns DNS NXDOMAIN / parked / persistent destination 4xx-5xx - NOT proxy block - BUT HubSpot name searches cleanly to a real business with its own canonical domain) → same domain-correction discovery + re-enrichment on the corrected domain. This is the case where a previously valid domain has died and the company has moved.
   - **Cost:** one web_search per candidate (zero Apollo). Adds ~2 seconds per record. At 100-record cap that's ~3 minutes additional runtime - fits in the 11am-noon window.
   - **Why this matters:** prior gap was ICP records with stale wrong domains being re-enriched against the wrong entity every 120 days, persisting wrong segment / sub_segment / Apollo data forever. This step closes the loop.

1. **Step 0C diff check** - compare current HubSpot state against fresh research; detect material changes (segment shift, M&A, leadership change).
2. **Stage 1a D1 quick check** - fast disqualification scan before deep research spend.
3. **Stage 1b deep research** - `web_search` (primary) + OPTIONAL `web_fetch` root + `/about`. Re-populate the 7 enriched fields with a 2-4 sentence cap each: `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event` (subject to Step 14 staleness handling). Per Cooper conciseness rule, do NOT pad to the cap - say it cleanly and stop.
4. **Stage 1c D1 deep check** - post-research disqualification re-test.
5. Run `skills/company-enrichment/SKILL.md` **Stages 1-3** workflow (this is the same content; the Stage labels above are the Phase 3 nomenclature).
6. Run **Apollo `apollo_organizations_enrich`** - authoritative for `state`, `country`, industry, employee count, revenue, funding. Apollo wins when it disagrees with stale HubSpot values. **EXCEPTION (Phase 3):** Apollo `annualrevenue` does NOT override `infrastructure_profile` for sub-segment classification - `infrastructure_profile` is the PRIMARY structured signal.
7. **Stage 2 segment routing** + **Stage 3 D3 flowchart traversal + D5 v2 protocol questions** per `context/account-tiering/sub-segment-qualification.md` and `context/account-tiering/enrichment-protocols.md`. Output: customer_segment + company_sub_segment + segmentation_confidence (calibrated - `manual_review_required` only on 2+ sub-segments with clear positive evidence + D5 tiebreaker failure).
8. **Apply Non-ICP Eviction Rule:**
   - **ICP** → continue.
   - **Non-ICP, PARTNER_KEEP** → `customer_segment = "Other"`, `account_brief = "[2-3 sentence pure-prose description of the entity — what it is, why it's a useful partner reference]. Kept as Partner Target ([reason])."` (no routine tag, no leading date.) Tier 1. Tier computed at Stage 4 (Tier 5 typical for partner keepers). Apply Completeness Gate. Skip cascade.
   - **Non-ICP, NOT PARTNER_KEEP** → `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason` (same update), leading with `No ICP fit` (re-enrichment confirmed no positive evidence for any ICP sub-segment and not a partner/competitor reference) OR `D1 disqualified (no reference value)` if the eviction was a D1 disqualifier match with no reference value. Format: `"<Reason code>: <one concrete sentence of evidence>"` (no em dashes; see property-schema §2.1). `account_brief = "[2-3 sentence pure-prose description of the entity — what it actually is, why it falls in [discovered category]]. Re-enrichment confirmed non-ICP, non-partner; flagged for deletion."` (no routine tag, no leading date.) Tier 2. Apply Completeness Gate. Skip cascade.
   - **AMBIGUOUS / LOW** (and only when 2+ sub-segments have positive evidence per F.3) → `skills/edge-case-researcher/SKILL.md`; if still uncertain → Tier 3 hold (NO date bump). Single-marker ambiguity assigns best-fit + `medium_7089`, NOT Tier 3.
9. **Greenfield auto-migration check (Phase 3).** If incoming `company_sub_segment = "Greenfield"`, apply the F.2 migration rule before continuing - operational milestone, abandoned/bankrupt, or 18+ month stall.
10. Apply `skills/import-processor/SKILL.md` enum mapping. **Enum case-sensitivity:** writes use `value` not `label` per `context/hubspot/property-schema.md`. **Sub-segment writes must use one of the 30 active values** in `context/account-tiering/sub-segment-qualification.md`; unknown pairs fall back to `customer_segment = null` + manual_review_required (per F.1).
11. **Field Resolution Ladder for state/country.** If Apollo returned null on state/country: Apollo → website → LinkedIn About → WHOIS. Tier 1 if resolved at HIGH (steps 1-2), Tier 2 at MEDIUM (step 3), Tier 3 hold only if all four return null. State resolution must happen BEFORE the Completeness Gate.
12. **Stage 4 tier + heat computation (Phase 3, MANDATORY EVERY RUN; heat added 2026-05-20).** Compute `account_tier` per `context/account-tiering/tier-compute-spec.md`. **Run this step on every FULL pass regardless of whether sub-segment changed** - signal modifiers, open-deal state, and hs_is_target_account flips may have shifted since last enrichment. **If `hs_is_target_account = true` on the record, SKIP the tier write only** (per F.4); all other writes proceed.

    Also compute `signal_heat` per `context/account-tiering/tier-compute-spec.md` §11.5. **Freshness anchor (post-2026-05-28):** `last_signal_date` stores the EVENT DATE (when the news/funding/hire actually happened), not detection date. **HubSpot enum is Title Case:** `Hot` / `Warm` / `Cool` / `Cold`. Inlined here:

    ```
    signal_heat is computed top-down, first match wins:

    Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
           OR signal_count_last_30d >= 2
           OR account has any associated open deal past `appointmentscheduled`

    Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

    Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

    Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

    Override behavior:
    - hs_is_target_account = true does NOT freeze signal_heat.
      Tier is rep-locked; heat always reports the truth.

    Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
    Output: enum `Hot` | `Warm` | `Cool` | `Cold` (Title Case per HubSpot).
    ```

    Heat writes proceed regardless of `hs_is_target_account` (heat is not frozen by the target-account flag). Idempotent: no write if `computed_heat == current_heat`. On change, add HubSpot company note `"Heat <old> -> <new> on YYYY-MM-DD by R2 RE_ENRICH_FULL: <reason>"` (Title Case heat values in the note). RE_ENRICH_LIGHT eviction paths do NOT touch `signal_heat` (eviction supersedes).
13. **Stage 5 Completeness Gate + write.** Verify all REQUIRED fields per Mandatory Fields table in `skills/company-enrichment/SKILL.md`. **Gate passes → full batch write including `last_enriched_date = today (ET)`. Gate fails → partial write only; date stays at prior value (could be blank or 120+ days old).** Surface in the run report under "Partial Enrichment - held for next run." **DO NOT write `maiaedge_value_proposition`** - it's an outreach concern, not an enrichment field.
14. Re-derive `hubspot_owner_id` from refreshed `state` per `context/hubspot/territory-model.md`. Tier 2 if state changed on a deal-protected account.
15. If `customer_segment` changed: execute Segment Change Cascade - re-derive sub-segment, recompute tier per Stage 4 spec, confidence, infrastructure_profile; sync segment to associated contacts (Tier 1).
16. **account_brief regeneration assurance (added 2026-05-03; Phase 3 cap clarification).** R2 FULL is the every-120-days mechanism for guaranteeing account_brief freshness. ALWAYS regenerate `account_brief` via `skills/account-brief/SKILL.md` on every FULL pass that reaches the Completeness Gate. Per Phase 3 + Cooper conciseness rule, `account_brief` honors the 2-4 sentence cap on the enriched fields.
17. **recent_news_or_trigger_event staleness handling (added 2026-05-03; simplified 2026-05-28).** R2 owns staleness clearing for the Signal Scan field. **Read `last_signal_date` directly from HubSpot** — no more string parsing of the narrative (the `[YYYY-MM-DD]` prefix convention was retired 2026-05-28; event date now lives structurally in `last_signal_date`).
   - If `last_signal_date` is **≤90 days old** → leave `recent_news_or_trigger_event` alone (the news is still considered fresh).
   - If `last_signal_date` is **>90 days old** AND no Signal Scan write has occurred in the last 7 days for this account → **clear `recent_news_or_trigger_event`** (write empty string) **AND clear `last_signal_date`** (write null) so the structured + narrative pair stay consistent. Stale news showing as current is worse than no news. Log to run report under "Recent news cleared (stale)".
   - If `last_signal_date` is >90 days old AND a Signal Scan write occurred in the last 7 days for this account → leave both fields alone (Signal Scan just touched it; trust the freshness).
   - If `last_signal_date` is null but the narrative is populated → likely a pre-2026-05-28 record that has not been re-enriched yet. Leave both alone; the next R2 FULL pass + the one-time backfill task will reconcile it. Log to run report under "Legacy format pending backfill" for visibility.
18. Apply Apollo Weekly Budget post-run update per `routines/_shared/apollo-weekly-budget-spec.md` - increment `consumed`, update `by_routine.stale-reenrichment`, append history entry, commit + push `weekly-reports/apollo-budget.json`.

#### RE_ENRICH_LIGHT records - eviction-decision path (NO Apollo)

These are records currently `Other`/`Unknown`/non-ICP at low tiers. Verify each is STILL a legitimate keeper (Partner Target) or finally flag-for-deletion the ones that aren't.

For each candidate:

1. **`web_search`** for entity identification - primary path.
2. **OPTIONAL `web_fetch`** root + `/about`.
2a. **MISDOMAIN check (BEFORE applying eviction rule).** If entity at the domain differs from HubSpot `name` AND the HubSpot name searches cleanly to its own canonical domain → MISDOMAIN. Run domain-correction discovery: `web_search "<HubSpot name>" official website` + optional validation `web_fetch`. On HIGH: write `domain = <discovered>` (Tier 1) and re-route to RE_ENRICH_FULL. FULL-path Stage 1b will rewrite `account_brief` as pure prose against the corrected entity; FULL-path Completeness Gate governs the date write (do NOT bump in LIGHT path). The domain-correction event itself is logged in the on-disk run report, NOT inside `account_brief`. On MEDIUM: same writes Tier 2. On LOW: skip MISDOMAIN, continue.
2b. **MISDOMAIN check on dead domain.** If web_search/web_fetch reveals a real DNS NXDOMAIN / parked / persistent destination 4xx-5xx BUT HubSpot name searches cleanly to a real business with its own canonical domain → MISDOMAIN. Same discovery + re-route. This is the case where a previously valid domain has died and the company has moved.
3. Apply Non-ICP Eviction Rule:
   - **PARTNER_KEEP** → `account_brief = "[2-3 sentence pure-prose description of the entity]. Re-verified as Partner Target ([reason]); was previously [old_segment]."` (no routine tag, no leading date.) Bump `last_enriched_date = today (ET)`. Tier 1.
   - **HARD_DELETE** → `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Hard junk / non-business: <one concrete sentence>"` (same update; lead with the canonical code per property-schema §2.1; no em dashes). `account_brief = "[2-3 sentence pure-prose description of [discovered_entity] — what it is, why it falls in [category]]. Was previously [old_segment]; flagged for deletion."` (no routine tag, no leading date.) Tier 2 + bump date.
   - **DEAD_DOMAIN** (real, not proxy) → `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Dead domain: <one concrete sentence>"` (same update; lead with the canonical code per property-schema §2.1; no em dashes), `account_brief`. Tier 2 + bump date.
   - **Surprise ICP** (company has pivoted) → re-route to RE_ENRICH_FULL within this run. FULL-path gate governs date write. **Clear-on-exit:** if this record was previously `Flagged for deletion`, clear `flagged_for_deletion_reason` to empty in the same update that writes the new active segment.
   - **AMBIGUOUS** → Tier 3 hold. **No date bump.**
   - **Web research failed** (web_search inconclusive AND web_fetch unavailable) → Tier 3 ("re-verification failed - held for next run"). **No date bump.**
4. Date bump rule (NOT blanket): bump ONLY on PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN clear resolutions.

---

## Safety Tiers

| Scenario | Tier |
|-----|-----|
| HIGH-confidence refresh, no segment change | Tier 1 |
| HIGH-confidence segment change, no open deals | Tier 1 + cascade |
| MEDIUM-confidence refresh | Tier 2 |
| Segment change on deal-protected account | Tier 3 |
| Downgrade from ICP → non-ICP on customer (closed-won) | Tier 3 hard stop |
| LOW / MANUAL_REVIEW after edge-case-researcher | Tier 3 |

**Pool-exhaustion signal:** if Filter A + B return fewer than 50 candidates, CRM is fully rotated within 120 days - log "CRM freshness: GREEN". But do NOT idle: when A + B are short, Filter group C (rotation pre-spread) tops the batch up to 40 of the oldest-enriched records to smooth the load curve toward the September cliff. So a low A/B count is expected and healthy; the run should still process ~40 pre-spread records until the population is evenly distributed across the 120-day window (after which C also returns near-zero and the run is genuinely quiet). Pre-spread is real rotation work, not fabricated work.

---

## Caps & Budgets

- **Record cap:** 100 accounts/run.
- **Apollo credits (changed 2026-05-03):** dual-cap enforcement.
  - **Weekly cap (NEW, primary):** per `routines/_shared/apollo-weekly-budget-spec.md`. Read `weekly-reports/apollo-budget.json` at run start. R2's sub-cap is **50 credits per run** (5 runs/week = 250/week, ~29% of the 850/week global cap; raised from 30 → 50 on 2026-05-21 - see footnote below). If the global weekly cap has been hit (`consumed >= 850`), skip Apollo for this run entirely - process RE_ENRICH_LIGHT only (0 credits) and surface in DM "Apollo weekly cap hit - RE_ENRICH_FULL deferred to next reset Monday [date]". If `available < 50`: scale R2's budget down to `available`. Prioritize Apollo spend on oldest-stale FULL records first.

> **2026-05-21:** R2 sub-cap raised from 30 → 50 cr/run to support 120-day rotation at 5,000 active records (need ~42 records/day FULL; 50/day buys 67% headroom). Sourced from R1's reduction in the same change. Global weekly cap unchanged at 850.
  - **Monthly cap (kept, secondary):** call `apollo_users_api_profile`. Confirm `(monthly_consumed + R2_budget) <= 6000`. If monthly is depleted, skip Apollo regardless of weekly state.
  - Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded`.
  - Post-run: update `weekly-reports/apollo-budget.json` per the spec - increment `consumed`, append history entry, commit + push.
- **HubSpot writes:** **batch cap 10 `objects` per `manage_crm_objects` call.** Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch after 3 consecutive 429s.
- **web_search:** ~3-5 per FULL record + 2 per LIGHT record. ≥1s between searches.
- **web_fetch:** opportunistic only.
- **Session pacing:** 100 records/page on HubSpot reads, ≥1s between pages.
- **Contact-segment sync:** when cascade fires, sync to associated contacts in a second batch update; do not issue one-contact-per-call writes.

---

## On-disk run report (structure)

Write this report to `weekly-reports/YYYY-MM-DD/r2-stale-reenrichment/run-report.md`. This is the durable record the CRM Ops Daily Digest reads from - it is NOT sent as a DM. Keep the structure intact.

**Header:**
```
CRM Guardian - Stale Re-Enrichment - [YYYY-MM-DD] - [N] Tier 2 flagged, [M] Tier 3 held
```

**Body:**
```
Run summary: [X]/[100] processed · [FULL/LIGHT/RECLASSIFY/DEFER distribution] · [Tier 1 / 2 / 3 counts] · Apollo: [credits used]/[remaining] · Freshness: [GREEN/YELLOW/RED]

What needs Cooper's attention:
- [If Tier 3 > 0] [N] Tier 3 holds - see tables below
- [If Tier 2 flagged > 0] [M] eviction Tier 2 - Filter HubSpot Companies → customer_segment = "Flagged for deletion"
- [If segment changes > 0] [S] segment transitions to verify - see tables below
- [If Partial Enrichment > 0] [P] records partial-enriched (gate failed); will retry next run

Run health: [GREEN / YELLOW / RED]

Errors: [None | description]
```

**Detail tables (append to the report):** Segment changes table (old → new + reason) / Tier 3 held / Partial Enrichment.

**Pool-exhausted run:** report `CRM freshness GREEN - only [N] stale records (steady state). [Counts]. Run health: GREEN.` + the ✅ Run-log row. No DM.

**Hard failure (abort / MCP unreachable / zero processed against a non-empty queue):** write the report with `Run health: RED` (`RUN ABORTED at Step [X]. [error]. Records processed: [N].`), write the ❌ Run-log row, AND send the one-line failure ping per the Delivery rule near the top of this prompt.

---

## Cross-routine ledger

- **At run start:** read canvas `F0B0AFSB9LN`. Drain Routine 2 items - re-evaluate; resolve and remove if Cooper acted manually.
- **At run end:** append NEW Tier 3 holds with `[YYYY-MM-DD]`. Append ONE row to "Run log":
  `| YYYY-MM-DD | CRM Guardian - Stale Re-Enrichment | <status emoji> | <summary> | <links> |`
  Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped.

---

## Delivery

See the "Delivery - quiet on success, ping only on hard failure" rule near the top of this prompt. Summary:

- **Success / partial-recoverable runs:** NO DM. Write the on-disk run report (structure in the "On-disk run report" section) + append the Run-log row to canvas `F0B0AFSB9LN`.
- **Hard failure only** (HubSpot/Slack/Apollo MCP unreachable, abort, or zero processed against a non-empty queue): one-line `:red_circle:` ping to `slack_send_message` channel_id `U0A24D9RJLS`. Retry the ping once (1s → 2s); if it still fails, the disk report + ❌ Run-log row are the fallback.
- **Body format:** Slack mrkdwn for the failure ping; the on-disk report uses plain markdown with tables in triple-backtick code blocks.

---

## Cross-routine coordination

- **Runs AFTER Routine 1 (10:00 AM CT):** R1's writes update `last_enriched_date` so freshly-enriched records aren't re-evaluated.
- **Runs BEFORE Routine 4 (12:00 PM CT Flagged Consolidation):** R2's HARD_DELETE writes feed R4's contact consolidation queue.
