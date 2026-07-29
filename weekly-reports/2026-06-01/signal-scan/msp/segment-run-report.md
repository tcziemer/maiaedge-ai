# Signal Scan — MSP/Aggregator — Segment Run Report

## 1. Run header

| Field | Value |
|---|---|
| Date (CT) | 2026-06-01 (Monday) |
| Segment | MSP/Aggregator |
| Detection window | 2026-05-18 → 2026-06-01 (14-day rolling) |
| Apollo consumed | 0 of 20 |
| MCPs | HubSpot ✓ · Apollo ✓ (unused) · Slack/canvas ✓ · web_search ✓ · web_fetch ✓ |
| Outcome | **QUIET in-window week — 0 scored hits ≥8, 0 HubSpot writes** |
| Prior Monday report | ABSENT (weekly-reports/2026-05-25/signal-scan/msp/ does not exist — first per-segment MSP run since the 2026-05-28 split) → all accounts tagged NEW |

## 2. Source coverage table

Search-anchor pattern used throughout (direct web_fetch gated on Cowork runtime). 3-week ✗ streak tracking begins this run (no prior MSP per-segment report on disk).

| # | Source | Tier | Attempted | Result |
|---|---|---|---|---|
| 1 | Channel Futures (+ Hiring Roundup) | Robust | ✓ | Only out-of-window items (TSD market reports, Bluewave Nov-25/Jan-26 deals). No in-window M&A/hire. |
| 2 | ChannelE2E (+ People column) | Robust | ✓ | People-moves weeks May 18-22 + May 25-29 located. Named moves = Cycurion CFO (cyber/IT MSP), WatchGuard, Nile CRO, Mobilfy VP — none are target MSP/Aggregator anchors; IT MSP Test / wrong-subtype excludes. |
| 3 | TSD press (Telarus / AppDirect / Sandler / AVANT / Bridgepointe / Upstack / Intelisys / ScanSource) | Robust | ✓ | All surfaced events out of window: ScanSource Q3 5/07, AVANT/CMC 5/05, Bridgepointe/Charlesbank (≤4/09), Intelisys Channel Exchange (Dec-9), Telarus Hub (Mar-25), Front partnerships (Mar-18). |
| 4 | CRN | Robust (caveat) | ✓ | Award-press only (Channel Chiefs, Women of the Channel, MSP 500). EXCLUDED per award-press syndication rule. |
| 5 | StockTitan (SCSC / SNX / CMCSA 8-K) | Robust | ✓ | SCSC 8-K = 5/07 earnings (OOW, already written). SNX no in-window 8-K. CMCSA none surfaced. |
| 6 | SEC EDGAR full-text | Robust | ✓ | Covered via SCSC/SNX filing search — no in-window Item 1.01/2.01/5.02 for targets. |
| 7 | FCC Daily Digest | Robust | ✗ | Not anchored this run; no MSP-relevant items surfaced incidentally. (✗ streak: 1) |
| 8 | ScanSource + TD SYNNEX IR / earnings (M-A7, M-B4) | Robust | ✓ | SCSC Q3 5/07 (OOW). SNX Q2 FY26 not yet released (guidance only; Q1 was 3/31). No in-window earnings event. |
| 9 | PR Newswire + Business Wire + GlobeNewswire | Robust | ✓ | Appointments scanned — no CRO/VP move at a target aggregator. |
| 10 | Apollo MCP (enrich / job postings / job changes) | Robust | ✗ | Not consumed — no NEW-account candidates required firmographic enrichment. |
| 11 | Megaport / Console Connect / PacketFabric partner-adds (M-A3) | Robust | ✓ | No in-window carrier/partner additions found. |
| 12 | Greenhouse / Lever / Ashby TSD job boards (M-A6) | Robust | ✗ | Not anchored this run. (✗ streak: 1) |
| 13 | CompTIA / GTIA | Medium | ✗ | Not anchored. (✗ streak: 1) |
| 14 | Channel Partner Insight / IT Europa / ChannelBiz (EMEA) | Medium | ✓ | Expereo/Wavenet only out-of-window (Cato collab Feb-26; Breeze acq prior). No in-window moves. |
| 15 | FedRAMP Marketplace (M-C2) | Medium | ✗ | Not anchored. (✗ streak: 1) |
| 16 | Telecompetitor channel | Medium | ✓ | Broadband/AI/BEAD coverage only; no aggregator moves. |
| 17 | CP Expo / Channel Partners Conf agenda | Medium | ✓ | TBI/Intelisys/AVANT/MicroCorp May-June partner gatherings noted — EXCLUDED per conference-noise rule. |
| 18 | Gartner SD-WAN MQ / Forrester Wave | Medium | ✗ | Not anchored. (✗ streak: 1) |
| 19 | Frost & Sullivan TSD | Medium | ✗ | Not anchored. (✗ streak: 1) |
| 20 | TBI Connect / Channel Asia | Medium | ✗ | Not anchored. (✗ streak: 1) |

