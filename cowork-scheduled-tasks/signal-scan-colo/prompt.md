# Signal Scan — Data Center Colo Provider (Cowork scheduled task)

You are running the **Colo segment** of MaiaEdge's weekly signal scan. This is one of 6 per-ICP scans that fire on Monday morning; the **Aggregator** task (`signal-scan-aggregator`, fires Mon 2:30pm CT) reads what all 6 wrote to HubSpot and builds the consolidated rep DMs + canvas Run log row + Cooper run report.

Your job: scrape Colo signal sources, score hits, write the 5 signal fields + tier to HubSpot, save a segment audit on disk. **Do NOT send rep DMs, do NOT update the canvas, do NOT write a Cooper run report.** That's the aggregator's job at 2:30pm CT.

## What changed 2026-05-28 (engine unification)

- `last_signal_date` semantics narrowed: stores the **event date** (when the news/funding/hire actually happened), NOT the engine's detection date.
- `recent_news_or_trigger_event` narrative format is now **pure prose** — the legacy `[YYYY-MM-DD] [Signal Type] - one-liner` prefix convention is retired. The date lives structurally in `last_signal_date`.
- `signal_heat` enum is **Title Case** (`Hot` / `Warm` / `Cool` / `Cold`) per HubSpot.
- Final 5-field signal engine: `recent_news_or_trigger_event` (narrative), `last_signal_date` (event date), `last_signal_score`, `signal_count_last_30d`, `signal_heat`. No new properties.
- `account_brief` is **pure prose, NO `[Routine N] [date]:` prefix** (Operating Principle #4). If you reclassify a tier or eviction, audit goes to the on-disk segment-run-report + Cooper run report, NOT into `account_brief`.

## What changed 2026-06-04 (coverage expansion)

- **Detection window widened 14d -> 180 days** (event-date basis), aligned to the `Cool` heat horizon. Anything scoring >=8 that computes to Hot/Warm/Cool is written; only >180d (Cold-by-recency) drops for staleness. Ends the prior behavior where 15-180-day-old material events were discarded before scoring (the cause of the 2026-06-01 "1 write fleet-wide" quiet week).
- **Scope widened to all tiers** - the target query no longer filters `account_tier IN (1,2,3)`; every non-Flagged record in this segment is eligible. Matched-account writes cost no Apollo; heat still ranks rep priority.
- **Anti-churn write rule** (Stage 5b) prevents the wide window from re-writing aging signals weekly.
- **Tier A freshness gained a 90-180d ×1 band** so strong, still-relevant events clear the score-8 floor out to 180 days.
- **Context-budget safeguard** (Stage 1) - sub-agent fan-out + batched writes + a real overflow backlog, since scope/window expansion roughly doubles candidates and risks the context-wall that forced the 2026-05-28 split.

## Phase 3 mode (locked rules)

- **Detection window: 180 days rolling** (event date within last 180 days - the `Cool` heat horizon). Any signal scoring >=8 that computes to Hot/Warm/Cool is written; only events >180 days old (Cold-by-recency) drop for staleness. (Widened from 14d on 2026-06-04 - the old gate discarded 15-180-day-old material events before scoring.)
- **Score floor: 8.** Score 12+ = Primary cascade tier (Highest 27+ / Strong 18-26 / Worth Reviewing 12-17). Score 8-11 = LIGHT cascade tier. Below 8 = silent drop, no CRM write.
- **Search-anchor pattern** is the canonical access method. For each documented source, run `web_search "{domain} {topic} {year}"` and read snippets + follow article URLs returned. `web_fetch` is a follow-up against article URLs, not against documented source domains directly. Generic searches that don't anchor on a documented domain do NOT count toward source coverage.
- **Stage 5b writes 5 signal fields + tier + heat** for every account with a score ≥8 match. `hs_is_target_account = true` freezes `account_tier` write only; heat always writes.

## Scope — Data Center Colo Provider only

HubSpot target query:
```
customer_segment = "Data Center Colo Provider"
-- all account_tier values in scope (no tier filter as of 2026-06-04); Flagged-for-deletion is already excluded by the customer_segment filter above
AND type != "Customer"
AND id != 124293230301  -- MaiaEdge's own record
```

Plus the Tier 3 carryover pool from canvas `F0B0AFSB9LN` (read at Stage 0).

Sub-segments (used at Stage 3 NEW-account classification — must route to one of these to remain in scope):
- `Standard - colo`
- `AI Signals - colo`
- `Modular - colo`
- `Hyperscale Wholesale - colo`
- `Greenfield` (cross-segment; pairs with Colo OR NeoCloud parent)

## Apollo budget

Sub-cap for this task: **35 credits/run** against the shared 850/week cap. At Stage 0, read `weekly-reports/apollo-budget.json`; effective budget = `min(35, available_in_weekly_pool)`. Stage 3 NEW-account creation is the only Apollo consumer. Post-run, append consumption to the tracker (best-effort; do NOT block on git contention).

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_fetch, web_search. Abort + DM Cooper (`U0A24D9RJLS`) if any required MCP is unavailable.
2. **Read canvas `F0B0AFSB9LN`** via `slack_read_canvas`. Pull any Tier 3 carryover items tagged with this segment from prior runs. Add to target pool.
3. **Read Apollo budget tracker** at `weekly-reports/apollo-budget.json`. Compute `effective_apollo = min(35, weekly_remaining)`. If `effective_apollo <= 0`, Stage 3 NEW-account creation is disabled for this run (still process matched-account writes normally).
4. **Build target list** via `mcp__claude_ai_HubSpot__search_crm_objects` with the scope filter above (all tiers, non-Flagged). Cap at 1000 records. NOTE (2026-06-04): removing the tier filter materially enlarges this pool (all-tier Colo vs the prior ~150-250 Tier 1-3); rely on the Stage 1 context-budget safeguard (sub-agent fan-out + batched writes + overflow backlog) to stay within budget.
5. **Check the prior Monday's segment-run-report** at `weekly-reports/[YYYY-MM-DD minus 7 days]/signal-scan/colo/segment-run-report.md`. Use it for source-coverage delta in the audit table. If absent (first run), skip this comparison and tag everything `NEW`.

---

## Stage 1 — Signal Detection (Colo sources only, 180-day window)

**Context-budget safeguard (2026-06-04).** The 180-day window + all-tier scope roughly doubles the candidate set, which risks the context-wall that forced the 2026-05-28 per-segment split. To stay within budget: (a) fan out source detection through research sub-agents so raw source text does not all live in the main context; (b) stream the matched-account list and write in batches of 10 rather than holding every candidate resident; (c) if scored candidates exceed 60 in a single run, write what you can this run and persist the remainder to `weekly-reports/[today CT]/signal-scan/colo/backlog.md` - the NEXT run reads and processes that backlog FIRST (a real carry that always writes, not a discard). Out-of-window deferral no longer exists; the only carry is this budget-overflow backlog.

### Per-segment signal codes (this segment's actionable patterns)

| Code | Signal | Tier | Freshness | Confidence baseline |
|---|---|---|---|---|
| **C-A0** | Greenfield Stage S2/S3 (permit + utility interconnection) | A | 90d | HIGH at S2-S3 |
| **C-A1** | Site Count Transition 1→2 facilities (+6 score bonus) | A | 90d | HIGH |
| **C-A2** | GPU Cloud Tenant Anchor (Lambda/Crusoe/Nebius/Nscale/Together AI/Fluidstack/Vultr/RunPod) | A | 30d | HIGH |
| **C-A3** | Liquid Cooling / D2C / Immersion deployment | A | 60d | HIGH |
| **C-A4** | Exec Hire — VP/Director Interconnection/Network/Fabric (within 90d of start) | A | 90d | HIGH |
| **C-A5** | Network Engineering Job-Req Surge (3+ concurrent reqs in 30d) | A | 30d | HIGH |
| **C-A6** | Anchor Tenant Signing (hyperscaler / enterprise / neocloud lease) | A | 1wk | HIGH |
| **C-A7** | M&A / PE Recap — Announcement OR Close (two-event firing; +6 stack if both within 12mo) | A | ≤60d | HIGH |
| **C-B1** | Public Colo Earnings/8-K Interconnection-Miss Language | B | 90d | MED-HIGH |
| **C-B3** | Power Capacity Uprate / PPA Announcement | B | 90d | MED |
| **C-B4** | Conference Speaking Slot — Interconnection/AI Panel (context only, never standalone) | B | 30d pre / 14d post | HIGH |
| **C-B5** | Sovereignty / Data-Residency Announcement | B | 90d | MED-HIGH |
| **C-C1** | Hyperscaler-Adjacent Claim (<50 miles) | C | 60d | MED |
| **C-C2** | Carrier-Neutral / Meet-Me-Room Expansion | C | 60d | MED |
| **C-C3** | Tenant Churn to Equinix / Megaport (loss signal) | C | 60d | MED |
| **C-C4** | Tenant RFP / Procurement Portal Post | C | 90d | MED-HIGH when it hits |
| **C-C5** | Modular / Edge Pod Deployment | C | 60d | HIGH for Modular sub-segment |

Plus the **Universal signal types** that fire across every segment:

| Code | Signal |
|---|---|
| U1 | Exec hire in Network/Infra/Automation role |
| U2 | M&A / PE roll-up (announcement OR close) |
| U3 | New facility / market / site launch |
| U4 | Earnings / 10-Q / 8-K language shift on provisioning/NaaS/automation/private fabric/wholesale |
| U5 | Conference speaking slot (context only, never standalone) |
| U6 | Public outage / RCA / status-page incident |

Plus **Apollo signal classes** (only AP-1, AP-2, AP-3, AP-4 paired, AP-7 active in Phase 3; AP-5, AP-6 disabled per noise list):

| Code | Signal | Standalone OK? |
|---|---|---|
| AP-1 | Job change to Tier A persona (<90d) | ✅ |
| AP-2 | Competitor / adjacent employer lateral | ✅ |
| AP-3 | Apollo Scoops / News feed | ✅ |
| AP-4 | Department headcount growth ≥15% | ⚠️ Pair required |
| AP-7 | Funding / M&A filter | ✅ |
| FR-1 | SEC 8-K material filings | ✅ |

### Source Registry (Colo — execute every source, record ✓/✗ in audit)

Per [`context/signals/colocation-signals.md`](../../context/signals/colocation-signals.md) §"Sources for This Segment" — full catalog. Robust + Medium tiers below; reliability tier governs whether single-source can score HIGH (Robust) vs needs cross-source confirm (Medium / Aspirational).

**Robust tier (single-source can score HIGH on non-major signals):**
1. Data Center Frontier — Site Selection / Energy / Colocation / Edge tags + DCF People column
2. Data Center Dynamics — company tags + keyword feeds + DCD Careers + DCD People column
3. Data Center Knowledge — DCD/DCF overlap; weekly diff
4. Bisnow Data Center — national + Bisnow Local DC for project announcements
5. PR Newswire + Business Wire + GlobeNewswire — Data Center feed + Appointments tag
6. StockTitan (`stocktitan.net/sec-filings/{ticker}/`) — SEC 8-K mirror for public Colo REITs (DLR, EQIX, IRM, DBRG, COR); covers 8-K Items 1.01 / 2.01 / 5.02 + S-4
7. SEC EDGAR full-text via search-anchor — backup to StockTitan
8. Greenhouse + Lever + Ashby public job boards at target operators — covers C-A4 + C-A5
9. Apollo MCP — `apollo_organizations_enrich`, Job Postings filter, Job Changes filter (AP-1, AP-2, AP-7)
10. Hyperscaler announcement feeds — AWS What's New, Azure announcements, Google Cloud blog (region/AZ expansion → anchor tenant signal)
11. NVIDIA Newsroom + GTC press — NVIDIA names colo partners in AI factory announcements

**Medium tier (cross-source confirm preferred for major M&A / anchor-tenant claims):**
12. Crunchbase News — Data Center tag (free tier)
13. Conference agenda scrapers — PTC, Capacity Latin America, ITW, AfricaCom, Datacloud, AI Infrastructure Summit (exec speaker lists; context only)
14. AFCOM news + 7x24 Exchange chapter announcements
15. Mighty Penguin DC newsletter (low cadence, sometimes scoops trade press)
16. Cross-segment exec hire stack — StockTitan 8-K 5.02, PR Newswire Appointments, company IR RSS, Crunchbase Exec Moves (C-A4)

**International supplement (Tim Z territory):** DCD EMEA/APAC/LATAM tags, Capacity Media, Data Centre Review, EUDCA releases, BNamericas LatAm DC Watch, Zawya, AGBI. See [`context/signals/signal-framework.md`](../../context/signals/signal-framework.md) §"International Source Stack" for the full regional list.

**Source Coverage Mandate:** every documented source above MUST be attempted via search-anchor and recorded ✓ (hits found, even if 0 actionable) / ✗ (errored / unreachable / search returned nothing). Generic queries that don't anchor on a documented source do NOT count. Skipping a source silently is a QA failure.

### False-positive patterns — DOWNGRADE or EXCLUDE at detection time

| Pattern | Action |
|---|---|
| "Data center" in a name where entity is real estate brokerage / construction contractor / engineering services | EXCLUDE (apply R0-style entity check) |
| Press release announcing "AI Practice" launch from helpdesk MSP | EXCLUDE (wrong ICP) |
| "Liquid cooling" mentioned in marketing blog with no facility named | EXCLUDE |
| "BEAD award" where recipient is sub-contractor not operator | EXCLUDE |
| "Anchor tenant" filing where tenant is shell company / unnamed | DOWNGRADE to MEDIUM unless inferable |
| Conference speaking slot alone (no other signal) | EXCLUDE per noise list |
| Uptime Tier Certification | EXCLUDE (trailing indicator) |
| AP-6 Apollo Intent without pairing | EXCLUDE (>50% false-positive rate) |

---

## Stage 2 — Match detected signals to target accounts

For each detected signal candidate, attempt match against the Stage 0 target list using:
1. Exact company name match (case-insensitive, with/without legal suffix)
2. Domain apex match + common subdomain variants
3. LinkedIn slug match (where parsed from signal source)

Surviving matches → `matched_accounts[]`. Unmatched candidates → `new_account_candidates[]` (route to Stage 3 if Apollo budget allows; otherwise drop with a log entry in the audit).

---

## Stage 3 — NEW-account creation (Apollo-bound, max 35 credits)

For each `new_account_candidate`:

1. **D1 disqualifier check** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D1. If disqualified → drop, log under "D1-evicted at signal scan".
2. **Stage 1a–1c research-first workflow** per [`skills/company-enrichment/SKILL.md`](../../skills/company-enrichment/SKILL.md) — D1 quick check → deep research populates 7 enriched fields → D1 deep check.
3. **Apollo enrichment** via `apollo_organizations_enrich` for state/country/industry/employee count/revenue/funding. Decrement Apollo budget.
4. **Segment routing per D3 flowchart** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D3. Must route to `customer_segment = "Data Center Colo Provider"` to remain in scope. If it routes elsewhere (e.g. NeoCloud, Fiber), create the HubSpot record with the correct segment and let next Monday's matching per-segment scan pick it up — do NOT score the signal in this scan (signal belongs to the segment it routes to).
5. **D5 sub-segment protocol** per [`context/account-tiering/enrichment-protocols.md`](../../context/account-tiering/enrichment-protocols.md) §6.
6. **Compute tier** per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). Default `signal_heat = Cold` (Title Case) on new accounts — heat for the actual scored signal lands at Stage 5b.
7. **Write to HubSpot** via `manage_crm_objects` with `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`. Bump `last_enriched_date = today (CT)` — this is a full enrichment pass per the Unified Stamping Policy.

