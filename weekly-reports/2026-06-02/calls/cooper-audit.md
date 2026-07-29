# Cooper Audit - Daily Sales Activity Brief - 2026-06-02 (Tue)

Run time: 2026-06-02 17:01 ET (late fire; nominal 4pm CT = 5pm ET). All 3 exec DMs delivered cleanly.

## Run health
- HubSpot MCP: connected. Slack MCP: connected.
- Held window: 2026-06-01 16:00 -> 2026-06-02 15:59 ET (24h Tue-Fri standard).
- Set window: same. Measured by MEETING create-date (true booking signal). NOTE: the auto-generated HUBSPOT_MEETINGS CALL logs have createdate == meeting time, so using CALL.createdate would conflate Set with Held; deliberately used MEETING.createdate. Result: 0 meetings booked in window.
- Upcoming window: next 7 days, queried on MEETING object (the CALL upcoming query returned 0 - future engagements log as MEETING).
- query_crm_data threw one transient internal error; fell back to association searches (clean).

## Activity (tracked reps only)
| Rep | Set | Held | Up7d |
|---|---|---|---|
| Tim Lieto | 0 | 0 | 2 |
| Ken Cunningham | 0 | 2 | 1 |
| Tim Ziemer | 0 | 3 | 7 |
| TOTAL | 0 | 5 | 10 |

## FRESH / DEAL classification (held + set)
Classified on the associated COMPANY's open-deal state (deals are not associated directly to engagements in this tenant - all direct-to-call deal searches returned 0).
| Engagement | Owner | Class | Basis |
|---|---|---|---|
| Astound | Tim Z | FRESH | no open deal on Astound |
| Technium/Pearce | Tim Z | DEAL | Technium "Technium - Lab" $5k presentationscheduled (open, close 05/29 PAST) |
| SIPNAV | Tim Z | FRESH | no company record |
| Broadstar/RocNet | Ken | DEAL | RocNet "RocNet - Lab Unit" $10,153 lab/POC (open, close 05/15 PAST) |
| Myakka | Ken | FRESH | no open deal on Myakka |

Held mix: 3 FRESH / 2 DEAL. Set mix: 0 / 0.

## Trend baseline (LIVE - 4 prior weekday runs: 05/26, 05/27, 05/28, 06/01; 05/29 Fri did not fire)
| Metric | Today | 5d avg | Tag |
|---|---|---|---|
| held_fresh | 3 | 1.5 | UP |
| held_deal | 2 | 1.0 | UP |
| set_fresh | 0 | 3.5 | DOWN |
| set_deal | 0 | 0.25 | FLAT |

## Calendar movement vs 2026-06-01 snapshot
- PUSHED: none. PULLED IN: none. DROPPED: none.
- NEW: Mplify Board of Directors - Strategy Meeting (369613257448, Tim Z, 06/09 09:00 ET) - rolled into the 7-day window as the horizon advanced; industry-body governance, low priority.
- Transitioned to held: yesterday's full 06/02 slate (Astound 6/1, Technium/Pearce x2 slots, SIPNAV, Broadstar/RocNet, Myakka) all converted to held calls/demo today.

## MEDDPICC writes (silent - founders do not see these)
FILLED (Tier 1):
| Contact | Field | Value summary |
|---|---|---|
| Ken Rice (SIPNAV CTO, 491948684990) | meddpicc_pain_contact | Intermediate SIP carrier ~1B calls/day, very low per-call margins -> needs efficient traffic management + resilient backup/peering |
| Ken Rice (SIPNAV CTO, 491948684990) | meddpicc_use_case | Backup connections + traffic management across carrier routes + peering to optimize voice traffic between providers (early discovery) |

REFRESHED: none. DRIFT (Tier 2): none. HOLDS (Tier 3): none.

SKIPPED (7 contacts):
- Astound: Kevin Fonkert, William Yates - already comprehensively populated from this call (smart-fill), matches, skip.
- Technium/Pearce: Kristyn Shaughnessy, Michael Joseph (CTO, 140 notes), Jeremy Gallagher (142), William Bushman (214), James Salvato - richly populated; today's 6-min SOW-housekeeping call read NOT_DISCUSSED across MEDDPICC fields. Preserve older snapshots.
- Broadstar/RocNet: David Clar (RocNet, 40 notes) - richly populated; today's call substance is Broadstar's needs (Anthony Salamoni, not a CRM contact), not David/RocNet. Writing here = mis-attribution. Skip.

## Data-quality flags for Cooper
1. SIPNAV has NO company record - only contact Ken Rice (CTO) exists. Recommend creating the SIPNAV company and associating Ken Rice. ICP fit unresolved (intermediate SIP/VoIP carrier - likely Network Operator or Other).
2. Broadstar (the actual buyer on the RocNet call) has no company record; Anthony Salamoni (Broadstar) has no contact record. Recommend creating both - the live POC (West Palm Beach) is currently tracked only under RocNet's partner record.
3. Myakka/Dragonfly demo (Ken, 10:00 ET) held with no summary/outcome logged. Counted as held but unscoreable - nudge Ken to log notes.
4. Both lab deals are past close date: Technium-Lab (close 05/29) and RocNet-Lab Unit (close 05/15). Stage/close-date hygiene needed.

## Per-recipient FOR YOU routing decision log
- Abilash (CEO): 2 items - Tier 1 logos this week (Digital Realty / Bell / 1623 Farnam); Astound intro landed well.
- Tim Z (CRO): 4 items - Technium SOW slip + overdue close (STALLING); RocNet/Broadstar overdue close vs live POC; 0 sets vs 5 held (refill gap); Tier 1 slate 6/3-6/4.
- Cooper (RevOps): 4 items - data gaps (SIPNAV/Broadstar/Anthony), Myakka no-summary, 2 MEDDPICC fills on Ken Rice, trend status.

## DM delivery
| Recipient | Channel | ts | Status |
|---|---|---|---|
| Abilash (U06RVK9NTQR) | D0A2YNPVB96 | 1780434705.510509 | delivered |
| Tim Ziemer (U08CMD5PMQE) | D0A2817RE68 | 1780434730.767079 | delivered |
| Cooper (U0A24D9RJLS) | D0A2YNL1TA4 | 1780434755.833439 | delivered |

## Dropped (non-tracked)
- MEETING 373010767566 "Austausch" - owner 164949459 (unmapped). Filtered to audit only.
