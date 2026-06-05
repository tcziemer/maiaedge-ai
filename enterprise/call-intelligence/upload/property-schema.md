# MaiaEdge HubSpot Property Schema  -  Unified Reference

> Last updated: March 2026
> CRM Instance: app-na2.hubspot.com | Hub ID: 242063281
> **This is the single source of truth for all HubSpot property mappings.** All skills, plugins, and enrichment workflows reference this file.

---

## 1. Territory Model  -  Owner Assignments

The US territory splits on the Mississippi River. Account ownership is determined by **HQ state**.

### Owner IDs (Active, Sales-Relevant)

| Owner | HubSpot Owner ID | Role | Territory |
|-------|----------------:|------|-----------|
| **Tim Lieto** | `161889085` | AE, East | 30 US states |
| **Ken Cunningham** | `162339176` | AE, West | 20 US states + DC |
| **Timothy Ziemer** | `159350430` | CRO / International | All non-US |
| Cooper Kennedy | `160267902` | RevOps | Internal/unassigned |
| Abilash Menon | `159974715` | CEO | Strategic accounts |
| Hannah Roberts | `159875488` | (Inactive  -  replaced by Ken) |  -  |

### State-to-Owner Mapping

**Tim Lieto (East  -  30 states):**
`AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV`

**Ken Cunningham (West  -  20 states + DC):**
`AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY`

**Tim Ziemer (International):**
All non-US countries

### Multi-State Operator Rules

| Scenario | Resolution |
|----------|------------|
| HQ in known state | HQ state determines owner |
| HQ unknown | First meaningful engagement wins (must log in HubSpot) |
| Non-US HQ | Tim Ziemer (International) |
| Strategic exception | Leadership can reassign with documented reason |

### Key Markets by Territory

