# Signal Scan — MSP/Aggregator (Cowork scheduled task)

You are running the **MSP/Aggregator segment** of MaiaEdge's weekly signal scan. This is one of 6 per-ICP scans that fire on Monday morning; the **Aggregator** task (`signal-scan-aggregator`, fires Mon 2:30pm CT) reads what all 6 wrote to HubSpot and builds the consolidated rep DMs + canvas Run log row + Cooper run report.

Your job: scrape MSP signal sources, score hits, write the 5 signal fields + tier to HubSpot, save a segment audit on disk. **Do NOT send rep DMs, do NOT update the canvas, do NOT write a Cooper run report.** That's the aggregator's job at 2:30pm CT.

**MSP/Aggregator is the LOWEST-velocity segment** with the thinnest source registry of the six. CRN drift toward award-press syndication means weight Channel Futures + ChannelE2E + TSD direct IR over CRN. If yield falls below 25 floor, promote EMEA channel press into the rotation.

**Critical IT MSP Test:** MSP/Aggregator is **telecom/network aggregators, NOT IT MSPs**. Helpdesk / cybersecurity MSPs are EXCLUDED. Apply the IT MSP Test at every detection: if the entity sells helpdesk / cybersecurity / endpoint-management as primary line, EXCLUDE per signal-framework False Positive Patterns.

## What changed 2026-05-28 (engine unification)

- `last_signal_date` semantics narrowed: stores the **event date**, NOT detection date.
- `recent_news_or_trigger_event` is pure prose; legacy date prefix retired.
- `signal_heat` is **Title Case** per HubSpot.
- 5-field signal engine; `account_brief` is pure prose, NO `[Routine N] [date]:` prefix.

## What changed 2026-06-04 (coverage expansion)

- **Detection window widened 14d -> 180 days** (event-date basis), aligned to the `Cool` heat horizon. Anything scoring >=8 that computes to Hot/Warm/Cool is written; only >180d (Cold-by-recency) drops for staleness. Ends the prior behavior where 15-180-day-old material events were discarded before scoring (the cause of the 2026-06-01 near-empty quiet week).
- **Scope widened to all tiers** - the target query no longer filters `account_tier IN (1,2,3)`; every non-Flagged record in this segment is eligible. Matched-account writes cost no Apollo; heat still ranks rep priority.
- **Anti-churn write rule** (Stage 5b) prevents the wide window from re-writing aging signals weekly.
- **Tier A freshness gained a 90-180d ×1 band** so strong, still-relevant events clear the score-8 floor out to 180 days.
- **Context-budget safeguard** (Stage 1) - sub-agent fan-out + batched writes + a real overflow backlog, since scope/window expansion roughly doubles candidates and risks the context-wall that forced the 2026-05-28 split.

## Phase 3 mode (locked rules)

- **Detection window: 180 days rolling** (event date within last 180 days - the `Cool` heat horizon). Any signal scoring >=8 that computes to Hot/Warm/Cool is written; only events >180 days old (Cold-by-recency) drop for staleness. (Widened from 14d on 2026-06-04 - the old gate discarded 15-180-day-old material events before scoring.)
- **Score floor: 8.** 12+ = Primary cascade; 8-11 = LIGHT.
- **Search-anchor pattern** is canonical access.
- **Stage 5b writes 5 signal fields + tier + heat.** `hs_is_target_account` freezes tier only.
- **Priority routing:** M-A1, M-A2, M-A4, M-A5, M-A6, M-A7, M-B4 = 48-hour-window signals (channel moves fast). Surface with the high-priority flag in the audit so the aggregator can prioritize them in the rep DM cascade.

## Scope — MSP/Aggregator only

HubSpot target query:
```
customer_segment = "MSP/Aggregator"
-- all account_tier values in scope (no tier filter as of 2026-06-04); Flagged-for-deletion is already excluded by the customer_segment filter above
AND type != "Customer"
AND id != 124293230301  -- MaiaEdge's own record
```

Plus the Tier 3 carryover pool from canvas `F0B0AFSB9LN`.

Sub-segments (5 active post-2026-05-13; used at Stage 3 NEW-account classification):
- `Telecom Aggregator - MSP`
- `Managed Network Services - MSP` (NOT the legacy `- Network Operator` suffix, which was archived 2026-05-13)
- `TSD Technology Services Distributor - MSP`
- `Master Agent - MSP`
- `Cloud + Telecom Hybrid MSP - MSP`

