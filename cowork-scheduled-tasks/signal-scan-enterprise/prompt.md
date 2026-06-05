# Signal Scan — Enterprise (Multi-DC ICP) (Cowork scheduled task)

You are running the **Enterprise segment** of MaiaEdge's weekly signal scan. This is one of 6 per-ICP scans that fire on Monday morning; the **Aggregator** task (`signal-scan-aggregator`, fires Mon 2:30pm CT) reads what all 6 wrote to HubSpot and builds the consolidated rep DMs + canvas Run log row + Cooper run report.

Your job: scrape Enterprise signal sources, score hits, write the 5 signal fields + tier to HubSpot, save a segment audit on disk. **Do NOT send rep DMs, do NOT update the canvas, do NOT write a Cooper run report.** That's the aggregator's job at 2:30pm CT.

**Enterprise is the newest ICP** (promoted 2026-05-11). Priority 5 (lowest of the ICPs but qualified and sellable). Anchor account: **Meijer** (Retail and Distribution - Enterprise, Ken Cunningham). Active April 2026 design on PBC + Port Extender for HAsync / HAfabric dark fiber diversity to SSR1300 nodes.

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
- **Context-budget safeguard** (Stage 1) - sub-agent fan-out + batched writes + a real overflow backlog.

## Phase 3 mode (locked rules)

- **Detection window: 180 days rolling** (event date within last 180 days - the `Cool` heat horizon). Any signal scoring >=8 that computes to Hot/Warm/Cool is written; only events >180 days old (Cold-by-recency) drop for staleness. (Widened from 14d on 2026-06-04 - the old gate discarded 15-180-day-old material events before scoring.)
- **Score floor: 8.** 12+ = Primary cascade (Highest 27+ / Strong 18-26 / Worth Reviewing 12-17); 8-11 = LIGHT.
- **Search-anchor pattern** is canonical access.
- **Stage 5b writes 5 signal fields + tier + heat.** `hs_is_target_account = true` freezes tier only.

## Scope — Enterprise (Multi-DC ICP) only

HubSpot target query:
```
customer_segment = "Enterprise-CustomerSegment"   -- display label is "Enterprise"
-- all account_tier values in scope (no tier filter as of 2026-06-04); Flagged-for-deletion is already excluded by the customer_segment filter above
AND type != "Customer"
AND id != 124293230301  -- MaiaEdge's own record
```

Plus the Tier 3 carryover pool from canvas `F0B0AFSB9LN`.

Sub-segments (only these 4; used at Stage 3 NEW-account classification):
- `Financial Services - Enterprise`
- `Healthcare Systems - Enterprise`
- `Retail and Distribution - Enterprise`
- `Outsourcing Services - Enterprise`

### Hard sourcing gate (BOTH must pass before any Enterprise-tagged record is created or scored)

- **Vertical gate:** one of the 4 sub-segments above. Manufacturing, Energy/Utilities, Logistics/Supply Chain → Watch List, NOT Enterprise. Government/Defense → FedRAMP-gated; not in this scan's scope.
- **Scale gate:** $1B+ revenue AND (3+ DCs OR direct Equinix Fabric / Megaport port OR confirmed in-house network engineering team via NOC presence or VP/Director/Principal Network Engineering job postings).

**Out-of-scope (auto-EXCLUDE):** sub-$1B mid-market, single-DC, network fully outsourced to single MSP, no direct carrier contracts.

## Apollo budget

Sub-cap for this task: **55 credits/run** (tied with NeoCloud for highest — Enterprise is the newest ICP and has the most NEW-account discovery + scale-gate verification volume). At Stage 0, read `weekly-reports/apollo-budget.json`; effective budget = `min(55, available_in_weekly_pool)`.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot, Apollo, Slack, web_fetch, web_search. Abort + DM Cooper if any required MCP is unavailable.
2. **Read canvas `F0B0AFSB9LN`** for Tier 3 carryovers tagged with this segment.
3. **Read Apollo budget tracker**. `effective_apollo = min(55, weekly_remaining)`.
4. **Build target list** via `search_crm_objects` with the scope filter above (all tiers, non-Flagged). Cap at 1000 records. NOTE (2026-06-04): removing the tier filter enlarges this pool; rely on the Stage 1 context-budget safeguard (sub-agent fan-out + batched writes + overflow backlog) to stay within budget. (Enterprise pool is currently small - R7 sourcing is expected to grow it.)
5. **Check prior Monday's segment-run-report** at `weekly-reports/[YYYY-MM-DD minus 7 days]/signal-scan/enterprise/`. If absent, tag everything `NEW`.

