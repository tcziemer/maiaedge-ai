# CRM Guardian - Routine 6: Territory & Hygiene Sweep

Daily, 1:00 AM ET - runs FIRST each day so the other routines operate on clean state. You validate territory ownership, auto-migrate deprecated enum values, fill gap fields, cascade contact owners, and flag clear-cut junk contacts. Apollo is used only for state verification when a company is missing state or the enrichment is 120+ days stale.

**CRM scale (as of 2026-04-24):** 3,489 companies, 13,309 contacts. Cooper-owned placeholder accounts: **0** (already clean). Deprecated `AI - Colocation Operator` enum values: **0** (already migrated). This routine is a safety-net sweep - steady-state output should be mostly "All clean" with minor daily drift.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/crm-hygiene/SKILL.md` (Modes 2-11 - this routine runs the audit-and-fix modes; duplicate merges are deferred to Routines 3+5)
- `skills/territory-manager/SKILL.md` (Mode 1 Full Territory Audit, contact owner cascade, Apollo state verification, strategic exception detection)

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/hubspot/territory-model.md`
- `context/hubspot/contact-schema.md`
- `context/hubspot/deals-schema.md`

**Required reading (Phase 3 Account Tiering & Segmentation Overhaul):**
- **Tier Compute Spec is INLINED below** in the "Inlined Tier Compute Spec" section. Do NOT attempt to read `context/account-tiering/tier-compute-spec.md` from the runtime - the Claude Code env cannot resolve repo paths. The inlined section is canonical and self-contained.
- `context/account-tiering/sub-segment-qualification.md` (file 06) - 30 active sub-segment values + retired-value rejection list. The 30 active values are also enumerated in the inlined defaults table below; if the repo file is unreachable, use the inlined table.
- `context/account-tiering/enrichment-protocols.md` - boundary rules: R6 does targeted/partial writes only, no full re-enrichment, no `last_enriched_date` bump. (Boundary rules are also restated inline under "Run-Time Invariants H. Write Authorization".)

**Connected tools:** HubSpot MCP, Apollo MCP (state verification only), Slack MCP (canvas Run-log append + failure-ping only; no per-run debrief DM - see Delivery).

## Inlined Tier Compute Spec

Inlined from `context/account-tiering/tier-compute-spec.md` 2026-05-20 because the Claude Code runtime env cannot resolve repo paths and the prior R6 runs were deferring Step 5.5 tier recompute with "tier-compute-spec.md absent." This section is canonical and self-contained for R6. If `context/account-tiering/tier-compute-spec.md` changes, this section MUST be re-inlined via `RemoteTrigger.update` on trigger `trig_01BmhnoyxFVrNXuqGcNnW6FV`.

### 1. Inverted tier convention

Tier 1 = HIGHEST priority. Tier 5 = LOWEST. Lower number = more priority. `-1` modifier = tier number decreases (more priority). `+1` modifier = tier number increases (less priority).

### 2. Operating principles (Cooper 2026-05-14)

1. **No-default-manual-review.** Best-fit + tiebreaker; `manual_review_required` is last resort (<5% target).
2. **Multi-marker classification.** `infrastructure_profile` is the PRIMARY structured signal; it wins over `annualrevenue` on conflict.
3. **Read from 8 enriched fields**, not HubSpot defaults: `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`. `description` / `industry` are last-resort only.
4. **Conciseness cap 2-4 sentences** on narrative enriched fields.
5. **`maiaedge_value_proposition` is NOT in enrichment scope.** Outreach skills populate at outreach time.
6. **`hs_is_target_account = true` freezes `account_tier` ONLY.** Segment / sub-segment / signal / enriched field writes proceed.

### 3. Function signature

```
compute_tier(account) -> {new_tier: str, reason: str}
```

**Inputs** (read from HubSpot company + associated objects):
- `customer_segment`, `company_sub_segment`, `segmentation_confidence`
- `last_signal_score`, `last_signal_date`, `signal_count_last_30d`
- `network_op_track` (informational only - does not affect tier)
- `hs_is_target_account`, `account_tier` (current value)
- Associated deals (open_deal_count past `appointmentscheduled`, not closed)
- `notes_last_contacted` or most recent engagement timestamp

**Outputs:** `new_tier` (one of `tier_1`, `tier_2`, `tier_3`, `tier_4`, `tier_5`) and `reason` (one-line audit string).

### 4. Algorithm

**Step A0 - Pre-classification guard.** If `customer_segment` is NOT in the 6 active ICP segments (i.e., is `Other`, `Unknown`, `Flagged for deletion`, `Partner Target`), return without modification. `compute_tier` only applies to active ICP segments.

**Step A - Manual override.** If `hs_is_target_account = true`:
- Return `{new_tier: <current account_tier>, reason: "Manual override locked via hs_is_target_account=true"}`.
- STOP tier compute.
- Calling routine STILL writes segment / sub-segment / signal / enriched fields normally.