If Apollo budget exhausts mid-Stage 3, finish the current record then halt new-account creation. Remaining candidates surface in the audit under "Apollo cap reached".

---

## Stage 4 — Score each matched signal

**Scoring formula** (inlined from [`context/signals/signal-framework.md`](../../context/signals/signal-framework.md) §"Scoring Model"):

```
Score = Tier × Freshness × Confidence

Tier:        A = 3, B = 2, C = 1
Freshness:   Tier A:  ≤60d = 3, 60-90d = 2, 90-180d = 1, >180d = drop
             Tier B:  ≤1wk = 3, ≤30d = 2, ≤90d = 1, >90d = drop
Confidence:  HIGH = 3, MEDIUM = 2, LOW = 1

Bonuses:
  +6 if 2+ signals same account in same 30d window AND at least one signal ≥8
  +6 if M&A announcement AND close both fire within 12mo (C-A7 specific)
  +3 if greenfield Stage S2/S3 (C-A0)
  +6 if 1→2 site count transition (C-A1; requires confident infrastructure_profile parse)

Score ranges:
  27+   → Highest Priority cascade tier
  18-26 → Strong Signals cascade tier
  12-17 → Worth Reviewing cascade tier
  8-11  → LIGHT cascade tier
  <8    → Silent drop (no CRM write, no audit row, log only)
```

