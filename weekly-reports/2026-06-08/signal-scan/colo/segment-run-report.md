# Signal Scan — Data Center Colo Provider — Segment Run Report

## 1. Run Header
- **Date (CT):** 2026-06-08 (Monday)
- **Segment:** Data Center Colo Provider
- **Detection window:** 2025-12-10 -> 2026-06-08 (180 days rolling, event-date basis; widened from 14d per 2026-06-04 coverage expansion)
- **Scope:** ALL tiers (no tier filter, per 2026-06-04 change), non-Flagged, type != Customer, excl. MaiaEdge own
- **Apollo consumed:** 0 of 35 (no NEW-account creation)
- **Runtime:** ~1 run (detection fanned out across 2 research subagents per context-budget safeguard; matched-account writes batched)
- **MCPs used:** HubSpot (search + manage_crm_objects), Slack (canvas read), web_search/web_fetch; Apollo NOT invoked
- **Outcome:** 5 matched-account signal writes; 0 NEW accounts; 0 Apollo. Active week (180d window surfaced a backlog of material M&A/buildout events not previously signal-scored).

## 2. Source Coverage Table
Search-anchor attempts against the documented Colo Source Registry. ✓ = reachable / returned results (even if 0 actionable); ✗ = errored / unreachable / nothing returned.

| # | Source (tier) | Status | In-window actionable hits |
|---|---|---|---|
| 1 | Data Center Frontier (Robust) | ✓ | 0 net-new (analysis/marketing + M&A scorecard; everything actionable also on wires) |
| 2 | Data Center Dynamics (Robust) | ✓ | High yield: QTS Van Wert, H5/NovaCap-365, I Squared/Cogent, RadiusDC/phoenixNAP, atNorth $4.2B, Equinix KL2, Bitzero, Hut 8 |
| 3 | Data Center Knowledge (Robust) | ✓ | 0 net-new (M&A outlook + Q2-2026 appointments roundup reviewed; WhiteFiber/Nscale already captured) |
| 4 | Bisnow Data Center (Robust) | ✓ | 0 unique (DataBank securitization = capital-markets excluded; PowerHouse Loudoun corroboration) |
| 5 | PR Newswire / Business Wire / GlobeNewswire (Robust) | ✓ | Highest yield: RadiusDC/phoenixNAP, DataBank/Goodman LA, PowerHouse Arcola, H5/365, I Squared $1B, DLR Malaysia, atNorth, Sify FY results |
| 6 | StockTitan 8-K mirror (DLR/EQIX/IRM/DBRG/COR) (Robust) | ✓ | EQIX atNorth $4B + Gemini/xScale; DLR Malaysia; IRM Q1 earnings-language. No fresh DBRG/COR item |
| 7 | SEC EDGAR full-text (Robust) | ✓ | Corroborated EQIX/DLR/IRM 8-Ks; no standalone net-new |
| 8 | Greenhouse / Lever / Ashby job boards (Robust) | ✗ | 0 (no indexed in-window VP/Dir Interconnection/Network/Fabric hire or 3+ net-eng req surge at a named colo; ATS pages not web-indexed). **2-week ✗ streak** |
| 9 | Apollo MCP (Robust) | n/a | Not invoked — 0 NEW-account creation, so 0 Apollo credits. Matched-account signal writes do not consume Apollo |
| 10 | Hyperscaler feeds AWS/Azure/GCP (Robust) | ✗ | 0 (no in-window region/AZ launch with a clean third-party colo anchor angle; hyperscaler self-build dominates). **2-week ✗ streak** |
| 11 | NVIDIA Newsroom / GTC (Robust) | ✓ | 0 colo (DSX AI-factory blueprint names neoclouds, not colo operators; DLR quantum-GPU interconnect has no discrete dated anchor). Streak broken (was ✗ last week) |
| 12 | Crunchbase News (Medium) | ✓ | 0 colo (zero disclosed colo equity deals YTD 2026; Crusoe $1.38B is NeoCloud). Streak broken (was ✗ last week) |
| 13 | Conference agendas PTC/Capacity/ITW/Datacloud/AI Infra (Medium) | ✓ | Context only (7x24 Spring Jun 7-10; Data Center World POWER Sep 21-23). No standalone signal per noise list |
| 14 | AFCOM + 7x24 Exchange (Medium) | ✗ | 0 (event-calendar / association overview only) |
| 15 | Mighty Penguin DC newsletter (Medium) | ✗ | 0 (not retrievable / no indexed in-window issue) |
| 16 | Cross-segment exec-hire stack (Medium) | ✓ | Reviewed StockTitan 5.02 + PRN Appointments + DCK Q2-2026 appointments: all CEO/CFO/CPO/board/sustainability roles. ZERO qualifying C-A4 interconnection/network/fabric hires |
| Intl | DCD EMEA/APAC/LATAM, Capacity, Data Centre Review, BNamericas, Zawya, AGBI | ✓ | Equinix KL2 (Malaysia/APAC), Bitzero Norway via DCD; BNamericas LatAm = market color; ME sovereign-cloud thematic, no discrete dated event |

