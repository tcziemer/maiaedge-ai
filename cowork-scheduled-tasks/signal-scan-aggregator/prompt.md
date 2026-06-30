# Signal Scan — Aggregator (Cowork scheduled task)

You are running the **Aggregator** stage of MaiaEdge's weekly signal scan. The 6 per-ICP scans (`signal-scan-colo`, `signal-scan-fiber`, `signal-scan-neocloud`, `signal-scan-networkop`, `signal-scan-msp`, `signal-scan-enterprise`) fired between 8:30am and 1:00pm CT, each writing the 5 signal fields + tier + heat to HubSpot for accounts in their segment.

Your job: read all of today's HubSpot signal writes, build the 5 territory-consolidated rep DMs (Tim Lieto Northeast + West, Ken Cunningham Southeast, Tory Teague Central, Markus Hendrich Europe, Tim Z International + Tier 1 Service Provider routed to Cooper), append the weekly Run log row to canvas `F0B0AFSB9LN`, and write Cooper's cross-ICP run report. **You do NOT write to HubSpot, do NOT scrape any web sources, do NOT consume Apollo.** Read-only on HubSpot; read-only on Slack until DM dispatch.

## Phase 3 mode (locked rules — same as the per-segment scans)

- **Score floor: 8** for fresh signal writes (the per-segment scans). The aggregator surfaces the full Hot/Warm/Cool heat pool; open-deal Hot accounts with score <8 are still included (they sort to the bottom of the score-ranked list).
- **Score bands** (for the xlsx legend + score reference, NOT the DM layout): Highest 27+ (red), Strong 18-26 (orange), Worth Reviewing 12-17 (yellow), LIGHT 8-11 (green). The rep DM body is a single flat numbered list ranked by score (Stage 4), not a per-band cascade.
- **Hard cap: 50 accounts per rep DM.** Target range 25-50/rep.
- **Heat enum is Title Case** (`Hot` / `Warm` / `Cool` / `Cold`).
- **Rep DMs are built from the CURRENT heat pool, not just today's writes (2026-06-04).** With the 180-day detection window the signal pool is continuously rich; surface every account whose `signal_heat` is Hot/Warm/Cool in the rep's territory, **selected** Hot -> Warm -> Cool then by `last_signal_score` desc, capped at 50, then **displayed** as a flat numbered list ranked by `last_signal_score` desc (Stage 4). The DM population is the heat pool, not "today's writes". The ⭐ marker = accounts NEW vs last week (the Stage 2 `NEW` tag), NOT "written today".
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
   - 5 rep xlsx files (Tim Lieto, Ken, Tory, Markus, Tim Z — naming `weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx` or equivalent)
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
- `name`, `domain`, `customer_segment`, `company_sub_segment`, `account_tier`, `hubspot_owner_id`, `territory_region`, `state`, `country`
- `recent_news_or_trigger_event` (the narrative), `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`
- `account_brief` (for the rep xlsx Account Brief column)
- `infrastructure_profile`, `provisioning_landscape` (for context in rep DMs when needed)
- `linkedin_company_page` (fallback to Apollo `linkedin_url` from prior enrichment; leave blank if both missing)
- `hs_is_target_account` (for the rep DM "strategic-pin" annotation — heat may be lower than tier because tier is pinned)

This is the authoritative population for today's rep DMs. Any record that made it to HubSpot during the 8:30am–~1:15pm window gets included regardless of per-segment audit-file presence.

---

## Stage 2 — NEW / CARRIED / LIGHT tagging

For each record in the Stage 1 population, assign:

- **NEW** — record was NOT in any of last Monday's 5 rep xlsx files. First time surfacing this week. **This is what the ⭐ marks in the rep DM** — the week-over-week "new signal" marker.
- **CARRIED** — record WAS in last Monday's rep xlsx for the matching rep. No star.
- **LIGHT** — `last_signal_score` is 8-11. An xlsx-only sub-tag (independent of NEW vs CARRIED); the DM does not separately label LIGHT since the score is shown inline.

If prior-week xlsx absent: tag everything `NEW (no prior file)` (every line gets a ⭐).

(CARRYOVER is retired — see Stage 3.)

---

## Stage 3 — Territory split + 50-cap per rep

