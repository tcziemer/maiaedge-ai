# Signal Scan — Aggregator (Cowork scheduled task)

You are running the **Aggregator** stage of MaiaEdge's weekly signal scan. The 6 per-ICP scans (`signal-scan-colo`, `signal-scan-fiber`, `signal-scan-neocloud`, `signal-scan-networkop`, `signal-scan-msp`, `signal-scan-enterprise`) fired between 8:30am and 1:00pm CT, each writing the 5 signal fields + tier + heat to HubSpot for accounts in their segment.

Your job: read all of today's HubSpot signal writes, build the 3 territory-consolidated rep DMs (Tim Lieto East + Ken West + Tim Z International routed to Cooper), append the weekly Run log row to canvas `F0B0AFSB9LN`, and write Cooper's cross-ICP run report. **You do NOT write to HubSpot, do NOT scrape any web sources, do NOT consume Apollo.** Read-only on HubSpot; read-only on Slack until DM dispatch.

## Phase 3 mode (locked rules — same as the per-segment scans)

- **Score floor: 8.** Surface score ≥8 in rep DMs.
- **Cascade tiers:** Highest 27+ (red), Strong 18-26 (orange), Worth Reviewing 12-17 (yellow), LIGHT 8-11 (green).
- **Hard cap: 50 accounts per rep DM.** Target range 25-50/rep.
- **Heat enum is Title Case** (`Hot` / `Warm` / `Cool` / `Cold`).
- **Rep DMs are built from the CURRENT heat pool, not just today's writes (2026-06-04).** With the 180-day detection window the signal pool is continuously rich; surface every account whose `signal_heat` is Hot/Warm/Cool in the rep's territory, ranked Hot -> Warm -> Cool then by `last_signal_score` desc, capped at 50. "Written today" is now only a NEW annotation within that pool, not the DM population.
- **Carryover News fill-down is RETIRED (2026-06-04).** It was a workaround for the thin 14-day-window pool. The Hot/Warm/Cool pool over the 180-day window now fills the rep lists directly. If a territory's pool is still under 25, that is the true count - do not pad it.

## Apollo budget

**0 credits.** No Apollo MCP calls. Read-only HubSpot + Slack + filesystem.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Slack. Abort + DM Cooper (`U0A24D9RJLS`) if HubSpot is unavailable. Slack DM failures degrade gracefully (rep DMs land in audit instead).

2. **Check the 6 per-segment audit files** under `weekly-reports/[today CT YYYY-MM-DD]/signal-scan/`:
   - `colo/segment-run-report.md`
   - `fiber/segment-run-report.md`
   - `neocloud/segment-run-report.md`
   - `networkop/segment-run-report.md`
   - `msp/segment-run-report.md`
   - `enterprise/segment-run-report.md`

   **Behavior is informational, NOT gating the rep-DM build:**
   - If all 6 exist: proceed normally.
   - If 1–2 are missing: log warning, note the gap in Cooper's run report (Stage 6). Rep DMs still ship.
   - **If 3+ are missing: ABORT the run, DM Cooper.** That's likely a Cowork platform issue and rep DMs would be substantially incomplete.

3. **Read the prior Monday's aggregator artifacts** at `weekly-reports/[YYYY-MM-DD minus 7 days]/`:
   - 3 rep xlsx files (Tim Lieto, Ken, Tim Z — naming `weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx` or equivalent)
   - Cooper run report at `signal-scan/cooper-run-report.md`

   If absent (first run after rollout, or prior-week files not generated): tag everything in this run as `NEW`. Log the absence in Cooper's run report.

4. **Read canvas `F0B0AFSB9LN`** via `slack_read_canvas` to identify any rows you'd accidentally double-write (in case this task already ran and partially completed).

---

## Stage 1 — Build the rep-facing heat pool + identify today's writes

**Two populations (2026-06-04 reframe).** Rep DMs are built from the CURRENT heat pool; "today's writes" is used only to NEW-tag rows and to populate Cooper's run report.

### 1a. Current heat pool (the rep-DM population)

