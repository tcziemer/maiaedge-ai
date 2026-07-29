# Signal Scan — NeoCloud — Segment Run Report

## 1. Run header
- **Date (CT):** 2026-06-08 (Monday)
- **Segment:** NeoCloud
- **Detection window:** 2025-12-10 → 2026-06-08 (180-day rolling, event date) — first full run under the widened window
- **Apollo consumed:** 0 of 55 (NEW-account creation done from public web research; matched writes are Apollo-free)
- **Runtime:** ~22 min
- **MCPs:** HubSpot ✓, Apollo ✓ (available, unused), Slack ✓ (canvas read; 851K-char canvas sliced offline), web_search ✓, web_fetch ✓
- **Detection method:** Source detection fanned out across 4 research sub-agents (crypto-to-AI publics / large-scale GPU / sovereign AI / inference + net-new) per the context-budget safeguard, returning structured candidates only. Scoring + QA + writes done centrally.
- **Verdict:** HIGH-yield run. The 180-day window surfaced the full backlog of material public AI-infra events the prior 14-day window discarded. **33 writes (31 matched + 2 NEW), 0 failures.**

## 2. Source coverage table
| # | Source | Status | Notes |
|---|---|---|---|
| 1 | DCD / DCF / DCK / The Register | ✓ | Riot/AMD, Bitdeer Tydal, Soluna Dorothy, TensorWave/TECfusions surfaced |
| 2 | NVIDIA Newsroom / GTC / partner page | ✓ | Lambda (Vera/STX), Vultr + YTL (Exemplar), GMI (Vera Rubin), Naver (DSX), Deutsche Telekom (Munich) |
| 3 | StockTitan (8-K mirror, public NeoClouds) | ✓ | Core Scientific notes, Cipher lease, Bitfarms/Keel converts, Hive Paraguay, Greenidge Q1, White Fiber Paris |
| 4 | SEC EDGAR full-text | ✓ | CoreWeave DDTL 5.0 (crwv-20260515), backup confirms |
| 5 | Crypto-to-AI outlets (CoinDesk / Bitcoin Mag / news.bitcoin.com) | ✓ | TeraWulf Muskie, CleanSpark Brazoria, Mawson rebrand (dropped) |
| 6 | IX member pages (DE-CIX / AMS-IX / LINX / Equinix IX / SIX) | ✗ | Not scraped this run (news/filing-signal focus); no NC-A10 detections — **2nd consecutive ✗ (also 2026-06-01); watch for 3-week streak** |
| 7 | Greenhouse / Lever / Ashby job boards | ✗ | Not scraped this run; no NC-A6 hiring-spike detections — **2nd consecutive ✗; watch for streak** |
| 8 | Apollo MCP | ✓ | Available, unused (NEW accounts enriched from public web research) |
| 9 | HPCwire / Next Platform / ServeTheHome | ✓ | Yotta Blackwell Ultra (dropped, Tier B stale), Firmus Southgate |
| 10 | Crunchbase / TechCrunch / SiliconANGLE | ✓ | Together $1B/$305M, FluidStack (anti-churn skip), Modal Series C, fal.ai (dropped) |
| 11 | PR Newswire / Business Wire / GlobeNewswire | ✓ | Hut 8 notes, Bitdeer Tydal, G42 Condor Galaxy India, Voltage Park merger |
| 12 | Per-NeoCloud IR / newsroom | ✓ | Applied Digital Goldman revolver, IREN $3.65B close, Core42 HSBC, TELUS, Cassava |
| 13-22 | Medium tier (Information / SemiAnalysis / newsletters / ratings) | ◐ | Snippet-level; corroborated funding rounds |
| Intl | EuroHPC / sovereign AI (EMEA/APAC/MENA) | ✓ | Deutsche Telekom, TELUS, Naver, G42, Core42, Sakura, YTL, Firmus, Cassava; no fresh EuroHPC AI Factory award in window |
| n/a | PeeringDB (NC-A9) | ✗ | Not diffed this run; no NC-A9 detections |

