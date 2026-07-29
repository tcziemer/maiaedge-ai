# Signal Scan — Enterprise (Multi-DC ICP) — Segment Run Report

## 1. Run header
- **Date (CT):** 2026-06-08 (Monday)
- **Segment:** Enterprise-CustomerSegment (4 sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services)
- **Detection window:** **180 days rolling** (event date >= 2025-12-10) — first Enterprise scan under the 2026-06-04 window widening (was 14d)
- **Scope:** all tiers, non-Flagged (tier filter removed 2026-06-04)
- **Apollo consumed:** 0 of 55 (effective budget min(55, 850 weekly remaining W24) = 55; no NEW-account creation → no Apollo)
- **Runtime:** ~9 min
- **MCPs used:** HubSpot ✓, Slack (canvas read — no Enterprise carryovers) ✓, web_search ✓, web_fetch (not required), Apollo (not consumed)
- **Verdict:** **3 scored writes** (Worldpay, Eli Lilly, Optum) — the 180-day window surfaced the in-window M&A/AI-infra backlog the prior 14-day window discarded. 0 NEW accounts, 0 Apollo, 0 backlog overflow.
- **Prior Monday report (2026-06-01):** present → records present then tagged CARRIED; 6 records added since (Blue Cross NC, T-Systems Brasil, T-Systems Iberia, HCL, Optum, plus J.P. Morgan & Co. already present) tagged NEW-to-pool.

## 2. Source coverage (Source Coverage Mandate)
Search-anchor attempts across the Enterprise registry. ✓ = attempted/reachable, ✗ = not reached this run.

| # | Source | Tier | Status | Notes |
|---|---|---|---|---|
| 1 | StockTitan / SEC 8-K mirror | Robust | ✓ | Global Payments 8-K (Worldpay close pro-formas), UHG Q1 2026 8-K, Citigroup FWP series surfaced via EDGAR anchor |
| 2 | SEC EDGAR full-text | Robust | ✓ | UNH 8-K Q1 2026 earnings release; GPN Worldpay close exhibits |
| 3 | PR Newswire / Business Wire / GlobeNewswire | Robust | ✓ | PRNewswire "GTCR Completes Sale of Worldpay to Global Payments" (E-A2 close confirm) |
| 4 | American Banker | Robust | ✓ | "Global Payments closes Worldpay purchase, issuer sale to FIS" (E-A2 cross-source) |
| 5 | Modern Healthcare | Robust | ✓ | Blue Cross NC / Horizon holding-company restructuring coverage (2025, out of window) |
| 6 | Becker's Hospital Review | Robust | ✓ | "UnitedHealth is spending $1.5B on AI this year" (E-A3 cross-source) + BCBS-NC CuraCor restructuring |
| 7 | Retail Dive | Robust | ✓ | Meijer/Dematic micro-fulfillment + WITRON automated DC — no fresh in-window dated trigger |
| 8 | Nelson Hall | Robust (awareness) | ✗ | Subscription-gated; awareness-only |
| 9 | Everest Group | Robust | ✗ | Not surfaced this run |
| 10 | Greenhouse / Lever / Ashby job boards | Robust | ✗ | No E-B1 senior-network-role surge anchored this run |
| 11 | Apollo MCP (job postings/changes) | Robust | ✗ | Not invoked (no NEW-account candidate; 0 credits) |
| 12 | Equinix newsroom / customer-story | Robust | ✗ | Not surfaced this run |
| 13 | Megaport customer-success | Robust | ✗ | Not surfaced this run |
| 14 | PacketFabric / Console Connect | Robust | ✗ | Not surfaced this run |
| 15 | HHS OCR / HIPAA Journal | Robust | ✓ | No in-window target-pool breach trigger |
| 16 | NY DFS portal | Robust | ✓ | No in-window enforcement on target accounts |
| 17 | PCI Security Standards Council | Robust | ✓ | v4.0 in full enforcement; no discrete in-window event |
| 18 | DORA (EBA/ESMA/EIOPA) | Robust | ✓ | Ongoing oversight; no discrete in-window CTPP event for targets |
| 19 | NVIDIA Newsroom / Partner pages | Robust | ✓ | Lilly LillyPod (E-A3), HCLTech Physical AI Lab (Nov 17 2025, OUT of window) |
| 20 | Earnings transcripts (Seeking Alpha/Fool/MarketBeat/StockTitan) | Robust | ✓ | UNH Q1 2026 call (E-A3); Santander ONE/Gravity 2.0 (no crisp in-window dated trigger) |
| 21 | Bloomberg AI/tech | Medium | ✗ | Not surfaced this run |
| 22 | WSJ / CIO Journal | Medium | ✗ | Not surfaced this run |
| 23 | Risk & Insurance / ISMG GovInfoSecurity | Medium | ✗ | Not surfaced this run |
| 24 | CIO.com / InformationWeek | Medium | ✓ | JPMorgan infra-chief AI piece (evergreen, no discrete in-window date) |
| 25 | Bisnow Data Center | Medium | ✗ | Not surfaced this run |
| 26 | Data Center Frontier / DCD | Medium | ✓ | JPMorgan $5T AI-infra research note (macro/analyst, not account trigger) |
| 27 | Mergermarket / S&P Global MI | Medium | ✗ | Not surfaced this run |
| 28 | PitchBook public | Medium | ✗ | Not surfaced this run |
| 29 | Crunchbase News | Medium | ✗ | Not surfaced this run |
| 30 | HIMSS Media / CHIME | Medium | ✗ | Not surfaced this run |
| 31 | RIS News / STORES | Medium | ✗ | Not surfaced this run |
| 32 | Conference agenda pages | Medium (context) | ✗ | Not surfaced this run |
| 33 | Cross-segment exec-hire stack | Medium | ✓ | No in-window VP/Director Network Infrastructure hire for target accounts |
| INTL | EMEA/APAC/LATAM supplement | Intl | ✓ (partial) | Santander OpenAI (Aug 2025 core, out of window); HCL Finergic tuck-in (minor); T-Systems Iberia Barcelona region (Feb 2024, out of window) |

