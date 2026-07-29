# CRM Ops Daily Digest — 2026-06-02

**Window:** Mon 2026-06-01 4:45 PM CT → Tue 2026-06-02 ~4:53 PM CT (prior ~24h).
**Dashboard canvas:** F0B7YMN4XEG (created this run — bootstrap; id needs hardcoding into prompt).
**Apollo:** 0 credits (read-only).

## Stage 1 — ground-truth deltas (HubSpot)
- Enriched / re-enriched (last_enriched_date >= 2026-06-02): 6
- Newly flagged for deletion (seg=Flagged + hs_lastmodifieddate >= 2026-06-01T21:45Z): 5
- Signal writes (last_signal_date >= 2026-06-02): 0
- Tier Δ: 0 · Heat Δ: 0 (R-Tier-Audit idempotent today)
- Segment Δ: ~5 (R1 Path α ICP writes)
- NEW accounts (createdate in window): 0
- Contacts touched (lastmodifieddate in window): 912
- Contacts flagged_for_deletion=true: 528

## Stage 2 — fleet health
| Routine | Last run CT | Status | Records | Apollo |
|---|---|---|---|---|
| R0 Import Validator | 6/2 9:02 AM | WARN | 9 scanned, 5 MATCH, 2 RENAMABLE, 2 T3 | 0 |
| R1 Fresh Enrichment | 6/2 10:09 AM | OK | 10/10, 5 ICP, 1 flag, 3 dedup T3 | 0/30 |
| R2 Stale Re-Enrichment | 6/2 11:03 AM | OK | 0 candidates (8th GREEN) | 0/50 |
| R4 Flagged Consolidation | 6/2 12:06 PM | WARN | 246 queue, 150 in-cap, 1 Mode B, 3 Mode A, 15 T3 | 0 |
| R-Tier-Audit | 6/2 3:04 PM | OK | 2,574 reviewed, 0 tier/0 heat | 0 |
| R3 Duplicate Accounts | 6/2 ~2 AM ET | OK | 3,367 scanned, 2 pairs, 28 contacts, 2 flags | 0 |
| R6 Territory & Hygiene | 6/2 ~1 AM ET | WARN | 636 NEW→OPEN, 44 cascades, 0 territory (model absent), 6 T3 | 0/5 |
| Daily Sales Activity Brief | 6/2 4:00 PM | OK (deliverable) | 5 held/0 set/10 up7d | n/a |
Not expected today: R5/R7/R8/R9/D7/Signal Scan.

## Stage 3 — Flagged-for-deletion queue (standing)
Total companies: 246 — reason split: 214 no-reason (legacy), 31 Duplicate (merged), 1 No ICP fit.
Contacts flagged: 528.
Verdict split not computed this run (too expensive). R4 same-day proxy: 77 zero-contact archive-ready vs 73 contact-bearing of 150 in-cap.
Filters: Companies customer_segment="Flagged for deletion"; Contacts flagged_for_deletion=true.

## Manual-review backlog
13 records (segmentation_confidence=manual_review_required), ~0.5% of active pool. No prior digest on disk — trend baseline starts today. D7 drains Wed 6/3.

## Anomalies
- R6 territory-model file absent → 0 territory corrections daily (recurring).
- Dashboard canvas created this run; DASHBOARD_CANVAS_ID still placeholder in prompt — reminder sent to Cooper.
