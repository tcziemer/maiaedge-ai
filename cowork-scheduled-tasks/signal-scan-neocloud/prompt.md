# Signal Scan — NeoCloud (Cowork scheduled task)

You are running the **NeoCloud segment** of MaiaEdge's weekly signal scan. This is one of 6 per-ICP scans that fire on Monday morning; the **Aggregator** task (`signal-scan-aggregator`, fires Mon 2:30pm CT) reads what all 6 wrote to HubSpot and builds the consolidated rep DMs + canvas Run log row + Cooper run report.

Your job: scrape NeoCloud signal sources, score hits, write the 5 signal fields + tier to HubSpot, save a segment audit on disk. **Do NOT send rep DMs, do NOT update the canvas, do NOT write a Cooper run report.** That's the aggregator's job at 2:30pm CT.

**NeoCloud is the highest-velocity segment** — most signals decay in 2-4 weeks before connectivity defaults to a vendor. Source coverage is broader than any other segment. Weekly cadence is mandatory.

## What changed 2026-05-28 (engine unification)

- `last_signal_date` semantics narrowed: stores the **event date** (when the news/funding/hire actually happened), NOT the engine's detection date.
- `recent_news_or_trigger_event` narrative format is now **pure prose** — legacy `[YYYY-MM-DD] [Signal Type] - one-liner` prefix retired. Date lives in `last_signal_date`.
- `signal_heat` enum is **Title Case** (`Hot` / `Warm` / `Cool` / `Cold`) per HubSpot.
- Final 5-field signal engine: `recent_news_or_trigger_event` (narrative), `last_signal_date` (event date), `last_signal_score`, `signal_count_last_30d`, `signal_heat`. No new properties.
- `account_brief` is **pure prose, NO `[Routine N] [date]:` prefix** (Operating Principle #4). Audit goes to on-disk segment-run-report + Cooper run report.

## What changed 2026-06-04 (coverage expansion)

- **Detection window widened 14d -> 180 days** (event-date basis), aligned to the `Cool` heat horizon. Anything scoring >=8 that computes to Hot/Warm/Cool is written; only >180d (Cold-by-recency) drops for staleness. Ends the prior behavior where 15-180-day-old material events were discarded before scoring (the cause of the 2026-06-01 near-empty quiet week).
- **Scope widened to all tiers** - the target query no longer filters `account_tier IN (1,2,3)`; every non-Flagged record in this segment is eligible. Matched-account writes cost no Apollo; heat still ranks rep priority.
- **Anti-churn write rule** (Stage 5b) prevents the wide window from re-writing aging signals weekly.
- **Tier A freshness gained a 90-180d ×1 band** so strong, still-relevant events clear the score-8 floor out to 180 days.
- **Context-budget safeguard** (Stage 1) - sub-agent fan-out + batched writes + a real overflow backlog, since scope/window expansion roughly doubles candidates and risks the context-wall that forced the 2026-05-28 split.

## Phase 3 mode (locked rules)

- **Detection window: 180 days rolling** (event date within last 180 days - the `Cool` heat horizon). Any signal scoring >=8 that computes to Hot/Warm/Cool is written; only events >180 days old (Cold-by-recency) drop for staleness. (Widened from 14d on 2026-06-04 - the old gate discarded 15-180-day-old material events before scoring.)
- **Score floor: 8.** Score 12+ = Primary cascade (Highest 27+ / Strong 18-26 / Worth Reviewing 12-17). Score 8-11 = LIGHT cascade. Below 8 = silent drop.
- **Search-anchor pattern** is the canonical access method. `web_search "{domain} {topic} {year}"` then `web_fetch` on article URLs returned. Generic searches that don't anchor on a documented source do NOT count.
- **Stage 5b writes 5 signal fields + tier + heat** for every score ≥8 match. `hs_is_target_account = true` freezes tier write only; heat always writes.
- **Signal code prefix is `NC-` for NeoCloud** (disambiguates from Network Operator `NO-` codes). Pattern matching in the catalog uses bare `N-` but runtime tagging in HubSpot writes uses the `NC-` prefix.

## Scope — NeoCloud only

HubSpot target query:
```
customer_segment = "NeoCloud"
-- all account_tier values in scope (no tier filter as of 2026-06-04); Flagged-for-deletion is already excluded by the customer_segment filter above
AND type != "Customer"
AND id != 124293230301  -- MaiaEdge's own record
```

Plus the Tier 3 carryover pool from canvas `F0B0AFSB9LN` (read at Stage 0).

Sub-segments (case-sensitive; used at Stage 3 NEW-account classification):
- `Large Scale GPU - Neocloud`
- `Tier 1 Inference - Neocloud`
- `AI Infrastructure providers - Neocloud` (lowercase "p" on providers)
- `Sovereign AI Clouds - Neocloud`
- `Crypto to AI - Neoclouds` (trailing "s"; INCLUSIVE of operator AND landlord per Operating Principle #9)
- `Greenfield` (cross-segment; pairs with Colo OR NeoCloud parent)

## Apollo budget

Sub-cap for this task: **55 credits/run** (highest among the 6 per-segment scans — NeoCloud has the most NEW-account discovery volume). At Stage 0, read `weekly-reports/apollo-budget.json`; effective budget = `min(55, available_in_weekly_pool)`.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_fetch, web_search. Abort + DM Cooper (`U0A24D9RJLS`) if any required MCP is unavailable.
2. **Read canvas `F0B0AFSB9LN`** via `slack_read_canvas`. Pull Tier 3 carryovers tagged with this segment.
3. **Read Apollo budget tracker** at `weekly-reports/apollo-budget.json`. Compute `effective_apollo = min(55, weekly_remaining)`.
4. **Build target list** (all tiers, non-Flagged) via `search_crm_objects` with the scope filter above. Cap at 1000 records. NOTE (2026-06-04): removing the tier filter materially enlarges this pool (all-tier vs the prior Tier 1-3); rely on the Stage 1 context-budget safeguard (sub-agent fan-out + batched writes + overflow backlog) to stay within budget.
5. **Check the prior Monday's segment-run-report** at `weekly-reports/[YYYY-MM-DD minus 7 days]/signal-scan/neocloud/segment-run-report.md`. Use for source-coverage delta. If absent, skip and tag everything `NEW`.

---

## Stage 1 — Signal Detection (NeoCloud sources only, 180-day window)

**Context-budget safeguard (2026-06-04).** The 180-day window + all-tier scope roughly doubles the candidate set, which risks the context-wall that forced the 2026-05-28 per-segment split. To stay within budget: (a) fan out source detection through research sub-agents so raw source text does not all live in the main context; (b) stream the matched-account list and write in batches of 10 rather than holding every candidate resident; (c) if scored candidates exceed 60 in a single run, write what you can this run and persist the remainder to `weekly-reports/[today CT]/signal-scan/neocloud/backlog.md` - the NEXT run reads and processes that backlog FIRST (a real carry that always writes, not a discard). Out-of-window deferral no longer exists; the only carry is this budget-overflow backlog.

### Per-segment signal codes (NC- prefix for NeoCloud disambiguation from NO- Network Operator)

| Code | Signal | Tier | Freshness | Confidence baseline |
|---|---|---|---|---|
| **NC-A0** | Greenfield S2/S3 (permit + utility + GPU-backed debt naming new region) | A | 90d | HIGH |
| **NC-A1** | Site Count Transition 1→2 regions (+6 score bonus) | A | 90d | HIGH |
| **NC-A2** | New Facility / Region Launch (N→N+1) | A | 1wk | HIGH |
| **NC-A3** | NVIDIA DGX Cloud Lepton / NCP / Exemplar Cloud Partner Announcement | A | 1wk | HIGH |
| **NC-A4** | Enterprise Customer Win (non-hyperscaler) | A | 1wk | HIGH |
| **NC-A5** | GPU-Backed Debt Raise / Credit Facility | A | 30d | HIGH |
| **NC-A6** | Network / SRE / Observability Hiring Spike (3+ roles in 30d) | A | 30d | HIGH |
| **NC-A7** | Anchor Tenant Signing (enterprise or hyperscaler; dual-sided with C-A6) | A | 1wk | HIGH |
| **NC-A8** | Colo Lease Filing (SEC 8-K Item 1.01 / 2.03) | A | 1wk | HIGH |
| **NC-A9** | PeeringDB Changes (new netixlan / netfac / prefix) | A | weekly diff | HIGH |
| **NC-A10** | IX Member Addition (100G/400G port at DE-CIX / AMS-IX / LINX / Equinix IX / SIX / Any2) | A | weekly | HIGH |
| **NC-A11** | MLPerf Inference / Training Submission (first-time submitter OR new category) | A | bi-annual | HIGH |
| **NC-B1** | SEC Filing CapEx / Capacity Disclosure (public NeoClouds) | B | 90d | HIGH |
| **NC-B2** | Series B+ / Growth Equity Funding Round | B | 90d | HIGH |
| **NC-B3** | Sovereign AI / Government Contract Win | B | 90d | HIGH |
| **NC-B4** | Multi-Carrier / Multi-Colo Partnership Press | B | 90d | MED-HIGH |
| **NC-B5** | Blackwell / GB200 / GB300 Allocation Win | B | 90d | HIGH |
| **NC-C1** | Crypto-to-AI Pivot Filing (10-K/10-Q pivot language) | C | 90d | MED-HIGH |
| **NC-C3** | Public Outage / Status Page Incident — context only, NEVER standalone | C | 60d | MED-HIGH for angle-only |
| **NC-C4** | Inference-Focused Product Launch / Pricing | C | 90d | MED |
| **NC-C5** | Executive Departure / Key Network-Role Hire | C | 60d | MED-HIGH arrival / HIGH departure |

### Compound Signals — Triple-Firing (auto-elevate to score 18+)

When stacked, meeting probability approaches certainty:

- **Funding + network hiring spike + new facility** = enterprise-scaling wall in real time
- **Debt raise + enterprise customer win** = margin pressure + first non-hyperscaler SLA
- **NVIDIA Lepton/Exemplar + multi-colo partnership** = NVIDIA forcing observability customer hasn't scoped
- **Funding + greenfield S2-S3 + facility count = 1** = capital + site #2 + first-ever multi-site design

### Tier 1 Qualifier Filter

Per [`context/segments/neocloud.md`](../../context/segments/neocloud.md): 5+ facilities, 100MW+ announced GPU capacity, enterprise growth plan referenced, active observability gap.

Plus the **Universal signal types** (U1-U6) and **Apollo signal classes** (AP-1, AP-2, AP-3, AP-4 paired, AP-7, FR-1 — AP-5/AP-6 disabled per noise list).

### Source Registry (NeoCloud — execute every source, record ✓/✗ in audit)

Per [`context/signals/neocloud-signals.md`](../../context/signals/neocloud-signals.md) §"Sources for This Segment".

**Robust tier (single-source can score HIGH on non-major signals):**
1. Data Center Frontier + Data Center Dynamics + Data Center Knowledge + The Register data centre
2. NVIDIA Newsroom + GTC press + NVIDIA partner page (DGX Cloud Lepton, NCP, Exemplar Cloud) — NVIDIA announces partner deals before the NeoCloud does
3. StockTitan (`stocktitan.net/sec-filings/{ticker}/`) — SEC 8-K mirror for public NeoCloud filers (CRWV, APLD, HUT, CORZ, IREN, BITF, MARA, WULF, CLSK, GLXY); covers 8-K Items 1.01 / 2.03 / 5.02 + S-1 / 424 + Form D
4. SEC EDGAR full-text via search-anchor — backup to StockTitan
5. Crypto-to-AI outlets — CoinDesk, Bitcoin Magazine, Cryptopolitan, news.bitcoin.com (24-48h ahead of mainstream on miner-to-AI pivot signals — promoted from Medium to Robust 2026-05-11)
6. IX member-list pages — DE-CIX, AMS-IX, LINX, Equinix IX, SIX, Any2, plus AMS-IX Asia, NetIX, AfricaIX for international (NC-A10)
7. Greenhouse + Lever + Ashby public job boards at target NeoClouds (NC-A6)
8. Apollo MCP — `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events
9. HPCwire + The Next Platform + ServeTheHome — technical confirmations of new GPU regions, deployment scale
10. Crunchbase News + TechCrunch + SiliconANGLE — AI Infrastructure tag, Cloud Computing tag
11. PR Newswire + Business Wire + GlobeNewswire — AI/Cloud Computing feed + Appointments tag
12. Per-NeoCloud IR / newsroom pages — CoreWeave, Nebius, Applied Digital, Hut 8, Iris Energy (IREN), Marathon Digital, TeraWulf, Bitfarms, Galaxy Digital, Fluidstack, Lambda, Cerebras (highest-yield single-company source)

**Medium tier (cross-source confirm preferred for major M&A / anchor-tenant / sovereign-AI claims):**
13. The Information — paywalled but headlines + lede paragraphs surface in search snippets
14. SemiAnalysis (Dylan Patel) — insider deployment news; headlines accessible
15. Compute Forecast newsletter — independent GPU economy tracker
16. Latent Space newsletter / podcast (Swyx) — NeoCloud deep-dives
17. Last Week in AI newsletter — weekly AI infra digest
18. Import AI newsletter (Jack Clark)
19. AI Index (Stanford HAI) — annual + interim deal trackers
20. Hugging Face Spaces partner announcements — model providers naming NeoCloud infra partners
21. WGMI ETF holdings + Hashrate Index — crypto-to-AI sub-segment context
22. Moody's / DBRS / Fitch debt-rating notes — GPU-backed lending coverage
23. AI Infrastructure Summit + NVIDIA GTC + Open Compute Summit — conference agenda scrapers (context only)
24. Cross-segment exec hire stack — StockTitan 8-K 5.02, PR Newswire Appointments, IR newsroom diffs, Crunchbase Exec Moves

**International (Tim Z territory — sovereign AI is the hot zone):**
- **EMEA:** EuroHPC JU AI Factory awards (13 awarded; each = neocloud-adjacent buildout), Gaia-X Federation, EURO-3C, IPCEI Next-Gen Cloud, UK AIRR / Isambard-AI, Bpifrance France 2030 AI grants. Key NeoClouds: Nebius, Nscale, Scaleway, Northern Data, Gcore, Ori, Nexgen Cloud, Atlas Cloud.
- **APAC:** IndiaAI (~62k GPUs Mar 2026), Japan IOWN Forum, METI Japan AI grants, MeitY India, Singapore AI Strategy 2.0, KISA Korea, NSTDA Thailand. Key NeoClouds: Shakti, Yotta (IN), Sustainable Metal Cloud (SG).
- **MENA:** HUMAIN (KSA), G42 (UAE), MGX, SDAIA, Zawya + AGBI.
- **I2 Sovereign AI Compute Grant** = core international signal class; +3 score bonus. EuroHPC AI Factory award = greenfield-equivalent (6-18mo before GPU cluster online).

**Source Coverage Mandate:** every documented source above MUST be attempted via search-anchor and recorded ✓ / ✗. Generic queries that don't anchor on a documented source do NOT count.

### False-positive patterns — DOWNGRADE or EXCLUDE at detection time

| Pattern | Action |
|---|---|
| Series Seed at a stealth NeoCloud (<50 employees) | DOWNGRADE to MEDIUM → route to Watch List (too early for MaiaEdge engagement) |
| Earnings transcript mention of inference SLA without product page | DOWNGRADE to MEDIUM |
| "Anchor tenant" filing with unnamed counterparty / "major tech company" | DOWNGRADE unless inferable from context |
| Status page incident standalone (no other Tier A/B signal) | EXCLUDE per NC-C3 demotion — never customer-facing |
| Conference speaking slot alone | EXCLUDE per noise list |
| AP-6 Apollo Intent without pairing | EXCLUDE (>50% false-positive) |
| Bitcoin miner with no public pivot filing (just speculation) | EXCLUDE — must have 10-K/10-Q HPC language to qualify for NC-C1 |
| GitHub commits from `@gmail.com` / personal email even if username matches employee | DOWNGRADE to MEDIUM (corporate-domain author = HIGH only) |

---

## Stage 2 — Match detected signals to target accounts

For each detected signal candidate:
1. Exact company name match (case-insensitive)
2. Domain apex match + subdomain variants
3. LinkedIn slug match
4. PeeringDB ASN match (NC-A9 specific)

Surviving → `matched_accounts[]`. Unmatched → `new_account_candidates[]` (route to Stage 3 if Apollo allows).

---

## Stage 3 — NEW-account creation (Apollo-bound, max 55 credits)

For each `new_account_candidate`:

1. **D1 disqualifier check** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D1.
2. **Stage 1a–1c research-first workflow** per [`skills/company-enrichment/SKILL.md`](../../skills/company-enrichment/SKILL.md).
3. **Apollo enrichment**. Decrement budget.
4. **Segment routing per D3 flowchart** — must route to `customer_segment = "NeoCloud"` to remain in scope. **Crypto-to-AI Bitcoin miners** route to `Crypto to AI - Neoclouds` sub-segment per Operating Principle #9 (inclusive of operator + landlord models).
5. **D5 sub-segment protocol** per [`context/account-tiering/enrichment-protocols.md`](../../context/account-tiering/enrichment-protocols.md) §6 + §6a (NC1 vs NC3 vs NC2 deterministic threshold matrix on disclosed GPU MW + facility count + pricing model + customer profile).
6. **Compute tier** per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). Default `signal_heat = Cold` on new accounts.
7. **Write to HubSpot**. Bump `last_enriched_date = today (CT)` — full enrichment pass per Unified Stamping Policy.

If Apollo exhausts mid-Stage 3, finish current record then halt. Remaining surface in audit.

---

## Stage 4 — Score each matched signal

```
Score = Tier × Freshness × Confidence

Tier:        A = 3, B = 2, C = 1
Freshness:   Tier A:  ≤60d = 3, 60-90d = 2, 90-180d = 1, >180d = drop
             Tier B:  ≤1wk = 3, ≤30d = 2, ≤90d = 1, >90d = drop
Confidence:  HIGH = 3, MEDIUM = 2, LOW = 1

Bonuses:
  +6 if 2+ signals same account in same 30d window AND at least one signal ≥8
  +6 if M&A announcement AND close both fire within 12mo
  +3 if greenfield Stage S2/S3 (NC-A0)
  +6 if 1→2 region transition (NC-A1; requires confident infrastructure_profile parse)
  +3 if I2 Sovereign AI Compute Grant (international)
  Compound Signal auto-elevate to 18+ (see Stage 1)

Score ranges:
  27+   → Highest Priority cascade tier
  18-26 → Strong Signals cascade tier
  12-17 → Worth Reviewing cascade tier
  8-11  → LIGHT cascade tier
  <8    → Silent drop
```

Highest-scored signal per account wins for the narrative + date write.

---

## Stage 4.5 — Sub-Agent QA Gate (10 rules)

1. **Source URL verification** — cited URL is real, reachable, returns content matching the signal claim.
2. **Freshness** — event date within 180 days rolling window. Drop only if older than 180 days (it would compute to `Cold`).
3. **Segment classification** — `customer_segment = "NeoCloud"` post-Stage 3.
4. **Field overflow** — narrative ≤250 chars.
5. **Owner mapping** — `hubspot_owner_id` maps to a current territory owner: Lieto NE+West `161889085` / Ken SE `162339176` / Tory Central `165480917` / Markus Europe `164949459` / Ziemer Intl+Tier 1 SP `159350430` / Cooper Unassigned `160267902`. Owner-less → audit for Cooper.
6. **Rep-facing copy scan** — pure prose, no `[YYYY-MM-DD]` prefix, no `[Routine N]` tag, no em dashes, no competitor names.
7. **Score arithmetic** — math correct, bonuses applied.
8. **Dedup** — same signal not double-counted from 2 sources.
9. **NEW/CARRIED integrity** — if CARRIED tag asserted, prior segment-run-report confirms; else NEW.
10. **Pure-prose narrative** — confirm Stage 5 writes pure prose.

Any rule failure → fix or drop. Log drops in audit under "QA gate drops".

---

## Stage 5 — HubSpot narrative write (pure prose, NO date prefix)

**Anti-churn write rule (required under the 180-day window):** write the signal fields only if the detected event date is newer than the record's current `last_signal_date`, OR the record has no `last_signal_date`, OR the new score exceeds the stored `last_signal_score`. If the freshest detected signal is not newer or higher than what is already stored, skip the write (idempotent no-op). Never overwrite a newer stored signal with an older detection. This keeps the wide window from re-writing the same aging signal every Monday.

For each scored hit ≥8 that passes the anti-churn rule, write `recent_news_or_trigger_event` via `manage_crm_objects` (batches of 10, 250ms between, exponential backoff on 429).

- **Format:** pure-prose 1-sentence narrative, ≤250 chars. Examples: `"GPU-Backed Debt Raise — CoreWeave closed $7.5B asset-backed financing for Blackwell allocation buildout; deterministic-path SLA pressure rising on tenant SLAs"` or `"PeeringDB Diff — Nebius added netfac at Equinix LD7 + new 400G IX session at LINX; UK region coming online"`.
- **NO leading `[YYYY-MM-DD]` prefix.** Date lives in `last_signal_date`.
- **NO `[Routine 2]` / `[Signal Scan]` / `[NeoCloud]` tag.** Routine identity is recoverable from `last_enriched_date` + on-disk audit.
- **NO em dashes** (use hyphens or restructure).
- **NO competitor names.**

**Do NOT bump `last_enriched_date`** (partial signal write). Exception: Stage 3 NEW-account creates DO bump.

---

## Stage 5b — Structured signal fields + tier/heat recompute

For each scored hit:

- **`last_signal_date`** = event date from source article (NOT today's date).
- **`last_signal_score`** = computed score from Stage 4.
- **`signal_count_last_30d`** = recompute (increment if new and within 30d, reset to 1 if all prior ≥30d).
- **`signal_heat`** = computed per inlined spec below (Title Case enum).
- **`account_tier`** = recomputed. **SKIP tier write if `hs_is_target_account = true`**.

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

**Do NOT bump `last_enriched_date`** (partial signal write).

---

## Stage 5c — Save segment audit on disk

Write a per-segment run report to:
```
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/neocloud/segment-run-report.md
```

Content:
1. Run header (date, segment, Apollo consumed X of 55, runtime, MCPs).
2. Source coverage table (every documented source above, ✓ / ✗; track 3-week ✗ streak).
3. Candidate funnel (target list size, candidates, matches, NEW accounts, total writes, drops).
4. Score distribution (8-11, 12-17, 18-26, 27+).
5. Writes summary per record (id, name, NC- signal code, score, heat delta, tier delta).
6. Tier 3 holds (carryover records still Tier 3; re-append to canvas `F0B0AFSB9LN`).
7. QA gate drops with reasons.
8. Failed writes.
9. Apollo budget post-run.
10. Compound-signal detections (any triple-firing matches above).

End the run. **No rep DMs, no canvas Run log, no Cooper run report.** Aggregator at 2:30pm CT handles all three from HubSpot writes.

---

## Failure handling

- **HubSpot MCP errors:** retry (250ms → 1s → 4s, max 3). Log to "Failed writes".
- **web_fetch / web_search errors:** log source as ✗. 3-week streak auto-flags.
- **Apollo MCP errors mid-Stage-3:** halt Stage 3, continue Stage 4 for matched-account writes.
- **PeeringDB API errors (NC-A9):** log as ✗, drop NC-A9 detection for this run.
- **Canvas read failure:** proceed without carryover, log warning.
- **Git contention on Apollo budget tracker:** log + continue; JSON updated locally.

## End-of-run footer

Log a single one-line summary to Cowork chat:
```
[NeoCloud] target=N matched=N new=N writes=N heat_promotions=N apollo=N/55 runtime=Nmin audit=weekly-reports/YYYY-MM-DD/signal-scan/neocloud/
```

No Slack DM from this task. The aggregator owns rep + Cooper communication.
