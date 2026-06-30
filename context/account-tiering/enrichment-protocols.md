# Enrichment Protocols (D5 v2 - Operational Layer)

**Status:** Canonical. Effective 2026-05-14 (Phase 3). All per-sub-segment protocols (N1-N5, F1-F6, C1-C4, NC1-NC5, M1-M5, E1-E4, G  -  **30 protocols total, one per sub-segment**) are inlined in §6 below. NC1 vs NC3 vs NC2 deterministic threshold matrix is in §6a. Greenfield migration patterns + D7 fallback are in §7. The bot is now self-contained  -  no external D5 working file dependency.
**Companion:** `context/account-tiering/tier-compute-spec.md` (tier computation), `context/account-tiering/sub-segment-qualification.md` (pointer to file 06).

This file is the operational layer for the enrichment skill. Every classification decision the bot makes flows through these protocols. The principle Cooper laid down 2026-05-14:

> "I want the CRM to manage and enrich itself over time. The last thing I want is a bunch of accounts funneling into manual review, creating a bunch of tedious qualification work for me. That's your job."

## 1. Operating principle - best-fit classification, NOT default-manual-review

The bias is toward CLASSIFICATION + calibrated confidence. Manual_review_required is the LAST resort, not a default.

### Decision hierarchy (in order)

1. **Disqualified by D1** -> `customer_segment = "Other"` (useful as competitive/partner reference) OR `customer_segment = "Flagged for deletion"` (no value).
2. **Matches all required questions for ONE sub-segment** -> classify with `high_90` confidence.
3. **Matches most required questions for ONE sub-segment** -> classify with `medium_7089` confidence.
4. **Matches some required questions for ONE sub-segment** -> classify with `low_5069` confidence (R2 + D7 will re-validate).
5. **Clear positive evidence for 2+ sub-segments (multi-classification)** -> apply the TIEBREAKER rule (defined per pair in file 06 §6 + §11). Only `manual_review_required` if tiebreaker truly cannot resolve.
6. **No positive evidence for any ICP sub-segment** -> `customer_segment = "Flagged for deletion"` (NOT "Other" - Other is reserved for D1 disqualifier matches that are useful references).

**Target:** manual_review_required population <5% of total per run. If exceeded, the protocols have bugs - alert Cooper.

### Mandatory companion write: `flagged_for_deletion_reason`

Whenever a decision above resolves to `customer_segment = "Flagged for deletion"`, you MUST in the SAME HubSpot update also set `flagged_for_deletion_reason` (multi-line text, Company object). This is the audit companion that lets Cooper filter the deletion pool by reason and bulk-delete with confidence.

Lead the value with ONE of the 7 canonical reason codes, then a colon and one concrete sentence of evidence. The scannable code lives here; the 2-4 sentence prose rationale stays in `account_brief`. No em dashes in the reason string - use a colon.

| Reason code | When it applies |
|---|---|
| `Dead domain` | DNS NXDOMAIN / parked / for-sale / persistent destination 4xx-5xx (NOT a proxy block). |
| `Hard junk / non-business` | Non-business or hard-flag category (restaurant, church, school, personal site), junk TLD, spoofed-brand or test record. |
| `D1 disqualified (no reference value)` | Matched a D1 global disqualifier with NO competitive/partner reference value. (If it carries reference value, route to `Other`, not Flagged.) |
| `No ICP fit` | Researched but no positive evidence for any of the 6 ICP sub-segments, and not a partner/competitor reference. |
| `Duplicate (merged)` | Duplicate of an existing record; contacts reassociated to the primary (cite primary name + record ID). |
| `Defunct / out of business` | Confirmed defunct / ceased operations / absorbed post-acquisition (cite the event). |
| `Stalled greenfield` | Greenfield record, no construction progress or relevant signal in 18+ months; web-verified stalled. |

Example: `No ICP fit: regional IT staffing firm; no infrastructure ownership and no positive evidence for any ICP sub-segment.`

**Clear-on-exit:** if a previously-flagged record is reclassified into any active segment (R2/D7 upgrade, un-flag), clear `flagged_for_deletion_reason` to empty in the same write. The field is conditional on the flag and must never be left stale on an active record. Full spec: `context/hubspot/property-schema.md` §2.1.

### Manual review is the LAST resort

A record gets `segmentation_confidence = manual_review_required` ONLY when:
- Two or more sub-segments have >=3 matching required questions each AND no tiebreaker rule applies, OR
- Critical evidence is contradictory (e.g., website says "wholesale-only" but customer logos include consumer retail brands), OR
- The record straddles two CUSTOMER_SEGMENTS (e.g., a colo + neocloud hybrid where revenue split is 50/50).

These records flow to D7 weekly edge-case-resolution routine. **Hard rule:** nothing in manual_review_required survives more than 14 days.

## 2. The 6 silent-failure modes + enforcement rules

| # | Failure mode | Enforcement rule |
|---|---|---|
| 1 | Record gets `customer_segment` but no `company_sub_segment` | Every ICP-classified record MUST have `company_sub_segment` populated. Best-fit logic picks closest match based on positive evidence. If NO positive evidence for any sub-segment -> flag the record `customer_segment = "Flagged for deletion"` with reasoning. ONLY use `manual_review_required` if clear evidence for 2+ sub-segments conflicts. |
| 2 | Framework default (Regional CLEC / Standard - colo / Telecom Aggregator) written without evidence | Protocols require positive-evidence questions specific to the default. If positive evidence fails, the record either gets classified into a more-specific sub-segment OR routed to `Flagged for deletion`. Never write a framework default as "I couldn't think of anything else." |
| 3 | Record matches multiple sub-segments without flagging | Tiebreaker rules defined per sub-segment (primary revenue line, dominant infrastructure marker, parent legal identity). Apply tiebreaker; only `manual_review_required` if tiebreaker truly fails. |
| 4 | Confidence written without evidence support | Deterministic thresholds per protocol. high_90 requires named anchor match OR all required questions confirmed. Confidence cannot be auto-inflated. |
| 5 | D1 disqualifier missed; non-ICP record gets ICP classified | D1 runs as Stage 1a (cheap pre-check) AND Stage 1c (after research surfaces structural signals) BEFORE any segment routing. Mandatory audit-log entry confirms D1 check ran. |
| 6 | Data drift over time | Quarterly anchor refresh + R2 120-day re-enrichment + R-Tier-Audit weekly + D7 edge-case-resolution weekly. |

## 3. The 8 enriched fields the bot populates (read these, NOT HubSpot defaults)

Classification reads from these 8 fields, NOT from HubSpot `description` / `industry` (last-resort only). Per Cooper 2026-05-14: populate enriched fields BEFORE classification. Classification (customer_segment + company_sub_segment + segmentation_confidence + account_tier) is the VERDICT made on the completed enriched profile.

**Conciseness rule (Cooper 2026-05-14):** All narrative fields capped at **2-4 sentences each**. At thousands-of-records scale, brevity beats completeness.

**`maiaedge_value_proposition` is OUT OF ENRICHMENT SCOPE** - populated by outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) on-demand at outreach time. The field exists in HubSpot but the enrichment bot leaves it alone.

| # | Field | Type | Description | Length cap |
|---|---|---|---|---|
| 1 | `account_brief` | string | Company overview - what they do, who they serve, notable context. Primary narrative source for classification. Excludes geography. | **2-4 sentences** |
| 2 | `geographic_focus` | string | Natural language scope (e.g., "HQ: Washington \| Scope: Global \| 4 states"). | **1-2 sentences / 1 line** |
| 3 | `infrastructure_profile` | enum (multi-select) | Bands for Facilities / Route Miles / POPs or "None Identified". **PRIMARY structured signal** (§4 canonical patterns). | Enum |
| 4 | `hyperscaler_proximity` | enum (single-select) | "Announced: <50 miles" / "Announced: 50-200 miles" / "Existing Facility Nearby" / "None Known". Primarily a Colocation signal. | Enum |
| 5 | `fabric_provisioning_approach` | enum (multi-select) | 11 options. Detects Network Op Track A (Homegrown) vs Track B (Manual/Legacy) + competitor adoption. | Enum |
| 6 | `provisioning_landscape` | string | Narrative on fabric / provisioning context. | **2-4 sentences** |
| 7 | `recent_news_or_trigger_event` | string | Most recent news / funding / leadership / signal. **Pure narrative, NO date prefix** (post-2026-05-28; the legacy `[YYYY-MM-DD]` prefix was retired — event date lives in `last_signal_date`). | **2-4 sentences** |
| 8 | `last_enriched_date` | date | Stamps only on a passing definitive gate (see Unified Stamping Policy in CLAUDE.md). | Date |

## 4. Multi-marker classification via `infrastructure_profile`

`infrastructure_profile` is the structured, multi-dimensional classification signal. Each sub-segment has a CANONICAL pattern. The bot uses both directions:
- **At classification:** match infrastructure_profile values against the canonical pattern -> confidence signal.
- **At enrichment:** infer the right infrastructure_profile values from research -> write to record.

### Canonical infrastructure_profile patterns per sub-segment

