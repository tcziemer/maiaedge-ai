# Signal Scan — Enterprise (Multi-DC ICP) — Segment Run Report

## 1. Run header
- **Date (CT):** 2026-06-15 (Monday)
- **Segment:** Enterprise-CustomerSegment (4 sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services)
- **Detection window:** **180 days rolling** (event date >= 2025-12-17)
- **Scope:** all tiers, non-Flagged (no tier filter), type != Customer, excl. MaiaEdge own (124293230301)
- **Apollo consumed:** 0 of 55 (effective budget = min(55, 848 weekly remaining W25) = 55; no NEW-account creation -> 0 Apollo)
- **Runtime:** ~14 min
- **MCPs used:** HubSpot ✓, Slack (canvas read ✓ — no Enterprise carryovers), web_search ✓ (sub-agent fan-out), web_fetch ✓, Apollo (health-checked, 0 consumed)
- **Verdict:** **1 scored write** (HCL Technologies, E-A2). Quiet week — 11 of 16 accounts had no in-window signal; 4 had nothing newer than stored; 1 fresh write. 0 NEW accounts, 0 Apollo, 0 backlog overflow.
- **Prior Monday report (2026-06-08):** present -> records present then tagged CARRIED. Pool grew 13 -> 16 since 06-08 (R1/R7 net-new: Swiss Re, Swiss Life, FPT Software added; J.P. Morgan & Co. already present).
- **Context-budget safeguard:** signal detection fanned out across 5 research sub-agents (4 account-anchored + 1 source-sweep/NEW-candidate) so raw source text stayed out of the main context. Single matched write; no batching or overflow backlog required.

## 2. Source coverage (Source Coverage Mandate)
Search-anchor attempts across the Enterprise registry. ✓ = attempted/reachable, ✗ = not reached this run.