**3-week ✗ streak watch:** sources 8, 9, 10, 11, 12, 13, 14, 21, 22, 23, 25, 27, 28, 29, 30, 31, 32 not reached this run. 2026-06-01 also missed 8/10/14/22/23/25/27/29/30/31/32. Sources **8, 10, 14, 22, 23, 25, 27, 29, 30, 31, 32** are now on a 2-week ✗ streak — auto-flag if missed again 2026-06-15.

## 3. Candidate funnel
| Stage | Count |
|---|---|
| Target list (Enterprise, all tiers, type!=Customer, excl. MaiaEdge own) | 13 |
| In-window signal candidates detected (>=8 after scoring) | 3 |
| Matched to target accounts | 3 |
| NEW account candidates (signal-derived) | 0 |
| NEW accounts created | 0 |
| Total HubSpot writes | 3 |
| Anti-churn skips | 2 (TD, Citi — already hold newer/higher signals) |
| QA-gate drops | 0 |
| Detected-but-not-written (out-of-window / below-materiality) | 4 (see §4) |

## 4. Hard-gate rejections + detected-but-not-written
No NEW signal-derived candidates entered the hard sourcing gate (0 NEW). Detected-but-not-written existing-account items:

| Account | Detected item | Why not written |
|---|---|---|
| HCL Technologies (326171164408) | NVIDIA Physical AI Lab (E-A3) | Event 2025-11-17 — OUTSIDE 180-day window (cutoff 2025-12-10). Finergic Solutions tuck-in (Mar 2026, E-A2) is below materiality for a connectivity trigger (minor consulting acquisition). recent_news already documents both. Held. |
| Banco Santander (324617947897) | OpenAI "AI-native bank" (E-A3) | Core OpenAI partnership announced ~Aug 2025 — OUTSIDE window. Gravity 2.0 / Brazil-onto-Gravity 2026 migration lacks a crisp in-window dated trigger. Held (no generic non-dated write). |
| JPMorgan Chase (324628785885) + J.P. Morgan & Co. (240446137023) | AI-infra / 500th-app decommission Q1 2026 | Evergreen AI-infra coverage, no discrete dated network/connectivity event (consistent with 2026-06-01 assessment). Dup pair (R3 merge pending) — avoids double-write. Held. |
| Blue Cross NC (326350146243) | CuraCor restructuring + voluntary buyouts | CuraCor holding-co restructure was 2025 (out of window). 2026 voluntary buyouts / ~$497M net loss = budget contraction, not a positive network-buyer trigger. Held. |
| Meijer (324001628912) | Dematic micro-fulfillment / WITRON DC automation | No fresh in-window dated discrete trigger; existing items pre-window. Anchor account (active MaiaEdge design) but no scoreable scan signal this run. Held. |
| T-Systems Brasil/Iberia (326188915439 / 326176546504) | Subsidiary-level | No in-window discrete subsidiary trigger; parent-level T-Systems news not subsidiary-specific. Held. |

## 5. Score distribution
| Band | Count | Accounts |
|---|---|---|
| 8-11 (LIGHT) | 2 | Worldpay (9), Eli Lilly (9) |
| 12-17 (Worth Reviewing) | 0 | — |
| 18-26 (Strong) | 1 | Optum (18) |
| 27+ (Highest) | 0 | — |

