# Cooper Audit — Daily Sales Activity Brief — Tue 2026-05-26

## Run summary

| Metric | Value |
|---|---|
| Run timestamp | 2026-05-26 ~16:03 CT (21:03 UTC) |
| Routine | Daily Sales Activity Brief (Cowork scheduled task `weekly-call-recap`) |
| Held window | 2026-05-25 16:00 ET → 2026-05-26 15:59 ET (24h) |
| Set window | same as held |
| Upcoming window | 2026-05-26 17:00 ET → 2026-06-02 17:00 ET (next 7d) |
| Held engagements (raw) | 3 (1 CALL, 2 MEETING_EVENT) |
| Set engagements (raw) | 2 (1 CALL, 1 MEETING_EVENT) |
| Upcoming engagements (raw) | 9 (0 CALL, 9 MEETING_EVENT) |
| Held tracked-rep | 2 |
| Set tracked-rep | 1 |
| Upcoming tracked-rep | 8 |
| MEDDPICC Tier 1 writes | 1 |
| MEDDPICC Tier 2 DRIFT flags | 0 |
| MEDDPICC Tier 3 holds | 1 |
| DMs delivered | 3 (Abilash ✅ + Tim Z ✅ + Cooper ✅) |
| Errors | 0 fatal · 1 minor (Abilash DM used `&gt;` HTML entity instead of `>` for blockquote prefix — content readable but blockquote indentation not honored; Tim Z + Cooper DMs use literal `>` correctly) |

## MEDDPICC writes

### Tier 1 fills (written to HubSpot)

| Contact ID | Name | Field | Source call | Value summary |
|---|---|---|---|---|
| 239294028513 | Cliff Miyake (Ocean Networks, COO) | `meddpicc_competition_contact` | 371748063961 (Cliff Miyake call, Tim Z, 2026-05-26) | Tier Fortress CEO Fred raised cheaper switches/routers as conventional equivalents; differentiation gap on provisioning-speed + reduced-configuration narrative needs targeted competitive comparison material |

### Tier 2 DRIFT (no overwrite)
None.

### Tier 3 holds (audit only)

| Contact ID | Name | Field | Reason | Action needed |
|---|---|---|---|---|
| 239294028513 | Cliff Miyake | (would-be `meddpicc_champion_contact`) | No `meddpicc_champion_contact` field exists in this HubSpot tenant — only `meddpicc_competition_contact`, `meddpicc_pain_contact`, `meddpicc_criteria_contact`, `meddpicc_metrics_contact`, `meddpicc_use_case`, `meddpicc_infrastructure_contact`, `key_stakeholders___meddpicc`, `buying_process___meddpicc` are available. Cliff displayed champion-grade brokering behavior on the 5/26 call (introducing MaiaEdge into 1547 Critical Systems Realty + Lumen federal beyond his own Ocean Networks deal). | Cooper: decide whether to (a) add a `meddpicc_champion_contact` field to HubSpot, (b) use `key_stakeholders___meddpicc` as the closest substitute, or (c) accept that champion behavior is captured at deal-level only and skip contact-level writes. |

## Filtered engagements (not in brief)

| Engagement ID | Type | Title | Owner | Reason filtered |
|---|---|---|---|---|
| 371729337031 | MEETING | Meeting with Darryl from Attobahn INC | 159875488 (UNMAPPED) | Owner not in tracked-rep list (Tim L / Ken / Tim Z). **Same unmapped owner ID surfaced on 2026-05-20 with 3 ITW meetings (Pearce, Ecotel, TW1) per that run's audit. Recurring data-hygiene flag.** Note: associated contact Darryl Grey is owned by Tim Lieto — meeting-owner-vs-contact-owner mismatch suggests calendar-bot or former-user artifact. |
| 371773858497 | MEETING | MaiaEdge Onboarding & Billing Flow (upcoming Fri 5/29) | 159701452 (Kyle Blackwell) | Kyle is SE not a tracked rep |

## Per-engagement FRESH/DEAL classification log

| ID | Type | Title | Owner | Class | Reason |
|---|---|---|---|---|---|
| 371748063961 | CALL | Call with Cliff Miyake | Tim Z | DEAL | Ocean Networks 1st Order $50k presentationscheduled open |
| 371085092597 | MEETING | EPS Global - MaiaEdge Video | Tim L | FRESH | No associated open deals |
| 371729337031 | MEETING | Attobahn meeting | unmapped | (filtered) | n/a |
| 371156031178 | MEETING | Dinner EPS Global/MaiaEdge/Aria Networks (upcoming) | Tim L | FRESH | No deal |
| 369770144486 | MEETING | Commercial Discussion - MaiaEdge (upcoming) | Tim Z | FRESH | No deal in associated set (company ambiguous — HDCO or Acuutech) |
| 371640554182 | MEETING | Technium/MaiaEdge - POC Discussion (upcoming) | Tim L | DEAL | Technium - Lab $5k presentationscheduled open |
| 369403183813 | MEETING | Verizon/MaiaEdge/Mplify Meeting (upcoming) | Tim Z | FRESH | No associated open deal |
| 369406782164 | MEETING | MaiaEdge Intro to Imperium Data (upcoming) | Tim L | FRESH | No deal |
| 369260239585 | MEETING | Maia / Movi - SW & CPE Cont'd (upcoming) | Tim L | DEAL | Movi - CPE expansion $600k qualifiedtobuy + Movi - 22 x 100G $400k open (both via associated-deal hydration, but Movi company record not located via name search — data-hygiene flag) |
| 369684404951 | MEETING | GDT / MaiaEdge intros (upcoming) | Ken | FRESH | GDT Partner Target Tier 5, no deal |
| 370631086828 | MEETING | Myakka/Dragonfly <> MaiaEdge (upcoming) | Ken | FRESH | Myakka Tier 3 Fiber Operator, no deal |

