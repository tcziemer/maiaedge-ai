# Signal Scan — MSP/Aggregator — Segment Run Report

## 1. Run header

| Field | Value |
|---|---|
| Date (CT) | 2026-06-15 (Monday) |
| Segment | MSP/Aggregator |
| Detection window | 2025-12-17 → 2026-06-15 (180-day rolling, event-date basis) |
| Scope | All tiers, non-Flagged, type != Customer, ≠ MaiaEdge own |
| Apollo consumed | 0 of 20 |
| MCPs | HubSpot ✓ · Apollo ✓ (unused) · Slack/canvas ✓ (read) · web_search ✓ (sub-agent fan-out) · web_fetch ✓ (search-anchor) |
| Outcome | **QUIET week — 0 writable signals, 0 HubSpot writes.** The Q1/Q2 TSD backlog (AppDirect, TD SYNNEX, AVANT, ScanSource, Bridgepointe, Expereo) was already swept and stored in prior runs; anti-churn correctly suppresses re-writes. The genuinely new in-window events this week are either out-of-segment (Megaport/Console Connect classify as `Other`, not MSP) or below the score-8 floor (Telarus+Telnyx = 6). |
| Prior Monday report | PRESENT (2026-06-08, 3 writes: AppDirect/TD SYNNEX/Expereo) → those accounts CARRIED with stored signals; re-confirmed no newer event |
| Backlog carry-in | None (no `backlog.md` on disk from 2026-06-08; that run had 3 writes, no overflow) |
| Context-budget safeguard | Detection fanned out across 3 read-only research sub-agents (M&A+earnings / hires+AI+carrier-adds / EMEA+NaaS-operators) so raw source text stayed out of main context |

## 2. Source coverage table

Search-anchor pattern throughout (direct `web_fetch` gated on Cowork runtime; sub-agents anchored each source via `web_search` then fetched article URLs). EMEA channel press kept in primary rotation per the standing 180-day-window recommendation.

| # | Source | Tier | Attempted | Result |
|---|---|---|---|---|
| 1 | Channel Futures (+ Hiring Roundup) | Robust | ✓ | Telnyx/Telarus partnership (2/10) + market context. No in-window M-A1/M-A5 at a target beyond items below. |
| 2 | ChannelE2E (+ People column) | Robust | ✓ | June 08–12 People column reviewed — every move (Mitel, Armadin, Team Cymru, Sonatype CRO, Hatz AI, iCOUNTER, IP Fabric) is cybersecurity/IT-MSP → all FAIL IT MSP Test. No telecom-aggregator exec move at the M-A5 title bar. |
| 3 | TSD press (Telarus / AppDirect / Sandler / AVANT / Bridgepointe / Upstack / Intelisys / ScanSource) | Robust | ✓ | ScanSource March exec restructuring (3/16) surfaced → anti-churn + freshness-drop (see §7). No newer carrier/hire at a target. |
| 4 | CRN | Robust (caveat) | ✓ | Award-press only (Channel Chiefs / rankings). EXCLUDED per syndication rule. |
| 5 | StockTitan (SCSC / SNX / CMCSA 8-K) | Robust | ✓ | SCSC 8-K (exec restructuring, effective 3/16) confirmed; out of Tier-B 90-day freshness + anti-churn. SNX Q2 FY26 not yet filed (earnings 2026-06-25). CMCSA nothing in-window for a target. |
| 6 | SEC EDGAR full-text | Robust | ✓ | Confirmed SCSC 8-K; no other in-window Item 1.01/2.01/5.02 for a target. |
| 7 | FCC Daily Digest | Robust | ✓ | Checked; no in-scope aggregator/wholesale item. (✗ streak RESET — was 2; now ✓) |
| 8 | ScanSource + TD SYNNEX IR / earnings (M-A7, M-B4) | Robust | ✓ | SCSC Q3 FY26 (5/07) already stored (anti-churn). SNX Q2 FY26 reports 2026-06-25 — re-scan next Monday for likely M-A7/M-B4. |
| 9 | PR Newswire + Business Wire + GlobeNewswire | Robust | ✓ | ScanSource CHRO BW release (3/16) confirmed. Telnyx/Telarus GlobeNewswire (2/10). No in-window appointment at the M-A5 bar for a target. |
| 10 | Apollo MCP (enrich / job postings / job changes) | Robust | ✗ | Not consumed — 0 NEW accounts created, no firmographic gaps to fill. |
| 11 | Megaport / Console Connect / PacketFabric partner-adds (M-A3) | Robust | ✓ | Megaport platform launches + Console Connect April ecosystem update surfaced — but both entities classify as `Other` in CRM (out of segment; see §7/§10). |
| 12 | Greenhouse / Lever / Ashby TSD job boards (M-A6) | Robust | ✗ | No public board indexed in search. **(✗ streak: 3 — auto-flag; see §11.)** |
| 13 | CompTIA / GTIA | Medium | ✗ | Not anchored. (✗ streak: 3) |
| 14 | Channel Partner Insight / IT Europa / ChannelBiz (EMEA) | Medium | ✓ | Attempted; UK/DACH trades did not surface in US-only web search. NaaS-operator coverage came via company press + wires (material moves captured — all out-of-segment). |
| 15 | FedRAMP Marketplace (M-C2) | Medium | ✗ | Not anchored. (✗ streak: 3) |
| 16 | Telecompetitor channel | Medium | ✓ | Broadband/BEAD coverage only; no aggregator move. |
| 17 | CP Expo / Channel Partners Conf agenda | Medium | ✗ | Not anchored / conference-noise (EXCLUDED). |
| 18 | Gartner SD-WAN MQ / Forrester Wave | Medium | ✗ | Not anchored. (✗ streak) |
| 19 | Frost & Sullivan TSD | Medium | ✗ | Not anchored. (✗ streak) |
| 20 | TBI Connect / Channel Asia | Medium | ✗ | Not anchored. (✗ streak) |