**Tier A freshness window (updated 2026-06-04):** announcements ≤60d score full freshness ×3; 60-90d ×2; 90-180d ×1 (so a HIGH-confidence Tier A event still clears the score-8 floor at up to 180 days and lands as `Cool`); drop only beyond 180 days. Steeper decay still applies to Tier B / C.

For each matched account, the **highest-scored** signal of the run wins for the HubSpot narrative + date write. Additional signals on the same account stack into Stage 4 scoring (compound bonus) but do NOT each produce a separate narrative.

---

## Stage 4.5 — Sub-Agent QA Gate (10 rules)

Before any write, validate every scored signal against:

1. **Source URL verification** — the cited URL is real, reachable via the same search-anchor pattern, and returns content consistent with the signal claim. NO fabricated URLs.
2. **Freshness** — event date within 180 days rolling window. Drop only if older than 180 days (it would compute to `Cold`).
3. **Segment classification** — account is `customer_segment = "Data Center Colo Provider"` post-Stage 3. Drop if it routes elsewhere.
4. **Field overflow** — narrative ≤250 chars. Trim or skip if exceeds.
5. **Owner mapping** — account has a non-null `hubspot_owner_id` mapping to a current territory owner: Northeast/West `161889085` (Lieto) / Southeast `162339176` (Ken) / Central `165480917` (Tory) / Europe `164949459` (Markus) / International + Tier 1 SP `159350430` (Ziemer) / Unassigned `160267902` (Cooper). Surface owner-less accounts in the audit for Cooper review.
6. **Rep-facing copy scan** — narrative is pure prose, no `[YYYY-MM-DD]` prefix, no `[Routine N]` tag, no em dashes (use hyphen or restructure), no competitor names (use "third-party fabrics" instead).
7. **Score arithmetic** — Tier × Freshness × Confidence math is correct; bonuses applied per the rules.
8. **Dedup** — same signal not double-counted from 2 sources (same company + same event date + same signal class = dedup, keep highest-confidence source).
9. **NEW/CARRIED integrity** — if a CARRIED tag is asserted, prior segment-run-report confirms the record. If no prior file, tag NEW.
10. **Pure-prose narrative** — confirm Stage 5 will write pure prose with no date prefix and no tag prefix.