**3-week ✗ streak watch:** Sources #8 (Greenhouse/Lever/Ashby job boards) and #10 (hyperscaler region feeds) are at **2 consecutive ✗** (also ✗ on 2026-06-01). If ✗ again next Monday (2026-06-15), flag to Cooper as "Sources Needing Development." #11 NVIDIA and #12 Crunchbase recovered to ✓ this week.

## 3. Candidate Funnel
| Stage | Count |
|---|---|
| Target list size (Colo, all tiers, type != Customer, excl. MaiaEdge own) | 466 active (467 total minus 1 type=Customer = HDCO GROUP; MaiaEdge own not in Colo pool) |
| Tier 3 canvas carryovers added | 1 (Digi Power X, from 2026-05-11 signal-scan hold) |
| Detected raw candidates (both subagents, in/near window) | ~18 |
| In-scope Colo candidates after routing/exclusions | 8 |
| Matched to existing account + written | 5 |
| Matched but skipped (anti-churn) | 3 (Equinix, DataBank, Digital Realty) |
| NEW accounts created | 0 (Apollo 0) |
| **Total HubSpot writes** | **5** |
| Dropped — routed to NeoCloud (flagged for NeoCloud scan) | 4 entities (Digi Power X, Bitzero, Hut 8, Applied Digital) |
| Dropped — below score floor | 1 (PowerHouse Arcola, score 6) |
| Dropped — out of window (>180d) | 2 (Centersquare $1B 10-DC 2025-10; Vantage Frontier 2025-12) |
| Dropped — no discrete entity / not Colo | 2 (I Squared $1B platform; Cogent DC divestiture = Network Op) |
| Dropped — same-event dedup | 1 (phoenixNAP; event written on acquirer RadiusDC) |
| Dropped — capital-markets-only | 4 (DataBank $665M + TierPoint $240M securitizations; DLR $7.5B ATM; QTS $3.5B refi - all already stored or non-operational) |

## 4. Score Distribution
| Bucket | Count |
|---|---|
| 27+ (Highest) | 1 (QTS 27) |
| 18-26 (Strong) | 2 (RadiusDC 18, Sify 18) |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 2 (H5 9, atNorth 9) |
| <8 (silent drop, log only) | 1 (PowerHouse 6) |

## 5. Writes Summary
All 5 succeeded (manage_crm_objects batch, 5/5, 0 failed). `last_enriched_date` NOT bumped (partial signal writes). sc30=1 for all (single current signal each).

| id | Name | Code | Event date | Score | Heat prior -> new | Tier |
|---|---|---|---|---|---|---|
| 251536944853 | QTS Realty Trust | U3 (mega-campus buildout) | 2026-05-29 | 27 | Cold -> **Warm** | tier_1 (tier write SKIPPED: hs_is_target_account=true) |
| 264034893521 | RadiusDC | C-A7 M&A | 2026-03-12 | 18 | Cold -> **Cool** | tier_1 -> tier_1 (no change; tgt not set) |
| 322877846251 | Sify Technologies | C-A6 anchor (earnings-stated) | 2026-04-13 | 18 | Cold -> **Cool** | tier_1 -> tier_1 (no change) |
| 251574626020 | H5 Data Centers | C-A7 M&A | 2026-01-29 | 9 | Cold -> **Cool** | tier_1 (tier write SKIPPED: hs_is_target_account=true) |
| 267092339390 | atNorth | C-A7 M&A | 2026-02-27 | 9 | Cold -> **Cool** | tier_1 (tier write SKIPPED: hs_is_target_account=true) |

**Narratives written (pure prose, no date prefix, no em dash, no competitor brand):**
- QTS: "Named as the end-user of a $10B, 902-acre greenfield mega-campus in Van Wert, Ohio, with up to seven buildings and 500MW planned, anchoring a major new Midwest AI capacity buildout."
- RadiusDC: "Acquiring phoenixNAP's Phoenix data center and colocation business, entering Arizona with close expected Q2 2026; plans to expand to 8MW and build a second 18MW facility (DC2)."
- Sify: "Disclosed in FY2025-26 results that a global hyperscaler contracted its largest single-building liquid-cooled capacity in the Indian subcontinent, confirming AI tenant readiness across its colocation portfolio."
- H5 Data Centers: "Launched the HyscaleIX carrier-hotel joint venture with NovaCap and acquired three interconnection-dense sites in Buffalo, Nashville, and Tampa, expanding its meet-me-room footprint."
- atNorth: "Agreed to be acquired by a major interconnection operator and CPP Investments for $4B, signaling consolidation of Nordic high-density AI colocation capacity across the Nordics."

**Anti-churn skips (already hold a newer/higher stored signal — correct no-op):**
- Equinix (303850136250): detected KL2 Malaysia C-A3 event 2026-05-11 score 27 < stored last_signal_date 2026-05-21 / score 27 (CFO appointment). No write.
- DataBank (193865438937): detected Goodman LA 32MW JV already stored (last_signal_date 2026-05-21, score 30, heat Hot, sc30 2). No write.
- Digital Realty (193856795322): stored last_signal_date 2026-05-04 / score 27 (ATM equity offering) newer/equal to detected (Malaysia 1/19 old; BCN1 5/18 below floor). No write.

