# MaiaEdge HubSpot Property Schema — Unified Reference

> Last updated: March 2026
> CRM Instance: app-na2.hubspot.com | Hub ID: 242063281
> **This is the single source of truth for all HubSpot property mappings.** All skills, plugins, and enrichment workflows reference this file.

---

## 1. Territory Model — Owner Assignments

The US territory splits on the Mississippi River. Account ownership is determined by **HQ state**.

### Owner IDs (Active, Sales-Relevant)

| Owner | HubSpot Owner ID | Role | Territory |
|-------|----------------:|------|-----------|
| **Tim Lieto** | `161889085` | AE, East | 30 US states |
| **Ken Cunningham** | `162339176` | AE, West | 20 US states + DC |
| **Timothy Ziemer** | `159350430` | CRO / International | All non-US |
| Cooper Kennedy | `160267902` | RevOps | Internal/unassigned |
| Abilash Menon | `159974715` | CEO | Strategic accounts |
| Hannah Roberts | `159875488` | (Inactive — replaced by Ken) | — |

### State-to-Owner Mapping

**Tim Lieto (East — 30 states):**
`AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV`

**Ken Cunningham (West — 20 states + DC):**
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
| `Data Center Colo Provider` | Colocation Operator | ✅ | 1 | Core ICP — owns DC facilities, meet-me rooms |
| `Fiber Operator` | Fiber Operator (Tier 2/Regional) | ✅ | 2 | Owns >500 route miles, sells dark/lit fiber |
| `Network Operator(Tier 1 / VNO)` | Network Operator (Tier 1) | ✅ | 3 | Tier 1/2 carrier, 10+ states, >2K employees |
| `Enterprise` | MSP/Aggregator | ✅ | 4 | Aggregates 3+ upstream carriers, <10% owned infra |
| `NeoCloud` | NeoCloud | ✅ | 1-2 | AI cloud infrastructure (CoreWeave, Lambda, etc.) |
| `Dark Fiber - Commercial Enterprise` | Dark Fiber - Commercial Enterprise | ⚠️ | — | Borderline — may qualify as Fiber Operator |
| `Enterprise-CustomerSegment` | Enterprise | ❌ | — | Consumers of telecom, not infrastructure owners |
| `Partner Target` | Partner Target | ❌ | — | Route to Partnerships |
| `Other` | Other | ❌ | — | Needs classification |
| `Unknown` | Unknown | ❌ | — | Needs enrichment |
| `Flagged for deletion` | Flagged for deletion | ❌ | — | Pending removal from CRM |

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
| **NeoCloud** | `Large Scale GPU - Neocloud` | Large Scale GPU - Neocloud | Multi-facility GPU cloud, 100MW+, $1B+ valuations |
| **NeoCloud** | `Tier 1 Inference - Neocloud` | Tier 1 Inference - Neocloud | Inference-as-a-service, real-time API SLAs |
| **NeoCloud** | `AI Infrastructure providers - Neocloud` | AI Infrastructure providers - Neocloud | Multi-cloud GPU platforms, API-driven, developer-first |
| **NeoCloud** | `Sovereign AI Clouds - Neocloud` | Sovereign AI Clouds - Neocloud | Regulatory-driven, national AI initiatives, data sovereignty |
| **NeoCloud** | `Crypto to AI - Neoclouds` | Crypto to AI - Neoclouds | Former crypto miners transitioning to AI compute |
| **Fiber Operator** | `Regional CLEC - Fiber operator` | Regional CLEC - Fiber operator | Licensed carrier, <5 states, metro/regional footprint |
| **Fiber Operator** | `Long Haul / Backbone - Fiber operator` | Long Haul / Backbone - Fiber operator | Multi-state fiber, 10K+ route miles |
| **Fiber Operator** | `Dark Fiber Specialist - Fiber Operator` | Dark Fiber Specialist - Fiber Operator | Primarily dark fiber/wavelength sales |
| **Network Operator** | `External Extension - Network operator` | External Extension - Network operator | Has internal automation, needs cross-carrier extension |
| **Network Operator** | `Internal + external unification - Network Operator` | Internal + external unification - Network Operator | No internal automation yet |
| **MSP/Aggregator** | `Telecom Aggregator - MSP` | Telecom Aggregator - MSP | Aggregates carrier circuits, wholesale connectivity |
| **MSP/Aggregator** | `Managed Network Services - Network Operator` | Managed Network Services - Network Operator | Managed WAN/MPLS, service-oriented |

