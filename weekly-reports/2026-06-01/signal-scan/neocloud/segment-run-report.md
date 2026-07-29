# Signal Scan — NeoCloud — Segment Run Report

## 1. Run header
- **Date (CT):** 2026-06-01 (Monday)
- **Segment:** NeoCloud
- **Detection window:** 2026-05-18 → 2026-06-01 (14-day rolling, event date)
- **Apollo consumed:** 0 of 55
- **Runtime:** ~12 min
- **MCPs:** HubSpot ✓, Apollo ✓ (unused), Slack ✓ (canvas read), web_search ✓, web_fetch ✓ (1 of 3 article fetches returned content; 2 client-rendered shells worked around via search snippets)
- **Verdict:** QUIET in-window week. 1 scored write (SoftBank AI Cloud). All other material NeoCloud moves event-dated before the 5/18 cutoff.

## 2. Source coverage table
| # | Source | Status | Notes |
|---|---|---|---|
| 1 | DCD / DCF / DCK / The Register | ✓ | SambaNova/Argyll (5/6-11, out of window), IREN/Nvidia (5/7, out of window) surfaced |
| 2 | NVIDIA Newsroom / GTC / partner page | ✓ | No new in-window NeoCloud partner announce |
| 3 | StockTitan (8-K mirror, public NeoClouds) | ✓ | Hut 8 5/6 lease (out of window), no new in-window 8-K |
| 4 | SEC EDGAR full-text | ✓ | Cipher/Core Scientific/TeraWulf filings = FY roundups, not fresh single events |
| 5 | Crypto-to-AI outlets (CoinDesk / Bitcoin Mag / news.bitcoin.com) | ✓ | TeraWulf $12.8B cumulative, no fresh in-window single event |
| 6 | IX member pages (DE-CIX / AMS-IX / LINX / Equinix IX / SIX) | ✗ | Not reachable this run; no NC-A10 detections |
| 7 | Greenhouse / Lever / Ashby job boards | ✗ | Not scraped this run (quiet-week triage); no NC-A6 |
| 8 | Apollo MCP | ✓ | Available, unused (no NEW-account discovery) |
| 9 | HPCwire / Next Platform / ServeTheHome | ✓ | No new in-window region confirmations |
| 10 | Crunchbase / TechCrunch / SiliconANGLE | ✓ | FluidStack $1B round (4/14 report, out of window) |
| 11 | PR Newswire / Business Wire / GlobeNewswire | ✓ | Nebius/Bloom (signed 5/14, out of window); IREN/Nvidia GlobeNewswire 5/7 |
| 12 | Per-NeoCloud IR / newsroom | ✓ | SoftBank press release 20260525_01 (IN WINDOW — scored) |
| 13-22 | Medium tier (Information / SemiAnalysis / newsletters / ratings) | ◐ | Snippet-level only; no incremental in-window signal |
| Intl | EuroHPC / sovereign AI (EMEA/APAC/MENA) | ✓ | SoftBank Japan sovereign launch (scored); no EuroHPC AI Factory award in window |

3-week ✗ streak watch: IX member pages (#6) and job boards (#7) — first miss logged this run; not yet a streak.

## 3. Candidate funnel
- Target list size: **154** NeoCloud tier 1-3 records (type != Customer, MaiaEdge own excluded)
- Tier 3 carryovers from canvas F0B0AFSB9LN: NeoCloud holds are R3 dedup/classification items (Hut 8, Riot — resolved 2026-05-18 R3; DataCrunch verda.com vs datacrunch.io; Ooredoo same-parent divisions). None are signal-scan re-scan targets.
- In-window signal candidates detected: **1** (SoftBank AI Cloud)
- Matched to target accounts: **1**
- NEW accounts created: **0**
- Total HubSpot writes: **1**
- Drops (out of window / below floor): **5+** (see §7)

## 4. Score distribution
| Band | Count |
|---|---|
| 27+ (Highest) | 1 |
| 18-26 (Strong) | 0 |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 0 |
| <8 (silent drop) | 0 in-window |

## 5. Writes summary per record
| HubSpot ID | Name | NC code | Score | Heat delta | Tier delta | last_enriched_date |
|---|---|---|---|---|---|---|
| 324007728852 | SoftBank AI Cloud (softbank.jp) | NC-A2 | 27 | Cold → Warm | frozen (hs_is_target_account=true; stays tier_1) | NOT bumped (partial signal write) |

**SoftBank detail:** Sovereign AI GPU cloud launch — "AI Data Center GPU Cloud" on NVIDIA GB200 NVL72 in Japan, beta live 2026-05-25, commercial availability Oct 2026. Source: SoftBank press release `softbank.jp/en/corp/news/press/sbkk/2026/20260525_01/` + RCR Wireless 2026-05-27 (published/modified 2026-05-27, references 5/25 announcement). NC-A2 New Region/GPU-cloud Launch, Tier A(3) × Freshness(3, event 7 days old, ≤60d) × Confidence HIGH(3) = 27. signal_count_last_30d set to 1. signal_heat = Warm (score 27-44 AND ≤60d; below Hot's 45 threshold, no open deal). Owner 159350430 (Tim Ziemer, International) — Japan, correct. Tag: NEW (no prior signal-scan entry; record was Cold with no last_signal_date).

## 6. Tier 3 holds
No NEW NeoCloud signal-scan Tier 3 holds this run. Existing NeoCloud canvas items are R3-owned dedup pairs (no re-append needed — they remain in the R3 queue, not signal-scan's).

## 7. QA gate drops (out-of-window / non-qualifying, with reasons)
| Candidate | Account in CRM? | Event date | Reason dropped |
|---|---|---|---|
| Hut 8 $9.8B Beacon Point lease | Yes (324208873163, Hot) | 2026-05-06 | Out of 14-day window; already carries 5/6 signal |
| IREN / Nvidia $2.1B strategic partnership (5GW DSX) | Yes (240444244684, Cool) | 2026-05-07 | Out of window; already carries 5/07 signal |
| SambaNova / Argyll UK sovereign AI inference cloud | Yes (303377637098, Cool) | 2026-05-06 to 05-11 | Out of window; SambaNova is tech partner, Argyll (not in CRM) is the operator |
| Nebius / Bloom Energy $2.6B / 328MW fuel-cell power | Yes (240440573644, Warm) | 2026-05-14 (signed) | Out of window; power partnership, weak connectivity relevance |
| FluidStack $1B round / $50B Anthropic | Yes (240447926006, Cool) | 2025-11-12 / 2026-04-14 | Out of window |
| Roundhill Neocloud ETF ($NCLD) filing | n/a | 2026-05-22 | Sector-level, not account-specific — no per-account signal |
| CoreWeave $3.1B DDTL 5.0 / Nebius $4.34B debt | Yes (tier_1) | mid-March 2026 | Out of window (prior Weekly Market News coverage) |

## 8. Failed writes
None. 1/1 HubSpot write succeeded.

## 9. Apollo budget post-run
- Sub-cap: 55/run. Used: **0**. Weekly W22: 0/850, 850 remaining (unchanged — no Apollo consumed).

## 10. Compound-signal detections
None. SoftBank scored as a single Tier A signal (27). No triple-firing / stacked-signal accounts in window.

---
*No rep DMs, no canvas Run log row, no Cooper run report — those are owned by signal-scan-aggregator (Mon 2:30pm CT), which reads HubSpot `last_signal_date = today` records.*
