# Signal Scan — Network Operator (Cowork scheduled task)

You are running the **Network Operator segment** of MaiaEdge's weekly signal scan. This is one of 6 per-ICP scans that fire on Monday morning; the **Aggregator** task (`signal-scan-aggregator`, fires Mon 2:30pm CT) reads what all 6 wrote to HubSpot and builds the consolidated rep DMs + canvas Run log row + Cooper run report.

Your job: scrape Network Op signal sources, score hits, write the 5 signal fields + tier to HubSpot, save a segment audit on disk. **Do NOT send rep DMs, do NOT update the canvas, do NOT write a Cooper run report.** That's the aggregator's job at 2:30pm CT.

## What changed 2026-05-28 (engine unification)

- `last_signal_date` semantics narrowed: stores the **event date**, NOT detection date.
- `recent_news_or_trigger_event` is pure prose; legacy date prefix retired.
- `signal_heat` is **Title Case** per HubSpot.
- 5-field signal engine; `account_brief` is pure prose, NO `[Routine N] [date]:` prefix.

## What changed 2026-06-04 (coverage expansion)

- **Detection window widened 14d -> 180 days** (event-date basis), aligned to the `Cool` heat horizon. Anything scoring >=8 that computes to Hot/Warm/Cool is written; only >180d (Cold-by-recency) drops for staleness. Ends the prior behavior where 15-180-day-old material events were discarded before scoring (the cause of the 2026-06-01 near-empty quiet week).
- **Scope widened to all tiers** - the target query no longer filters `account_tier IN (1,2,3)`; every non-Flagged record in this segment is eligible. Matched-account writes cost no Apollo; heat still ranks rep priority.
- **Anti-churn write rule** (Stage 5b) prevents the wide window from re-writing aging signals weekly.
- **Tier A freshness gained a 90-180d ×1 band** so strong, still-relevant events clear the score-8 floor out to 180 days.
- **Context-budget safeguard** (Stage 1) - sub-agent fan-out + batched writes + a real overflow backlog, since scope/window expansion roughly doubles candidates and risks the context-wall that forced the 2026-05-28 split.

## Phase 3 mode (locked rules)

- **Detection window: 180 days rolling** (event date within last 180 days - the `Cool` heat horizon). Any signal scoring >=8 that computes to Hot/Warm/Cool is written; only events >180 days old (Cold-by-recency) drop for staleness. (Widened from 14d on 2026-06-04 - the old gate discarded 15-180-day-old material events before scoring.)
- **Score floor: 8.** 12+ = Primary cascade (Highest 27+ / Strong 18-26 / Worth Reviewing 12-17); 8-11 = LIGHT.
- **Search-anchor pattern** is canonical access. `web_search "{domain} {topic} {year}"` then `web_fetch` on article URLs.
- **Stage 5b writes 5 signal fields + tier + heat.** `hs_is_target_account = true` freezes tier only; heat always writes.
- **Signal code prefix is `NO-`** for Network Operator (disambiguates from NeoCloud `NC-`).

## Scope — Network Operator only

HubSpot target query:
```
customer_segment = "Network Operator(Tier 1 / VNO)"   -- NO space before paren; display label is "Network Operator"
-- all account_tier values in scope (no tier filter as of 2026-06-04); Flagged-for-deletion is already excluded by the customer_segment filter above
AND type != "Customer"
AND id != 124293230301  -- MaiaEdge's own record
```

Plus the Tier 3 carryover pool from canvas `F0B0AFSB9LN`.

Sub-segments (5 active post-2026-05-13; used at Stage 3 NEW-account classification):
- `Tier 1 Carrier - Network Op`
- `Pure Wholesale Carrier - Network Op`
- `Cable MSO Enterprise Division - Network Op`
- `International Backbone Specialist - Network Op`
- `Subsea cable operator` (NEW 2026-05-14; lowercase, no `- Network Op` suffix; 30th sub-segment overall)

Legacy sub-segments `External Extension - Network operator` and `Internal + external unification - Network Operator` were archived 2026-05-13 (Phase 1.6); track A vs B distinction now lives in the `network_op_track` field (values: `external_extension` for Track A, `internal_external_unification` for Track B). Do NOT write these as sub-segment values.

## Apollo budget