Bucket the Stage 1 population by **`territory_region`** (the live HubSpot company property, populated on all active companies by the 5-region territory migration that went live 2026-06-17). Each region routes to its owner's DM. This replaces the old bucket-by-`hubspot_owner_id` / re-derive-from-state logic — `territory_region` is now the canonical routing key. (Owners are assigned go-forward to match region by the "Territory Assignment (Go-Forward)" keeper workflow, so owner and region agree; key off region.)

| `territory_region` | Region owner | Owner ID | Slack DM target |
|---|---|---|---|
| `Northeast` | Tim Lieto | `161889085` | `U0A973L1HFF` (direct) |
| `West` | Tim Lieto (interim) | `161889085` | `U0A973L1HFF` (direct) |
| `Southeast` | Ken Cunningham | `162339176` | `U0AE1PGCB6C` (direct) |
| `Central` | Tory Teague | `165480917` | `U0B7MU3P3QD` (direct) |
| `Europe` | Markus Hendrich | `164949459` | `U0B6B4U8QKD` (direct) |
| `International` | Timothy Ziemer | `159350430` | `U0A24D9RJLS` (still routed to Cooper, validating) |
| `Tier 1 Service Provider` | Timothy Ziemer (interim) | `159350430` | `U0A24D9RJLS` (Cooper) |
| `Unassigned` | Cooper Kennedy | `160267902` | `U0A24D9RJLS` (Cooper) |

This yields **5 rep DMs**: Tim Lieto (Northeast + West accounts consolidated into one DM), Ken Cunningham (Southeast), Tory Teague (Central), Markus Hendrich (Europe), and the Ziemer/Cooper DM (International + Tier 1 Service Provider + Unassigned). Tim Lieto's two regions collapse into his single DM; the Ziemer/Cooper DM still routes to Cooper under Phase 0 validation.

Records with a blank or unrecognized `territory_region` → surface in Cooper's run report under "Unrouted accounts (no territory_region)". Don't include in rep DMs.

### Per-rep selection + capping (apply per bucket)

1. **Select the 50 by heat first:** rank `Hot` → `Warm` → `Cool`, then by `last_signal_score` desc within each heat band, then `last_signal_date` desc. This guarantees the rep's highest-intent accounts (incl. open-deal Hot accounts that may carry a low/zero score) are always included.
2. **Cap at 50.** Hard cap; overflow goes to silent nurture (note in Cooper run report under "Below cap"; do NOT surface in the rep DM).
3. **No 25-floor padding.** If a territory's pool is under 25, that is the true count — do not pad. (The old Primary / LIGHT / Carryover fill-down is RETIRED; the 180-day heat pool fills the lists directly.)
4. **Then DISPLAY the capped set as a flat numbered list ranked by `last_signal_score` descending** (Stage 4). Selection is heat-first (keeps open-deal Hot accounts); display is score-first (highest-scoring news at the top), so score-0/null Hot accounts sit at the bottom of the displayed list.

---

## Stage 4 — Rep DM dispatch (flat numbered list)

**Format (updated 2026-06-15 per Cooper).** The rep DM body is a SINGLE FLAT NUMBERED LIST ranked by `last_signal_score` descending — NOT a per-band cascade. The old band-grouped cascade, the "THIS WEEK'S TOP 5" block, the "NEW ACCOUNTS THIS WEEK" block, and the threaded full-list table are all **RETIRED**. The DM is just a short header + the list. The per-rep xlsx (Stage 4b) remains the full-detail artifact. Goal: one scannable list a rep can read top-to-bottom.

### DM body template

```
Weekly Signal Scan — [Rep First Name] — Week of [YYYY-MM-DD]
Heat: 🔥 Hot N / 🌤️ Warm N / ❄️ Cool N  ·  N accounts (cap 50)  ·  ⭐ = new since last week

1. [⭐ ][Account Name] · [score][heat emoji] · [recent news in one sentence]
2. [⭐ ][Account Name] · [score][heat emoji] · [recent news in one sentence]
3. ...
N. ...
```