Robust-tier: 10 of 12 attempted; **in-window writable yield = 0** (anti-churn-driven, not a coverage gap — see §11).

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target accounts (MSP/Aggregator, all tiers, type != Customer, ≠ MaiaEdge) | 480 (tier_1 = 11; remainder tier_2/3/4/5 long-tail) |
| Canvas F0B0AFSB9LN MSP signal-scan Tier 3 carryovers requiring action | 0 (2026-05-11 holds for Bridgepointe/ScanSource/AVANT were NEW-account recommendations since fulfilled — all now in CRM) |
| Backlog carry-in (2026-06-08 overflow) | 0 |
| Raw in-window signal candidates detected | 6 (ScanSource M-B1, Telarus M-A3, Megaport M-B2 ×3, Console Connect M-A3) |
| Matched to MSP/Aggregator target accounts (Stage 2) | 2 (ScanSource, Telarus) — both dropped at Stage 4 (see §7). 4 out-of-segment (Megaport/Console Connect = `Other`). |
| NEW-account candidates (Stage 3) | 0 (all signal companies already in CRM; no fresh in-window Upstack event to justify onboarding the 2026-06-08 deferred candidate) |
| Scored hits ≥8 (Stage 4) | 0 |
| HubSpot writes (Stage 5/5b) | 0 |

## 4. Score distribution

| Band | Count | Accounts |
|---|---|---|
| Highest (27+) | 0 | — |
| Strong (18-26) | 0 | — |
| Worth Reviewing (12-17) | 0 | — |
| LIGHT (8-11) | 0 | — |
| Below floor / dropped | 2 | Telarus M-A3 (6) · ScanSource M-B1 (freshness-drop) |

## 5. Writes summary

**None.** 0 narrative writes · 0 signal-field sets · 0 tier writes · 0 heat promotions · 0 NEW accounts · 0 priority-48h hits. No `last_enriched_date` bump (no writes). Anti-churn held the stored backlog intact (AppDirect 4/14·27, TD SYNNEX 3/31·18, AVANT 5/05·27, ScanSource 5/07·27, Bridgepointe 4/09·27, Expereo 3/10·12).

## 6. Tier 3 holds

None added. Canvas MSP signal-scan carryover queue remains empty. (Unrelated: today's R4 Flagged Consolidation added a TELESYSTEM review item to the canvas — telesystem.us, a managed-IT/UCaaS record in the Flagged-for-deletion pool. That is out of this scan's scope, sits in the Flagged pool [not MSP/Aggregator], and is an R4/Cooper review item, not a signal-scan carryover. Noted for awareness only; no action taken.)

## 7. QA gate drops with reasons

