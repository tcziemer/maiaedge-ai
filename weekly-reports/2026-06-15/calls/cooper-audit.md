# Daily Sales Activity Brief — Cooper Audit — 2026-06-15 (Mon)

## Run summary
- Fire: 2026-06-15 19:00 ET (6:00 PM CT). Weekday check PASS.
- Held window: 2026-06-12 16:10 ET -> 2026-06-15 19:00 ET (rolling prior-run -> now; Monday weekend catch-up ~72h, gapless).
- Watermark continuity: PASS. held_start (6/12 16:10 ET) == Friday run held_end (6/12 16:10 ET). No gap back-fill. (Friday fired early at 16:10 ET, so Fri-evening activity is correctly captured here.)
- Late-log catch-up window (createdate): 6/12 16:10 -> 6/15 19:00 ET; event lookback floor 2026-06-01.
- Delivery: GREEN. All 6 DMs first attempt.
- Totals: Held 5 (4 FRESH / 1 DEAL) · Set 4 (3 FRESH / 1 DEAL) · Upcoming 8.

## Per-rep activity
| Rep | Set | Held | Up7d |
|---|---|---|---|
| Tim Lieto (161889085) | 3 | 2 | 3 |
| Ken Cunningham (162339176) | 0 | 0 | 0 |
| Tim Ziemer (159350430) | 0 | 3 | 3 |
| Markus Hendrich (164949459) | 1 | 0 | 2 |
| TOTAL | 4 | 5 | 8 |

## FRESH/DEAL classification log
| Engagement | Pool | Owner | FRESH/DEAL | Basis |
|---|---|---|---|---|
| Cirrascale (CALL 375973892802) | Held | Tim L | FRESH | no associated deal |
| Socket Fiber (CALL 375974098629) | Held | Tim L | FRESH | no associated deal |
| Fusion Broadband SA (CALL 375911640772) | Held | Tim Z | DEAL | open deal 324841512688 @ presentationscheduled |
| NTT / Yuta (MEETING 375905805049) | Held [late log] | Tim Z | FRESH | no deal |
| Verizon / Scott (MEETING 375917926102) | Held [late log] | Tim Z | FRESH | no deal |
| Ecoblox (MEETING 375900414684) | Set+Up7d | Tim L | FRESH | no deal |
| ambiFOX (MEETING 375918337767) | Set+Up7d | Markus | DEAL | open deal 323417141980 @ presentationscheduled ($50k) |
| Globalgig (MEETING 375964040925) | Set+Up7d | Tim L | FRESH | no deal |
| ConRes / Lunch (MEETING 375972764394) | Set+Up7d | Tim L | FRESH | no deal (company created today) |

## Trend baseline (LIVE — 5 prior weekday runs 6/8-6/12)
- Averages: held_fresh 2.0, held_deal 0.6, set_fresh 1.8, set_deal 0.8.
- Today: held_fresh 4 (UP), held_deal 1 (FLAT, abs diff <1), set_fresh 3 (UP), set_deal 1 (FLAT).

## MEDDPICC writes (silent side effect) — 6 Tier 1 fills, 2 contacts
| Contact | Company | Fields filled | Notes |
|---|---|---|---|
| Al Lucarelli (499028845289) | Cirrascale | meddpicc_pain_contact, meddpicc_infrastructure_contact | competition + use_case smart-filled today (match -> skip); criteria + metrics ambiguous (skip). No deal -> contact-level only. |
| Steve Bremer (492002195149) | Socket Fiber | meddpicc_pain_contact, meddpicc_use_case, meddpicc_competition_contact, meddpicc_infrastructure_contact | All 6 empty pre-write. criteria (next-step, not stated) + metrics (none quantified) skipped. No deal -> contact-level only. |

MEDDPICC skips:
- Fusion Broadband contact(s): empty-content recording, no evidence -> skip.
- Yuta Yamagishi (NTT, 502191387339): conference note, no MEDDPICC category stated -> skip.
- Scott Lawrence (Verizon, 492087057130): 'Ethernet over 5G' too exploratory to attribute -> skip (confidence guard).

Write result: manage_crm_objects updateRequest, 2 contacts, 2 updated / 0 failed, CONFIRMATION_WAIVED_FOR_SESSION. last_enriched_date NOT bumped (contact-level MEDDPICC only).

