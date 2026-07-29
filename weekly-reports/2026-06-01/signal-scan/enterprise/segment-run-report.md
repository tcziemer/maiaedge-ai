# Signal Scan — Enterprise (Multi-DC ICP) — Segment Run Report

## 1. Run header
- **Date (CT):** 2026-06-01 (Monday)
- **Segment:** Enterprise-CustomerSegment (4 sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services)
- **Detection window:** 2026-05-18 → 2026-06-01 (14 days rolling)
- **Apollo consumed:** 0 of 55 (effective budget min(55, 850 weekly remaining) = 55)
- **Runtime:** ~6 min
- **MCPs used:** HubSpot ✓, Slack (canvas read) ✓, web_search ✓, web_fetch (not required this run), Apollo (not consumed)
- **Verdict:** **QUIET in-window week.** 0 scored writes, 0 NEW accounts, 0 Apollo. Consistent with sibling Colo + NeoCloud scans (both QUIET, same window).
- **Prior Monday report (2026-05-25):** ABSENT → all 8 target records tagged NEW.

## 2. Source coverage (Source Coverage Mandate)
Search-anchor attempts across the Enterprise registry. ✓ = attempted/reachable, ✗ = not reached this run.

| # | Source | Tier | Status | Notes |
|---|---|---|---|---|
| 1 | StockTitan (SEC 8-K mirror) | Robust | ✓ | Via SEC EDGAR full-text anchor; no in-window material network/M&A 8-K for target list |
| 2 | SEC EDGAR full-text | Robust | ✓ | M&A 425/8-K hits = sub-scale community banks (Brookfield/NSTS 5/12, Bank First/PSB 5/19, Scotiabank/MapleMark 5/29); none in target pool, none clear scale gate |
| 3 | PR Newswire / Business Wire / GlobeNewswire | Robust | ✓ | No in-window network/connectivity trigger for target accounts |
| 4 | American Banker | Robust | ✗ | Not surfaced via anchor this run |
| 5 | Modern Healthcare | Robust | ✗ | Not surfaced this run |
| 6 | Becker's Hospital Review | Robust | ✓ | Via healthcare breach/IDN anchor; no in-window IDN DC / Epic go-live for target pool (Eli Lilly only Healthcare target) |
| 7 | Retail Dive | Robust | ✓ | Retail DC/automation items (Meijer/Kroger/Target) all pre-window |
| 8 | Nelson Hall | Robust (awareness) | ✗ | Subscription-gated; awareness-only |
| 9 | Everest Group | Robust | ✓ | BPO rankings/Cognizant FCC; no in-window delivery-center trigger |
| 10 | Greenhouse / Lever / Ashby job boards | Robust | ✗ | No E-B1 surge anchored this run |
| 11 | Apollo MCP (job postings/changes) | Robust | ✗ | Not invoked (no qualifying signal candidate; 0 credits) |
| 12 | Equinix newsroom / customer-story | Robust | ✓ | Fabric Intelligence general launch; no named Enterprise customer win in window |
| 13 | Megaport customer-success | Robust | ✓ | No in-window named Enterprise win |
| 14 | PacketFabric / Console Connect | Robust | ✗ | Not surfaced this run |
| 15 | HHS OCR / HIPAA Journal | Robust | ✓ | In-window healthcare breaches (Brockton 4/6 pre-window; UMMC Feb) not in target pool / out of window |
| 16 | NY DFS portal | Robust | ✓ | Part 500 cert deadline 4/15 (out of window); no in-window enforcement on target accounts |
| 17 | PCI Security Standards Council | Robust | ✓ | v4.0 in full enforcement; no discrete in-window event |
| 18 | DORA (EBA/ESMA/EIOPA) | Robust | ✓ | Ongoing enforcement; no discrete in-window CTPP/supervisory event for targets |
| 19 | NVIDIA Newsroom / Partner pages | Robust | ✓ | Lilly/NVIDIA AI team-up referenced at JPM26 (Jan, out of window); no in-window E-A3 for targets |
| 20 | Earnings transcripts (Seeking Alpha/Fool/MarketBeat/StockTitan) | Robust | ✓ | No in-window keyword trigger (network modernization / private connectivity / GenAI infra) for targets |
| 21 | Bloomberg AI/tech | Medium | ✓ | Meta DC financing led by JPM/Morgan Stanley (5/4, pre-window; advisory role, not network-buyer signal) |
| 22 | WSJ / CIO Journal | Medium | ✗ | Not surfaced this run |
| 23 | Risk & Insurance / ISMG GovInfoSecurity | Medium | ✗ | Not surfaced this run |
| 24 | CIO.com / InformationWeek | Medium | ✓ | JPMorgan infra-chief AI compute strategy piece (undated/evergreen); not an in-window discrete event |
| 25 | Bisnow Data Center | Medium | ✗ | Not surfaced this run |
| 26 | Data Center Frontier / DCD | Medium | ✓ | JPMorgan $5T AI-infra spend research note (macro, not account trigger) |
| 27 | Mergermarket / S&P Global MI | Medium | ✗ | Not surfaced this run |
| 28 | PitchBook public | Medium | ✓ | Cognizant profile; no in-window deal trigger |
| 29 | Crunchbase News | Medium | ✗ | Not surfaced this run |
| 30 | HIMSS Media / CHIME | Medium | ✗ | Not surfaced this run |
| 31 | RIS News / STORES | Medium | ✗ | Not surfaced this run |
| 32 | Conference agenda pages (Sibos/Money20/20/HIMSS/NRF/CCW/NASSCOM) | Medium (context) | ✗ | Not surfaced this run |
| 33 | Cross-segment exec-hire stack | Medium | ✓ | No in-window VP/Director Network Infrastructure hire for target accounts |
| INTL | EMEA/APAC/LATAM supplement | Intl | ✓ (partial) | Santander UK 6-K (5/1, out of window, TSB-related not network); no in-window APAC/LATAM Enterprise trigger |