| # | Source | Tier | Status | Notes |
|---|---|---|---|---|
| 1 | StockTitan / SEC 8-K mirror | Robust | ✓ | UNH Q1'26 8-K, Global Payments 8-K/10-Q surfaced via EDGAR anchor |
| 2 | SEC EDGAR full-text | Robust | ✓ | GPN/UNH filings; JPM 10-Q references |
| 3 | PR Newswire / Business Wire / GlobeNewswire | Robust | ✓ | HCLTech-HPE Telco PR (E-A2); GPN/Worldpay close exhibits |
| 4 | American Banker | Robust | ✓ | Citi-Google (confirmed OLD, Oct-2024); no in-window target trigger |
| 5 | Modern Healthcare | Robust | ✗ | Fierce Healthcare + DistilINFO reached as equivalents; Modern Healthcare not specifically anchored |
| 6 | Becker's Hospital Review | Robust | ✗ | Fierce Healthcare reached as equivalent; Becker's not specifically anchored |
| 7 | Retail Dive | Robust | ✗ | Grocery Dive / Progressive Grocer / Supermarket News reached as equivalents (Meijer) |
| 8 | Nelson Hall | Robust (awareness) | ✗ | Subscription-gated; **3-week ✗ streak** |
| 9 | Everest Group | Robust | ✗ | Not surfaced this run |
| 10 | Greenhouse / Lever / Ashby job boards | Robust | ✗ | No company-specific E-B1 surge isolated; **3-week ✗ streak** |
| 11 | Apollo MCP (job postings/changes) | Robust | ✗ | Not invoked (0 NEW-account creates; 0 credits) |
| 12 | Equinix newsroom / customer-story | Robust | ✓ | 2026 enterprise-AI/Fabric posts + 500K-interconnections milestone; no NEW in-window named-enterprise win |
| 13 | Megaport customer-success | Robust | ✓ | No in-window NEW enterprise win (Citi item = shareholder exit, unrelated) |
| 14 | PacketFabric / Console Connect | Robust | ✗ | Not individually reached; **3-week ✗ streak** |
| 15 | HHS OCR / HIPAA Journal | Robust | ✓ | March-2026 recap: NYC H+H 1.8M breach (NEW candidate); no in-window target-pool breach |
| 16 | NY DFS portal | Robust | ✓ | Part 500 landscape checked (Debevoise/Baker McKenzie); only 2026 action was Delta Dental — no target named |
| 17 | PCI Security Standards Council | Robust | ✓ | v4.0.1 in force; no discrete in-window account event |
| 18 | DORA (EBA/ESMA/EIOPA) | Robust | ✓ | First CTPP list (Nov-18-2025) designates ICT vendors, not Enterprise buyers; no E-A5 on targets |
| 19 | NVIDIA Newsroom / Partner pages | Robust | ✓ | GTC-2026 enterprise partners are infra vendors (Oracle/HPE/Cisco/Dell), not qualifying end-buyers |
| 20 | Earnings transcripts | Robust | ✓ | UNH Q1'26 (Optum, = stored), Santander Q1'26, GPN Q1'26, JPM Q1'26 |
| 21 | Bloomberg AI/tech | Medium | ✗ | Not surfaced this run |
| 22 | WSJ / CIO Journal | Medium | ✓ | CIO Dive reached (Citi-Google migration confirmed OLD) — streak broken |
| 23 | Risk & Insurance / ISMG GovInfoSecurity | Medium | ✗ | Not reached; **3-week ✗ streak** |
| 24 | CIO.com / InformationWeek | Medium | ✓ | CIO Dive coverage |
| 25 | Bisnow Data Center | Medium | ✓ | DC capital-markets items operator/REIT-side (DataBank securitization); no NEW enterprise tenant — streak broken |
| 26 | Data Center Frontier / DCD | Medium | ✓ | DCD reached (T-Systems verification) |
| 27 | Mergermarket / S&P Global MI | Medium | ✓ | M&A-wire sweep (Capgemini-WNS closed Oct-25; C&S-SpartanNash) — streak broken |
| 28 | PitchBook public | Medium | ✗ | Not surfaced this run |
| 29 | Crunchbase News | Medium | ✓ | Exec-move sweep (S&P Global CTO) — streak broken |
| 30 | HIMSS Media / CHIME | Medium | ✗ | Not reached; **3-week ✗ streak** |
| 31 | RIS News / STORES | Medium | ✗ | Not reached; **3-week ✗ streak** |
| 32 | Conference agenda pages | Medium (context) | ✗ | Not reached; **3-week ✗ streak** |
| 33 | Cross-segment exec-hire stack | Medium | ✓ | S&P Global CTO 2026-03-31 (NEW candidate); no VP/Director Network hire on target pool |
| INTL | EMEA/APAC/LATAM supplement | Intl | ✓ (partial) | Santander Gravity (Brazil 2026), HCLTech-HPE (39 countries), T-Systems Brasil/Iberia, FPT (Vietnam) all checked |

**3-week ✗ streak AUTO-FLAG (missed 06-01, 06-08, 06-15):** sources **8 (Nelson Hall), 10 (Greenhouse/Lever/Ashby job boards), 14 (PacketFabric/Console Connect), 23 (Risk & Insurance/ISMG), 30 (HIMSS/CHIME), 31 (RIS News/STORES), 32 (conference agendas)** now on a confirmed 3-week miss. Several are subscription-gated (Nelson Hall) or need per-company search anchors (job boards). **Recommend source-development pass.** Streaks BROKEN this run: 22 (WSJ/CIO Journal), 25 (Bisnow), 27 (Mergermarket), 29 (Crunchbase).

## 3. Candidate funnel
| Stage | Count |
|---|---|
| Target list (Enterprise, all tiers, type!=Customer, excl. MaiaEdge own) | 16 |
| In-window signal candidates scored >=8 | 1 |
| Matched to target accounts | 1 |
| NEW account candidates (signal-derived) | 0 |
| NEW accounts created | 0 |
| Total HubSpot writes | 1 |
| Anti-churn skips | 4 (TD, Citi, Optum, Eli Lilly — hold newer/equal-or-higher stored) |
| Below-floor / no-fresh-event drops | 3 (Santander, Worldpay, JPMorgan) |
| QA-gate drops | 0 |