**Step B - Defaults lookup.** Look up `(customer_segment, company_sub_segment)` in the defaults table (§5). Get `starting_tier`, `ceiling`, `floor`.

**Step C - Null + unknown-pair fallback.**
- If `company_sub_segment` is null/empty: use segment null fallback (§6).
- If `(customer_segment, company_sub_segment)` is not in the defaults table: use segment null fallback AND log warning `"Unknown (segment, sub-segment) pair: <X>, <Y>. Using null fallback for segment <X>."`. Do NOT throw.

**Step D - Signal modifiers (additive, applied in order).** Apply §7 modifiers in this order: hot -> white-hot (caps at ceiling) -> stacked -> open deal -> stale -> sustained quiet.

**Step E - Clamp.** Clamp running tier to `[ceiling, floor]` inclusive. Ceiling = smallest allowed tier number (highest priority). Floor = largest allowed tier number (lowest priority).

**Step F - Build reason string.**
```
"Default <segment>/<sub-segment> = T<starting>, <modifier list> = T<final>. <file 06 §X.Y / D5 protocol ID>"
```

**Step G - Return.** `{new_tier: "tier_" + clamped_value, reason: reason_string}`

### 5. Canonical defaults table

Internal values are CASE-SENSITIVE. Verified via HubSpot MCP 2026-05-14.

| Segment | Sub-segment (HubSpot internal value) | Default | Ceiling | Floor |
|---|---|---:|---:|---:|
| `Network Operator(Tier 1 / VNO)` | `Tier 1 Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Pure Wholesale Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Cable MSO Enterprise Division - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `International Backbone Specialist - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Subsea cable operator` | 2 | 1 | 3 |
| `Data Center Colo Provider` | `AI Signals - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Standard - colo` | 3 | 1 | 5 |
| `Data Center Colo Provider` | `Modular - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Hyperscale Wholesale - colo` | 1 | 1 | 3 |
| `NeoCloud` | `Large Scale GPU - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Sovereign AI Clouds - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Tier 1 Inference - Neocloud` | 2 | 1 | 2 |
| `NeoCloud` | `AI Infrastructure providers - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Crypto to AI - Neoclouds` | 1 | 1 | 2 |
| `Fiber Operator` | `Tier 2 National Wholesale - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Long Haul / Backbone - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Dark Fiber Specialist - Fiber Operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Regional CLEC - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Regional Cable Operator - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Municipal / Cooperative - Fiber operator` | 4 | 2 | 5 |
| `MSP/Aggregator` | `Telecom Aggregator - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `Managed Network Services - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `TSD Technology Services Distributor - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Master Agent - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Cloud + Telecom Hybrid MSP - MSP` | 2 | 1 | 4 |
| `Enterprise-CustomerSegment` | `Financial Services - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Healthcare Systems - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Retail and Distribution - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Outsourcing Services - Enterprise` | 3 | 2 | 4 |
| `Data Center Colo Provider` OR `NeoCloud` | `Greenfield` | 2 | 1 | 3 |

**Case-sensitivity quirks (do NOT normalize):**
- `Dark Fiber Specialist - Fiber Operator` - capital `O` in `Operator` (every other Fiber sub-segment uses lowercase `o`).
- `AI Infrastructure providers - Neocloud` - lowercase `p` in `providers`.
- `Crypto to AI - Neoclouds` - trailing `s` on `Neoclouds`.
- `Network Operator(Tier 1 / VNO)` - NO space before the open paren.
- `Subsea cable operator` - lowercase `c` and `o`; NO `- Network Op` suffix.
- `Managed Network Services - MSP` - `- MSP` suffix (the `- Network Operator` variant is RETIRED).
- `Greenfield` pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` parent.

**Retired sub-segment values - REJECT on write, log error, surface as Tier 3 hold:**
- `Tier 1 Global Incumbent` (use `Tier 1 Carrier - Network Op`)
- `AI - Colocation Operator` (use `Data Center Colo Provider` + `AI Signals - colo`)
- `Managed Network Services - Network Operator` (use `Managed Network Services - MSP`)
- `Co-op/consortium`
- `External Extension - Network operator`
- `Internal + external unification - Network Operator`

### 6. Null sub-segment fallbacks

When `company_sub_segment` is null OR `(segment, sub-segment)` pair is unknown:

| Segment | Null fallback `(default, ceiling, floor)` |
|---|---|
| `NeoCloud` | (2, 1, 2) |
| `Fiber Operator` | (3, 1, 4) |
| `Data Center Colo Provider` | (3, 1, 5) - Standard fallback |
| `Network Operator(Tier 1 / VNO)` | (1, 1, 2) |
| `MSP/Aggregator` | (2, 1, 4) |
| `Enterprise-CustomerSegment` | (3, 2, 4) |

Known unknown pairs as of Phase 2 audit: Mapletree, Montera, PTS, Lonestar, LS Power (MSP/Aggregator parent with colo sub-segment values). Apply MSP/Aggregator null fallback and log warning.