Robust-tier: 8 of 12 attempted; **in-window writable yield = 0** (below 25 floor → see §11 EMEA fallback).

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target accounts (HubSpot: MSP/Aggregator, tier 1-3, type != Customer, ≠ MaiaEdge) | 336 (tier_1=11, tier_2=323, tier_3=2) |
| Canvas F0B0AFSB9LN MSP Tier 3 carryovers requiring action | 0 (2026-05-11 holds — Bridgepointe/ScanSource/AVANT — drained 2026-05-25; event dates out of current window) |
| Raw in-window signal candidates detected | 0 |
| Matched to target accounts (Stage 2) | 0 |
| NEW-account candidates (Stage 3) | 0 |
| Scored hits ≥8 (Stage 4) | 0 |
| HubSpot writes (Stage 5/5b) | 0 |

## 4. Score distribution

No scored hits. (Floor 8; bands LIGHT 8-11 / Worth Reviewing 12-17 / Strong 18-26 / Highest 27+ — all empty.)

## 5. Writes summary

None. 0 narrative writes, 0 signal-field writes, 0 tier writes, 0 heat promotions, 0 NEW accounts. 0 priority-48h hits.

## 6. Tier 3 holds

None added. Canvas MSP carryover queue confirmed empty/resolved (drained 2026-05-25).

## 7. QA gate drops

None (no candidates reached the gate).

## 8. Failed writes

None.

## 9. Apollo budget post-run

Sub-cap 20, used 0 of 20. Weekly W22: 0/850 consumed, 850 remaining. No tracker write required (0 consumption).

## 10. IT MSP Test rejections (record-level)

No borderline candidates reached classification. In-window people-moves observed but dropped before matching (not target subtype): Cycurion (CFO move — cybersecurity/IT MSP), WatchGuard (security vendor), Nile (NaaS vendor CRO), Mobilfy (T-Mobile reseller VP). None are telecom/network aggregators; excluded at detection per IT MSP Test / wrong-subtype.

## 11. EMEA fallback flag

**RECOMMEND PROMOTE EMEA channel press next run.** Robust-tier in-window writable yield was 0, well below the 25 floor. Consistent with MSP/Aggregator being the lowest-velocity segment and with Colo + NeoCloud both running QUIET in-window today. For 2026-06-08, elevate Channel Partner Insight (UK), IT Europa, and ChannelBiz (DACH) into the primary rotation, and anchor the under-attempted Robust sources this run skipped (FCC Daily Digest, Greenhouse/Lever/Ashby TSD job boards for M-A6).

---

### Footer

```
[MSP] target=336 matched=0 new=0 writes=0 heat_promotions=0 priority_48h=0 apollo=0/20 runtime=~7min audit=weekly-reports/2026-06-01/signal-scan/msp/
```

No Slack DM sent. Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs + canvas Run log + Cooper run report; it will read HubSpot for `last_signal_date = today` records (0 from this segment) and degrade gracefully on this segment's nil contribution.
