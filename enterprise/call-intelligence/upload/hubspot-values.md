# HubSpot Value Reference

Definitive mapping from internal classification to exact HubSpot property values.
All output must use these exact strings -- case-sensitive, no variations.

---

## Company Properties

### customer_segment (Dropdown)

| Internal Classification | HubSpot `customer_segment` Value |
|---|---|
| Colocation Operator | `Data Center Colo Provider` |
| Neocloud | `NeoCloud` |
| Fiber Operator | `Fiber Operator` |
| Network Operator | `Network Operator(Tier 1 / VNO)` |
| MSP/Aggregator | `Enterprise` |
| Enterprise (Dark Fiber) | `Dark Fiber - Commercial Enterprise` |
| Enterprise (Standard) | `Enterprise-CustomerSegment` |
| Software/Platform Vendor | `Other` |
| Other/Unknown | `Unknown` |

> **IMPORTANT:** `AI - Colocation Operator` is NO LONGER a main segment. Use `Data Center Colo Provider` + `company_sub_segment = AI Signals - colo` instead. The `NeoCloud` value is its own segment -- do NOT map to `Colocation Operator`.

> **MSP/Aggregator gotcha:** The HubSpot internal value is `Enterprise` (legacy naming). The display label shows "MSP/Aggregator" but imports must use `Enterprise`.

### company_sub_segment (Dropdown)

**Property name:** `company_sub_segment`
**Type:** Enumeration (single-select)

Each value includes the parent segment suffix. Use these exact strings for imports.

| Main Segment (`customer_segment`) | Sub-Segment | HubSpot `company_sub_segment` Value |
|---|---|---|
| `Data Center Colo Provider` | Standard Colocation | `Standard - colo` |
| `Data Center Colo Provider` | AI Infrastructure | `AI Signals - colo` |
| `NeoCloud` | Large-Scale GPU NeoClouds | `Large Scale GPU - Neocloud` |
| `NeoCloud` | Tier 1 Inference Providers | `Tier 1 Inference - Neocloud` |
| `NeoCloud` | AI Infrastructure Providers | `AI Infrastructure providers - Neocloud` |
| `NeoCloud` | Sovereign AI Clouds | `Sovereign AI Clouds - Neocloud` |
| `NeoCloud` | Crypto-to-AI Pivots | `Crypto to AI - Neoclouds` |
| `Fiber Operator` | Regional CLEC | `Regional CLEC - Fiber operator` |
| `Fiber Operator` | Long-Haul / Backbone | `Long Haul / Backbone - Fiber operator` |
| `Fiber Operator` | Dark Fiber Specialist | `Dark Fiber Specialist - Fiber Operator` |
| `Network Operator(Tier 1 / VNO)` | External Extension | `External Extension - Network operator` |
| `Network Operator(Tier 1 / VNO)` | Internal + External Unification | `Internal + external unification - Network Operator` |
| `Enterprise` (MSP) | Telecom Aggregator | `Telecom Aggregator - MSP` |
| `Enterprise` (MSP) | Managed Network Services | `Managed Network Services - Network Operator` |

#### Sub-Segment Assignment Rules

- **Colocation:** `AI Signals - colo` if STRONG AI signals (confirmed GPU tenants OR liquid cooling). Otherwise `Standard - colo`.
- **Neocloud:** Classify based on primary business model. See neocloud-cheatsheet.md for detailed profiles.
- **Fiber:** `Regional CLEC - Fiber operator` if <5 states and CLEC-licensed. `Long Haul / Backbone - Fiber operator` if 10K+ route miles or multi-state backbone. `Dark Fiber Specialist - Fiber Operator` if primarily dark fiber/wavelength sales.
- **Network Operator:** `External Extension - Network operator` if evidence of portal/API/self-service. `Internal + external unification - Network Operator` if no evidence of internal automation. Default External Extension if unclear.
- **MSP:** `Telecom Aggregator - MSP` if aggregates carrier circuits for wholesale. `Managed Network Services - Network Operator` if primarily managed WAN/MPLS services.

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

| Internal Value | Display Label | Enrichment Label | Criteria |
|---|---|---|---|
| `tier_1` | Tier 1 | `TIER_1_STRATEGIC` | NeoCloud (any), AI Colo (`AI Signals - colo`), or any ICP segment with trigger event + HIGH confidence |
| `tier_2` | Tier 2 | `TIER_2_CORE` | Standard Colo/Fiber/Network Op with HIGH confidence, no trigger |
| `tier_3` | Tier 3 | `TIER_3_EMERGING` | MEDIUM confidence, small-scale, or MSP/Aggregator |
| `tier_4` | Tier 4 | `UNRANKED` | LOW confidence or no clear use case signal |
| `tier_5` | Tier 5 | (manual only) | Never set by enrichment, reserved for manual assignment |

> **Note:** Tier 1 = HIGHEST priority. Inverted from HubSpot's default description.

### segmentation_confidence (Dropdown)

| Internal Value | Display Label | Confidence |
|---|---|---|
| `high_90` | High (90%+) | 90%+ clear signals |
| `medium_7089` | Medium (70-89%) | 70-89% mostly clear |
| `low_5069` | Low (50-69%) | 50-69% conflicting signals |
| `manual_review_required` | Manual Review Required | Cannot determine |

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