Sub-cap for this task: **50 credits/run** (second highest after NeoCloud — GitHub commits + procurement portals drive volume). At Stage 0, read `weekly-reports/apollo-budget.json`; effective budget = `min(50, available_in_weekly_pool)`.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_fetch, web_search. Abort + DM Cooper if any required MCP is unavailable.
2. **Read canvas `F0B0AFSB9LN`** for Tier 3 carryovers tagged with this segment.
3. **Read Apollo budget tracker**. `effective_apollo = min(50, weekly_remaining)`.
4. **Build target list** (all tiers, non-Flagged) via `search_crm_objects` with the scope filter above. Cap at 1000 records. NOTE (2026-06-04): removing the tier filter materially enlarges this pool (all-tier vs the prior Tier 1-3); rely on the Stage 1 context-budget safeguard (sub-agent fan-out + batched writes + overflow backlog) to stay within budget.
5. **Check prior Monday's segment-run-report** at `weekly-reports/[YYYY-MM-DD minus 7 days]/signal-scan/networkop/`. If absent, tag everything `NEW`.

---

## Stage 1 — Signal Detection (Network Op sources only, 180-day window)

**Context-budget safeguard (2026-06-04).** The 180-day window + all-tier scope roughly doubles the candidate set, which risks the context-wall that forced the 2026-05-28 per-segment split. To stay within budget: (a) fan out source detection through research sub-agents so raw source text does not all live in the main context; (b) stream the matched-account list and write in batches of 10 rather than holding every candidate resident; (c) if scored candidates exceed 60 in a single run, write what you can this run and persist the remainder to `weekly-reports/[today CT]/signal-scan/networkop/backlog.md` - the NEXT run reads and processes that backlog FIRST (a real carry that always writes, not a discard). Out-of-window deferral no longer exists; the only carry is this budget-overflow backlog.

### Per-segment signal codes (NO- prefix for Network Operator disambiguation from NC- NeoCloud)

| Code | Signal | Tier | Freshness | Confidence baseline |
|---|---|---|---|---|
| **NO-A1** | Private-Connectivity-Fabric Copycat / Multi-Billion AI Deal Announcement | A | 1wk | HIGH |
| **NO-A2** | Earnings Transcript Mentions — NaaS / Network APIs / Private Fabric / Programmable | A | 30d | HIGH |
| **NO-A3** | Exec Transition — CTO / CNO / VP Automation / Chief Network Strategy | A | 30d post-hire | HIGH |
| **NO-A4** | Wholesale / Consumer Divestiture or Spin-off — Announcement OR Close (two-event firing) | A | ≤60d | HIGH |
| **NO-A5** | GitHub Commits from `@carrier.com` to CAMARA / Nephio / ONAP / OpenConfig / Sylva | A | 30d | HIGH |
| **NO-A6** | TM Forum Autonomous Networks Self-Assessment Publication | A | 90d | HIGH |
| **NO-A7** | SRv6 / Segment-Routing Production Rollout Announcement | A | 90d | HIGH |
| **NO-A8** | Public RFI / RFP — Multi-Domain Orchestrator / TE Controller / Inter-Carrier Automation | A | 30d | HIGH |
| **NO-A9** | PCEP / SR-TE / BGP-LS / YANG-NETCONF Job Requisitions (sub-10-employee TE team starting up) | A | 30d | HIGH |
| **NO-A10** | CTrO / CDO Appointment (distinct from CTO/CNO) — platformization mandate | A | 90d | MED-HIGH |
| **NO-B1** | Tier 1 Supplier Customer Win (Ciena / Nokia / Cisco / Juniper / Infinera) | B | 90d | HIGH |
| **NO-B2** | GSMA Open Gateway / Network API Commercial Launch in New Market | B | 90d | MED-HIGH |
| **NO-B3** | TM Forum Autonomous Network Level 3 / Level 4 Certification | B | 90d | HIGH |
| **NO-B4** | Submarine Cable Landing / Consortium Joining | B | 90d | MED |
| **NO-B5** | MEF (Mplify) LSO Sonata / Open API Certification | B | 90d | MED |
| **NO-C1** | Private 5G + Network Slicing Enterprise Win | C | 90d | MED |
| **NO-C2** | Sovereign Cloud / Edge Federation Partnership (Euro Edge Continuum / EURO-3C) | C | 90d | MED-HIGH for EU carriers |
| **NO-C3** | Activist Investor / PE Position Disclosure (13D/13G + strategic review) | C | 60d | HIGH when it hits |
| **NO-C4** | Hyperscaler Carrier Deal (bypass signal — losers call fastest) | C | 90d | HIGH |
| **NO-C5** | Carrier Layoff / Restructuring (nuanced — classify reason) | C | 60d | MED (reason-dependent) |