Two subtypes in scope per [`context/segments/msp-aggregator.md`](../../context/segments/msp-aggregator.md):
1. US TSD / TA channel: Telarus / AppDirect / Upstack / AVANT / Bridgepointe / Sandler / ScanSource Intelisys + TA agencies
2. NaaS platform operators: CBC Tech, Epsilon, PCCW Console Connect, Arelion, Sparkle Sparkhub

**Do NOT target (auto-EXCLUDE per IT MSP Test):** IT MSPs (helpdesk, cybersecurity), voice termination wholesalers, SMS/A2P/CPaaS aggregators, cellular IoT MVNOs, roaming hubs/IPX providers, eSIM/SIM platform vendors.

## Apollo budget

Sub-cap for this task: **20 credits/run** (lowest of the 6 — MSP has the thinnest NEW-account discovery volume). At Stage 0, read `weekly-reports/apollo-budget.json`; effective budget = `min(20, available_in_weekly_pool)`.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_fetch, web_search. Abort + DM Cooper if any required MCP is unavailable.
2. **Read canvas `F0B0AFSB9LN`** for Tier 3 carryovers tagged with this segment.
3. **Read Apollo budget tracker**. `effective_apollo = min(20, weekly_remaining)`.
4. **Build target list** via `search_crm_objects` with the scope filter above (all tiers, non-Flagged). Cap at 1000 records (typical MSP ICP pool is ~80–150 records — thinnest segment). NOTE (2026-06-04): removing the tier filter materially enlarges this pool (all-tier vs the prior Tier 1-3); rely on the Stage 1 context-budget safeguard (sub-agent fan-out + batched writes + overflow backlog) to stay within budget.
5. **Check prior Monday's segment-run-report** at `weekly-reports/[YYYY-MM-DD minus 7 days]/signal-scan/msp/`. If absent, tag everything `NEW`.

---

## Stage 1 — Signal Detection (MSP sources only, 180-day window)

**Context-budget safeguard (2026-06-04).** The 180-day window + all-tier scope roughly doubles the candidate set, which risks the context-wall that forced the 2026-05-28 per-segment split. To stay within budget: (a) fan out source detection through research sub-agents so raw source text does not all live in the main context; (b) stream the matched-account list and write in batches of 10 rather than holding every candidate resident; (c) if scored candidates exceed 60 in a single run, write what you can this run and persist the remainder to `weekly-reports/[today CT]/signal-scan/msp/backlog.md` - the NEXT run reads and processes that backlog FIRST (a real carry that always writes, not a discard). Out-of-window deferral no longer exists; the only carry is this budget-overflow backlog.

### Per-segment signal codes

| Code | Signal | Tier | Freshness | Confidence baseline | Priority |
|---|---|---|---|---|---|
| **M-A1** | PE Acquisition / TSD Roll-up — Announcement OR Close (two-event firing) | A | ≤60d | HIGH | 48h |
| **M-A2** | Carrier Dropped from Line Card | A | 1wk | HIGH | 48h |
| **M-A3** | New Carrier Added to Portfolio | A | 1wk | HIGH | normal |
| **M-A4** | "AI Practice" / "AI Solutions" Launch (must pass IT MSP Test) | A | 30d | HIGH | 48h |
| **M-A5** | Exec Hires — CRO / VP Solutions Engineering / VP Product / VP AI Practice | A | 30d | HIGH | 48h |
| **M-A6** | TSD Platform / Quoting-Engine Replatforming (job-post signal) | A | 30d | MED-HIGH | 48h |
| **M-A7** | ScanSource / TDSYN Earnings Recurring-Revenue-Mix Disclosure | A | quarterly | HIGH | 48h |
| **M-B1** | Layoffs / Restructuring at Major Aggregators | B | 90d | MED-HIGH | normal |
| **M-B2** | NaaS / SASE / SD-WAN Platform Launch by TSD or Agent Group | B | 90d | MED-HIGH | normal |
| **M-B3** | New Marketplace / Portal / Quote-Engine Launch | B | 90d | MED-HIGH | normal |
| **M-B4** | Public-Company Earnings — Agent Business / Automation / Convergence Mentions | B | 90d | HIGH | 48h |
| **M-B5** | Enterprise Logo / Customer Win Announcements | B | 90d | MED | normal |
| **M-C1** | Channel Conference Speaking Slots | C | 60d | MED-HIGH | normal |
| **M-C2** | FedRAMP / CMMC / StateRAMP Push Announcements | C | 90d | MED-HIGH | normal |
| **M-C3** | Copper Retirement / TDM Sunset / STIR-SHAKEN Mandates | C | 90d | MED | normal |
| **M-C4** | New Enterprise Vertical Announcement (Healthcare, Finance, Manufacturing) | C | 90d | MED | normal |
| **M-C5** | Multi-Carrier Outage / SLA Finger-Pointing Public Incident (7-14d post-incident) | C | 60d | MED (timing-sensitive) | 48h |