---

## Stage 1 — Signal Detection (Enterprise sources only, 180-day window)

**Context-budget safeguard (2026-06-04).** The 180-day window + all-tier scope can enlarge the candidate set and risk the context-wall that forced the 2026-05-28 per-segment split. To stay within budget: (a) fan out source detection through research sub-agents so raw source text does not all live in the main context; (b) stream the matched-account list and write in batches of 10 rather than holding every candidate resident; (c) if scored candidates exceed 60 in a single run, write what you can this run and persist the remainder to `weekly-reports/[today CT]/signal-scan/enterprise/backlog.md` - the NEXT run reads and processes that backlog FIRST (a real carry that always writes, not a discard). Out-of-window deferral no longer exists; the only carry is this budget-overflow backlog.

### Per-segment signal codes

| Code | Signal | Tier | Freshness | Confidence baseline |
|---|---|---|---|---|
| **E-A1** | New DC Build / DC Expansion / Major Capacity Add (sub-segment-specific patterns) | A | 60d | HIGH on corporate IT DC; MED on press-only |
| **E-A2** | Definitive M&A Agreement — Announcement OR Close (two-event firing) | A | ≤60d | HIGH (cross-source confirm) |
| **E-A3** | AI / GPU Workload Announcement Requiring Enterprise GPU Connectivity | A | 60d post-announce | HIGH (named GPU partner) / MED (AI strategy alone) |
| **E-A4** | Exec Hire — VP Network Infrastructure / Director Network Engineering / Principal Network Engineer | A | 30-90d post-hire | HIGH (cross-source confirm) |
| **E-A5** | Regulatory Enforcement Event / New Framework Effective Date (DORA / NY DFS / HIPAA / PCI v4.0 / India DPDP) | A | ≤60d post-event | HIGH on regulator portal + named enterprise |
| **E-A6** | Equinix Fabric / Megaport / PacketFabric / Console Connect Customer Win Naming a Named Enterprise | A | 60d | HIGH (vendor + enterprise voices) / MED (vendor-only) |
| **E-A7** | SOX 10-K / Annual Report Disclosure of Network/IT Modernization Initiative | A | 90d post-filing | HIGH |
| **E-B1** | Senior Network Role Job-Posting Surge (3+ concurrent reqs at named enterprise) | B | 30d | HIGH on Greenhouse/Lever/Ashby; MED on LinkedIn-only |
| **E-B2** | Recent Ransomware / Public-Disclosure Incident at a Peer in Same Sub-Segment (segment-wide buying shift) | B | 90d | MED (signal on segment, not account; pair to elevate) |
| **E-B3** | New Cloud / Multi-Cloud Migration Kickoff Announcement | B | 90d | MED-HIGH (named cloud + enterprise spokesperson) |
| **E-C1** | Industry Conference Speaking Slot — Network / IT Architecture Track | C | 30d pre / 14d post | HIGH on engagement; LOW alone — paired-only |
| **E-C2** | Earnings Transcript Mention of Network / Infrastructure Pain or Investment | C | 90d | MED |
| **E-C3** | Tenant of an Equinix / CoreSite / Cologix Facility — Inferred via Customer-Logo Page | C | 90d | MED-HIGH on appearance; LOW alone — paired-only |

### Sub-segment-specific trigger language

