# D7 - Edge Case Resolution (Weekly Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget, stateless across runs (the manual_review queue lives in HubSpot, not in any task-local state). Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Weekly (Cooper-chosen day). Suggested cron: `0 9 * * 3` (Wed 9am CT, local time - Cowork interprets cron in the user's local timezone, not UTC) - sits between Mon Signal Scan and Fri R8 Persona Fill so it has fresh classifications to work with and ample time before the next signal cascade. Cooper can pick any day.
**Owner:** Cooper Kennedy (Slack DM: U0A24D9RJLS)
**Platform:** Cowork-only
**Apollo budget:** 0 (deep web research only - web_fetch + web_search; no Apollo enrichment)
**Per-run cap:** 30 records (manageable for human-in-the-loop review via the digest)
**Created:** 2026-05-14 (Phase 3 of Account Tiering & Segmentation Overhaul). Reframed as scheduled task (not routine) 2026-05-14 per Cooper.

## What this scheduled task does

Resolves the manual_review_required queue + stale low_5069 records + Unknown/Other escalations with deep web research. Each record either:
- **PASSES** - resolved classification with upgraded confidence (high_90 or medium_7089)
- **EVICTS** - `Flagged for deletion` (no ICP fit / defunct / D1 disqualifier / acquired-absorbed / sub-scale no growth / stalled greenfield / unresolvable contradiction)
- **ESCALATES** - surfaced on the working-ledger canvas `F0B0AFSB9LN` (Tier 3 / "Cooper decision needed") + the on-disk run report; the CRM Ops Daily Digest renders it for Cooper. NOT a DM. (rare; target <=3 per run)

**Hard rule:** Nothing in `segmentation_confidence = manual_review_required` survives more than 14 days. Records that fail D7 resolution get evicted to `Flagged for deletion`.

D5 v2 protocols minimize the manual_review_required queue at write time (Cooper 2026-05-14: target <5% of records). D7 catches the long-tail that genuinely needs deep research.