- **ScanSource — exec restructuring (M-B1, event 2026-03-16):** DROPPED for two independent reasons. (a) Tier-B freshness: 91 days old > 90-day Tier-B cutoff → freshness-drop (Tier B has no 90-180d band; only Tier A does). (b) Anti-churn: 3/16 is OLDER than the stored ScanSource signal (2026-05-07, score 27) and would not exceed score 27. Idempotent no-op either way.
- **Telarus — Telnyx joined the line card (M-A3, event 2026-02-10):** DROPPED. Score = Tier A (3) × Freshness (125 days → 90-180d band → 1) × Confidence (MED → 2) = **6, below the score-8 floor → silent drop.** Telarus is Cold (no stored signal) so anti-churn would permit a write, but the score does not clear the floor. Confidence held at MED because Telnyx's CPaaS / voice-AI lineage is borderline-adjacent to the excluded "CPaaS aggregator" category — a weak "carrier added" for MaiaEdge's connectivity thesis. The below-floor score makes the adjacency question moot (no escalation needed).
- **Megaport — Megaport Storage (M-B2, 6/03), On-ramp-as-a-Service (M-B2, 1/29), High-Speed Cross-Cloud Encryption (M-B2, 2/16):** DROPPED — out of segment. Megaport (193906531041) classifies as `customer_segment = Other` (competitor/reference, tier_3, Tim Z). The MSP scan writes only to MSP/Aggregator records. (Megaport platform launches are competitive-intel context, not an MSP signal.)
- **Console Connect — April 2026 ecosystem update / on-ramp + DC expansion (M-A3, ~4/30):** DROPPED — out of segment (Console Connect 193863998193 = `Other`, tier_5, Tim Z) AND LOW confidence (recurring monthly-cadence blog post, not a discrete named carrier add; month-level date only).
- **Anti-churn skips (already stored at equal-or-higher score, no newer in-window event found):** AppDirect (4/14/27), TD SYNNEX (3/31/18), AVANT (5/05/27), Bridgepointe (4/09/27), Expereo (3/10/12). All re-confirmed quiet since their stored event.

## 8. Failed writes

None (0 writes attempted).

## 9. Apollo budget post-run

Sub-cap 20, used 0 of 20. Weekly W25: 2/850 consumed (the 2 are Signal Scan Fiber's earlier-today new-account enrich attempts), 848 remaining. No tracker write required (0 consumption by this task).

## 10. IT MSP Test rejections (record-level)

- **Wavenet (Mitel Healthcare Partner of the Year, 6/11):** EXCLUDED — Wavenet is primarily a UK MSSP/managed-IT provider (FAIL IT MSP Test) + award-press (double exclusion).
- **Entire ChannelE2E June 08–12 People column** (Mitel, Armadin, Team Cymru, Sonatype/Casey Watson CRO, Hatz AI, iCOUNTER, IP Fabric): EXCLUDED — all cybersecurity/IT-MSP, none telecom/NaaS aggregators. Sonatype CRO is the only CRO-title hit but it's a software-supply-chain security vendor (FAIL).
- **Front × Intelisys/Sandler/Telarus (3/18):** EXCLUDED — Front is a CX/customer-ops software vendor, not a carrier/NaaS supplier (fails M-A3 "carrier added").
- **Out-of-segment (not IT-MSP, but wrong customer_segment for this scan):** Megaport (`Other`), Console Connect (`Other`), PCCW Global / PCCW (`Network Operator(Tier 1 / VNO)`), Epsilon Telecommunications (`Network Operator(Tier 1 / VNO)`). The NaaS-operator names in the catalog's "subtype 2" are classified in the live CRM as Network Operator or Other — HubSpot is source of truth, so they fall to the Network Op scan / competitive-intel, not here.

## 11. EMEA fallback flag

**Writable yield = 0 this week, but this is anti-churn-driven, NOT a source-coverage gap.** The Q1/Q2 TSD backlog the 180-day window first surfaced on 2026-06-08 is now stored; anti-churn correctly suppresses re-writes, and the channel is genuinely quiet on NEW in-window telecom-aggregator buying signals (ChannelE2E's freshest People column was entirely cybersecurity/IT-MSP). EMEA press was already in the primary rotation and was attempted; it surfaced only out-of-segment NaaS-operator moves.

Recommendations for next run (2026-06-22):
1. **Anchor the TSD careers pages directly** (Telarus/AppDirect/ScanSource/AVANT/Bridgepointe Greenhouse/Lever/Ashby boards) — the M-A6 job-board source is on a 3-week ✗ streak because search indexing doesn't surface ATS boards; a direct careers-page check or Apollo `organization_job_postings` would close the gap.
2. **Re-scan TD SYNNEX after its 2026-06-25 Q2 FY26 earnings** for a likely M-A7/M-B4 recurring-revenue-mix disclosure.
3. Keep EMEA channel press in the primary rotation while the 180-day window remains in effect.

---

### Footer

```
[MSP] target=480 matched=0 new=0 writes=0 heat_promotions=0 priority_48h=0 apollo=0/20 runtime=~12min audit=weekly-reports/2026-06-15/signal-scan/msp/
```

No Slack DM sent. Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs + canvas Run log + Cooper run report; it reads HubSpot for `last_signal_date = today` records. **This scan touched 0 MSP records today, so the aggregator will correctly see 0 MSP updates** — a true quiet-week zero, not a backdated-date visibility gap.
