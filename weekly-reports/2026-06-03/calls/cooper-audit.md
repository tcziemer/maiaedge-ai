# Cooper Audit - Daily Sales Activity Brief - 2026-06-03 (Wed)

## Run meta
- Run time: 2026-06-03 ~17:01 ET (nominal cadence 4pm CT = 5pm ET)
- Held window: 2026-06-02 16:00 -> 2026-06-03 15:59 ET (24h Tue-Fri standard)
- Set window: same as held; measured on true MEETING bookings created in window, excluding auto call-logs whose createdate equals meeting time (consistent with prior-run methodology)
- Upcoming window: 2026-06-03 17:01 -> 2026-06-10 17:01 ET. Upcoming CALL query = 0; MEETING query = 8 tracked-rep items.
- Tracked reps: Tim Lieto (161889085), Ken Cunningham (162339176), Tim Ziemer (159350430)

## Per-rep activity
| Rep | Set | Held | Up7d |
|---|---|---|---|
| Tim Lieto | 1 | 0 | 3 |
| Ken Cunningham | 1 | 0 | 2 |
| Tim Ziemer | 0 | 2 | 3 |
| TOTAL | 2 | 2 | 8 |

## FRESH / DEAL classification log
| Engagement | Pool | Company | Open deal? | Class |
|---|---|---|---|---|
| 373669254885 Digital Realty intro | Held | Digital Realty | none | FRESH |
| 373416124109 LatWan intro | Held | LatWan | none | FRESH |
| 373696105146 BroadStar huddle | Set | BroadStar | none | FRESH |
| 373499554501 Myakka pricing | Set | Myakka Communications | none found | FRESH |

## Trend baseline (LIVE - 5 prior weekday runs)
Prior runs used: 2026-05-26, 05-27, 05-28, 06-01, 06-02.
Averages: held_fresh 1.8, held_deal 1.2, set_fresh 2.8, set_deal 0.2.
Today: held_fresh 2, held_deal 0, set_fresh 2, set_deal 0.
Tags: held_fresh FLAT, held_deal DOWN, set_fresh FLAT, set_deal FLAT.

## Calendar movement (vs 2026-06-02 snapshot)
- PUSHED: none. PULLED IN: none. DROPPED: none.
- NEW: Myakka pricing proposal (Ken, 6/5); BroadStar huddle (Tim Lieto, 6/4, Tier 5).
- Transitioned to held: Digital Realty (372944438972 -> call 373669254885), LatWan (372352846528 -> call 373416124109).
- Note: yesterday's 6/3-dated items (Digital Realty, LatWan, ACG, ONUG) all reached meeting time today; none dropped. ONUG (16:00 ET) occurred just after the 15:59 cutoff -> lands in tomorrow's held window.

## MEDDPICC writes (silent side effect - founder-invisible)
### Tier 1 fills (2)
| Contact | Company | Fields | Evidence |
|---|---|---|---|
| Thiago Caro (467642756839), CEO | LatWan | meddpicc_pain_contact, meddpicc_use_case | LatWan intro call 373416124109 (transcript+summary). CEO explicitly wants to extend DIA customers into multiple DCs without IP complexity, keeping brand+margin in-house vs a third-party interconnection fabric. Both fields empty pre-write (num_notes 6 / num_contacted 4). Property names verified via search_properties before write. |

### Skips / holds
- Digital Realty: founder-led intro (Tim Z + Abilash with Travis Ewert + team). Travis Ewert NOT among the 217 associated CRM contacts (mostly facilities/network-eng). No clean attributable contact -> SKIP. ACTION FOR COOPER: create/identify Travis Ewert as a CRM contact so the relationship and MEDDPICC are captured.

## Data quality / routine health flags (Cooper)
1. WINDOW GAP: CALL 373322854124 "Discovery Call - Voice Exchange & Path Border Controller" (Tim Z, 10 min) timestamped 6/2 09:30 ET, createdate 6/2 21:17 ET. Logged after yesterday's run fired and before today's held window started -> never surfaced in a brief. Substantive discovery call. Recommend manual review or a one-off backfill window.
2. Duplicate engagement logging on both held calls: Digital Realty has CALL 373669254885 + MEETING 372944438972 + owner-less CALL 373696168663; LatWan has CALL 373416124109 + MEETING 372352846528 + owner-less MEETING 373514089155. Deduped by hs_object_id + owner; no double counting. Owner-less duplicates are a recurring HubSpot logging artifact.
3. ACG Research meeting (373757620963, Tim Z) has no transcript/summary and no deal substance - excluded from the brief as a contentless analyst/AR touch.
4. BroadStar "Huddle" (373696105146) counted as a Set booking for Tim Lieto; title reads possibly-internal but owned by a tracked rep and external company referenced - included with this note in case it is an internal prep huddle.

## Per-recipient FOR YOU routing log
- Abilash (CEO): Digital Realty Tier 1 logo intro held (he was on the call) + CEO follow-up ask; 1623 Farnam Tier 1 demo 6/4. Rationale: Tier 1 logo + strategic, CEO-actionable.
- Tim Z (CRO): both held calls his, technical deep-dives next; deal-call DOWN signal (0 vs 1.2); heavy 6/4 slate. Rationale: runs the team + owns the follow-ups.
- Cooper (RevOps): routine health, MEDDPICC summary, Travis Ewert contact-creation flag, window-gap flag, Set methodology note. Rationale: data quality + routine health.

## DM delivery
| Recipient | Channel | ts | Status |
|---|---|---|---|
| Abilash (U06RVK9NTQR) | D0A2YNPVB96 | 1780520916.197009 | delivered |
| Tim Z (U08CMD5PMQE) | D0A2817RE68 | 1780520930.635789 | delivered |
| Cooper (U0A24D9RJLS) | D0A2YNL1TA4 | 1780520947.686039 | delivered |

All 3 delivered first attempt. Run status: GREEN.
