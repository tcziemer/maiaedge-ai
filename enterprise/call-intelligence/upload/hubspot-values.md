# HubSpot Value Reference

Definitive mapping from internal classification to exact HubSpot property values.
All output must use these exact strings -- case-sensitive, no variations.

---

## Company Properties

### customer_segment (Dropdown)

**Active values:** 10 (verified via HubSpot MCP 2026-05-14). 6 ICP + 4 non-ICP.

| Internal Classification | HubSpot `customer_segment` Value (internal) | Display Label | ICP? | Post-migration record count (2026-05-13) |
|---|---|---|---|---:|
| Colocation Operator | `Data Center Colo Provider` | Colocation Provider | ICP | 503 |
| Neocloud | `NeoCloud` | Neocloud | ICP | 156 |
| Fiber Operator | `Fiber Operator` | Fiber Operator | ICP | 1,376 |
| Network Operator | `Network Operator(Tier 1 / VNO)` (NO space before paren) | Network Operator | ICP | 315 |
| MSP/Aggregator | `MSP/Aggregator` | MSP/Aggregator | ICP | 345 |
| Enterprise (Multi-DC ICP) | `Enterprise-CustomerSegment` | Enterprise | ICP | 5 |
| Partner | `Partner Target` | Partner Target | non-ICP | 192 |
| Software/Platform Vendor / hyperscaler / equipment vendor / etc. | `Other` | Other | non-ICP | 269 |
| Pre-classification | `Unknown` | Unknown | non-ICP | 8 |
| Pre-deletion holding | `Flagged for deletion` | Flagged for deletion | non-ICP | 179 |

> **COMPANION FIELD:** Every write of `customer_segment = "Flagged for deletion"` MUST also set `flagged_for_deletion_reason` (multi-line text, Company object) in the same update. Lead the value with one of the 7 canonical reason codes, then a colon and one concrete sentence of evidence: `Dead domain` / `Hard junk / non-business` / `D1 disqualified (no reference value)` / `No ICP fit` / `Duplicate (merged)` / `Defunct / out of business` / `Stalled greenfield`. Clear the field to empty if the record is ever moved back off `Flagged for deletion`. Full spec + examples in `context/hubspot/property-schema.md` §2.1.

> **IMPORTANT:** `AI - Colocation Operator` is NO LONGER a main segment. Use `Data Center Colo Provider` + `company_sub_segment = AI Signals - colo` instead. The `NeoCloud` value is its own segment -- do NOT map to `Colocation Operator`.

> **IMPORTANT (May 2026):** `Enterprise-CustomerSegment` is now an ICP segment (priority 5 - lowest of the ICPs but qualified). Scope is multi-DC enterprises with in-house network engineering teams. Always pair with one of the four `company_sub_segment` values: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Records that fail the vertical or scale gate stay as `Other` or `Unknown`.

### company_sub_segment (Dropdown)

**Property name:** `company_sub_segment`
**Type:** Enumeration (single-select)
**Active values:** 30 (verified via HubSpot MCP 2026-05-14). Internal values are CASE-SENSITIVE.

