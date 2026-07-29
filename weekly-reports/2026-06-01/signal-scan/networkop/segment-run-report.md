# Signal Scan — Network Operator — Segment Run Report

## 1. Run header

- **Date (CT):** 2026-06-01 (Monday)
- **Segment:** Network Operator (`customer_segment = "Network Operator(Tier 1 / VNO)"`)
- **Detection window:** 14-day rolling, 2026-05-18 → 2026-06-01
- **Apollo consumed:** 0 of 50 (weekly pool W22: 0/850 at run start; effective budget min(50, 850) = 50)
- **Runtime:** ~7 min
- **MCPs:** HubSpot ✓, Apollo ✓ (available, unused), Slack ✓ (canvas read), web_search ✓, web_fetch ✓
- **Result:** QUIET in-window week — 0 scored hits ≥ floor, 0 HubSpot writes, 0 NEW accounts. Consistent with sibling Colo + NeoCloud scans today (both QUIET in-window).

## 2. Source coverage

Source Coverage Mandate: every documented source attempted via search-anchor for the 2026-05-18 → 2026-06-01 window.

| # | Source (registry tier) | Status | Note |
|---|---|---|---|
| 1 | Company IR / newsroom diffs (Lumen, AT&T, Verizon, T-Mobile, Charter, Cox, Comcast, BT, Vodafone, DT, Orange, Telefónica, NTT, Tata, Singtel, Telstra) | ✓ | Via search-anchor; surfaced moves all out-of-window or administrative (see §3) |
| 2 | StockTitan (8-K / 13D-G mirror) | ✗ | Not directly reached; M&A/divestiture coverage routed through Fierce M&A tracker search instead |
| 3 | SEC EDGAR full-text | ✗ | Backup to StockTitan; not reached this run |
| 4 | Earnings transcripts (Seeking Alpha / Motley Fool / MarketBeat) — NaaS/API/SRv6 keyword filter | ✓ | No in-window Q-call transcript hits for target carriers; earnings windows quiet late May |
| 5 | Fierce Network + Light Reading + TelecomTV + RCR + Total Telecom | ✓ | Searched; career-moves + M&A trackers returned client-rendered shell on direct fetch but content surfaced via search |
| 6 | Ciena/Nokia/Cisco/Juniper/Arista/Infinera newsrooms (supplier wins) | ✗ | Not reached; no NO-B1 candidate surfaced incidentally |
| 7 | MEF/Mplify + TM Forum + Catalyst | ✓ (partial) | Mplify co-CEO appointment (Mancuso/Sparkle + Morales/Orange Wholesale) surfaced — standards-body appointment, not a carrier exec transition; EXCLUDE per NO-A3 scope |
| 8 | GSMA + CAMARA GitHub + Open Gateway | ✓ (partial) | No in-window commercial-launch signal for target accounts |
| 9 | GlobeNewswire / PR Newswire / Business Wire (Appointments) | ✓ | Via search; no in-window scoreable appointment at a target account |
| 10 | Apollo MCP (AP-1/2/7) | ✗ | Not consumed — no unmatched in-window candidate warranted enrichment |
| 11 | GitHub commit feeds CAMARA/Nephio/ONAP/OpenConfig/Sylva (NO-A5) | ✗ | Not reached this run — log as ✗ (watch 3-week streak) |
| 12 | FedBizOpps / SAM.gov / state procurement (NO-A8) | ✗ | Not reached this run |
| 13 | Greenhouse/Lever/Ashby job boards (NO-A9) | ✗ | Not reached this run |
| 14 | Capacity Media (international primary) | ✓ | Via search; no in-window board-level move |
| 15 | Mobile World Live + Mobile Network UK | ✓ | US D2D satellite JV surfaced (out-of-window, 5/14) |
| 16-22 | TIA/USTelecom/CTIA, ONUG, ONF, LFN, ETSI, 3GPP, IETF | ✗ | Medium-tier; not reached this run |
| Intl | Capacity Asia/LATAM/MENA, ETNO, BNamericas | ✓ (partial) | Tata TComm Turkey subsidiary incorporation surfaced (administrative, below floor) |
| Subsea | TeleGeography Submarine Cable Map RFS feed + SubmarineNetworks.com + SubseaCables.net | ✓ | No in-window RFS / landing / consortium-join for subsea operators; Submarine Networks EMEA conf 5/27 = noise EXCLUDE |
| I2 | Sovereign AI Compute Grants | ✗ | None surfaced for carrier targets in window |