## FOR YOU routing decisions

| Item | Routed to | Why |
|---|---|---|
| 1547 + Lumen federal strategic vector | Abilash | CEO-level narrative pull-through if either lands |
| Verizon/Mplify Thu meeting | Abilash | Tier 1 logo touchpoint |
| Movi $1M open pipeline (Thu meeting) | Abilash + Tim Z | Big logo open pipeline; Abilash gets it as expansion narrative, Tim Z gets it as a flag-to-attend |
| Legacy-switch differentiation one-pager ask | Tim Z | CRO assigns enablement ownership; Cliff needs it before 6/01 Hawaii meeting |
| 1547 not in HubSpot | Tim Z | RevOps-adjacent but Tim Z is the lead-sales relationship owner via Cliff |
| Routine health (missing 5/21+5/22+5/25 runs) | Cooper | RevOps owns routine ops |
| Movi data-hygiene flag | Cooper | RevOps owns CRM cleanup |
| Attobahn unmapped owner | Cooper | RevOps owns owner remapping |
| 1547 sourcing seed for R7 | Cooper | RevOps owns sourcing queue |

## Items NOT routed to any recipient

- EPS Global Held meeting (thin content, no outcome logged) — not actionable beyond the dinner tonight which Tim Lieto already owns. No surface required.
- Tier Fortress CEO Fred reference — covered indirectly via Tim Z's legacy-switch one-pager ask.

## Routine health notes

1. **Prior weekday runs sparse on disk.** Only 5/20 (Wed) and 5/18 (Mon) have call-routine artifacts. 5/15 (Fri), 5/19 (Tue), 5/21 (Thu), 5/22 (Fri), 5/25 (Mon) all missing. 5/25 was Memorial Day so a skip is reasonable, but the 5/15 / 5/19 / 5/21 / 5/22 gaps are unexplained.

2. **No yesterday upcoming-snapshot.** Calendar-movement detection requires yesterday's snapshot. Memorial Day skip is fine but combined with the prior gaps, we have BASELINE BUILDING for both trend AND calendar-movement.

3. **Slack mrkdwn rendering bug on Abilash DM.** First-send used `&gt;` HTML entity instead of `>` for blockquote prefix on the per-call snapshot lines (4 lines × 2 calls = 8 lines affected). Slack renders `&gt;` as literal text rather than blockquote indent. Content is still legible but visual format degraded. Tim Z + Cooper DMs sent immediately after used literal `>` correctly. Not severe enough to re-send + double-ping Abilash; flagging for routine prompt to clarify "use literal `>` not HTML entity".

## HubSpot data-quality flags (for R3 / R6 / Cooper)

1. **Movi company record missing.** Two open deals ($600k Movi - CPE expansion + $400k Movi - 22 x 100G expansion) and an upcoming Thu meeting tagged "Maia / Movi - SW & CPE Cont'd" — but `search_crm_objects` on COMPANY with `name CONTAINS_TOKEN "Movi"` returned 0 results. Either (a) company is archived, (b) stored under a different legal name with no "Movi" substring, or (c) deal-to-company association is broken. R6 territory/hygiene or R3 duplicate-account audit candidate.

2. **Owner 159875488 recurring on unmapped meetings.** Today's Attobahn meeting + 5/20's three ITW meetings. Likely a former HubSpot user OR a calendar-integration service account. Recommend either (a) deactivate so meetings flow to actual rep owners, (b) map the ID to a real rep, or (c) document as "external calendar bot — meetings need manual owner reassignment after import."

3. **1547 Critical Systems Realty not in CRM.** Cliff Miyake's call substance was largely about 1547 — they're a real colo developer (Critical Systems Realty / now part of CSR / aka 1547 cube companies). Worth queueing for R7 monthly sourcing or a manual seed before Cliff's 6/1 Hawaii meeting.

4. **Tier Fortress not in CRM (likely intentional).** Tier Fortress is referenced via Cliff as a competitive frame, not a target account. Verify.

5. **Cliff Miyake contact carries 1 num_associated_deals** (Ocean Networks 1st Order $50k). Healthy.

6. **EPS Global meeting (371085092597) has null hs_meeting_outcome** despite the meeting having started + ended within the held window. Tim Lieto may log the outcome after the day; tomorrow's run could re-pick-it-up via the Set query if hs_lastmodifieddate moves but no second-run dedup is built in — log only.