| Sub-segment | E-A1 patterns | E-A4 title patterns | E-A5 regulatory drivers |
|---|---|---|---|
| Financial Services | "trading-floor-adjacent build", "NY4/NY5 colo expansion", "European data center launch", "new corporate IT campus" | + "Markets Network", "Trading Infrastructure", "Connectivity Engineering" | DORA enforceable Jan 17 2025 + CTPP designations Nov 18 2025; NY DFS Part 500 cert due Apr 15 2026; ESMA T+1 Oct 11 2027; FFIEC BCM IV.A.6 |
| Healthcare Systems | "acquired hospital go-live", "Epic Hyperdrive cutover at [acquired site]", "new IDN data center", "PACS consolidation site" | + "Clinical Network Operations", "EHR Infrastructure", "Imaging Network" | HIPAA Security Rule NPRM (Dec 27 2024); HSCC Sector Mapping Oct 2025; CA AB 749 effective Jan 1 2025 |
| Retail and Distribution | "new fulfillment center", "Symbotic deployment", "robotics-enabled DC", "regional flow center", "new home office IT campus" | + "Store-and-DC Network", "Distribution Network Operations", "Retail Connectivity" | PCI DSS v4.0 fully in effect March 2025 — 64 new requirements, continuous segmentation validation |
| Outsourcing Services | "new delivery center", "[N]-seat ramp", "nearshore expansion", "Manila/Pune/Bangalore capacity add" | + "Delivery Center Network", "Client Connectivity", "Site Operations Network" | DORA flow-down to EU-FS BPO clients; India DPDP Rules 2025 + cross-border (Rule 15); RBI 2025 NBFC Outsourcing Directions |

### Anchor proof points (real 2024-2026 examples to validate scrapers against)

- Publix Lakeland IT campus expansion (2024-2025)
- Home Depot CIO Angie Brown appointment (June 2025) → infrastructure modernization announcements followed
- Albertsons FY2025 capex $1.7-$1.9B with Azure preferred public cloud
- Meijer (anchor for Retail and Distribution sub-segment; HAsync/HAfabric design active April 2026)
- TaskUs Medellín + Cali simultaneous opening (2025)
- Concentrix + Webhelp (closed Sep 2023), Teleperformance + Majorel (early 2025), Cognizant + Astreya (April 2026)
- Capital One / Discover (closed May 18 2025)
- CommonSpirit South region single-Epic go-live (June 2025), UPMC consolidating from 9 EHRs
- JPMorgan IndexGPT, Goldman GS AI, Morgan Stanley Knowledge Assistant
- Walmart Sparky / WIBEY agents (production 2025), Lowe's Mylow at 1,700+ stores
- Cognizant Neuro AI + NVIDIA (March 2025), Genpact AI Gigafactory with GE Vernova (Jan 2025)
- Change Healthcare BlackCat (Feb 2024, 190M records, $3.09B annual hit)
- Hot Topic Nov 2024 (57M customers via third-party analytics vendor Robling)
- Shopify Cyber Monday outage Dec 1 2025 ($14.2B day)

Plus the **Universal signal types** (U1-U6) and **Apollo signal classes** (AP-1, AP-2, AP-3, AP-4 paired, AP-7, FR-1 — AP-5/AP-6 disabled).

### Source Registry (Enterprise — execute every source, record ✓/✗ in audit)

Per [`context/signals/enterprise-signals.md`](../../context/signals/enterprise-signals.md) §"Sources for This Segment". Largest source registry of the 6 segments.

