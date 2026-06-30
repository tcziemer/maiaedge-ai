# CRM Guardian — R10 Field Completeness Sweep (Cowork scheduled task)

**Status: ACTIVE — enabled 2026-06-04 per Cooper.**
**Schedule:** Daily M-F, 1:30 PM CT (`30 13 * * 1-5` local). Slots after R2 (11:03) + R4 (12:06) so their writes settle, before R-Tier-Audit (15:04). Monday overlap with the tail of the signal scans is benign (idempotent writes, different field sets).
**Apollo sub-cap:** 25 credits/run (most fills are web-research; Apollo only for firmographic gaps). Draws on the shared weekly cap.

## Purpose — the catch-all that keeps the CRM full + clean

R10 is the safety net for records that fall *between* the other routines: a record that is **confidently classified and recently enriched, yet missing one or more enriched fields or carrying a blank `account_tier`**. Those records are invisible to R1 (blank/low-confidence segment), R2 (120-day stale rotation), and R-Tier-Audit (tier drift, which skips blank-tier frozen accounts). R10 sweeps them daily, fills only the gaps, and seeds blank tiers — so no classified record ever sits incomplete between its enrichment and its 120-day refresh.

This is an **autonomous filler, not a review queue** — it writes the fills directly so Cooper's only manual job stays the Flagged-for-deletion review.

## What it does NOT touch (no collision with existing routines)

- **Blank `customer_segment`** -> R1 Fresh Enrichment owns these. Excluded.
- **Non-ICP segments (`customer_segment IN ("Other", "Partner Target")`)** -> Excluded (2026-06-08 loop fix). These are competitive/partner reference records, NOT ICP accounts. The 30 `company_sub_segment` values are ICP-only and the narrative/structured enriched fields are ICP-classification inputs, so an `Other`/`Partner Target` record can NEVER satisfy the `company_sub_segment` trigger — leaving it pulled into the pool every run as a permanently-unfillable "incomplete" record (the same non-drainable class as the `hs_is_target_account` frozen-tier loop). R10 chases ICP records that fell between R1/R2/R-Tier-Audit; non-ICP `signal_heat`/`account_tier` upkeep is covered by R0/R1 creation defaults (`Cold`) + R2's 120-day rotation. Excluded at the trigger (Stage 1) so they never enter the pool.
- **`last_enriched_date` ≥ 120 days stale** -> R2 owns full re-enrichment. Excluded (R10 is for the *non-stale but incomplete* gap).
- **`segmentation_confidence = manual_review_required`** -> D7 owns these. Excluded.
- **`last_enriched_date = today`** -> R1/R2 just wrote it; don't re-touch. Excluded.
- **`customer_segment = "Flagged for deletion"`** and **MaiaEdge own (124293230301)**. Excluded.
- Canvas `F0B0AFSB9LN` Tier 3 holds (read at Stage 0; skip those IDs).

---

## Mandatory completeness set (the fields R10 guarantees are present)

**Segment-aware (2026-06-08).** R10 only runs against ICP `customer_segment` values (the 6 ICPs); `Other` / `Partner Target` are excluded at the trigger. The forced set below therefore applies to ICP records. The `Forced?` column is marked **ICP** where the field only makes sense for an ICP record — if a non-ICP record ever reaches Stage 2 by another path, treat the ICP-only fields as N/A (do NOT invent an ICP `company_sub_segment` or fabricate ICP-classification enriched fields on a non-ICP reference; framework wins — the 30 sub-segments are ICP-only).

