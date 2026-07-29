# Cooper Run Audit - Daily Sales Activity Brief - 2026-05-27 (Wed)

Run time: 2026-05-27 16:00 ET (Wed)
Status: ✅ SUCCESS - 3 of 3 DMs delivered, no MEDDPICC writes, no errors

## Window Computation

| Window | Start (ET) | End (ET) | Epoch ms |
|---|---|---|---|
| Held | 2026-05-26 16:00:00 | 2026-05-27 15:59:59 | 1779825600000 - 1779911999000 |
| Set | 2026-05-26 16:00:00 | 2026-05-27 15:59:59 | 1779825600000 - 1779911999000 |
| Upcoming | 2026-05-27 16:00:00 | 2026-06-03 16:00:00 | 1779912000000 - 1780516800000 |

## Engagement Pulls

| Pool | Object Type | Filter | Raw count | After filters |
|---|---|---|---|---|
| Held | CALL (hs_timestamp window) | 0 | 0 |
| Held | CALL (hs_createdate window) | 0 | 0 |
| Held | MEETING (hs_timestamp window) | 1 | 1 |
| Set | CALL (hs_createdate window) | 0 | 0 |
| Set | MEETING (hs_createdate window) | 6 | 6 |
| Upcoming | CALL (next 7d) | 0 | 0 |
| Upcoming | MEETING (next 7d) | 11 | 11 (1 dropped: Kyle internal) |

## Filtered Engagements

| Engagement ID | Title | Owner | Reason filtered |
|---|---|---|---|
| 371773858497 | MaiaEdge Onboarding & Billing Flow | Kyle Blackwell (159701452) | Untracked rep - filtered to audit only |

No internal-only-attendee filters fired this run (the EPS Global Dinner had external company + external contact, included).

## FRESH vs DEAL Classification

| Engagement | Title | Date (ET) | Owner | Classification | Reason |
|---|---|---|---|---|---|
| 371156031178 | EPS Global Dinner | 5/26 19:00 (HELD) | Tim L | FRESH | EPSGlobal company has no associated open deals |
| 371802892010 | ITW HGC Global Communications | 5/19 10:00 (SET-backfill) | Tim Z | FRESH | No HS company association, no deal |
| 371795700449 | ITW SBA Edge | 5/21 10:00 (SET-backfill) | Tim Z | FRESH | No HS company association, no deal |
| 371909524207 | Bell & MaiaEdge | 6/4 15:00 (SET+Upcoming) | Tim Z | FRESH | Bell - no associated deal |
| 371813082833 | Lunch (AT&T) | 6/1 13:30 (SET+Upcoming) | Tim Z | FRESH | AT&T - no associated deal |
| 371927577302 | MaiaEdge Update Chris/AT&T | 6/1 14:30 (SET+Upcoming) | Tim Z | FRESH | AT&T - no associated deal |
| 371835531965 | Broadstar/RocNet | 5/29 13:00 (SET+Upcoming) | Ken | FRESH | Broadstar+RocNet - no associated deal |
| 371640554182 | Technium POC | 5/28 12:00 (Upcoming) | Tim L | DEAL | Technium - Lab $5K presentationscheduled |
| 369403183813 | Verizon/Mplify | 5/28 15:00 (Upcoming) | Tim Z | FRESH | Verizon - no associated deal |
| 369406782164 | Imperium Data Intro | 5/28 15:30 (Upcoming) | Tim L | FRESH | Imperium - no associated deal |
| 369260239585 | Movi 5/28 | 5/28 16:30 (Upcoming) | Tim L | DEAL | Movi - CPE expansion $600K + 22x100G $400K |
| 369770144486 | Commercial Discussion (Acuutech) | 6/1 09:30 (Upcoming, PUSHED) | Tim Z | DEAL | Acuutech presentationscheduled (no amount) |
| 369684404951 | GDT Intro | 6/1 12:00 (Upcoming) | Ken | FRESH | GDT - no associated deal |
| 370631086828 | Myakka/Dragonfly | 6/2 10:00 (Upcoming) | Ken | FRESH | Myakka - no associated deal |

## Calendar Movement (vs 2026-05-26 snapshot)

| Movement | Engagement | Old Date (ET) | New Date (ET) | Owner | Notes |
|---|---|---|---|---|---|
| ⏩ PUSHED | Commercial Discussion (Acuutech) (369770144486) | 5/27 09:30 | 6/1 09:30 | Tim Z | DEAL presentationscheduled. 5-day push. Close date 4/30 already past. STALLING signal. |
| 🆕 NEW | Bell & MaiaEdge (371909524207) | n/a | 6/4 15:00 | Tim Z | Tier 1 Network Op (Quebec). First Bell engagement. |
| 🆕 NEW | MaiaEdge Update Chris/AT&T (371927577302) | n/a | 6/1 14:30 | Tim Z | Tier 1 AT&T. |
| 🆕 NEW | Lunch (AT&T) (371813082833) | n/a | 6/1 13:30 | Tim Z | Tier 1 AT&T. Generic title; AT&T associated. |
| 🆕 NEW | Broadstar/RocNet (371835531965) | n/a | 5/29 13:00 | Ken | Tier 5 Fiber (Broadstar) + MSP/Aggregator (RocNet). |

Note: EPS Global Dinner (371156031178) was in yesterday's Upcoming snapshot at 5/26 19:00 and now appears in today's Held pool - expected rollover, not flagged as movement.

## MEDDPICC Writes

**Zero writes this run.** The only held engagement (EPS Global Dinner) had no meeting body content (just an EPS standard email disclaimer), no outcome logged, no transcript. No transcript evidence available for any of the 8 MEDDPICC contact-level fields on either attendee (Alan Fagan, Tory Teague), so all field actions resolved to "Skip silently - topic never came up in this engagement" per the policy matrix.

