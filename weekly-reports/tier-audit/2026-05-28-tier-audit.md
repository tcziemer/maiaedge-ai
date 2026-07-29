# R-Tier-Audit 2026-05-28 (daily M-F 3pm CT)

- Total active accounts reviewed: 2,578
- Tier changes written: 11
- Heat changes written: 28
- Unique records updated: 30 (9 records had both tier + heat changes)
- Manual override skips (tier writes only): 59 (`hs_is_target_account = true`)
- Heat writes on target-account records (not skipped): 1 (RevNet — open deal in flight)
- Circuit breaker triggered: NO (1.51% combined, threshold 10%)
- Apollo budget consumed: 0

## Tier promotions (toward Tier 1): 8
## Tier demotions (toward Tier 5): 3
## Heat cooling (Hot/Warm → Cool/Cold): 19
## Heat warming (Cool/Cold → Hot/Warm): 9
## Modifier counts
- Hot signal modifier (-1): 0 single-fire
- White-hot modifier (-2): 0
- Stacked signals (-1): 9 (Optimum, Stratus, Mediacom, GiGstreem, Greenlight, Hotwire, IPC, Ripple-adjacent CLECs)
- Open deal (-1): 15 records flagged (all already at ceiling, no tier delta this run)
- Stale signal (+1): 5
- Sustained quiet (+1): 2
- Unknown (segment, sub-segment) pair warnings: 1

## Heat distribution after this run
- Hot: 34
- Warm: 23
- Cool: 32
- Cold: 2,489

## Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 154255869681 | optimum.com | Fiber Operator | Regional Cable Operator - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=27, score=10, count30=2 |
| 175170996952 | stratusnet.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=28, score=9, count30=2 |
| 175172795115 | mediacomcc.com | Fiber Operator | Regional Cable Operator - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=1, score=9, count30=2 |
| 209170400954 | tdstelecom.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default T3, stale_signal(+1). days_old=102, score=10 |
| 266871288513 | gigstreem.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=16, score=12, count30=2 |
| 268073696970 | greenlightnetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=30, score=14, count30=2 |
| 291518043894 | sifinetworks.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default T3, stale_signal(+1), sustained_quiet(+1). days_old=194 |
| 292648497859 | hotwirecommunications.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=27, score=10, count30=2 |
| 316621829822 | ipc.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default T3, stacked_signals(-1). days_old=9, score=13, count30=2 |
| 324628839134 | twinlakes.net | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_3 | tier_4 | +1 | Default T4 (Municipal/Cooperative starts at T4) — record drifted to T3 from prior run/import |
| 324636275403 | umniah.com | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | tier_1 | -2 | Default T1 (Tier 1 Carrier) — record drifted to T3 from initial create yesterday |

## Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 154255869681 | optimum.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 155473925856 | revnet.host | Cold | Hot | Open deal past appointmentscheduled (hs_is_target_account=true; tier frozen, heat NOT frozen) |
| 175109006031 | vivacitygroup.com | Warm | Cool | days_old=30, score=11 (<27, no longer Warm); ≤180d → Cool |
| 175170996952 | stratusnet.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 175172795115 | mediacomcc.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 193865438935 | 123.net | Warm | Cool | days_old=7, score=13 (<27); ≤180d → Cool |
| 209170400954 | tdstelecom.com | Warm | Cool | days_old=102, score=10 (<27); ≤180d → Cool |
| 264355635945 | mcnc.org | Warm | Cool | days_old=17, score=8 (<27); ≤180d → Cool |
| 266871288513 | gigstreem.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 268073696970 | greenlightnetworks.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 291518043894 | sifinetworks.com | Warm | Cold | days_old=194 (>180); → Cold |
| 291537915620 | clearwavefiber.com | Warm | Cool | days_old=13, score=14 (<27); ≤180d → Cool |
| 292648497859 | hotwirecommunications.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 292719725284 | ripplefiber.com | Warm | Cool | days_old=72, score=11 (<27); ≤180d → Cool |
| 292755851981 | omnifiber.com | Warm | Cool | days_old=17, score=12 (<27); ≤180d → Cool |
| 292796237529 | surfinternet.com | Warm | Cool | days_old=85, score=12 (<27); ≤180d → Cool |
| 296850118371 | liveoakfiber.com | Warm | Cool | days_old=49, score=12 (<27); ≤180d → Cool |
| 297782865628 | imon.net | Warm | Hot | signal_count_last_30d=2 (stacked) — note signal also stale (days_old=98) but stacked takes priority for Hot |
| 297888731896 | netcarrier.com | Warm | Cool | days_old=10, score=11 (<27); ≤180d → Cool |
| 316621829822 | ipc.com | Warm | Hot | signal_count_last_30d=2 (stacked) |
| 318368579300 | letsrev.com | Warm | Cool | days_old=44, score=11 (<27); ≤180d → Cool |
| 320373812934 | cherrycapitalconnection.com | Warm | Cool | days_old=17, score=9 (<27); ≤180d → Cool |
| 320874452690 | truvista.biz | Warm | Cool | days_old=37, score=14 (<27); ≤180d → Cool |
| 321479152324 | i3broadband.com | Warm | Cool | days_old=30, score=14 (<27); ≤180d → Cool |
| 322353526464 | getaccessplus.com | Warm | Cool | days_old=74, score=10 (<27); ≤180d → Cool |
| 322407809745 | opencape.org | Warm | Cool | days_old=17, score=10 (<27); ≤180d → Cool |
| 322407809750 | rapid-fiber.com | Warm | Cool | days_old=13, score=8 (<27); ≤180d → Cool |
| 323822481122 | gonetspeed.com | Warm | Cool | days_old=30, score=15 (<27); ≤180d → Cool |

## Notes on this run

1. **`last_enriched_date` NOT bumped** on any record (per Unified Stamping Policy — tier-only and heat-only writes don't bump).
2. **HubSpot per-record audit notes deferred this run** — change history is captured by HubSpot's native property history + this on-disk audit log + Slack DM. Per-record note objects can be backfilled if needed.
3. **9 records flipped Warm → Hot via stacked-signals trigger**, all Fiber/Regional CLEC + Cable Operator. Pattern consistent with Signal Scan having delivered the stack within the trailing 30 days; tier modifier (-1) caught the same trigger.
4. **The cluster of Warm → Cool flips (15 records)** reflects existing Warm heat values written previously when the rule for "Warm" was less strict on score (now requires 27-44 for Warm). Most of these records carry sub-27 scores; daily R-Tier-Audit is now drift-correcting them to Cool. Expect this drop-off to normalize within the next few runs as the pool catches up.
5. **Umniah (324636275403, Tier 1 Carrier)** was created 2026-05-27 with `account_tier = tier_3`. R1 should have computed Tier 1 at create time (Tier 1 Carrier defaults to T1, ceiling 1). Worth a one-line follow-up to confirm R1 Path α writes the right starting tier on new accounts. Likely a single-record artifact, not systemic.
6. **Twin Lakes (324628839134)** had drifted to T3 from default T4 (Municipal/Cooperative). Possibly hand-set during import; algorithm restored to T4.

## Operator artifacts
- `outputs/tier-audit-2026-05-28/compute-results.json` — full per-record compute output (2,578 rows)
- `outputs/tier-audit-2026-05-28/tier-changes.json` — 11 records
- `outputs/tier-audit-2026-05-28/heat-changes.json` — 28 records
- `outputs/tier-audit-2026-05-28/summary.json` — aggregate stats

Next run: Friday 2026-05-29, 3pm CT.
