# Weekly Market News (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget, stateless across runs (sources are scraped fresh per run). Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Friday, 1:00 PM CT. Cron: `0 13 * * 5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**

Pure web-scraping → Slack delivery. Zero CRM reads, zero CRM writes.

Scrapes the prior 7 days of industry news across the **6 ICPs** MaiaEdge sells into (5 operator segments + Enterprise as 6th, ICP-promoted 2026-05-11) and delivers a market-awareness digest with a "What this means for MaiaEdge" angle on every story. Awareness, not action.

This is **the companion** to Weekly Signal Scan:
- Signal Scan: "these specific accounts in your CRM had buying-relevant events this week"
- Market News: "here's what's happening across our 5 ICPs as a market this week so you walk into every conversation hyper-educated"

**Phase 0 delivery (ACTIVE 2026-04-28):** Cooper-only DM (2 messages: digest + audit). Reps DO NOT receive direct delivery yet - Cooper reviews quality and forwards manually until rep-direct routing is approved after 2-4 clean runs.

---

## Connected Tools (Cowork)

- **Slack MCP** - `slack_send_message` (2 DMs: digest + audit), `slack_read_canvas` + `slack_update_canvas`
- **`web_search`** - PRIMARY research path
- **`web_fetch`** - opportunistic enhancement (skip on failure, no penalty)
- **Bash + git** - commit markdown mirror to `weekly-reports/YYYY-MM-DD/market-news/`
- **No HubSpot, no Apollo.** This routine is purely web-scraping.

---

## Loud Failure Rule

Every run MUST end with both DMs (digest + audit), including:
- Quiet weeks ("0 on-thesis stories across all 6 ICPs - back next Friday")
- Fatal errors ("Routine aborted at Stage X")
- Partial runs (some sources unreachable)

No silent runs ever. Retry the DMs 3× on send failure; if all fail, append summary to ledger canvas.

---

## Reference Files (read at run start)

### Repo conventions
- `CLAUDE.md` (key rules, MSP label "MSP / Aggregator", "Carrier infrastructure" only)