Plus the **Universal signal types** (U1-U6) and **Apollo signal classes** (AP-1, AP-2, AP-3, AP-4 paired, AP-7, FR-1 — AP-5/AP-6 disabled).

### Source Registry (Network Op — execute every source, record ✓/✗ in audit)

Per [`context/signals/network-operator-signals.md`](../../context/signals/network-operator-signals.md) §"Sources for This Segment".

**Robust tier (single-source can score HIGH on non-major signals):**
1. Company IR pages — direct newsroom diffs at target Tier 1/2 carriers (Lumen, AT&T, Verizon, T-Mobile, Charter, Cox, Comcast Business, BT, Vodafone, DT, Orange, Telefónica, NTT, Tata Comms, Singtel, Telstra) — highest single-source yield
2. StockTitan — SEC 8-K mirror; covers 8-K Items 1.01 / 2.01 / 5.02 + 13D/G activist + 10-Q earnings; international: 20-F annual filings
3. SEC EDGAR full-text via search-anchor — backup to StockTitan
4. Earnings transcripts — Seeking Alpha (free-tier headlines) + Motley Fool + MarketBeat + 10-Q transcripts via StockTitan; keyword filter for `"NaaS"`, `"API"`, `"private fabric"`, `"programmable network"`, `"SRv6"`, `"autonomous network"`, `"MEF"`, `"TM Forum"` (NO-A2)
5. Fierce Network + Light Reading + TelecomTV + RCR Wireless + Total Telecom — primary US trade press
6. Ciena / Nokia / Cisco / Juniper / Arista / Infinera newsrooms — supplier customer-win press
7. MEF / Mplify (rebrand) newsroom + TM Forum newsroom + Catalyst announcements
8. GSMA newsroom + CAMARA project GitHub + GSMA Open Gateway press
9. GlobeNewswire + PR Newswire + Business Wire filtered to carrier list + Appointments tag
10. Apollo MCP — `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events (AP-1, AP-2, AP-7)
11. GitHub commit feeds for CAMARA / Nephio / ONAP / OpenConfig / Sylva — corporate-domain authors only (NO-A5; accessed via search anchor)
12. FedBizOpps + SAM.gov + state procurement portals — federal RFI/RFP for multi-domain orchestration / TE controllers / inter-carrier automation (NO-A8; federal = Robust, state = Aspirational)
13. Greenhouse + Lever + Ashby public job boards at target carriers (NO-A9 PCEP / SR-TE / BGP-LS / YANG reqs)

**Medium tier (Tier B fallback):**
14. Capacity Media — international fallback (content depth weaker than peer US trade press)
15. Mobile World Live + Mobile Network UK — carrier-economic news
16. TIA + USTelecom + CTIA press
17. ONUG (Open Networking User Group) announcements
18. ONF (Open Networking Foundation) press
19. LFN (Linux Foundation Networking) member commits + leadership announcements
20. ETSI standards activity — NFV / MEC / MANO / Open RAN WG output (leading indicator)
21. 3GPP work item tracker — carrier roadmap commitments
22. IETF working groups — carrier-participation WGs (PCE, IDR, BESS, SR, OPSAWG)

**International supplement (Tim Z territory — elevated priority for this segment; global Tier 1/2 carriers are Tim Z's heaviest book):**
- **Global/EMEA:** Capacity Media (PRIMARY for international), TelecomTV (PRIMARY), Light Reading Europe, Total Telecom, ETNO press. Target operators: Orange Business, BT Global, Colt, DT International, KPN International, TIM Sparkle, Telia Carrier, Arelion, Liberty Global, Telefónica Tech.
- **APAC:** Capacity Asia, TelecomAsia.net. Targets: NTT, Tata Comms, PCCW Global, Telstra, Singtel, Axiata, Epsilon, Console Connect.
- **LATAM:** BNamericas, Capacity LATAM. Targets: Cirion, Telxius.
- **MENA:** Capacity MENA, Commsmea. Targets: e& Carrier Wholesale, Etisalat International.
- **Subsea (global):** TeleGeography Submarine Cable Map RFS feed (PRIMARY for Subsea cable operator sub-segment), SubmarineNetworks.com.
- **I-series:** I2 Sovereign AI Compute Grants hit Network Op targets frequently (carriers winning government sovereign-network contracts; +3 score bonus).

**Quarterly batch:** Earnings transcript sweep across full Tier 1/2 target list — highest-yield recurring task.

**Source Coverage Mandate:** every documented source above MUST be attempted via search-anchor and recorded ✓ / ✗. Generic queries that don't anchor on a documented source do NOT count.

### False-positive patterns — DOWNGRADE or EXCLUDE at detection time

| Pattern | Action |
|---|---|
| GitHub commits from `@gmail.com` / personal email matching carrier employee | DOWNGRADE to MEDIUM (corporate-domain = HIGH only) |
| "Liquid cooling" mentioned in marketing blog with no facility named | EXCLUDE |
| Layoff press citing "cost-cutting" / declining 5G capex without automation language (NO-C5) | DOWNGRADE / defer 60d |
| State procurement portal listing without federal/major-trade-press confirmation | DOWNGRADE to MEDIUM (state portals = Aspirational tier) |
| Earnings transcript mention of NaaS without operational confirmation (no product, no portal) | DOWNGRADE to MEDIUM |
| Subsea cable filing from pure consortium / SPV without operating entity | DOWNGRADE; check if operator routes to `Subsea cable operator` sub-segment |
| Conference speaking slot alone | EXCLUDE per noise list |
| AP-6 Apollo Intent without pairing | EXCLUDE |

---

## Stage 2 — Match detected signals to target accounts

For each detected signal candidate:
1. Exact company name match (case-insensitive, with/without legal suffix)
2. Domain apex match + subdomain variants
3. LinkedIn slug match
4. GitHub author-email `@carrier-domain` match (NO-A5)
5. SEC CIK lookup (for 13D/G + 10-Q + 8-K signals)

Surviving → `matched_accounts[]`. Unmatched → `new_account_candidates[]` (route to Stage 3 if Apollo allows).

---

## Stage 3 — NEW-account creation (Apollo-bound, max 50 credits)

For each `new_account_candidate`:

1. **D1 disqualifier check** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D1.
2. **Stage 1a–1c research-first workflow** per [`skills/company-enrichment/SKILL.md`](../../skills/company-enrichment/SKILL.md).
3. **Apollo enrichment**. Decrement budget.
4. **Segment routing per D3 flowchart** — must route to `customer_segment = "Network Operator(Tier 1 / VNO)"` to remain in scope. **Subsea cable operators** that pass D1 + are pure-play subsea (not consortium SPV) route to `Subsea cable operator` sub-segment (the 30th sub-segment).
5. **D5 sub-segment protocol** per [`context/account-tiering/enrichment-protocols.md`](../../context/account-tiering/enrichment-protocols.md) §6. Subsea operator anchor list: Aqua Comms (now EXA-owned — verify operating status), Seaborn Networks, Hawaiki Submarine Cable / BW Digital. D1-evicted: pure consortiums (FLAG, SEA-ME-WE, ACE, EIG), cable vendors (ASN, HMN Tech, NEC OCC, SubCom), pure-financing hyperscaler SPVs.
6. **Determine `network_op_track`** (Track A external_extension vs Track B internal_external_unification) per the field's value map. Write alongside sub-segment.
7. **Compute tier** per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). Default `signal_heat = Cold` on new accounts.
8. **Write to HubSpot**. Bump `last_enriched_date = today (CT)` — full enrichment pass.

If Apollo exhausts mid-Stage 3, finish current then halt. Remaining surface in audit.

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
  +6 if NO-A4 announcement AND close both fire within 18mo (two-event firing)
  +3 if I2 Sovereign AI Compute Grant on a carrier target

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

1. **Source URL verification** — cited URL real, reachable, content matches claim.
2. **Freshness** — event date within 180 days rolling window. Drop only if older than 180 days (it would compute to `Cold`).
3. **Segment classification** — `customer_segment = "Network Operator(Tier 1 / VNO)"` post-Stage 3.
4. **Field overflow** — narrative ≤250 chars.
5. **Owner mapping** — `hubspot_owner_id` maps to East / West / International.
6. **Rep-facing copy scan** — pure prose, no date prefix, no `[Routine N]` tag, no em dashes, no competitor names.
7. **Score arithmetic** — math + bonuses correct.
8. **Dedup** — no double-counting same signal from 2 sources.
9. **NEW/CARRIED integrity** — CARRIED requires prior segment-run-report confirmation.
10. **Pure-prose narrative** — Stage 5 writes pure prose, no prefix.

Any rule failure → fix or drop. Log drops in audit.

---

## Stage 5 — HubSpot narrative write (pure prose, NO date prefix)

For each scored hit ≥8, write `recent_news_or_trigger_event` via `manage_crm_objects` (batches of 10, 250ms between, exponential backoff on 429).

- **Format:** pure-prose 1-sentence narrative, ≤250 chars. Examples: `"CTO Transition — Carrier appointed Dr. Lisa Chen Chief Network Officer (ex-Nokia); 90-day mandate window for programmable-fabric strategy"` or `"GitHub Commit Signal — 12 commits to Nephio from @colt.net authors this quarter; engineering investment in federated infrastructure"`.
- **NO leading `[YYYY-MM-DD]` prefix.** Date lives in `last_signal_date`.
- **NO `[Routine 2]` / `[Signal Scan]` / `[Network Op]` tag.** Routine identity is recoverable from `last_enriched_date` + on-disk audit.
- **NO em dashes** (use hyphens or restructure).
- **NO competitor names** (use "third-party fabrics" instead).

**Do NOT bump `last_enriched_date`** (partial signal write). Exception: Stage 3 NEW-account creates DO bump.

---

## Stage 5b — Structured signal fields + tier/heat recompute

**Anti-churn write rule (required under the 180-day window):** write the signal fields only if the detected event date is newer than the record's current `last_signal_date`, OR the record has no `last_signal_date`, OR the new score exceeds the stored `last_signal_score`. If the freshest detected signal is not newer or higher than what is already stored, skip the write (idempotent no-op). Never overwrite a newer stored signal with an older detection. This keeps the wide window from re-writing the same aging signal every Monday.

For each scored hit that passes the anti-churn rule, write via the same `manage_crm_objects` batch:

- **`last_signal_date`** = event date from source article (NOT today's date).
- **`last_signal_score`** = computed score from Stage 4.
- **`signal_count_last_30d`** = recompute.
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
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/networkop/segment-run-report.md
```