**Robust tier (single-source can score HIGH on non-major signals):**
1. StockTitan (`stocktitan.net/sec-filings/{ticker}/`) — SEC 8-K mirror for public Enterprise targets; covers 10-K, 10-Q, 8-K Items 1.01 / 2.01 / 5.02 / 8.01, DEF 14A, 20-F
2. SEC EDGAR full-text via search-anchor — backup; preferred for 20-F + DEF 14A
3. PR Newswire + Business Wire + GlobeNewswire — Data Center / Healthcare / Banking / BPO tags + "People on the Move" + "Appointments"
4. American Banker — Financial Services IT/leadership/regulatory/M&A
5. Modern Healthcare — IT capex, M&A, leadership at multi-hospital IDNs
6. Becker's Hospital Review — IT leadership column, HIPAA breach roundup, IDN expansion (strongest single Healthcare Systems source per 2026-05-11 reachability audit)
7. Retail Dive — store/DC openings, retail IT, M&A
8. Nelson Hall — BPO leadership briefs, deal coverage, AI moves (awareness-tier only — most content subscription-gated; treat as market awareness, not specific-account triggering)
9. Everest Group — BPO + IT services rankings, deal news, leadership moves
10. Greenhouse + Lever + Ashby public job boards — senior network role postings at target Enterprise list (E-B1)
11. Apollo MCP — `apollo_organizations_enrich` + Job Postings + Job Changes (AP-1 paired with E-A4 is high-fit)
12. Equinix newsroom + customer-story page — E-A6 vendor customer wins naming Enterprise sub-segment accounts
13. Megaport customer-success page + press releases — E-A6
14. PacketFabric + Console Connect customer-success pages — E-A6
15. HHS OCR breach portal + HIPAA Journal monthly recap (`hipaajournal.com` — operational mirror; portal is JSF dynamic table not scrape-friendly) — E-A5 Healthcare trigger
16. NY DFS portal — enforcement actions + Part 500 cert filings (E-A5 Financial Services)
17. PCI Security Standards Council news — v4.0 enforcement (E-A5 Retail)
18. DORA enforcement updates — EBA / ESMA / EIOPA CTPP designations + supervisory expectations
19. NVIDIA Newsroom + Partner pages — Cognizant Neuro, Teleperformance, enterprise GenAI + GPU partnerships (E-A3)
20. Earnings transcripts — Seeking Alpha (free headlines) + Motley Fool + MarketBeat + 10-Q transcripts via StockTitan; keyword filter `"network modernization"`, `"third-party fabric"`, `"private connectivity"`, `"GenAI infrastructure"`, `"DC consolidation"` (E-A7, E-C2)

**Medium tier (cross-source confirm preferred for major M&A / regulatory claims):**
21. Bloomberg AI + tech beat — enterprise GenAI deployments, GPU contract coverage (paywalled; headlines in search snippets)
22. WSJ tech beat + CIO Journal — enterprise IT capex, connectivity, AI strategy
23. Risk & Insurance + ISMG GovInfoSecurity — segment-wide segmentation reviews post-incident (strongest Financial Services breach feed per 2026-05-11 audit)
24. CIO.com + InformationWeek — enterprise IT leadership coverage
25. Bisnow Data Center — enterprise as DC tenant (when leasing colo)
26. Data Center Frontier + Data Center Dynamics — enterprise-tenant lease coverage
27. Mergermarket + S&P Global Market Intelligence — M&A deal coverage
28. PitchBook public pages — PE / strategic deal coverage
29. Crunchbase News — enterprise tech leadership moves + acquisitions
30. HIMSS Media + CHIME news — healthcare IT leadership + IDN coverage
31. RIS News + STORES Magazine — retail IT including PCI v4.0 reactions
32. Sibos / Money 20/20 / HIMSS / NRF / CCW / NASSCOM agenda pages — speaker scrapes (context only)
33. Cross-segment exec hire stack — StockTitan 8-K 5.02, PR Newswire Appointments, IR newsroom diffs, Crunchbase Exec Moves (E-A4)

**International supplement (Tim Z territory):**
- **EMEA:** Financial News London, Bobsguide, Risk.net (DORA + ECB CTPP), EBA / ESMA / EIOPA / FCA UK portals. Retail Week (UK), Linéaires (FR), Lebensmittel Zeitung (DE). Big-3 EU IDNs via national portals.
- **APAC:** Asian Banker, Risk.net APAC, Nikkei Asia financial. Outsourcing Services is biggest APAC sub-segment (Cognizant, Tata, Wipro, Infosys, Genpact, Concentrix India + Manila/Cebu BPOs) — Economic Times India IT, Business Standard India, Inquirer Manila tech, Nasscom, Contact Center Pipeline Asia.
- **LATAM + MENA:** Limited Enterprise ICP presence; defer to opportunistic surfacing.

**Source Coverage Mandate:** every documented source above MUST be attempted via search-anchor and recorded ✓ / ✗. Generic queries that don't anchor on a documented source do NOT count.

### Explicitly NOT Tracked (Enterprise-specific noise list)