**Line rules:**
- **Rank by `last_signal_score` descending.** Ties broken by `last_signal_date` (more recent first). Records with no score (open-deal / sustained-intent Hot accounts) sort to the bottom and show `—` for score.
- **⭐ prefix ONLY on accounts that are NEW vs last week** — i.e. NOT in last Monday's rep list (the Stage 2 `NEW` tag). No star on `CARRIED` accounts. This is the week-over-week "new signal" marker. (Do NOT base the star on "written today" — base it on week-over-week presence.)
- **Score** = the integer `last_signal_score`. **Heat emoji** = 🔥 Hot / 🌤️ Warm / ❄️ Cool.
- **Recent news = ONE sentence** distilled from `recent_news_or_trigger_event`. Strip any legacy `[CODE]` or `[YYYY-MM-DD]` prefix; clip to ~80 chars at a word boundary so each line stays to ~1 line. If a Hot account has no scoreable news this window, use its stored news if present, else `Open deal / sustained intent — no fresh news this window`.
- **Body line carries ONLY:** number, ⭐ (if new), account name, score, heat emoji, one-sentence news. NO segment / sub-segment / tier / state / owner / links in the body — those live in the xlsx. Keep it clean.

### Slack length handling (pagination)
A 50-line list exceeds Slack's ~5,000-char-per-message limit, so split the list across the fewest messages needed:
- First message = header + as many numbered lines as fit under ~4,500 chars.
- Remaining lines continue as threaded replies to that first message (`thread_ts`), each ≤4,500 chars, each headed `*… (cont.)*`. Split ONLY at line boundaries — never split a line. Continue the numbering (do not restart at 1).
- This is still "just the list" — no separate cascade, Top 5, or detail table.

### Slack dispatch
Send the DM (and any continuation replies) via `slack_send_message` to the rep's user ID:

| Region(s) | Rep | Slack target |
|---|---|---|
| Northeast + West | Tim Lieto | `U0A973L1HFF` (direct) |
| Southeast | Ken Cunningham | `U0AE1PGCB6C` (direct) |
| Central | Tory Teague | `U0B7MU3P3QD` (direct) |
| Europe | Markus Hendrich | `U0B6B4U8QKD` (direct) |
| International + Tier 1 Service Provider | Timothy Ziemer | `U0A24D9RJLS` (Cooper — Phase 0) |

**Tim Z still routes to Cooper.** Prepend `_(Tim Z list — validate before forwarding to Tim Z.)_` to the Ziemer/Cooper first message. Tory and Markus are LIVE direct (same as Lieto and Ken).

### Stage 4b — Excel attachment (retained; the full-detail artifact)

Write `weekly-reports/[today CT YYYY-MM-DD]/weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx` per rep. One tab per segment (max 6 tabs: Colo / Fiber / NeoCloud / Network Op / MSP / Enterprise). Segments with zero hits get no tab. Columns per tab: Rank | Account Name | Segment | Sub-Segment | Tier | Heat | Score | Signal Type | Signal Body (3-5 sentences) | Detection Date | Account Brief | State | LinkedIn | HubSpot URL | Suggested Angle | Tag (NEW / CARRIED / LIGHT). Include a **Legend tab** with the score-band color coding (red ≥27 / orange 18-26 / yellow 12-17 / green 8-11) + Heat enum reference. Tim Z's xlsx writes as `weekly-signal-scan-ziemer-[YYYY-MM-DD].xlsx`; Cooper attaches after validation.

---

## Stage 5 — Canvas Run log append

Append exactly ONE row to canvas `F0B0AFSB9LN` summarizing the entire 6-segment + aggregator run.

Row format (canvas table convention):

```
| YYYY-MM-DD | Weekly Signal Scan | <status emoji> | <one-sentence summary> | <artifact links> |
```

**Status emoji:**
- ✅ `:white_check_mark:` — all 6 segments wrote successfully, all 5 rep DMs dispatched, ≥ canvas-defined coverage floor
- ⚠️ `:warning:` — 1-2 per-segment scans missing audit / Slack DM degraded / coverage below floor
- 🔴 `:red_circle:` — 3+ per-segment audits missing OR HubSpot population query returned 0 records (likely platform issue)

**One-sentence summary template:**
```
6 segments wrote N total signal records (Colo:N / Fiber:N / NeoCloud:N / NetOp:N / MSP:N / Enterprise:N). N rep DMs dispatched. N heat promotions (N→Hot, N→Warm). N NEW accounts auto-enriched.
```

**Artifact links:**
- 5 rep xlsx paths (`weekly-reports/YYYY-MM-DD/weekly-signal-scan-lieto-YYYY-MM-DD.xlsx`, `-cunningham-`, `-teague-`, `-hendrich-`, `-ziemer-`)
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

4. **Rep DM dispatch table** — one row per rep with: rep name, owner ID, Slack target, account count surfaced, NEW (⭐) count, CARRIED count, LIGHT count, top-account name + score.

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