Content:
1. Run header (date, segment, Apollo consumed X of 50, runtime, MCPs).
2. Source coverage table (every documented source above, ✓ / ✗; track 3-week ✗ streak).
3. Candidate funnel (target list size, candidates, matches, NEW accounts, total writes, drops).
4. Score distribution (8-11, 12-17, 18-26, 27+).
5. Writes summary per record (id, name, NO- signal code, score, heat delta, tier delta).
6. Tier 3 holds (carryover records still Tier 3; re-append to canvas).
7. QA gate drops with reasons.
8. Failed writes.
9. Apollo budget post-run.
10. International signal flags (I2 Sovereign AI Compute Grants surfaced).

End the run. **No rep DMs, no canvas Run log, no Cooper run report.** Aggregator at 2:30pm CT handles all three.

---

## Failure handling

- **HubSpot MCP errors:** retry (250ms → 1s → 4s, max 3). Log to "Failed writes".
- **web_fetch / web_search errors:** log source as ✗. 3-week streak auto-flags.
- **Apollo MCP errors mid-Stage-3:** halt Stage 3, continue Stage 4.
- **GitHub commit search errors (NO-A5):** log as ✗, drop NO-A5 detection for this run.
- **Canvas read failure:** proceed without carryover, log warning.
- **Git contention on Apollo budget tracker:** log + continue; JSON updated locally.

## End-of-run footer

```
[Network Op] target=N matched=N new=N writes=N heat_promotions=N apollo=N/50 runtime=Nmin audit=weekly-reports/YYYY-MM-DD/signal-scan/networkop/
```

No Slack DM from this task. The aggregator owns rep + Cooper communication.