## 4. Hard-gate rejections + detected-but-not-written
No signal-derived NEW candidates entered the hard sourcing gate (0 signal-derived NEW). Detected items not written:

| Account | Detected item | E-code | Why not written |
|---|---|---|---|
| Banco Santander (324617947897) | Q1'26 earnings: Gravity cloud core "ready for Brazil rollout 2026" + global platform deployment, Payments 4B txns | E-C2 | Tier C (1) x MED (2) caps at score 6 < floor 8 even at max freshness. Forward-looking earnings statement, no named connectivity contract. Consistent with 06-08 hold. The Santander Mexico Gravity 100%-migration (2025-11-18) is ~1 month pre-window. |
| Worldpay (321479592663) | Global Payments Q1'26 call advances combined-entity platform/cloud migration (Genius) | E-C2 | Score 6 < floor; and it restates the SAME integration captured by the stored stronger E-A2 M&A-close signal (2026-01-12, score 9). Stored signal retained; no churn. |
| JPMorgan Chase (324628785885) | ~$1B Orangeburg NY data center build (completion 2028) surfaced via Apr-2026 tax-break coverage | E-A1 (LOW) | The real corporate trigger (subsidy approval) is Feb-2024 (out of window); Apr-2026 is investigative press coverage of the old deal, not a fresh milestone. Fails event-date integrity. JPM's DC-financing headlines (Vantage/Abilene) are lender deals, not own-network. Also a dup pair w/ J.P. Morgan & Co. (R3 merge pending). Held. |
| TD (198403706563) | Q2 results (May-28) + TD Insurance chatbot (May-1, product launch excluded) | — | Nothing newer/higher than stored 2026-05-21 score-27 (Layer 6 agentic AI). Anti-churn skip. |
| Citi (198431710965) | Citi/Google migration recirculated by DCD | — | That is 2024 news; nothing newer than stored 2026-04-22 score-27 (Citi Sky). Anti-churn skip. |
| Optum (325636927166) | UHG Q1'26 ~$1.5B AI / OptumInsight AI-first | — | Byte-for-byte the stored 2026-04-22 score-18 signal. Anti-churn skip. |
| Eli Lilly (322677223115) | $4.5B Indiana manufacturing/genetic-medicine facility (2026-05-06) | — | Excluded per noise list (manufacturing-plant expansion). LillyPod = stored 2026-02-27. Anti-churn skip. |
| Meijer (324001628912) | No fresh in-window DC/automation/network trigger | — | Anchor account; all DC-automation items pre-window. No scoreable scan signal. Held. (Data-quality note in §11.) |
| Swiss Re / Swiss Life / Blue Cross NC / FPT Software / T-Systems Brasil / T-Systems Iberia | — | — | No in-window material connectivity/DC/exec-hire/regulatory signal. (Swiss Life TELIS Gruppe M&A and FPT Flezi Foundry are non-network / AI-tooling -> excluded.) |

## 5. Score distribution
| Band | Count | Accounts |
|---|---|---|
| 8-11 (LIGHT) | 1 | HCL Technologies (9) |
| 12-17 (Worth Reviewing) | 0 | — |
| 18-26 (Strong) | 0 | — |
| 27+ (Highest) | 0 | — |

## 6. Writes summary per record
| ID | Name | Sub-segment | Signal | Event date | Score calc | Score | Heat delta | Tier delta | Owner |
|---|---|---|---|---|---|---|---|---|---|
| 326171164408 | HCL Technologies | Outsourcing Services | E-A2 M&A announcement (HCLTech to acquire HPE Telco Solutions, up to $160M, ~1,500 specialists / 39 countries / OSS + 5G IP) | 2025-12-18 | A(3) x Fr1(90-180d, 179d) x HIGH(3) | 9 | Cold -> Cool | none (tier_3; signal-derived modifiers do not fire at score 9) | Tim Ziemer (International) |