### ICP cheatsheets - all 6 every run (story relevance depends on this)
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/network-operator.md`
- `context/segments/neocloud.md`
- `context/segments/msp-aggregator.md` (TSD channel + NaaS platform operators, ICP exclusion list)
- `context/segments/enterprise.md` (Multi-DC ICP, 4 sub-segments - Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services. Anchor: Meijer)
- `context/segments/enterprise-use-cases.md` (8 priority use cases × sub-segment fit, for "What this means for MaiaEdge" angle on Enterprise stories)

### Core context (for "What this means for MaiaEdge" angle)
- `context/core/maiaedge-101.md` (PBC / Port Extender / PCE)
- `context/core/messaging-framework.md`
- `context/core/competitive-positioning.md`
- `context/copy-strategy/segment-language.md`

### Signal framework + per-segment Source Registries
- `context/signals/signal-framework.md` (Source Reliability + Validation Framework + cross-segment + I-series international)
- `context/signals/colocation-signals.md` "Sources for This Segment" (~22 sources + International)
- `context/signals/fiber-signals.md` "Sources for This Segment" (~26 sources + International)
- `context/signals/network-operator-signals.md` "Sources for This Segment" (~27 sources + International elevated)
- `context/signals/neocloud-signals.md` "Sources for This Segment" (~29 sources + International with sovereign AI)
- `context/signals/msp-aggregator-signals.md` "Sources for This Segment" (~25 sources)
- `context/signals/enterprise-signals.md` "Sources for This Segment" (~37 sources + International - added 2026-05-11 with Enterprise ICP promotion. SEC EDGAR 10-K + American Banker + Modern Healthcare + Becker's + Retail Dive + Nelson Hall + Everest Group; HHS OCR + NY DFS + PCI Council; Equinix / Megaport / PacketFabric customer pages)
- `context/signals/universal-platform-signals.md`

**Same comprehensive source registries as Weekly Signal Scan Phase 2.** ~160 sources total across reliability tiers (~125 prior + ~37 added with Enterprise catalog).

**Cross-check:** if a story already informed a signal in last Monday's signal-scan (check `weekly-reports/[last-monday]/cooper-run-report.md`), reference it as context but don't re-hash it as the lead story - point to broader trend coverage instead.

**Confidence + validation rules apply.** Even though no HubSpot writes, the on-thesis story-quality bar leverages signal-framework cross-source confirmation rules. Major M&A or anchor-tenant claim from a single Aspirational-tier source is suspect; require Robust-tier confirmation (SEC filing or major trade press) before surfacing.

---

## Preflight Checks (before Stage 1)

A. Verify Slack MCP connected. If not → write digest to `weekly-reports/YYYY-MM-DD/market-news/` anyway, commit, exit cleanly.

B. Verify `web_search` available. If not → log to run report, exit.

C. Verify today is Friday in America/New_York. If not → STOP with abort report.

D. Compute week window in ET:
- `window_end_et` = today at 06:00 ET (just before run kicks off, avoid pulling stories logged hours ago)
- `window_start_et` = window_end - 7 days

---

## Critical Invariants

### Timezone
America/New_York. "This week" = previous 7 calendar days ending at run start.

### Read-Only Routine
ZERO HubSpot writes. ZERO HubSpot reads either. Pure web scraping → Slack delivery.

### Content Rules
- NO em dashes in MaiaEdge-facing commentary (the "What this means for MaiaEdge" lines, intros, summaries). Verbatim quotes from articles can keep original punctuation.
- Category descriptor: "Carrier infrastructure" only in MaiaEdge angle lines. Never "IaaS / NaaS / platform" in your commentary.
- Competitor naming in MaiaEdge angle lines: factual names OK (Megaport, Equinix, Lumen, Zayo, PacketFabric). Genericize PRODUCT names: "Megaport Fabric" / "Equinix Fabric" → "third-party interconnection fabric." Headlines + direct article quotes stay verbatim.
- MSP segment label = "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).

### On-Thesis Filter
A story is **on-thesis** if it touches:
- **Colo:** new builds, expansions, M&A, exec hires (esp. interconnection / network engineering / sales), AI tenant wins, power/permitting, vacancy/pricing trends, sovereign-tenant deals, modular-DC moves, vertical-integration plays
- **Fiber:** BEAD awards (federal NTIA + state allocations), PE roll-ups, route lit announcements, ABS/refinancing, dark-fiber IRUs, AI-DC fiber wins, NaaS/portal launches, consortium/federation
- **Network Operator:** earnings (Tier 1/2 carrier transcripts and tone shifts), divestitures/spin-offs, automation maturity (CAMARA/Nephio/ONAP/Sylva commits, TM Forum AN scoring), SRv6 production, exec moves at CTO/CNO/CTrO/CDO, multi-domain RFPs
- **Neocloud:** funding rounds, GPU-backed debt, NVIDIA partnerships (Lepton/NCP/Exemplar), MLPerf submissions, capacity announcements, anchor tenant signings, colo lease 8-Ks, PeeringDB/IX changes, GPU price moves, sovereign AI grants
- **MSP / Aggregator:** TSD M&A and PE roll-ups, AI Practice launches, carrier line-card moves (added/dropped), CRO/VP SE hires at TSDs, ScanSource earnings disclosures, NaaS platform operator strategic announcements
- **Enterprise (Multi-DC ICP, 4 sub-segments - added 2026-05-11):** new corporate IT DC builds + DC expansions, M&A close at named ICP enterprise (Capital One/Discover, BMO/Bank of the West, CommonSpirit, UPMC, Concentrix/Webhelp, TP/Majorel, Cognizant/Astreya), Enterprise GenAI / GPU partnership announcements (JPMorgan IndexGPT, Walmart Sparky, Cognizant Neuro, Teleperformance Azure OpenAI), VP/Director Network Infrastructure exec hires at Tier 1/2 enterprises, regulatory enforcement events at named enterprises (NY DFS, HHS OCR breach disclosures, PCI v4.0 reactions, DORA CTPP designations), Equinix Fabric / Megaport / PacketFabric customer wins naming Enterprise sub-segment accounts

A story is **off-thesis (skip)** if it's:
- IT MSP / managed services consultancy news (we sell to telecom aggregators, not IT MSPs)
- Voice / SMS / A2P / CPaaS / cellular IoT MVNO / roaming hub / eSIM platform news
- Generic tech industry news with no carrier-infrastructure angle
- Press releases that are pure marketing fluff (no factual event)
- Already-old news re-circulated (verify date - don't surface anything older than 30 days)

### Story Quality Bar
For each story in the digest:
- Headline = ACTUAL article headline (or tight paraphrase). Don't fabricate.
- 2-line summary sourced from the article. Don't extrapolate beyond what the article says.
- MaiaEdge angle line MUST be inferential, not in the article. This is the value-add over the rep just reading Light Reading directly.
- Source URL mandatory. Drop the story if no working URL.

---

## Stage 1: Per-Segment News Scrape (6 parallel sub-stages, mirrors Weekly Signal Scan)

For each segment, read its catalog's "Sources for This Segment" section and apply web_search/web_fetch across that comprehensive source registry. **6 parallel sub-stages** (was 5 before Enterprise ICP promotion 2026-05-11), same pattern as Weekly Signal Scan, applied to news scraping instead of signal detection.

**Stage 1.A Colocation:** Source registry per `context/signals/colocation-signals.md` (~22 sources). Robust + Medium + Aspirational + International (EMEA / APAC / LATAM / MENA per Tim Z). Output: `colo_stories[]`.

**Stage 1.B Fiber:** Source registry per `context/signals/fiber-signals.md` (~26 sources). Output: `fiber_stories[]`.

**Stage 1.C NeoCloud:** Source registry per `context/signals/neocloud-signals.md` (~29 sources, broadest coverage). Output: `neocloud_stories[]`. Highest velocity.

**Stage 1.D Network Operator:** Source registry per `context/signals/network-operator-signals.md` (~27 sources, International elevated). Output: `network_op_stories[]`.

**Stage 1.E MSP / Aggregator:** Source registry per `context/signals/msp-aggregator-signals.md` (~25 sources). Output: `msp_stories[]`.

**Stage 1.F Enterprise (Multi-DC ICP - NEW 2026-05-11):** Source registry per `context/signals/enterprise-signals.md` (~37 sources). Vertical-specific trade press: American Banker (Financial Services), Modern Healthcare + Becker's (Healthcare Systems), Retail Dive + RIS News (Retail and Distribution), Nelson Hall + Everest Group (Outsourcing Services). Plus regulator portals (NY DFS, HHS OCR, PCI Council, DORA enforcement updates), SEC EDGAR 10-K + 8-K, hyperscaler customer-case-study pages, Equinix / Megaport customer-win pages. Apply Phase 0 awareness lens - Cooper-only delivery while Enterprise voice + sources validate over 2-4 runs. Output: `enterprise_stories[]`.

**Stage 1.G Aggregate:** Combine all 6 → `all_stories[]`. Dedup by `(canonical_url_hash, date)`. Per-segment story counts go in Cooper's audit DM. Flag any segment with <3 on-thesis stories as "thin coverage - investigate sources." (Enterprise sub-stage may run thin in early weeks - that's expected during Phase 0 source validation.)

### IT MSP Test (mandatory for MSP/Aggregator stories)
Per `context/segments/msp-aggregator.md` ICP Exclusion List. MSP/Aggregator means **telecom/network aggregators**, NOT IT MSPs.
- Carrier names mentioned (AT&T, Lumen, Comcast, Megaport)? → Telecom signal
- MPLS / WAN / SD-WAN / DIA listed? → Telecom signal
- Helpdesk / endpoint management / cybersecurity listed? → IT MSP signal - DROP
- "AI Practice" announcement at a helpdesk + cybersecurity MSP? → DROP per signal-framework False Positive Patterns

### Cross-source confirmation for major claims
For HIGH-stakes claims (M&A announcement OR close, anchor-tenant signing, BEAD subgrant award, exec hire at Tier A persona, GPU-backed debt facility, colo lease 8-K), require ≥2 independent sources before surfacing at "Highest priority" or "High" relevance ranking. Single trade-press story without SEC filing + counterparty confirmation gets surfaced at "Medium" tier or held for next week.

---

## Stage 2: Per-ICP Filtering

For each of the 5 ICPs, filter scraped stories down to on-thesis only. Drop everything else silently - don't mention dropped stories in the digest unless something interesting was filtered (in which case surface ONLY in Cooper's audit DM, never in the rep DMs).

---

## Stage 3: Per-ICP Ranking (top 3)

Rank on-thesis stories by strategic relevance to MaiaEdge:

1. **Highest priority:** stories matching an active signal code (greenfield S2/S3, BEAD award, AI tenant anchor, divestiture). Overlaps with what last Monday's signal-scan caught at the account level; surface here as "industry-wide context."
2. **High:** stories about specific named accounts in our CRM. Heuristic (no HubSpot access in this routine): well-known segment names - Equinix, Digital Realty, Brightspeed, altafiber, Lambda, Crusoe, Nebius, Megaport, Telarus, etc.
3. **Medium:** market dynamics that shape positioning even when no named account involved (GPU pricing moves, BEAD timeline updates, NVIDIA partnership tier changes, TSD consolidation trends).
4. **Low:** general industry color (skip unless nothing better in the ICP).

Pick top 3 per ICP. Fewer is fine - never pad with low-relevance content just to hit 3.

---

## Stage 4: Compose the Digest

Output structure:

```
:newspaper: *MaiaEdge Market News - Week of [YYYY-MM-DD to YYYY-MM-DD]*