```
HubSpot search:
  customer_segment IN (
    "Data Center Colo Provider",
    "Fiber Operator",
    "NeoCloud",
    "Network Operator(Tier 1 / VNO)",   -- NO space before paren
    "MSP/Aggregator",
    "Enterprise-CustomerSegment"
  )
  AND signal_heat IN ("Hot", "Warm", "Cool")   -- the workable pool; Cold/null excluded
  AND hubspot_owner_id IS NOT NULL
  AND type != "Customer"
  AND id != 124293230301               -- MaiaEdge own record
```
Rank Hot -> Warm -> Cool, then by `last_signal_score` desc. Split by territory (owner), cap 50/rep.

### 1b. Written/updated today (NEW tagging + Cooper report only)

Do NOT use `last_signal_date = today` — `last_signal_date` is the EVENT date (semantics narrowed 2026-05-28), so that query returns ~0 every Monday (this was the 2026-06-01 aggregator bug). Identify today's writes from BOTH:
- the 6 per-segment audit files read at Stage 0 (each lists its Stage 5c "Writes summary" with company id + name + score) - authoritative; and
- a HubSpot supplement: `hs_lastmodifieddate >= today 00:00 CT` intersected with the segment filter above (catches any write an audit file missed).

Mark these records `NEW` within the heat pool; everything else is `CARRIED`.

Properties to fetch per record:
- `name`, `domain`, `customer_segment`, `company_sub_segment`, `account_tier`, `hubspot_owner_id`, `state`, `country`
- `recent_news_or_trigger_event` (the narrative), `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`
- `account_brief` (for the rep xlsx Account Brief column)
- `infrastructure_profile`, `provisioning_landscape` (for context in rep DMs when needed)
- `linkedin_company_page` (fallback to Apollo `linkedin_url` from prior enrichment; leave blank if both missing)
- `hs_is_target_account` (for the rep DM "strategic-pin" annotation — heat may be lower than tier because tier is pinned)

This is the authoritative population for today's rep DMs. Any record that made it to HubSpot during the 8:30am–~1:15pm window gets included regardless of per-segment audit-file presence.

---

## Stage 2 — NEW / CARRIED / LIGHT / CARRYOVER tagging

For each record in the Stage 1 population, assign one of these tags:

- **NEW** — record was NOT in any of last Monday's 3 rep xlsx files. First time surfacing.
- **CARRIED** — record WAS in last Monday's rep xlsx for the matching rep. Surfaces again this week with a fresh / updated signal.
- **LIGHT** — record's `last_signal_score` is 8-11 (LIGHT cascade tier). Tagging is independent of NEW vs CARRIED.
- **CARRYOVER** — special — used only at Stage 3 fill-down when natural Primary + LIGHT pool < 25/rep. Carryover candidates are accounts NOT in this run's Stage 1 population but with prior-week `recent_news_or_trigger_event` ≤30 days old AND no rep activity ≤14 days. Pulled in to fill the rep DM to the 25 floor.

If prior-week xlsx absent: tag everything `NEW (no prior file)`.

---

## Stage 3 — Territory split + 40-cap per rep + fill-down

Bucket the Stage 1 population by `hubspot_owner_id`:

| Owner ID | Rep | Territory | Slack DM target |
|---|---|---|---|
| `161889085` | Tim Lieto | East (30 states) | `U0A973L1HFF` (LIVE direct per Phase 0 partial lift 2026-05-04) |
| `162339176` | Ken Cunningham | West (20 states + DC) | `U0AE1PGCB6C` (LIVE direct) |
| `159350430` | Timothy Ziemer | International | `U0A24D9RJLS` (still routed to Cooper, validating) |

Other owners → surface in Cooper's run report under "Unrouted accounts (non-rep-owned)". Don't include in rep DMs.

### Per-rep ranking + capping (apply per bucket)

1. **Rank by `last_signal_score` descending.**
2. **Cap at 50 accounts.** Hard cap; overflow goes to silent nurture (mention in Cooper run report under "Below cap"; do NOT surface in rep DM).
3. **Three-tier fill-down to ensure 25-50 range:**
   - **Primary** (score ≥12): always include up to cap. If natural Primary ≥50, you're done — drop the rest.
   - **LIGHT** (score 8-11): include if Primary pool <25. Fill from LIGHT until you hit 25 OR exhaust LIGHT pool.
   - **Carryover News fill-down**: ONLY if Primary + LIGHT pool < 25 after both passes. Pull from prior-week's records (per-territory) where `recent_news_or_trigger_event` ≤30 days old AND no rep activity ≤14 days. Tag these `CARRYOVER`. Stop when total = 25 OR Carryover pool exhausted.