**Coverage note:** This run leaned on WebSearch aggregation across the trade-press + IR + subsea + M&A-tracker layer (the Robust single-source-yield tier) and confirmed a quiet window. Sources marked ✗ (StockTitan/EDGAR direct, supplier newsrooms, GitHub NO-A5, procurement NO-A8, job boards NO-A9, medium-tier standards bodies) were not individually reached this run. **First ✗ for NO-A5 / NO-A8 / NO-A9 this segment** — begin 3-week streak watch; if ✗ persists 3 consecutive Mondays, auto-flag to Cooper.

## 3. Candidate funnel

- **Target list:** 404 active Network Op tier 1-3 records (183+193 tier_1, 17+7 tier_2, balance tier_3; ~350 International/Tim Z, ~30 East/Lieto, ~16 West/Cunningham). MaiaEdge own (124293230301) and `type = Customer` excluded at query time.
- **Tier 3 signal-scan carryover pool:** 0 (no prior networkop segment-run-report on disk; canvas F0B0AFSB9LN holds only R0-R3 enrichment holds, no Network-Op signal-scan items).
- **In-window candidates detected:** 5 material moves, all dropped (see below).
- **Matched to target accounts AND scoring ≥ floor (8):** 0
- **NEW account candidates pursued:** 0
- **Total HubSpot writes:** 0
- **Drops:** 5

### Detected moves and disposition

| Move | Event date | Target match | Signal code | Disposition |
|---|---|---|---|---|
| Vocus revives CTO role — Nikos Katinakis (ex-Zayo, ex-Telstra), effective July | 2026-05-12 | Vocus (251600877280, tier_1, Intl) | NO-A3 | **DROP — out of 14d window** (event 5/12 < 5/18 cutoff). Strong NO-A3 if it had been in-window. Carryover-log for 2026-06-08 eval. |
| AT&T + T-Mobile + Verizon D2D satellite JV (agreement in principle) | 2026-05-14 | AT&T / Verizon / T-Mobile (all tier_1) | ~NO-A1 adjacent | **DROP — out of window** (5/14 < 5/18). |
| Lumen → Alkira acquisition ($475M, programmable networking for AI) | ~May 2026 | None (Lumen not in Network Op target list) | NO-A1 (rival-deal type) | **DROP — not a target account** (Lumen absent from tier 1-3 Network Op pool). |
| Zayo closes Crown Castle Fiber Solutions acquisition | 2026-05-01 | None (Zayo not in target list) | NO-A4-adjacent | **DROP — not a target + out of window.** |
| Tata Communications incorporates TComm Turkey step-down subsidiary | 2026-05-21 | Tata Communications (303925580513, tier_1, Intl) | — | **DROP — in-window but administrative**; no Tier A/B/C signal-code match. Even forced as C-tier LOW = score 3, below floor 8. Tata AGM/dividend notice (5/26) also administrative — drop. |

## 4. Score distribution

| Band | Count |
|---|---|
| 27+ (Highest) | 0 |
| 18-26 (Strong) | 0 |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 0 |
| <8 (silent drop) | 5 |

## 5. Writes summary

None. 0 records written. No `recent_news_or_trigger_event`, `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`, or `account_tier` changes this run.

## 6. Tier 3 holds

None carried in; none added. Canvas F0B0AFSB9LN requires no new Network-Op signal-scan appends this run.

## 7. QA gate drops

Stage 4.5 gate vacuous (0 scored hits to evaluate). The 5 detected moves were dropped at Stage 1/2 (freshness window or target-match), before scoring.

## 8. Failed writes

None (0 write attempts).

## 9. Apollo budget post-run

- Sub-cap: 50 / run. Consumed: 0.
- Weekly pool W22 unchanged: 0 / 850, 850 remaining.
- No JSON update required (0 consumption); tracker left as-is.

## 10. International signal flags

- No I2 Sovereign AI Compute Grants surfaced for carrier targets in window.
- Carryover watch for 2026-06-08 (events that fell just outside this window):
  - **Vocus** CTO Nikos Katinakis (5/12) — re-evaluate; if a follow-on confirmation lands in-window next Monday, NO-A3 fires.
  - US **AT&T/T-Mobile/Verizon** D2D satellite JV (5/14) — monitor for close/definitive-agreement event (second-event firing).

---

**[Network Op] target=404 matched=0 new=0 writes=0 heat_promotions=0 apollo=0/50 runtime=7min audit=weekly-reports/2026-06-01/signal-scan/networkop/**

No Slack DM sent from this task (per task spec). The Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs, canvas Run log, and Cooper run report — it will read HubSpot for `last_signal_date = today` records (0 from this segment) and reflect this segment's quiet run.
