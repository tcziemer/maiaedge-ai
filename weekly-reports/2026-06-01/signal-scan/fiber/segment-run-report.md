# Signal Scan — Fiber Operator — Segment Run Report

**Date:** 2026-06-01 (Monday, CT)
**Segment:** Fiber Operator
**Detection window:** 2026-05-18 → 2026-06-01 (14 days rolling, event-date semantics)
**Outcome:** QUIET week — **0 net new HubSpot writes**
**Apollo consumed:** 0 of 35 (weekly W22 pool: 0/850 before run, 0/850 after)
**Runtime:** ~12 min
**MCPs used:** HubSpot (read), Slack (canvas read), web_search; Apollo not invoked

---

## 1. Run header

| Item | Value |
|---|---|
| Target pool (Fiber, account_tier 1-3, type != Customer, excl. MaiaEdge own) | 989 records |
| Canvas F0B0AFSB9LN read | OK — no signal-scan-owned Fiber Tier 3 carryovers (Fiber items present are R1/R3 dedup holds owned by other routines: Vero Fiber dup, segrafiber dup, Fidium carryover, Zirrus, Bulk Fiber) |
| Apollo budget tracker | Read OK — W22, 850 remaining, effective_apollo = min(35, 850) = 35 |
| Prior-Monday report (2026-05-25) | ABSENT (first per-segment Fiber run) — all matches tagged NEW; no source-coverage delta available |

## 2. Source coverage (search-anchor pattern)

Robust tier and high-yield Medium tier sources attempted this run:

| # | Source / topic anchor | Status |
|---|---|---|
| 1 | Fierce Network / Fierce Telecom — M&A tracker, career moves | ✓ |
| 2 | Light Reading — M&A watch, fiber giant coverage | ✓ |
| 3 | Lightwave Online — 400G/800G, IRU, AI-DC fiber | ✓ |
| 4 | Telecompetitor — regional operators, BEAD, expansions | ✓ |
| 5 | Broadband Communities / bbcmag | ✓ (via cross-source) |
| 6 | NTIA BEAD progress + state broadband offices | ✓ |
| 7 | SEC 8-K / StockTitan (Uniti / Kinetic ABS) | ✓ |
| 8 | PR Newswire / Business Wire / GlobeNewswire (BIG Fiber, Heartland, GCI, Uniti) | ✓ |
| 9 | DataCenterKnowledge / IEEE ComSoc (AI dark fiber) | ✓ |
| 10 | BroadbandBreakfast (KKR/Metronet, Cable One) | ✓ |
| 11 | Fiber Broadband Association (Fiber Connect 2026, awards) | ✓ |
| 12 | Exec-hire boards / career-moves columns | ✓ |
| — | International supplement (CVC DIF / Celeste FR) | ✓ |
| — | Lightwave 400G/800G IRU (no in-window deal found) | ✓ (negative) |

No 3-week ✗ streaks (first per-segment run; no prior baseline). Source Coverage Mandate satisfied for robust + priority-medium tiers.

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target list size | 989 |
| Detected candidates (raw, any date) | ~14 |
| In-window candidates (event ≥ 2026-05-18) | 3 |
| Matched to target pool | 1 (BIG Fiber) |
| NEW accounts created | 0 |
| Total writes | 0 |
| Dropped — out of window | 9 |
| Dropped — dedup (already recorded) | 1 |
| Dropped — out of segment / not in pool | 1 |

## 4. Score distribution