Each value includes the parent segment suffix EXCEPT `Subsea cable operator` (no `- Network Op` suffix despite sitting under Network Operator parent) and `Greenfield` (cross-segment - pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` parent).

For classification logic + per-sub-segment evidence questions + tiebreaker rules, see [`context/account-tiering/sub-segment-qualification.md`](../core/sub-segment-qualification.md) -> file 06 (primary source) + [`context/account-tiering/enrichment-protocols.md`](../core/enrichment-protocols.md) (D5 v2 operational layer).

| Main Segment (`customer_segment`) | HubSpot `company_sub_segment` Value | Case-sensitivity note |
|---|---|---|
| `Network Operator(Tier 1 / VNO)` | `Tier 1 Carrier - Network Op` |  |
| `Network Operator(Tier 1 / VNO)` | `Pure Wholesale Carrier - Network Op` |  |
| `Network Operator(Tier 1 / VNO)` | `Cable MSO Enterprise Division - Network Op` |  |
| `Network Operator(Tier 1 / VNO)` | `International Backbone Specialist - Network Op` |  |
| `Network Operator(Tier 1 / VNO)` | `Subsea cable operator` | **NEW 2026-05-14.** Lowercase `c` and `o`. No `- Network Op` suffix. |
| `Fiber Operator` | `Regional CLEC - Fiber operator` | Catch-all default for ambiguous mid-size fiber. |
| `Fiber Operator` | `Long Haul / Backbone - Fiber operator` |  |
| `Fiber Operator` | `Dark Fiber Specialist - Fiber Operator` | **Capital "O"** in `Operator` - every other Fiber sub-segment uses lowercase `o`. |
| `Fiber Operator` | `Tier 2 National Wholesale - Fiber operator` |  |
| `Fiber Operator` | `Regional Cable Operator - Fiber operator` |  |
| `Fiber Operator` | `Municipal / Cooperative - Fiber operator` | Renamed from `Co-op/consortium` 2026-05-13. |
| `Data Center Colo Provider` | `Standard - colo` |  |
| `Data Center Colo Provider` | `AI Signals - colo` |  |
| `Data Center Colo Provider` | `Modular - colo` |  |
| `Data Center Colo Provider` | `Hyperscale Wholesale - colo` |  |
| `NeoCloud` | `Large Scale GPU - Neocloud` |  |
| `NeoCloud` | `Tier 1 Inference - Neocloud` |  |
| `NeoCloud` | `AI Infrastructure providers - Neocloud` | **Lowercase "p"** in `providers`. |
| `NeoCloud` | `Sovereign AI Clouds - Neocloud` |  |
| `NeoCloud` | `Crypto to AI - Neoclouds` | **Trailing "s"** on `Neoclouds`. |
| `MSP/Aggregator` | `Telecom Aggregator - MSP` |  |
| `MSP/Aggregator` | `Managed Network Services - MSP` | `- MSP` suffix post-Phase 1.7c.1 (`- Network Operator` archived 2026-05-13). |
| `MSP/Aggregator` | `TSD Technology Services Distributor - MSP` |  |
| `MSP/Aggregator` | `Master Agent - MSP` |  |
| `MSP/Aggregator` | `Cloud + Telecom Hybrid MSP - MSP` |  |
| `Enterprise-CustomerSegment` | `Financial Services - Enterprise` |  |
| `Enterprise-CustomerSegment` | `Healthcare Systems - Enterprise` |  |
| `Enterprise-CustomerSegment` | `Retail and Distribution - Enterprise` |  |
| `Enterprise-CustomerSegment` | `Outsourcing Services - Enterprise` |  |
| `Data Center Colo Provider` OR `NeoCloud` | `Greenfield` | **REAL sub-segment per Cooper feedback 2026-05-14.** Cross-segment - pairs with EITHER parent. For pre-operational / actively-in-build colocation or neocloud companies. |

#### Retired sub-segment values (archived 2026-05-13 Phase 1.6 - DO NOT USE)

| Retired Value | Reason | Replacement |
|---|---|---|
| `Co-op/consortium` | Renamed for clarity | `Municipal / Cooperative - Fiber operator` |
| `External Extension - Network operator` | Migrated to dedicated field | `network_op_track = external_extension` |
| `Internal + external unification - Network Operator` | Migrated to dedicated field | `network_op_track = internal_external_unification` |
| `Managed Network Services - Network Operator` (pre-Phase 1.7c.1) | Suffix renamed | `Managed Network Services - MSP` |

`import-processor` rejects writes to these values with error: `"Retired enum value - archived 2026-05-13 Phase 1.6"`.

#### Sub-Segment Assignment Rules

Best-fit classification with calibrated confidence - see [`context/account-tiering/enrichment-protocols.md`](../core/enrichment-protocols.md) for the full D5 v2 protocols. NO default `manual_review_required` (Cooper 2026-05-14).

Key tiebreakers:

- **Network Operator / Tier 1 Carrier vs Pure Wholesale Carrier vs International Backbone Specialist:** retail consumer presence in account_brief -> Tier 1 Carrier. Pure-wholesale model (no consumer/retail) -> Pure Wholesale Carrier. International-only (no domestic retail) -> International Backbone Specialist. Subsea-primary with minimal terrestrial -> Subsea cable operator (more specific).
- **Cable MSO Enterprise Division vs Regional Cable Operator (Fiber):** national cable parent AND distinct B2B brand AND B2B revenue >=$1.5B -> Cable MSO Network Op. Regional multi-state cable AND no separate B2B brand -> Regional Cable Operator Fiber.
- **Standard - colo vs AI Signals vs Hyperscale Wholesale (split-book operators - Equinix, Vantage, Aligned, NTT, Iron Mountain, QTS):** parent record -> `Standard - colo` by majority revenue. xScale child record (if separate) -> `Hyperscale Wholesale - colo`. Same logic for Vantage, Aligned, NTT, Iron Mountain, QTS. NO manual_review default for parent records.
- **Crypto to AI - Neoclouds (Cooper 2026-05-14: inclusive of operator AND landlord):** Bitcoin mining history confirmed -> Crypto to AI - Neoclouds (regardless of current business model). No mining history + landlord-only with GPU tenants -> AI Signals - colo. No mining history + operator-only with multi-facility GPU compute -> Large Scale GPU - Neocloud.
- **Greenfield + announced AI/GPU tenant or liquid cooling at planned site:** Greenfield (Colo) with future migration target = AI Signals colo. Greenfield + announced distributed modular pod model -> Greenfield (Colo) -> Modular colo. Greenfield + Bitcoin mining history + AI pivot announcement -> Crypto to AI - Neoclouds (not Greenfield).
- **TSD vs Master Agent boundary:** >=100 sub-agents AND gross billings >=$1B -> TSD. Otherwise Master Agent (Cooper 2026-05-14: no default manual_review - classify best-fit with calibrated confidence; `low_5069` acceptable for thin anchor verification).
- **IT integrators (CDW, Insight, WWT, ePlus) - Managed Network Services vs Cloud + Telecom Hybrid:** AWS Premier / Azure Expert / GCP Premier partner status + cloud revenue >=30% -> Cloud + Telecom Hybrid. Network services dominant AND cloud <30% -> Managed Network Services.
- **CVS / UnitedHealth / McKesson (Enterprise diversified):** dominant revenue line. CVS retail-pharmacy + insurance hybrid -> retail-pharmacy revenue dominant -> Retail and Distribution; insurance/PBM dominant -> Financial Services. UnitedHealth parent -> Financial Services (insurer); Optum split as separate record. McKesson/Cardinal/AmerisourceBergen (pharma distribution) -> Healthcare Systems.
- **Pure subsea consortia (FLAG, SEA-ME-WE 4/5/6, ACE, EIG):** D1.4 disqualifier - not sellable entities. Route to `customer_segment = "Other"`, NOT Subsea cable operator.
- **NaaS Platform Operators (Cooper 2026-05-14):** classify as `customer_segment = "Other"` (competitive reference) or `Flagged for deletion` (no value). NO MSP/Aggregator sub-segment.

**Enterprise hard gate (BOTH must pass):** vertical gate (one of the four sub-segments) AND scale gate ($1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering team via NOC presence or VP Network / Principal Network Engineer / Director Network Engineering job postings)). **Hard disqualifiers:** network fully outsourced to single MSP, single DC or single geography, no direct carrier contracts, pure SaaS without owned DCs. **Out of scope (Watch List):** Manufacturing, Energy and Utilities, Logistics and Supply Chain, restaurant chains. Government/Defense FedRAMP-gated.

### infrastructure_profile (Multi-select)

Select ONE value per dimension where data exists. Semicolon-separated in output.

```
Facilities: Small (<5)
Facilities: Mid-Size (5-19)
Facilities: Large (20-49)
Facilities: Enterprise (50+)
Route Miles: Small (<1K)
Route Miles: Mid-Size (1K-10K)
Route Miles: Large (10K-50K)
Route Miles: Enterprise (50K+)
POPs: Small (<10)
POPs: Mid-Size (10-49)
POPs: Large (50-99)
POPs: Enterprise (100+)
```

Bucketing rules:
- Data Centers: 50+ = Enterprise, 20-49 = Large, 5-19 = Mid-Size, <5 = Small
- Fiber Route Miles: 50K+ = Enterprise, 10K-50K = Large, 1K-10K = Mid-Size, <1K = Small
- POPs: 100+ = Enterprise, 50-99 = Large, 10-49 = Mid-Size, <10 = Small
- No metrics found = `None Identified`

### fabric_provisioning_approach (Multi-select)

Select ALL that apply. Semicolon-separated in output.

**External NaaS Fabrics:**
- `Megaport`
- `PacketFabric`
- `Equinix ECX Fabric`
- `Console Connect`
- `Other External NaaS`

**Competitor Fabric Solutions:**
- `Lumen Private Connectivity Fabric`
- `Other Competitor Fabric`

**Internal Approach:**
- `Homegrown/Proprietary Platform`
- `Standard OSS/BSS Stack`
- `Manual/Legacy Processes`

**No Capability:**
- `None Identified`

### hyperscaler_proximity (Dropdown)

```
Announced: <50 miles
Announced: 50-200 miles
Existing Facility Nearby
None Known
```

### account_tier (Dropdown)

| Internal Value | Display Label | Meaning |
|---|---|---|
| `tier_1` | Tier 1 | Highest priority - white-glove rep weekly attention |
| `tier_2` | Tier 2 | Strong ICP fit - rep 1:1 attention |
| `tier_3` | Tier 3 | Qualified but smaller scale or medium confidence - BDR/mass outreach |
| `tier_4` | Tier 4 | Low confidence or signal-quiet - nurture |
| `tier_5` | Tier 5 | Lowest priority - mass outreach / nurture only |

> **Note:** Tier 1 = HIGHEST priority. Inverted from HubSpot's default description.

**Computed by `compute_tier()`** - see [`context/account-tiering/tier-compute-spec.md`](../account-tiering/tier-compute-spec.md) for the canonical algorithm, defaults table (30 sub-segment rows), signal modifiers (6), null + unknown-pair fallbacks, and manual override behavior. Every routine that writes tier (R1, R2, Weekly Signal Scan Stage 5b, R6, R-Tier-Audit weekly, D7 weekly) inlines that spec.

Manual override: `hs_is_target_account = true` freezes `account_tier` ONLY. Segment / sub-segment / signal field / enriched field writes proceed normally.

### segmentation_confidence (Dropdown)

| Internal Value | Display Label | Confidence |
|---|---|---|
| `high_90` | High (90%+) | Anchor match (from file 06 §6 anchor list) OR all required protocol questions confirmed |
| `medium_7089` | Medium (70-89%) | 3-4 of 5 required protocol questions confirmed |
| `low_5069` | Low (50-69%) | 2 of 5 required protocol questions confirmed (R2 + D7 re-validate) |
| `manual_review_required` | Manual Review Required | Clear positive evidence for 2+ sub-segments AND tiebreaker fails. **Last resort, NOT default** (Cooper 2026-05-14). Target <5% of records. |

D7 weekly edge-case-resolution routine processes the manual_review_required queue. Hard rule: nothing stays in manual_review_required more than 14 days - D7 either upgrades to a resolved classification or evicts to `Flagged for deletion`.

### network_op_track (Dropdown)

**Active values:** 2 (verified via HubSpot MCP 2026-05-14). 678 records populated post-Phase 2.7 migration. Replaces retired sub-segment values (`External Extension - Network operator`, `Internal + external unification - Network Operator`).

| Internal Value | Display Label | Messaging Track | What to detect |
|---|---|---|---|
| `external_extension` | External Extension (Track A) | Lead with cross-carrier extension | Homegrown/proprietary platform in `fabric_provisioning_approach`; sophisticated internal OSS/BSS; portal/API/self-service visible |
| `internal_external_unification` | Internal + External Unification (Track B) | Lead with internal unification first | Manual/Legacy Processes in `fabric_provisioning_approach`; no portal; manual quoting / circuit ordering |

Track value is retained on records even after their `customer_segment` or `company_sub_segment` changes (e.g., Spectrum, Stealth Communications still carry track values after their sub-segment moved).

### Signal Persistence Fields

Populated by Weekly Signal Scan Stage 5b. Consumed by `compute_tier` modifiers.

| Property | Type | Description |
|---|---|---|
| `last_signal_score` | Number | Highest signal score in last 60d. Drives hot (-1, 27-44) and white-hot (-2, >=45) tier modifiers. |
| `last_signal_date` | Date (YYYY-MM-DD) | Date of most recent signal scoring >=8. Drives stale (+1, >90d) and sustained quiet (+1, >180d) modifiers. |
| `signal_count_last_30d` | Number | Count of signals scoring >=8 in last 30d. Drives stacked signals (-1) modifier when >=2. |

### hs_is_target_account (Boolean - HubSpot built-in ABM)

| Internal Value | Display Label | Effect |
|---|---|---|
| `true` | True | Freezes `account_tier` ONLY. Segment / sub-segment / signal field / enriched field writes proceed normally. |
| `false` | False | Algorithmic tier control resumes. |

382 records carry `true` post-migration 2026-05-13. Renamed from legacy `target_account` to HubSpot's built-in `hs_is_target_account` 2026-05-13.

### Enriched Text Fields (the 8 the enrichment bot populates)

Per Cooper 2026-05-14: enrichment bot populates 8 fields during Stage 1b research BEFORE classification (Stages 2-3). **Conciseness cap: 2-4 sentences each** on narrative fields. `maiaedge_value_proposition` is OUT OF ENRICHMENT SCOPE - populated by outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) on-demand at outreach time. See `context/account-tiering/enrichment-protocols.md` for the full operational layer.

| Property | Type | Length cap | Owner | Description |
|---|---|---|---|---|
| `account_brief` | String | 2-4 sentences (Cooper 2026-05-14; overrides prior 3-6 sentence hint in HubSpot description) | Enrichment bot | Company overview - what they do, who they serve, notable context. Primary narrative source for classification. Excludes geography. |
| `geographic_focus` | String | 1-2 sentences / 1 line | Enrichment bot | Natural language scope (e.g., "HQ: Washington \| Scope: Global \| 4 states"). |
| `provisioning_landscape` | String | 2-4 sentences | Enrichment bot | Narrative companion to `fabric_provisioning_approach` - platforms / tools / processes the operator uses + messaging angle. |
| `recent_news_or_trigger_event` | String | 2-4 sentences, **pure narrative** (no date prefix post-2026-05-28; event date lives in `last_signal_date`) | Enrichment bot (Signal Scan partial writes also touch this field; 5 outreach skill push-backs write at outreach time per CLAUDE.md Operating Principle #12) | Most recent news / funding / leadership / signal. Surfaces Greenfield funding rounds, M&A drift, anchor drift, operational-status transitions. |
| `last_enriched_date` | **Date** (HubSpot date-type, verified live 2026-05-14; accepts/returns YYYY-MM-DD strings in search API) | YYYY-MM-DD | Enrichment bot (auto-populated at Stage 5 on a passing definitive gate per CLAUDE.md Unified Stamping Policy) | Gates R2 120-day re-enrichment cadence. |
| `infrastructure_profile` | Enumeration (multi-select; see above) | Enum | Enrichment bot | PRIMARY structured classification signal. Each sub-segment has a canonical pattern in `context/account-tiering/enrichment-protocols.md` §4. |
| `hyperscaler_proximity` | Enumeration (see above) | Enum | Enrichment bot | Primarily Colocation classification signal. |
| `fabric_provisioning_approach` | Enumeration (multi-select; see above) | Enum | Enrichment bot | Detects Network Op Track A vs Track B + competitor adoption. |

### Outreach-time Field (NOT in enrichment scope)

| Property | Type | Length cap | Owner | Description |
|---|---|---|---|---|
| `maiaedge_value_proposition` | String | 4-5 sentence email body, 500 char cap | **Outreach skills only** (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) | Copy-paste-ready email body synthesizing prospect situation + problem + MaiaEdge solution + proof. Tailored to `customer_segment`-specific messaging template + enriched-field personalization. **Enrichment bot does NOT write this field** (Cooper 2026-05-14: "we figure this out when we are doing outreach to them anyways"). Populated on-demand at outreach time when value_prop is empty OR stale (>90 days). Does NOT bump `last_enriched_date`. |

---

## Deal Properties

### dealstage (Dropdown)

| Internal Value | Display Label |
|---|---|
| `appointmentscheduled` | Appointment Scheduled |
| `qualifiedtobuy` | Discovery & Scoping |
| `presentationscheduled` | POC & Technical Validation |
| `1996673735` | Quote Provided |
| `decisionmakerboughtin` | Price Agreement & Final Configuration |
| `contractsent` | Contract Review |
| `closedwon` | Closed Won |
| `closedlost` | Closed Lost |

### dealtype (Dropdown)

| Internal Value | Display Label |
|---|---|
| `newbusiness` | New Logo |
| `existingbusiness` | Expansion |
| `Renewal` | Renewal |
| `Partnership` | Partnership |

### deal_source (Dropdown)

| Internal Value | Display Label |
|---|---|
| `trade_show` | Trade Show |
| `founder_network` | Founder Network |
| `inbound` | Inbound |
| `outbound` | Outbound - Email |
| `Outbound - Call` | Outbound - Call |
| `partner_referral` | Partner Referral |
| `other` | Other |

### bandwidth_tier (Dropdown)

| Internal Value | Display Label |
|---|---|
| `p_10_gbps` | 10 Gbps |
| `p_100_gbps` | 100 Gbps |
| `tbd` | TBD |

### deployment_timeline (Dropdown)

| Internal Value | Display Label |
|---|---|
| `all_at_once_30_days` | All at once (<30 days) |
| `phased_13_months` | Phased: 1-3 months |
| `phased_36_months` | Phased: 3-6 months |
| `phased_612_months` | Phased: 6-12 months |
| `ongoing_as_sites_added` | Ongoing as sites added |

### quote_status (Dropdown)

| Internal Value | Display Label |
|---|---|
| `request_approval` | Approval request |
| `approved` | Approved |
| `changes_requested` | Changes requested |
| `sent` | Sent |

### poc_objective (Dropdown)

| Internal Value | Display Label |
|---|---|
| `Fiber Monetization` | Fiber Monetization |
| `Speed to Revenue` | Speed to Revenue |
| `Network Extension` | Network Extension |
| `Private Connectivity Validation` | Private Connectivity Validation |
| `Competitive Displacement` | Competitive Displacement |

### infrastructure_in_scope (Multi-select)

| Internal Value | Display Label |
|---|---|
| `dark_fiber_strands` | Dark fiber strands |
| `metro_rings__regional_fiber_routes` | Metro rings / regional fiber routes |
| `spare_fiber_capacity` | Spare fiber capacity |
| `longhaul__backbone_routes` | Long-haul / backbone routes |
| `data_center_facilities__colos` | Data center facilities / colos |
| `meetme_rooms` | Meet-me rooms |
| `tenant_crossconnects` | Tenant cross-connects |
| `cloud_onramps_awsazuregcp` | Cloud on-ramps (AWS/Azure/GCP) |
| `leased_type2_circuits` | Leased type-2 circuits |
| `virtual_overlay_networks` | Virtual overlay networks |
| `iru__longterm_leases` | IRU / long-term leases |
| `multicarrier_aggregation` | Multi-carrier aggregation |
| `upstream_provider_partnerships` | Upstream provider partnerships |
| `regional_fiber_operator_partnerships` | Regional fiber operator partnerships |
| `networktonetwork_interconnects_nnis` | Network-to-network interconnects (NNIs) |
| `campus__multibuilding_connectivity` | Campus / multi-building connectivity |
| `private_wan_sites` | Private WAN sites |
| `data_center_interconnects_dci` | Data center interconnects (DCI) |
| `hybrid_owned__leased` | Hybrid (owned + leased) |

### wholesale_vs_retail_mix (Dropdown)

| Internal Value | Display Label |
|---|---|
| `mostly_wholesale_70` | Mostly wholesale (>70%) |
| `balanced` | Balanced |
| `mostly_retail_70` | Mostly retail (>70%) |
| `unknown` | Unknown |

---

## Contact Properties

### customer_segment (Dropdown)

Same values as company `customer_segment`. See Company Properties section above.

### lifecyclestage (Dropdown)

| Internal Value | Display Label |
|---|---|
| `subscriber` | Prospect |
| `lead` | Lead |
| `2098366179` | Engaged |
| `marketingqualifiedlead` | Marketing Qualified Lead |
| `salesqualifiedlead` | Sales Qualified Lead |
| `opportunity` | Opportunity |
| `customer` | Customer |
| `2099121898` | Unqualified - bad fit |
| `other` | Other |

---

## POC Ticket Properties

### hs_pipeline_stage (Ticket Status)

| Internal Value | Display Label |
|---|---|
| `1` | POC Requested |
| `2` | Scoping |
| `2203327170` | Criteria Approved |
| `2203327171` | Configuration Locked |
| `2611948268` | Building & Preparing for Shipment |
| `3329075934` | Shipped |
| `3329085138` | Customer Testing |
| `3329075912` | On Hold |
| `2203327172` | POC Successful |
| `2203327173` | POC Unsuccessful |

### poc_trend (Dropdown)

| Internal Value | Display Label |
|---|---|
| `On Track` | On Track |
| `Needs Attention` | Needs Attention |
| `At Risk` | At Risk |
| `Blocked` | Blocked |
| `On Hold` | On Hold |

### poc_approval_status (Dropdown)

| Internal Value | Display Label |
|---|---|
| `pending` | Pending |
| `approval_requested` | Approval Requested |
| `approved` | Approved |
| `conditional_approval` | Conditional Approval |
| `denied` | Denied |

### poc_number_of_sites (Dropdown)

| Internal Value | Display Label |
|---|---|
| `p_1` | 1 |
| `p_2` | 2 |
| `p_3` | 3 |
| `p_4` | 4 |
| `p_5` | 5 |

### poc_type / poc_objective (Dropdown)

Same values as deal `poc_objective`. See Deal Properties section above.

### Site Configuration Dropdowns (Same pattern for Sites 1-5)

**site_N_config_type:**
| Internal Value | Display Label |
|---|---|
| `pbc_only` | PBC Only |
| `pbc__switch` | PBC + Switch |

**site_N_power_supply_type:**
| Internal Value | Display Label |
|---|---|
| `ac` | AC |
| `dc` | DC |

**site_N_power_cable_type:**
| Internal Value | Display Label |
|---|---|
| `c13` | C13 |
| `c14` | C14 |

**site_N_fan_direction:**
| Internal Value | Display Label |
|---|---|
| `reartofront` | Rear-to-Front |
| `fronttoback` | Front-to-Back |

### infrastructure_type (Multi-select, on Tickets)

Same values as deal `infrastructure_in_scope`. See Deal Properties section above.

---

## HubSpot Import Rules

- Multi-select: Semicolons with NO spaces (`Megaport;PacketFabric` not `Megaport; PacketFabric`)
- Dropdown: Must match exactly (case-sensitive)
- Date: YYYY-MM-DD
- Text: Respect character limits (account_brief 400, geographic_focus 150, recent_trigger 250, provisioning_landscape 500, maiaedge_value_proposition 500)
- Company matching: HubSpot matches on `domain` -- no http://, no trailing slashes