## Calendar movement (vs Friday 6/12 snapshot)
- NEW (4): Ecoblox (T1 AI colo, Tim L, 6/16) · ambiFOX (T2 MSP + $50k deal + active POC, Markus, 6/16) · Globalgig (T2 MSP, Tim L, 6/19) · ConRes (unclassified, Tim L, 6/16).
- PUSHED / PULLED IN / DROPPED: none.
- Transitioned to held (audit only): Cirrascale (6/15 16:00) · Fusion (6/15 12:00).
- Carryover upcoming unchanged: Arc Compute 6/16, Pearce 6/16, FiberLight 6/17, Bouygues 6/17.

## Calendar-connection health (Stage 2.6)
- Tim Lieto: healthy (Cirrascale HUBSPOT_MEETINGS + 3 bookings). FLAG: Socket Fiber held call hand-logged (INTEGRATIONS_PLATFORM, manual notes, no MEETING twin) — the Socket pattern; routed to Cooper.
- Ken Cunningham: non-zero trailing 7d (702 6/12, Myakka+United 6/10). 0 activity THIS window — silence, not a calendar-health flag. FOR YOU omitted (0 owned items).
- Tim Ziemer: non-zero (Fusion HUBSPOT_MEETINGS + Arc/Pearce/FiberLight bookings). The 2 Mplify late-logs are CRM_UI manual conference notes (expected, not calendar-sourced).
- Markus Hendrich: non-zero (ambiFOX + Bouygues bookings). Untitled 6/16 artifact persists.
- Zero-calendar-sourced reps: none.

## Data hygiene flags (Cooper)
1. NTT (Yuta Yamagishi 502191387339) + Verizon (Scott Lawrence 492087057130) contacts have NO associated company record — link to NTT / Verizon company records. Both Tier 1 carriers Tim Z is networking into via Mplify Lisbon.
2. Socket Fiber held call hand-logged, not calendar-sourced (calendar-sync watch — would have auto-created if Tim L's calendar were syncing).
3. "Meat" personal recording (Tim Z + Andy Epstein, personal gmail, no company) — recommend delete.
4. Markus untitled 6/16 meeting 374360388287 — recurring artifact; recommend delete.

## FOR YOU routing log
- Abilash: Tier 1 logo momentum (Cirrascale + Ecoblox/Arc/Bouygues); NTT + Verizon senior contacts warmed at Mplify Lisbon. (2 items)
- Tim Z: convert NTT (Yuta) + Verizon (Scott SVP) hallway interest to booked sessions; loaded week Arc/Pearce/FiberLight; Fusion touch-base empty - re-log. (2 items)
- Cooper: Socket calendar-sync watch; NTT+Verizon missing company record; Meat + Markus artifact delete; MEDDPICC 6 fills + trend LIVE + watermark continuous. (4 items, cap)
- Tim Lieto: Cirrascale demo priority; Socket PBC business case + Equinix port; 3 fresh meetings booked this week. (3 items)
- Ken Cunningham: OMITTED (0 owned items this window).
- Patrick Timmons (PT): ambiFOX active POC + 6/16 sync + $50k deal; Fusion POC quiet since 6/5 + empty touch-base status check. (2 items)

## DM links
- Abilash: https://maia-edge.slack.com/archives/D0A2YNPVB96/p1781565588428309
- Tim Z: https://maia-edge.slack.com/archives/D0A2817RE68/p1781565613935639
- Cooper: https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781565630900859
- Tim Lieto: https://maia-edge.slack.com/archives/D0A9UNDR5EW/p1781565653251409
- Ken Cunningham: https://maia-edge.slack.com/archives/D0AE4AGC5KJ/p1781565666996009
- Patrick Timmons: https://maia-edge.slack.com/archives/D0A28180WG4/p1781565682033899

## Tooling notes
- query_crm_data cross-object SELECT with `hs_object_id IN (...)` returned repeated HubSpot internal errors; pivoted to search_crm_objects `associatedWith` for all association hydration (reliable, used throughout).
- Slack canvas F0B0AFSB9LN read returned >1M chars (oversized for inline read); run-log section located via saved tool-result file; row appended at canvas end per the per-routine dated-section pattern.
- DMs sent with standard markdown (**bold**, fenced code blocks) per the connected Slack MCP contract; converts to Slack mrkdwn server-side.