4. **Sort final list by score descending** for the cascade body.

---

## Stage 4 — Rep DM cascade dispatch

For each of the 3 rep buckets, build one Slack DM with this structure:

### DM Body Template

```
Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]

Heat distribution: [H] Hot N / [W] Warm N / [C] Cool N / [K] Cold N
Total: N accounts in this run (cap 50).

CASCADE BY SCORE

🔴 Highest Priority (score 27+)  -  N accounts
  - [Account Name] ([Segment] / [Sub-segment]) - [Signal type one-liner] - score [N] - heat [emoji + Title Case]
  - ... (top of cascade; expect 0-10 accounts at this tier)

🟠 Strong Signals (score 18-26)  -  N accounts
  - ...

🟡 Worth Reviewing (score 12-17)  -  N accounts
  - ...

🟢 LIGHT Signals (score 8-11)  -  N accounts
  - ...

🔵 Carryover News (filled to floor of 25; fired only when natural pool was thin)  -  N accounts
  - [Account Name] ([Segment]) - [stale signal narrative] - score [N] - [days since last rep activity]d quiet

THIS WEEK'S TOP 5 (regardless of segment, ranked by score):
1. [Account Name] - [signal one-liner] - score [N] - [Why this matters in one phrase]
2. ...

NEW ACCOUNTS THIS WEEK (signal-surfaced + auto-enriched):
- [Account Name] ([Segment]) - [signal that triggered + who their target persona is]
- ... (if any; many weeks will have zero)

Full table threaded below ⤵
```

### Threaded full-list markdown table (posted as a reply to the DM)

Columns: Rank | Account Name | Segment | Sub-Segment | Tier | Owner | Heat | Score | Signal Type | Signal Body (3-5 sentences) | Detection Date | Account Brief | State | LinkedIn | HubSpot URL | Suggested Angle | NEW/CARRIED/LIGHT/CARRYOVER tag.

### Excel attachment

Write `weekly-reports/[today CT YYYY-MM-DD]/weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx` per rep. One tab per segment (max 6 tabs: Colo / Fiber / NeoCloud / Network Op / MSP / Enterprise). Segments with zero hits get no tab.

Columns per tab match the threaded markdown table above. Include a **Legend tab** with the 4-band score color coding (red ≥27 / orange 18-26 / yellow 12-17 / green 8-11) and Heat enum reference.

### Slack dispatch

Send each rep DM via `slack_send_message` to the corresponding user ID above. Then post the threaded full-list table as a reply (via `slack_send_message` with thread_ts).

**Tim Z DM** still routes to Cooper (`U0A24D9RJLS`) per Phase 0 partial lift. Append a one-line annotation: `(Tim Z cascade - validate before forwarding to Tim Z.)`

**Tim Z xlsx writes to disk as if it were Tim Z's own** — naming `weekly-signal-scan-ziemer-[YYYY-MM-DD].xlsx`. Cooper attaches manually after validation.

---

## Stage 5 — Canvas Run log append

Append exactly ONE row to canvas `F0B0AFSB9LN` summarizing the entire 6-segment + aggregator run.

Row format (canvas table convention):

```
| YYYY-MM-DD | Weekly Signal Scan | <status emoji> | <one-sentence summary> | <artifact links> |
```

**Status emoji:**
- ✅ `:white_check_mark:` — all 6 segments wrote successfully, all 3 rep DMs dispatched, ≥ canvas-defined coverage floor
- ⚠️ `:warning:` — 1-2 per-segment scans missing audit / Slack DM degraded / coverage below floor
- 🔴 `:red_circle:` — 3+ per-segment audits missing OR HubSpot population query returned 0 records (likely platform issue)

**One-sentence summary template:**
```
6 segments wrote N total signal records (Colo:N / Fiber:N / NeoCloud:N / NetOp:N / MSP:N / Enterprise:N). N rep DMs dispatched. N heat promotions (N→Hot, N→Warm). N NEW accounts auto-enriched.
```