| Sub-segment | Canonical `infrastructure_profile` pattern |
|---|---|
| `Tier 1 Carrier - Network Op` | Facilities: Enterprise + Route Miles: Enterprise + POPs: Enterprise |
| `Pure Wholesale Carrier - Network Op` | Route Miles: Large/Enterprise + POPs: Large/Enterprise + Facilities: Mid-Size/Large |
| `Cable MSO Enterprise Division - Network Op` | Facilities: Large/Enterprise + Route Miles: Mid-Size/Large + POPs: Large |
| `International Backbone Specialist - Network Op` | Route Miles: Enterprise + POPs: Large/Enterprise + Facilities: Small/Mid-Size |
| `Subsea cable operator` | Route Miles: Enterprise (cable mileage) + POPs: Mid-Size/Large + Facilities: Small (landings only) |
| `Tier 2 National Wholesale - Fiber operator` | Route Miles: Enterprise + POPs: Large/Enterprise + Facilities: Small/Mid-Size |
| `Long Haul / Backbone - Fiber operator` | Route Miles: Enterprise + POPs: Mid-Size/Large + Facilities: Small/Mid-Size |
| `Dark Fiber Specialist - Fiber Operator` | Route Miles: Large/Enterprise + POPs: Small/Mid-Size + Facilities: Small |
| `Regional CLEC - Fiber operator` | Route Miles: Mid-Size/Large + POPs: Small/Mid-Size + Facilities: Small/Mid-Size |
| `Regional Cable Operator - Fiber operator` | Route Miles: Mid-Size/Large + POPs: Small/Mid-Size + Facilities: Mid-Size/Large |
| `Municipal / Cooperative - Fiber operator` | Route Miles: Small/Mid-Size/Large + POPs: Small/Mid-Size + Facilities: Small/Mid-Size |
| `Standard - colo` | Facilities: Mid-Size/Large/Enterprise + Route Miles: None Identified or Small + POPs: Small/Mid-Size |
| `AI Signals - colo` | Facilities: Small/Mid-Size + Route Miles: None Identified + POPs: Small |
| `Modular - colo` | Facilities: Mid-Size/Large (site count, not campus) + Route Miles: None Identified + POPs: Small |
| `Hyperscale Wholesale - colo` | Facilities: Mid-Size/Large + Route Miles: None Identified + POPs: Small (few hyperscaler anchor tenants) |
| `Large Scale GPU - Neocloud` | Facilities: Mid-Size/Large + Route Miles: None Identified + POPs: Small/Mid-Size |
| `Tier 1 Inference - Neocloud` | Facilities: Small (carrier hotels) + Route Miles: None Identified + POPs: Mid-Size/Large (distributed inference) |
| `AI Infrastructure providers - Neocloud` | Facilities: Small/Mid-Size + Route Miles: None Identified + POPs: Small/Mid-Size |
| `Sovereign AI Clouds - Neocloud` | Facilities: Small/Mid-Size + Route Miles: None Identified + POPs: Small |
| `Crypto to AI - Neoclouds` | Facilities: Mid-Size/Large + Route Miles: None Identified + POPs: Small |
| `Telecom Aggregator - MSP` / `Managed Network Services - MSP` / `TSD Technology Services Distributor - MSP` / `Master Agent - MSP` / `Cloud + Telecom Hybrid MSP - MSP` | None Identified across all 3 dimensions (MSPs don't OWN infrastructure) |
| `Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Retail and Distribution - Enterprise` / `Outsourcing Services - Enterprise` | Facilities: Mid-Size/Large (data centers / hospitals / DCs / delivery centers) + Route Miles: None Identified + POPs: None Identified |
| `Greenfield` (cross-segment) | Facilities: Small (1-4 sites under construction) + Route Miles: None Identified + POPs: None Identified or Small |

### Tiebreaker when revenue conflicts with infrastructure_profile

**`infrastructure_profile` wins.** Revenue data is dirty more often than infrastructure_profile. Example: NaviSite shows $211.9B revenue (Phase 2 audit confirmed copy/paste error from Spectrum) but `infrastructure_profile` shows None Identified / Facilities Small -> classify as MSP/Aggregator (Cloud + Telecom Hybrid likely), NOT as Tier 1 Carrier. Don't trust dirty revenue.

### Confidence implication

- Anchor company match (named in file 06 §6 anchor list) + infrastructure_profile matches canonical pattern -> `high_90` baseline
- Infrastructure_profile matches canonical pattern + 3+ protocol questions confirmed -> `high_90`
- Infrastructure_profile partially matches (2 of 3 dimensions) + 2+ protocol questions confirmed -> `medium_7089`
- Infrastructure_profile mismatches OR is None Identified across dimensions that should have signals -> `low_5069` + reasoning "Infrastructure profile incomplete; classification based on narrative evidence"

## 4.5 Additional structured signals - `hyperscaler_proximity` + `fabric_provisioning_approach`

### `hyperscaler_proximity` (single-select)

| Value | Classification signal |
|---|---|
| `Announced: <50 miles` | Colocation Greenfield + announced hyperscaler proximity -> likely future Hyperscale Wholesale; AI Signals Colo if GPU tenant focus already announced |
| `Announced: 50-200 miles` | Medium-proximity colocation build - relevant for Modular - colo (edge pods near hyperscaler regions) or Hyperscale Wholesale |
| `Existing Facility Nearby` | Operational colo with hyperscaler adjacency - strong AI Signals - colo OR Hyperscale Wholesale signal |
| `None Known` | Colocation without hyperscaler proximity -> Standard - colo or Modular - colo (edge-focus); or non-colo segment entirely |

Cross-segment usage: meaningful only for Colocation + Greenfield. For Fiber Op / Network Op / NeoCloud / MSP / Enterprise this field is typically `None Known`.

### `fabric_provisioning_approach` (multi-select)

| Value | Classification signal |
|---|---|
| `homegrownproprietary_platform` | Sophisticated operator with internal automation. **Network Op Track A signal** (lead with cross-carrier extension). Common for Tier 1 Carrier, mature Fiber operators. |
| `standard_ossbss_stack` | Standard automation maturity. Doesn't distinguish Track A vs B by itself. |
| `manuallegacy_processes` | **Network Op Track B signal** (lead with internal unification first). Often seen in Regional CLECs, regional cable, Municipal / Cooperative. |
| `megaport` / `packetfabric` / `equinix_ecx_fabric` / `console_connect` / `other_external_naas` | Operator currently uses external NaaS competitor. Probably a smaller operator that hasn't built their own fabric. Competitive intelligence - MaiaEdge positioning is "you own the fabric, not them." |
| `lumen_private_connectivity_fabric` | Has adopted Lumen PCF (key competitive challenge). Classification signal: large operator with capex for proprietary buildout (Tier 1 Carrier ambition) OR large customer of Lumen. |
| `other_competitor_fabric` | Adopted some other competitor solution. Probe in research. |
| `none_identified` | Either pre-enrichment OR genuinely no fabric/provisioning strategy visible. If pre-enrichment, rerun research. |

If actual `fabric_provisioning_approach` diverges from the expected pattern for the sub-segment (e.g., a record classified as Tier 1 Carrier with `Manual/Legacy Processes` - unusual), downgrade confidence by one notch and route to D7 for review.

## 5. The 5-stage research-first workflow

Per Cooper 2026-05-14: populate enriched fields FIRST during research, THEN classify as the VERDICT on the completed profile.

```
Stage 0: Identity resolution
  - Verify domain valid + record name matches a real entity
  - Resolve parent-vs-subsidiary per D2 wholesale-arm policy
  - If domain dead / record is a duplicate -> Flagged for deletion

Stage 1a: D1 quick check (cheap - runs BEFORE expensive deep research)
  - Match domain against hyperscaler / equipment vendor / government domain patterns
  - Check website primary navigation for hardware SKUs (equipment vendor signal)
  - MATCH -> customer_segment = "Other" (useful reference) or "Flagged for deletion"
     (skip deep research; eviction confirmed)
  - NO MATCH -> continue

Stage 1b: DEEP RESEARCH - populate 7 enriched fields (CONCISELY, 2-4 sentences each)
  1. account_brief (2-4 sentence business overview)
  2. geographic_focus (1-2 sentence scope description)
  3. infrastructure_profile (multi-select bands - Facilities + Route Miles + POPs)
  4. hyperscaler_proximity (enum - colocation-specific signal)
  5. fabric_provisioning_approach (multi-select - competitor adoption + Track A/B)
  6. provisioning_landscape (2-4 sentence narrative)
  7. recent_news_or_trigger_event (2-4 sentences, pure narrative — NO date prefix; event date lives in last_signal_date)
  - NOT populated here: maiaedge_value_proposition (outreach-time concern)
  - last_enriched_date stamps at Stage 5 only on a definitive gate pass

Stage 1c: D1 deep check (runs AFTER research surfaces structural signals)
  - Catch disqualifiers not visible at Stage 1a: defunct entity, post-acquisition brand,
    OTT-only platform, IoT/eSIM platform, logistics misclassification, etc.
  - MATCH -> customer_segment = "Other" or "Flagged for deletion"
  - NO MATCH -> continue

Stage 2: Segment routing
  - Read enriched fields -> determine which of 6 ICPs the record fits
  - Apply pre-gates from D3 flowchart for inferred segment
  - FAIL pre-gate AND no other segment fits -> customer_segment = "Flagged for deletion"
  - PASS pre-gate -> enter sub-segment protocol

Stage 3: D3 flowchart traversal + sub-segment classification
  - Walk the D3 decision tree for the segment (file 06 §5)
  - At leaf node: enter the per-sub-segment enrichment protocol (§6 below)
  - Run protocol questions reading from the 7 enriched fields populated in Stage 1b
  - Apply confidence thresholds based on question-count + infrastructure_profile pattern match
  - Best-fit selection: if no perfect match, pick closest sub-segment based on positive evidence
  - Tiebreaker if 2+ sub-segments match (defined per pair, file 06 §6)
  - Output: (sub_segment_value, confidence_level, reasoning_string)

Stage 4: Tier computation
  - Per context/account-tiering/tier-compute-spec.md
  - Read (customer_segment, company_sub_segment) -> defaults table
  - Apply signal modifiers (hot/white-hot/stacked/open deal/stale/sustained quiet)
  - Clamp to ceiling/floor
  - Honor hs_is_target_account = true (skip tier write; segment/sub-segment still write)

Stage 5: HubSpot write + audit (FINAL STAGE - no Stage 6 value_prop generation)
  - Write 7 enriched fields (or update if newer/better than existing); all narrative
    fields capped at 2-4 sentences per §3 conciseness rule
  - Write customer_segment + company_sub_segment + segmentation_confidence
  - Write account_tier (per compute_tier output; skip if hs_is_target_account = true)
  - Write last_enriched_date (only on a passing definitive gate per CLAUDE.md
    Unified Stamping Policy)
  - Write HubSpot note with full reasoning string citing D1/D2/D3/D5 rule references
    + enriched-field evidence summary
  - DO NOT write maiaedge_value_proposition (outreach skills handle this at outreach time)
```

**Why this order matters:** classification quality depends on the completeness of enriched fields. If the bot tries to classify Ziply Fiber based only on the HubSpot description ("fast and reliable fiber internet services"), it would miss the 2,100-mile Northern Link Route announcement (recent_news) and the Bell Canada subsidiary status (account_brief) - both critical classification signals. The 8-field profile gives the classifier the complete picture before deciding.

**Fall-through enforcement at Stage 3:** if no sub-segment yields positive evidence:
- Re-check segment assignment (Stage 2) - maybe the record was misrouted.
- If segment is correct but no sub-segment fits -> `customer_segment = "Flagged for deletion"` with explicit reasoning "No sub-segment evidence in <segment>; not an ICP fit."
- Only fall to manual_review_required if multiple sub-segments have meaningful positive evidence AND tiebreaker fails.

## 6. Per-sub-segment protocols (full questions inlined from D5 v2)

Each protocol contains 5 positive-evidence questions read against the 8 enriched fields (Stage 1b). The bot answers each question against the populated fields, then applies confidence thresholds and tiebreakers below.

### Network Operator(Tier 1 / VNO)  -  5 protocols (N1-N5)

#### Protocol N1  -  `Tier 1 Carrier - Network Op`

| Q | Question | Source field | Weight |
|---|---|---|---|
| N1.1 | Does `account_brief` describe a state-protected former incumbent OR post-Bell System national carrier? | `account_brief` | Required for high_90 |
| N1.2 | Does `infrastructure_profile` show Facilities Enterprise + Route Miles Enterprise + POPs Enterprise (or any 2 of 3 at Enterprise)? | `infrastructure_profile` | Required for high_90 |
| N1.3 | Does `account_brief` mention multi-segment activity (retail + enterprise + wholesale + (often) international)? | `account_brief` | Required |
| N1.4 | Subsea cable ownership or co-ownership mentioned in `account_brief` or `recent_news_or_trigger_event`? | `account_brief`, `recent_news_or_trigger_event` | Strong marker (high_90) |
| N1.5 | Multinational reach: wholesale or enterprise in >=10 countries per `account_brief`? | `account_brief` | Strong marker |

**Tiebreaker** (vs N2 Pure Wholesale Carrier / N4 International Backbone Specialist):
- Retail consumer presence mentioned in `account_brief` -> Tier 1 Carrier wins
- Pure-wholesale model (no consumer/retail) -> Pure Wholesale Carrier
- International-only (no domestic retail) -> International Backbone Specialist

**Best-fit thresholds:**
- `high_90`: anchor match (AT&T, Verizon, Deutsche Telekom, NTT, Orange, KDDI, BT, Telstra, China Telecom/Mobile/Unicom, Singtel, Vodafone, América Móvil) OR N1.1 + N1.2 + N1.3 + N1.4
- `medium_7089`: 3 of 5 confirmed; clear Tier 1 archetype
- `low_5069`: 2 of 5 confirmed; revenue confirms but infrastructure_profile is incomplete
- `Flagged for deletion`: <=1 of 5 AND doesn't fit any other sub-segment

#### Protocol N2  -  `Pure Wholesale Carrier - Network Op`

| Q | Question | Source | Weight |
|---|---|---|---|
| N2.1 | Is the business 100% B2B (no consumer retail mentioned in `account_brief`)? | `account_brief` | Required |
| N2.2 | Does `account_brief` OR `recent_news` mention "Tier 1 IP transit" or BGP-based routing? | `account_brief`, `recent_news_or_trigger_event` | Strong marker |
| N2.3 | `infrastructure_profile` shows Route Miles Large/Enterprise + POPs Large/Enterprise? | `infrastructure_profile` | Required |
| N2.4 | Wholesale customer base mentioned in `account_brief` (other carriers, hyperscalers, large enterprises)? | `account_brief` | Required |
| N2.5 | Multi-country footprint OR regional density at hub metros? | `account_brief` | Strong marker |

**Tiebreaker:** If subsea ownership AND international focus dominant -> International Backbone Specialist wins (more specific).

**Best-fit thresholds:**
- `high_90`: anchor (Cogent, Arelion, EXA Infrastructure, Hurricane Electric, Sparkle) OR N2.1 + N2.3 + N2.4
- `medium_7089`: 3 of 5
- `low_5069`: 2 of 5 (e.g., revenue band met but no detailed B2B-only confirmation)
- `manual_review_required`: ONLY if `account_brief` clearly shows BOTH retail + pure-wholesale activity (Lumen post-divestitures pattern)

**Anchor verification 2026-05-14:** Liberty Networks REMOVED from N2 anchor list. Web verification confirms Liberty Networks (Liberty Latin America subsidiary) operates ~60,000 km of submarine + terrestrial fiber across 30+ countries in Latin America / Caribbean, with significant subsea ownership (MAYA-1.2 launched H1 2026). Per N2 tiebreaker ("subsea ownership AND international focus dominant -> International Backbone Specialist wins"), Liberty Networks correctly routes to **N4 International Backbone Specialist - Network Op**, not N2. Existing HubSpot Liberty Networks records should be re-classified at next R2 cycle.

#### Protocol N3  -  `Cable MSO Enterprise Division - Network Op`

| Q | Question | Source | Weight |
|---|---|---|---|
| N3.1 | Does `account_brief` mention parent is a cable / HFC legacy operator (Comcast / Charter / Cox / Altice pattern)? | `account_brief` | Required (gate) |
| N3.2 | Does `account_brief` OR record name reflect a distinct B2B brand (Comcast Business / Spectrum Enterprise / Cox Business pattern)? | `account_brief`, record name | Required |
| N3.3 | `infrastructure_profile` shows Facilities Large/Enterprise + Route Miles Mid-Size/Large + POPs Large? | `infrastructure_profile` | Required for high_90 |
| N3.4 | Parent residential cable in >=10 US states OR national per `account_brief`? | `account_brief` | Required |
| N3.5 | Sells fiber + Ethernet + MPLS + SD-WAN to mid-market and enterprise per `account_brief`? | `account_brief` | Strong marker |

**Tiebreaker** (vs F5 Regional Cable Operator - Fiber operator):
- Parent is NATIONAL cable AND distinct B2B brand exists AND B2B revenue >=$1.5B -> Cable MSO Network Op
- Parent is REGIONAL multi-state cable AND no separate B2B brand -> Regional Cable Operator Fiber

**Best-fit thresholds:**
- `high_90`: anchor (Comcast Business, Spectrum Enterprise, Cox Business, Optimum Business) OR N3.1 + N3.2 + N3.4
- `medium_7089`: 3 of 5
- `low_5069`: 2 of 5 (regional cable but B2B revenue unclear)

#### Protocol N4  -  `International Backbone Specialist - Network Op`

| Q | Question | Source | Weight |
|---|---|---|---|
| N4.1 | `account_brief` says HQ outside US AND markets primarily as international connectivity? | `account_brief`, `country` | Required for high_90 |
| N4.2 | Subsea cable ownership OR IRU positions on >=3 cable systems per `account_brief` or `recent_news`? | `account_brief`, `recent_news_or_trigger_event` | Required for high_90 |
| N4.3 | `infrastructure_profile` shows Route Miles Enterprise + POPs Large/Enterprise + Facilities Small/Mid-Size? | `infrastructure_profile` | Strong marker |
| N4.4 | 60-80%+ international cross-border revenue mentioned? | `account_brief` | Strong marker |
| N4.5 | Tier 1 IP transit with global routing presence? | `account_brief` | Strong marker |

**Tiebreaker** (vs N5 Subsea cable operator + N2 Pure Wholesale Carrier):
- Subsea ownership is THE primary business + no terrestrial backbone -> Subsea cable operator (more specific)
- Subsea ownership + significant terrestrial backbone + international wholesale -> International Backbone Specialist
- No subsea ownership but international wholesale -> Pure Wholesale Carrier with international flag

**Best-fit thresholds:**
- `high_90`: anchor (Tata Communications, PCCW Global, Telstra International, HGC Global, Epsilon, Console Connect, Bharti Airtel International, EXA Infrastructure, Sparkle) + N4.1 + N4.2
- `medium_7089`: 3 of 5
- `low_5069`: 2 of 5

#### Protocol N5  -  `Subsea cable operator` (NEW 2026-05-14)

**Definition:** Pure-play subsea cable operators whose primary business is owning, operating, or selling capacity on submarine fiber cables. NO terrestrial backbone OR terrestrial backbone is incidental.

**Quantitative markers:**
- Owns >=1 named subsea cable system (verifiable via TeleGeography Submarine Cable Map)
- Revenue range typically $20M-$500M (smaller than full International Backbone Specialists)
- Few or no terrestrial PoPs; landing stations only
- Customer base: hyperscalers, content providers, regional carriers buying capacity
- Often consortium-affiliated or hyperscaler-SPV-affiliated

| Q | Question | Source | Weight |
|---|---|---|---|
| N5.1 | Does `account_brief` explicitly describe a subsea cable operator OR submarine cable company? | `account_brief` | Required (gate) |
| N5.2 | Does the company own or co-own >=1 named cable system (verifiable via TeleGeography)? | `account_brief`, `recent_news_or_trigger_event`, web research | Required (gate) |
| N5.3 | `infrastructure_profile` shows Route Miles Enterprise (submarine cable mileage) + POPs Small/Mid-Size + Facilities Small (cable landings only)? | `infrastructure_profile` | Strong marker |
| N5.4 | Does `account_brief` describe minimal or no terrestrial backbone? | `account_brief` | Required (negative check vs N4) |
| N5.5 | Customer base described as hyperscalers / content providers / regional carriers buying capacity (not enterprise direct)? | `account_brief` | Strong marker |

**Tiebreaker** (vs N4 International Backbone Specialist):
- Subsea PRIMARY + minimal terrestrial -> Subsea cable operator
- Subsea + significant terrestrial + international wholesale -> International Backbone Specialist
- Pure consortium with no operating entity (FLAG, SEA-ME-WE, ACE, EIG) -> D1.4 disqualifier (not a sellable entity)

**Customer_segment parent:** `Network Operator(Tier 1 / VNO)`  -  Subsea cable operators are a network sub-archetype, not their own customer_segment.

**Best-fit thresholds:**
- `high_90`: anchor match OR N5.1 + N5.2 + N5.4  -  subsea ownership is the defining trait
- `medium_7089`: 3 of 5 confirmed (subsea ownership confirmed but tenant mix unclear)
- `low_5069`: 2 of 5 (subsea ownership confirmed but rest of profile is thin)
- `Flagged for deletion`: hyperscaler-owned subsea SPV with no commercial sales motion (pure infrastructure financing vehicle)

**Anchor companies** (verified via TeleGeography Submarine Cable Map - see file 06 §6.1 for the quarterly-refreshed list; anchor expansion is the primary D7 + quarterly-refresh workstream  -  DO NOT expand this list without verification):

VERIFIED commercial pure-play subsea operators (HIGH confidence):
- Seaborn Networks (Seabras-1, ARBR  -  US-Brazil-Argentina pure-play). VERIFIED-ACTIVE independent operator (cost-optimizing publicly as of May 2026)  -  use as the primary HIGH subsea anchor.
- Aqua Comms / DGNet  -  legacy AEC-1/AEC-2/Havfrue/HAVSIL/CC-2 fleet. **Note: EXA Infrastructure completed its acquisition of Aqua Comms on Dec 31, 2025 (~$46M, distressed). A post-acquisition Aqua Comms record should reassign to the EXA parent (`Pure Wholesale Carrier - Network Op` / `International Backbone Specialist - Network Op`); only classify a child record as N5 if it commercially still operates as an independent subsea brand within EXA.**
- Hawaiki Submarine Cable / BW Digital (Hawaiki, Hawaiki Nui  -  Pacific; BW Digital is the parent holding company)

BORDERLINE candidates (require Phase B / quarterly-refresh verification before promoting to HIGH):
- Telxius  -  Telefónica subsidiary; MAREA, BRUSA, Junior, SAm-1. Has terrestrial backbone via Telefónica parent. Tiebreaker per N4 vs N5: if Telxius itself is the operating entity with subsea-primary revenue mix -> N5; if Telefónica parent record is the active HubSpot record -> N4 International Backbone Specialist.
- Pacific Light Data Communication (PLDC)  -  operates PLCN segments after Google/Facebook withdrew US-HK landing. Verify current operating status before classifying.

#### Subsea-specific D1 exclusions (DO NOT classify as N5):
- Pure consortium ownership with no operating entity (FLAG, SEA-ME-WE 4/5/6, ACE, EIG, IMEWE)  -  D1.4 disqualifier
- Cable manufacturing / laying / maintenance vendors with no capacity ownership (Alcatel Submarine Networks, HMN Tech, NEC OCC, SubCom, Global Marine, IT International Telecom Marine)  -  D1 equipment-vendor disqualifier. **These were previously listed as anchor candidates in some legacy docs  -  they are NOT anchors; they are D1-evicted.**
- Hyperscaler SPVs with no commercial sales motion (Meta MAREA SPV, Google Curie SPV, Amazon CAP-1 SPV)  -  `Flagged for deletion`; not commercial operators
- Cable consortiums under construction without operating-entity announcement (Stargate-aligned Pacific consortia 2025-26 announcements)  -  Greenfield (NC parent if neocloud-aligned) or `Other` if not commercial

**Anchor list quality note (2026-05-14):** The current verified-pure-play subsea operator population is genuinely small (~3-5 globally). Most "subsea" entities in the broader market are either (a) consortium-affiliated, (b) hyperscaler SPVs, (c) vendor/manufacturers, or (d) terrestrial-backbone operators with subsea positions (N4 territory). Records that look subsea but don't match the 3 HIGH anchors should classify at `low_5069` with D7 weekly re-validation; D7 web-fetches TeleGeography or company filings to confirm operating status before promoting to `high_90`. Anchor expansion is on Cooper's quarterly anchor-refresh agenda (next: 2026-08-14).

### Fiber Operator  -  6 protocols (F1-F6)

#### Protocol F1  -  `Regional CLEC - Fiber operator` (framework default; requires POSITIVE evidence)

| Q | Question | Source | Weight |
|---|---|---|---|
| F1.1 | Does `account_brief` describe a CLEC OR fiber-overbuilder OR competitive local exchange carrier? | `account_brief` | Required (gate) |
| F1.2 | `infrastructure_profile` shows Route Miles Mid-Size/Large + POPs Small/Mid-Size + Facilities Small/Mid-Size? | `infrastructure_profile` | Required |
| F1.3 | `account_brief` describes selling fiber to enterprise + SMB direct (CLEC business model)? | `account_brief` | Required |
| F1.4 | Multi-state but not national footprint (3-12 states per `account_brief`)? | `account_brief` | Strong marker |
| F1.5 | NOT a cable / HFC legacy operator (negative check) AND NOT municipal/co-op (negative check)? | `account_brief` | Required (negative) |

**Tiebreaker:** Regional CLEC is the catch-all default for mid-size fiber operators. If a record doesn't fit a more specific sub-segment (F2/F3/F4/F5/F6) AND IS a fiber CLEC archetype, it lands here.

**Best-fit thresholds:**
- `high_90`: All 5 confirmed
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5 (catch-all without all positive evidence; routes to R2/D7 re-validation)
- `Flagged for deletion`: fails F1.1 AND no other Fiber sub-segment fits -> not a Fiber Operator ICP

#### Protocol F2  -  `Long Haul / Backbone - Fiber operator`

| Q | Question | Source | Weight |
|---|---|---|---|
| F2.1 | `account_brief` describes national or multi-national long-haul backbone? | `account_brief` | Required |
| F2.2 | `infrastructure_profile` shows Route Miles Enterprise (50K+) + POPs Mid-Size/Large + Facilities Small/Mid-Size? | `infrastructure_profile` | Required for high_90 |
| F2.3 | Primary product is long-haul dark fiber OR wavelengths (NOT metro-only)? | `account_brief` | Required |
| F2.4 | Runs incumbent automation (DynamicLink / RapidRoutes / similar productized backbone services)? | `account_brief`, `recent_news_or_trigger_event` | Strong marker |
| F2.5 | Customer base includes hyperscalers + large enterprises + Tier 1 carriers? | `account_brief` | Strong marker |

**Tiebreaker** (vs F4 Tier 2 National Wholesale + N2 Pure Wholesale Carrier):
- Long-haul-primary (cross-metro dark fiber + wavelengths) -> Long Haul / Backbone
- Wholesale-only + national US/EU + 20K+ route miles -> Tier 2 National Wholesale
- Tier 1 IP transit primary (BGP routing) -> Pure Wholesale Carrier (Network Op, not Fiber)

**Best-fit:**
- `high_90`: anchor (Lumen  -  parent flag, Cogent boundary, Zayo post-CCF) + 50K+ route miles confirmed
- `medium_7089`: 3-4 of 5
- `low_5069`: 2-3 of 5

#### Protocol F3  -  `Dark Fiber Specialist - Fiber Operator` (capital "O")

| Q | Question | Source | Weight |
|---|---|---|---|
| F3.1 | `account_brief` describes 80%+ revenue from dark fiber IRU sales (vs lit transport)? | `account_brief` | Required for high_90 |
| F3.2 | Primary activity is metro / specific-route dark fiber for data center campus interconnect OR enterprise dark fiber OR specific corridors? | `account_brief` | Required |
| F3.3 | `infrastructure_profile` shows Route Miles Large/Enterprise + POPs Small/Mid-Size + Facilities Small? | `infrastructure_profile` | Required |
| F3.4 | NOT a Long Haul national backbone (negative)? | `account_brief` | Required (negative) |
| F3.5 | NOT metro lit Ethernet primary (e.g., Lightpath-style  -  negative)? | `account_brief` | Required (negative) |

**Tiebreaker:** Boundary with F2 Long Haul and F4 Tier 2 National Wholesale  -  if dark fiber is a SIDE business (<50% revenue), classify as the dominant model.

**Best-fit:**
- `high_90`: anchor (FiberLight, Stealth Communications, Allied Fiber, ITS Fiber, Conterra) + dark-fiber-primary confirmed
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

#### Protocol F4  -  `Tier 2 National Wholesale - Fiber operator`

| Q | Question | Source | Weight |
|---|---|---|---|
| F4.1 | National US or pan-EU footprint (wholesale-only) per `account_brief`? | `account_brief` | Required |
| F4.2 | `infrastructure_profile` shows Route Miles Enterprise (50K+) + POPs Large/Enterprise? | `infrastructure_profile` | Required for high_90 |
| F4.3 | 80%+ revenue from wholesale (NOT direct-enterprise) per `account_brief`? | `account_brief` | Required |
| F4.4 | PE-owned or recently consolidated (DigitalBridge / I Squared / Stonepeak / similar)? | `account_brief`, `recent_news_or_trigger_event` | Strong marker |
| F4.5 | Sells dark fiber + lit transport + waves + IRUs (broad wholesale product portfolio)? | `account_brief` | Strong marker |

**Tiebreaker:** Boundary with N2 Pure Wholesale Carrier (fiber-primary vs IP-primary). Boundary with F2 Long Haul  -  metro+long-haul lit services vs primarily long-haul dark fiber.

**Best-fit:**
- `high_90`: anchor (Zayo post-CCF acquisition, EXA Infrastructure EU) + F4.1 + F4.2 + F4.3
- `medium_7089`: 3-4 of 5  -  `Lightpath` falls here (ownership-wise wholesale-anchored, but ~10,000 route miles is below F4.2 Route Miles Enterprise 50K+ threshold; alternative classification: F2 Long Haul / Backbone or F5 Regional Cable Operator depending on dominant revenue mix)
- `low_5069`: 2 of 5

**Anchor verification note (2026-05-14, web-verified):**
- **Zayo (post-CCF):** Acquired by EQT + DigitalBridge 2020. CCF (Crown Castle Fiber) acquisition closed 2025 adding ~90K route miles to Zayo's national wholesale footprint. Currently ~224K total route miles. Solid HIGH F4 anchor.
- **Lightpath:** Jointly owned by Altice USA / Optimum (50.01%) and Morgan Stanley Infrastructure Partners (49.99%) since 2021. ~10,000 route miles + 15,000 locations. AI/hyperscaler revenue +35% YoY Q4 2025 (~$362M AI contracts in 2025). **Doesn't meet F4.2 Route Miles 50K+ threshold** - classify medium_7089 F4 or route to F2 Long Haul / Backbone depending on dominant revenue line (hyperscaler interconnect + NYC-Ashburn 323-mile corridor is F2-leaning).
- **Uniti Group (post-Windstream merger, Aug 1 2025):** Combined company has ~240,000 fiber route miles + 1.1M+ customers + 1.5M FTTH homes passed across 300+ metro markets. **NO LONGER pure-wholesale** - the Windstream side brought significant consumer FTTH + enterprise direct retail. **REMOVED from F4 anchor list** as of 2026-05-14. Per N1/N2 tiebreaker (multi-segment activity with consumer retail presence -> Tier 1 Carrier), the COMBINED Uniti entity may now classify N1 Tier 1 Carrier - Network Op or as split-book operator. The LEGACY Uniti pre-merger wholesale book WAS a clean F4 anchor; the combined entity is not. Existing HubSpot Uniti records should re-classify at next R2 cycle - apply split-book treatment if separate "Uniti Wholesale" sub-entity exists.
- **EXA Infrastructure:** Formerly GTT Infrastructure (separated 2021). Completed acquisition of Aqua Comms Dec 31, 2025 (subsea fleet; ~$46M distressed deal). Pan-EU + transatlantic wholesale fiber. Solid HIGH F4 anchor for EU operations; flag for N4 International Backbone Specialist if the HubSpot record reflects the international/subsea dominant revenue mix.

#### Protocol F5  -  `Regional Cable Operator - Fiber operator`

| Q | Question | Source | Weight |
|---|---|---|---|
| F5.1 | `account_brief` describes parent as regional or multi-state (3-22 states) cable operator? | `account_brief` | Required (gate) |
| F5.2 | Mostly residential cable parent with growing commercial fiber book? | `account_brief` | Required |
| F5.3 | `infrastructure_profile` shows Route Miles Mid-Size/Large + POPs Small/Mid-Size + Facilities Mid-Size/Large? | `infrastructure_profile` | Strong marker |
| F5.4 | NOT a national cable parent (negative  -  re-route to N3 Cable MSO Network Op if national)? | `account_brief` | Required (negative) |
| F5.5 | Legacy MSO that bought or built fiber for enterprise / community anchor sales? | `account_brief` | Marker |

**Tiebreaker:** Regional vs National scale. National + B2B >=$1.5B -> N3 Cable MSO Network Op. Regional -> F5 Regional Cable Operator Fiber.

**Best-fit:**
- `high_90`: anchor (Breezeline, WOW!, Mediacom Business, Midco Business, Cable ONE / Sparklight)
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

#### Protocol F6  -  `Municipal / Cooperative - Fiber operator`

| Q | Question | Source | Weight |
|---|---|---|---|
| F6.1 | Ownership: municipal utility, electric cooperative, community-owned, or multi-operator consortium? | `account_brief`, `.gov`/`.coop` domain | Required (gate) |
| F6.2 | Member of NTCA / NRECA / state broadband consortium? | `account_brief`, `recent_news_or_trigger_event` | Strong marker |
| F6.3 | BEAD / NTIA / USDA RUS subgrant recipient? | `recent_news_or_trigger_event` | Strong marker |
| F6.4 | Open-access OR federation-organized business model? | `account_brief` | Marker |
| F6.5 | NOT middle-mile-only (negative  -  middle-mile-only is EXCLUDED per file 05)? | `account_brief` | Required (negative) |

**Tiebreaker:** Middle-mile-only operators (no commercial wholesale) -> not even Municipal/Cooperative; route to `customer_segment = "Other"` or `Flagged for deletion`.

**Best-fit:**
- `high_90`: F6.1 + F6.5 + 2 of (F6.2, F6.3, F6.4)  -  anchor matches EPB Chattanooga, UTOPIA Fiber, Diamond State Networks, NEMR Telecom
- `medium_7089`: F6.1 + F6.5 + 1 strong marker
- `low_5069`: F6.1 confirmed only; markers unverified

### Data Center Colo Provider  -  4 protocols (C1-C4)

#### Protocol C1  -  `Standard - colo` (framework default; requires POSITIVE evidence)

| Q | Question | Source | Weight |
|---|---|---|---|
| C1.1 | `account_brief` describes per-rack / per-cabinet / per-kW pricing (retail interconnection model)? | `account_brief` | Required |
| C1.2 | High cross-connect volume / large MMR / named carrier hotel positioning? | `account_brief` | Strong marker |
| C1.3 | Tenant count described as hundreds (NOT 3-10 anchor tenants)? | `account_brief` | Required |
| C1.4 | `infrastructure_profile` shows Facilities Mid-Size/Large/Enterprise + Route Miles None Identified + POPs Small/Mid-Size? | `infrastructure_profile` | Required for high_90 |
| C1.5 | NOT primarily GPU-tenant focused with liquid cooling (negative)? | `account_brief` | Required (negative) |

**Tiebreaker** (vs C2 AI Signals + C4 Hyperscale Wholesale): Standard sells retail per-rack/cabinet. AI Signals sells anchor-tenant capacity with GPU customer concentration. Hyperscale Wholesale sells per-MW with hyperscaler concentration. Split-book operators (Equinix parent vs xScale child): parent record -> Standard by majority revenue; xScale child record (if separate) -> Hyperscale Wholesale.

**Best-fit:**
- `high_90`: anchor (Equinix parent, Digital Realty parent, CoreSite, Cologix, DataBank, Flexential, ARK, Centra) + C1.1 + C1.3 + C1.4. **NOTE: Switch (DigitalBridge + IFM take-private Dec 2022, $11B) is NO LONGER a C1 anchor as of 2026-05-14 verification  -  Switch's "PRIMES" campuses are hyperscale-focused (Microsoft / Google / Amazon are major tenants, 100MW+ per campus, $5B+ contracted build pipeline). Switch is now C4 Hyperscale Wholesale by majority revenue. The Switch HubSpot record should re-classify to C4 unless the parent record specifically reflects the legacy Las Vegas / Atlanta / Grand Rapids retail-interconnection book.**
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

#### Protocol C2  -  `AI Signals - colo`

| Q | Question | Source | Weight |
|---|---|---|---|
| C2.1 | `account_brief` describes confirmed GPU tenants (named neocloud or hyperscale-AI customers)? | `account_brief`, `recent_news_or_trigger_event` | Required for high_90 |
| C2.2 | `account_brief` or `recent_news` mentions liquid cooling (D2C / immersion / direct-to-chip)? | `account_brief`, `recent_news_or_trigger_event` | Required |
| C2.3 | 30kW+ rack densities standard per `account_brief` or `recent_news`? | `account_brief`, `recent_news_or_trigger_event` | Required |
| C2.4 | Anchor-tenant economics (10-15 year leases, 60%+ revenue from named tenants)? | `account_brief` | Strong marker |
| C2.5 | NOT primarily hyperscaler cloud capacity (>60% from AWS/Azure/Google/Meta/Oracle  -  negative for AI Signals; that's HW)? | `account_brief` | Required (negative) |

**Tiebreaker:** Boundary with C4 Hyperscale Wholesale  -  hyperscaler-anchored = HW; GPU-tenant-anchored = AI Signals. Boundary with NC5 Crypto to AI - Neoclouds  -  crypto-miner pivots (Crusoe, Applied Digital / APLD, IREN, Core Scientific, Hut 8, Galaxy Digital, TeraWulf, Bitfarms, Northern Data Group) ALL fit NC5 regardless of landlord vs operator model (per Cooper 2026-05-14). C2 anchors must have verifiable NO Bitcoin mining history. **Prometheus Hyperscale verified clean (founded 2020 by Trenton Thornock on family ranch land in Wyoming, no crypto lineage)  -  qualifies as C2 anchor, not NC5.**

**Best-fit:**
- `high_90`: anchors verified via 2026-05-14 web research  -  `Colovore` (Santa Clara, liquid-cooled, 15-50kW/cabinet today scaling to 250kW DLC, no crypto history, serves Fortune 500 + SV GPU tenants); `Prometheus Hyperscale` (formerly Wyoming Hyperscale Whitebox, founded 2020 on Thornock family ranch land, no crypto history, Oklo nuclear partnership, Wyoming + Texas I-35 corridor build  -  if currently pre-operational at the record date, may also score G Greenfield until first site goes live). Boutique GPU-tenant-anchored colos with verifiable NO-mining-history qualify on best-fit (file 06 §6.2 quarterly-refresh-targeted list).
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

**Anchor list state (2026-05-14):** C2 anchor pool is genuinely thin because most AI-tenant-anchored colos in the market today have Bitcoin mining heritage (Crusoe, Applied Digital / APLD, IREN, Core Scientific, Hut 8, Galaxy Digital, TeraWulf, Bitfarms)  -  those all route to NC5 Crypto to AI - Neoclouds per Cooper 2026-05-14 (inclusive of operator AND landlord models). True C2 anchors are operators who built AI-density colocation from scratch without a mining past. Verified HIGH anchors as of 2026-05-14: Colovore + Prometheus Hyperscale. Quarterly anchor refresh on 2026-08-14 will expand this list.

#### Protocol C3  -  `Modular - colo`

| Q | Question | Source | Weight |
|---|---|---|---|
| C3.1 | `account_brief` describes distributed/prefabricated/containerized DC operator (>=3 sites OR explicit "modular DC" build language)? | `account_brief` | Required |
| C3.2 | Growth = site count, not campus expansion? | `account_brief`, `recent_news_or_trigger_event` | Required |
| C3.3 | `infrastructure_profile` shows Facilities Mid-Size/Large (site-count-based) + Route Miles None Identified? | `infrastructure_profile` | Strong marker |
| C3.4 | `recent_news` mentions pod expansion at new power sites? | `recent_news_or_trigger_event` | Strong marker |
| C3.5 | NOT a hyperscaler-only operator (negative  -  that's HW)? | `account_brief` | Required (negative) |

**Best-fit:**
- `high_90`: anchor (Nodiac - Denver-HQ, 1-15MW containerized modules co-located at renewable energy sites, 800MW + 500+ site PIPELINE not operational, recent PowerBank LOI Mar 2026; EdgePresence / Ubiquity; Armada; Colony Compute) + C3.1 + C3.2
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5  -  boundary with Greenfield if pre-operational

**Anchor verification note (2026-05-14):**
- Nodiac claim "500+ sites" in legacy file 06 was overstated; web verification 2026-05-14 confirms the 500+ sites are an IDENTIFIED PIPELINE for deployment, not operational sites. Nodiac's operational site count is in the low double digits as of Q1 2026. The 800MW pipeline figure is accurate. Boundary with Greenfield (G): records that have a Nodiac-style pipeline announced but <3 operational sites should classify as `Greenfield` (cross-segment, Colo parent) until first operational site goes live, at which point R2 auto-migrates to `Modular - colo`.
- EdgePresence acquired by Ubiquity 2023 - the combined entity (Ubiquity portfolio) is the active HubSpot record.
- Armada operates containerized DCs at remote / edge sites. Verified active 2025-26.
- Colony Compute is a newer entrant (2024); thin commercial track record. Classify `medium_7089` until quarterly refresh.

#### Protocol C4  -  `Hyperscale Wholesale - colo`

| Q | Question | Source | Weight |
|---|---|---|---|
| C4.1 | `account_brief` describes 10MW+ standard single deployments? | `account_brief` | Required |
| C4.2 | 5-15 year lease terms with ROFR/ROFO per `account_brief` or `recent_news`? | `account_brief`, `recent_news_or_trigger_event` | Required |
| C4.3 | 60%+ revenue from hyperscalers (AWS/Azure/Google/Meta/Oracle) per `account_brief`? | `account_brief` | Required for high_90 |
| C4.4 | 3-10 anchor tenants total per `account_brief` (vs hundreds for Standard)? | `account_brief` | Required |
| C4.5 | `infrastructure_profile` shows Facilities Mid-Size/Large + power capacity 100MW-5GW per `recent_news`? | `infrastructure_profile`, `recent_news_or_trigger_event` | Strong marker |

**Tiebreaker (vs C1 Standard - colo for split-book operators):** Equinix parent record -> Standard. Equinix xScale separate record (if exists) -> Hyperscale Wholesale. Same logic for Vantage, Aligned, NTT, Iron Mountain, QTS  -  classify the PARENT record by its majority revenue, classify the CHILD record (xScale-equivalent) by hyperscale focus. NO `manual_review_required` for parent records.

**Best-fit:**
- `high_90`: anchor (Compass, Aligned, Stack Infrastructure, NTT GDCA, QTS, CyrusOne, Vantage, EdgeConneX, AirTrunk, Equinix xScale child) + C4.1 + C4.2 + C4.3
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

### NeoCloud  -  5 protocols (NC1-NC5)

#### Quantitative threshold matrix for NC1 vs NC3 boundary (CRITICAL  -  see §6a below)

The `Large Scale GPU - Neocloud` (NC1) vs `AI Infrastructure providers - Neocloud` (NC3) boundary is the most frequently mis-classified pair. See §6a for the deterministic threshold table.

#### Protocol NC1  -  `Large Scale GPU - Neocloud`

| Q | Question | Source | Weight |
|---|---|---|---|
| NC1.1 | `account_brief` describes 10+ facilities OR multi-facility GPU compute footprint with disclosed >=50MW capacity? | `account_brief`, `recent_news_or_trigger_event` | Required |
| NC1.2 | Bare-metal GPU clusters with custom network topologies (InfiniBand or Ultra Ethernet)? | `account_brief` | Strong marker |
| NC1.3 | Named hyperscaler + enterprise training customer base per `account_brief`? | `account_brief` | Required |
| NC1.4 | Reserved-instance / multi-week-or-month-contract pricing model (NOT per-GPU-hour on-demand only)? | `account_brief` | Required for boundary vs NC3 |
| NC1.5 | NOT a former crypto miner (negative  -  that's NC5)? | `account_brief` | Required (negative) |

**Tiebreaker** (vs NC3 AI Infrastructure providers + NC5 Crypto to AI):
- Bitcoin mining history -> NC5 Crypto to AI (regardless of current model)
- Disclosed GPU capacity >=50MW AND 10+ GPU facilities -> NC1 Large Scale GPU
- Disclosed GPU capacity <50MW OR <10 facilities OR per-GPU-hour primary pricing -> NC3 AI Infrastructure providers
- See §6a for the full threshold matrix

**Best-fit:**
- `high_90`: anchor (Nebius, Lambda Labs, Voltage Park, CoreWeave) + NC1.1 + NC1.3 + NC1.4
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

**Anchor verification 2026-05-14:**
- REMOVED from NC1 (route to NC5): Crusoe - flared-gas BTC mining operation before AI pivot 2023-2024. Per Cooper 2026-05-14 NC5 inclusive rule, Bitcoin mining heritage routes to NC5 regardless of current operating model.
- KEPT as VERIFIED NC1 anchors (no BTC mining heritage): Nebius (Yandex N.V. cloud spin-off 2024), Lambda Labs (15+ US DCs, 320MW), CoreWeave (NVIDIA-anchored, post-IPO 2025).
- FLAG for D7 re-verification: Voltage Park merged with Lightning AI in February 2026. If Voltage Park brand still operates as a distinct GPU cloud entity post-merger, keep as NC1 anchor. If Lightning AI absorbed the brand entirely (Lightning AI is AI-platform tooling, NOT a GPU operator), reclassify under Lightning AI parent and remove Voltage Park as an NC1 anchor.

#### Protocol NC2  -  `Tier 1 Inference - Neocloud`

| Q | Question | Source | Weight |
|---|---|---|---|
| NC2.1 | `account_brief` describes distributed inference endpoints at 20-50+ edge cities? | `account_brief`, `recent_news_or_trigger_event` | Required |
| NC2.2 | Sub-100ms token latency SLA mentioned? | `account_brief`, `recent_news_or_trigger_event` | Required |
| NC2.3 | Per-million-tokens pricing model (NOT per-GPU-hour) per `account_brief`? | `account_brief` | Required (boundary test) |
| NC2.4 | `infrastructure_profile` shows Facilities Small (carrier hotels) + POPs Mid-Size/Large (distributed)? | `infrastructure_profile` | Strong marker |
| NC2.5 | NOT a former crypto miner (negative)? | `account_brief` | Required (negative) |

**Best-fit:**
- `high_90`: anchor (Together.ai, Groq, Cirrascale, DeepInfra, Fireworks AI, SambaNova, Baseten) + NC2.1 + NC2.2 + NC2.3
- `medium_7089`: 3-4 of 5 (Mistral AI La Plateforme is a boundary case - foundation-model lab that runs its own inference API. Classify NC2 `medium_7089` if their inference platform footprint is the dominant commercial offering; otherwise route to `Other` as a foundation-model lab rather than an infrastructure operator)
- `low_5069`: 2 of 5

**Anchor verification note (2026-05-14):** Sakana AI was previously listed as an NC2 anchor in legacy docs but is REMOVED. Web verification 2026-05-14: Sakana AI is a Tokyo-based AI research and model-development company (founded by David Ha, Llion Jones, Ren Ito) that CONSUMES GPU compute from GMO Internet's GMO GPU Cloud, NOT provides infrastructure. Sakana fails NC2.1 (no distributed inference endpoints across edge cities) and NC2.3 (no per-million-tokens commercial inference platform as primary offering). Classify Sakana AI as `customer_segment = "Other"` (AI lab / foundation-model developer category, not an infrastructure-operator ICP).

#### Protocol NC3  -  `AI Infrastructure providers - Neocloud` (lowercase "p")

| Q | Question | Source | Weight |
|---|---|---|---|
| NC3.1 | `account_brief` describes mid-market cloud provider (5-30 locations, broad customer mix) ADDING GPU compute to existing base? | `account_brief` | Required |
| NC3.2 | Per-GPU-hour pricing primary (NOT per-million-tokens, NOT reserved-instance multi-month only)? | `account_brief` | Required |
| NC3.3 | Existing non-GPU products visible (cloud licensing, VPS, basic compute)  -  not pure GPU-only? | `account_brief` | Required |
| NC3.4 | `infrastructure_profile` shows Facilities Small/Mid-Size + POPs Small/Mid-Size? | `infrastructure_profile` | Strong marker |
| NC3.5 | NOT sovereign-positioning primary (negative  -  that's NC4)? | `account_brief` | Required (negative) |

**Tiebreaker** (vs NC1 Large Scale GPU + NC2 Tier 1 Inference + NC4 Sovereign AI):
- Pricing model is the test  -  per-GPU-hour = NC3; per-million-tokens = NC2; reserved-instance/multi-month + >=50MW + 10+ facilities = NC1
- Sovereignty primary marketing = NC4
- See §6a for quantitative thresholds

**Best-fit:**
- `high_90`: anchor (Vultr, DigitalOcean, Fluidstack, Modal, RunPod, OVHcloud, Scaleway) + NC3.1 + NC3.2 + NC3.3
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

#### Protocol NC4  -  `Sovereign AI Clouds - Neocloud`

**Triple-signal qualifier preferred but not strictly required. Apply best-fit.**

| Q | Question | Source | Weight |
|---|---|---|---|
| NC4.1 | `account_brief` uses explicit sovereign positioning (sovereign cloud / GAIA-X / national AI program / national sovereignty)? | `account_brief` | Required (gate) |
| NC4.2 | `recent_news` mentions GDPR / DPDP / national-program regulatory compliance? | `recent_news_or_trigger_event` | Required |
| NC4.3 | >=1 sovereign-mandated customer reference (regulated industry, government, sovereign-affiliated)? | `account_brief`, `recent_news_or_trigger_event` | Strong marker |
| NC4.4 | National AI program affiliation (UK AI Research Resource, GAIA-X, BSC, etc.)? | `account_brief` | Strong marker |
| NC4.5 | In-country marketing primary (vs global marketing with sovereign add-on)? | `account_brief`, `country` | Strong marker |

**Tiebreaker** (vs NC3): Sovereignty PRIMARY brand identity = NC4. Sovereignty add-on with global brand = NC3.

**Best-fit:**
- `high_90`: anchor (Nscale, Firmus, E2E Networks, Yotta, G42 / Inception, BSC - Barcelona Supercomputing Center, Scaleway boundary if French/EU sovereignty positioning is dominant) + NC4.1 + NC4.2
- `medium_7089`: NC4.1 + 1 strong marker
- `low_5069`: NC4.1 only (sovereignty marketing without supporting evidence)

**Anchor verification note (2026-05-14):** Sakana AI was previously listed as an NC4 anchor in legacy docs but is REMOVED for the same reason as NC2: Sakana is an AI research / foundation-model company, not a sovereign-cloud infrastructure operator. They may operate in Japan with NVIDIA partnership and have national-sovereignty undertones, but they don't run a sovereign-cloud commercial offering. Classify as `Other` (AI lab category).

#### Protocol NC5  -  `Crypto to AI - Neoclouds` (trailing "s"; INCLUSIVE of operator AND landlord per Cooper 2026-05-14)

**Definition:** "Companies that used to mine for Bitcoin that have since pivoted to being more of a neocloud / co-location operator." The defining trait is the BITCOIN MINING PAST + AI PIVOT, regardless of current business model.

| Q | Question | Source | Weight |
|---|---|---|---|
| NC5.1 | `account_brief` confirms verifiable Bitcoin mining history (current or historical)? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| NC5.2 | `account_brief` or `recent_news` confirms AI infrastructure pivot OR active GPU compute deployment? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| NC5.3 | <=$0.05/kWh power AND immersion / liquid cooling deployed? | `account_brief` | Strong marker |
| NC5.4 | `infrastructure_profile` shows Facilities Mid-Size/Large + Route Miles None Identified + POPs Small? | `infrastructure_profile` | Strong marker |
| NC5.5 | Pivot announcement >=6 months old (mature enough to qualify)? | `recent_news_or_trigger_event` | Required |

**Business model is NOT a gate.** Both landlord (IREN with Microsoft, Core Scientific with CoreWeave) and operator (Galaxy GPU compute, Bitfarms post-pivot, hybrid TeraWulf) qualify if NC5.1 + NC5.2 + NC5.5 confirm.

**Tiebreaker** (vs C2 AI Signals colo + NC1 Large Scale GPU):
- Bitcoin mining history confirmed -> NC5 Crypto to AI (regardless of operator vs landlord)
- No mining history + landlord-only with GPU tenants -> C2 AI Signals colo
- No mining history + operator-only with multi-facility GPU compute -> NC1 Large Scale GPU

**Best-fit:**
- `high_90`: anchor (full verified BTC-to-AI pivot list - see below) + NC5.1 + NC5.2 + NC5.5
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5

**Verified NC5 anchor list (2026-05-14, web-verified BTC mining + AI pivot):**

| Company | BTC mining heritage | AI pivot evidence | Operator vs Landlord |
|---|---|---|---|
| IREN (Iris Energy) | Original flared-gas BTC miner, ASX-listed | Microsoft $9.7B / 200MW landlord deal Nov 2025; NVIDIA 5GW global AI factory partnership | Landlord (Microsoft hosting) |
| Core Scientific | Public BTC miner, post-Chapter-11 emergence | CoreWeave host landlord deal, multi-site retrofit | Landlord (CoreWeave hosting) |
| Galaxy Digital | Crypto financial services with mining + datacenter arm | Helios West Texas campus 800MW lease to CoreWeave ($4.5B over 15yr); $1.4B Deutsche Bank loan for retrofit | Landlord (CoreWeave hosting) |
| Bitfarms | Public BTC miner, multi-site | Post-2024 GPU compute pivot, hybrid operator | Operator + Landlord hybrid |
| TeraWulf | Public BTC miner, Lake Mariner NY | Lake Mariner HPC/AI buildout, Core42 hosting deal | Landlord (Core42 hosting) + Operator |
| APLD / Applied Digital | Hosted Marathon Digital BTC mining at ND campuses | Polaris Forge 1 (100MW CoreWeave lease ~$11B 15yr revenue); Polaris Forge 2 (200MW lease to investment-grade hyperscaler, $5B 15yr revenue Oct 2025); Delta Forge 1 (430MW broke ground Jan 2026); ChronoScale spin-out announced Dec 29 2025 (cloud business + EKSO merger, expected close H1 2026, Applied Digital retains ~97% of CHRN) | Landlord primary (post-ChronoScale spin, APLD = landlord; CHRN = operator) |
| Crusoe | Flared-gas BTC mining 2018-2024 (425+ modular DCs, 250+ MW deployed across 7 states + 2 countries) | NYDIG acquired Crusoe's BTC mining business March 2025; Crusoe retains equity stake but now 100% AI-focused. Stargate Abilene partnership with OpenAI / Oracle; expanding from 2 buildings / 200MW H1 2025 to 8-building multi-hundred-MW; $1.4B Series funding (Mubadala + Valor Equity) at $10B valuation | Operator (Crusoe Cloud GPUaaS) - mining business divested but mining heritage routes per Cooper 2026-05-14 |
| Northern Data Group | German BTC miner (Taiga, Ardennes) | AI compute pivot 2024-26 (Taiga Cloud, Ardennes GPU buildouts) | Operator (Taiga Cloud) |
| Hut 8 | Public BTC miner since 2018 (Canadian / US, 205MW Texas BTC facility 2025) | River Bend Louisiana 15yr / 245MW / $7B Fluidstack lease (Anthropic partnership); Beacon Point Texas 15yr / 352MW / $9.8B lease announced May 2026 | Landlord primary (hyperscaler AI tenants) |
| Hive Digital Technologies | Public BTC miner since 2017 | HPC / AI compute pivot announced 2023-24 - verify current commercialization status at D7 cycle | Operator (HPC / GPU rentals; verify) |

**Verification note (2026-05-14):**
- ADDED to NC5: APLD / Applied Digital (was incorrectly in C2 AI Signals colo - Applied Blockchain Bitcoin/Ethereum mining heritage confirmed via web research), Crusoe (was incorrectly in NC1 Large Scale GPU - flared-gas BTC mining 2018-2024 confirmed, NYDIG divested March 2025 but heritage routes per Cooper 2026-05-14 inclusive rule), Hut 8 (verified BTC miner with $7B Fluidstack/Anthropic + $9.8B Beacon Point AI DC deals 2025-2026), Hive Digital Technologies (public BTC miner with confirmed HPC/AI pivot).
- REMOVED FALSE ENTRY: Prometheus Hyperscale was previously listed as a "Hut 8 rebrand" in NC5 - web verification 2026-05-14 confirmed Prometheus Hyperscale is a SEPARATE company (formerly Wyoming Hyperscale Whitebox, founded 2020 by Trenton Thornock on family ranch land in Wyoming, Oklo nuclear partnership). NO Hut 8 lineage. Prometheus Hyperscale is now a C2 AI Signals colo anchor, NOT NC5.
- Crusoe note: 2-3 years post-pivot, the BTC heritage is still recent enough to qualify NC5 per Cooper's rule. Quarterly refresh may "graduate" Crusoe to NC1 in 2027-28 once mining lineage is no longer material to current ops (5+ years post-pivot).
- DGHI (DMG Blockchain Solutions) and Bitdeer Technologies are BORDERLINE - have BTC mining heritage but limited public AI-pivot evidence. Classify low_5069 with D7 re-verification.
- NOT in NC5: Marathon Digital, Riot Platforms, CleanSpark - these still primarily mine BTC with limited or no public AI pivot. Stay in `Other` (out-of-ICP) until pivot is announced. Re-evaluate at quarterly refresh.

### MSP/Aggregator  -  5 protocols (M1-M5)

#### Protocol M1  -  `Telecom Aggregator - MSP` (framework default; requires POSITIVE evidence)

| Q | Question | Source | Weight |
|---|---|---|---|
| M1.1 | `account_brief` describes traditional channel aggregator / telecom broker reselling carrier connectivity? | `account_brief` | Required |
| M1.2 | Multi-vendor agency model with vendor portfolio of 30-100 carriers? | `account_brief` | Required |
| M1.3 | NOT sub-agent / 1099 channel-based (negative  -  that's TSD or Master Agent)? | `account_brief` | Required (negative) |
| M1.4 | NOT cloud-reselling primary (negative  -  that's Cloud + Telecom Hybrid)? | `account_brief` | Required (negative) |
| M1.5 | NOT IoT/eSIM platform (negative  -  D1 EXCLUDE)? | `account_brief` | Required (negative) |

**Tiebreaker:** Boundary with M5 Cloud + Telecom Hybrid  -  Hybrid has explicit AWS Premier / Azure Expert partner status; Telecom Aggregator does not.

**Best-fit:**
- `high_90`: anchor (Granite, Nitel) + M1.1 + M1.2 + M1.3 + M1.4 + M1.5
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5
- `Flagged for deletion`: IoT/eSIM platform (Aeris-style) -> D1.5 disqualifier triggers eviction

#### Protocol M2  -  `Managed Network Services - MSP`

| Q | Question | Source | Weight |
|---|---|---|---|
| M2.1 | `account_brief` describes 70%+ revenue from managed services contracts (NOT commission resell)? | `account_brief` | Required |
| M2.2 | Vendor-neutral OR vendor-specific partner status (Cisco / Fortinet / Palo Alto)? | `account_brief` | Strong marker |
| M2.3 | Customer base of mid-market and enterprise per `account_brief`? | `account_brief` | Required |
| M2.4 | NOT primary agent network (sub-agents)  -  direct service delivery? | `account_brief` | Required (negative) |
| M2.5 | NOT pure cloud (must have network services component)? | `account_brief` | Required (negative) |

**Tiebreaker** (vs M5 Cloud + Telecom Hybrid for IT integrators): Cloud revenue >=30% AND AWS Premier / Azure Expert partner -> Cloud + Telecom Hybrid. Network services primary AND <30% cloud -> Managed Network Services.

**Best-fit:**
- `high_90`: anchor (Open Systems, Hughes, Logicalis, Presidio, GTT) + M2.1 + M2.3 + M2.4
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5  -  IT integrators (CDW, Insight, ePlus, WWT) at $10B+ scale; apply tiebreaker

#### Protocol M3  -  `TSD Technology Services Distributor - MSP`

| Q | Question | Source | Weight |
|---|---|---|---|
| M3.1 | `account_brief` describes 100+ active sub-agents AND aggregates carrier contracts through sub-agent network? | `account_brief` | Required (gate) |
| M3.2 | Gross billings >=$1B mentioned in `account_brief` or `recent_news` (Omdia-style)? | `account_brief`, `recent_news_or_trigger_event` | Required |
| M3.3 | National US footprint with Canada / EU expansion? | `account_brief`, `country` | Required |
| M3.4 | Multi-vendor portfolio of 100+ carriers? | `account_brief` | Strong marker |
| M3.5 | Separate enablement / training arm for sub-agents? | `account_brief` | Marker |

**Best-fit:**
- `high_90`: anchor (Telarus $2.9B GB, AVANT $2.1B, Intelisys/ScanSource $2.7B, AppDirect $2.0B, Sandler Partners ~$209M, Bridgepointe firmly TSD-tier post-2026 recap) + M3.1 + M3.2 + M3.3
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5  -  boundary with M4 Master Agent (sub-$1B gross billings)

#### Protocol M4  -  `Master Agent - MSP` (NO DEFAULT MANUAL REVIEW per Cooper 2026-05-14)

Classify as Master Agent based on best-fit positive evidence. Lower confidence (`low_5069`) if anchor list is thin  -  R2 + D7 will re-validate.

| Q | Question | Source | Weight |
|---|---|---|---|
| M4.1 | `account_brief` describes 10-50 active sub-agents (smaller than TSD)? | `account_brief` | Required |
| M4.2 | Net commission revenue $5M-$100M OR gross billings sub-$1B per `account_brief`? | `account_brief` | Required |
| M4.3 | Regional footprint (3-20 states) OR vertical specialty (healthcare-only, hospitality-only, multifamily-only)? | `account_brief`, `country`, `state` | Strong marker |
| M4.4 | Independent (NOT acquired by AppDirect / AVANT / Telarus / ScanSource since 2018)? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| M4.5 | Operating post-2022 with verified current activity (LinkedIn / press)? | `recent_news_or_trigger_event` | Required (gate) |

**Tiebreaker** (vs M3 TSD): >=100 sub-agents AND >=$1B gross billings -> TSD; otherwise Master Agent. Acquired entities (TBI, CarrierSales, PlanetOne, MicroCorp, World Telecom Group) -> re-classify under acquirer; historical record gets `Flagged for deletion` after consolidation per R4.

**Best-fit:**
- `high_90`: anchor (X4 Solutions confirmed; CyberNet Communications medium  -  Phase B verified independents; quarterly-refresh-targeted list at file 06 §6.5) + M4.1 + M4.4 + M4.5
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5  -  typical Master Agent archetype with thin anchor verification
- `Flagged for deletion`: M4.4 fails (already acquired) AND M4.5 fails (no current activity)

**Master Agent anchor list (Phase B verified; quarterly refresh 2026-08-14):**

HIGH confidence (verified independent post-2022):
- X4 Solutions  -  named in file 06 §6.5; web-verified active 2026; primary verified independent. Sub-agent network with UCaaS + carrier portfolio.

MEDIUM confidence (post-Phase-B, needs D7 re-validation):
- CyberNet Communications  -  referenced in file 06 §6.5 as MEDIUM. **NOTE 2026-05-14 web verification: `cybernetcom.com` markets services TO master agents (carrier services, wholesale voice, IaaS)  -  operates as a CLEC offering carrier infrastructure to master-agency channels rather than itself being a master agency. May be misclassified in legacy file 06. Flag for D7 web-research re-validation before any new write uses this as a Master Agent anchor.**

ACQUIRED / DO-NOT-USE as Master Agent (per M4.4 negative gate):
- TBI (acquired by AppDirect 2021)  -  re-route to AppDirect TSD parent
- CarrierSales (acquired by AVANT 2020)  -  re-route to AVANT TSD parent
- PlanetOne (acquired by AppDirect 2022)  -  re-route to AppDirect TSD parent
- MicroCorp (acquired by Sandler Partners 2021)  -  re-route to Sandler TSD parent
- World Telecom Group (acquired by Telarus 2019)  -  re-route to Telarus TSD parent

**Honest anchor-list state (Cooper-approved expected steady state):** The verified-independent Master Agent population is thin (1 HIGH + 1 MEDIUM-pending-reverification). Master Agent is the most consolidated MSP sub-segment  -  Telarus, AppDirect, AVANT, Sandler, ScanSource have rolled up most boutique agencies since 2018. Records that match the M4 archetype but lack named-anchor match should classify at `low_5069` and route to D7 weekly re-validation. D7 webfetches the company website + LinkedIn + recent press to verify (a) independent operating status, (b) post-2022 activity, (c) sub-agent count band, before promoting to `medium_7089` or `high_90`. Anchor list expansion is on Cooper's quarterly anchor-refresh agenda  -  DO NOT add speculative anchors here.

**Distinguishing Master Agent vs CLEC-with-channel-program (common misclassification):** A CLEC, TSD, or carrier that sells its own services THROUGH master agents is NOT itself a Master Agent. The Master Agent is the agency that aggregates carrier portfolios and sells THROUGH sub-agents. M4.1 (10-50 active sub-agents) + M4.4 (not acquired) are the load-bearing gates. Records that show "we work with master agents" or "master agent program available" without showing sub-agent recruitment are likely the carrier side, not the agency side  -  classify as M2 Managed Network Services, M5 Cloud + Telecom Hybrid, or `Other` per dominant business model.

#### Protocol M5  -  `Cloud + Telecom Hybrid MSP - MSP`

| Q | Question | Source | Weight |
|---|---|---|---|
| M5.1 | AWS Premier Tier OR Azure Expert MSP OR Google Cloud Premier partner status? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| M5.2 | `account_brief` describes >=30% cloud revenue (licensing, migration, managed cloud)? | `account_brief` | Required |
| M5.3 | Network services in PRIMARY marketing (SD-WAN, SASE, managed circuits)? | `account_brief` | Required |
| M5.4 | Customer base of mid-market and enterprise? | `account_brief` | Strong marker |
| M5.5 | NOT pure cloud MSP without network services (negative  -  D1 EXCLUDE)? | `account_brief` | Required (negative) |

**Tiebreaker** (vs M2 Managed Network Services for IT integrators): Cloud revenue >=30% AND cloud partner status confirmed -> Cloud + Telecom Hybrid. Network services dominant AND cloud <30% -> Managed Network Services.

**Best-fit:**
- `high_90`: anchor (AHEAD, CDW post-Mission, Insight post-SADA, WWT, ePlus, Effectual Cloud, RapidScale) + M5.1 + M5.2 + M5.3
- `medium_7089`: 3-4 of 5
- `low_5069`: 2 of 5
- `Flagged for deletion`: pure cloud MSP with no network services (Mission Cloud pre-acquisition standalone, SADA pre-acquisition standalone)

### Enterprise-CustomerSegment  -  4 protocols (E1-E4) + Greenfield cross-segment (G)

Enterprise has the strictest pre-gate (vertical + scale). If pre-gate fails, record goes to `customer_segment = "Other"` or `Flagged for deletion`, NOT Enterprise.

#### Protocol E1  -  `Financial Services - Enterprise`

| Q | Question | Source | Weight |
|---|---|---|---|
| E1.1 | `account_brief` describes financial services (banking / investment / insurance / payment / capital markets) OR commercial-procurement defense contractor? | `account_brief` | Required (gate) |
| E1.2 | $1B+ revenue per `account_brief`? | `account_brief`, `annualrevenue` | Required (gate) |
| E1.3 | `infrastructure_profile` shows Facilities Mid-Size/Large/Enterprise (3+ DCs) OR direct Equinix Fabric/Megaport port mentioned? | `infrastructure_profile`, `recent_news_or_trigger_event` | Required (gate) |
| E1.4 | In-house network engineering team (NOC presence OR job postings for VP/Director/Principal Network Engineering)? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| E1.5 | Direct carrier contracts (NOT everything through MSP/reseller)? | `account_brief` | Required (gate) |

**Tiebreaker** (CVS / UnitedHealth / McKesson  -  diversified players): Use DOMINANT REVENUE LINE in `account_brief`. CVS retail-pharmacy + insurance hybrid -> if retail-pharmacy revenue dominant -> Retail and Distribution; if insurance/PBM dominant -> Financial Services. UnitedHealth parent -> Financial Services (insurer); Optum split as separate record. McKesson/Cardinal/AmerisourceBergen (pharma distribution) -> Healthcare Systems.

**Best-fit:**
- `high_90`: anchor (JPMorgan, Goldman, BNY, State Street, Visa, Mastercard, BoA, Wells Fargo, Citi, BlackRock, Schwab, HSBC, Barclays, BNP Paribas, Mizuho, Nomura, defense contractors w/ commercial procurement Lockheed/RTX/Northrop/BAE/L3Harris) + all 5 gates
- `medium_7089`: 4 of 5 gates
- `low_5069`: 3 of 5 gates
- `Flagged for deletion`: fewer than 3 gates pass AND no clear path to other ICP

#### Protocol E2  -  `Healthcare Systems - Enterprise`

| Q | Question | Source | Weight |
|---|---|---|---|
| E2.1 | `account_brief` describes multi-hospital IDN OR large health system? | `account_brief` | Required (gate) |
| E2.2 | $1B+ revenue OR >=3 hospitals per `account_brief`? | `account_brief`, `annualrevenue` | Required (gate) |
| E2.3 | EHR data center(s) + imaging archives + regional clinic networks? | `account_brief`, `recent_news_or_trigger_event` | Required (gate) |
| E2.4 | `infrastructure_profile` shows Facilities Mid-Size/Large + in-house net eng team? | `infrastructure_profile`, `account_brief` | Required (gate) |
| E2.5 | HITRUST / HIPAA in-scope systems language? | `account_brief` | Strong marker |

**Best-fit:**
- `high_90`: anchor (HCA, Ascension, CommonSpirit, Kaiser Permanente, Cleveland Clinic, NewYork-Presbyterian, Trinity Health, Adventist, Banner, Providence) + 4 of 5
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5

#### Protocol E3  -  `Retail and Distribution - Enterprise`

| Q | Question | Source | Weight |
|---|---|---|---|
| E3.1 | `account_brief` describes national retailer with multi-DC corporate IT (NOT just multi-warehouse)? | `account_brief` | Required (gate) |
| E3.2 | $5B+ retail revenue OR >=100 stores per `account_brief`? | `account_brief`, `annualrevenue` | Required (gate) |
| E3.3 | `infrastructure_profile` shows Facilities Mid-Size/Large (DCs) + in-house net eng? | `infrastructure_profile`, `account_brief` | Required (gate) |
| E3.4 | Direct carrier contracts (NOT through MSP)? | `account_brief` | Required (gate) |
| E3.5 | Multi-store + corporate IT footprint distinct from store-level networks? | `account_brief` | Strong marker |

**Tiebreaker (Watch List handling):** Restaurant chains (McDonald's, Yum, Chick-fil-A) -> Watch List, classify `Other` for now. 3PLs (XPO, GXO, J.B. Hunt) -> Other. Wholesale-only (Sysco, US Foods) -> Retail and Distribution if corporate IT matches.

**Best-fit:**
- `high_90`: anchor (Meijer canonical, Walmart, Kroger, Target, Costco, Home Depot, Lowe's, Albertsons, Publix, Tesco, Sainsbury's, Aeon, Sysco, US Foods) + 4 of 5
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5

#### Protocol E4  -  `Outsourcing Services - Enterprise`

| Q | Question | Source | Weight |
|---|---|---|---|
| E4.1 | `account_brief` describes BPO / outsourcing on ongoing operational basis (NOT project consulting)? | `account_brief` | Required (gate) |
| E4.2 | $1B+ revenue per `account_brief`? | `account_brief`, `annualrevenue` | Required (gate) |
| E4.3 | Multi-country / multi-state delivery footprints? | `account_brief`, `country`, `state` | Required (gate) |
| E4.4 | `infrastructure_profile` shows Facilities Mid-Size/Large + in-house net eng? | `infrastructure_profile`, `account_brief` | Required (gate) |
| E4.5 | NOT hard-excluded project consulting (Deloitte / McKinsey / BCG / Bain / Accenture Strategy)? | `account_brief` | Required (negative) |

**Tiebreaker (Kyndryl / NTT Data / DXC / IBM Consulting):** Use service-line analysis. Operational BPO arm dominant -> Outsourcing. Project consulting dominant -> exclude (Other). Hybrid -> classify by larger revenue line.

**Best-fit:**
- `high_90`: anchor (Cognizant, Genpact, Concentrix post-Webhelp, TaskUs, Conduent, Capgemini, Wipro BPS, TCS BPS, Infosys BPM, HCL Tech, Teleperformance, Atento, Sutherland, Firstsource borderline) + 4 of 5
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5
- `Flagged for deletion`: project consulting only (Deloitte, McKinsey, BCG, Bain, Accenture Strategy)

#### Protocol G  -  `Greenfield` (cross-segment: pairs with `Data Center Colo Provider` OR `NeoCloud` parent)

**Definition:** Pre-operational or actively-in-build colocation or neocloud companies. Series A-C funded, sites under construction, no operational customer base yet (or only LOI customers).

| Q | Question | Source | Weight |
|---|---|---|---|
| G.1 | `account_brief` describes pre-operational status OR active build-out of new colo / neocloud infrastructure? | `account_brief` | Required (gate) |
| G.2 | `recent_news` mentions funding round (Series A/B/C) announced in last 24 months? | `recent_news_or_trigger_event` | Required |
| G.3 | `recent_news` mentions sites under construction (groundbreaking, "first site," planned operational date)? | `recent_news_or_trigger_event` | Required (gate) |
| G.4 | `infrastructure_profile` shows Facilities Small (<5  -  1-4 sites under construction) + Route Miles None Identified + POPs None Identified or Small? | `infrastructure_profile` | Strong marker |
| G.5 | NOT yet operational at scale (no large operational customer base, <2 operational sites)? | `account_brief` | Required |

**Customer_segment parent + future migration target:**
- Greenfield + announced AI/GPU tenant or liquid cooling at planned site -> `Data Center Colo Provider` parent / future migration to `AI Signals - colo`
- Greenfield + announced distributed modular pod model -> `Data Center Colo Provider` parent / future migration to `Modular - colo`
- Greenfield + announced hyperscaler anchor + 10MW+ deployment at first site -> `Data Center Colo Provider` parent / future migration to `Hyperscale Wholesale - colo`
- Greenfield + announced GPU compute service / neocloud launch -> `NeoCloud` parent / future migration to `Large Scale GPU - Neocloud` or `AI Infrastructure providers - Neocloud`
- Greenfield + Bitcoin mining history + AI pivot announcement -> NC5 `Crypto to AI - Neoclouds` (NOT Greenfield)

**Best-fit:**
- `high_90`: G.1 + G.2 + G.3 all confirmed + clear customer_segment parent
- `medium_7089`: 4 of 5
- `low_5069`: 3 of 5
- `Flagged for deletion`: G.2 + G.3 both fail (no recent funding, no construction announcement)

**Auto-migration trigger (R2 responsibility):** See §7 below for the expanded operational-milestone pattern catalog.

---

## 6a. NC1 vs NC3 vs NC2 boundary  -  deterministic threshold matrix

The most-frequently-mis-classified NeoCloud boundary. Use this table to decide between `Large Scale GPU - Neocloud` (NC1), `AI Infrastructure providers - Neocloud` (NC3), and `Tier 1 Inference - Neocloud` (NC2) before falling back to question scoring.

| Axis | NC1 Large Scale GPU | NC3 AI Infrastructure providers | NC2 Tier 1 Inference |
|---|---|---|---|
| **Disclosed GPU MW capacity** | >=50MW | <50MW (typically 1-20MW) | Variable (often <20MW, edge POPs) |
| **GPU-capable facility count** | >=10 | <10 (typically 3-8) | 20-50+ (edge cities, carrier hotels) |
| **Primary pricing model** | Reserved-instance / multi-week-or-month / per-cluster commit | Per-GPU-hour on-demand (primary) | Per-million-tokens (API-based inference) |
| **Customer profile** | Named hyperscaler/enterprise training contracts (NVIDIA, OpenAI, Microsoft, Anthropic) | Developer-mix + SMB AI startups + research labs | Application developers consuming inference API |
| **Workload type** | Distributed training (multi-week jobs, 1K+ GPU clusters) | Mixed training + fine-tuning + inference; smaller clusters | Inference-as-a-service, low-latency token streaming |
| **Network architecture** | InfiniBand or Ultra Ethernet GPU-to-GPU clustering (sub-microsecond) | Standard datacenter Ethernet; no custom interconnect | Distributed edge POPs; cloud peering for inference traffic |
| **SLA pattern** | Cluster uptime + scheduling | On-demand availability | Sub-100ms p95 token latency |
| **Anchor examples** | Nebius, Lambda Labs, Voltage Park, CoreWeave (NOTE: Crusoe routes to NC5 due to Bitcoin-mining heritage) | Vultr, DigitalOcean GPU, Fluidstack, Modal, RunPod, OVHcloud, Scaleway, Linode (Akamai) | Together.ai, Groq, Cirrascale, DeepInfra, Fireworks AI, SambaNova, Baseten (NOTE: Mistral La Plateforme is a boundary `medium_7089` case - foundation-model lab with own inference API. Sakana AI is NOT an anchor - it is an AI research/model company that consumes GPU compute, not provides it; route to `Other`.) |

**Decision rule (apply in order):**

1. If pricing model is **per-million-tokens** primary AND distributed edge POPs in 20+ cities AND sub-100ms token-latency SLA -> NC2 Tier 1 Inference
2. Else if (disclosed GPU capacity >=50MW) AND (10+ GPU-capable facilities) AND (reserved-instance / multi-week pricing OR named hyperscaler training contract) -> NC1 Large Scale GPU
3. Else if mid-market cloud (5-30 locations) AND per-GPU-hour on-demand pricing AND broad customer mix (existing non-GPU cloud products) -> NC3 AI Infrastructure providers
4. Else if Bitcoin mining history confirmed -> NC5 Crypto to AI - Neoclouds
5. Else if explicit sovereign positioning + national-program affiliation -> NC4 Sovereign AI Clouds
6. Else -> Apply protocol question scoring (best-fit) with `low_5069` and route to D7

**Boundary cases (low_5069 with D7 re-validation):**
- Voltage Park: ~24K H100 GPUs at ~20-30MW. Anchor-tagged NC1 (Phase B research) but borderline NC3 by raw MW. Tiebreaker: named hyperscaler training customer base + multi-week-contract pricing model -> stays NC1.
- DigitalOcean (post-Paperspace acquisition 2023): mid-market cloud adding GPU. Stays NC3  -  per-GPU-hour primary + broad customer mix.
- OVHcloud: GPU compute in 5 European DCs, sovereignty messaging mixed. NC4 if sovereign positioning dominant, else NC3.
- Scaleway: GPU compute + sovereignty undertones (French/EU positioning). NC4 if Scaleway markets sovereignty primary, else NC3.
- RunPod: rapidly growing, ~5-10 facilities, per-GPU-hour primary. NC3 unless disclosed capacity passes 50MW.

**Crypto to AI override:** Any record with verifiable Bitcoin mining history goes to NC5 regardless of current MW/facility count (IREN has 200MW+ and would otherwise score NC1, but mining history routes to NC5 per Cooper 2026-05-14).

### Confidence thresholds (per protocol, applied uniformly)

- `high_90`: anchor match (from file 06 §6 list) OR all required questions confirmed
- `medium_7089`: 3-4 of 5 required questions confirmed
- `low_5069`: 2 of 5 required questions confirmed (R2 + D7 re-validate)
- `Flagged for deletion`: 0-1 required questions confirmed AND no other sub-segment fits
- `manual_review_required`: clear positive evidence for 2+ sub-segments AND tiebreaker fails (rare - target <5%)

### Specific tiebreakers (file 06 §6 + §11)

- **Tata Communications, Lumen Technologies (drift toward Pure Wholesale post-divestitures):** by dominant revenue line in account_brief.
- **Equinix parent vs xScale child:** parent record -> `Standard - colo` by majority revenue; xScale child record (if separate) -> `Hyperscale Wholesale - colo`. Same logic for Vantage, Aligned, NTT, Iron Mountain, QTS split-book operators. NO manual_review default for parent records.
- **Crypto-to-AI vs AI Signals colo vs Large Scale GPU:** Bitcoin mining history confirmed -> `Crypto to AI - Neoclouds` (regardless of operator vs landlord). No mining history + landlord -> AI Signals colo. No mining history + operator with multi-facility GPU -> Large Scale GPU.
- **CVS / UnitedHealth / McKesson:** dominant revenue line. CVS retail-pharmacy + insurance hybrid -> if retail-pharmacy revenue dominant -> Retail and Distribution; if insurance/PBM dominant -> Financial Services. UnitedHealth parent (insurer) -> Financial Services; Optum split as separate record. McKesson/Cardinal/AmerisourceBergen (pharma distribution) -> Healthcare Systems.
- **Master Agent vs TSD boundary:** >=100 sub-agents AND >=$1B gross billings -> TSD; otherwise Master Agent (no default manual_review).
- **IT integrators (CDW, Insight, WWT, ePlus) - Managed Network Services vs Cloud + Telecom Hybrid:** cloud revenue >=30% + AWS Premier/Azure Expert partner -> Cloud + Telecom Hybrid; otherwise Managed Network Services.
- **Pure subsea consortium (FLAG, SEA-ME-WE, ACE, EIG) without operating entity:** D1.4 disqualifier (NOT Subsea cable operator) - they're not sellable entities.

## 7. Greenfield auto-migration rule (special handling)

Greenfield is a TIME-BASED status, not a permanent sub-segment. R2 watches for operational-status transitions and re-classifies.

### 7.1 Operational milestone detection patterns (R2 reads `recent_news_or_trigger_event`)

R2 performs case-insensitive substring match against the patterns below. Match on ANY pattern in a tier triggers the corresponding action.

**Tier 1  -  operational milestone (migrate to operational sub-segment):**

```
first site operational | first site live | site goes live | site is live
first customer live | first tenant live | first tenant move-in | first move-in
ribbon cutting | grand opening | site commissioning | commissioning ceremony
powered shell delivered | powered on | first power | energization complete
first revenue | revenue milestone | revenue generating | first paying customer
first customer move-in | tenants begin moving in | tenant operations begin
operational launch | service launch | commercial launch | service availability
ribbon-cutting | go-live | goes live | went live
first deployment | first workload | first cluster online | first cluster operational
phase 1 operational | phase 1 complete | phase 1 live
campus operational | campus opens | campus open
```

**Tier 2  -  abandonment / failure (migrate to `Flagged for deletion`):**

```
abandoned project | abandoned the project | project abandoned
funding pulled | funding withdrawn | lost funding | failed to secure funding
bankruptcy | Chapter 11 | Chapter 7 | files for bankruptcy | filed bankruptcy
liquidation | wind down | winding down | ceasing operations | shut down
project cancelled | project canceled | construction halted | construction stopped
permit denied | permit revoked | utility interconnection denied
investor pullback | board terminated | foreclosure on site
```

**Tier 3  -  construction-progress signals (REMAIN Greenfield; re-validate at next R2 cycle):**

```
under construction | construction underway | groundbreaking | breaking ground
permit filed | permit approved | permit granted | site plan approved
utility interconnection | substation construction | power agreement signed
construction progress | site selection | site prep | site preparation
zoning approval | zoning approved | environmental review complete
funding round closed | Series B closed | Series C closed | new funding announced
```

**Tier 4  -  stalled greenfield (migrate to `Flagged for deletion`):**

- Greenfield record AND no Tier 1 or Tier 3 signal in `recent_news_or_trigger_event` in last 18 months AND no construction progress AND no operational sites -> `Flagged for deletion` (stalled greenfield).
- Greenfield record AND `last_signal_date` > 18 months ago AND no D7 escalation in last 90 days -> route to D7 for manual operational-status verification (D7 web-research check before evicting).

### 7.2 R2 action matrix

| Greenfield record state | Trigger | R2 action | last_enriched_date bump? |
|---|---|---|---|
| Tier 1 milestone matched | Operational signal | Re-run Stage 3 protocols -> migrate to operational sub-segment (`AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo`, `Standard - colo`, `Large Scale GPU - Neocloud`, `AI Infrastructure providers - Neocloud`, `Tier 1 Inference - Neocloud`, `Sovereign AI Clouds - Neocloud`) | YES |
| Tier 2 abandonment matched | Failure signal | Migrate to `customer_segment = "Flagged for deletion"`; clear `company_sub_segment` | YES |
| Tier 3 construction progress | Active build signal | Remain Greenfield; refresh `recent_news_or_trigger_event`; re-validate in 120 days | NO |
| Tier 4 stalled (>18 mo silence) | No signals in window | Route to D7 manual operational-status verification first; D7 web-fetches the company website + funding news; if verified stalled -> `Flagged for deletion` | NO (R2); YES (D7 on resolution) |
| Bitcoin mining history + AI pivot announced | NC5 path triggered | Migrate to `NeoCloud` / `Crypto to AI - Neoclouds` (NOT operational colo/neocloud sub-segment) | YES |

### 7.3 D7 fallback (safety net for missed migrations)

D7 Edge Case Resolution weekly routine treats Greenfield records as a P2 priority cohort:

- Pull all Greenfield records where `last_enriched_date` > 180 days OR `recent_news_or_trigger_event` is blank / >90 days stale
- Deep web research per record (5-10 `web_fetch` calls to company website + funding news + datacenter trade press)
- If operational status confirmed -> migrate to operational sub-segment
- If stalled/failed/abandoned confirmed -> `Flagged for deletion`
- If still genuinely greenfield -> refresh `recent_news_or_trigger_event` with current construction status, remain Greenfield

D7 covers the cases R2's string-match misses (euphemistic language, foreign-language press, smaller-trade-press coverage).

### 7.4 Structured field deferred decision

A structured `operational_site_count` field was considered but deferred (Cooper, 2026-05-14). String-match patterns in §7.1 + D7 fallback in §7.3 + 120-day R2 cadence + 14-day max for `manual_review_required` are sufficient for steady-state Greenfield handling. Revisit if Greenfield mis-classification rate exceeds 10% of the population at quarterly anchor refresh (next: 2026-08-14).

R2 logs every migration with a reasoning string citing which Tier-N pattern matched and writes a HubSpot note documenting the operational status change.

## 8. End-of-pipeline verification queries (4 self-validation checks, run at end of run)

Each routine that classifies records runs these checks at end of pipeline. Failures alert Cooper.

1. **Sub-segment nullness check:** if `customer_segment` IN (6 ICPs) AND `company_sub_segment` IS NULL -> set `customer_segment = "Flagged for deletion"` with reasoning "No sub-segment fit; not ICP." Do NOT silently leave null.

2. **Confidence-evidence alignment check:** if `segmentation_confidence = high_90` -> confirm reasoning string includes named anchor match OR "all N required questions confirmed." If alignment fails, downgrade to `medium_7089`.

3. **Disqualifier audit check:** if `customer_segment = "Other"` -> confirm reasoning cites a D1 rule (`D1.<class>.<rule>`). If not, escalate to D7 edge-case-resolution queue.

4. **Framework default guard check:** if `company_sub_segment` IN (`Regional CLEC - Fiber operator`, `Standard - colo`, `Telecom Aggregator - MSP`) -> confirm positive-evidence questions confirmed. If only negative-exclusion (no other sub-segment matched), downgrade to `low_5069` and route to R2 + D7 for verification.

5. **Best-fit verification:** confirm Stage 3 selected the sub-segment with the highest POSITIVE evidence count. If 2+ sub-segments have similar positive evidence (no tiebreaker resolved), set `manual_review_required` (rare; expected <5%).

6. **Manual review queue cap:** if `manual_review_required` exceeds 5% of records reviewed in any single run, alert Cooper - protocol bug, not real ambiguity rate.

## 9. Cross-skill verification (crm-hygiene weekly audit)

`crm-hygiene` SKILL runs weekly to catch records that escaped Stage 5 enforcement (defense in depth):

- Records on framework default sub-segments (Regional CLEC / Standard - colo / Telecom Aggregator) without positive-evidence reasoning string -> flag for R2 re-enrichment
- Records on `manual_review_required` for >14 days -> route to D7 edge-case-resolution (hard rule)
- Records on `low_5069` for >60 days without R2 touch -> flag for R2
- Records with `segmentation_confidence` written but no reasoning string -> flag for R2 re-enrichment

## 10. Audit string format

Every classification or tier write produces a reasoning string that explicitly cites the file 06 rule:

```
Phase X.Y / R1 / R2 / R0 Enrichment classification on YYYY-MM-DD by <routine>

D1 Disqualifier check: PASS (no match) | FAIL (D1.<class> matched: <evidence>)
D2 Wholesale-arm policy: <single record | parent + child | wholesale arm record>
D3 Flowchart traversal: <segment flowchart, decisions 1 -> ... -> leaf>
D5 Protocol applied: <protocol ID, e.g., N1, F4, NC5, G>
Primary fields read:
  account_brief: <yes/no - version timestamp>
  infrastructure_profile: <yes/no - values present>
  recent_news_or_trigger_event: <yes/no - most recent signal>
Questions answered: <count/total>
  Q1: <answer>
  Q2: ...
Infrastructure_profile pattern match: <matches canonical / partial / mismatches>
Best-fit verdict: <sub_segment_value>
Tiebreaker applied (if any): <name + reasoning>
Confidence: <high_90 | medium_7089 | low_5069 | manual_review_required>
Confidence reasoning: <e.g., "All 5 N1 questions confirmed; anchor match Verizon; infrastructure_profile matches Tier 1 canonical">

Action:
  customer_segment <old> -> <new>
  company_sub_segment <old> -> <new>
  segmentation_confidence <old> -> <new>
  account_brief: updated (if newer/better than existing)
  infrastructure_profile: updated (if newer evidence)
  recent_news_or_trigger_event: updated (if new signal)

Routine: <name>
Session: <ID>
```

## 11. Quarterly anchor refresh

Per Cooper RevOps calendar, quarterly:

1. Re-validate the top 20 records per sub-segment against the protocols.
2. Verify anchor companies still match archetype (no acquisitions / pivots / divestitures invalidating them).
3. Update file 06 anchor lists with corrections.
4. If >10% of top-20 per sub-segment drift -> root-cause investigation.

Next refresh: 2026-08-14.

## 12. See-also

- File 06 (`context/account-tiering/sub-segment-qualification-full.md`) - sub-segment definitions, anchors, confidence rules, D1+D2+D3 references. Quarterly anchor refresh source.
- `context/account-tiering/tier-compute-spec.md` - tier computation algorithm (Stage 4)
- `context/account-tiering/sub-segment-qualification.md` - short pointer to file 06
- `context/hubspot/property-schema.md` - full property schema (case-sensitivity, enriched fields, signal persistence fields)
- `context/hubspot/hubspot-values.md` - exact case-sensitive internal values

**This file is self-contained as of 2026-05-14.** All 30 D5 protocol question tables (one per sub-segment) are inlined in §6; NC threshold matrix is in §6a; Greenfield patterns are in §7.
