# CRM Ops Daily Digest — 2026-06-11

Window: since 2026-06-10 16:45 CT (prior ~24h). HubSpot = ground truth. Read-only on HubSpot; Apollo 0.

## Stage 1 — Ground-truth deltas (window)
- Enriched / re-enriched (`last_enriched_date >= 2026-06-11`): **39** (R2 37 + R1 2; all of today's stamps are in-window since enrichment runs 9am–3pm)
- Newly flagged for deletion: **+4 net** (standing pool 301 → 305). All 4 = R2 No-ICP-fit evictions (PowerBridge, Backbone Digital, EIS Visual, Exa wrong-entity Dassault-CFD). 6 flagged records had in-window modifications total.
- Signal writes (`last_signal_date >= 2026-06-10`): **0** (Monday-only cadence; normal Thursday)
- Tier Δ: **7** — 5 R-Tier-Audit (3 open-deal promotions: Gigabit Fiber, Wisper ISP, HTC T4→T3; 2 stale demotions: RadiusDC T1→T2, Dynascale T3→T4) + 2 R1 new-account seeds (Mosaic tier_4, Nextlink tier_3). Heat Δ: **5** + 2 Cold seeds.
- Segment Δ: **6** (2 R1 ICP classifications + 4 R2 evictions). Confidence Δ: 2 R2 upgrades (T-Systems, Madison→high_90) + 3 manual_review stubs.
- Companies modified in window (`hs_lastmodifieddate >= 2026-06-10T21:45Z`): **180**
- NEW accounts (`createdate >= window`): **9** — 4 evening imports 06-10 (Lumos, Long Lines, Anthem, Mosaic — processed by today's R0/R1), 1 routine re-create (Nextlink Internet, R1 MISDOMAIN Tier 1 fix), 4 mid-day imports today AFTER R0's 9am pass (Grantsburg Telecom, Union Transtel, inlandcell.com, ftmojave.net) → tomorrow's R0/R1 pool.
- Contacts touched (`lastmodifieddate >= window`): **439**. Flagged contacts (`flagged_for_deletion = true`): **346** (327 → 346, +19 net; R4 Mode B set 54 new flags, 266 idempotent confirms per run report).
- Manual-review backlog (`segmentation_confidence = manual_review_required`): **3** (Anthem Business Group 326986523374, Lumos Networks 326675592899, Long Lines Broadband 326675587819 — today's R1 R3-dedup stubs, deliberate).

## Stage 2 — Fleet health
| Routine | Last run (CT) | Status | Records touched | Apollo |
|---|---|---|---|---|
| R0 Import Validator | 06-11 09:02 | ⚠️ | 9 scanned · 3 HIGH renames · 1 MATCH · 5 QA-fixture T3 holds · 5 carryovers drained · 0 errors (self-graded YELLOW on holds only) | 0 |
| R1 Fresh Enrichment | 06-11 10:09 | ✅ | 9/9 drained (22 raw − 13 standing-hold excludes) · 2 ICP writes · 7 T3 holds (3 dedup stubs + 4 QA) · 0 evictions | 0/30 |
| R2 Stale Re-Enrichment | 06-11 11:03 | ✅ | Filter-C pre-spread: 40 taken of 45 (pool 3,412), 37 written, 5 deferred · FULL×2 · 4 evictions · 12 brief-fixes | 0/50 |
| R4 Flagged Consolidation | 06-11 12:06 | ⚠️ | 150/305 (cap) · 359 contacts evaluated · 54 Mode B flags · 6 reassociations · 33 T3 holds · ~155 carryover (~1 run) | 0 |
| R10 Completeness Sweep | 06-11 13:31 | ✅ | 0 ICP candidates — pool 2,864 complete on trigger fields, gap 0%, breaker clear | 0/25 |
| R-Tier-Audit | 06-11 15:05 | ✅ | 5 tier + 5 heat of 2,862 (0.3%, breaker 286 clear) · connector healthy (signal-date pop 243 verified) | 0 |
| R3 Duplicate Accounts | 06-11 02:00 ET | ✅ | 3,733 scanned · 0 new HIGH (idempotent) · 1 T3 closed (Hotwire) · 3 new T3 (Mid-Plains, nicos, HyperLink) | 0 |
| R6 Territory & Hygiene | 06-11 ~01:00 ET | ✅ | 2 owner corrections (Anthem Business Group→Ken/West, longlines.biz→Lieto/East) · 1 state fill (lumosnet.com VA) · 1 QA hold | 0/5 |

Fleet: 8/8 expected fired (scheduler lastRunAt cross-checked for all Cowork tasks; R3/R6 confirmed via ledger rows — not inferred). Daily Sales Activity Brief dispatched 06-10 18:01 CT ✅ GREEN (3 held / 4 set / in-window); today's fires 18:00 CT post-digest. Not expected today: D7 (Wed — ran 06-10 09:01, prior window, 30 resolved), R5 (Sun), R8 (Fri), R7 (1st), R9 (qtr), Signal Scans (Mon), Weekly Market News (Fri). Apollo W24: 0/850, all routines 0.

## Stage 3 — Flagged-for-deletion queue (standing pool)
**305 companies + 346 contacts.**
| Reason code | Companies |
|---|---|
| Duplicate (merged) | 107 |
| No ICP fit | 77 |
| D1 disqualified (no reference value) | 74 |
| Defunct / out of business | 31 |
| Hard junk / non-business | 14 |
| Dead domain | 2 |
| Stalled greenfield | 0 |
| (empty reason) | 0 |

Breakdown via leading-code parse + R3-prefix fallback over full 305-record pull (2 pages, sorted hs_object_id ASC). 304 parsed direct; 1 page-2 record pinned to No ICP fit by delta reconciliation (301 + 4 No-ICP evictions = 305 exactly; all other codes unchanged vs 06-10). SAFE_TO_DELETE split not computed this run. Open-deal carve-out: Bits in Flight (326674182894) — flagged, has OPEN deal "H5 Data Centers - Partner Reg" → do not delete.
Filters → Companies: `customer_segment = "Flagged for deletion"`; Contacts: `flagged_for_deletion = true`.

## Attention
1. **5 ZZZ QA fixtures await Cooper disposition** (zzz-qa-retest-conflict/-retest-clean/-conflict-prospect/-happy-prospect/-prospect-b, created 06-10 17:25–20:17 UTC). R0/R1/R6 all independently HELD with no HubSpot writes to avoid contaminating QA state. Confirm: keep / delete / flag.
2. **HyperLink R1-vs-R3 conflict** (T3-2026-06-11-003): R1 flagged HyperLink Infrastructure LLC (316164220626) No-ICP-fit before R3 caught HIGH name-dup vs active Hyperlink Infrastructure (298009434824, Fiber Operator, 3 contacts). If same entity: reassociate contacts pre-delete.
3. No missed fires, no circuit breakers, no failed dispatches, no Apollo consumption.

## Manual-review backlog trend
26 (06-05) → 33 (06-08) → 33 (06-09) → 0 (06-10) → **3 (06-11)**. The 3 are deliberate R1 dedup stubs routed to R3 (not classification ambiguity). Record for next trend: 3.

## Run metadata
- Working ledger F0B0AFSB9LN read OK this run (947K chars via saved tool-result file; headers + tail sections parsed in full — first successful full-ledger read since 06-09).
- R4 count note: ledger row says "54 net-new flags" = contact-level Mode B writes (54 new + 266 idempotent confirms = 320 on its 150-company page); company pool delta is +4 (R2 evictions only).
- Dashboard canvas F0B7YMN4XEG refreshed (full replace) 2026-06-11 16:55 CT.
- DM sent to Cooper (U0A24D9RJLS) 16:55 CT. Apollo W24: 0/850.