| Pattern | Action |
|---|---|
| "AI Practice" launches at consulting firms inside Enterprise sub-segments (Deloitte, McKinsey, BCG, Bain) | EXCLUDE — those are project firms, NOT Outsourcing Services - Enterprise |
| Generic IT modernization press releases without specific network/connectivity programs | EXCLUDE |
| Branch SD-WAN deployments at retailers (branch is saturated; inter-DC + cloud-on-ramp is the live conversation) | EXCLUDE |
| Manufacturing plant network expansions | EXCLUDE — fails vertical gate (Watch List, not Enterprise ICP) |
| ESG / sustainability data center announcements without operational connectivity mention | EXCLUDE |
| Conference sponsorship logos (vs. speaking slots) | EXCLUDE — sponsorship = marketing budget, not network intent |
| LinkedIn posts about "AI strategy" without specific compute provider or production deployment | EXCLUDE |
| Conference speaking slot alone (E-C1) | EXCLUDE per noise list — paired-only |
| AP-6 Apollo Intent without pairing | EXCLUDE (>50% false-positive rate) |
| Sub-$1B mid-market enterprise OR single-DC OR fully-outsourced network OR no direct carrier contracts | EXCLUDE — fails scale gate |

---

## Stage 2 — Match detected signals to target accounts

For each detected signal candidate:
1. Exact company name match (case-insensitive)
2. Domain apex + subdomain variants
3. LinkedIn slug match
4. SEC CIK lookup (for 10-K / 8-K / 13D signals)

Surviving → `matched_accounts[]`. Unmatched → `new_account_candidates[]`.

---

## Stage 3 — NEW-account creation (Apollo-bound, max 55 credits) + Hard Sourcing Gate

For each `new_account_candidate`:

1. **Apply the hard sourcing gate first** — verify vertical (one of the 4 sub-segments) AND scale ($1B+ revenue AND multi-DC marker). If either fails, EXCLUDE. Apollo budget is precious — don't burn it on candidates that will fail the gate.
2. **D1 disqualifier check** per [`context/account-tiering/sub-segment-qualification-full.md`](../../context/account-tiering/sub-segment-qualification-full.md) §D1.
3. **Stage 1a–1c research-first workflow** per [`skills/company-enrichment/SKILL.md`](../../skills/company-enrichment/SKILL.md). Confirm scale-gate criteria during research (3+ DCs via 10-K Properties section; direct Equinix Fabric / Megaport port via E-A6 source registry; in-house network engineering via VP/Director/Principal Network postings on Greenhouse/Lever/Ashby).
4. **Apollo enrichment** for $1B+ revenue confirmation + firmographics. Decrement budget.
5. **Segment routing per D3 flowchart** — must route to `customer_segment = "Enterprise-CustomerSegment"` AND one of the 4 sub-segments to remain in scope.
6. **D5 sub-segment protocol** per [`context/account-tiering/enrichment-protocols.md`](../../context/account-tiering/enrichment-protocols.md) §6 (E1-E4 protocols).
7. **Compute tier** per [`context/account-tiering/tier-compute-spec.md`](../../context/account-tiering/tier-compute-spec.md). Default `signal_heat = Cold` on new accounts.
8. **Write to HubSpot**. Bump `last_enriched_date = today (CT)` — full enrichment pass.

If Apollo exhausts mid-Stage 3, finish current then halt. Remaining surface in audit.

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
  +6 if E-A2 M&A announcement AND close both fire within 12mo

Pairing rules (E-C1 / E-C3 paired-only):
  E-C1 (conference speaking) fires ONLY when stacked with another Enterprise signal on the same account in same 30d window.
  E-C3 (colo logo-page tenant) fires ONLY when stacked with another Enterprise signal on the same account in same 30d window.
  E-B2 (peer ransomware) is segment-wide context — score against ALL Tier 1+2 accounts in the same sub-segment when fresh; pairs with an account-specific signal to elevate.

Score ranges:
  27+   → Highest Priority cascade tier
  18-26 → Strong Signals cascade tier
  12-17 → Worth Reviewing cascade tier
  8-11  → LIGHT cascade tier
  <8    → Silent drop