Existing populated MEDDPICC on Alan Fagan (metrics_contact, competition_contact) and Tory Teague (metrics_contact, competition_contact) from prior calls preserved untouched.

| Tier | Field | Contact | Action | Reason |
|---|---|---|---|---|
| - | (all 8) | Alan Fagan (475276585695) | Skip | No transcript evidence in this engagement |
| - | (all 8) | Tory Teague (270047784644) | Skip | No transcript evidence in this engagement |

## Trend Baseline

| Status | BASELINE BUILDING |
|---|---|
| Prior weekday runs used | 2026-05-26 (Tue) |
| Missing | Memorial Day 5/25 (holiday), no other recent runs on disk |
| Required for trend tags | ≥3 prior weekday runs |
| Trend arrows in brief | OMITTED - no UP/DOWN/FLAT tags this run |
| Expected go-live | After 2026-05-29 (Fri) run completes |

## Activity Summary (per rep)

| Rep | Set | Held | Upcoming (7d) |
|---|---|---|---|
| Tim Lieto (161889085) | 0 | 1 | 3 (Technium 5/28, Imperium 5/28, Movi 5/28) |
| Ken Cunningham (162339176) | 1 | 0 | 3 (Broadstar/RocNet 5/29, GDT 6/1, Myakka 6/2) |
| Tim Ziemer (159350430) | 5 | 0 | 5 (Verizon 5/28, Acuutech 6/1, Lunch 6/1, AT&T Chris 6/1, Bell 6/4) |
| **TOTAL** | **6** | **1** | **11** |

Note on Tim Z's heavy Set: 2 of the 5 are ITW backfills (HGC Global 5/19, SBA Edge 5/21) - he's logging past ITW meetings retroactively. The other 3 (Bell, AT&T Lunch, AT&T Chris) are genuine future bookings. Pure forward-booking count for Tim Z is 3; the 5 figure is the formal Set count per spec.

## FOR YOU Routing Log

| Item | Recipient | Reason |
|---|---|---|
| Acuutech PUSH 5 days | Tim Z | His own deal slipping; STALLING signal |
| Tim Z heavy load-ahead | Tim Z | Self-awareness of week's cadence |
| Movi $1M tomorrow | Tim Z + Abilash | Tim Z (sync with Tim L) + Abilash (CEO wants million-dollar conversation visibility) |
| Technium POC tomorrow | Tim Z | POC conversion engine awareness |
| AT&T motion 3 touchpoints | Abilash | Strategic logo concentration |
| Bell 6/4 first engagement | Abilash | Strategic Tier 1 logo |
| Verizon/Mplify tomorrow | Abilash | Strategic Tier 1 logo |
| ITW backfill associations missing | Cooper | RevOps data quality nudge |
| Movi company record missing | Cooper | Recurring data quality flag |
| Trend baseline status | Cooper | Routine health monitoring |
| Kyle Onboarding filter | Cooper | Routine health (no action needed) |

Items per recipient: Tim Z 4 | Abilash 4 | Cooper 4. All within 4-item cap, no overflow.

## DM Delivery Log

| Recipient | Slack User | DM Channel | Message TS | Status |
|---|---|---|---|---|
| Cooper Kennedy | U0A24D9RJLS | D0A2YNL1TA4 | 1779916150.109309 | ✅ delivered |
| Abilash Menon | U06RVK9NTQR | D0A2YNPVB96 | 1779916168.151419 | ✅ delivered |
| Tim Ziemer | U08CMD5PMQE | D0A2817RE68 | 1779916186.840329 | ✅ delivered |

No retries triggered. All 3 delivered cleanly.

## Notes for Cooper

1. **Acuutech deal hygiene.** Tim Z's Acuutech deal (Commercial Discussion meeting) just slipped 5 days. The deal is in presentationscheduled stage, 2.5 months old (created 3/5), no amount, and its forecast close date 4/30 is already in the past. This is the textbook STALLING profile - R-Tier-Audit's open-deal modifier and signal_heat should already be reflecting heat decay. Worth a manual check that the tier+heat compute caught it.

2. **Movi company record absence.** Same flag as yesterday - $1M associated to tomorrow's meeting but no findable company record by name search. The associated company id should appear in the meeting's company association graph; consider running R3 / R6 query to surface the actual record.

3. **ITW backfills.** Tim Z is processing post-ITW notes 5+ days after the event. The 2 backfilled meetings (HGC Global Communications 5/19, SBA Edge 5/21) have no HubSpot company associations - those prospects don't have records yet, or weren't linked. Worth a Cooper ask to Tim Z: "Want me to source HGC and SBA Edge into HubSpot so these meetings have real homes?"

4. **AT&T concentration.** Tim Z booked 3 separate AT&T touchpoints today (Lunch 6/1 + Chris Update 6/1 + the existing Verizon/Mplify 5/28 wasn't AT&T). Actually checking: Verizon/Mplify is Verizon. So 2 AT&T meetings + Verizon (separate Tier 1) + Bell. International territory is loud this week.

5. **No held calls of substance.** The single held engagement was a relationship dinner with no notes. This is a thin day for call intelligence - the brief leans entirely on the calendar movement section for narrative.

6. **Internal-Only Filter calibration.** The EPS dinner included Tory Teague (cloud sales consultant, toryteague.com domain - external) and Alan Fagan (EPS Global - external). Filter correctly retained the meeting. Kyle Blackwell's onboarding meeting (5/29) was filtered as untracked-rep, not strictly "internal-only" - but Kyle's recurring onboarding/billing meetings are operationally internal regardless.