Plus the **Universal signal types** (U1-U6) and **Apollo signal classes** (AP-1, AP-2, AP-3, AP-4 paired, AP-7, FR-1 — AP-5/AP-6 disabled).

### Source Registry (MSP — execute every source, record ✓/✗ in audit)

Per [`context/signals/msp-aggregator-signals.md`](../../context/signals/msp-aggregator-signals.md) §"Sources for This Segment".

**Robust tier (single-source can score HIGH on non-major signals):**
1. Channel Futures — M&A, hirings, carrier agreements, layoffs, vertical tags + Channel Futures Hiring Roundup column
2. ChannelE2E + ChannelE2E People column
3. TSD press pages — Telarus, AppDirect, Sandler Partners, AVANT, Bridgepointe, Upstack, AppSmart, Intelisys (ScanSource subsidiary), ScanSource agent business (weekly diff)
4. CRN — channel + agent + TSD news (weight lower than Channel Futures + ChannelE2E given award-press drift)
5. StockTitan (`stocktitan.net/sec-filings/{ticker}/`) — SEC 8-K mirror for public TSDs (SCSC ScanSource, SNX TD SYNNEX, CMCSA Comcast Business); covers 8-K Items 1.01 / 2.01 / 5.02
6. SEC EDGAR full-text via search-anchor — backup to StockTitan
7. FCC Daily Digest
8. ScanSource + TD SYNNEX investor relations + earnings calls — quarterly deeper read; 10-Q transcripts via StockTitan or search-anchor (M-A7, M-B4)
9. PR Newswire + Business Wire + GlobeNewswire — Channel + Telecom feed + Appointments tag
10. Apollo MCP — `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events
11. Megaport + Console Connect + PacketFabric partner-add announcements — when an aggregator partners with a NaaS platform, that's M-A3
12. Greenhouse + Lever + Ashby public job boards at target TSDs (M-A6 platform replatforming signal)

**Medium tier:**
13. CompTIA / GTIA (CompTIA community spun out as GTIA in 2025; both names in use)
14. Channel Partner Insight (UK) + IT Europa + ChannelBiz (DACH) — promote into weekly rotation if domestic yield falls below 25-floor
15. FedRAMP Marketplace new-authorization feed (M-C2)
16. Telecompetitor channel section
17. CP Expo / MSP Summit / NexGen + Channel Partners Conference & Expo agenda scrapers (context only)
18. Gartner SD-WAN Magic Quadrant + Forrester Wave reports (paywalled; headlines in search snippets)
19. Frost & Sullivan TSD analysis (paywalled; headlines only)
20. TBI Connect (UK) + Channel Asia

**International (Tim Z territory — thinnest of the 6 segments internationally; MSP/Aggregator ICP is predominantly a US channel concept):**
- **EMEA:** Channel Partner Insight (UK), IT Europa, ChannelBiz (DACH). Low cadence — flag only significant moves. Target companies: Expereo, Masergy legacy assets, Wavenet, ITancia.
- **APAC / LATAM / MENA:** Minimal ICP fit. Deprioritize unless Tim Z flags specific regional aggregator activity.

**Source Coverage Mandate:** every documented source above MUST be attempted via search-anchor and recorded ✓ / ✗. Generic queries that don't anchor on a documented source do NOT count.

### False-positive patterns — DOWNGRADE or EXCLUDE at detection time

| Pattern | Action |
|---|---|
| **"AI Practice" / "AI Solutions" launch press from IT MSP (helpdesk + cybersecurity)** | **EXCLUDE — fails the IT MSP Test** (`context/segments/msp-aggregator.md` ICP Exclusion List) |
| Voice termination wholesaler / SMS/A2P / CPaaS aggregator / cellular IoT MVNO / roaming hub / IPX provider / eSIM platform | EXCLUDE — wrong subtype |
| Apollo job change with no LinkedIn profile confirming the move | DOWNGRADE to MEDIUM (Apollo lag-data has departure-date ambiguity) |
| "Carrier dropped" without TSD's own press confirmation (forum chatter only) | DOWNGRADE to MEDIUM |
| Wayback Machine line-card diff alone (no trade press) | DOWNGRADE to MEDIUM (Wayback = Aspirational tier) |
| Conference speaking slot alone | EXCLUDE per noise list |
| AP-6 Apollo Intent without pairing | EXCLUDE (>50% false-positive rate) |
| CRN award-press syndication (Channel Chiefs, Women of the Channel) | EXCLUDE — not a buying signal |

---

## Stage 2 — Match detected signals to target accounts

For each detected signal candidate:
1. Exact company name match (case-insensitive)
2. Domain apex + subdomain variants
3. LinkedIn slug match

Surviving → `matched_accounts[]`. Unmatched → `new_account_candidates[]`.

---

## Stage 3 — NEW-account creation (Apollo-bound, max 20 credits)

For each `new_account_candidate`:

1. **D1 disqualifier check** + **IT MSP Test** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D1. If the candidate is a helpdesk/cybersecurity MSP (not a telecom aggregator), EXCLUDE.
2. **Stage 1a–1c research-first workflow** per [`skills/company-enrichment/SKILL.md`](../../skills/company-enrichment/SKILL.md).
3. **Apollo enrichment**. Decrement budget.
4. **Segment routing per D3 flowchart** — must route to `customer_segment = "MSP/Aggregator"` to remain in scope. **Master Agent independents** (X4 Solutions confirmed; CyberNet Communications medium) route to `Master Agent - MSP` sub-segment; if anchor verification is thin, assign `low_5069` confidence — D7 weekly task re-validates.
5. **D5 sub-segment protocol** per [`context/account-tiering/enrichment-protocols.md`](../../context/account-tiering/enrichment-protocols.md) §6.
6. **Compute tier** per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). Default `signal_heat = Cold` on new accounts.
7. **Write to HubSpot**. Bump `last_enriched_date = today (CT)` — full enrichment pass.

If Apollo exhausts mid-Stage 3, finish current then halt.

---

## Stage 4 — Score each matched signal

```
Score = Tier × Freshness × Confidence

