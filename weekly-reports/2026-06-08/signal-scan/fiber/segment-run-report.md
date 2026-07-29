# Signal Scan — Fiber Operator — Segment Run Report

**Date:** 2026-06-08 (Monday, CT)
**Segment:** Fiber Operator
**Detection window:** 2025-12-10 → 2026-06-08 (180 days rolling, event-date semantics)
**Outcome:** CATCH-UP week — **20 HubSpot signal writes** (first Fiber run under the 180-day window; prior runs used the 14-day gate and dropped a backlog of material M&A / financing / expansion events now in scope)
**Apollo consumed:** 0 of 35 (weekly W24 pool: 0/850 before, 0/850 after — W23 closed 0/850, rollover pending other routines)
**Runtime:** ~30 min
**MCPs used:** HubSpot (read + write), Slack (canvas read — oversized, see §1), web_search / web_fetch (via 4 detection sub-agents); Apollo not invoked

---

## 1. Run header

| Item | Value |
|---|---|
| Target pool (Fiber Operator, all tiers, type != Customer; MaiaEdge own + Flagged excluded by segment filter) | 1,270 records |
| Canvas F0B0AFSB9LN read | Returned oversized (851K chars) — not fully parsed. Carryover determination based on prior 2026-06-01 report (no signal-scan-owned Fiber Tier 3 items) + last week's zero new holds. No Fiber Tier 3 carryover to drain. |
| Apollo budget tracker | Read OK — file header still W23 (consumed 0/850); today is ISO W24. effective_apollo = min(35, 850) = 35. 0 consumed this run, so no tracker write (consistent with prior 0-consumption pattern). |
| Prior-Monday report (2026-06-01) | Present. Used for source-coverage delta + to recover its out-of-window backlog (now in the 180-day window). |
| Detection method | 4 parallel research sub-agents (M&A/financing; BEAD/expansion; AI-DC dark fiber/optical/subsea; exec hires/NaaS/earnings) to keep raw source text out of main context per the 2026-06-04 context-budget safeguard. |

## 2. Source coverage (search-anchor pattern)

