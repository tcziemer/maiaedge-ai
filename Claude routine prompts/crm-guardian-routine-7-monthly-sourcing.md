# CRM Guardian — Routine 7: Monthly New Account Sourcing

Monthly, 1st of each month at 9:00 AM ET (after the 6 daily routines complete). You execute the account-sourcing skill's CRM gap analysis + search-query generation pipeline to surface net-new prospect companies in priority segments. **No HubSpot writes** — every candidate surfaces as a Tier 3 review item for Cooper. Auto-creation is deliberately not enabled for this routine: the false-positive cost of a mis-classified non-ICP account entering the CRM (then diluting outreach quality and burning enrichment credits) is high. Cooper finalizes creation in the HubSpot UI after reviewing.

**CRM scale (as of 2026-04-24):** 3,489 active companies. Monthly sourcing typically surfaces 10-30 candidates, biased toward `Data Center Colo Provider` + `AI Signals - colo` and `NeoCloud` per Cooper's priority. First run may produce more if the segment-supply gap is wider than expected.

## Repo

**Orchestrator reference (for invariants + safety tiers):**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/account-sourcing/SKILL.md` (Mode 4 CRM gap analysis, Mode 2 search query generation, source evaluation)
- `skills/company-enrichment/SKILL.md` (Phase 1 quick-check on each candidate — website read only, no Apollo)
- `skills/segment-classification/SKILL.md` (qualification gates, EXCLUDE verdict routing)

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/core/icp-playbook.md`
- `context/core/segment-qualification.md`
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/neocloud.md`
- `context/segments/network-operator.md`
- `context/segments/msp-aggregator.md`
- `context/enrichment/sourcing-reference-guide.md`

**Connected tools:** HubSpot MCP (read-only this routine — dedup checks against existing CRM), Slack MCP (report delivery via `slack_send_message`), web_search + web_fetch. **Apollo not used.** **No HubSpot writes** — Tier 3 surfacing only.

## Run-Time Invariants

### A. Timezone
America/New_York. "1st of month" = Eastern calendar date.

### B. Day-Gate
Run only when today's ET date is the 1st. If not, exit cleanly with a one-line Slack DM `:mag_right: *CRM Guardian — Monthly Sourcing* — [YYYY-MM-DD] — not a 1st-of-month run, skipping.` so Cooper sees the cron fired but the routine correctly self-gated. This guards against cron firing on the wrong day across DST or scheduler bugs.

### C. Read-Only
This routine does NOT write to HubSpot. Every candidate surfaces as Tier 3 review only. The output is the Slack DM with a candidate table; Cooper or a rep finalizes creation in the HubSpot UI.

### D. Error Containment
Per-candidate try/except. On failure: log candidate identifier + step + error, continue. Surface failures in the Errors section.

### E. Default to Tier 3 When Uncertain
This routine is Tier 3 by design — every candidate is held for review. LOW / MANUAL_REVIEW classifications go to a separate "needs deeper investigation" subsection.

### F. Idempotency
Two runs on the same day produce the same candidate set (CRM state hasn't changed in 24h, search-result freshness is daily-stable for monthly cadence). Safe to re-run.

### G. MaiaEdge Gotchas
- `account_tier` is INVERTED (Tier 1 = highest priority).
- `customer_segment = "Enterprise"` is MSP/Aggregator (legacy).
- AI Colo: `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. Never use deprecated `AI - Colocation Operator` for new candidates.
- No em dashes in any candidate-facing text.
- Category descriptor: "Carrier infrastructure" only.

### H. Write Authorization
N/A — this routine writes nothing to HubSpot.

**Hard stops:** MaiaEdge own record (124293230301) — exclude from dedup-comparison set.

## Workflow

1. **CRM gap analysis (account-sourcing Mode 4):** Identify segment + sub-segment combinations where MaiaEdge is under-represented vs. estimated TAM. Priority focus per crm-guardian Job 4: `Data Center Colo Provider` + `AI Signals - colo` and `NeoCloud` (any sub-segment). Secondary focus: `Fiber Operator` + `Co-op/consortium` (BEAD-driven greenfield wave).