### Import Mapping

```
company_sub_segment = "Standard - colo"                                    ← Colo (no AI signals)
company_sub_segment = "AI Signals - colo"                                  ← Colo (confirmed AI signals)
company_sub_segment = "Large Scale GPU - Neocloud"                         ← Neocloud
company_sub_segment = "Tier 1 Inference - Neocloud"                        ← Neocloud
company_sub_segment = "AI Infrastructure providers - Neocloud"             ← Neocloud
company_sub_segment = "Sovereign AI Clouds - Neocloud"                     ← Neocloud
company_sub_segment = "Crypto to AI - Neoclouds"                           ← Neocloud
company_sub_segment = "Regional CLEC - Fiber operator"                     ← Fiber
company_sub_segment = "Long Haul / Backbone - Fiber operator"              ← Fiber
company_sub_segment = "Dark Fiber Specialist - Fiber Operator"             ← Fiber
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
| `tier_1` | Tier 1 | **Highest priority** — timing + fit are both strong. See Tier 1 criteria below |
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
| `tier_1` | Tier 1 | Great fit — matches ICP strongly |
| `tier_2` | Tier 2 | Good fit — some qualification signals |
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
| `subscriber` | Prospect | Top of funnel — sourced, not yet engaged |
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

| Category | Internal Value | Display Label |
|----------|----------------|--------------|
| External NaaS | `Megaport` | Megaport |
| External NaaS | `PacketFabric` | PacketFabric |
| External NaaS | `Equinix ECX Fabric` | Equinix ECX Fabric |
| External NaaS | `Console Connect` | Console Connect |
| External NaaS | `Other External NaaS` | Other External NaaS |
| Competitor | `Lumen Private Connectivity Fabric` | Lumen Private Connectivity Fabric |
| Competitor | `Other Competitor Fabric` | Other Competitor Fabric |
| Internal | `Homegrown/Proprietary Platform` | Homegrown/Proprietary Platform |
| Internal | `Standard OSS/BSS Stack` | Standard OSS/BSS Stack |
| Internal | `Manual/Legacy Processes` | Manual/Legacy Processes |
| None | `None Identified` | None Identified |

> **Multi-select import format:** `Megaport;PacketFabric` (semicolons, no spaces)

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
| `last_enriched_date` | Last enriched date | String | — | YYYY-MM-DD format, auto-populated when enrichment runs |
| `domain` | Company Domain Name | String | — | Primary company domain (e.g., `equinix.com`) |

---

## 13. Geographic Properties

| Property Name | Label | Notes |
|--------------|-------|-------|
| `state` | State/Region | Free-text — use full state name or 2-letter abbreviation consistently |
| `hs_state_code` | State/Region Code | 2-letter code (auto-populated by HubSpot in some cases) |
| `country` | Country/Region | Free-text |
| `hs_country_code` | Country/Region Code | 2-letter ISO code |

> **Territory routing depends on `state`.** Ensure this reflects **HQ location**, not operational footprint.

---

## 14. Standard Import Template — Column Headers

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
    # Tim Lieto (East) — Owner ID: 161889085
    'AL': '161889085', 'AR': '161889085', 'CT': '161889085', 'DE': '161889085',
    'FL': '161889085', 'GA': '161889085', 'IA': '161889085', 'IL': '161889085',
    'IN': '161889085', 'KY': '161889085', 'LA': '161889085', 'MA': '161889085',
    'MD': '161889085', 'ME': '161889085', 'MI': '161889085', 'MN': '161889085',
    'MO': '161889085', 'MS': '161889085', 'NC': '161889085', 'NH': '161889085',
    'NJ': '161889085', 'NY': '161889085', 'OH': '161889085', 'PA': '161889085',
    'RI': '161889085', 'SC': '161889085', 'VA': '161889085', 'VT': '161889085',
    'WI': '161889085', 'WV': '161889085',

    # Ken Cunningham (West) — Owner ID: 162339176
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
| Stale enrichment | `last_enriched_date` > 6 months ago | Re-enrich through pipeline |
| Low confidence segment | `segmentation_confidence` = `low_5069` or `manual_review_required` | Manual review or re-enrich |
| Legacy `Enterprise` segment | `customer_segment` = `Enterprise` | Verify: is it MSP/Aggregator or actual Enterprise consumer? |