**Field set written:** `recent_news_or_trigger_event` (pure prose, no date prefix), `last_signal_date` = 2025-12-18 (event date), `last_signal_score` = 9, `signal_count_last_30d` = 0 (event >30d old), `signal_heat` = Cool. **No `account_tier` write** (base Outsourcing-Enterprise = tier_3; hot/white-hot/stacked modifiers do not fire at score 9; stale/open-deal drift is R-Tier-Audit's daily job — verified 0 open deals). **No `last_enriched_date` bump** (partial signal write; stays 2026-06-08). Read-back verified post-write.

**Classification note (HCL):** the HPE Telco Solutions deal was MISSED by the 06-08 scan (which focused on the out-of-window NVIDIA Physical AI Lab + sub-materiality Finergic tuck-in). The deal announcement (2025-12-18) is genuinely in-window (179d, barely inside the 180-day edge) and is a delivery-footprint M&A (1,500 staff, 39 countries) — a legitimate Outsourcing-Enterprise E-A2. The catalog's per-signal ">90d drop" freshness line for E-A2 predates the 2026-06-04 window widening; the governing Tier A ladder (90-180d x1) applies, matching the 06-08 precedent that scored Worldpay's 147-day-old M&A close at freshness 1.

## 7. Tier 3 holds (carryover)
No Enterprise-tagged signal-scan Tier 3 carryovers in canvas F0B0AFSB9LN. The only Enterprise-flagged canvas hold is General Motors (Manufacturing -> Watch List, already self-resolved to Other tier_5) — R1/R4 framework scope, not this segment. Standing canvas holds (gatco, columbus-networks, NTT/SoftBank/Telstra dedup stubs, ICE Enterprise-vs-Colo, MMR Fiber) are R0/R1/R2/R3/Cooper scope. Nothing to re-append.

## 8. QA gate drops
None. The single scored hit (HCL) passed all 10 rules: (1) source verified across HCLTech PR + PRNewswire + RCR Wireless + telecoms.com; (2) event 179d within 180-day window -> computes Cool; (3) segment Enterprise/Outsourcing + scale gate confirmed ($13B+ revenue, Facilities Enterprise 50+, in-house delivery network 39+ countries); (4) narrative 228 chars <= 250; (5) owner Tim Z = International; (6) pure prose, no prefix/tag, no em dashes, HPE is the M&A counterparty not a connectivity competitor; (7) score arithmetic A(3)xFr1xHIGH(3)=9, no bonus (single non-stacked signal); (8) no dedup collision; (9) HCL is CARRIED (in pool 06-08), new signal on carried account; (10) pure-prose narrative.

## 9. Failed writes
None. HubSpot batch 1/1 updated, 0 failed. Read-back confirmed all 5 fields landed.

## 10. Apollo budget post-run
- Sub-cap: 55/run. Consumed this run: **0** (no NEW-account creation; matched-account writes are Apollo-free).
- Weekly W25 (week_start 2026-06-15): 2/850 before run (Signal Scan Fiber 8:30am), **2/850 after run**. No tracker write needed (zero consumption; avoids concurrent-write truncation risk noted in prior incidents).

## 11. Sub-segment volume breakdown (target pool of 16)
| Sub-segment | Target records | In-window writes |
|---|---|---|
| Financial Services - Enterprise | 9 (Swiss Re, Swiss Life, Blue Cross NC [tagged FinSvc], JPMorgan Chase, J.P. Morgan & Co., Banco Santander, Worldpay, TD, Citi) | 0 |
| Healthcare Systems - Enterprise | 2 (Optum, Eli Lilly) | 0 |
| Retail and Distribution - Enterprise | 1 (Meijer — anchor) | 0 |
| Outsourcing Services - Enterprise | 4 (FPT Software, T-Systems Brasil, T-Systems Iberia, HCL Technologies) | 1 (HCL) |

Pool grew 13 -> 16 since 06-08. Financial Services remains the largest active sub-segment (9/16) but produced 0 writes (TD/Citi recently saturated; the rest no fresh trigger). Outsourcing produced the only write this run (HCL HPE deal). The Enterprise pool is heavily FinSvc-weighted; Healthcare (2), Retail (1), Outsourcing (4) remain thin — R7 sourcing is the growth lever (06-01 R7 surfaced 14 net-new Enterprise candidates incl. HCA / CommonSpirit / Mayo / Ascension / Cleveland Clinic / Kroger / Target / Home Depot / Genpact / Teleperformance not yet all in CRM).

## 12. NEW gate-passing candidates — sourcing hand-offs (NOT created)
Two not-in-CRM companies surfaced by the source sweep pass BOTH hard gates but carry NO scoreable signal-scan E-code signal, so they were NOT created via this scan (creating accounts without a scoreable signal is R7/account-sourcing's job; preserves the 0-Apollo discipline). Logged here for R7 / account-sourcing:

| Candidate | Domain | Proposed sub-segment | Scale evidence | Why not a scan create |
|---|---|---|---|---|
| S&P Global | spglobal.com | Financial Services - Enterprise | ~$14.2B revenue; Equinix NY4 proximity hosting (NYSE/NASDAQ/CBOE hub); unified global enterprise tech org | In-window item is a CTO / Chief Technology Transformation Officer hire (2026-03-31) — not an E-A4 network-role hire; no scoreable signal. HIGH gate-pass confidence. |
| NYC Health + Hospitals | nychealthandhospitals.org | Healthcare Systems - Enterprise | ~$11B operating budget; 2 consolidated corporate DCs + 24/7 NOC + in-house net eng across 11 hospitals | In-window item is the company's OWN breach (March-2026, 1.8M records) — not a clean positive E-code (E-B2 is peer-breach, segment-wide). MEDIUM gate-pass; public-benefit-corp nuance (reads as Healthcare IDN, not a govt regulator). |

## 13. Data-quality notes (for Cooper / backfill — not acted on this run)
- **Meijer (324001628912)** — `recent_news_or_trigger_event` carries a legacy `[2026-05-22]:` date prefix and has NO structured `last_signal_date`. Legacy pre-2026-05-28 format; eligible for the one-time Signal Engine Backfill. Not touched this run (no new signal; anti-churn / no-overwrite).
- **JPMorgan Chase (324628785885) + J.P. Morgan & Co. (240446137023)** — duplicate pair, R3 merge pending (flagged 06-08 too).
- **Blue Cross NC (326350146243)** — tagged `Financial Services - Enterprise`; it is a health insurer and arguably `Healthcare Systems - Enterprise`. Not reclassified in a signal scan; flag for R-Tier-Audit / Cooper.
- **Intercontinental Exchange (311326703342)** — R2/Cooper Enterprise-vs-Colo disambiguation hold (currently Other segment, not in this pool) — awareness only.

---

**End of run. No rep DMs, no canvas Run log, no Cooper run report — aggregator (signal-scan-aggregator, Mon 2:30pm CT) owns all three. HCL's write will surface in the aggregator's HubSpot `last_signal_date = today`... note: HCL last_signal_date = 2025-12-18 (event date), so it will NOT appear in the aggregator's `last_signal_date = today` query. The aggregator reads event-dated signals; this LIGHT/Cool write is captured for Tim Z (International) via heat ranking, but flag: a 179-day-event write does not register as a same-day signal. Documented here for the aggregator's awareness.**

```
[Enterprise] target=16 matched=1 new=0 writes=1 heat_promotions=1 gate_rejections=0 apollo=0/55 runtime=~14min audit=weekly-reports/2026-06-15/signal-scan/enterprise/
```