### 7. Signal modifiers (additive, applied in order)

| Modifier | Delta | Source field(s) | Evaluated by |
|---|---:|---|---|
| Hot signal score 27-44 in last 60d | -1 | `last_signal_score` 27-44 AND `last_signal_date` <= 60d | Weekly Signal Scan |
| White-hot signal score >=45 in last 60d | -2 (capped at ceiling) | `last_signal_score` >= 45 AND `last_signal_date` <= 60d | Weekly Signal Scan |
| Stacked signals (2+ scoring >=8 in same 30d) | -1 additional | `signal_count_last_30d` >= 2 | Weekly Signal Scan |
| Open deal past `appointmentscheduled` | -1 | Association lookup: any deal not in {`closedwon`, `closedlost`} past `appointmentscheduled` | R6 (this routine) |
| Stale signal (>90d) AND no rep activity <=30d | +1 | `last_signal_date` > 90d AND no engagement <=30d | R-Tier-Audit, R6 |
| Sustained quiet (>180d AND no activity <=180d) | +1 additional | `last_signal_date` > 180d AND no engagement <=180d | R-Tier-Audit |

Order: hot -> white-hot -> stacked -> open deal -> stale -> sustained quiet.

### 8. Worked examples (sanity reference)

1. **AT&T (Tier 1 Carrier, no signals):** Default `Network Operator(Tier 1 / VNO)`/`Tier 1 Carrier - Network Op` = T1. No modifiers. Output `tier_1`.
2. **Nscale (Sovereign AI Neocloud, white-hot signal):** Default T1, ceiling 1. White-hot -2 capped at ceiling. Output `tier_1`.
3. **Standard colo with stale + sustained quiet:** Default T3, +1 stale +1 sustained quiet = T5. Output `tier_5`.
4. **Greenfield colo + hot signal:** Default `Greenfield` = T2, hot -1 = T1. Output `tier_1`.
5. **`hs_is_target_account = true`:** Step A returns current tier unchanged with reason "Manual override locked". Other field writes proceed.
6. **JPMorgan Enterprise Financial Services with open deal:** Default T3 (ceiling 2, floor 4), open deal -1 = T2. Output `tier_2`.
7. **IREN Crypto-to-AI Neoclouds + white-hot:** Default T1, white-hot -2 capped at ceiling. Output `tier_1`.
8. **Mapletree unknown pair (MSP/Aggregator + Standard - colo):** Step C MSP/Aggregator null fallback = T2. Output `tier_2`.
9. **Seaborn Subsea cable operator:** Default T2. Output `tier_2`.

### 9. Audit log format

Every tier change produces a HubSpot company timeline note:

```
Tier <old> -> <new> on <ISO date> by R6 Territory & Hygiene: <reason citing modifier list or file 06 / D5 ID>
```

Use a hyphen ("->"), NOT an em dash. If `new_tier == current account_tier`, no HubSpot write happens (idempotent no-op).

### 10. Implementation note for R6

This spec is referenced from:
- **Step 3 Mode 3 missing `account_tier` cascade fill** (drain cap 400/run).
- **Step 5.5 Tier maintenance step** (per-touched-account recompute).

Both references mean: apply Step A0 -> Step A -> Step B -> Step C -> Step D -> Step E -> Step F -> Step G against the company's current state, then write if the result differs from `account_tier` and `hs_is_target_account != true`.

## Run-Time Invariants

### A. Timezone
America/New_York.

### B. Skip Already-Flagged
Exclude `customer_segment = "Flagged for deletion"` companies from territory / hygiene operations (Routine 4 owns them).

### C. Customer Protection
Closed-won companies are protected from segment/tier changes - but territory/owner corrections remain Tier 1 (reps still need correct routing).

### D. Error Containment
Per-record try/except.

**Distinguish web_fetch failure modes when running the Field Resolution Ladder (state/country resolution, ladder step 2 is `web_fetch` on the company website footer):**

- **Proxy block (HTTP 403 with `x-deny-reason: host_not_allowed`)** → infrastructure failure, NOT a domain signal. Skip ladder step 2 (website fetch) and proceed directly to step 3 (LinkedIn About) and step 4 (WHOIS). Do NOT treat this as "state unresolvable" - the ladder still has remaining steps. If steps 3-4 also fail, Tier 3 hold (state genuinely unknown).
- **DNS NXDOMAIN / parked-page / persistent destination 4xx-5xx** → real dead website. Note this in the audit but continue ladder steps 3-4 (LinkedIn / WHOIS may still resolve state).
- **Timeout** → retry once with 5-sec backoff; if still times out → skip step 2, proceed to step 3.
- **Captcha / Cloudflare** → skip step 2, proceed to step 3.

### E. Default to Tier 3 When Uncertain
State still blank after Apollo verification → Tier 3 hold. Strategic / leadership-assigned owner overrides → skip (territory-manager detects these).

