# Signal Scan - Fiber Operator - Segment Run Report

**Date:** 2026-06-15 (Monday, CT)
**Segment:** Fiber Operator
**Detection window:** 2025-12-17 -> 2026-06-15 (180 days rolling, event-date semantics)
**Outcome:** Steady-state week - **21 HubSpot signal writes** (1 recovered from a wrong-domain match). First post-catch-up run; anti-churn held back ~10 same-event re-detections already written in the 2026-06-08 catch-up.
**Apollo consumed:** 2 of 35 (Stage 3 enrich attempts; weekly W24 pool 0/850 -> 2/850 after)
**Runtime:** ~50 min
**MCPs used:** HubSpot (read + write), Slack (canvas read - oversized, see notes), web_search / web_fetch (via 5 detection sub-agents + 1 new-account research sub-agent), Apollo (3 enrich attempts, 2 billable)

---

## 1. Run header

| Item | Value |
|---|---|
| Target pool (Fiber Operator, all tiers, type != Customer; MaiaEdge own + Flagged excluded by segment filter) | 1,260 records |
| Canvas F0B0AFSB9LN read | Returned oversized (~1.0M chars). No Fiber-tagged Tier 3 carryover from prior runs (consistent with 2026-06-08 report: no signal-scan-owned Fiber Tier 3 items). No carryover to drain; no new Tier 3 holds created this run. |
| Apollo budget tracker | weekly-reports/apollo-budget.json - W24, 0/850 before, sub-cap 35, effective 35 |
| Prior segment report | weekly-reports/2026-06-08/signal-scan/fiber/segment-run-report.md (CATCH-UP, 20 writes) - used as anti-churn baseline |
| Overflow backlog | None (scored candidates < 60; no budget-overflow carry) |

---

## 2. Source coverage

Detection fanned out across 5 sub-agents (BEAD/public-funding, M&A/PE, debt/ABS/earnings, exec-hires, network/AI-DC) using the search-anchor pattern. Every documented Source Registry family was attempted.

| Source family | Status | Notes |
|---|---|---|
| NTIA BEAD dashboard + state broadband offices (TX, NY, KS) | ✓ | TX final subgrantee contracts (06-03), NY $542M plan (04-24), KS BAG+BEAD |
| Telecompetitor / Broadband Communities | ✓ | Primary BEAD coverage source |
| Fierce Network / Fierce Telecom (M&A + People) | ✓ | T-Mobile fiber JVs, hiring roundups |
| Light Reading (M&A Watch + People + optical) | ✓ | |
| Lightwave Online | ✓ | Heartland Fiber Project, route builds |
| StockTitan / SEC EDGAR (LUMN/UNIT/FYBR/CCOI/ATUS/WOW/TDS) | ✓ | Lumen 8-Ks, Uniti ABS, Zayo ABS |
| KBRA / Fitch / Moody's ABS summaries | ✓ | Zayo $2.37B, Lightpath $1.657B |
| PR Newswire / Business Wire / GlobeNewswire | ✓ | Appointments + M&A + financing |
| BroadbandBreakfast | ✓ | Cable One / Point Broadband close |
| Capacity Media / BNamericas / Light Reading Europe (intl) | ✓ | Lyntia refi, DTCP/Dark Fiber Group, Vocus |
| SubmarineNetworks / TeleGeography | ✓ | I-AM subsea JV (routed to Network Op, not scored here) |
| Greenhouse / Lever / Ashby job boards | ✗ | Not individually scraped; exec-hire coverage via press wires instead |
| Federal Register | ✓ | BEAD allocation context |
| Apollo MCP (job changes / funding / scoops) | ~ | Used for Stage 3 firmographics only; not run as a standalone signal feed this run |

Coverage note: 3 of 6 sub-agents could not read the priority watchlist file from their sandbox; they reported every fiber-operator event on merit and matching was performed in-process against the full 1,260-record index, so coverage was not degraded.

---

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target list size | 1,260 |
| Detected raw candidates (deduped) | 39 |
| Matched to target accounts | 34 (incl. Range, recovered via corrected domain range.net) |
| Skipped by anti-churn / same-event / below-floor | 13 |
| QA-gate / segment-scope drops | 5 (Network-Op-classified: Vocus, Spectrum, Charter, AT&T; + Plains Internet domain-collision) |
| Net signal writes | 21 |
| NEW accounts created | 0 (2 strong candidates already existed in CRM; 3 deferred) |

---

## 4. Score distribution (writes)

| Band | Count |
|---|---|
| Highest 27+ | 10 |
| Strong 18-26 | 7 |
| Worth Reviewing 12-17 | 1 |
| LIGHT 8-11 | 3 |

Heat of writes: Hot 3 / Warm 8 / Cool 10 / Cold 0.