| Field | Fill source | Forced? |
|---|---|---|
| `company_sub_segment` | classification (D3/D5) | Yes (ICP only — no valid value on non-ICP) |
| `account_tier` | `compute_tier` (tier-compute-spec) | Yes (seed-once on frozen blanks — see below) |
| `signal_heat` | `compute_signal_heat` | Yes (default `Cold` if no signal history) |
| `segmentation_confidence` | classification | Yes |
| `account_brief` | research (account-brief skill, 2-4 sentence cap) | Yes |
| `geographic_focus` | research | Yes (ICP only) |
| `infrastructure_profile` | research (canonical enum bands) | Yes (ICP only — ICP-classification input) |
| `hyperscaler_proximity` | research (enum, `None Known` sentinel) | Yes (ICP only) |
| `fabric_provisioning_approach` | research (enum, snake_case multi-select) | Yes (ICP only) |
| `provisioning_landscape` | research (2-4 sentence cap) | Yes (ICP only) |
| `state` / `country` | Apollo firmographic (if web research can't resolve) | Yes |
| `hubspot_owner_id` | territory model (only if blank AND state/country known; else leave for R6) | Best-effort |
| `recent_news_or_trigger_event` | NOT forced — event-driven, owned by Signal Scan | No |

`maiaedge_value_proposition` is OUT of scope (outreach concern, per the inviolable rules).

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_search/web_fetch. Abort + DM Cooper (`U0A24D9RJLS`) if HubSpot is unavailable.
2. **Read Apollo budget** `weekly-reports/apollo-budget.json`; `effective_apollo = min(25, weekly_remaining)`. If ≤0, run in Apollo-free mode (fill everything resolvable from web research; defer firmographic-only gaps to tomorrow).
3. **Read canvas `F0B0AFSB9LN`** — collect Tier 3 hold IDs to skip.

## Stage 1 — Build candidate pool

HubSpot `search_crm_objects` on COMPANY. Because HubSpot caps filterGroups, query on the **highest-yield missing-field triggers** and then do a full client-side completeness check on each returned record:

Trigger (OR-combined filterGroups, each AND-ing the common exclusions below):
- `account_tier` NOT_HAS_PROPERTY
- `account_brief` NOT_HAS_PROPERTY
- `infrastructure_profile` NOT_HAS_PROPERTY
- `company_sub_segment` NOT_HAS_PROPERTY
- `signal_heat` NOT_HAS_PROPERTY

Common exclusions applied to every group:
- `customer_segment` HAS_PROPERTY AND NEQ `"Flagged for deletion"`
- `customer_segment` NOT_IN (`"Other"`, `"Partner Target"`) — **2026-06-08 loop fix.** Non-ICP references can never satisfy the `company_sub_segment` trigger (ICP-only enum), so without this they re-surface every run as permanently-unfillable "incomplete" records. R10 is an ICP-record completeness sweep; this keeps the pool drainable. (HubSpot caps filterGroups at 18 filters total, so 5 trigger groups x (1 trigger + 1 NEQ-flagged + 2 NEQ-non-ICP) = 20 exceeds the cap — instead keep the server filter to `NEQ "Flagged for deletion"` + the trigger, and apply the `Other`/`Partner Target` drop CLIENT-SIDE on each returned page.)
- `segmentation_confidence` NEQ `manual_review_required`
- `last_enriched_date` NEQ today (ET) AND (`last_enriched_date` ≥ today-120d OR NOT_HAS_PROPERTY) — i.e. not in R2's stale window
- Company ID != `124293230301`

**Sort:** `last_enriched_date ASCENDING` (most-neglected first; nulls first). **Cap: 75 records/run.**

For each returned record, fetch the full mandatory set and compute the exact `missing[]` list client-side (catches gaps in the fields not in the trigger, e.g. `geographic_focus`, `fabric_provisioning_approach`).

### Circuit breaker (connector-dropout guard)
Before writing, check the pool size against the active-population baseline. **If >15% of the active pool suddenly shows the same field blank, STOP and DM Cooper** — a pool-wide gap spike is almost always a HubSpot connector dropping a field, not real gaps (the 2026-05 tier-audit connector-dropout lesson). Do not mass-fill against a dropout. Hold, save a dry-run report, DM Cooper.

## Stage 2 — Fill per record

**Order of operations (INVIOLABLE): enrich first, compute tier LAST.** `compute_tier` reads the enriched fields — `infrastructure_profile` is its PRIMARY input, plus `customer_segment`, `company_sub_segment`, and the signal fields. Never run `compute_tier` (or `compute_signal_heat`) until every tier-input field is populated, or you will compute a tier off missing data and write a wrong tier. This mirrors the research-first workflow: enrichment is Stage 1b, tier compute is Stage 4 (after classification), write is Stage 5. Routing consequence: if `account_tier` is blank AND any tier-input field (`infrastructure_profile` / `company_sub_segment` / `segmentation_confidence`) is ALSO missing, the record is an **enriched-field gap (Path B)**, not a tier-only gap (Path A) — enrich it first, then compute tier.

For each candidate, fill ONLY the missing fields:

**A. Tier/heat-only gap** (missing `account_tier` and/or `signal_heat`, AND every tier-input enriched field — `infrastructure_profile`, `customer_segment`, `company_sub_segment` — is already present and current):
- Compute tier per `tier-compute-spec.md`; compute heat per §11.5.
- **Frozen-tier seed-once rule (fixes the ResetData loop):** if `hs_is_target_account = true` AND `account_tier` is blank, WRITE the computed tier this once. The freeze is meant to prevent *algorithmic overwrite* of a rep-set tier, NOT to block *initial population* of an empty tier. After the seed, future drift writes stay frozen as normal.
- Write tier + heat. **Do NOT bump `last_enriched_date`** (tier/heat-only write, per Unified Stamping Policy).

**B. Enriched-field gap** (any of the 6 narrative/structured enriched fields, or `company_sub_segment` / `segmentation_confidence` / `state` / `country` missing):
- **Step 1 — enrich first.** Run the research-first targeted fill per `skills/company-enrichment/SKILL.md` — populate ONLY the missing fields (do not rewrite fields already present unless they're clearly wrong). Honor the 2-4 sentence cap, "carrier infrastructure" descriptor, no em dashes, canonical enum values. `infrastructure_profile` MUST be resolved here before any tier compute, since it is the primary tier input.
- **Step 2 — Apollo** ONLY for firmographic gaps (state/country/employees/revenue) within the 25-credit sub-cap.
- **Step 3 — compute tier LAST, off the now-complete fields.** Only after the enriched + tier-input fields are populated, run `compute_tier` (+ seed-once rule) and `compute_signal_heat`. If `infrastructure_profile` could not be resolved this run, do NOT compute a tier off the gap — leave `account_tier` as-is, write the fields you did resolve, and surface the record under "Partial — held for next run" so tomorrow's sweep completes it. Never tier a record whose primary input is still missing.
- **Completeness Gate:** if, after the fill, ALL mandatory fields are present, bump `last_enriched_date = today (ET)` (full enrichment pass). If the gate still fails (couldn't resolve a field), write what you have, leave `last_enriched_date` unbumped, and surface under "Partial — held for next run."

**C. Owner gap:** if `hubspot_owner_id` blank AND state/country resolved, derive per `context/hubspot/territory-model.md`. If state/country unknown, leave for R6.

### Hard stops
- **MaiaEdge own (124293230301):** never write.
- **`hs_is_target_account = true`:** freezes `account_tier` *overwrite* only (seed-once on a blank tier is allowed); `signal_heat` + all enriched-field + `company_sub_segment` fills proceed.
- **Open deals are NOT a stop for R10 (Cooper 2026-06-04).** R10 writes enrichment fields on the COMPANY record only and never touches deal records, so company enriched-field / `company_sub_segment` / `account_tier` / `signal_heat` fills proceed normally regardless of any associated deal stage (including `contractsent`+). R10 is a gap-filler, not a reclassifier or a downgrader — it fills blanks and does not move a populated `customer_segment` to non-ICP, so the closed-won downgrade-protection path does not apply here.

## Stage 3 — Write
`manage_crm_objects`, batches of 10, 250ms between batches, exponential backoff on 429, `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`. `flagged_for_deletion_reason` companion rule applies if any record is routed to Flagged (rare here).

## Stage 4 — Audit (NO standalone DM — folds into the one Ops Digest)
- On-disk audit: `weekly-reports/[today CT]/r10-completeness-sweep/run-report.md` — pool size, per-field gap counts before/after, records filled, tiers seeded (incl. frozen-blank seeds resolved), Apollo used, partials held, circuit-breaker status.
- Append one row to the canvas `F0B0AFSB9LN` "Run log" (status emoji: ✅ success / ⚠️ partial / ❌ failed), same as the other ops routines, so the digest + dashboard pick it up.
- **Do NOT send a per-run summary Slack DM (Cooper 2026-06-04).** R10 is quiet-on-success and rolls into the single **CRM Ops Daily Digest** DM (4:45 PM CT), which reads this run report + the ledger row. The digest is the one notification.
- **DM Cooper (`U0A24D9RJLS`) directly ONLY on hard failure / escalation:** fatal abort (`:rotating_light: R10 ABORTED at Step X`) or circuit-breaker trip (`:warning:` connector-dropout hold). Success and zero-candidate runs are silent (captured in the digest + dashboard).

## Caps & budget
- Record cap: 75/run. Apollo sub-cap: 25/run (~125/wk). Draws on the shared weekly cap (recommend the 850 -> ~1,100 raise lands before this goes daily).
- `last_enriched_date` stamping: full gate-passing fill = bump; tier/heat-only or single-field structured fill = no bump.

## Failure handling
Mirror the other routines: HubSpot 429/5xx -> backoff x3 then log + continue; 400 invalid enum -> STOP + DM Cooper the exact value; 404 -> skip + log; Apollo quota -> stop Apollo for the run, continue web-only; Slack fail -> retry x3 then log to canvas `F0B0AFSB9LN`; circuit breaker -> STOP + dry-run report + DM Cooper.

---

## Decisions (confirmed 2026-06-04, Cooper)
1. **Mandatory set** as above; `recent_news_or_trigger_event` stays best-effort (owned by Signal Scan).
2. **Cadence:** daily M-F, 1:30 PM CT. Enabled.
3. **Open deals are not a stop** — enriched-field / sub_segment / tier / heat fills write on the company record regardless of deal stage; deal records are never touched.
4. **No standalone DM** — quiet-on-success; rolls into the one CRM Ops Daily Digest (4:45 PM). Direct DM only on fatal abort or circuit-breaker trip.
5. **Apollo:** 25/run sub-cap. Current weekly utilization is near zero, so this fits inside the 850 cap today; revisit toward the recommended ~1,100 raise as overall volume grows.

## Decisions (added 2026-06-08, Cooper — non-drainable-pool loop fix)
6. **R10 is ICP-only.** `customer_segment IN ("Other", "Partner Target")` is excluded at the Stage 1 trigger (server `NEQ "Flagged for deletion"` + client-side `Other`/`Partner Target` drop, because the 18-filter cap blocks doing all of it server-side). Root cause: the `company_sub_segment NOT_HAS_PROPERTY` trigger group re-surfaced the entire `Other`/`Partner Target` population every run (2026-06-08: 75/75 of the capped pool, dominating the ~553 raw union) and could never be satisfied, because the 30 `company_sub_segment` values are ICP-only and a non-ICP reference has no valid value — the same non-drainable class as the `hs_is_target_account` frozen-tier ResetData loop. Fix carries through three places: the "What it does NOT touch" list, the Stage 1 common exclusions, and the now segment-aware mandatory completeness set. Non-ICP `signal_heat`/`account_tier` upkeep remains covered by R0/R1 creation defaults + R2's 120-day rotation. The one-time backlog of pre-default `Other` records missing `signal_heat` was cleared in the 2026-06-08 R10 run (22 set to `Cold`).