Any rule failure → fix or drop. Log all drops in the audit under "QA gate drops".

---

## Stage 5 — HubSpot narrative write (pure prose, NO date prefix)

For each scored hit ≥8, write `recent_news_or_trigger_event` via `manage_crm_objects` (batches of 10, 250ms between batches, exponential backoff on HTTP 429, `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`).

- **Format:** pure-prose 1-sentence narrative, ≤250 chars. Examples: `"VP Network Hire — Sarah Chen (ex-AWS) joined as VP Network Engineering; 90-day fabric mandate window open"` or `"Anchor Tenant — signed 30MW build-to-suit lease with hyperscaler at Reno campus; procurement window for connectivity now open"`.
- **NO leading `[YYYY-MM-DD]` prefix.** The date lives in `last_signal_date`.
- **NO `[Routine 2]` / `[Signal Scan]` / `[Colo]` tag.** The routine that wrote it is recoverable from `last_enriched_date` + the on-disk segment-run-report.
- **NO em dashes** (use hyphens or restructure).
- **NO competitor names** in the narrative (use "third-party fabrics" / "third-party platform" / "another provider").

**Do NOT bump `last_enriched_date`.** This is a partial signal write, not a full enrichment pass (per Unified Stamping Policy in CLAUDE.md). Exception: Stage 3 NEW-account creates DO bump (the full pipeline ran).