2. **Search query generation (account-sourcing Mode 2):** Generate 5-10 web search queries per priority segment, biased toward last-30-days news flow (greenfield builds, expansions, funding announcements, exec hires that imply a new build).

3. **Web search execution:** Run each query via `web_search`. Collect candidate companies (~50-100 raw hits per priority segment).

4. **Per candidate, quick classify:**
   - Run **company-enrichment Phase 1** on the candidate's website (one `web_fetch` of the homepage + about/products page). No Apollo call — Apollo budget is reserved for Routines 1, 2, and 8.
   - Run **segment-classification** qualification gates → verdict (ICP segment + confidence) or EXCLUDE.

5. **Dedup against HubSpot:** For each surviving ICP candidate, search HubSpot by domain (normalized: lowercase, strip `www.`, strip trailing `/`). If exists → drop, log as "already in CRM."

6. **Surface results:** Each new ICP candidate goes into the Tier 3 candidate table with: name, domain, classified segment + sub-segment, classification confidence, signal/source URL that surfaced them, recommended account_tier (per `hubspot-values.md` tier criteria).

7. **EXCLUDE candidates:** Surface separately in a "Sourced but EXCLUDE" subsection so Cooper sees what the queries pulled in (helps tune queries next month).

## Caps & Budgets

- **Candidate cap:** 50 surfaced candidates per run (HARD cap). If more pass classification, take the top 50 by confidence + tier.
- **Web fetches:** soft cap 200 web_fetch calls per run. Each candidate consumes 1-2 (homepage + sometimes one deeper page).
- **Web searches:** soft cap 50 search queries per run.
- **HubSpot reads:** dedup-by-domain only — paginated read of `domain` + `customer_segment` + `customer_segment != "Flagged for deletion"` for the 3,489 active companies (~35 pages at 1s/page = ~35s).
- **Apollo:** NOT USED. If a candidate needs Apollo enrichment to classify, defer to manual review (Tier 3 with note "needs Apollo enrich before classifying").

## Output

Structured report.

- **Subject line:** `CRM Guardian — Monthly Sourcing — [YYYY-MM-DD] — [N] candidates surfaced for review` (or `no candidates this month` if empty).
- **Hero:** total candidates surfaced, breakdown by segment + sub-segment, breakdown by confidence (HIGH / MEDIUM / LOW).
- **Candidates (Tier 3 — review needed):** Name | Domain | Segment | Sub-Segment | Recommended Tier | Confidence | Source URL | Why-Surfaced
- **Sourced but EXCLUDE (informational):** Name | Domain | Reason for exclusion (e.g., "IT MSP — out of ICP," "voice termination — out of ICP")
- **Already in CRM (informational):** count only — confirms dedup is working.
- **Query effectiveness summary:** which queries returned the most ICP candidates (helps Cooper tune next month).
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 7: Monthly Sourcing | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (Cooper Kennedy's Slack user ID — DM to self, workspace `maia-edge.slack.com`)
- **First line (subject):** `:mag_right: *CRM Guardian — Monthly Sourcing* — [YYYY-MM-DD] — [N] candidates for review`
- **Body format:** Slack mrkdwn. Candidate table in triple-backtick code block (monospace preserves alignment). Footer: `> Next run: 1st of [next month name].`
- **Thread prefix:** `CRM Guardian — Monthly Sourcing —` for Slack search grouping.
- **Character limit:** 5,000 per text element. If candidate table overflows (50 candidates × ~150 chars/row ≈ 7,500 chars), post the hero + EXCLUDE summary + query effectiveness as the parent message and nest the full Tier 3 candidates table as a threaded reply via `thread_ts`.
- On send failure: retry once with exponential backoff (1s → 2s). If still failing, log in Errors and rely on routine-platform fallback.
