# CRM Ops Daily Digest — 2026-06-17

**Run time:** 2026-06-17 16:56 CT
**Window:** since Tue 2026-06-16 4:45 PM CT (date floor 2026-06-16 CT; spans 06-16 + 06-17 to-date)
**Apollo:** W25 (start 2026-06-15) = 2 / 850 consumed (0.2%), 848 remaining. 0 Apollo used by this digest.
**MCP health:** HubSpot ✅ reachable · Slack ✅ reachable (ledger read OK, dashboard write OK, DM OK).

---

## Stage 1 — Ground-truth deltas (HubSpot)

| Metric | Count | Source / note |
|---|---|---|
| Enriched / re-enriched (`last_enriched_date` ≥ 2026-06-16) | **93** | search_crm_objects total. Spans 06-16 + 06-17; dominated by R2 Filter-C re-stamps (~39/day) + R10/R1. |
| Newly flagged for deletion (window) | **14** | Net pool delta 341 → 355. Reconciled to R3 8 dedup + D7 6 dup-merged evicts. All "Duplicate (merged)". |
| Signal writes (`last_signal_date` ≥ 2026-06-16) | **0** | No signal scan since Mon 06-15; no outreach push-backs in window. |
| Tier moves | **1** | R-Tier-Audit 06-17 (authoritative daily reconciler), 0.07%, breaker not tripped. |
| Heat moves | **1** | R-Tier-Audit 06-17. R2 re-stamped 39 heat=Cold (idempotent on already-Cold). |
| Segment moves | **14** → Flagged + 8 D7 manual-review cleared (6 EVICT + 2 reclass) | From routine reports. |
| NEW accounts (`createdate` ≥ 2026-06-16) | **9** | search_crm_objects total. |
| Contacts touched (`lastmodifieddate` ≥ 2026-06-16) | **12,121** *(noise)* | ≈ entire contact base → HubSpot-wide property/recompute bump, NOT routine activity. Genuine routine contact writes ~dozens (R3 16 reassoc, R6 1, R4 evals). NOT surfaced as a real metric. |
| Contacts flagged for deletion (standing) | **376** | was 374 (06-16), +2. |
| Manual-review backlog (`segmentation_confidence = manual_review_required`) | **2** | was 8 (06-16). D7 drained 8→0; R1 added 2 (Nextlink Internet, Schwarz Digits). |

**Methodology note:** the spec's literal "newly flagged = customer_segment EQ Flagged AND hs_lastmodifieddate ≥ WINDOW_START" returns the entire 355-record pool, because R4's daily re-affirmation pass bumps `hs_lastmodifieddate` on every flagged record. Used net-pool-delta (+14) reconciled against today's flagging actions (R3 8 + D7 6) instead. Tier/heat/segment per-field attribution via search API is impossible (hs_lastmodifieddate is bumped org-wide), so those counts come from the authoritative routine reports.

---

## Stage 2 — Fleet health (9 ops routines expected today, Wed)

| Routine | Last run (CT) | Status | Records touched | Apollo |
|---|---|---|---|---|
| R6 Territory & Hygiene | Wed 1:00a ET | ✅ | 2 owners corrected (Currency.com→Ziemer, digits.schwarz→Ziemer) · 1 state fill (Nextlink, Apollo) · 1 contact cascaded | ~1 / 5 |
| R3 Duplicate Accounts | Wed 2:00a ET | ✅ | 3,753 scanned · 8 HIGH pairs consolidated · 16c reassociated · 8 dups flagged · 24 writes · 0 err · 0 new T3 (37 carry) | 0 |
| R0 Import Validator | Wed 9:02a | ✅ | 3 fresh imports · 2 RENAMABLE renamed (Schwarz Digits) · 5 zzz-qa holds resolved (4 standing) | 0 |
| D7 Edge Case Resolution | Wed 9:00a | ✅ | 8 P1 resolved · manual-review 8→0 · 6 EVICT (dup-merged: Long Lines, Lumos, Anthem, Midtel, Grantsburg, +1) | 0 |
| R1 Fresh Enrichment | Wed 10:08a | ⚠️ YELLOW | 2/100 processable · 0 ICP writes · 0 evict · 2 NEW T3 dedup holds → R3 (Nextlink Internet, Schwarz Digits) | 0 / 30 |
| R2 Stale Re-Enrichment | Wed 11:02a | ✅ | 39 re-stamps (Filter C pre-spread) · 1 NEW T3 (New Era Helium → Cooper/D7) · 6 standing holds carried | 0 / 50 |
| R4 Flagged Consolidation | Wed 12:05p | ✅ | 355 flagged (125 zero-contact archive-ready / 230 w-contacts) · Mode A 119 dups/436c preserved · Mode B 82 processed | 0 |
| R10 Completeness Sweep | Wed 1:31p | ✅ | 0 writes (ICP pool clean, idempotent; non-ICP blanks excluded by loop fix) · 0 tiers seeded · 0 partials · 1 DQ flag → Cooper (Sumauma) | 0 / 25 |
| R-Tier-Audit | Wed 3:26p | ✅ | 2,844 active ICP reviewed (2 type=Customer excluded) · 1 tier · 1 heat · 0.07% · breaker (284) not tripped | 0 |