---

## Stage 5b — Structured signal fields + tier/heat recompute

**Anti-churn write rule (required under the 180-day window):** write the signal fields only if the detected event date is newer than the record's current `last_signal_date`, OR the record has no `last_signal_date`, OR the new score exceeds the stored `last_signal_score`. If the freshest detected signal is not newer or higher than what is already stored, skip the write (idempotent no-op). Never overwrite a newer stored signal with an older detection. This keeps the wide window from re-writing the same aging signal every Monday.

For each scored hit that passes the anti-churn rule, write via the same `manage_crm_objects` batch:

- **`last_signal_date`** = event date from the source article (NOT today's date). Extract from publication date / event mention. If only article publication date is available, use it as a ±few-day approximation of the event.
- **`last_signal_score`** = computed score from Stage 4.
- **`signal_count_last_30d`** = recompute: query HubSpot for the account's prior signal history (use `last_signal_date` + any prior writes); increment if today's signal is new and within 30 days, reset to 1 if all prior signals are ≥30 days old.
- **`signal_heat`** = computed per the inlined spec below (Title Case enum: `Hot` / `Warm` / `Cool` / `Cold`). Heat ALWAYS writes — `hs_is_target_account` does NOT freeze heat.
- **`account_tier`** = recomputed per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). **SKIP the tier write only if `hs_is_target_account = true`** (target-account flag freezes tier). All other writes proceed.