**Why a scheduled task, not a routine:** D7 reads the manual_review queue from HubSpot, runs web research on at most 30 records, writes resolutions back to HubSpot, writes an on-disk run report + a ledger Run-log row (and pings Cooper ONLY on a hard failure), and exits. No persistent state across runs (HubSpot is the source of truth for what's in the queue), no cross-run agentic behavior. The Cowork scheduled-task primitive matches the design exactly; the "routine" abstraction would add machinery this task doesn't need.

## Required reading at run start

Read these files in order BEFORE any HubSpot calls.

1. **`CLAUDE.md`** - repo conventions, operating principles, last_enriched_date stamping policy
2. **`context/account-tiering/sub-segment-qualification.md`** - 30 active sub-segment values (verified 2026-05-14), retired-value list, pointer to file 06 for full deep-dives
3. **`context/account-tiering/enrichment-protocols.md`** - **canonical, self-contained as of 2026-05-14.** §6 inlines all 30 D5 v2 protocols (one per sub-segment, with 5-question evidence tables + anchors + tiebreakers); **§6a is the deterministic NC1 vs NC3 vs NC2 threshold matrix (disclosed GPU MW + facility count + pricing model + customer profile) - REQUIRED reading when resolving a NeoCloud manual_review_required record**; **§7 is the Greenfield 4-tier migration pattern catalog (operational milestone / abandonment / construction-progress / stalled) + D7 fallback - REQUIRED reading when resolving a stalled-Greenfield record**.
4. **`context/account-tiering/tier-compute-spec.md`** - for tier recompute after PASS resolution
5. **File 06:** `context/account-tiering/sub-segment-qualification-full.md` - **canonical source for D1 global disqualifiers (§3), D2 wholesale-arm policy (§4), and D3 disambiguation flowcharts (§5)**. Also holds the full sub-segment research deep-dives that back the 30 protocols inlined in §6 above.
6. **`context/hubspot/property-schema.md`** + **`context/hubspot/hubspot-values.md`** - case-sensitive enums

The canonical knowledge lives in `context/account-tiering/`: `sub-segment-qualification-full.md` (D1/D2/D3 §3-§5), companion docs `d1-global-disqualifiers.md` / `d2-wholesale-arm-policy.md` / `d3-disambiguation-flowcharts.md`, and `enrichment-protocols.md` (D5 inlined §6 protocols + §6a NC matrix + §7 Greenfield). D7 itself is this routine. No external working files.

## Entry criteria (which records flow into D7)

D7 reads records matching ANY of these criteria:

| Source | Filter | Priority |
|---|---|---|
| Manual review queue | `segmentation_confidence = manual_review_required` AND age (last_enriched_date) > 7 days | P1 (highest) |
| Stale low confidence | `segmentation_confidence = low_5069` AND last_enriched_date > 60 days | P2 |
| Unknown / Other escalation | `customer_segment IN ("Unknown", "Other")` AND has any associated deal OR >=1 engagement in last 30 days | P3 |
| crm-hygiene flags | Records flagged by weekly crm-hygiene audit (framework default without positive evidence) | P3 |

**Per-run cap:** 30 records. If queue exceeds 30, prioritize P1 first, then P2, then P3. Overflow records carry to next weekly run.

## Resolution criteria

For each record, run deep research (5-10 `web_fetch` calls per record, deeper than R1/R2). Then apply:

### PASS criteria (record resolves with upgraded classification)

ANY of:
1. **Anchor company match.** Matches a named anchor in file 06 §6 OR matches the archetype within 1 SD of the anchor's quantitative markers -> upgrade to `high_90`.
2. **Three or more D5 protocol questions confirmed with verifiable evidence.** Web research found sufficient evidence for best-fit at `medium_7089`.
3. **Tiebreaker rule applies cleanly.** Multi-classification was the issue; D7 research clarifies which sub-segment dominates via revenue line / infrastructure focus / parent identity -> resolve to dominant sub-segment + `medium_7089`.
4. **Operational status change for Greenfield records.** Greenfield with stale construction data; D7 verifies current operational state -> migrate to operational sub-segment (AI Signals colo / Modular colo / Hyperscale Wholesale / Large Scale GPU / etc.).
5. **Wholesale-arm policy applies.** Record is a wholesale arm of a parent that has its own record (per D2) -> classify per D2 + `medium_7089` or `high_90`.

### EVICT criteria (record gets `Flagged for deletion`)

ANY of:
1. **No verifiable positive evidence for ANY of the 30 ICP sub-segments.** Doesn't match any archetype even with deep research -> reasoning "No ICP fit after D7 deep research."
2. **Domain dead / website non-resolving / company effectively defunct.** Verified via WebFetch failures or company-status searches -> reasoning "Defunct entity."
3. **Match to D1 disqualifier that initial R1/R2 missed.** Deep research surfaces hyperscaler/equipment-vendor/OTT/government identity -> `Flagged for deletion` (or `customer_segment = "Other"` if useful as competitive/partner reference).
4. **Acquired and absorbed into parent.** Record is post-acquisition with no separate operational entity -> reassociate contacts to parent record per R4 logic, then `Flagged for deletion`.
5. **Below ICP scale threshold AND no growth signals.** Mid-market <$50M revenue with no infrastructure footprint AND no funding signals AND no LinkedIn growth -> reasoning "Sub-scale; no growth signals."
6. **Greenfield with stalled construction or pulled funding.** Greenfield record where recent_news shows abandoned project, bankruptcy, or 18+ months without construction progress -> reasoning "Stalled greenfield."
7. **Contradictory evidence that cannot be resolved.** Genuinely conflicting signals (e.g., website says network operator but financial filings say SaaS only) where deep research can't determine truth -> reasoning "Unresolvable contradiction after D7 deep research; record likely has data quality issues that exceed enrichment scope."

### ESCALATE criteria (rare - Cooper makes final call)

ANY of:
1. **Anchor refresh signal.** D7 finds 5+ records in the same sub-segment drifting in a similar way -> potential anchor list / protocol staleness. Cooper decides whether to update file 06 anchor list.
2. **New sub-segment candidate.** D7 finds 3+ records that don't fit any of the 30 sub-segments but share a coherent archetype -> potential new sub-segment. Cooper decides.
3. **Customer relationship preservation.** Record has `type = "Customer"` OR active open deal AND would be Flagged for deletion -> halt; ask Cooper.

Target escalations: <=3 per weekly run. More than 3 -> D7 criteria need refinement.

## Per-record D7 research process

### Step 1 - Pull current record state

- `customer_segment`, `company_sub_segment`, `segmentation_confidence`
- `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`
- `account_tier`, `hs_is_target_account`
- Reasoning string from last R1/R2 audit (HubSpot company notes)
- Associated deals, engagements (last 90 days)

### Step 2 - Read the prior reasoning

- Why was this record manual_review or low_5069?
- Which D5 protocol questions were unanswered?
- What evidence was insufficient?

### Step 3 - Deep web research (5-10 calls)

- `web_fetch` the company website (about, products, customers, news pages)
- `web_search` for `"<company name> revenue"`, `"<company name> customers"`, `"<company name> news 2025-2026"`, `"<company name> acquisition"`, `"<company name> funding"`
- `web_fetch` industry-source URLs from `context/account-tiering/sub-segment-qualification-full.md` §6 + `context/account-tiering/icp-deep-dives/B-and-C-{icp}.md` (TeleGeography for subsea, Omdia for TSDs, FCC BDC for ISPs, etc.)
- If revenue is the gap: `web_fetch` 10-K filings (SEC EDGAR), Companies House (UK), Crunchbase profile
- If infrastructure_profile is the gap: `web_fetch` the company's "Locations" / "Coverage" / "Facilities" pages and infer Facilities / Route Miles / POPs bands

### Step 4 - Apply PASS / EVICT / ESCALATE criteria

Run the criteria above. Determine resolution path.

### Step 5 - Write HubSpot updates

For PASS:
- Update `customer_segment` + `company_sub_segment` + `segmentation_confidence` to upgraded values.
- **Clear-on-exit:** if the record being upgraded was previously `customer_segment = "Flagged for deletion"`, clear `flagged_for_deletion_reason` to empty in the SAME update that writes the new active segment. A record promoted back into an active segment must not retain a stale deletion reason.
- Refresh `account_brief` + `infrastructure_profile` + `recent_news_or_trigger_event` with new evidence (2-4 sentence conciseness cap on narrative fields per CLAUDE.md / enrichment-protocols.md). **`recent_news_or_trigger_event` is pure narrative — no date prefix** (post-2026-05-28).
- **If the D7 web research surfaced a fresh signal-grade event** (funding round, exec hire, M&A, facility launch, etc. — any signal class that would score ≥8 per `context/signals/signal-framework.md`): also write `last_signal_date` to the event date (extract from the source article; use article pub date as a ±few-day approximation if the body doesn't state the event date explicitly). Write `last_signal_score` per the rubric. Do NOT touch `signal_count_last_30d` (D7 is per-record, not a TAM sweep — leave count maintenance to Signal Scan / R-Tier-Audit).
- Recompute tier per `context/account-tiering/tier-compute-spec.md` Step A-G. Honor `hs_is_target_account = true` (skip tier write).
- **Recompute `signal_heat`** per `context/account-tiering/tier-compute-spec.md` §11.5 using the freshly-written signal fields. Title Case values (`Hot` / `Warm` / `Cool` / `Cold`). Idempotent — no write if `computed_heat == current_heat`. Heat writes proceed regardless of `hs_is_target_account` (heat is not frozen by the target-account flag).
- **Bump `last_enriched_date`** per CLAUDE.md Unified Stamping Policy (D7 PASS resolution stamps the date).
- Write HubSpot note: `"D7 PASS YYYY-MM-DD: <prior> -> <new> at <confidence>. Reasoning: <D5 protocol citation + evidence summary>. Tier <X> -> <Y>: <reason>."`

For EVICT:
- Set `customer_segment = "Flagged for deletion"` AND, in the SAME HubSpot update, set `flagged_for_deletion_reason = "<Reason code>: <one concrete sentence of evidence>"`. Lead with the canonical reason code (per property-schema §2.1) that matches the EVICT criterion that fired, then a colon and one concrete evidence sentence. No em dashes in the reason string. Map the 7 EVICT criteria to the 7 codes:
  - Criterion 1 (no verifiable positive evidence for any ICP sub-segment) -> `No ICP fit`
  - Criterion 2 (domain dead / website non-resolving / effectively defunct) -> `Dead domain` if the trigger is a dead/non-resolving domain; `Defunct / out of business` if the company has confirmably ceased operations
  - Criterion 3 (match to D1 disqualifier missed initially) -> `D1 disqualified (no reference value)` (NOTE: if the entity is useful as a competitive/partner reference, write `customer_segment = "Other"` instead of `Flagged for deletion` per the existing carve-out, and do NOT set `flagged_for_deletion_reason`)
  - Criterion 4 (acquired and absorbed into parent) -> `Defunct / out of business` (cite the acquisition and absence of a separate operational entity); if a primary parent record exists and contacts were reassociated, `Duplicate (merged)` is also acceptable when the record is functionally a duplicate of the parent (cite primary name + record ID)
  - Criterion 5 (below ICP scale AND no growth signals) -> `No ICP fit`
  - Criterion 6 (Greenfield with stalled construction or pulled funding) -> `Stalled greenfield` if the trigger is an 18+ month stall with no progress; `Defunct / out of business` if the trigger is confirmed abandonment/bankruptcy
  - Criterion 7 (unresolvable contradiction) -> `No ICP fit` (cite the contradictory signals and that deep research could not establish ICP fit)
- Clear `company_sub_segment`.
- **Bump `last_enriched_date`** per CLAUDE.md Unified Stamping Policy (D7 D1 eviction or definitive non-ICP eviction stamps the date).
- Write HubSpot note: `"D7 EVICT YYYY-MM-DD: <prior> -> Flagged for deletion. Reasoning: <criterion + evidence>."`
- **Hook R4:** D7 EVICT records flow into R4 (Flagged Consolidation) next run for contact reassociation.

For ESCALATE:
- Leave classification UNCHANGED.
- Do NOT bump `last_enriched_date` (no resolution this run).
- Write HubSpot note: `"D7 ESCALATE YYYY-MM-DD to Cooper: <reason>. Awaiting decision."`
- **Surface on the ledger, NOT a DM.** Append the record to the Tier 3 / "Cooper decision needed" section of the working-ledger canvas `F0B0AFSB9LN` (`### D7 Edge Case Resolution YYYY-MM-DD - escalations`) with HubSpot ID + reason, and list it in the on-disk run report's ESCALATED section. The CRM Ops Daily Digest renders escalations for Cooper. D7 does NOT DM escalations.

### Step 6 - Local audit log

Append to `weekly-reports/edge-case-resolution/YYYY-MM-DD-d7-run.md`:

```markdown
### Record N
- HubSpot ID: <id>
- Domain: <domain>
- Prior state: customer_segment=<X>, sub_segment=<Y>, confidence=<Z>
- Priority: P1 / P2 / P3
- Web research: <list of URLs fetched + queries>
- D7 verdict: PASS / EVICT / ESCALATE
- New state (if PASS): customer_segment=<X'>, sub_segment=<Y'>, confidence=<Z'>, tier=<T'>
- Reasoning: <D5 protocol ID + evidence summary>
```

## Run summary + Delivery (on-disk + ledger, NO success DM)

**Delivery - quiet on success, ping only on hard failure.** Do NOT DM Cooper a per-run debrief. On a clean run (including a zero-queue run), the full record is: (1) the on-disk audit log at `weekly-reports/edge-case-resolution/YYYY-MM-DD-d7-run.md` (the per-record entries from Step 6 plus the summary block below), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). ESCALATE items go to the ledger Tier 3 / "Cooper decision needed" section (per Step 5), NOT a DM. The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's resolutions + escalations from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack MCP unreachable, an abort, or zero records processed against a non-empty queue - as ONE line:

`:red_circle: D7 Edge Case Resolution [FAILED/ABORTED] - [one-clause reason].`

Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk audit log + Run-log row are the fallback.

**Ledger Run-log append (every run):** append ONE row to the "Run log" table on canvas `F0B0AFSB9LN` via `slack_update_canvas`:

`| YYYY-MM-DD | D7 Edge Case Resolution | <status emoji> | <one-sentence summary: A resolved, B evicted, C escalated> | weekly-reports/edge-case-resolution/YYYY-MM-DD-d7-run.md |`

Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped.

Write this summary block into the on-disk audit log, appended after the per-record entries:

```
Edge Case Resolution - YYYY-MM-DD (weekly)

Records reviewed: <N> (of which P1: <X>, P2: <Y>, P3: <Z>)
Per-run cap: 30 (overflow carried to next run: <M>)

OUTCOMES:
:white_check_mark: Resolved with upgraded classification: <A>
  - Upgraded to high_90: <A1>
  - Upgraded to medium_7089: <A2>

:wastebasket: Flagged for deletion: <B>
  - No ICP fit: <B1>
  - Defunct: <B2>
  - D1 disqualifier (missed in initial enrichment): <B3>
  - Acquired/absorbed: <B4>
  - Sub-scale no growth: <B5>
  - Stalled Greenfield: <B6>
  - Unresolvable contradiction: <B7>

:warning: ESCALATED for Cooper decision: <C>
  - Anchor refresh signal: <list max 5 records>
  - New sub-segment candidate: <list>
  - Customer/deal conflict: <list>

NOTABLE RESOLUTIONS (top 10, one-line reasoning):
  - <company> [<prior>] -> <new>: <reasoning>
  - ...

PATTERNS DETECTED:
  - <e.g., "5 Modular - colo records drifting toward Hyperscale Wholesale -- investigate anchor list">
  - <e.g., "3 records on Master Agent confirmed independent -- consider anchor list addition">

Next run: YYYY-MM-DD (+7d)
```

## Quality checks at end of run

Before finalizing the on-disk audit log + Run-log row, D7 self-validates:

1. **Resolution coverage:** every queue record has a verdict (PASS / EVICT / ESCALATE). No nulls.
2. **Audit string completeness:** every HubSpot note has D5 protocol citation + web source references.
3. **Manual review queue size:** post-D7, manual_review_required queue size <= 1% of total active ICP records.
4. **Escalation cap:** <=3 escalations per run. More than 3 -> review whether D7 criteria need refinement.
5. **Hard rule enforcement:** no record left in `manual_review_required` with age > 14 days. Either resolved (PASS) or evicted (EVICT) before the 14-day deadline.

If any check fails, write a warning to the audit log (and, if it rises to a hard failure, fire the failure ping per the Delivery rule above) but proceed with the writes that did succeed.

## Cadence interaction with other routines

D7 runs WEEKLY. Other routines run on their own cadence:
- R1 Fresh Enrichment (M-F daily) - produces some `low_5069` and `manual_review_required` records; D7 catches the long-tail
- R2 Stale Re-Enrichment (M-F daily) - re-validates `low_5069` records on 60-day cycle; D7 catches what R2 can't resolve
- R4 Flagged Consolidation (M-F daily) - processes `Flagged for deletion` queue including D7 evictions
- R-Tier-Audit (weekly, every Sunday 11pm CT) - tier drift; not classification-related
- Quarterly anchor refresh - Cooper-driven; D7 surfaces patterns that inform refresh priorities

D7 does NOT replace R2. R2 is broad re-enrichment on a cadence; D7 is targeted deep-research on hard cases.

## Configuration parameters (tunable)

| Parameter | Default | Tunable rationale |
|---|---|---|
| Per-run cap | 30 records | Manageable for digest review; bump to 50 if backlog grows |
| Stale low_5069 threshold | 60 days | After 60 days, R2 has had multiple chances; D7 takes over |
| Manual review max age | 14 days | Hard rule per Cooper feedback - nothing stays in manual review more than 14 days |
| Escalation cap per run | 3 | More than 3 = D7 criteria need refinement |
| Manual review queue % cap | 5% of total ICP records | If exceeded, alert Cooper - protocol bugs likely |
| Deep research call budget per record | 5-10 web_fetch / web_search calls | Balance depth vs cost |

## Post-D7 cleanup

The `Flagged for deletion` records D7 produces flow into Cooper's manual deletion step (per CLAUDE.md "Cooper's only manual step" section): filter HubSpot -> `customer_segment = "Flagged for deletion"` -> bulk-archive.

D7 EVICT writes also automatically flow into R4 (Flagged Consolidation) next run for contact reassociation. Cooper's manual archive step still applies for review.

---

**End of D7 prompt.** Apollo budget 0. Hard 14-day max for manual_review_required. PASS / EVICT / ESCALATE with deep web research per record. Updates HubSpot via MCP; logs audit locally + appends a ledger Run-log row; ESCALATE items go to the ledger/digest, not a DM; pings Cooper ONLY on a hard failure.