---

## 5. Writes summary (21)

| ID | Company | Signal | Score | last_signal_date | Heat Δ | Tier Δ | Owner |
|---|---|---|---:|---|---|---|---|
| 266871288512 | Point Broadband | F-A7 | 33 | 2026-05-04 | Cool->Warm | tier_2 (frozen) | Tim Lieto (East) |
| 175225132733 | Frontier | F-A1 | 27 | 2026-06-03 | Cool->Warm | tier_2 (frozen) | Ken Cunningham (West) |
| 322837060291 | Aristotle Unified Communications Inc. | F-A1 | 27 | 2026-06-03 | Cold->Warm | tier_3->tier_2 | Tim Lieto (East) |
| 316149788366 | Brightspeed Business | F-A1 | 27 | 2026-06-03 | Cold->Warm | tier_2 (frozen) | Tim Lieto (East) |
| 292817295084 | 360 Broadband | F-A1 | 27 | 2026-06-03 | Cold->Warm | tier_3->tier_2 | Ken Cunningham (West) |
| 297858169562 | RTA Telecommunications of America | F-A1 | 27 | 2026-06-03 | Cold->Warm | tier_2->tier_1 | Ken Cunningham (West) |
| 107187281647 | Lumen Technologies | FR-1 | 27 | 2026-06-11 | Hot->Hot | tier_2 (frozen) | Tim Lieto (East) |
| 264241842927 | ALLO Communications | F-A5 | 27 | 2026-06-01 | Cold->Warm | tier_3->tier_2 | Ken Cunningham (West) |
| 194004502229 | Arvig | F-A5 | 27 | 2026-05-21 | Hot->Hot | tier_2 (no change) | Tim Lieto (East) |
| 154278570716 | Range Telephone Cooperative | F-A3 | 27 | 2026-05-28 | Cold->Warm | tier_4->tier_3 | Ken Cunningham (West) |
| 292520998645 | Archtop Fiber | F-A1 | 18 | 2026-04-24 | Cold->Cool | tier_3 (no change) | Tim Lieto (East) |
| 297777475262 | Reasnor Telephone | F-A1 | 18 | 2026-04-24 | Cold->Cool | tier_3 (no change) | Tim Lieto (East) |
| 318097753791 | Dark Fiber Group | F-A2 | 18 | 2026-03-24 | Cold->Cool | tier_2 (no change) | Tim Ziemer (Intl) |
| 316303584979 | Lyntia Networks | F-A8 | 18 | 2026-04-22 | Cold->Cool | tier_2 (no change) | Tim Ziemer (Intl) |
| 175156545265 | Dobson Cellular Operations | F-A5 | 18 | 2026-04-13 | Cold->Cool | tier_3 (no change) | Ken Cunningham (West) |
| 292788993740 | Wecom Fiber | F-A5 | 18 | 2026-03-23 | Cold->Cool | tier_3 (no change) | Ken Cunningham (West) |
| 252507461351 | Intermountain Infrastructure Group, LLC | F-B2 | 18 | 2026-06-08 | Cold->Cool | tier_2 (frozen) | Ken Cunningham (West) |
| 322368676578 | Segra | F-B3 | 12 | 2026-05-19 | Cold->Cool | tier_2 (frozen) | Tim Lieto (East) |
| 320366552764 | Gigapower | F-A5 | 9 | 2026-03-03 | Cold->Cool | tier_2 (frozen) | Ken Cunningham (West) |
| 297906089706 | Fibernow | F-A5 | 9 | 2026-02-09 | Hot->Hot | tier_2 (no change) | Tim Lieto (East) |
| 193100077770 | Alaska Communications Systems Group | F-A5 | 9 | 2026-01-19 | Cold->Cool | tier_2 (no change) | Ken Cunningham (West) |

Tier promotions (5): Aristotle T3->T2, 360 Broadband T3->T2, RTA Telecommunications T2->T1, ALLO Communications T3->T2, Range Telephone Cooperative T4->T3. All driven by the hot-signal -1 modifier (score 27-44, event <=60d); non-target accounts only. Frozen-tier accounts (hs_is_target_account=true) had heat written but tier untouched: Frontier, Brightspeed, Point Broadband, Lumen, Gigapower, Intermountain IG, Segra.

Heat promotions to Warm/Hot: 8 (Frontier, Aristotle, Brightspeed, 360 Broadband, RTA, Point Broadband, ALLO, Range). Lumen / Arvig / Fibernow remained Hot (count>=2 or open deal). 10 Cold->Cool minor bumps.

No last_enriched_date bumped (all partial signal writes per Unified Stamping Policy).

---

## 6. Tier 3 holds

None this run. No canvas carryover drained; no new Tier 3 holds appended.