No new scored writes this run. (BIG Fiber's in-window signal was already scored and recorded by a prior run at score 30.)

| Bucket | Count |
|---|---|
| 27+ (Highest) | 0 |
| 18-26 (Strong) | 0 |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 0 |

## 5. Writes summary

**None.** Zero HubSpot writes this run.

## 6. Tier 3 holds

None taken this run. No signal-scan-owned Fiber Tier 3 carryovers were present on canvas F0B0AFSB9LN at Stage 0, and none created this run. No canvas re-append required.

## 7. QA gate drops & detection-stage dispositions

| Candidate | Event date | Disposition | Reason |
|---|---|---|---|
| **BIG Fiber** (320875891447, tier_2, owner Tim Z) — $250M debt facility led by Stonepeak Credit + La Caisse for AI-era dark fiber (F-A8) | 2026-05-19 | **Dedup no-op** (QA rule 8) | Record already carries last_signal_date 2026-05-19, last_signal_score 30, signal_count_last_30d 1, heat Warm. Heat recompute confirms Warm is correct (score 30 ∈ [27,44], 13d ≤60d, no open deal). Tier frozen (hs_is_target_account=true). No write needed. **Note:** owner = 159350430 (Tim Z International) but HQ is Sunnyvale CA (West / Ken). Possible territory misassignment — surfaced for R6 / Cooper, not corrected here. |
| **Heartland Fiber Project** — $700M, 2,000-mi Denver-Chicago AI backbone (DCN + Range + WIN Technology) (F-A3/F-A9) | 2026-05-15 | **Drop — out of window** (QA rule 2) | Primary PRNewswire/Morningstar wire dated 2026-05-15 = 17 days back, 3 days outside the 14-day gate. Telecompetitor's 5/18 article is a re-publication, not the event date. **Carryover flagged for 2026-06-08** (will also be out of window then; logging for awareness only). Participants DCN (208908440283, Fiber Op / Long Haul-Backbone, tier_2) and WIN Technology (316278520568, MSP/Aggregator, tier_2) already exist in CRM; "Range" not dup-checked (moot — signal out of window). No NEW-account creation. |
| **CNMI / IT&E** — $31.3M BEAD subgrant, fully-underground FTTH, ~10k homes Saipan/Rota/Tinian (F-A1) | 2026-05-18 | **Deferred — out of segment** | IT&E (PTI Pacifica) is an integrated CNMI mobile+fiber territory carrier; not in the Fiber T1-3 pool and would route to Network Operator, not Fiber. No Apollo spend; logged for the Network Op scan / account-sourcing follow-up. |

### Out-of-window detected (logged, not scored)

| Event | Company | Event date | Pool? |
|---|---|---|---|
| Quintillion acquisition ($310M) | GCI (175217873639, tier_3) | 2026-04-22 | yes — but out of window |
| Crown Castle Fiber Solutions close (+90k route mi) | Zayo (193910127352, tier_2, Hot) | 2026-05-01 | yes — out of window |
| ExteNet enterprise fiber acquisition | Pilot Fiber | 2026-02-05 | no |
| Celeste ~88% stake (CVC DIF) | Celeste (FR) | 2026-01-14 | no |
| 1,100-mi south-central AI dark fiber (+$500M, 20-yr) | Uniti Wholesale (193906530037, tier_1, Hot) | 2026-01-13 | yes — out of window |
| Kinetic ABS fiber notes ($960M-$1.14B) | Uniti | 2026-01-30 (priced) | yes — out of window |
| Arizona expansion ($80M, 50k homes) | Ripple Fiber (292719725284, tier_3) | 2026-05-12 | yes — out of window |
| Myakka Communications acquisition (close) | Dragonfly Internet | 2025-12-24 | no |
| COO hire (Doug Guthrie) | IQ Fiber | 2026-02-04 | no |
| Segra commercial/carrier acquisition | Cox / Segra (322368676578, tier_2) | 2021 (re-referenced) | yes — 5yr-old deal, not 2026 |

## 8. Failed writes

None (no writes attempted).

## 9. Apollo budget post-run

0 credits consumed. Weekly W22 unchanged at 0/850. No tracker write required (no consumption); JSON left as-is.

---

**Handoff:** Aggregator (`signal-scan-aggregator`, 2:30pm CT) will read HubSpot for `last_signal_date = today` Fiber records — there are none from this run — and build the consolidated rep DMs + canvas Run log row + Cooper run report. No rep DM, canvas update, or Cooper report sent by this task.
