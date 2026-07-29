# Weekly Signal Scan — Cross-ICP Run Report

**Date:** 2026-06-08 (Monday)
**Aggregator runtime window:** per-segment scans 8:30am–~1:15pm CT → aggregator ~2:30pm CT
**Status:** ✅ All 6 per-segment audit files present · all 6 segments wrote · all 3 rep DMs dispatched · Apollo 0 consumed

---

## 1. Run header

- **Total HubSpot signal writes across 6 segments:** 67 (Colo 5 / Fiber 20 / NeoCloud 33 / NetOp 3 / MSP 3 / Enterprise 3)
- **Total heat promotions:** ~57 (3 → Hot: Omni Fiber Cool→Hot, Lightpath Cold→Hot, TeraWulf Warm→Hot). 2 truthful NeoCloud demotions (Hut 8 Hot→Warm, CoreWeave Hot→Warm — 2nd recent signal aged past the 30-day count window).
- **NEW accounts auto-enriched:** 2 — Digi Power X (326692012738) and Bitzero (326672272092), both NeoCloud, both `last_enriched_date`-stamped. These are the only 2 records with `last_enriched_date` bumped this run.
- **Apollo consumed:** 0 / 250 signal-scan weekly sub-cap (every per-segment scan enriched from public web research; both NEW NeoCloud creates were web-research only).

## 2. Per-segment summary

| Segment | Audit | Target | Writes | NEW created | Score dist (8-11 / 12-17 / 18-26 / 27+) | Heat promotions | Tier Δ | Apollo (of sub-cap) | Source coverage |
|---|---|---|---|---|---|---|---|---|---|
| Colo | ✓ | 466 | 5 | 0 | 2 / 0 / 2 / 1 | 5 (1 Cold→Warm, 4 Cold→Cool) | 0 (3 frozen, 2 no-change) | 0 / 35 | ~11/17 (~65%) |
| Fiber | ✓ | 1,270 | 20 | 0 | 7 / 2 / 3 / 8 | 16 (Cool→Hot 1, Cold→Hot 1, Cold→Warm 3, Cool→Warm 2, Cold→Cool 9) | 5 promotions (Omni→t1, Aureon→t2, TDS→t2, Lyte→t1, Nexstream→t2) | 0 / 35 | ~16/19 (high) |
| NeoCloud | ✓ | 163 | 33 | 2 | 3 / 1 / 11 / 18 | 27 promotions / 2 demotions (Hut 8, CoreWeave Hot→Warm) | 0 (19 frozen; NEW at t1) | 0 / 55 | main IR/filing ✓ (~14/22) |
| Network Op | ✓ | 423 | 3 | 0 | 0 / 0 / 1 / 2 | 3 (Cool→Warm 1, Cold→Warm 1, Cold→Cool 1) | 0 (all 3 frozen) | 0 / 50 | partial (~11/22) |
| MSP/Aggregator | ✓ | 482 | 3 | 0 | 0 / 1 / 1 / 1 | 3 (Cold→Warm 1, Cold→Cool 2) | 0 (2 frozen, 1 unchanged) | 0 / 20 | ~11/20 (~55%) |
| Enterprise | ✓ | 13 | 3 | 0 | 2 / 0 / 1 / 0 | 3 (all Cold→Cool) | 0 (idempotent, base t3) | 0 / 55 | ~14/34 (~41%) |
| **TOTAL** | **6/6** | — | **67** | **2** | **14 / 4 / 19 / 30** | **~57** | **5 written** | **0 / 250** | — |

## 3. Cross-ICP heat distribution rollup (rep-owned heat pool, current)

- **Hot:** 41 · **Warm:** 58 · **Cool:** 104 · (Cold/null excluded from the workable pool) → **203 rep-owned accounts** in the Hot/Warm/Cool pool.
- **Delta vs prior Monday (2026-06-01):** 2026-06-01 was a deliberately quiet, in-window-only run (61 accounts surfaced across the 3 rep files). This week the 180-day heat pool is far richer — 150 surfaced across the 3 capped rep DMs (each rep at the 50 cap). The high NEW counts below are a true reflection of that pool expansion, not noise.

## 4. Rep DM dispatch

| Rep | Owner ID | Slack target | Surfaced | NEW | CARRIED | LIGHT | written-today | Top account (score) | Status |
|---|---|---|---|---|---|---|---|---|---|
| Tim Lieto (East) | 161889085 | U0A973L1HFF (live) | 50 (of 87 pool; 37 below cap) | 35 | 15 | 5 | 17 | Omni Fiber (33) | ✅ sent |
| Ken Cunningham (West) | 162339176 | U0AE1PGCB6C (live) | 50 (of 65 pool; 15 below cap) | 37 | 13 | 6 | 22 | Applied Digital (33) | ✅ sent |
| Tim Ziemer (Intl) | 159350430 | routed → Cooper U0A24D9RJLS | 50 (of 51 pool; 1 below cap) | 37 | 13 | 3 | 20 | Nscale (33) | ✅ sent (validate before forwarding) |