**Source Coverage Mandate note:** This run weighted funding / facility / financing / partnership signals (the densest NeoCloud classes) over IX/PeeringDB/job-board diffs. IX member pages (#6), job boards (#7), and PeeringDB are now at a 2-run ✗ for NC-A6/A10/A9; if missed again 2026-06-15 they hit the 3-week auto-flag.

## 3. Candidate funnel
- Target list size: **163** NeoCloud records (all tiers, non-Flagged, type != Customer, MaiaEdge own excluded). Complete pool (total 163, no pagination).
- Tier 3 carryovers from canvas F0B0AFSB9LN: NeoCloud canvas items are R3-owned dedup pairs (Hut 8, Riot, Soluna, DataCrunch, Hive, Bitfarms/Keel). None are signal-scan re-scan targets. Budget-overflow backlog: none (no prior run left one).
- In-window scored candidates detected: **~50** across the 4 slices
- Passed score floor (>=8) AND anti-churn: **33** (31 matched + 2 NEW)
- Matched to existing accounts: **31**
- NEW accounts created: **2** (Digi Power X, Bitzero)
- Total HubSpot writes: **33** (0 failed)
- Drops (below floor / out of Tier-B freshness / anti-churn / not-actionable): see §7

## 4. Score distribution
| Band | Count |
|---|---|
| 27+ (Highest) | 18 |
| 18-26 (Strong) | 11 |
| 12-17 (Worth Reviewing) | 1 |
| 8-11 (LIGHT) | 3 |
| <8 (silent drop) | (numerous — see §7) |

Heat distribution (33 writes): **Hot 3 · Warm 15 · Cool 15 · Cold 0.** Heat promotions: **27** (mostly Cold → Cool/Warm). 2 truthful demotions (Hut 8, CoreWeave — Hot → Warm; their 2nd recent signal aged past the 30-day count window, so a fresh single material event computes to Warm, not Hot).

## 5. Writes summary per record
| HubSpot ID | Name | NC code | Event date | Score | Heat (prev → new) | Tier | last_enriched bump |
|---|---|---|---|---|---|---|---|
| 239751073471 | Applied Digital | NC-A5 | 2026-05-29 | 33 | Hot → Hot | frozen (tgt) tier_1 | no |
| 324208873163 | Hut 8 | NC-A5 | 2026-06-04 | 33 | Hot → Warm | frozen (tgt) tier_1 | no |
| 240444244684 | IREN | NC-A5 | 2026-06-01 | 33 | Cool → Warm | frozen (tgt) tier_1 | no |
| 324007013098 | TeraWulf | NC-A2 | 2026-05-26 | 33 | Warm → Hot | frozen (tgt) tier_1 | no |
| 240415542983 | Core Scientific | NC-A5 | 2026-05-06 | 27 | Cold → Warm | frozen (tgt) tier_1 | no |
| 296850118389 | Cipher Mining | NC-A8 | 2026-03-25 | 18 | Cold → Cool | frozen (tgt) tier_1 | no |
| 297892337355 | Riot Platforms | NC-A4 | 2026-04-30 | 27 | Cold → Warm | frozen (tgt) tier_1 | no |
| 264413011658 | CleanSpark | NC-A2 | 2026-01-14 | 9 | Cold → Cool | tier_1 | no |
| 240442367678 | Bitdeer | NC-A2 | 2026-03-30 | 18 | Cold → Cool | tier_1 | no |
| 298005835457 | Bitfarms (Keel) | NC-A5 | 2026-06-04 | 27 | Cool → Warm | frozen (tgt) tier_1 | no |
| 244551342805 | Hive Digital | NC-A2 | 2026-03-18 | 18 | Cold → Cool | frozen (tgt) tier_1 | no |
| 303374043856 | Soluna | NC-A2 | 2026-05-19 | 27 | Warm → Warm | frozen (tgt) tier_1 | no |
| 303405064911 | Greenidge | NC-A2 | 2026-05-18 | 33 | Cool → Warm | frozen (tgt) tier_1 | no |
| 240431524557 | CoreWeave | NC-A5 | 2026-05-15 | 33 | Hot → Warm | frozen (tgt) tier_1 | no |
| 240190285514 | White Fiber | NC-A4 | 2026-05-21 | 27 | Cool → Warm | frozen (tgt) tier_1 | no |
| 303399739102 | Lambda | NC-A3 | 2026-03-16 | 18 | Cold → Cool | frozen (tgt) tier_1 | no |
| 240242364125 | Nscale | NC-A4 | 2026-06-02 | 33 | Hot → Hot | frozen (tgt) tier_1 | no |
| 240392240847 | Vultr | NC-A3 | 2026-04-01 | 18 | Cold → Cool | frozen (tgt) tier_1 | no |
| 298009434842 | GMI Cloud | NC-A3 | 2026-06-03 | 18 | Cold → Cool | tier_1 | no |
| 298011233986 | DigitalOcean | NC-A2 | 2026-04-21 | 18 | Cold → Cool | tier_1 | no |
| 301316953844 | G42 | NC-B3 (+I2) | 2026-05-15 | 21 | Cool → Cool | frozen (tgt) tier_1 | no |
| 303842934518 | Core42 | NC-A5 | 2026-05-26 | 27 | Cold → Warm | tier_1 | no |
| 251659209450 | TELUS Sovereign AI | NC-A2 | 2026-05-12 | 27 | Cold → Warm | frozen (tgt) tier_1 | no |
| 303925580502 | Deutsche Telekom AI Cloud | NC-A2 | 2026-04-30 | 27 | Cold → Warm | frozen (tgt) tier_1 | no |
| 300347451125 | Cassava Technologies | NC-A2 | 2026-03-18 | 18 | Cold → Cool | tier_1 | no |
| 239793615562 | Firmus | NC-A2 | 2026-04-15 | 18 | Cold → Cool | tier_1 | no |
| 298002235113 | Sakura Internet | NC-B3 (+I2) | 2026-03-27 | 9 | Cold → Cool | tier_1 | no |
| 301136592630 | Naver Cloud | NC-A3 | 2026-06-07 | 27 | Cold → Warm | tier_1 | no |
| 303399663350 | YTL AI Cloud | NC-A3 | 2026-05-15 | 18 | Cold → Cool | tier_1 | no |
| 240390403774 | Groq | NC-B2 | 2026-05-28 | 8 | Cold → Cool | tier_2 | no |
| 297918677710 | Modal | NC-B2 | 2026-05-21 | 12 | Cold → Cool | tier_2 | no |
| **326692012738** | **Digi Power X (NEW)** | NC-A4 | 2026-05-05 | 27 | (new) → Warm | tier_1 | **YES** |
| **326672272092** | **Bitzero (NEW)** | NC-A4 | 2026-05-05 | 27 | (new) → Warm | tier_1 | **YES** |

Tier writes: no `account_tier` changes were needed (all matched writes already sit at their computed tier; the 2 tier_2 inference names received sub-18 signals that do not warrant promotion). `hs_is_target_account = true` froze tier on 19 records anyway; heat always written.

**NEW account detail:**
- **Digi Power X** (326692012738, digipower.com) — NeoCloud / Crypto to AI - Neoclouds / tier_1 / Warm. Cerebras $1.1B-$2.5B 10-yr MSA for a 40MW AI campus in Columbiana AL (15MW phase by Dec 2026). Owner **Tim Lieto (East, 161889085)** assigned on US operational footprint (Alabama/North Carolina, DGXX-listed) despite Toronto incorporation — flagged for R6 to confirm. Source: stocktitan.net/news/DGXX/.
- **Bitzero** (326672272092, bitzero.com) — NeoCloud / Crypto to AI - Neoclouds / tier_1 / Warm. OneQode 110MW 15-yr ~$2.6B TCV AI lease at Norway site. Owner **Ken Cunningham (West, 162339176)** on Fargo ND HQ — flagged for R6 to confirm ND territory. Source: bitzero.com press release.

## 6. Tier 3 holds
No NEW NeoCloud signal-scan Tier 3 holds this run. The standing NeoCloud canvas items are R3-owned dedup pairs and are **not** re-appended by signal-scan. Awareness-only dedup pairs touched this run (write directed to ONE record each to avoid double-counting, per QA rule 8):
- **Hut 8**: wrote 324208873163 (tgt, prior signal); 323823198916 left untouched — R3.
- **Bitfarms / Keel Infrastructure**: wrote Bitfarms 298005835457 (ticker BITF, prior signal); Keel Infrastructure 311386967793 is the rebrand-dup, left untouched — R3.
- **Hive Digital**: wrote 244551342805 (tgt, hiveblockchain.com); 316412310231 (hivedigitaltechnologies.com) untouched — R3.
- **Soluna**: wrote 303374043856 (tgt, soluna.io); 301205051103 untouched — R3.
- **Riot**: wrote 297892337355 (tgt, riotplatforms.com); 322537130689 (riot.inc) untouched — R3.
- **DataCrunch / Verda**: both records (240435183333 verda.com, 318219155162 datacrunch.io) — no write (signal scored below floor); R3 dedup pending.

## 7. QA gate drops (out-of-Tier-freshness / below-floor / anti-churn / not-actionable, with reasons)
| Candidate | In CRM? | Event date | Reason dropped |
|---|---|---|---|
| Nebius | Yes (Warm, 5/01/27) | 2026-03-16 (Meta $27B) | Anti-churn: freshest event OLDER than stored 5/01; no post-5/01 material event |
| FluidStack | Yes (Cool, 4/30) | 2026-04-14 ($1B/$18B round) | Anti-churn: round reported before stored 4/30; not newer |
| SoftBank AI Cloud | Yes (Warm, 5/25/27) | 2026-05-25 | Stored signal already captures the Infrinia GPU-cloud launch; no newer event |
| SambaNova | Yes (Cool, 3/15) | 2026-02-24 (Series E) | Anti-churn: Series E predates stored 3/15; no fresher event (stored score still blank — backfill candidate) |
| Together AI | Yes | 2026-02-24 / 04-01 | NC-B2 Tier B, >90d / 68d → freshness ×1, score 4-6 < floor 8 |
| Voltage Park | Yes | 2026-01-21 | NC-B2 Tier B, 138d > 90d → freshness drop |
| TensorWave | Yes | 2026-01-13 (TECfusions 20MW) | NC-A2 Tier A, 146d → ×1, M conf → score 6 < floor |
| Scaleway | Yes | 2026-03-01 (Milan MIL-1) | NC-A2 Tier A, 99d → ×1, M conf → score 6 < floor |
| Gcore | Yes | 2026-03-11 (Dynamo) | Product integration (NC-C4), weak/context-only → below floor |
| DataCrunch / Verda | Yes (dup) | 2026-04-24 ($117M) | NC-B2 Tier B, 45d → ×1, score 6 < floor |
| Reliance Jio AI | Yes | 2026-02-19 ($110B plan) | NC-B3 Tier B, 109d > 90d → freshness drop |
| Singtel RE:AI | Yes | 2026-02-24 (CoE w/NVIDIA) | NC-A3 soft (CoE, not Exemplar/NCP), M conf, 104d → score 6 < floor |
| Telenor AI Factory | Yes | 2026-03-02 (Red Hat stack) | Stack choice, M conf, 98d → below floor |
| Yotta Data Services | Yes | 2026-02-19 (Blackwell Ultra) | NC-B5 Tier B, 109d > 90d → freshness drop |
| Sarvam AI | Yes | 2026-03-15 (round in talks) | NC-B2 Tier B, 85d, M conf → score 4 < floor |
| Civo | Yes | 2026-04-14 (Project Mercury) | NC-B3 Tier B, soft, M conf → score 4 < floor |
| Domyn | Yes | 2026-01-15 (gigafactory) | NC-A2, 144d → ×1, M conf → score 6 < floor |
| HUMAIN | Yes | 2026-06-01 | In-window event is autonomous-mobility, not AI-cloud — out of connectivity scope |
| Northern Data Group | Yes | 2026-06-08 (Rumble ~85%) | Control change / acquisition — connectivity decisions move to acquirer; not an actionable standalone signal |
| Lightning AI | Yes | 2026-01-21 (Voltage Park merger) | 138d aging + dedup-entangled with Voltage Park record + poor NC-code fit → hold for R3 dedup, not written |
| Mawson Infrastructure | Yes | 2026-04-30 (rebrand BGDE) | Corporate rebrand only — not a connectivity-material trigger |
| Sharon AI | Yes | 2026-04-01 ($1.25B ESDS) | Contract under short-seller scrutiny; materiality uncertain — default to NOT writing |
| fal.ai | Yes | 2026-03 (in talks) | Round unconfirmed/in-progress, no firm date, M conf → below floor |
| FriendliAI | Yes | 2026-03-13 (InferenceSense) | NC-C4 product launch, Tier C → below floor |
| Replicate | Yes | 2025-12-01 (Cloudflare acq) | Out of window (9 days before 12-10 open) |
| Crusoe / Galaxy Digital / Marathon / Ionic / Prometheus / OVHcloud / Hyperstack-NexGen / GreenNode / Foxconn / SF Compute / Vast / Cudo / Denvr / Nebul / KDDI / Swisscom / Fastweb / Taiga / Indosat / SK Telecom / Inference.net | Yes | — | NONE in-window-and-newer-than-stored |

**Net-new discovery, no record created:** Mistral AI Compute (France sovereign cloud — but a model lab that owns its infra, weak connectivity-buyer fit), BharatGen (India model-allocation program, not an infra operator), Hosted.ai / General Compute (sub-$50M threshold). All logged for awareness; no creation.

## 8. Failed writes
None. 33/33 HubSpot writes succeeded (batches of 10/10/10/1 + 2 creates).

## 9. Apollo budget post-run
- Sub-cap: 55/run. Used: **0**. NEW accounts (Digi Power X, Bitzero) enriched from public web research (DGXX filings, press releases) — no firmographic gap required Apollo, consistent with the established unattended-run pattern (Apollo interactive-confirmation guardrail cannot be satisfied in a scheduled run). Weekly W23: 0/850, 850 remaining (unchanged).

## 10. Compound-signal detections (triple-firing / stacked)
Seven accounts carried 2+ material signals within a 30-day window (+6 stacked bonus applied), reflecting the public AI-infra financing/buildout wall:
- **Applied Digital** — anchor lease history + Goldman revolver (5/23 + 5/29) → count 2, **Hot**, 33
- **TeraWulf** — Kentucky Muskie campus + prior (5/15 + 5/26) → count 2, **Hot**, 33
- **Nscale** — Microsoft Portugal Rubin + prior Microsoft supply (5/20 + 6/02) → count 2, **Hot**, 33
- **IREN** — NVIDIA strategic partnership + $3.65B financing close (5/07 + 6/01), 33
- **CoreWeave** — prior facility + $3.1B DDTL 5.0 (5/07 + 5/15), 33
- **Hut 8** — Beacon Point lease + $4.25B notes (5/06 + 6/04), 33
- **Greenidge** — prior + 60MW NYSEG interconnect (5/08 + 5/18), 33

---
*No rep DMs, no canvas Run log row, no Cooper run report — owned by signal-scan-aggregator (Mon 2:30pm CT), which reads HubSpot `last_signal_date = today` records.*