**Artifact links:**
- 3 rep xlsx paths (`weekly-reports/YYYY-MM-DD/weekly-signal-scan-lieto-YYYY-MM-DD.xlsx`, `-cunningham-`, `-ziemer-`)
- Cooper run report path (Stage 6)

Use `slack_update_canvas` to append. Do NOT replace prior rows. Do NOT invent new status emojis (use only the ones defined in the canvas header).

---

## Stage 6 — Cooper run report

Write a cross-ICP run report to:
```
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/cooper-run-report.md
```

Content:

1. **Run header** — date, total runtime (8:30am → aggregator end), total HubSpot writes across 6 segments, total heat promotions, total NEW accounts auto-enriched.

2. **Per-segment summary table** — one row per segment with:
   - Audit file present? (✓ / ✗)
   - Target list size
   - Matched accounts
   - NEW accounts created
   - Total writes
   - Score distribution (8-11 / 12-17 / 18-26 / 27+ counts)
   - Heat promotions (Cold→Warm, Cold→Hot, Warm→Hot, Cool→Warm, Cool→Hot counts)
   - Tier promotions / demotions (count of records where account_tier changed)
   - Apollo consumed (of sub-cap)
   - Source coverage % (count ✓ / total documented sources)

3. **Cross-ICP heat distribution rollup** — total Hot, Warm, Cool, Cold counts across all 6 segments today, plus delta vs. prior Monday.

4. **Rep DM dispatch table** — one row per rep with: rep name, owner ID, Slack target, account count surfaced, NEW count, CARRIED count, LIGHT count, CARRYOVER count, top-account name + score.

5. **Source Coverage delta vs. prior Monday** — sources that flipped ✓→✗ or ✗→✓ this week. Surface 3-week ✗ streaks under "Sources Needing Development" with the date the streak started.

6. **Anomalies** — gaps where the aggregator detected something worth Cooper's attention:
   - Per-segment audit files missing
   - Rep DM dispatch failures (Slack errors)
   - Unrouted accounts (signal hits without owner mapping)
   - HubSpot population query returning unexpected zeros for a segment
   - Score arithmetic mismatches between per-segment audits and HubSpot writes (audit said 47, HubSpot returned 45)

7. **R3 dup flags** — accounts surfaced with a likely-duplicate sibling in the population (same domain root, same `name` modulo legal suffix). Surfaces for Routine 3 to handle next 2am ET run.

8. **Apollo budget post-run** — total weekly consumption to date, remaining capacity, projection for the rest of the week.

9. **Tier 3 holds carryover** — sum of per-segment Tier 3 holds re-appended to canvas this run. Confirm the canvas write succeeded (since each per-segment scan appends to canvas individually, this is a count check, not a re-write).

10. **What needs Cooper's attention** — top 3 items, written tactically.

---

## Failure handling

- **HubSpot MCP errors at Stage 1:** retry (250ms → 1s → 4s, max 3). If all retries fail, abort + DM Cooper with the error trace. Rep DMs cannot be built without the Stage 1 population.
- **Per-segment audit file read errors:** log as "missing audit" in Cooper run report, proceed normally.
- **Prior-week file read errors:** tag everything `NEW (prior file unreadable)`, log warning.
- **Slack DM dispatch errors:** retry once per recipient with 2-second pause. On second failure, write the rep DM body + table to `weekly-reports/[today]/rep-dm-failed-[rep-last-name].md` and continue. Surface in Cooper run report under "Slack dispatch failures".
- **Canvas write errors:** retry once. On second failure, write the row to `weekly-reports/[today]/canvas-row-pending.txt` and surface in Cooper run report. The next run picks it up.
- **xlsx generation errors:** fall back to markdown table on disk for the failed rep; surface in Cooper run report.

## End-of-run footer

Log a single one-line summary to Cowork chat:
```
[Aggregator] segments=6 audits_present=N rep_dms=N writes_aggregated=N heat_promotions=N anomalies=N runtime=Nmin canvas=YYYY-MM-DD cooper_report=weekly-reports/YYYY-MM-DD/signal-scan/cooper-run-report.md
```

This is the visible signal that the full Monday cycle completed. Cooper looks for this in the Cowork chat at ~2:45pm CT each Monday.