### F. Idempotency
All writes idempotent. A second same-day run finds clean state and returns "All clean" (minor).

### G. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest).
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07).
- `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") was promoted to ICP on 2026-05-11. Four sub-segments only: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. R6 must NOT auto-correct `Enterprise-CustomerSegment` to anything else (including `Other` or `Unknown`) - these records belong in R1/R2 for full enrichment, not R6 for hygiene drift fixes. Treat `Enterprise-CustomerSegment` like any other ICP segment in territory + owner cascade + sub_segment fill (Step 3 Mode 3 cascade fills Enterprise sub_segment from segment-classification's Enterprise rules per `context/segments/enterprise.md` vertical signals - but only for HIGH confidence Enterprise records; if confidence is unclear, defer to R1/R2 per the existing Tier 3 hold rule).
- AI Colo: `Data Center Colo Provider` + `AI Signals - colo`. Auto-migrate deprecated `AI - Colocation Operator` (crm-hygiene Mode 7).
- No em dashes in customer-facing field values.

### H. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:**
- Company: `hubspot_owner_id` per territory-model, `state`, `country`, `customer_segment` (deprecated enum migration ONLY - e.g., `AI - Colocation Operator` → `Data Center Colo Provider`), `company_sub_segment` (cascade from segment migration; values constrained to the 30 active values in the Inlined Tier Compute Spec §5 defaults table), `account_tier` (cascade fill in Step 3 AND tier-maintenance recompute in Step 5.5 per the Inlined Tier Compute Spec section above), `signal_heat` (recompute in Step 5.5 alongside tier per the inlined heat compute logic).
- Contact: `hubspot_owner_id` (cascade from corrected company owner), `customer_segment` (sync from company), `flagged_for_deletion = true` on Mode 11 junk.

**`hs_is_target_account` interaction:** When `hs_is_target_account = true` on a company, R6 SKIPS the `account_tier` write only. All other writes (segment correction, sub-segment fill, signal field updates, `signal_heat`, owner cascade, enrichment-adjacent fields) proceed normally. `hs_is_target_account` is an `account_tier` freeze, not a global write freeze. **Heat is NOT frozen** by the target-account flag - tier is rep-locked; heat always reports the truth.

**`last_enriched_date` is NOT in the pre-authorized list (documented 2026-05-03).** R6 makes targeted/partial corrections - territory, state, sub_segment fill, contact owner cascade, junk flagging. None of these are full re-enrichments. R2 owns the 120-day rotation guarantee; bumping the date here would hide the corrected record from R2 for another 120 days and skip its full segment/Apollo refresh. Leave `last_enriched_date` alone.

**Hard stops:** MaiaEdge's own record (ID 124293230301). Never set `customer_segment = "Flagged for deletion"` (Routine 3 owns that specific transition).

## Workflow

Order matters - territory runs first so downstream hygiene operates on correct owners.

### Step 0: Preflight

1. Confirm Apollo MCP is connected. Call `apollo_users_api_profile` once. If `monthly_consumed >= 6000` (or no headroom for at least 5 credits): note `apollo_skip = true` and continue without Apollo state verification (every Step 1 Apollo path falls through to the Field Resolution Ladder). If the call fails: same - `apollo_skip = true`, log the error in the on-disk run report's Errors section, continue.
2. Confirm HubSpot MCP is connected. If not: send the one-line hard-failure ping per Delivery (`:red_circle: CRM Guardian - Territory & Hygiene ABORTED - HubSpot MCP unreachable.`), write the matching ❌ Run-log row, and exit.

No early-checkpoint smoke-signal DM. The fact that R6 fired is recoverable from the on-disk run report + the canvas Run-log row + the CRM Ops Daily Digest. Capture `apollo_skip` + the Apollo monthly counter for the on-disk run report hero.

NO `git pull` / `git fetch` / `git status` at preflight. NO `weekly-reports/apollo-budget.json` read. Cross-run Apollo state lives entirely in the on-disk run reports + Apollo's native `apollo_users_api_profile.monthly_consumed`. The Bash tool is still available for non-git uses (e.g., date math), but git commands MUST NOT be invoked from this routine.

### Step 1: Territory Audit (territory-manager Mode 1)

1. Pull all active companies (`customer_segment != "Flagged for deletion"`).
2. For each company:
   - If `state` is populated and owner mismatches state-to-owner mapping → correct owner (Tier 1). Cascade contact owners.
   - If `state` is blank OR `last_enriched_date` is 120+ days stale: call **Apollo `apollo_organizations_enrich`** for state/country. Apollo is authoritative. Write the refreshed state + country (Tier 1 if write succeeds, Tier 2 if the account has an open deal and the state overwrite shifts territory).
   - **If state is still blank after Apollo → run the Inlined Field Resolution Ladder below (steps 2-4).** Do NOT attempt to read `skills/company-enrichment/SKILL.md` from the runtime - the ladder is inlined here. Write at the confidence level the ladder yields. Only if all four ladder steps return null → Tier 3 hold. The previous "Apollo blank → manual research" pattern lost 100% of the 3 records on 2026-04-24 (Shaun Telecom, Surf USA Mobile, kiocompany.com); the ladder recovers most of them.

     **Inlined Field Resolution Ladder (Step 2-4 fallback when Apollo returns null/empty/unknown on `state` or `country`):**

     | Step | Source | Confidence -> Tier write | Cost |
     |---|---|---|---|
     | 2 | `web_fetch` on `https://[domain]` - read footer + About + Contact page | HIGH -> Tier 1 | 1-3 web_fetch calls |
     | 3 | `web_fetch` on `https://www.linkedin.com/company/[slug]/about` Headquarters block | MEDIUM -> Tier 2 | 1 web_fetch |
     | 4 | `web_search` `"[domain] WHOIS registrant address"` -> registrant city/state | LOW -> Tier 3 hold (applied + surfaced) | 1 web_search |

     Run in order; stop at first HIGH/MEDIUM result. Do NOT skip step 2 to "save fetches" - the website is HIGH confidence and free of Apollo cost. The on-disk run report MUST include source attribution per write (e.g., "state filled via website footer" or "via LinkedIn About"). Handle web_fetch failure modes per Run-Time Invariants D below (proxy block / NXDOMAIN / timeout / captcha).
   - Strategic exceptions (per territory-manager detection) → skip.
   - Cooper-owned accounts with known state → re-route per territory-model (Tier 1).
