# Mass Re-Enrichment Sweep (Cowork Manual-Trigger Task)

**Execution model:** Single unified, reusable prompt for full-CRM re-enrichment sweeps. Fired manually from inside the CRM Guardian Cowork project whenever the framework changes meaningfully and existing enrichment needs validation against the new model. Each fire processes a batch of records and self-resumes across Cowork chats via HubSpot's `last_enriched_date` and a sweep kickoff date.
**Owner:** Cooper Kennedy (Slack DM: `U0A24D9RJLS`)
**Platform:** Cowork-only
**Apollo budget:** Uncapped during sweep window; track per-batch + cumulative; restore standard 850/wk enforcement post-sweep
**Tool type:** Permanent reusable capability — not tied to a specific framework migration
**First created:** 2026-05-18 (post-Phase-3 framework refinement of 2026-05-14)

---

## 1. When to fire this prompt

Fire this sweep when:
1. The framework (`context/account-tiering/tier-compute-spec.md`, `sub-segment-qualification.md`, `enrichment-protocols.md`, or `Operating Principles` in `CLAUDE.md`) changed meaningfully and existing enriched records need re-validation under the new model
2. A new sub-segment was added that retroactively requires reclassification of existing records
3. Tier-compute defaults table changed (new ceiling/floor, new sub-segment-tier mapping)
4. A data-quality audit reveals widespread drift that steady-state R2 won't catch within an acceptable window
5. Cooper explicitly requests "full CRM re-enrichment"

**Do not fire** for routine drift correction — that's R-Tier-Audit's (weekly) and R2 Stale Re-Enrichment's (daily) job. This sweep is the heavy hammer.

---

## 2. Sweep parameters (Cooper sets at kickoff)

Before firing the first batch of a sweep, Cooper fills in these parameters and they remain constant for the duration of that sweep:

```
SWEEP_NAME              = "<short slug, e.g. 2026-05-18-post-phase-3-framework>"
SWEEP_KICKOFF_DATE      = "<YYYY-MM-DD of first batch, e.g. 2026-05-18>"
BATCH_SIZE              = 50    # records per chat session; bump to 75-100 if context headroom, drop to 25 if research is heavy
VERIFY_DEPTH            = "leverage-and-patch"   # alternative: "full-rebuild" (forces FULL path on every record)
APOLLO_ENFORCEMENT      = "disabled"   # set to "enabled" if you want to respect the 850/wk cap even during sweep
SEGMENT_SCOPE           = "all_active_icp"   # or specify a single segment: "Fiber Operator", "NeoCloud", etc.
```

The continuation token (provided at end of every batch DM) embeds these values so the next Cowork chat inherits them automatically.

**SWEEP_KICKOFF_DATE is the gate.** Records with `last_enriched_date >= SWEEP_KICKOFF_DATE` are excluded from the trigger query. Once a record is processed in this sweep, its date stamps to today, which is always `>= kickoff`, so it falls out of the pool naturally.

---

## 3. How Cooper uses this

### Kickoff (first batch of a new sweep)