Hey Cooper - here's what moved across our 5 ICPs this week.

*CROSS-ICP THEMES*
[2-3 bullets capturing the BIG meta-themes for the week. e.g., "Three colo M&A deals closed; PE roll-up tempo accelerating," "BEAD obligation deadlines triggered 4 state-level award announcements," "GPU pricing softened ~8% on H100 spot market." Cite specific stories below as evidence. This is the "if you only read 30 seconds" view.]

---

*COLOCATION*
:large_blue_circle: *[Headline]* (<[source URL]|source>)
[2-line summary pulled from the article - what happened, key numbers, who's involved.]
> *MaiaEdge angle:* [1 line - what this means for our positioning, our pipeline, or a specific value prop. Use segment-language vocabulary.]

:large_blue_circle: *[Headline]* (<[source URL]|source>)
[summary]
> *MaiaEdge angle:* [1 line]

[third story or skip]

---

*FIBER*
[same structure, top 3 stories]

---

*NETWORK OPERATOR*
[same structure, top 3 stories]

---

*NEOCLOUD*
[same structure, top 3 stories]

---

*MSP / AGGREGATOR*
[same structure, top 3 stories]

---

*ENTERPRISE (Multi-DC ICP)*
[same structure, top 3 stories. Use Enterprise sub-segment vocabulary from `context/segments/enterprise.md` Insider Language Bank when crafting MaiaEdge angles - match the sub-segment of the named enterprise (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services). Do NOT mix sub-segment vocabularies in a single angle line; mixing breaks the peer-recognition test.]

---

*EXEC MOVES THIS WEEK*
[Separately scannable. One line per move: Name, new title at Company (segment) | source. Buying-persona seniority only - VP Network / VP Engineering / CTO / CNO / CTrO / CDO / CRO / VP Sales for TSDs. Skip junior moves, skip lateral moves with no strategic implication. Omit section if none worth noting.]

---

Markdown copy: <[GitHub raw URL]|open>
```

### Length Budget
6 ICPs × 3 stories × ~80 chars/headline + ~200 chars/summary + ~120 chars/MaiaEdge angle = ~7,200 chars worst case (was 6,000 with 5 ICPs).

If digest exceeds 5,000 chars: split via threading.
- Parent message = Cross-ICP Themes + Colo + Fiber + Network Op
- Threaded reply (`thread_ts` = parent ts) = Neocloud + MSP/Aggregator + Enterprise + Exec Moves

Better to thread than truncate or drop "MaiaEdge angle" lines - the angle is the value-add.

### Voice
The digest should read like a sharp industry analyst on Cooper's team, not a press release roll-up. MaiaEdge angle lines specifically should sound like Cooper or Tim Z would phrase them - direct, opinionated, segment-aware. Avoid generic "this is interesting because" filler.

✓ "PE-backed colo roll-up fits the consolidation thesis - these acquired sites usually have a fabric-replacement window 6-12 months post-close."
✗ "This is an interesting development that could affect the colo market."

✓ "BEAD timeline tightening means F-A1 awards in Q3-Q4 - fiber operators with portal/NaaS gaps will be cutting purchase orders against this revenue."
✗ "BEAD continues to drive fiber investment."

---

## Stage 5: Output Delivery - Phase 0 Cooper-Only

**TWO Slack DMs to `U0A24D9RJLS`:**
1. **Digest DM** - the full market news content per Stage 4 (greeting "Hey Cooper")
2. **Audit DM** - separate message (same channel) with run stats + diagnostics

**DO NOT** send to Tim Lieto (`U0A973L1HFF`) or Ken (`U0AE1PGCB6C`). Rep-direct routing deferred until Cooper approves after 2-4 clean runs.

### Cooper Audit DM body - Critical Info Only

**Subject:** `:newspaper: *Market News Audit - Week of [YYYY-MM-DD to YYYY-MM-DD]*`

**Body - keep under 1,500 chars:**
```
*Run summary:* [N] stories scanned · [M] surfaced · [K] dropped (top reasons: off-thesis IT MSP / off-thesis voice / duplicate of last Monday's signal-scan / fluff PR) · sources hit: [count] · sources errored: [count]

*Per-segment story counts (flag any <3 as thin coverage):*
- Colo [N/M] [thin?]
- Fiber [N/M] [thin?]
- NetworkOp [N/M] [thin?]
- NeoCloud [N/M] [thin?]
- MSP [N/M] [thin?]
- Enterprise [N/M] [thin? - expected during Phase 0 source validation; thin coverage is OK for first 2-4 runs]

*Cross-routine cross-reference:* [N] stories overlap with last Monday's signal-scan - see thread

*Notable filtered-out stories:* [1-3 stories Cooper might want to know about even though they didn't make the digest. Skip if nothing worth surfacing.]

*Run health:* [GREEN / YELLOW / RED]
- GREEN: all 5 sub-stages ran, ≤3 source errors, ≥3 stories per segment, voice-quality bar met
- YELLOW: 1+ thin-coverage segment OR 4-10 source errors OR cross-source confirmation failures on major claims
- RED: aborted, runtime budget exceeded, or systemic source failures

*Errors:* [None | description]
*Markdown:* [GitHub raw URL to digest.md]
```

**Threaded replies (mandatory if relevant):**
1. Source coverage attempted - full per-source list with status
2. Sources that returned 0 hits / errors / repeated failures (3+ weeks running flagged for source-development review)
3. Cross-routine cross-reference details (which stories appeared in last Monday's signal-scan)
4. Recipient delivery status (digest DM, audit DM, reps not delivered Phase 0)

---

## Markdown Audit File

Write to `weekly-reports/YYYY-MM-DD/market-news/`:
- `digest.md` - full digest body (same content as the Cooper digest DM)
- `cooper-audit.md` - Cooper's audit DM body
- `sources-scanned.md` - list of every URL fetched this run with timestamp + HTTP status (diagnostic)

ATX-style headings. NO em dashes.

---

## Commit + Post

1. **Commit** to `main`: `market news YYYY-MM-DD - [N] stories surfaced across [M] ICPs`. If date directory exists from another routine, write into `market-news/` subfolder.

2. **Post Slack DMs** via `slack_send_message` (Phase 0 - TWO messages total):
   - Cooper digest DM → `U0A24D9RJLS` (the market news content)
   - Cooper audit DM → `U0A24D9RJLS` (separate message - diagnostics + per-segment counts + delivery status)
   - **DO NOT** send to Tim Lieto (`U0A973L1HFF`) or Ken (`U0AE1PGCB6C`).

3. **GitHub raw URL** in each DM: `https://raw.githubusercontent.com/cooperfkennedy/maiaedge-ai/main/weekly-reports/YYYY-MM-DD/market-news/digest.md`.

---

## Cross-routine ledger

- **At run start:** read canvas `F0B0AFSB9LN` for prior context (no Tier 3 holds expected - this routine is read-only awareness - but reading keeps the run-log consistent).
- **At run end:** weekly-market-news produces no Tier 3 work items. Append ONE row to "Run log":
  `| YYYY-MM-DD | Weekly Market News | <status emoji> | <one-sentence summary> | <artifact links> |`
  Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped.

---

## Failure Modes

- Per-source try/except on every web_search + web_fetch. Log in audit Errors section, do NOT abort. Flaky source shouldn't kill the digest.
- Rate limit on web_search/web_fetch: pause 30s, retry once. After second failure on same source → skip + log.
- Slack send failure: retry once with 2s backoff. Persistent → log in audit "Recipient delivery status," continue.
- Empty week (no on-thesis stories across all 6 ICPs): unlikely but possible (holidays). Send short DM: `:newspaper: *MaiaEdge Market News - Week of [dates]* - Quiet week across our ICPs. No stories cleared the on-thesis bar. Back next Friday.` No padding. Cooper audit still runs with full source-scan stats so we can verify the routine actually worked vs. silently failed.

---

## Final Checklist

- [ ] Today is Friday in America/New_York
- [ ] All 6 ICPs evaluated; top 3 per ICP picked (or fewer if quality didn't justify 3) - Enterprise can run thin during Phase 0
- [ ] Every story has working source URL, 2-line article-grounded summary, non-generic MaiaEdge angle
- [ ] Cross-ICP Themes captures 2-3 meta-themes with specific story citations as evidence
- [ ] Exec Moves limited to buying-persona seniority hires (skip junior / lateral with no strategic implication)
- [ ] No em dashes in MaiaEdge-facing commentary
- [ ] No competitor product names in MaiaEdge angle lines (genericized); article headlines + quotes preserve original wording
- [ ] MSP shown as "MSP / Aggregator"
- [ ] Markdown audit committed to `weekly-reports/YYYY-MM-DD/market-news/`
- [ ] Slack DMs posted: Cooper-only - 2 messages (digest + audit). NOT sent to Tim Lieto / Ken (Phase 0)
- [ ] Cooper digest DM contains GitHub raw URL for digest markdown
- [ ] Cooper audit captures per-segment story counts, source coverage, drop reasons, cross-routine cross-reference vs. last Monday's signal-scan, delivery status
- [ ] All 6 Stage 1 sub-stages ran using per-segment Source Registries from each catalog (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise)
- [ ] IT MSP Test applied to MSP/Aggregator stories (helpdesk + cybersecurity dropped)
- [ ] Cross-source confirmation rule applied to major M&A / anchor-tenant / BEAD / exec-hire / GPU-debt / colo-lease claims (≥2 independent sources for HIGH/Highest priority)