---

## 7. QA gate drops + anti-churn skips

**Segment-scope drops (route to a non-Fiber segment - not scored here):**
- Vocus (vocus.com.au) - classified Network Operator(Tier 1 / VNO) in CRM; CTO hire (ex-Zayo) belongs to the Network Op scan.
- Spectrum / Spectrum Business (Charter) - Network Operator(Tier 1 / VNO). TX BEAD awards route to Network Op.
- AT&T (Southwestern Bell) - Network Operator(Tier 1 / VNO). TX BEAD routes to Network Op.
- Intra-Asia Marine Networks (NTT DATA JV) - pure-play subsea; routes to Network Operator/Subsea cable operator.

**Data-ambiguity drop:**
- Plains Internet (TX BEAD $96.1M, 06-03) - domain plainsinternet.com resolves in CRM to "AMA TechTel Communications", which separately BACKED OUT of its TX BEAD provisional award. Writing a $96.1M award narrative onto that record would be factually wrong. Not written. Flag for data-quality review (entity/domain mismatch).

**Anti-churn / same-event skips (already in CRM at equal-or-fresher state):**
- GCI/Quintillion (stored 04-22 score 30 > re-detection 27, same deal), GoNetspeed + i3 Broadband + Hunter Communications (same 04-28 / 03-31 JV announcements already stored), Astound CEO hire (March activity already stored at 03-15), Uniti ABS pricing 06-05 (stored 06-01 score 33 is the same securitization at higher score), Zayo $2.37B ABS (stored 05-21 score 29 newer), Lightpath securitization 03-03 (stored 05-19 newer), Fidium/Consolidated NY BEAD (stored 05-21 score 27 newer), BIG Fiber $250M (stored 05-19 score 30 same deal), Cirion NaaS (stored 05-20 newer), Light Source Communications x3 (stored 05-21 newer), Vyve (stored 05-18 newer).
- Twin Valley KS BEAD ($7.6M blended, 03-10) - score 6 below floor 8 (Tier A x 90-180d freshness x MED). Dropped.
- US Signal OH/IN build (02-06) - Tier B event >90d, dropped per Tier B freshness cap.
- WOW! CEO hire (01-06) - score 6 below floor, dropped.

---

## 8. New-account candidates (deferred, NOT created)

| Candidate | Domain | Signal | Why deferred |
|---|---|---|---|
| USConnect Holdings | usconnect.net | F-A1 TX BEAD $36.6M (06-03) | MED confidence - entity-identity ambiguity (US Connect LLC ~7-employee PA holding vs Livingston Telephone / Highline TX operating ILEC sharing the domain); HQ state unresolved for owner. Default-to-not-writing. Re-verify next pass / R7 sourcing. |
| CBN America | cbn.net | F-A1 NY BEAD $121.2M (04-24) | MED - award is fiber to only 3,087 locations plus heavy fixed-wireless; ICP fit borderline. Needs deeper research. |
| Altibox Carrier | altiboxcarrier.com | F-A5 CTO hire ex-Microsoft (01-01) | International (Norway) wholesale carrier; signal 165d old (LIGHT). Clean fit but low urgency - log for intl sourcing. |

**Misclassification flag (for R2 / D7):** WIN Technology (wintechnology.com, id 316278520568) is classified `MSP/Aggregator` in CRM but research shows a carrier-neutral operator owning a ~20,000-mile fiber backbone (route-miles band 10K-50K, ~150 POPs, 2 owned DCs), a co-builder on the Heartland AI dark-fiber project. Multi-marker (infrastructure_profile) points to Fiber Operator. Out of scope for this signal scan (MSP-classified); flag for reclassification review. Heartland F-A3 signal NOT written pending re-segment.

---

## 9. Failed writes

None. 21/21 company updates returned success (2 batches of 10 + 1 single, 0 failed).

---

## 10. Apollo budget post-run

| Item | Value |
|---|---|
| Sub-cap (Fiber) | 35 / run |
| Effective budget | 35 (weekly W24 pool 0/850 at start) |
| Consumed this run | 2 (usconnect.net found = 1; win-technology.com wrong-entity match = 1; gorange.com empty = 0) |
| Weekly pool after | 2 / 850 |
| Notes | gorange.com + win-technology.com were wrong domains supplied by detection; corrected to range.net + wintechnology.com via research (both already in CRM). |

---

## Handoff

Aggregator (signal-scan-aggregator, 2:30pm CT) will read HubSpot for last_signal_date = today's writes, build the 3 territory rep DMs, append the canvas Run log row, and write Cooper's cross-ICP run report. This task sent NO rep DMs, made NO canvas Run-log edits, and wrote NO Cooper run report, per the per-segment task contract.