```

Highest-scored signal per account wins for the narrative + date write.

---

## Stage 4.5 — Sub-Agent QA Gate (10 rules)

1. **Source URL verification** — cited URL real, reachable, content matches claim.
2. **Freshness** — event date within 180 days rolling window. Drop only if older than 180 days (it would compute to `Cold`).
3. **Segment classification + hard gate** — `customer_segment = "Enterprise-CustomerSegment"` post-Stage 3 + scale gate ($1B+ revenue, multi-DC) confirmed. Drop if scale gate not confirmed.
4. **Field overflow** — narrative ≤250 chars.
5. **Owner mapping** — `hubspot_owner_id` maps to East / West / International.
6. **Rep-facing copy scan** — pure prose, no date prefix, no `[Routine N]` tag, no em dashes, no competitor names.
7. **Score arithmetic** — math + bonuses correct; paired-only signals (E-C1, E-C3) only score when stacked.
8. **Dedup** — no double-counting.
9. **NEW/CARRIED integrity** — CARRIED requires prior segment-run-report confirmation.
10. **Pure-prose narrative** — Stage 5 writes pure prose, no prefix.

Any rule failure → fix or drop. Log drops in audit.

---

## Stage 5 — HubSpot narrative write (pure prose, NO date prefix)

**Anti-churn write rule (required under the 180-day window):** write the signal fields only if the detected event date is newer than the record's current `last_signal_date`, OR the record has no `last_signal_date`, OR the new score exceeds the stored `last_signal_score`. If the freshest detected signal is not newer or higher than what is already stored, skip the write (idempotent no-op). Never overwrite a newer stored signal with an older detection. This keeps the wide window from re-writing the same aging signal every Monday.

For each scored hit ≥8 that passes the anti-churn rule, write `recent_news_or_trigger_event` via `manage_crm_objects` (batches of 10, 250ms between, exponential backoff on 429).

- **Format:** pure-prose 1-sentence narrative, ≤250 chars. Examples: `"M&A Close — Capital One completed acquisition of Discover; 18-36 month network integration project window now open; inter-DC + cloud on-ramp consolidation in flight"` or `"Healthcare Network Modernization — IDN's 10-K disclosed multi-quarter network modernization tied to Epic Hyperdrive cutover at 4 acquired hospitals"`.
- **NO leading `[YYYY-MM-DD]` prefix.** Date lives in `last_signal_date`.
- **NO `[Routine 2]` / `[Signal Scan]` / `[Enterprise]` tag.**
- **NO em dashes** (use hyphens or restructure).
- **NO competitor names** (use "third-party fabrics" / "third-party platform" instead).

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
weekly-reports/[today CT YYYY-MM-DD]/signal-scan/enterprise/segment-run-report.md
```

Content:
1. Run header (date, segment, Apollo consumed X of 55, runtime, MCPs).
2. Source coverage table (every documented source above, ✓ / ✗; track 3-week ✗ streak).
3. Candidate funnel (target list size, candidates, matches, NEW accounts, total writes, drops).
4. Hard-gate rejections — record-level audit of candidates that failed the vertical or scale gate (useful for refining the target list).
5. Score distribution (8-11, 12-17, 18-26, 27+).
6. Writes summary per record (id, name, E- signal code, score, heat delta, tier delta, sub-segment).
7. Tier 3 holds (carryover records still Tier 3; re-append to canvas).
8. QA gate drops with reasons.
9. Failed writes.
10. Apollo budget post-run.
11. Sub-segment volume breakdown (Financial / Healthcare / Retail / Outsourcing) — useful for monitoring whether one sub-segment is dominating the registry.

End the run. **No rep DMs, no canvas Run log, no Cooper run report.** Aggregator at 2:30pm CT handles all three.

---

## Failure handling

- **HubSpot MCP errors:** retry (250ms → 1s → 4s, max 3). Log to "Failed writes".
- **web_fetch / web_search errors:** log source as ✗. 3-week streak auto-flags.
- **Apollo MCP errors mid-Stage-3:** halt Stage 3, continue Stage 4.
- **SEC EDGAR / StockTitan errors:** fall back to the other (StockTitan = primary; EDGAR = backup). Log if both fail.
- **HHS OCR portal access errors (E-A5 Healthcare):** fall back to HIPAA Journal monthly recap. Log.
- **Canvas read failure:** proceed without carryover, log warning.
- **Git contention on Apollo budget tracker:** log + continue; JSON updated locally.

## End-of-run footer

```
[Enterprise] target=N matched=N new=N writes=N heat_promotions=N gate_rejections=N apollo=N/55 runtime=Nmin audit=weekly-reports/YYYY-MM-DD/signal-scan/enterprise/
```

No Slack DM from this task. The aggregator owns rep + Cooper communication.