**3-week ✗ streak watch:** sources 4, 8, 10, 14, 22, 23, 25, 27, 29, 30, 31, 32 not reached this run. First-occurrence flag for most (this is the first per-segment Enterprise scan with a saved report — no prior baseline). Monitor next 2 Mondays; auto-flag at 3-week streak.

## 3. Candidate funnel
| Stage | Count |
|---|---|
| Target list (Enterprise tier 1-3, type!=Customer, excl. MaiaEdge own) | 8 |
| In-window signal candidates detected | 0 |
| Matched to target accounts | 0 |
| NEW account candidates (signal-derived) | 0 |
| NEW accounts created | 0 |
| Total HubSpot writes | 0 |
| QA-gate drops | 0 |

## 4. Hard-gate rejections
None — no NEW signal-derived candidates entered the gate this run. (Note: today's separate account-sourcing run posted Enterprise net-new candidates to canvas F0B0AFSB9LN for Cooper review — HCA Healthcare, CommonSpirit, Mayo Clinic, Ascension, Cleveland Clinic, Kroger, Target, Home Depot, Genpact, Teleperformance. Those are sourcing-pipeline candidates, NOT signal matches, and are out of scope for this scan. Not actioned here.)

## 5. Score distribution
| Band | Count |
|---|---|
| 8-11 (LIGHT) | 0 |
| 12-17 (Worth Reviewing) | 0 |
| 18-26 (Strong) | 0 |
| 27+ (Highest) | 0 |

## 6. Writes summary per record
None. 0 writes this run.

**Note on TD (198403706563, Financial Services, tier_2, Tim Z):** carries a pre-existing in-window signal — `last_signal_date = 2026-05-21`, `last_signal_score = 27`, `signal_heat = Warm` (E-A3 AI/GPU: TD agentic AI mortgage/HELOC pre-adjudication, Layer 6). Written by a prior run; still current and in-window. No new detection this run → no re-write (avoids double-count per QA rule 8). Narrative retains a legacy code-prefix format; not modified here (retroactive prefix cleanup is the out-of-scope optional one-time backfill, not a signal-scan action).

## 7. Tier 3 holds (carryover)
No Enterprise-tagged signal-scan Tier 3 carryovers in canvas F0B0AFSB9LN. Standing canvas Tier 3 holds are R0/R1/R3 scope (gatco, columbus-networks, Verizon dedup) — not this segment. Nothing to re-append.

## 8. QA gate drops
None (0 candidates reached the gate).

## 9. Failed writes
None.

## 10. Apollo budget post-run
- Sub-cap: 55/run. Consumed this run: **0**.
- Weekly W22 (week_start 2026-05-25): 0/850 before run, **0/850 after run**. No tracker write needed (zero consumption).

## 11. Sub-segment volume breakdown (target pool of 8)
| Sub-segment | Target records | In-window writes |
|---|---|---|
| Financial Services - Enterprise | 6 (JPMorgan Chase, J.P. Morgan & Co., Banco Santander, Worldpay, TD, Citi) | 0 |
| Healthcare Systems - Enterprise | 1 (Eli Lilly) | 0 |
| Retail and Distribution - Enterprise | 1 (Meijer — anchor) | 0 |
| Outsourcing Services - Enterprise | 0 in CRM | 0 |

Financial Services dominates the active Enterprise pool (6/8). Healthcare and Retail each carry a single anchor; Outsourcing has no CRM record yet (sourcing-pipeline candidates Genpact/Teleperformance pending Cooper review on canvas).

---

**End of run. No rep DMs, no canvas Run log, no Cooper run report — aggregator (signal-scan-aggregator, Mon 2:30pm CT) owns all three.**

```
[Enterprise] target=8 matched=0 new=0 writes=0 heat_promotions=0 gate_rejections=0 apollo=0/55 runtime=~6min audit=weekly-reports/2026-06-01/signal-scan/enterprise/
```