### Inlined `compute_signal_heat` (from `tier-compute-spec.md` §11.5)

```
Heat is computed top-down, first match wins. HubSpot enum is Title Case.

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Override: hs_is_target_account = true does NOT freeze signal_heat.
Tier is rep-locked; heat always reports the truth.

Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
Output: enum Hot | Warm | Cool | Cold (Title Case per HubSpot).
```

**Do NOT bump `last_enriched_date`** on these writes (per the same Unified Stamping Policy carve-out — Stage 5b is a partial signal write).

---

## Stage 5c — Save segment audit on disk

Write a per-segment run report to:
```
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/colo/segment-run-report.md
```

Content:

1. **Run header** — date, segment, Apollo consumed (X of 35), runtime minutes, MCPs used.
2. **Source coverage table** — every documented source above, ✓ (hits found, even if 0 actionable) or ✗ (errored / unreachable / search returned nothing). Track 3-week ✗ streak (auto-flag for "Sources Needing Development" — surface in Cooper run report via the aggregator).
3. **Candidate funnel** — target list size, detected candidates, matched accounts, NEW accounts created, total writes, dropped by reason.
4. **Score distribution** — count by bucket (8-11 LIGHT, 12-17, 18-26, 27+).
5. **Writes summary** — per write: company id, name, signal code, score, prior heat → new heat delta, prior tier → new tier delta (or `tier write skipped: hs_is_target_account=true`).
6. **Tier 3 holds** — any records that came in as canvas carryovers and stayed Tier 3 this run. Re-append to canvas `F0B0AFSB9LN` at end of run.
7. **QA gate drops** — records dropped by Stage 4.5 with reason.
8. **Failed writes** — any `manage_crm_objects` errors, with retry attempts logged.
9. **Apollo budget post-run** — credits consumed, weekly total updated.

End the run. **Do NOT send rep DMs. Do NOT update canvas Run log. Do NOT write Cooper run report.** The aggregator at 2:30pm CT handles all three from the records you just wrote to HubSpot (HubSpot is source of truth — your audit file feeds Cooper's cross-ICP context but doesn't gate the rep DMs).

---

## Failure handling

- **HubSpot MCP errors:** retry with exponential backoff (250ms → 1s → 4s, max 3). On final failure, log to "Failed writes" in the segment-run-report and continue.
- **web_fetch / web_search errors:** log source as ✗ in coverage table and continue. 3-week ✗ streak auto-flags for Cooper.
- **Apollo MCP errors mid-Stage-3:** halt Stage 3 NEW-account creation, log remaining candidates as "Apollo halted mid-run" in audit, continue to Stage 4 for matched-account writes.
- **Canvas read failure at Stage 0:** proceed without carryover pool, log warning.
- **Git contention on Apollo budget tracker write:** log "Git commit deferred (concurrent routine); JSON updated locally" and continue. The local JSON is the source of truth; Slack DM (next aggregator) is the audit trail.

## End-of-run footer

Log a single one-line summary to Cowork chat for Cooper's at-a-glance visibility:
```
[Colo] target=N matched=N new=N writes=N heat_promotions=N apollo=N/35 runtime=Nmin audit=weekly-reports/YYYY-MM-DD/signal-scan/colo/
```

No Slack DM from this task. The aggregator owns rep + Cooper communication.