1. Decide on the four parameters above (use today's date as kickoff)
2. Open the CRM Guardian Cowork project, start a new chat
3. Paste this entire prompt + a single line at the top specifying the parameters, like:
   ```
   Run Mass Re-Enrichment Sweep with: SWEEP_NAME="2026-05-18-post-phase-3-framework", SWEEP_KICKOFF_DATE="2026-05-18", BATCH_SIZE=50, VERIFY_DEPTH="leverage-and-patch", APOLLO_ENFORCEMENT="disabled", SEGMENT_SCOPE="all_active_icp".
   ```
4. Fire. The session processes one batch and ends with a copy-pasteable continuation token

### Continuation (every subsequent batch)

1. When the chat reports batch complete OR context fills up
2. Open a new Cowork chat in CRM Guardian
3. Paste the continuation token (provided at end of each batch DM and chat output)
4. Repeat until DM reads `:white_check_mark: SWEEP COMPLETE - 0 records remaining`
5. Run the final verification pass (§11)
6. Restore steady-state R2 + Apollo enforcement

No state-passing is required beyond the four sweep parameters in the continuation token — HubSpot's `last_enriched_date` tracks per-record progress.

---

## 4. Required reading at every batch start

The runtime MUST load these files BEFORE any HubSpot calls. Re-reading every batch is cheap; misclassification from skipped reads is expensive.

**Phase 3 primary references (single source of truth for the framework):**
- `CLAUDE.md` — Operating Principles, inverted tier convention, `last_enriched_date` stamping policy, `hs_is_target_account` tier-freeze, `account_tier_legacy` archived, `maiaedge_value_proposition` out-of-scope
- `context/account-tiering/tier-compute-spec.md` — `compute_tier()` algorithm + 30-row defaults table + 6 signal modifiers + null/unknown-pair fallbacks
- `context/account-tiering/sub-segment-qualification.md` — the 30 active sub-segment values + D3 flowchart + D5 questions
- `context/account-tiering/enrichment-protocols.md` — D5 v2 protocols §6 (per-sub-segment evidence tables) + §6a (NC1/NC2/NC3 threshold matrix) + §7 (Greenfield migration patterns)

**Skill + context references:**
- `skills/crm-guardian/SKILL.md` — Non-ICP Eviction Rule + safety tiers
- `skills/company-enrichment/SKILL.md` — 5-stage workflow, Field Resolution Ladder, Completeness Gate
- `skills/segment-classification/SKILL.md`
- `skills/territory-manager/SKILL.md`
- `skills/edge-case-researcher/SKILL.md`
- `skills/account-brief/SKILL.md`
- `context/hubspot/property-schema.md` — write formats, multi-select enum syntax
- `context/hubspot/hubspot-values.md` — case-sensitive internal values
- `context/hubspot/territory-model.md`
- `context/segments/` — all 6 segment cheatsheets

---

## 5. Operating principles (apply to every record)

1. **Multi-marker classification.** `infrastructure_profile` is the PRIMARY structured signal for sub-segment routing. When Apollo `annualrevenue` conflicts with `infrastructure_profile`, `infrastructure_profile` wins.
2. **No-default-manual-review.** Target `manual_review_required` <5% of records per batch. Fires ONLY when 2+ sub-segments have clear positive evidence AND the D5 v2 tiebreaker fails. Single-marker ambiguity → assign best-fit + `medium_7089` confidence.
3. **2-4 sentence conciseness cap** on `account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`. Don't pad to the cap.
4. **`maiaedge_value_proposition` is OUT OF SCOPE.** Do not read it, write to it, or factor it into decisions. Outreach skills own it.
5. **`account_tier_legacy` is ARCHIVED.** Do not read, write, or reference.
6. **Aggressive `customer_segment = "Flagged for deletion"`** for records with no positive evidence for any ICP sub-segment. `Other` is reserved for D1 disqualifier matches useful as competitive/partner references. **Mandatory companion write:** every time you set `customer_segment = "Flagged for deletion"`, set `flagged_for_deletion_reason` in the SAME update, leading with one of the 7 canonical codes + a colon + one concrete sentence of evidence (no em dashes). Reason-code mapping for this sweep: dead/non-resolving domain → `Dead domain`; non-business / junk TLD / spoofed-brand / test record → `Hard junk / non-business`; D1 disqualifier with no competitive/partner value → `D1 disqualified (no reference value)`; researched but no positive evidence for any of the 6 ICP sub-segments → `No ICP fit`; confirmed defunct / ceased ops / absorbed post-acquisition → `Defunct / out of business`; stalled greenfield (see #7) → `Stalled greenfield`. The scannable code lives in this field; the 2-4 sentence prose rationale stays in `account_brief`. Full spec: `context/hubspot/property-schema.md` §2.1. **Clear-on-exit:** any record this sweep moves OFF "Flagged for deletion" back into an active ICP segment (re-upgrade) must clear `flagged_for_deletion_reason` to empty in the same write.
7. **Greenfield auto-migration** per `enrichment-protocols.md` §7 — operational milestone → operational sub-segment; abandonment/bankruptcy → Flagged for deletion (reason `Defunct / out of business`); 18+ month stall → Flagged for deletion (reason `Stalled greenfield`). Both eviction branches set `flagged_for_deletion_reason` per #6.
8. **`hs_is_target_account = true` tier freeze.** Skip `account_tier` write only; all other writes proceed (segment, sub-segment, 7 enriched fields, signal fields, owner re-derive).
9. **Idempotent.** Re-running the sweep over the same record produces the same end state.
10. **Tier recompute ALWAYS runs** at the end of each record's pass, regardless of which path it took (signal modifiers + open-deal state + `hs_is_target_account` flips may have shifted).

---

## 6. Trigger query (run at start of every batch)

HubSpot `search_crm_objects` on COMPANY. Construct the filters dynamically based on sweep parameters:

```
Filters (AND):
  customer_segment IN [
    "NeoCloud",
    "Data Center Colo Provider",
    "Fiber Operator",
    "Network Operator(Tier 1 / VNO)",
    "MSP/Aggregator",
    "Enterprise-CustomerSegment"
  ]
  -- If SEGMENT_SCOPE != "all_active_icp", filter to that single segment only.

  customer_segment NEQ "Flagged for deletion"
  type NEQ "Customer"
  company_id NEQ 124293230301   -- MaiaEdge own record

  (
    last_enriched_date IS NULL
    OR last_enriched_date LT "<SWEEP_KICKOFF_DATE>"
  )

Sort: last_enriched_date ASCENDING (oldest first; NULL sorts earliest)
Cap: BATCH_SIZE
```

### 6.1 Pagination

HubSpot returns up to 100 records per page. If `BATCH_SIZE > 100`:
- Paginate (`page=1`, `page=2`, etc.) until aggregated record count ≥ BATCH_SIZE OR no more pages
- ≥1s between page calls
- Realistic ceiling: 200 records/batch (context budget gets tight beyond that)

### 6.2 Pool exhaustion signal

If the trigger query returns 0 records: sweep is complete. DM `:white_check_mark: SWEEP COMPLETE` (see §10 for full DM template), run the final verification pass (§11), stop firing this prompt.

### 6.3 Concurrency warning

**Do not fire two batches simultaneously in two different Cowork chats.** HubSpot does not support transactions; concurrent writes to the same record will race. Wait for one batch to complete before firing the next.

---

## 7. Per-record verify-and-patch workflow

For each of the BATCH_SIZE records, run this decision tree:

### 7.1 Read current state from HubSpot

Pull these properties:
- Identity: `name`, `domain`, `company_id`
- Classification: `customer_segment`, `company_sub_segment`, `segmentation_confidence`
- Tier + override: `account_tier`, `hs_is_target_account`
- Heat: `signal_heat`
- Signal persistence: `last_signal_score`, `last_signal_date`, `signal_count_last_30d`
- Enriched narrative (the 7): `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`
- Apollo-authoritative: `state`, `country`, `annualrevenue`, `numberofemployees`, `industry`
- Lifecycle: `last_enriched_date`, `hubspot_owner_id`
- Open-deal state: count of associated deals past `appointmentscheduled` not in `closedwon` / `closedlost`
- **Closed-won state**: count of associated deals in `closedwon` stage. >0 means this is a customer — apply customer protection (§7.5)
- Last engagement date (most recent activity)

### 7.2 Customer protection guard (runs BEFORE classification)

If the record has `closedwon` deals (i.e. it's a customer), tag it `is_customer = true` for the rest of the workflow. This unlocks the closed-won protection in §7.5: any proposed downgrade from ICP → non-ICP becomes a Tier 3 HARD STOP (escalate to Cooper, do not write the downgrade).

A customer record briefly reclassifying as non-ICP is a re-evaluation signal, not a delete signal. Customer ICP downgrades require human review.

### 7.3 Identity sanity check (MISDOMAIN)

One `web_search "<domain>"` to confirm the entity at `domain` matches HubSpot `name`. Outcomes:

- **MATCH** → continue to §7.4
- **MISDOMAIN** (entity at domain ≠ HubSpot name AND HubSpot name searches cleanly to its own canonical domain) → domain-correction discovery. `web_search "<HubSpot name>" official website` + optional validation `web_fetch`. On HIGH confidence: write `domain = <new>` (Tier 1), append a one-sentence correction note to `account_brief`. Continue §7.4 using the corrected domain. On MEDIUM: same writes Tier 2. On LOW: skip MISDOMAIN, continue with existing domain.
- **DEAD-DOMAIN MISDOMAIN** (current domain returns NXDOMAIN / parked / persistent 4xx-5xx, AND HubSpot name searches cleanly to a real business) → same correction flow.

MISDOMAIN correction routes the record to FULL path automatically — research the new entity from scratch.

### 7.4 Existing data assessment

Score the current record across these checks:

| Check | Pass criteria | Fail action |
|---|---|---|
| `customer_segment` is one of the 6 active ICPs | "NeoCloud", "Data Center Colo Provider", "Fiber Operator", "Network Operator(Tier 1 / VNO)", "MSP/Aggregator", "Enterprise-CustomerSegment" | Re-classify (FULL path) |
| Sub-segment in the 30 active values | `company_sub_segment` in `sub-segment-qualification.md` | Auto-migrate legacy values per §7.4a; counts as MEDIUM path trigger if anything else also failed |
| All 7 enriched fields non-empty | Each has >0 characters | 1-3 missing → MEDIUM; 4+ missing → FULL |
| 7 fields are 2-4 sentence range | ≥20 chars, ≤~600 chars each | Over-long → trim (LIGHT); empty → fill (MEDIUM/FULL per count) |
| `infrastructure_profile` consistent with `customer_segment` | E.g., "Fiber Operator" segment + profile showing route miles / POPs | Conflict → FULL re-research |
| `recent_news_or_trigger_event` not stale | Date prefix `[YYYY-MM-DD]` ≤90 days old OR Signal Scan wrote in last 7 days | Stale → clear field (LIGHT side-action; doesn't bump the path) |
| `account_brief` framework-consistent | None of the legacy-strings list (§7.4b) | Detected → regenerate (MEDIUM) |
| Apollo data freshness | `state` + `country` populated; last Apollo refresh ≤180 days | Stale → 1 Apollo call (MEDIUM); missing → Field Resolution Ladder (FULL) |

#### 7.4a Sub-segment auto-migration table (deterministic 1-to-1 mappings)

Apply automatically before classification logic runs. These are not research-triggered; just rewrite the value.

| Legacy value | New value | Parent segment |
|---|---|---|
| `Tier 1 Global Incumbent` | `Tier 1 Carrier - Network Op` | Network Operator(Tier 1 / VNO) |
| `AI - Colocation Operator` | `AI Signals - colo` | Data Center Colo Provider |
| `Managed Network Services - Network Operator` | `Managed Network Services - MSP` | MSP/Aggregator |

If a record's only framework issue is one of these mappings AND all other checks pass: LIGHT path.

#### 7.4b Legacy-string detection for `account_brief`

Strings that indicate `account_brief` was written under a pre-Phase 3 framework. If detected: regenerate (MEDIUM path).

- "Tier 1 Global Incumbent" — retired sub-segment label
- "AI - Colocation Operator" — retired sub-segment label
- "Managed Network Services - Network Operator" — retired sub-segment label
- "Co-op/consortium" — retired enum value
- "External Extension - Network operator" — retired enum value
- "Internal + external unification - Network Operator" — retired enum value
- "account_tier_legacy" — archived field reference
- "maiaedge_value_proposition" or "value proposition" framed as an enrichment output — out-of-scope concept
- "Enterprise" framed as non-ICP — Enterprise became an ICP segment 2026-05-11
- 5-tier old tiering language ("white-glove rep weekly attention" without the current modifier framing, etc.)
- Any reference to the pre-2026-05-14 framework operating principles

### 7.4c Decision: LIGHT / MEDIUM / FULL / HOLD

Based on §7.4 check outcomes:

| Path | Trigger | Cost per record |
|---|---|---|
| **LIGHT** | All 7 fields present, framework-consistent, sub-segment in 30 active (or deterministic auto-migration applied), `recent_news` fresh, `account_brief` framework-consistent, Apollo data fresh | 1 web_search for material drift check, recompute tier, bump date |
| **MEDIUM** | 1-3 enriched fields missing, OR sub-segment needs auto-migration AND something else minor, OR `account_brief` references legacy concepts, OR `recent_news` stale, OR Apollo stale | 2-3 web_searches to fill gaps + optional 1 Apollo, recompute tier, bump date |
| **FULL** | 4+ enriched fields missing OR contradictions found OR MISDOMAIN correction applied OR invalid `customer_segment` OR `infrastructure_profile` ↔ `customer_segment` conflict | Full 5-stage research-first workflow (3-5 web_searches + 1 Apollo), recompute tier, bump date |
| **HOLD** | Customer protection triggered (closed-won deal + proposed ICP→non-ICP downgrade) OR true 2+ sub-segment ambiguity after D5 tiebreaker OR Completeness Gate fails after FULL pass | No write, no date bump. Tier 3 hold added to canvas `F0B0AFSB9LN`; D7 picks up next weekly run. |

If `VERIFY_DEPTH = "full-rebuild"` is set in sweep params, treat every record as FULL regardless of §7.4 results.

### 7.5 Execute the chosen path

#### LIGHT
1. One `web_search "<company name>" 2025 OR 2026` to spot-check material recent news
2. If recent news found and not already in `recent_news_or_trigger_event`: append a 1-sentence update with `[YYYY-MM-DD]` prefix (2-4 sentence cap on the field overall)
3. Apply sub-segment auto-migration from §7.4a if applicable
4. Run tier recompute (§7.6)
5. Write batch (tier + recent_news if updated + auto-migration if applicable + `last_enriched_date = today (ET)`)
6. Add HubSpot company note (§7.7)

#### MEDIUM
1. For each missing/stale field, targeted `web_search` to fill the gap. Respect 2-4 sentence cap.
2. Apply sub-segment auto-migration if applicable
3. If `account_brief` matched legacy-string detection, regenerate via `skills/account-brief/SKILL.md`
4. If `recent_news_or_trigger_event` stale (>90d, no Signal Scan in last 7d): clear the field
5. If Apollo data stale (>180d) and state/country/headcount/funding needed: one `apollo_organizations_enrich` call
6. Run tier recompute (§7.6)
7. Write batch
8. Add HubSpot company note (§7.7)

#### FULL
1. Full 5-stage research-first workflow per `skills/company-enrichment/SKILL.md`:
   - **Stage 1a** D1 quick check (fast disqualification scan)
   - **Stage 1b** Deep research populates all 7 enriched fields (2-4 sentence cap each)
   - **Stage 1c** D1 deep check (post-research disqualification)
   - **Stage 2** Segment routing to one of the 6 ICPs OR Other OR Flagged for deletion
   - **Stage 3** D3 flowchart + D5 v2 protocols → sub-segment + `segmentation_confidence`
2. Apollo `apollo_organizations_enrich` (authoritative for state/country/employee count/funding; NOT for sub-segment routing — `infrastructure_profile` wins per §5.1)
3. Apply Non-ICP Eviction Rule:
   - ICP → continue. **If the record was previously `customer_segment = "Flagged for deletion"` and is now re-upgrading to an active ICP segment, clear `flagged_for_deletion_reason` to empty in the same write (clear-on-exit).**
   - Non-ICP PARTNER_KEEP → `customer_segment = "Other"`, typical Tier 5 (Other is not "Flagged for deletion" — do NOT set `flagged_for_deletion_reason`; if the record was previously flagged, clear it on this transition)
   - Non-ICP NOT PARTNER_KEEP → `customer_segment = "Flagged for deletion"` + companion `flagged_for_deletion_reason` in the SAME update, code per §5 #6 (typically `No ICP fit` for a researched non-fit, `D1 disqualified (no reference value)` for a D1 match with no reference value, `Dead domain` / `Hard junk / non-business` / `Defunct / out of business` as applicable). Reason leads with the code + colon + one evidence sentence; no em dashes.
   - **If `is_customer = true` (from §7.2) AND classification proposes ICP → non-ICP:** STOP, route to HOLD path
   - True 2+ sub-segment positive evidence + D5 tiebreaker failure → `edge-case-researcher`; if still uncertain → HOLD path
4. Greenfield auto-migration per `enrichment-protocols.md` §7 (operational milestone / abandonment / stall)
5. Field Resolution Ladder for state/country (Apollo → website → LinkedIn About → WHOIS)
6. Re-derive `hubspot_owner_id` from refreshed `state` per `territory-model.md`
7. Regenerate `account_brief`
8. Run tier recompute (§7.6)
9. **Completeness Gate** (per `skills/company-enrichment/SKILL.md` Mandatory Fields table):
   - Gate passes → full batch write including `last_enriched_date = today (ET)`
   - Gate fails → partial write only, NO date bump. Record will re-appear in next batch's pool.
10. Segment Change Cascade if `customer_segment` changed: sync to associated contacts (Tier 1 cascade)
11. Add HubSpot company note (§7.7)

#### HOLD
1. No HubSpot writes for this record (no tier, no segment, no fields, no date)
2. Append to canvas `F0B0AFSB9LN` under "Tier 3 Holds — Mass Re-Enrichment Sweep `<SWEEP_NAME>`":
   ```
   - [YYYY-MM-DD] <company_id> <name> — <reason>
   ```
3. Surface in batch DM under "Manual review escalations"
4. D7 Edge Case Resolution picks up the record on its next weekly fire

### 7.6 Tier recompute (always runs, all paths except HOLD)

Apply `compute_tier()` per `context/account-tiering/tier-compute-spec.md`:

1. **Step A0:** If `customer_segment` not in the 6 ICPs (post-classification), skip tier
2. **Step A:** If `hs_is_target_account = true`, return current `account_tier` unchanged (do NOT overwrite). Mark `tier_skipped_target_account = true`
3. **Step B:** Look up `(customer_segment, company_sub_segment)` in the 30-row defaults table. Get `starting_tier`, `ceiling`, `floor`
4. **Step C:** Null + unknown-pair fallback per spec (segment null fallback for unrecognized pairs; log a warning)
5. **Step D:** Apply signal modifiers in order:
   - Hot signal (score 27-44 in last 60d): **-1**
   - White-hot signal (score ≥45 in last 60d): **-2** (caps at ceiling)
   - Stacked signals (signal_count_last_30d ≥ 2): **-1 additional**
   - Open deal past `appointmentscheduled` not closed-lost: **-1**
   - Stale signal (>90d AND no engagement ≤30d): **+1**
   - Sustained quiet (>180d AND no engagement ≤180d): **+1 additional**
6. **Step E:** Clamp to `[ceiling, floor]`
7. **Step F:** Build reason string citing defaults-table row + modifiers applied

Write `account_tier` if `computed_tier != current_tier` AND `hs_is_target_account != true`. Values write as `tier_1` / `tier_2` / `tier_3` / `tier_4` / `tier_5` (internal, lowercase).

### 7.6b Signal heat recompute (always runs, all paths except HOLD)

Apply `compute_signal_heat()` per `context/account-tiering/tier-compute-spec.md` §11.5 alongside the tier recompute. **Freshness anchor (post-2026-05-28):** `last_signal_date` stores the EVENT DATE (when the news/funding/hire actually happened), not detection date. **HubSpot enum is Title Case:** `Hot` / `Warm` / `Cool` / `Cold`. Inlined:

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

Write `signal_heat` if `computed_heat != current_heat`. Heat writes proceed REGARDLESS of `hs_is_target_account` (heat is not frozen by the target-account flag). **Values write Title Case:** `Hot` / `Warm` / `Cool` / `Cold` (lowercase rejected by HubSpot enum validator). Idempotent: no write if equal. On change, include the heat delta in the HubSpot company note (see 7.7 below) and in the batch DM.

### 7.7 HubSpot company note format

Add one note per record (Tier 1 / 2 / 3 / FULL / LIGHT / MEDIUM / HOLD all log; tag SWEEP_NAME):

```
[Mass Re-Enrichment Sweep <SWEEP_NAME>] [YYYY-MM-DD]
Path: <LIGHT|MEDIUM|FULL|HOLD>
Segment: <old> -> <new> (or unchanged)
Sub-segment: <old> -> <new> (legacy auto-migration: yes/no)
Confidence: <old> -> <new>
Tier: <old> -> <new> (skipped target_account: yes/no)
Heat: <old> -> <new> (or unchanged)
Apollo: <yes|no>
Reason: <one-line summary>
```

### 7.8 Write format notes

| Field | Format |
|---|---|
| `account_tier` | Lowercase internal: `tier_1`, `tier_2`, `tier_3`, `tier_4`, `tier_5` |
| `signal_heat` | **Title Case** internal: `Hot`, `Warm`, `Cool`, `Cold` (verified via HubSpot MCP 2026-05-28) |
| `customer_segment` | Case-sensitive internal label per `context/hubspot/hubspot-values.md` |
| `flagged_for_deletion_reason` | Multi-line text. Mandatory companion whenever `customer_segment = "Flagged for deletion"` is written. Leads with one of the 7 canonical codes (`Dead domain` / `Hard junk / non-business` / `D1 disqualified (no reference value)` / `No ICP fit` / `Duplicate (merged)` / `Defunct / out of business` / `Stalled greenfield`) + colon + one evidence sentence. No em dashes. Clear to empty on any re-upgrade off "Flagged for deletion". Spec: `context/hubspot/property-schema.md` §2.1 |
| `company_sub_segment` | Case-sensitive internal label; must be one of the 30 active values |
| `segmentation_confidence` | Lowercase: `high_90`, `medium_7089`, `low_5069`, `manual_review_required` |
| `infrastructure_profile` | Multi-select enum; semicolon-separated values per HubSpot convention (e.g. `"Band 1 (1-2 facilities);Band 2 (3-5 facilities)"`) |
| `last_enriched_date` | YYYY-MM-DD string (date field, not timestamp) |
| `last_signal_date` | YYYY-MM-DD string |
| `recent_news_or_trigger_event` | Free text, 2-4 sentence cap, `[YYYY-MM-DD]` date prefix on each entry |
| `account_brief` | Free text, 2-4 sentence cap |
| All other narrative enriched fields | Free text, 2-4 sentence cap, no em dashes |

All writes use `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"` on every `manage_crm_objects` call.

### 7.9 Audit log entry

For each record processed, append to `weekly-reports/mass-reenrichment/<SWEEP_NAME>/batch-<N>.md`:

```markdown
### <Company name> (<company_id>)
- Path: LIGHT / MEDIUM / FULL / HOLD
- Domain: <domain> (corrected from <old>? yes/no)
- Segment: <old> -> <new>
- Sub-segment: <old> -> <new> (legacy auto-migration: yes/no)
- Confidence: <old> -> <new>
- Tier: <old> -> <new> (skipped hs_is_target_account: yes/no)
- Customer protection invoked: yes/no
- Apollo used: yes/no
- web_searches: <count>
- Completeness Gate: pass/fail
- Reason: <one-line summary>
```

The audit log path uses `<SWEEP_NAME>` as a subfolder so each sweep is organized separately. Cooper or future analysts can audit specific sweeps by name.

---

## 8. Caps + safety

- **Batch cap:** BATCH_SIZE (50 default; 100 ceiling for context budget; do not exceed)
- **HubSpot write batching:** 10 `objects` per `manage_crm_objects` call, ≥250ms between batches. Exponential backoff on 429 (1s → 2s → 4s); halve to 5/batch after 3 consecutive 429s
- **Apollo:** Per `APOLLO_ENFORCEMENT` sweep parameter
  - `"disabled"` (default for sweeps): track per-batch + cumulative in DM. Hard stop only on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded`. Do NOT update `weekly-reports/apollo-budget.json` (sweep is outside the cap)
  - `"enabled"`: read `weekly-reports/apollo-budget.json` at batch start, respect remaining budget, update post-batch per `Apollo_Weekly_Budget_Spec.md`
- **web_search:** ≥1s between calls. LIGHT: 1/record. MEDIUM: 2-3/record. FULL: 3-5/record
- **web_fetch:** opportunistic only; skip on failure with no penalty
- **HubSpot reads:** 100/page, ≥1s between pages
- **Safety tiers:**

| Scenario | Tier | Action |
|---|---|---|
| HIGH-confidence refresh, no segment change | T1 | Write |
| HIGH-confidence segment change, no open deals | T1 | Write + cascade |
| MEDIUM-confidence refresh | T2 | Write |
| Segment change on deal-protected account (open deal past `appointmentscheduled`) | T3 | HOLD path |
| Downgrade ICP → non-ICP on customer (closed-won) | T3 | HOLD path (customer protection) |
| LOW / `manual_review_required` after edge-case-researcher | T3 | HOLD path |

- **Hard stops:**
  - MaiaEdge own record (`company_id = 124293230301`) — excluded by trigger query
  - Open deals at `contractsent` or later — block any write that would change segment or sub-segment
  - `hs_is_target_account = true` — block `account_tier` write only; other writes proceed

---

## 9. Pre-batch sanity checks

Run at batch start, after reading the trigger query result but before per-record processing:

1. **Concurrency check:** If any record in the pool has `last_enriched_date = today (ET)` and was written by this sweep (i.e., note prefix matches `[Mass Re-Enrichment Sweep <SWEEP_NAME>]`), another batch is running concurrently. STOP, DM Cooper, wait
2. **Steady-state R2 pause check:** If `APOLLO_ENFORCEMENT = "disabled"` AND `weekly-reports/apollo-budget.json` shows `by_routine.stale-reenrichment` incremented today, R2 ran today — likely not paused. DM Cooper a warning but continue
3. **Framework reference freshness check:** Verify `context/account-tiering/tier-compute-spec.md` last-modified date hasn't changed since SWEEP_KICKOFF_DATE. If it has, framework moved mid-sweep — DM Cooper to decide whether to abort and re-kickoff
4. **Expected pool size sanity:** First batch only — record total pool size from trigger query (without LIMIT) so we can track drain progress. Subsequent batches compare actual drain to projection

---

## 10. End-of-batch Slack DM to Cooper (`U0A24D9RJLS`)

**Subject line:**
```
:arrows_counterclockwise: *Mass Re-Enrichment* — <SWEEP_NAME> — Batch <N> — YYYY-MM-DD
```

**Body (target under 2,000 chars):**
```
*Sweep:* <SWEEP_NAME>
*Batch:* <N>  ·  *Processed:* <X>/<BATCH_SIZE>
*Path mix:* LIGHT <L> · MEDIUM <M> · FULL <F> · HOLD <H>
*Apollo this batch:* <C> credits  ·  *Sweep cumulative:* <T>

*Tier writes:*
  Promotions (toward T1): <P>
  Demotions (toward T5): <D>
  Skipped (hs_is_target_account=true): <K>

*Sub-segment auto-migrations:* <A>
*Greenfield migrations:* <G> (operational <a>, abandoned <b>, stall <c>)
*Segment changes (cascade fired):* <S>
*Customer-protection HOLDs:* <CP>
*Completeness Gate fails (held for next batch):* <GF>
*Manual-review HOLDs (true 2+ ambiguity):* <U>

*Top 5 notable changes:*
1. <Company> — <change summary>
2. ...

*Drain status:*
  Done in this sweep: <X_total>/<expected_pool>  (<P>%)
  Remaining: <R>  ·  ETA: ~<E> more batches at BATCH_SIZE=<BATCH_SIZE>

*Run health:* GREEN / YELLOW / RED
*Errors:* <None | one-line description>

*Audit log:* weekly-reports/mass-reenrichment/<SWEEP_NAME>/batch-<N>.md
```

### Continuation token (append at end of EVERY batch DM and chat output)

```
─────────────────────────────────────────────────────────
TO CONTINUE THIS SWEEP IN A NEW COWORK CHAT:

1. Open a new chat in the CRM Guardian Cowork project
2. Paste the block below verbatim:

   Run Mass Re-Enrichment Sweep with:
     SWEEP_NAME="<SWEEP_NAME>"
     SWEEP_KICKOFF_DATE="<SWEEP_KICKOFF_DATE>"
     BATCH_SIZE=<BATCH_SIZE>
     VERIFY_DEPTH="<VERIFY_DEPTH>"
     APOLLO_ENFORCEMENT="<APOLLO_ENFORCEMENT>"
     SEGMENT_SCOPE="<SEGMENT_SCOPE>"

   Read `routines/cowork/mass-reenrichment/prompt.md` and process the next batch.

3. Fire. The new chat will pick up from where this one left off.
─────────────────────────────────────────────────────────
```

### Pool-exhausted DM (replaces the continuation block when query returns 0)

```
:white_check_mark: *SWEEP COMPLETE* — <SWEEP_NAME>

Active ICP pool fully re-enriched under current framework.
Total batches: <N>
Total records processed: <total>
Total records held for D7: <held_total>
Total Apollo credits consumed: <T>
Total runtime span: <SWEEP_KICKOFF_DATE> to <today>

NEXT STEPS:
1. Run the final verification pass — see §11 of `Mass_Reenrichment_Prompt.md`
2. Re-enable steady-state `Stale_Re_Enrichment_Prompt.md` cron (if paused)
3. Restore `APOLLO_ENFORCEMENT = "enabled"` on the Apollo weekly cap (if disabled)
4. Forward summary to Tim Z for sign-off
5. Append any new data-quality patterns to CLAUDE.md "Known Data Quality Follow-ups"

Final audit logs: weekly-reports/mass-reenrichment/<SWEEP_NAME>/
```

### Fatal-error DM

```
:rotating_light: *Mass Re-Enrichment — <SWEEP_NAME> — Batch <N> ABORTED*

Failure at Step <X>: <error description>
Records processed this batch before abort: <P>
Records held for retry: <BATCH_SIZE - P>
Run health: RED

Recovery:
- Records written so far have last_enriched_date = today; they will be excluded from next batch's trigger query
- Records not yet written keep their prior date; they will re-appear in next batch's pool
- Investigate the error before firing the continuation token
```

---

## 11. End-of-sweep verification pass

After the pool-exhausted DM fires, Cooper runs ONE additional batch to catch tier drift between the first and last record processed (signal field updates that may have shifted modifiers during the sweep window).

```
Trigger query for verification pass:
  Same filters as §6, but with ONE change:
  Replace the last_enriched_date filter with:
    last_enriched_date >= <SWEEP_KICKOFF_DATE>
  Cap: no limit (read all)
```

For each record in the verification pool:
1. Read current state
2. Run tier recompute (§7.6) ONLY — do not re-classify, do not re-research
3. If `computed_tier != current_tier`: write the corrected tier + HubSpot note `"[Mass Re-Enrichment Sweep <SWEEP_NAME> Verification Pass] [YYYY-MM-DD]: Tier <X> -> <Y> drift correction. Reason: <signal modifier change since first pass>."`
4. Bump `last_enriched_date = today (ET)` only on records that needed correction
5. DM Cooper with:
   ```
   :mag: Verification pass complete — <SWEEP_NAME>
   Records reviewed: <total>
   Tier corrections written: <M>
   Top 10 corrections: <list>
   Sweep is fully closed.
   ```

If verification pass corrects >5% of records, that's signal of high mid-sweep drift — flag for investigation but don't block sweep closure.

---

## 12. Coordination with steady-state routines (Cooper's pre-sweep checklist)

Before firing the kickoff batch, Cooper should:

| Routine | Action |
|---|---|
| `Stale_Re_Enrichment_Prompt.md` (R2 steady-state) | **PAUSE** — disable the cron. Mass sweep replaces R2's coverage. Re-enable after sweep complete + verification pass. |
| Apollo weekly cap (`Apollo_Weekly_Budget_Spec.md`) | If sweep param `APOLLO_ENFORCEMENT = "disabled"`: cap not enforced during sweep. Restore after. |
| R0 Import Validator | Leave running — handles records outside sweep pool (blank segment) |
| R1 Fresh Enrichment | Leave running — handles brand-new records that arrive during the sweep |
| R4 Flagged Consolidation | Leave running |
| Weekly Signal Scan | Leave running (Mon 1pm CT). Sweep respects Signal Scan freshness per Step 14 of `Stale_Re_Enrichment_Prompt.md` (7-day grace window) |
| Weekly Market News | Leave running (Fri 1pm CT) |
| Daily Sales Activity Brief | Leave running (4pm M-F) |
| R-Tier-Audit (weekly) | Leave running. Idempotent against sweep writes (if sweep wrote tier_2 and R-Tier-Audit computes tier_2, no double-write). |
| D7 Edge Case Resolution (weekly) | Leave running. Catches sweep's HOLD escalations. |

---

## 13. Failure handling

| Symptom | Action |
|---|---|
| HubSpot 429 / 5xx storms | Exponential backoff per §8. After 3 retries per record, log to `weekly-reports/mass-reenrichment/<SWEEP_NAME>/failed-writes-YYYY-MM-DD.md` and continue with remaining records |
| Apollo `quota_exceeded` mid-batch | If `APOLLO_ENFORCEMENT = "disabled"`: stop using Apollo for the rest of this batch only. Continue tomorrow. If enforcement was enabled: per `Apollo_Weekly_Budget_Spec.md` |
| Slack DM send fails | Retry 3× exponential backoff. If all fail, log locally to audit folder. Continue. |
| Mid-batch crash | Writes up to crash are persisted (records have `last_enriched_date = today`). Re-fire continuation — trigger query auto-skips processed records |
| Concurrent batch detection (§9.1) | STOP. DM Cooper. Wait for the other batch to complete |
| Framework reference file changed since SWEEP_KICKOFF_DATE (§9.3) | DM Cooper warning; let Cooper decide abort vs continue |
| Manual review queue ballooning (>10% per batch over 3+ batches) | Framework calibration likely off. DM Cooper. Cooper may pause the sweep, review D5 v2 protocols for the affected sub-segment, then resume |
| "Held for next batch" (Completeness Gate fails) count growing batch-over-batch | Thin web research data. After sweep complete, fire `edge-case-researcher` skill on the held set |
| MISDOMAIN correction proposes a domain Cooper hasn't approved at LOW confidence | Skip the correction, continue MEDIUM/FULL on the existing domain. Log to audit for Cooper review |
| Customer-protection HOLD fires | Log to canvas `F0B0AFSB9LN`; DM Cooper for human review; do NOT write the downgrade |
| Records keep appearing in pool after multiple batches | Likely Completeness Gate failures repeatedly. Investigate via the audit logs — usually thin research data on small/obscure companies. Hand to `edge-case-researcher` |

---

## 14. Definition of done

The sweep is complete when ALL of these are true:

- [ ] Trigger query returns 0 records (all in-scope records have `last_enriched_date >= SWEEP_KICKOFF_DATE`)
- [ ] DM reads `:white_check_mark: SWEEP COMPLETE`
- [ ] Verification pass (§11) has run and DM'd
- [ ] Audit logs persisted under `weekly-reports/mass-reenrichment/<SWEEP_NAME>/`
- [ ] Cooper has reviewed the HOLD queue in canvas `F0B0AFSB9LN` (or delegated to next D7 run)
- [ ] Steady-state `Stale_Re_Enrichment_Prompt.md` re-enabled
- [ ] Apollo weekly cap enforcement restored if it was disabled
- [ ] CLAUDE.md "Known Data Quality Follow-ups" section appended with any new patterns surfaced
- [ ] Tim Z signed off on the sweep summary

---

**End of Mass Re-Enrichment Sweep prompt.** Self-contained, parameterized, idempotent, self-resuming. Reusable for any future framework migration.