## 6. Writes summary per record
| ID | Name | Sub-segment | Signal | Event date | Score calc | Score | Heat delta | Tier delta | Owner |
|---|---|---|---|---|---|---|---|---|---|
| 321479592663 | Worldpay | Financial Services | E-A2 M&A close (Global Payments completed $24.3B Worldpay acquisition from FIS/GTCR) | 2026-01-12 | A(3)×Fr1(90-180d)×HIGH(3) | 9 | Cold→Cool | none (tier_3, Cool fires no modifier) | Tim Lieto (OH=East) |
| 322677223115 | Eli Lilly | Healthcare Systems | E-A3 AI/GPU (LillyPod NVIDIA DGX SuperPOD AI factory, 1,016 Blackwell Ultra GPUs, go-live) | 2026-02-27 | A(3)×Fr1(90-180d)×HIGH(3) | 9 | Cold→Cool | none (tier_3) | Tim Lieto (IN=East) |
| 325636927166 | Optum | Healthcare Systems | E-A3 AI/GPU ($1.5B 2026 AI investment, OptumInsight AI-first platform transition, Q1 call) | 2026-04-22 | A(3)×Fr3(<=60d)×MED(2) | 18 | Cold→Cool | none (tier_3) | Tim Lieto (MN=East) |

**Field set per write:** `recent_news_or_trigger_event` (pure prose, no date prefix), `last_signal_date` (event date), `last_signal_score`, `signal_count_last_30d` = 0 (all events >30d old), `signal_heat`. **No `account_tier` write** (all 3 compute idempotent — Cool signal fires no tier modifier; base tier_3 unchanged; none carry `hs_is_target_account`). **No `last_enriched_date` bump** (partial signal write).

**Classification note (Optum):** the $1.5B AI investment was classified E-A3 (AI/GPU workload) at MED confidence (no named GPU partner; AI-first platform transition). Defensible over E-C2 earnings-mention (Tier C would score 6 and drop) because it is a discrete, dated, dollar-specific AI-infrastructure program with named platform transition (OptumInsight legacy→AI-first), not a passing transcript remark. Distinguished from JPMorgan's evergreen AI-infra coverage (held) by the discrete dated disclosure.

## 7. Tier 3 holds (carryover)
No Enterprise-tagged signal-scan Tier 3 carryovers in canvas F0B0AFSB9LN. Standing canvas holds (gatco, columbus-networks, Verizon/NTT/SoftBank dedup stubs) are R0/R1/R3 scope — not this segment. Nothing to re-append.

## 8. QA gate drops
None. All 3 scored hits passed the 10-rule gate (source verified, freshness <=180d, scale gate confirmed $1B+ multi-DC, narrative <=250 chars, owner mapping East, pure prose / no prefix / no em dash / no competitor names, score arithmetic, no dedup collision, no NEW/CARRIED integrity issue).

## 9. Failed writes
None. HubSpot batch 3/3 updated, 0 failed.

## 10. Apollo budget post-run
- Sub-cap: 55/run. Consumed this run: **0** (no NEW-account creation; matched-account writes are Apollo-free).
- Weekly W24 (week_start 2026-06-08): 0/850 before run, **0/850 after run**. No tracker write needed (zero consumption).

## 11. Sub-segment volume breakdown (target pool of 13)
| Sub-segment | Target records | In-window writes |
|---|---|---|
| Financial Services - Enterprise | 7 (JPMorgan Chase, J.P. Morgan & Co., Banco Santander, Worldpay, TD, Citi, Blue Cross NC) | 1 (Worldpay) |
| Healthcare Systems - Enterprise | 3 (Eli Lilly, Optum, [Blue Cross NC tagged FinSvcs]) | 2 (Eli Lilly, Optum) |
| Retail and Distribution - Enterprise | 1 (Meijer — anchor) | 0 |
| Outsourcing Services - Enterprise | 3 (HCL Technologies, T-Systems Brasil, T-Systems Iberia) | 0 |

Pool grew 8 → 13 since 2026-06-01 (R1/R2 + R7 sourcing net-new: Optum, HCL, T-Systems Brasil, T-Systems Iberia, Blue Cross NC). Financial Services still the largest active sub-segment (7/13). Healthcare now the strongest signal producer this run (2/3 writes). Outsourcing has 3 CRM records but produced 0 in-window writes (HCL marquee signal out of window).

---

**End of run. No rep DMs, no canvas Run log, no Cooper run report — aggregator (signal-scan-aggregator, Mon 2:30pm CT) owns all three.**

```
[Enterprise] target=13 matched=3 new=0 writes=3 heat_promotions=3 gate_rejections=0 apollo=0/55 runtime=~9min audit=weekly-reports/2026-06-08/signal-scan/enterprise/
```