| # | Source / topic anchor | Status |
|---|---|---|
| 1 | Fierce Network / Fierce Telecom (M&A tracker, People column) | ✓ |
| 2 | Light Reading (M&A Watch, People moves, optical) | ✓ |
| 3 | Lightwave Online (400G/800G, IRU, AI-DC fiber) | ✓ |
| 4 | Telecompetitor (regional operators, BEAD) | ✓ |
| 5 | Broadband Communities / bbcmag | ✓ |
| 6 | StockTitan SEC 8-K mirror (LUMN, UNIT; no in-window FYBR/CCOI/ATUS) | ✓ |
| 7 | SEC EDGAR full-text | ✓ |
| 8 | NTIA BEAD Progress Dashboard | ✓ |
| 9 | State broadband offices (TX, NY, PA, AL, MA, WA, AZ/Navajo) | ✓ |
| 10 | Greenhouse / Lever / Ashby job boards at operators | ✗ (no in-window qualifying hit; exec hires found via trade press instead) |
| 11 | Apollo MCP (job changes / funding) | n/a (not invoked — budget reserved for Stage 3, which was deferred) |
| 12 | USTelecom / NTCA / Fiber Broadband Association / INCOMPAS | ✓ FBA; ✗ USTelecom/NTCA (only sub-$5M co-op aggregates) |
| 13 | PR Newswire / Business Wire / GlobeNewswire | ✓ |
| 14 | DataCenterKnowledge | ✓ |
| 15 | BroadbandBreakfast | ✓ |
| 16 | ABS market data (KBRA / Fitch / Moody's via Asset Securitization Report) | ✓ |
| 17 | SubmarineNetworks.com / TeleGeography | ✓ Submarine; ✗ TeleGeography (covered via SubmarineNetworks) |
| 18 | Earnings (Seeking Alpha / Motley Fool / MarketBeat) | ✓ |
| 19 | International (Light Reading Europe, Total Telecom, Capacity, BNamericas, Telecompaper, UK Project Gigabit/ISPreview) | ✓ |

**3-week ✗ streaks:** none confirmed. Job boards (Greenhouse/Lever/Ashby) and USTelecom/NTCA were ✗ this run but were not tracked as ✗ in the prior per-segment baseline; not yet a streak. Source Coverage Mandate satisfied for robust + priority-medium tiers.

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target list size (Fiber, all tiers) | 1,270 |
| Detected candidates (raw, in-window ≥ 2025-12-10) | ~40 distinct fiber-operator events |
| Matched to target pool (existing Fiber records) | 33 companies |
| NEW accounts created | 0 (deferred — see §6) |
| **Total HubSpot writes** | **20** |
| Anti-churn / dedup no-ops (already recorded) | 13 |
| Dropped — out of segment (other scan owns) | 8 |
| Dropped — below score floor (<8) | 4 |

## 4. Score distribution (writes)

| Bucket | Count | Companies |
|---|---|---|
| 27+ (Highest) | 8 | Uniti 33, Omni Fiber 33, Lyte Fiber 33, Great Plains 27, Aureon 27, Dakota Carrier Network 27, TDS Telecom 27, Nexstream 27 |
| 18-26 (Strong) | 3 | Lightpath 18, Vero Fiber Networks 18, Lumos Fiber 18 |
| 12-17 (Worth Reviewing) | 2 | MetroNet 12, Ripple Fiber 12 |
| 8-11 (LIGHT) | 7 | Bluebird 9, Pilot 9, Frontier 9, Point Broadband 9, WOW! 9, Celeste 9, FiberLight 9 |

## 5. Writes summary (20)

| ID | Company | Signal | Score | last_signal_date | Heat Δ | Tier Δ |
|---|---|---|---:|---|---|---|
| 193906530037 | Uniti | F-A8 2nd Kinetic ABS ~$1.14B (+stack) | 33 | 2026-06-01 | Hot→Hot | tier_1 (frozen, target acct) |
| 292755851981 | Omni Fiber | F-A7 Citizens Fiber acquisition (+stack) | 33 | 2026-06-01 | Cool→Hot | tier_3→tier_1 |
| 193856074473 | Great Plains Communications | F-A7 Fastwyre NE fiber acquisition | 27 | 2026-05-19 | Cold→Warm | tier_2 (frozen) |
| 323823198919 | Lightpath | F-B2 Columbus-Chicago + NYC-metro build (+stack) | 18 | 2026-05-19 | Cold→Hot | tier_2 (frozen) |
| 193855354612 | Aureon | F-A3 100Tbps Ellendale-Chicago AI route | 27 | 2026-05-19 | Cold→Warm | tier_3→tier_2 |
| 208908440283 | Dakota Carrier Network | F-A9/F-A3 Heartland Fiber Project ($700M backbone) | 27 | 2026-05-15 | Cold→Warm | tier_2 (frozen) |
| 209170400954 | TDS Telecom | F-A7 Granite State Communications acquisition | 27 | 2026-04-23 | Cool→Warm | tier_4→tier_2 |
| 324007013094 | MetroNet | F-A8 ~$903M fiber-network securitization | 12 | 2026-03-12 | Cold→Cool | tier_2 (frozen) |
| 292719725284 | Ripple Fiber | F-B2 Arizona $80M new-market entry | 12 | 2026-05-12 | Cool→Cool | tier_3 (no change) |
| 323821758151 | Bluebird Network | F-A7 Everstream $384.6M asset purchase | 9 | 2026-03-06 | Cold→Cool | tier_3 (frozen) |
| 320875891448 | Pilot | F-A7 ExteNet enterprise-fiber acquisition | 9 | 2026-02-05 | Cool→Cool | tier_3 (no change) |
| 323221077752 | Vero Fiber Networks | F-A8 $425M credit-facility expansion | 18 | 2026-04-06 | Cold→Cool | tier_3 (no change) |
| 193866158814 | FiberLight | F-A3 $350M West Texas 1,400-mi AI dark fiber | 9 | 2026-02-26 | Cold→Cool | tier_2 (frozen) |
| 175225132733 | Frontier | F-A7 $20B Verizon acquisition closed | 9 | 2026-01-20 | Cold→Cool | tier_2 (frozen) |
| 324060022515 | Lumos Fiber | F-A5 CEO hire (Scott Mispagel, ex-Frontier) | 18 | 2026-05-19 | Cold→Cool | tier_2 (frozen) |
| 266871288512 | Point Broadband | F-A7 Clearwave Fiber combination (12 states) | 9 | 2026-01-05 | Cold→Cool | tier_2 (frozen) |
| 322038348534 | WOW! (WideOpenWest) | F-A2 $1.5B DigitalBridge/Crestview take-private | 9 | 2026-01-01 | Cold→Cool | tier_2 (frozen) |
| 326325669589 | Celeste | F-A2 CVC DIF ~88% stake (France) | 9 | 2026-01-14 | Cold→Cool | tier_3 (no change) |
| 292748543699 | Lyte Fiber | F-A1 Texas BEAD ~$116M finalized (+stack) | 33 | 2026-06-03 | Hot→Hot | tier_2→tier_1 |
| 322364279512 | Nexstream | F-A1 Texas BEAD ~$401M finalized | 27 | 2026-06-03 | Cool→Warm | tier_3→tier_2 |

Tier promotions written (non-target records): Omni Fiber tier_3→tier_1 (hot+stacked), Aureon tier_3→tier_2 (hot), TDS Telecom tier_4→tier_2 (hot), Lyte Fiber tier_2→tier_1 (hot+stacked), Nexstream tier_3→tier_2 (hot). Open-deal modifier was not evaluated (no per-record association lookups this run); all writes are promotions or no-change, so no risk of regressing a deal-driven tier — R-Tier-Audit (daily) reconciles open-deal modifiers.

## 6. Anti-churn no-ops, out-of-segment drops, sub-floor drops, NEW candidates

### Anti-churn / dedup no-ops (already carry a newer or equal signal — no write)
| Company | Stored | Detected (older/equal) |
|---|---|---|
| Zayo (193910127352) | 2026-05-21 / 29 / Hot | Crown Castle close 05-01, $2.37B ABS 04-24 |
| GCI (175217873639) | 2026-04-22 / 30 / Warm | Quintillion 04-21 (same event) |
| Astound (324060022514) | 2026-03-15 / 18 / Cool | GFiber merger 03-12 (same event); CEO hire 03-17 scored <8 |
| Truvista Fiber (320874452690) | 2026-04-21 / 14 / Cool | City of Commerce GA 04-21 (same event) |
| Consolidated Communications (314374535919) | 2026-05-21 / 27 / Hot | Fidium ABS 02-26 (<8, older) |
| Lumen Technologies (107187281647, lumen.com=Fiber) | 2026-05-21 / 27 / Hot | NorthLine 05-12, Level3 refi 05-13, tender 05-19, Alkira 05-05 (all ≤ stored date) |
| Cirion Technologies (133506047726) | 2026-05-20 / 27 / Warm | NaaS launch 05-19 (same event) |
| Light Source Communications (251535204086) | 2026-05-21 / 27 / Warm | 500-mi 02-23, 400-mi 04-14 (older) |
| Greenlight Networks (268073696970) | 2026-04-28 / 14 / Hot | T-Mobile JV 04-28 (same event); NE PA build 03-12 (older) |
| GoNetspeed (323822481122) | 2026-04-28 / 15 / Cool | T-Mobile JV 04-28 (same event) |
| i3 Broadband (321479152324) | 2026-04-28 / 14 / Cool | T-Mobile JV 04-28 (same event) |
| Clearwave Fiber (291537915620) | 2026-05-15 / 0 / Cool | Point/Clearwave combine 01-05 (older — would regress date) |
| BIG Fiber (320875891447) | 2026-05-19 / 30 / Warm | $250M Stonepeak/La Caisse 05-19 (same event) |

### Dropped — out of segment (route to the named scan, not Fiber)
- Lumen Technologies / CenturyLink (296880096970, customer_segment = Other) — Network Op / Other scan.
- Verizon (192899501812, Network Operator) — Frontier-close signal written on Frontier (in-scope); Verizon itself out of scope.
- Vocus (251600877280, Network Operator) — CTO hire (Nikos Katinakis) belongs to Network Op scan.
- Spectrotel / AireSpring merger — MSP/Aggregator scan.
- IT&E / CNMI BEAD ($31.3M) — Network Op scan (integrated territory carrier).
- EXA Infrastructure / Aqua Comms close — Network Op `Subsea cable operator`.
- WIN Technology (Heartland partner) — MSP/Aggregator scan.
- Alkira (Lumen acquisition target) — not a fiber operator.

### Dropped — below score floor (<8)
- Fidium / Consolidated ABS 2026-1 (F-A8, 02-26, MED) → 6.
- Ezee Fiber / DayNet acquisition (F-A7, 02-10, MED) → 6.
- Altibox Carrier CTO hire (F-A5, 01-05, MED) → 6.
- Astound CEO hire (F-A5, 03-17, LOW) → 6.

### NEW-account candidates (NOT created this run — documented for account-sourcing / next run)
NEW-account creation was deferred this run: the matched-record refresh (20 writes) was the high-value, low-risk core, and unattended full enrichment of net-new records is the highest-risk action without Cooper oversight (per the "default to NOT writing when unsure" principle). Apollo budget untouched (35 available). Candidates, all clear fiber operators with in-window signals not currently in the Fiber pool:
- **Nexstream is IN CRM** (wrote). **Lyte Fiber IN CRM** (wrote). **Light Source Communications IN CRM** (anti-churn).
- 360 Broadband — Texas BEAD finalized subgrant (~$16M, F-A1, 2026-06-03). Verify not already in CRM under another name.
- Mereo Fiber — national fiber platform, two acquisitions (F-A7, 2026-03-16, score ~12).
- Dark Fiber Group (DTCP, Nordic) — new AI dark-fiber operator launch (F-A6, 2026-03-24, score ~18). International (Tim Z).
- Netomnia / Substantial Group (UK) — £2B nexfibre JV acquisition (F-A7, 2026-02-18, score 9). International (Tim Z).
- CityFibre (UK) — Project Gigabit redesign £25.2M (F-A1/F-B2, 2026-05).
- Dragonfly Internet (FL) — Myakka acquisition (F-A7, 2025-12-24, score 9).
- "Range" (Heartland Fiber Project partner) — UNVERIFIED whether = Range Telephone Cooperative (154278570716, MT) or a different entity; not attributed this run to avoid mis-write. DCN carries the Heartland signal.

## 7. Tier 3 holds

None taken this run. No signal-scan-owned Fiber Tier 3 carryovers were present (per prior report + last week's zero new holds), and none created this run. No canvas F0B0AFSB9LN re-append required.

## 8. QA gate drops

None from the final write list — all 20 writes passed the 10-rule gate (source-URL verification via sub-agent article follows, freshness ≤180d, segment = Fiber Operator confirmed, narrative ≤250 char pure prose with no date/tag prefix and no em dashes/competitor names, score arithmetic, dedup one-narrative-per-account, owner mapping present, NEW/CARRIED integrity). Sub-floor and out-of-segment items were dropped at detection/match (see §6), not at the QA gate.

## 9. Failed writes & Apollo budget

- **Failed writes:** none. Batch 1 = 10/10, Batch 2 = 10/10 (totalProcessed 20, updated 20, failed 0).
- **Apollo budget post-run:** 0 credits consumed (Stage 3 deferred). Weekly W24: 0/850. No tracker write (0 consumption; W23→W24 header rollover left to the next Apollo-consuming routine).
- **last_enriched_date:** not bumped on any record (all partial signal writes per the Unified Stamping Policy; no NEW creates).

---

**Handoff:** Aggregator (`signal-scan-aggregator`, 2:30pm CT) will read HubSpot for `last_signal_date = today` Fiber records. Note: most of this run's writes carry **historical** event dates (the 180-day backlog), so only the two 2026-06-03 BEAD writes (Lyte Fiber, Nexstream) and any other true-today events will surface under a `last_signal_date = 2026-06-08` filter — the aggregator should key off this report for the full 20-write set, not a today-only date filter. No rep DM, canvas update, or Cooper report sent by this task.
