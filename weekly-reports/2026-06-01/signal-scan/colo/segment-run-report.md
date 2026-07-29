# Signal Scan — Data Center Colo Provider — Segment Run Report

## 1. Run Header
- **Date (CT):** 2026-06-01 (Monday)
- **Segment:** Data Center Colo Provider
- **Detection window:** 2026-05-18 → 2026-06-01 (14 days rolling, event-date basis)
- **Apollo consumed:** 0 of 35
- **Runtime:** ~1 run (detection fan-out via research subagent + supplementary direct searches)
- **MCPs used:** HubSpot (search), Slack (canvas read), web_search; Apollo not invoked (no NEW-account creation)
- **Outcome:** QUIET — 0 in-window signals cleared the score floor of 8 → **0 HubSpot writes, 0 NEW accounts.**
- **NEW/CARRIED tagging:** ALL NEW. No prior per-segment colo report exists (per-segment split was 2026-05-28; last Monday 2026-05-25 ran the monolithic scan). No source-coverage delta available this week.

## 2. Source Coverage Table
Search-anchor attempts against the documented Colo Source Registry. ✓ = reachable / returned results (even if 0 actionable); ✗ = errored / unreachable / nothing returned.

| # | Source | Status | In-window actionable hits |
|---|---|---|---|
| 1 | Data Center Frontier | ✓ | 0 (index/land-and-expand articles only; none with confirmed 5/18–6/1 event date) |
| 2 | Data Center Dynamics | ✓ | 1 (Digital Realty BCN1 Barcelona — below floor; also surfaced out-of-window Equinix KL2, I Squared/Elea, Hut 8 Beacon Point) |
| 3 | Data Center Knowledge | ✓ | 0 (May-2026 developments + Q2 appointments roundups; individual items undated or out of window) |
| 4 | Bisnow Data Center | ✓ | 0 (DataBank $665M securitization = capital-markets, not operational; excluded) |
| 5 | PR Newswire / Business Wire / GlobeNewswire | ✓ | 1 (Digital Realty BCN1 via GlobeNewswire 5/18 — below floor; WhiteFiber/Nscale = Dec-2025 deal, May-30 billing milestone only) |
| 6 | StockTitan (8-K mirror: DLR/EQIX/IRM/DBRG/COR) | ✓ | 0 net-new (DLR Barcelona mirror = dup of #5; IRM Q1 8-K 4/30 out of window) |
| 7 | SEC EDGAR full-text | ✓ | 0 (Digi Power X 8-K 5/5, Iron Mountain Q1 8-K 4/30 — both out of window) |
| 8 | Greenhouse / Lever / Ashby job boards | ✗ | 0 (no confirmable in-window exec hire or 3+ net-eng req surge at a named colo operator) |
| 9 | AWS / Azure / Google Cloud region feeds | ✗ | 0 (no in-window region launch with colo anchor angle) |
| 10 | NVIDIA Newsroom / GTC | ✗ | 0 (DGX Cloud Lepton named neoclouds, not a colo facility signing; GTC was March) |
| 11 | Crunchbase News (Data Center tag) | ✗ | 0 (no in-window colo funding/M&A distinct from wire-covered deals) |
| 12 | Conference agendas (PTC/Capacity/ITW/Datacloud/AI Infra Summit) | ✓ | 0 (context only; no standalone signal — per noise list) |
| 13 | Capacity Media / Data Centre Review / BNamericas (international) | ✓ | 0 (I Squared/Elea LATAM dated late April, out of window) |

**3-week ✗ streak watch:** First per-segment colo run, so no streak history yet. Sources 8–11 returned no in-window hits this week — establish baseline; re-check next Monday before flagging "Sources Needing Development."

## 3. Candidate Funnel
| Stage | Count |
|---|---|
| Target list size (Colo, tier 1–3, type≠Customer, excl. MaiaEdge own) | 460 (459 after excluding HDCO Group, type=Customer) |
| Tier 3 canvas carryovers added | 0 (no prior colo signal-scan holds on F0B0AFSB9LN) |
| Detected raw candidates (any date) | 6 (Digital Realty BCN1; + out-of-window: Digi Power X/Cerebras, Bitzero/OneQode, Equinix KL2, Hut 8 Beacon Point; + milestone-only: WhiteFiber/Nscale) |
| In-window candidates (event 5/18–6/1) | 1 (Digital Realty BCN1) |
| Matched to existing account | 1 (Digital Realty, id 193856795322) |
| NEW account candidates | 0 |
| NEW accounts created | 0 |
| Total HubSpot writes | 0 |
| Dropped — below score floor | 1 (Digital Realty, score 4 < 8) |
| Dropped — out of window | 4 |
| Dropped — milestone of old deal (not fresh event) | 1 (WhiteFiber/Nscale) |

## 4. Score Distribution
| Bucket | Count |
|---|---|
| 27+ (Highest) | 0 |
| 18–26 (Strong) | 0 |
| 12–17 (Worth Reviewing) | 0 |
| 8–11 (LIGHT) | 0 |
| <8 (silent drop, log only) | 1 (Digital Realty BCN1 = 4) |

## 5. Writes Summary
**None.** 0 records written to HubSpot this run.

Below-floor detail (logged, not written):
- **Digital Realty** (id 193856795322, AI Signals - colo, tier_1, hs_is_target_account=true, current heat=Warm, owner Tim Lieto/East). Signal: opened BCN1, its first Barcelona data center (14MW, Sant Adrià de Besòs), entering the Mediterranean Spain interconnection market. Event date 2026-05-18 (GlobeNewswire/StockTitan, HIGH confidence). Closest colo code: **C-C2** (carrier-neutral / meet-me-room expansion, Tier C, MED). Score = Tier(1) × Freshness(2, ≤30d) × Confidence(2, MED) = **4 < floor 8 → silent drop.** No Tier A/B code applies: an established ~300-facility REIT entering one new metro is not a C-A1 (1→2 site transition) or C-A0 (greenfield) trigger. Writing it would also have downgraded the account's existing Warm heat to Cool on a score-12-or-lower input — additional reason the below-floor drop is correct.

## 6. Tier 3 Holds
None. No canvas carryovers came in; none created. Nothing to re-append to canvas F0B0AFSB9LN.

## 7. QA Gate Drops
No signals reached the Stage 4.5 QA gate as write candidates (the single in-window signal was dropped earlier at Stage 4 scoring for being below the floor). 0 QA-gate drops.

## 8. Failed Writes
None (no write attempts).

## 9. Apollo Budget Post-Run
- Credits consumed this run: **0** (no NEW-account creation; no firmographic enrichment needed).
- Sub-cap: 35/run. Used 0 of 35.
- Weekly W22 (2026-W22): 0/850 before run → 0/850 after run. 850 remaining.

---

## Carryover candidates for next Monday's window (out-of-window this week)
These are confirmed material colo signals whose event dates fell 5/5–5/12, just before this window's left edge (5/18). They will be inside the window for the 2026-06-08 run if not yet captured. Surfaced here for the aggregator/Cooper context only — NOT written this run.

| Company | Signal | Event date | Note |
|---|---|---|---|
| Digi Power X (DGXX) / Cerebras | C-A6 anchor signing | 2026-05-05 | 40MW AI colo, Columbiana AL; 10-yr MSA ~$1.1B. domain digipowerx.com. Not in colo pool → would be a NEW-account candidate. |
| Bitzero (BTZRF) / OneQode | C-A6 / C-A2 | 2026-05-05 | 110MW 15-yr Namsskogan, Norway lease to GPU tenant OneQode. BTC-mining heritage → operator side may route NeoCloud (NC5) per Op Principle 9; segment borderline. |
| Equinix KL2 (Kuala Lumpur) | U3 / C-C2 | 2026-05-11/12 | $190M 4th Malaysia IBX, liquid-cooling-ready, carrier-neutral. Equinix already in pool (id 303850136250, hs_is_target_account=true, heat=Hot). |
| Hut 8 / Beacon Point TX | C-A6 anchor signing | 2026-05-06/07 | 352MW, 15-yr, ~$9.8B (up to $25.1B) to confidential investment-grade tenant. Hut 8 is NeoCloud-classified; colo record "Hut 8 HPC" not in colo tier-1/3 pool. Belongs to NeoCloud scan. |

Dropped (not carryover): I Squared/Elea M&A (late April, out of window); WhiteFiber/Nscale (Dec-2025 deal, May-30 billing milestone is not a fresh signing); DataBank $665M securitization (capital markets); Ecolab/CoolIT (cooling-vendor M&A, not a colo operator); market-research report wires; Equinix CFO Leonetti (CFO is not a C-A4 interconnection/network persona).

---
*End of segment run report. No rep DMs, no canvas Run log row, no Cooper run report sent — those are owned by signal-scan-aggregator at 2:30pm CT, which reads HubSpot (source of truth) for last_signal_date = today records.*