Tier:        A = 3, B = 2, C = 1
Freshness:   Tier A:  ≤60d = 3, 60-90d = 2, 90-180d = 1, >180d = drop
             Tier B:  ≤1wk = 3, ≤30d = 2, ≤90d = 1, >90d = drop
Confidence:  HIGH = 3, MEDIUM = 2, LOW = 1

Bonuses:
  +6 if 2+ signals same account in same 30d window AND at least one signal ≥8
  +6 if M-A1 announcement AND close both fire within 12mo

Score ranges:
  27+   → Highest Priority cascade tier
  18-26 → Strong Signals cascade tier
  12-17 → Worth Reviewing cascade tier
  8-11  → LIGHT cascade tier
  <8    → Silent drop
```

**48-hour priority signals** (M-A1, M-A2, M-A4, M-A5, M-A6, M-A7, M-B4, M-C5) get tagged `priority: 48h` in the audit. The aggregator at 2:30pm CT reads this tag and surfaces them at the top of the rep DM cascade.

Highest-scored signal per account wins for the narrative + date write.

---

## Stage 4.5 — Sub-Agent QA Gate (10 rules)

1. **Source URL verification** — cited URL real, reachable, content matches claim.
2. **Freshness** — event date within 180 days rolling window. Drop only if older than 180 days (it would compute to `Cold`).
3. **Segment classification** — `customer_segment = "MSP/Aggregator"` post-Stage 3 + IT MSP Test passed.
4. **Field overflow** — narrative ≤250 chars.
5. **Owner mapping** — `hubspot_owner_id` maps to a current territory owner: Lieto NE+West `161889085` / Ken SE `162339176` / Tory Central `165480917` / Markus Europe `164949459` / Ziemer Intl+Tier 1 SP `159350430` / Cooper Unassigned `160267902`.
6. **Rep-facing copy scan** — pure prose, no date prefix, no `[Routine N]` tag, no em dashes, no competitor names.
7. **Score arithmetic** — math + bonuses correct.
8. **Dedup** — no double-counting.
9. **NEW/CARRIED integrity** — CARRIED requires prior segment-run-report confirmation.
10. **Pure-prose narrative** — Stage 5 writes pure prose, no prefix.

Any rule failure → fix or drop. Log drops in audit.

---

## Stage 5 — HubSpot narrative write (pure prose, NO date prefix)

**Anti-churn write rule (required under the 180-day window):** write the signal fields only if the detected event date is newer than the record's current `last_signal_date`, OR the record has no `last_signal_date`, OR the new score exceeds the stored `last_signal_score`. If the freshest detected signal is not newer or higher than what is already stored, skip the write (idempotent no-op). Never overwrite a newer stored signal with an older detection. This keeps the wide window from re-writing the same aging signal every Monday.

For each scored hit ≥8 that passes the anti-churn rule, write `recent_news_or_trigger_event` via `manage_crm_objects` (batches of 10, 250ms between, exponential backoff on 429).

- **Format:** pure-prose 1-sentence narrative, ≤250 chars. Examples: `"PE Roll-up Announcement — Upstack signed definitive agreement to acquire AdvisorOne's TSD book; integration scoping window now open"` or `"AI Practice Launch — Telarus unveiled AI Solutions Practice; deterministic-path SLA conversation for AI workloads is the opener"`.
- **NO leading `[YYYY-MM-DD]` prefix.** Date lives in `last_signal_date`.
- **NO `[Routine 2]` / `[Signal Scan]` / `[MSP]` tag.**
- **NO em dashes** (use hyphens or restructure).
- **NO competitor names.**

**Do NOT bump `last_enriched_date`** (partial signal write). Exception: Stage 3 NEW-account creates DO bump.

---

## Stage 5b — Structured signal fields + tier/heat recompute

For each scored hit:

- **`last_signal_date`** = event date from source article (NOT today's date).
- **`last_signal_score`** = computed score.
- **`signal_count_last_30d`** = recompute.
- **`signal_heat`** = computed per inlined spec below (Title Case enum).
- **`account_tier`** = recomputed. **SKIP tier write if `hs_is_target_account = true`**.

### Inlined `compute_signal_heat` (from `tier-compute-spec.md` §11.5)

```
Heat is computed top-down, first match wins. HubSpot enum is Title Case.

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Override: hs_is_target_account = true does NOT freeze signal_heat.
Tier is rep-locked; heat always reports the truth.

Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
Output: enum Hot | Warm | Cool | Cold (Title Case per HubSpot).
```

**Do NOT bump `last_enriched_date`** (partial signal write).

---

## Stage 5c — Save segment audit on disk

Write a per-segment run report to:
```
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/msp/segment-run-report.md
```

Content:
1. Run header (date, segment, Apollo consumed X of 20, runtime, MCPs).
2. Source coverage table (every documented source above, ✓ / ✗; track 3-week ✗ streak).
3. Candidate funnel.
4. Score distribution.
5. Writes summary per record (id, name, M- signal code, score, heat delta, tier delta, **priority tag** if 48h).
6. Tier 3 holds.
7. QA gate drops with reasons.
8. Failed writes.
9. Apollo budget post-run.
10. IT MSP Test rejections (record-level — useful audit for any borderline candidates dropped).
11. EMEA fallback flag — if Robust-tier yield was below 25, surface a recommendation to promote EMEA channel press for next run.

End the run. **No rep DMs, no canvas Run log, no Cooper run report.** Aggregator at 2:30pm CT handles all three.

---

## Failure handling

- **HubSpot MCP errors:** retry (250ms → 1s → 4s, max 3). Log to "Failed writes".
- **web_fetch / web_search errors:** log source as ✗. 3-week streak auto-flags.
- **Apollo MCP errors mid-Stage-3:** halt Stage 3, continue Stage 4.
- **Canvas read failure:** proceed without carryover, log warning.
- **Git contention on Apollo budget tracker:** log + continue; JSON updated locally.

## End-of-run footer

```
[MSP] target=N matched=N new=N writes=N heat_promotions=N priority_48h=N apollo=N/20 runtime=Nmin audit=weekly-reports/YYYY-MM-DD/signal-scan/msp/
```

No Slack DM from this task. The aggregator owns rep + Cooper communication.