All 3 DMs dispatched as parent + threaded continuation + threaded full-list table (rows split 20/20/10 to stay under Slack's 5,000-char/message limit). Each xlsx written to `weekly-reports/2026-06-08/weekly-signal-scan-<rep>-2026-06-08.xlsx` (per-segment tabs + Legend). Tim Z xlsx written as `-ziemer-` for manual attach after validation.

## 5. Source coverage delta vs prior Monday

Per-segment audits flagged the following sources on a **2-week ✗ streak** (auto-flag if missed again 2026-06-15):
- **Greenhouse / Lever / Ashby job boards** — ✗ across Colo (#8), Fiber (#10), NeoCloud (#7), NetOp (#13), MSP (#12). Cross-segment recurring gap; the hiring-signal lane is effectively dark fleet-wide.
- **Colo:** #8 job boards, #10 hyperscaler feeds (2-week ✗).
- **NeoCloud:** #6 IX member pages, PeeringDB NC-A9 (2-run ✗).
- **Network Op:** NO-A5 GitHub commit feeds, NO-A8 FedBizOpps/SAM.gov, NO-A9 job boards (2-week ✗).
- **Enterprise:** sources 8, 10, 14, 22, 23, 25, 27, 29–32 (2-week ✗) — Enterprise has the thinnest realized coverage (~41%) of the six.

**Sources Needing Development (3-week ✗ streak):** none confirmed at 3 weeks yet — Greenhouse/Lever/Ashby is the leading candidate and will cross the threshold next Monday if still dark.

## 6. Anomalies

- **No per-segment audit files missing** (6/6 present).
- **No rep DM dispatch failures** (all 3 + threads sent clean).
- **`last_signal_date = today` is NOT a usable population filter** (re-confirmed): every per-segment audit carried the standing caveat that writes use EVENT dates (mostly backdated), so a today-only date query returns ~0. Aggregator keyed off the audit Writes summaries + the current Hot/Warm/Cool heat pool, per the 2026-06-04 reframe. This is the documented correct behavior, not a defect.
- **Score arithmetic:** audit Writes summaries (67 total) reconciled cleanly against the heat-pool population; no audit-vs-HubSpot count mismatch detected.
- **Heat-pinned (score 0 / blank) volume:** the Cool tail of each rep cap is partly filled by `hs_is_target_account` pins whose `last_signal_score` is 0/blank (Fiber-Connect-attendee artifacts, R1-onboarding stubs, and target accounts like Qubrid/FlexAI/SambaNova whose stored score is blank). They carry real heat but no current score — surfaced under a "Heat-pinned" group in each DM rather than dropped. **SambaNova (303377637098) stored `last_signal_score` is blank** — backfill candidate (also flagged by the NeoCloud scan).
- **Data-quality (Colo):** Equinix (303850136250) stored score 27 / heat Hot derives from a CFO appointment (Olivier Leonetti) — likely over-scored; flagged for manual correction / R-Tier-Audit awareness. Anti-churn correctly prevented a re-write.
- **Digi Power X domain inconsistency:** NeoCloud audit lists `digipower.com` in NEW detail vs `digipowerx.com` in the Colo cross-ref — verify the canonical domain on 326692012738.

## 7. R3 duplicate flags (for next 2am ET R3 run)

- **Orange Business / Orange Business Services** — 303410169565 (orange.com, Tier 1 Carrier) vs 318223391443 (orange-business.com). Signal written to the exact-domain match; recommend R3 merge.
- **JPMorgan Chase / J.P. Morgan & Co.** — 324628785885 vs 240446137023. Both held (avoids double-write).
- **Standing NeoCloud dedup pairs** (signal written to one record each, sibling untouched): Hut 8 (324208873163 / 323823823916), Bitfarms/Keel (298005835457 / 311386967793), Hive Digital (244551342805 / 316412310231), Soluna (303374043856 / 301205051103), Riot (297892337355 / 322537130689), DataCrunch/Verda (240435183333 / 318219155162 — both below floor, no write).

## 8. Apollo budget post-run

- **This run consumed:** 0 credits (signal-scan total sub-cap is 250/week; 0 drawn).
- **Remaining weekly capacity:** full 850 available less whatever R1/R2/R6/R8 draw across the rest of the ISO week. Signal-scan's 250 sub-cap is entirely unspent and will lapse for the week (NEW-account enrichment ran on free web research).

## 9. Tier 3 holds carryover

- **Per-segment Tier 3 holds appended to canvas this run:** 0 (no segment took or carried a signal-scan Tier 3 hold). 1 Colo carryover (Digi Power X) was re-routed to NeoCloud NC5 rather than re-appended. Canvas Run-log row append for this run **verified landed exactly once** (no double-write).

## 10. What needs Cooper's attention

1. **Validate the Tim Z cascade before forwarding** — 50 accounts, NeoCloud-sovereign-heavy (Nscale, IREN, NHN/Kakao/Naver/TELUS/DT/Core42 sovereign clouds). DM + xlsx are in `U0A24D9RJLS` and `weekly-reports/2026-06-08/`.
2. **Greenhouse/Lever/Ashby hiring-signal lane is dark fleet-wide (2-week ✗, all 6 segments).** It crosses the 3-week "Sources Needing Development" line next Monday. Worth deciding whether to fix the source path or formally retire the hiring lane.
3. **Two quick data-quality fixes:** SambaNova (303377637098) blank `last_signal_score` backfill, and the Digi Power X domain reconciliation (digipower.com vs digipowerx.com on 326692012738). Both small, both surfaced by per-segment scans this run.