| Territory | Top Colo Markets | Key Fiber | Carrier HQs |
|-----------|------------------|-----------|-------------|
| **Tim Lieto** | NoVA (#1), Chicago (#3), Atlanta (#5) | altafiber (OH), Hoosier Net (IN), Bluebird (MO/IL) | Verizon (NY), Lumen (LA), Frontier (CT), Windstream (AR) |
| **Ken Cunningham** | Dallas (#2), Phoenix (#4), Austin (#6), Silicon Valley, Nashville | Texas CLECs, SDN Communications (SD), ALLO (NE/CO) | T-Mobile (WA), AT&T (TX) |

---

## 2. Customer Segment (`customer_segment`)

**Property name:** `customer_segment`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | ICP? | Priority | Notes |
|----------------|--------------|------|----------|-------|
| `Data Center Colo Provider` | Colocation Operator | ✅ | 1 | Core ICP  -  owns DC facilities, meet-me rooms |
| `Fiber Operator` | Fiber Operator (Tier 2/Regional) | ✅ | 2 | Owns >500 route miles, sells dark/lit fiber |
| `Network Operator(Tier 1 / VNO)` | Network Operator (Tier 1) | ✅ | 3 | Tier 1/2 carrier, 10+ states, >2K employees |
| `Enterprise` | MSP/Aggregator | ✅ | 4 | Aggregates 3+ upstream carriers, <10% owned infra |
| `NeoCloud` | NeoCloud | ✅ | 1-2 | AI cloud infrastructure (Lambda, Crusoe, etc.) |
| `Dark Fiber - Commercial Enterprise` | Dark Fiber - Commercial Enterprise | ⚠️ |  -  | Borderline  -  may qualify as Fiber Operator |
| `Enterprise-CustomerSegment` | Enterprise | ❌ |  -  | Consumers of telecom, not infrastructure owners |
| `Partner Target` | Partner Target | ❌ |  -  | Route to Partnerships |
| `Other` | Other | ❌ |  -  | Needs classification |
| `Unknown` | Unknown | ❌ |  -  | Needs enrichment |
| `Flagged for deletion` | Flagged for deletion | ❌ |  -  | Pending removal from CRM |

### Import Mapping Quick-Reference

When building HubSpot import files, use the **Internal Value** column exactly:

```
customer_segment = "Data Center Colo Provider"    ← Colo
customer_segment = "Fiber Operator"               ← Fiber
customer_segment = "Network Operator(Tier 1 / VNO)" ← Network Operator
customer_segment = "Enterprise"                   ← MSP/Aggregator
customer_segment = "NeoCloud"                     ← NeoCloud
```

> ⚠️ **Gotcha:** The internal value for MSP/Aggregator is `Enterprise` (legacy naming). The display label shows "MSP/Aggregator" but imports must use `Enterprise`.

> ⚠️ **CHANGE (March 2026):** `AI - Colocation Operator` is NO LONGER a main segment. AI colos now use `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. The `AI - Colocation Operator` value still exists in HubSpot but should not be used for new imports.

---

## 2.5 Company Sub-Segment (`company_sub_segment`)

**Property name:** `company_sub_segment`
**Type:** Enumeration (single-select)

This field provides granular classification within each main segment. Each value includes the parent segment suffix for clarity.

| Main Segment | Internal Value | Display Label | Description |
|---|---|---|---|
| **Data Center Colo Provider** | `Standard - colo` | Standard - colo | Traditional colo, no strong AI signals |
| **Data Center Colo Provider** | `AI Signals - colo` | AI Signals - colo | Confirmed GPU tenants, liquid cooling, 30kW+ racks |
| **Data Center Colo Provider** | `Modular - colo` | Modular - colo | Distributed / prefab / edge-pod operators (Nodiac, EdgePresence, Armada, Compass). Typically 1-100 MW per site; pod-based deployment; edge or far-edge locations |
| **NeoCloud** | `Large Scale GPU - Neocloud` | Large Scale GPU - Neocloud | Multi-facility GPU cloud, 100MW+, $1B+ valuations |
| **NeoCloud** | `Tier 1 Inference - Neocloud` | Tier 1 Inference - Neocloud | Inference-as-a-service, real-time API SLAs |
| **NeoCloud** | `AI Infrastructure providers - Neocloud` | AI Infrastructure providers - Neocloud | Multi-cloud GPU platforms, API-driven, developer-first |
| **NeoCloud** | `Sovereign AI Clouds - Neocloud` | Sovereign AI Clouds - Neocloud | Regulatory-driven, national AI initiatives, data sovereignty |
| **NeoCloud** | `Crypto to AI - Neoclouds` | Crypto to AI - Neoclouds | Former crypto miners transitioning to AI compute |
| **Fiber Operator** | `Regional CLEC - Fiber operator` | Regional CLEC - Fiber operator | Licensed carrier, <5 states, metro/regional footprint |
| **Fiber Operator** | `Long Haul / Backbone - Fiber operator` | Long Haul / Backbone - Fiber operator | Multi-state fiber, 10K+ route miles |
| **Fiber Operator** | `Dark Fiber Specialist - Fiber Operator` | Dark Fiber Specialist - Fiber Operator | Primarily dark fiber/wavelength sales |
| **Fiber Operator** | `Co-op/consortium` | Co-op/consortium | Municipal utility fiber, co-op, or multi-operator consortium (EPB, UTOPIA, Diamond State Networks). Open-access or federation-organized |
| **Cross-segment** | `Greenfield` | Greenfield | New build / pre-operational site where sub-segment is not yet determinable. Use during early research; reassign to specific sub-segment once operational model clarifies |
| **Network Operator** | `External Extension - Network operator` | External Extension - Network operator | Has internal automation, needs cross-carrier extension |
| **Network Operator** | `Internal + external unification - Network Operator` | Internal + external unification - Network Operator | No internal automation yet |
| **MSP/Aggregator** | `Telecom Aggregator - MSP` | Telecom Aggregator - MSP | Aggregates carrier circuits, wholesale connectivity |
| **MSP/Aggregator** | `Managed Network Services - Network Operator` | Managed Network Services - Network Operator | Managed WAN/MPLS, service-oriented |

### Import Mapping

```
company_sub_segment = "Standard - colo"                                    ← Colo (no AI signals)
company_sub_segment = "AI Signals - colo"                                  ← Colo (confirmed AI signals)
company_sub_segment = "Modular - colo"                                     ← Colo (prefab / edge-pod / distributed)
company_sub_segment = "Large Scale GPU - Neocloud"                         ← Neocloud
company_sub_segment = "Tier 1 Inference - Neocloud"                        ← Neocloud
company_sub_segment = "AI Infrastructure providers - Neocloud"             ← Neocloud
company_sub_segment = "Sovereign AI Clouds - Neocloud"                     ← Neocloud
company_sub_segment = "Crypto to AI - Neoclouds"                           ← Neocloud
company_sub_segment = "Regional CLEC - Fiber operator"                     ← Fiber
company_sub_segment = "Long Haul / Backbone - Fiber operator"              ← Fiber
company_sub_segment = "Dark Fiber Specialist - Fiber Operator"             ← Fiber
company_sub_segment = "Co-op/consortium"                                   ← Fiber (muni / co-op / consortium)
company_sub_segment = "Greenfield"                                         ← Cross-segment (pre-operational)
company_sub_segment = "External Extension - Network operator"              ← Network Op
company_sub_segment = "Internal + external unification - Network Operator" ← Network Op
company_sub_segment = "Telecom Aggregator - MSP"                           ← MSP
company_sub_segment = "Managed Network Services - Network Operator"        ← MSP
```

---

## 3. Account Tier (`account_tier`)

**Property name:** `account_tier`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Criteria |
|----------------|--------------|----------|
| `tier_1` | Tier 1 | **Highest priority**  -  timing + fit are both strong. See Tier 1 criteria below |
| `tier_2` | Tier 2 | Strong ICP fit, high confidence, no urgency trigger |
| `tier_3` | Tier 3 | Qualified but smaller scale or medium confidence |
| `tier_4` | Tier 4 | Low confidence or no clear use case signal |
| `tier_5` | Tier 5 | Manual assignment only (enrichment never sets this) |

> ⚠️ **Note:** Tier 1 = highest priority. This is **inverted** from HubSpot's default property description which says "1 (lowest) to 5 (highest)." Our convention: **Tier 1 = best, Tier 5 = worst.**

### Tier 1 Criteria (must meet ANY of the following)

| Condition | Why |
|-----------|-----|
| NeoCloud (any sub-segment) | Building and buying now, highest urgency |
| Colo with `company_sub_segment` = `AI Signals - colo` | Confirmed GPU tenants or liquid cooling, actively serving AI workloads |
| Any ICP segment + recent trigger event (past 6 months) + `segmentation_confidence` = `high_90` | Trigger (expansion, funding, leadership change) creates a time-sensitive window |

### Tier 2 Criteria

| Condition | Why |
|-----------|-----|
| Standard Colo (`Standard - colo`) with `high_90` confidence + Mid-Size or larger infrastructure | Strong fit, no urgency signal |
| Fiber Operator with `high_90` confidence | Passes all qualification gates, large whitespace |
| Network Operator (either track) with `high_90` confidence | Carrier-scale, strong use case |

### Tier 3 Criteria

| Condition | Why |
|-----------|-----|
| Any ICP segment with `medium_7089` confidence | Qualified but less certain |
| Small-scale accounts (infrastructure_profile = Small in all dimensions) | Fit is there but deal size may be limited |
| MSP/Aggregator (any confidence) | Lowest segment priority |

### Tier 4 Criteria

| Condition | Why |
|-----------|-----|
| `low_5069` or `manual_review_required` confidence | Not enough evidence for active outreach |
| Qualified segment but no observable use case signal | Hold for re-enrichment later |

---

## 4. ICP Tier (`hs_ideal_customer_profile`)

**Property name:** `hs_ideal_customer_profile`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Meaning |
|----------------|--------------|---------|
| `tier_1` | Tier 1 | Great fit  -  matches ICP strongly |
| `tier_2` | Tier 2 | Good fit  -  some qualification signals |
| `tier_3` | Tier 3 | Acceptable but low priority |

---

## 5. Segmentation Confidence (`segmentation_confidence`)

**Property name:** `segmentation_confidence`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | When to Use |
|----------------|--------------|-------------|
| `high_90` | High (90%+) | Bot classification confirmed by known signals |
| `medium_7089` | Medium (70-89%) | Bot classification, some ambiguity |
| `low_5069` | Low (50-69%) | Weak signals, may need manual review |
| `manual_review_required` | Manual review required | Bot couldn't classify confidently |

---

## 6. Lifecycle Stage (`lifecyclestage`)

**Property name:** `lifecyclestage`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Pipeline Position |
|----------------|--------------|-------------------|
| `subscriber` | Prospect | Top of funnel  -  sourced, not yet engaged |
| `lead` | Lead | Identified, initial qualification done |
| `2098366179` | Engaged | Responded to outreach or showed intent |
| `marketingqualifiedlead` | Marketing Qualified Lead | Meets marketing criteria |
| `salesqualifiedlead` | Sales Qualified Lead | Sales-validated, ready for opportunity |
| `opportunity` | Opportunity | Active deal in pipeline |
| `customer` | Customer | Closed-won |
| `2099121898` | Unqualified - bad fit | Does not meet ICP criteria |
| `other` | Other | Catch-all |

### Import Mapping for New Accounts

Most enrichment imports should use:
```
lifecyclestage = "subscriber"    ← New sourced accounts (Prospect)
```

---

## 7. Lead Status (`hs_lead_status`)

**Property name:** `hs_lead_status`
**Type:** Enumeration (single-select)

| Internal Value | Display Label |
|----------------|--------------|
| `NEW` | New |
| `OPEN` | Open |
| `IN_PROGRESS` | In Progress |
| `OPEN_DEAL` | Open Deal |
| `UNQUALIFIED` | Unqualified |
| `ATTEMPTED_TO_CONTACT` | Attempted to Contact |
| `CONNECTED` | Connected |
| `BAD_TIMING` | Bad Timing |

---

## 8. Company Type (`type`)

**Property name:** `type`
**Type:** Enumeration (single-select)

| Internal Value | Display Label |
|----------------|--------------|
| `PROSPECT` | Prospect |
| `PARTNER` | Partner |
| `RESELLER` | Reseller |
| `OTHER` | Other |
| `Customer` | Customer |
| `Disqualified - bad fit` | Disqualified - bad fit |

---

## 9. Infrastructure Profile (`infrastructure_profile`)

**Property name:** `infrastructure_profile`
**Type:** Enumeration (**multi-select**)

Select all that apply per company:

### Facilities (Data Centers)
| Internal Value | Display Label |
|----------------|--------------|
| `Facilities: Small (<5)` | Facilities: Small (<5) |
| `Facilities: Mid-Size (5-19)` | Facilities: Mid-Size (5-19) |
| `Facilities: Large (20-49)` | Facilities: Large (20-49) |
| `Facilities: Enterprise (50+)` | Facilities: Enterprise (50+) |

### Route Miles (Fiber)
| Internal Value | Display Label |
|----------------|--------------|
| `Route Miles: Small (<1K)` | Route Miles: Small (<1K) |
| `Route Miles: Mid-Size (1K-10K)` | Route Miles: Mid-Size (1K-10K) |
| `Route Miles: Large (10K-50K)` | Route Miles: Large (10K-50K) |
| `Route Miles: Enterprise (50K+)` | Route Miles: Enterprise (50K+) |

### POPs (Points of Presence)
| Internal Value | Display Label |
|----------------|--------------|
| `POPs: Small (<10)` | POPs: Small (<10) |
| `POPs: Mid-Size (10-49)` | POPs: Mid-Size (10-49) |
| `POPs: Large (50-99)` | POPs: Large (50-99) |
| `POPs: Enterprise (100+)` | POPs: Enterprise (100+) |

| `None Identified` | None Identified |

> **Multi-select import format:** Separate values with semicolons:
> `Facilities: Mid-Size (5-19);Route Miles: Small (<1K);POPs: Mid-Size (10-49)`

---

## 10. Hyperscaler Proximity (`hyperscaler_proximity`)

**Property name:** `hyperscaler_proximity`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Tier Impact |
|----------------|--------------|-------------|
| `Announced: <50 miles` | Announced: <50 miles | Tier 1 trigger for colos |
| `Announced: 50-200 miles` | Announced: 50-200 miles | Tier 2 signal |
| `Existing Facility Nearby` | Existing Facility Nearby | Strong signal |
| `None Known` | None Known | Neutral |

---

## 10.5 Fabric Provisioning Approach (`fabric_provisioning_approach`)

**Property name:** `fabric_provisioning_approach`
**Type:** Enumeration (**multi-select**)

Select ALL that apply per company. Semicolon-separated in output.

> ⚠️ **Internal values are lowercase snake_case, NOT the title-case display labels.** This is the property that bit Routine 1 on 2026-04-28 (write of `'None Identified'` was rejected; lowercase `none_identified` succeeded). HubSpot will reject any title-case write with a 400 enum-mismatch error. See the **Enum Case-Sensitivity Reference** appendix at the bottom of this file for the full per-property convention.

| Category | Internal Value | Display Label |
|----------|----------------|--------------|
| External NaaS | `megaport` | Megaport |
| External NaaS | `packetfabric` | PacketFabric |
| External NaaS | `equinix_ecx_fabric` | Equinix ECX Fabric |
| External NaaS | `console_connect` | Console Connect |
| External NaaS | `other_external_naas` | Other External NaaS |
| Competitor | `lumen_private_connectivity_fabric` | Lumen Private Connectivity Fabric |
| Competitor | `other_competitor_fabric` | Other Competitor Fabric |
| Internal | `homegrownproprietary_platform` | Homegrown/Proprietary Platform |
| Internal | `standard_ossbss_stack` | Standard OSS/BSS Stack |
| Internal | `manuallegacy_processes` | Manual/Legacy Processes |
| None | `none_identified` | None Identified |

> **Multi-select import format:** `megaport;packetfabric` (semicolons, no spaces, lowercase values).
> **Note on the slash-stripped values:** `homegrownproprietary_platform`, `standard_ossbss_stack`, and `manuallegacy_processes` are HubSpot's slug-collapsed forms of the labels (the "/" character gets dropped, not converted to underscore). These are the only values HubSpot's API accepts — verified against `/properties/v2/companies/properties/named/fabric_provisioning_approach` on 2026-04-28.

---

## 11. Key Tenant Segments (`key_tenant_segments__cloned_`)

**Property name:** `key_tenant_segments__cloned_`
**Type:** Enumeration (multi-select)

| Internal Value | Display Label |
|----------------|--------------|
| `cloud_providers` | Cloud Providers |
| `enterprises` | Enterprises |
| `carriers` | Carriers |
| `content__hyperscale` | Content & Hyperscale |
| `financial_services` | Financial Services |
| `other` | Other |

> Used primarily for Colo operators to track what types of tenants they serve.

---

## 12. Enrichment Properties (Text Fields)

| Property Name | Label | Type | Max Chars | Description |
|--------------|-------|------|-----------|-------------|
| `account_brief` | Company brief | String | 400 | 3-6 sentence overview: what they do, who they serve, positioning |
| `maiaedge_value_proposition` | MaiaEdge value proposition | String | 500 | 4-5 sentence email body: prospect situation + problem + MaiaEdge solution + proof |
| `geographic_focus` | Geographic focus | String | 150 | Natural language description of where the company operates (e.g., "Southeast US", "National", "Multi-state Northeast"). Separate from account_brief for geographic personalization |
| `provisioning_landscape` | Provisioning landscape | String | 500 | Narrative synthesis of the company's fabric and provisioning approach, including platforms/tools/processes they use and a messaging angle for MaiaEdge |
| `recent_news_or_trigger_event` | Recent News / Trigger Events | String | 250 | Expansion, funding, leadership change from the past calendar year |
| `last_enriched_date` | Last enriched date | String |  -  | YYYY-MM-DD format, auto-populated when enrichment runs. **String-typed, not Date-typed.** ISO YYYY-MM-DD format is required because CRM Guardian Routines 1, 2, and 6 query this field with HubSpot search `LT`/`GT` operators relying on lexicographic comparison (which only works correctly with zero-padded ISO dates). If this property is ever converted to a Date-type in HubSpot, all routine query filters must switch from ISO-string values to epoch milliseconds — search files for `last_enriched_date` to find the affected filters. |
| `domain` | Company Domain Name | String |  -  | Primary company domain (e.g., `equinix.com`) |
| `linkedin_company_page` | LinkedIn Company Page | String |  -  | LinkedIn company page URL. Apollo `linkedin_url` is the authoritative source on BOTH new-account creation AND re-enrichment — overwrite when Apollo returns a non-empty value that differs from HubSpot (companies change LinkedIn handles after rebrands / M&A). Used by weekly-signal-scan Excel output column and outreach personalization flows. |

---

## 13. Geographic Properties

| Property Name | Label | Notes |
|--------------|-------|-------|
| `state` | State/Region | Free-text  -  use full state name or 2-letter abbreviation consistently |
| `hs_state_code` | State/Region Code | 2-letter code (auto-populated by HubSpot in some cases) |
| `country` | Country/Region | Free-text |
| `hs_country_code` | Country/Region Code | 2-letter ISO code |

> **Territory routing depends on `state`.** Ensure this reflects **HQ location**, not operational footprint.

---

## 14. Standard Import Template  -  Column Headers

For HubSpot company imports, use these exact column headers:

```csv
Company Domain Name,Name,Customer segment,Company Sub Segment,Account Tier,Lifecycle Stage,Company owner,State/Region,Country/Region,Company brief,MaiaEdge value proposition,Geographic focus,Provisioning landscape,Infrastructure profile,Hyperscaler Proximity,Segmentation confidence,Target Account,Lead Status
```

### Default Values for New Sourced Accounts

| Property | Default Value | Notes |
|----------|--------------|-------|
| `lifecyclestage` | `subscriber` | All new sourced accounts start as Prospect |
| `hs_lead_status` | `NEW` | Fresh, no outreach attempted |
| `type` | `PROSPECT` | Until qualified otherwise |
| `hs_is_target_account` | `true` | If ICP-qualified |
| `segmentation_confidence` | Per bot output | `high_90`, `medium_7089`, or `low_5069` |

---

## 15. Quick Reference: Owner Assignment for Imports

Use this lookup when building import files:

```python
TERRITORY_MAP = {
    # Tim Lieto (East)  -  Owner ID: 161889085
    'AL': '161889085', 'AR': '161889085', 'CT': '161889085', 'DE': '161889085',
    'FL': '161889085', 'GA': '161889085', 'IA': '161889085', 'IL': '161889085',
    'IN': '161889085', 'KY': '161889085', 'LA': '161889085', 'MA': '161889085',
    'MD': '161889085', 'ME': '161889085', 'MI': '161889085', 'MN': '161889085',
    'MO': '161889085', 'MS': '161889085', 'NC': '161889085', 'NH': '161889085',
    'NJ': '161889085', 'NY': '161889085', 'OH': '161889085', 'PA': '161889085',
    'RI': '161889085', 'SC': '161889085', 'VA': '161889085', 'VT': '161889085',
    'WI': '161889085', 'WV': '161889085',

    # Ken Cunningham (West)  -  Owner ID: 162339176
    'AK': '162339176', 'AZ': '162339176', 'CA': '162339176', 'CO': '162339176',
    'DC': '162339176', 'HI': '162339176', 'ID': '162339176', 'KS': '162339176',
    'MT': '162339176', 'ND': '162339176', 'NE': '162339176', 'NM': '162339176',
    'NV': '162339176', 'OK': '162339176', 'OR': '162339176', 'SD': '162339176',
    'TN': '162339176', 'TX': '162339176', 'UT': '162339176', 'WA': '162339176',
    'WY': '162339176',
}

# International → Tim Ziemer: 159350430
# Unknown state → Leave unassigned for manual routing
```

---

## Appendix: Data Quality Flags

| Issue | How to Detect | Resolution |
|-------|--------------|------------|
| Missing `customer_segment` | `customer_segment` = `Unknown` or blank | Run through enrichment pipeline |
| Missing `state` | `state` is blank | Research HQ location for territory routing |
| Wrong territory owner | `state` doesn't match `hubspot_owner_id` per map | Reassign owner per territory map |
| Stale enrichment | `last_enriched_date` > 120 days ago | Re-enrich through pipeline |
| Low confidence segment | `segmentation_confidence` = `low_5069` or `manual_review_required` | Manual review or re-enrich |
| Legacy `Enterprise` segment | `customer_segment` = `Enterprise` | Verify: is it MSP/Aggregator or actual Enterprise consumer? |

---

## Appendix: Enum Case-Sensitivity Reference

> **Why this exists.** HubSpot's `manage_crm_objects` API rejects enum writes with `400 PROPERTY_VALUE_NOT_RECOGNIZED` when the value's case or punctuation doesn't exactly match the property's `options[].value` (the *internal* value, not the *display label*). On 2026-04-28, Routine 1 wrote `fabric_provisioning_approach='None Identified'` (the label) and got rejected; lowercase `none_identified` (the value) succeeded on retry. **This is silent for routines that don't retry — partial enrichment writes appear to succeed but the enum field stays blank.** Every routine that writes an enum field MUST consult this table or pipe through `skills/import-processor/` enum mapping.
>
> **Verification.** Values below were retrieved from live HubSpot via `mcp__claude_ai_HubSpot__get_properties` on 2026-04-28. To re-verify on schema drift, run that tool against the property name. If a value here disagrees with what the API returns, the API wins — update this file.

### Casing convention by property (single source of truth)

| Property | Case Convention | Example Value | Sample Wrong Value |
|---|---|---|---|
| `customer_segment` | **Title Case with spaces and special chars** (preserved verbatim) | `Data Center Colo Provider`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `Flagged for deletion` | `data center colo provider` (lowercase rejected); `Colocation Operator` (label not value) |
| `company_sub_segment` | **Title Case with spaces, dashes, slashes** (preserved verbatim) | `AI Signals - colo`, `Standard - colo`, `Co-op/consortium`, `Greenfield`, `Crypto to AI - Neoclouds` | `ai_signals_colo` (snake-case rejected); `AI - Colocation Operator` (deprecated value) |
| `account_tier` | **lowercase snake_case** | `tier_1`, `tier_2`, `tier_3`, `tier_4`, `tier_5` | `Tier 1` (label rejected); `tier1` (no underscore rejected) |
| `hs_ideal_customer_profile` | **lowercase snake_case** | `tier_1`, `tier_2`, `tier_3` | same gotchas as `account_tier` |
| `segmentation_confidence` | **lowercase snake_case + digit suffix** | `high_90`, `medium_7089`, `low_5069`, `manual_review_required` | `high (90%+)` (label rejected); `HIGH_90` (uppercase rejected); `medium_70_89` (extra underscore rejected) |
| `lifecyclestage` | **lowercase + numeric custom-stage IDs** (mixed) | `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`, `2098366179` (Engaged), `2099121898` (Unqualified) | `Subscriber` (uppercase rejected); `MQL` (alias rejected) |
| `hs_lead_status` | **UPPER_SNAKE_CASE** | `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING` | `New` (title-case rejected); `In Progress` (space rejected) |
| `type` (company type) | **Mixed UPPER and Title Case** (legacy) | `PROSPECT`, `PARTNER`, `RESELLER`, `OTHER` (uppercase) AND `Customer`, `Disqualified - bad fit` (title-case) — the values are NOT consistent across this property | `prospect` (lowercase rejected); `customer` (lowercase rejected) |
| `infrastructure_profile` | **Title Case with colons and parens** (preserved verbatim, multi-select semicolon-separated) | `Facilities: Small (<5)`, `Route Miles: Mid-Size (1K-10K)`, `POPs: Enterprise (100+)`, `None Identified` | `facilities_small` (snake-case rejected); `Facilities: Small <5` (missing parens rejected) |
| `fabric_provisioning_approach` | **lowercase snake_case** (multi-select semicolon-separated) | `megaport`, `packetfabric`, `equinix_ecx_fabric`, `console_connect`, `other_external_naas`, `lumen_private_connectivity_fabric`, `other_competitor_fabric`, `homegrownproprietary_platform`, `standard_ossbss_stack`, `manuallegacy_processes`, `none_identified` | `Megaport` (title-case rejected — this is the bug from 2026-04-28); `Homegrown/Proprietary Platform` (preserved punctuation rejected — slashes get stripped, not converted to underscore) |
| `hyperscaler_proximity` | **Title Case with spaces, colons, and special chars** (preserved verbatim) | `Announced: <50 miles`, `Announced: 50-200 miles`, `Existing Facility Nearby`, `None Known` | `announced_lt_50_miles` (snake-case rejected) |

### Universal rules

1. **Always write the `value`, never the `label`.** When in doubt, query the property: `mcp__claude_ai_HubSpot__get_properties({objectType: "companies", propertyNames: ["<name>"]})` returns `options[].value` (write target) and `options[].label` (display). Never substitute one for the other.
2. **Slash and punctuation are unpredictable.** `Homegrown/Proprietary Platform` becomes `homegrownproprietary_platform` (slash stripped) — but `Co-op/consortium` is preserved as-is in `company_sub_segment`. There is no universal rule. Always check live values before constructing a write.
3. **Multi-select is semicolon-separated, no spaces around the semicolons.** `megaport;packetfabric` is correct. `megaport; packetfabric` and `megaport,packetfabric` both fail.
4. **Trailing/leading whitespace fails silently.** `' tier_1'` and `'tier_1 '` are rejected as invalid enum values, but the error message can be misleading. Trim values before writing.
5. **Case-sensitivity is per-property, not global.** Don't assume "we use snake_case" or "we use Title Case" — different properties on the same object follow different conventions. The table above is the only reliable reference.
6. **`import-processor` skill owns the canonical mapping.** Routines that need to translate human-readable input ("High confidence" → `high_90`, "Tier 1" → `tier_1`) should call into `skills/import-processor/` rather than inlining the conversion. That skill is the single point of update if HubSpot adds a new enum value.

### When you encounter a `400 PROPERTY_VALUE_NOT_RECOGNIZED` error

1. The error message includes the rejected value AND the property name. Capture both.
2. Query the live property: `get_properties({objectType, propertyNames: ["<name>"]})`. Compare your write value against `options[].value` (NOT `options[].label`).
3. If the live values disagree with this appendix, **the API is authoritative** — update this appendix to match and add a note in the change log below.
4. If the live values match this appendix but your write still fails, check for trailing whitespace, label/value swaps, and multi-select delimiter format.

### Change log (track schema drift)

| Date | Property | Change | Caught by |
|------|----------|--------|-----------|
| 2026-04-28 | `fabric_provisioning_approach` | Internal values discovered to be lowercase snake_case (`megaport`, `none_identified`, etc.), NOT title-case as previously documented. Doc was wrong since first written. | Routine 1 production run hit `400 PROPERTY_VALUE_NOT_RECOGNIZED` on `'None Identified'`; retry with lowercase succeeded. |