**8 of 9 green; R1 yellow (benign).** No routine failed to fire; no 🔴 errors.

**Not expected today (correctly idle):** Signal Scan (Mon), R5 (Sun), R8 (Fri), R7 (1st of month), R9 (quarterly), Weekly Market News (Fri), Smartlead Health (Tue/Thu).

**Rep deliverable:** Daily Sales Activity Brief scheduled 6:00 PM CT (cron-confirmed nextRunAt today 23:00 UTC); not yet fired at digest time (16:56 CT) — on schedule.

**Day-over-day improvements vs 06-16 digest:** R4 recovered ⚠️ read-only → ✅ green; R10 recovered ⚠️ circuit-breaker HOLD → ✅ green (ICP pool clean); D7 fired (Wednesday cadence) and drained manual-review.

---

## Stage 3 — Flagged-for-deletion queue (standing, full pool)

**Companies: 355 · Contacts: 376.** Exact parse of all 355 (4 pages, sum-checked).

| Reason code | Companies |
|---|---|
| Duplicate (merged) | 131 |
| No ICP fit | 79 |
| D1 disqualified (no reference value) | 71 |
| Defunct / out of business | 32 |
| Hard junk / non-business | 16 |
| Dead domain | 3 |
| Stalled greenfield | 0 |
| Legacy `R3 2026-06-08:` dup prefix (non-canonical) | 23 |
| Empty / missing reason | 0 |
| **Total** | **355** |

- The 23 legacy `R3 2026-06-08:` records (16 "Normalized name match" + 7 "Exact domain match") are functionally Duplicate (merged) → duplicate-class total **154**. A one-time normalization pass would fold these into the canonical code. Logged as a minor data-hygiene opportunity (not an action item).
- 0 empty-reason flags — `flagged_for_deletion_reason` companion-write discipline holding at 100%.
- **SAFE_TO_DELETE vs needs-review split: NOT computed this run** (per-record deal/activity/attachment checks too expensive at 355). Cheap proxy from R4's own run: **125 zero-contact (clean archive now) / 230 carry contacts** (R4 preserves active/ICP-linked first).
- HubSpot filters: Companies → `customer_segment = "Flagged for deletion"` (archive); Contacts → `flagged_for_deletion = true` (bulk-delete).

---

## Manual-review backlog trend

| Date | manual_review_required count |
|---|---|
| 2026-06-16 | 8 |
| **2026-06-17** | **2** |

Trend ↓ (D7 drained 8→0; R1 added 2 dedup holds → R3). Healthy, not growing. Not an Attention item.

---

## Anomalies / notes

1. **Contacts-touched = 12,121** is a HubSpot org-wide `lastmodifieddate` bump (≈ entire contact base), not routine activity. Suppressed from "Today at a glance" as a real metric. If it recurs, worth a one-line check that it's a benign property recompute (not a runaway routine).
2. **Newly-flagged literal query** returns whole pool (R4 daily re-touch noise) — used net-delta + routine reconciliation. Carry this method forward.
3. **R6 Apollo (Nextlink state fill, ~1 cr)** not yet reflected in apollo-budget.json (shows 2). Negligible vs 850 cap.
4. Awareness items routed to Cooper (on dashboard, no digest action): R10 Sumauma DQ flag; R2 New Era Helium reclass (oil/gas → AI-DC, Sharon AI JV).

---

## Attention summary

**All clear** — no failed fires, no errors, Apollo 2/850 (0.2%), manual-review shrinking 8 → 2.