3. For every corrected owner: execute territory-manager Contact Owner Cascade. Contact writes are Tier 1.

### Step 2: Deprecated Enum Migration (crm-hygiene Mode 7)

1. Find companies where `customer_segment = "AI - Colocation Operator"`.
2. Migrate to `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"` (Tier 1).
3. Execute segment-classification Segment Change Cascade Rules (re-derive tier, confidence).

### Step 3: Gap Filling (crm-hygiene Modes 3, 8) - auto-drain mode

This routine fills `account_tier` deterministically (the tier compute spec is a pure function of `customer_segment`, `company_sub_segment`, signals, and `hs_is_target_account`). Sub-segment is NOT deterministic post-Phase 3 - it requires research against the 8 enriched fields per the D5 protocols, which is R1/R2 work, not R6 work. The 2026-04-24 hygiene run found 1,451 records missing `account_tier` (R6 now drains 400/run) and 748 missing `company_sub_segment` (R6 now surfaces as Tier 3 hold for R1/R2 - do NOT attempt classification in R6).

1. **Mode 3 - Missing critical fields:**
   - Missing `customer_segment` with a usable domain → surface as Tier 3 ("belongs in Routine 1 or 2 - deferred"). Do NOT enrich here; enrichment is owned by Routines 1 + 2.
   - Missing `state` → already covered by Step 1 Apollo verification + Field Resolution Ladder.
   - Missing `hubspot_owner_id` with known `state` → apply territory mapping (Tier 1). Drain cap: 200/run.
   - **Missing `account_tier` where `customer_segment` is populated** → apply the **Inlined Tier Compute Spec** section above (Steps A0 -> A -> B -> C -> D -> E -> F -> G) to derive tier, write at Tier 1. Respect `hs_is_target_account = true` (Step A returns current tier and skips the write). Drain cap: **400/run** (drains 1,451 backlog in ~4 days).
   - **Missing `company_sub_segment` where `customer_segment` is populated** → surface as Tier 3 hold for R1/R2 to classify via full enrichment. Do NOT attempt classification in R6. Sub-segment requires the 8 enriched fields + D5 protocols, which is research work outside R6's scope. The R6 tier-fill step still runs against the segment-only null fallback in §6 above (e.g., NeoCloud with null sub-segment defaults to T2 / ceiling 1 / floor 2 - safe Tier 1-2 placement) so the account_tier is set correctly even while sub_segment remains pending. R2 will fill `company_sub_segment` properly when the account hits its 120-day rotation.

     **Separate concern - retired sub-segment values that already exist on records:** if R6 reads a record where `company_sub_segment` is currently set to a RETIRED value (`Tier 1 Global Incumbent`, `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `AI - Colocation Operator`, `Managed Network Services - Network Operator`), R6 does NOT overwrite (that's a re-classification, not a hygiene fix). Surface as Tier 3 hold for R1/R2 to re-classify and log a one-line warning in the Errors section: `Retired sub-segment value on company [ID]: [value] - deferred to R1/R2`.

2. **Mode 8 - Contact-level hygiene (inlined operational logic - do NOT attempt to read `skills/crm-hygiene/SKILL.md` from the runtime):**

   **8a. Owner / segment cascade sync (Tier 1 auto-write, no drain cap):**
   1. Pull contacts with at least one associated company. For each contact, read the contact's `hubspot_owner_id` + `customer_segment` AND the associated company's `hubspot_owner_id` + `customer_segment`.
   2. **Owner mismatch:** if `contact.hubspot_owner_id != company.hubspot_owner_id`, write the company's owner to the contact at Tier 1. (Strategic exceptions per Step 1 still skip.)
   3. **Segment mismatch:** if `contact.customer_segment != company.customer_segment`, write the company's segment to the contact at Tier 1. Company is source of truth.
   4. Skip contacts associated to multiple companies (ambiguous - surface count only). Skip if the company itself is `customer_segment = "Flagged for deletion"` (Routine 4 owns those).

   **8b. Orphaned-contact auto-association (Tier 2 auto-write, drain cap 300/run, drains 995 backlog in ~4 days):**
   1. Pull contacts WHERE no associated company (orphans). HubSpot MCP: `search_crm_objects` on `contacts` with filter `associations.company` empty / absent.
   2. For each orphan, extract email domain: lowercase `email`, take everything after the `@`. Skip if email is blank, freemail (gmail.com, yahoo.com, outlook.com, hotmail.com, icloud.com, aol.com, protonmail.com, me.com, mac.com, msn.com, live.com), role-based (`noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@`, `postmaster@`, `admin@`, `info@`, `support@`, `sales@`, `contact@`), or test (`@test`, `@example.com`, `@yourdomain.com`).
   3. **Domain match:** HubSpot MCP `search_crm_objects` on `companies` with filter `domain = <extracted_domain>` (exact match, case-insensitive). Also try the bare second-level domain if the email domain is a subdomain (e.g. `mail.zayo.com` -> try `zayo.com`).
   4. **Apply the match:**
      - **Exactly 1 company match** AND that company is NOT `customer_segment = "Flagged for deletion"`: create the contact-to-company association via `manage_crm_objects` (associationCategory `HUBSPOT_DEFINED`, associationTypeId for contact-to-primary-company). Cascade owner + segment from the newly-associated company to the contact (8a logic). Tier 2 - log in report as "auto-associated, please spot-check".
      - **0 matches** OR **matched company is `Flagged for deletion`**: leave orphaned. Increment orphan-no-match count.
      - **2+ matches** (ambiguous - e.g., `Lightpath Fiber` and legacy `Lightpath Inc`): leave orphaned, surface in report as `ambiguous orphan - <N> domain matches`. Do not auto-associate.
   5. **Drain cap 300/run**: stop processing once 300 orphans have been written-or-decided this run. Remaining orphans roll to tomorrow's R6 run.

   **8c. Missing-email contacts → report-only.** Surface count in DM Errors-or-Info section. No auto-fix path that doesn't burn Apollo credits, and contact email enrichment is R8 Persona Fill's job, not R6's.

### Step 4: Stale-record drain (crm-hygiene Modes 4, 5, 6, 9)

- **Mode 4 - Stale records (no activity 90+ days):** Report only - no auto-action. Stale doesn't mean junk; the contact may be valuable but cold. Surface counts.
- **Mode 5 - Incomplete enrichment tracking:** Surface stale-enrichment candidates that Routine 2 will pick up. Counts only.
- **Mode 9 - Stale NEW leads (the 9,811 backlog from 2026-04-24):** Auto-advance `hs_lead_status` from `NEW` to `OPEN` for every contact where ALL of: `createdate > 14 days ago`, `hs_lead_status = NEW`, no logged sales activity (`notes_last_contacted IS EMPTY` and `hs_email_last_send_date IS EMPTY`), no open deal association, `hs_email_optout != true`. Tier 1 auto-write. Drain cap: **1000/run** (drains 9,811 backlog in ~10 days). Reasoning: NEW means "imported but never touched"; after 14 days the import is stale and OPEN better reflects reality. Reps can still re-stage to NEW if they choose to actively work the lead.
- **Mode 6 - Completeness health score:** Include in report hero.

### Step 5: Contact Deletion Flagging (crm-hygiene Mode 11)

Auto-flag clear-cut junk contacts. Full criteria per Mode 11; protection filters apply (`hs_email_optout`, customer lifecyclestage, open deals, open POC).

**Tier 1 auto-flags:**
- Hard-bounced emails (`hs_email_hard_bounce_reason_enum` populated).
- Generic spam patterns (`noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@`).
- Test / placeholder addresses (`test@test`, `@example.com`, `@yourdomain`, `firstname` and `lastname` both "test").
- Contacts associated ONLY to `Flagged for deletion` companies with zero open deals.

**Tier 2 auto-flags (applied + surfaced):**
- No email / phone / mobilephone / company AND `createdate > 180 days` AND `lifecyclestage` in {blank, subscriber, lead} AND zero deals AND no sales-activity timestamp.

**Never-flag:**
- Contacts < 30 days old with no contact info → route to Routine 5 or persona fill, not here.

### Step 5.5: Tier + Signal Heat maintenance step

Runs AFTER all territory + hygiene writes (Steps 1-5) so the tier + heat compute sees current state. R6 does NOT recompute tier or heat for ALL accounts daily - only the accounts it TOUCHED this run for any territory or hygiene reason (owner correction, enum migration, gap fill, contact cascade upstream, Mode 11 flag).

For each touched account:

1. Read open deals associated with the account.
2. Count `open_deal_count` = deals where `dealstage` is past `appointmentscheduled` AND `dealstage` NOT in {`closedwon`, `closedlost`}. Use boolean `hs_is_closed_won` / `hs_is_closed_lost` to identify closed deals (per the deal-status check rule in Caps & Budgets - pipeline IDs are custom numeric, do NOT string-match `dealstage`).
3. Apply `-1` modifier to tier if `open_deal_count >= 1` (the "open deal" modifier per **Inlined Tier Compute Spec** §7 above).
4. Read `notes_last_contacted` (or most recent engagement timestamp) as last_activity_date.
5. Read all signal persistence fields on the company: `last_signal_score`, `last_signal_date`, `signal_count_last_30d`. Also read current `signal_heat`.
6. Compute current tier per the **Inlined Tier Compute Spec** section above (do NOT attempt to read `context/account-tiering/tier-compute-spec.md` from the runtime - it's not resolvable, the spec is inlined):
   - **Step A0:** Pre-classification guard. If `customer_segment` not in 6 active ICP segments, return without modification.
   - **Step A:** Honor `hs_is_target_account = true`. If true, SKIP the tier write (other field writes proceed normally). Log the skip reason in the Errors-or-Info section of the on-disk run report.
   - **Step B:** Look up `(customer_segment, company_sub_segment)` in the inlined defaults table (§5 above).
   - **Step C:** Apply null + unknown-pair fallback (§6 above) if either field is missing or the pair is not in the defaults table.
   - **Step D:** Apply all modifiers (hot / white-hot / stacked / open deal / stale / sustained quiet) per §7 above, in order.
   - **Step E:** Clamp to the ceiling/floor from §5 above.
7. If `new_tier != stored account_tier` AND `hs_is_target_account != true`:
   - Write `account_tier = new_tier` via HubSpot MCP.
   - Add a HubSpot company note (timeline note via `manage_crm_objects` on the engagement object, associated to the company):
     `Tier <X> -> <Y> on YYYY-MM-DD by R6 Territory & Hygiene: <reason citing modifiers applied>`
     Use a hyphen ("->"), not an em dash.
8. **Compute `signal_heat`** using the same signal-field inputs read in step 5 + the open-deal state read in step 1. **Freshness anchor (post-2026-05-28):** `last_signal_date` stores the EVENT DATE (when the news/funding/hire actually happened), not detection date. **HubSpot enum is Title Case:** `Hot` / `Warm` / `Cool` / `Cold`. Algorithm (inlined from `context/account-tiering/tier-compute-spec.md` §11.5):

   ```
   signal_heat is computed top-down, first match wins:

   Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
          OR signal_count_last_30d >= 2
          OR open_deal_count >= 1

   Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

   Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

   Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

   Override behavior:
   - hs_is_target_account = true does NOT freeze signal_heat.
     Tier is rep-locked; heat always reports the truth.

   Output: enum `Hot` | `Warm` | `Cool` | `Cold` (Title Case per HubSpot).
   ```

   If `new_heat != stored signal_heat` -> write `signal_heat = new_heat` via HubSpot MCP using Title Case values. **Heat writes proceed REGARDLESS of `hs_is_target_account`** (heat is not frozen by the target-account flag). Add a HubSpot company note: `"Heat <X> -> <Y> on YYYY-MM-DD by R6 Territory & Hygiene: <reason>"` (Title Case in the note).

9. Do NOT bump `last_enriched_date` for the tier or heat write. R6 territory / hygiene / sub_segment / tier / heat corrections are non-bumping per CLAUDE.md Unified `last_enriched_date` Stamping Policy. R2 owns the 120-day rotation guarantee.

Drift catch-all for accounts R6 did NOT touch this run is handled by R-Tier-Audit (`cowork-scheduled-tasks/r-tier-audit/prompt.md`, daily M-F 3pm CT as of 2026-05-21; was weekly Fri before that) - do not attempt to expand R6's scope to all accounts.

### Step 6: Health Score

Calculate overall CRM health score per crm-hygiene Mode 6 and include in report hero.

## Caps & Budgets

- **Record cap:** full-table sweep (3,489 companies) for read; no per-record write cap (this is a low-write routine in steady state). Full read = ~35 pages × 1s = ~35s.
- **Apollo credits (revised 2026-05-07):** monthly-only cap, no git, no shared tracker file. R6 is a state-verification consumer only - most accounts have populated state and won't need Apollo. Soft per-run target: **5 credits**. Hard per-run cap: **20 credits** (defensive ceiling).
  - **Preflight check** (Step 0 above): call `apollo_users_api_profile` once. If `monthly_consumed >= 6000` OR no headroom for at least 5 credits → set `apollo_skip = true`, fall every Step 1 Apollo path through to the Field Resolution Ladder.
  - **Per-credit account selection** when `apollo_skip = false`: prioritize (a) accounts with open deals, then (b) Tier 1 accounts, then (c) Tier 2 - stop at the 20-credit hard cap regardless of remaining candidates.
  - **Hard stop** on explicit Apollo `rate_limit` / `credit_exhausted` / `quota_exceeded` errors - flip `apollo_skip = true` mid-run, continue with ladder fallback.
  - **Cross-run accounting** lives in the on-disk run reports. Each run's on-disk report hero records `Apollo credits consumed: N (monthly: X / 6000 used after this run)`. NO git pull, NO tracker file read, NO commit/push. If Cooper wants weekly-rollup numbers, they're trivially derivable from the past 5 R6 on-disk reports (the CRM Ops Daily Digest also rolls these up).
- **HubSpot writes:** use `manage_crm_objects.updateRequest` in batch mode. **Batch cap: 10 `objects` per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. Owner cascades to contacts should still batch all contacts per company affected, but split across multiple 10-object calls if a single company has more than 10 contacts. **Soft cap 1,950 writes/run** (Step 1 territory: ~50; Step 3 tier-fill: 400; Step 3 orphan-associate: 300; Step 4 stale-NEW advance: 1000; Mode 11 contact flags: ~200) → expect ~195 batched calls per run at cap. Well under HubSpot's 250K/day rate limit. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s. (Sub-segment fill removed from soft cap 2026-05-20 - R6 no longer attempts sub-segment classification, that's R1/R2 work.)
- **Deal-status checks:** when checking deal protection, use boolean `hs_is_closed_won` + `hs_is_closed_lost` flags. Do NOT rely on `dealstage` string matching - HubSpot pipelines use custom numeric IDs (e.g. `3401264867` = Closed Won in MaiaEdge's custom pipeline) that would be missed by string comparison.
- **Duplicate detection:** explicitly deferred - Routine 3 owns company dedup, Routine 5 owns contact dedup. This routine does not run crm-hygiene Mode 2.

## Output (on-disk run report)

Write this structured report to the on-disk run report at `weekly-reports/YYYY-MM-DD/r6-territory-hygiene/run-report.md`. It is NOT a DM body (see Delivery).

- **Subject (use as the report's top heading):** `CRM Guardian - Territory & Hygiene - [YYYY-MM-DD] - [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Hero:** health score, owner corrections applied, deprecated enums migrated, contact flags applied, Apollo credits consumed.
- **Territory corrections (Tier 1/2):** company ID, old owner → new owner, reason (state mapping / Apollo-refreshed state / Cooper-owned re-route).
- **Enum migrations (Tier 1):** companies migrated from deprecated values.
- **Tier + Heat maintenance (Step 5.5):** count of accounts re-tiered this run, table of `(company_id, old_tier -> new_tier, modifier reason)`, count of `hs_is_target_account = true` tier-write skips, count of retired-sub-segment rejections (with company IDs). Plus count of accounts where `signal_heat` changed, table of `(company_id, old_heat -> new_heat, reason)`, count of heat writes on `hs_is_target_account = true` accounts (heat is not frozen by the target-account flag - this count is informational, not an exception).
- **Contact hygiene:** owner cascades, segment syncs, Mode 11 flags (Tier 1 + Tier 2 counts).
- **Stale / completeness reports:** counts from Modes 4, 5, 6, 9 - informational, no action taken.
- **Tier 3 held:**
  - State still blank after Apollo.
  - Missing segment on accounts with domains (deferred to Routine 1/2).
  - Strategic-exception owner overrides (surfaced for visibility, not action).
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian - Routine 6: Territory & Hygiene | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the on-disk run report's Errors section and continue - do not abort the routine.

## Delivery - quiet on success, ping only on hard failure

Do NOT DM Cooper a per-run debrief, and do NOT send an early-checkpoint smoke-signal DM. On a clean or partial-but-recoverable run, the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r6-territory-hygiene/run-report.md` (the Output structure above is that report, not a DM body - health score in hero, correction tables, Apollo credits line `Apollo credits consumed: N (monthly: X / 6000 used after this run)`), and (2) the one Run-log row this routine already appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji from the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`, self-DM, workspace `maia-edge.slack.com`) ONLY on a hard failure - HubSpot, Slack, or Apollo MCP unreachable, an abort (e.g. the Step 0 HubSpot-unreachable abort), or zero records processed against a non-empty work queue - as ONE line:
`:red_circle: CRM Guardian - Territory & Hygiene [FAILED/ABORTED/PAUSED] - [one-clause reason].`
Still write the matching ❌/⚠️ Run-log row to the canvas. Retry the ping once (1s -> 2s); if it still fails, the disk report + Run-log row are the fallback.