## 6. Tier 3 Holds
- **Came in:** 1 — Digi Power X (digipowerx.com), from the 2026-05-11 Weekly Signal Scan hold ("C-A2 GPU tenant anchor - Cerebras 40MW Columbiana AL; defer to next R1 cycle").
- **Resolution: RE-ROUTED to NeoCloud (NC5, Crypto to AI - Neoclouds) per Operating Principle 9.** Digi Power X = formerly Digihost Technology, a Bitcoin miner pivoting to AI infrastructure. Op Principle 9 routes BTC-mining-heritage AI-pivot companies to NC5 "regardless of business model (operator AND landlord)." The Cerebras 40MW colocation lease is a landlord-model deal, but the BTC heritage governs the segment route (same basis on which Bitzero and Hut 8 were routed to NeoCloud this run, and Applied Digital/Crusoe/Prometheus were moved 2026-05-14). The prior "Small Canadian colo" tag predates Op Principle 9 (2026-05-14). 
  - NOT scored as a Colo signal. NOT created as a Colo record. NOT re-appended to canvas as a Colo Tier 3 hold (resolved by re-route).
  - **Action for NeoCloud scan (fires 10:30am CT):** create/score Digi Power X (DGXX, digipowerx.com) under NeoCloud NC5. C-A2/C-A6, Cerebras 40MW Columbiana AL, ~$1.1B, event 2026-05-05. Net-new to CRM. (Also note its NVIDIA Vera Rubin GPU order 2026-06-03 = NeoCloudz GPUaaS arm signal.)
- **New Tier 3 holds created this run:** 0.
- **Net canvas action:** nothing re-appended to F0B0AFSB9LN.

## 7. QA Gate Drops
0. All 5 write candidates passed the 10-rule Stage 4.5 gate (source URLs verified live against primary sources; event dates confirmed; segment = Data Center Colo Provider; narratives <=250 chars, pure prose, no em dash, no competitor brand; owner mapping valid; score arithmetic checked; deduped). PowerHouse Arcola was dropped earlier at Stage 4 scoring (score 6 < floor 8), not at the QA gate.

## 8. Failed Writes
None. 5/5 succeeded.

## 9. Apollo Budget Post-Run
- Credits consumed this run: **0** (no NEW-account creation; no firmographic enrichment needed).
- Sub-cap: 35/run. Used 0 of 35.
- Weekly W23 (2026-W23): 0/850 before run -> 0/850 after run. 850 remaining.

---

## Routed to NeoCloud (flagged for the NeoCloud segment scan — NOT scored as Colo)
Material AI-infra anchor/lease events on BTC-mining-heritage operators (Op Principle 9 -> NC5):
| Entity | Event | Date | Note |
|---|---|---|---|
| Digi Power X (digipowerx.com, DGXX) | Cerebras 40MW colocation + MSA, Columbiana AL, ~$1.1B (C-A2/C-A6) | 2026-05-05 | Digihost BTC heritage. Net-new to CRM. Resolves the 2026-05-11 colo carryover. |
| Bitzero Holdings (bitzero.com) | OneQode 110MW 15-yr lease, Namsskogan Norway, ~$2.6B lifetime | 2026-05-05 | BTC heritage -> NC5. International (Tim Z). |
| Hut 8 (hut8.com) | Beacon Point TX 352MW 15-yr, investment-grade tenant, ~$9.8B | 2026-05-06 | NeoCloud-classified. East (TX). |
| Applied Digital | Delta Forge 1 ($7.5B/300MW, 2026-04-23) + Polaris Forge 3 (2026-05-20) | 2026-04/05 | NC5. Already NeoCloud-classified. |

## Notes for Cooper / aggregator
- **Data-quality flag (no action taken):** Equinix's stored signal (last_signal_score 27, heat Hot) is a CFO appointment (Olivier Leonetti) - a CFO is not a C-A4 interconnection/network buying persona, so 27 likely over-scores it. Anti-churn correctly prevented this run from touching it; flagging for a possible manual correction or for R-Tier-Audit awareness.
- **I Squared $1B US AI-inference/edge colo platform** (announced 2026-05-25, seeded by a ~$225M Cogent 10-facility acquisition) is a real, fresh, high-relevance signal but has no discrete operating-company name/domain yet (PE-launched platform). Deferred - revisit when the platform is named so a clean CRM record can be created. The Cogent DC divestiture itself is a Network Operator signal (Cogent), not Colo.
- **Carryover for next Monday:** none material to Colo. The largest fresh leases (Bitzero, Hut 8) belong to the NeoCloud scan.

---
*End of segment run report. No rep DMs, no canvas Run log row, no Cooper run report sent — those are owned by signal-scan-aggregator at 2:30pm CT, which reads HubSpot (source of truth) for last_signal_date = today records.*
