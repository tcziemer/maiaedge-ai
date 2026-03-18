# HubSpot Value Reference

Definitive mapping from internal classification to exact HubSpot property values.
All output must use these exact strings — case-sensitive, no variations.

## customer_segment (Dropdown)

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

> ⚠️ **IMPORTANT:** `AI - Colocation Operator` is NO LONGER a main segment. Use `Data Center Colo Provider` + `customer_sub_segment = AI Infrastructure` instead. The `NeoCloud` value is its own segment — do NOT map to `Colocation Operator`.

> ⚠️ **MSP/Aggregator gotcha:** The HubSpot internal value is `Enterprise` (legacy naming). The display label shows "MSP/Aggregator" but imports must use `Enterprise`.

## customer_sub_segment (Dropdown — NEW PROPERTY)

**Property name:** `customer_sub_segment`
**Type:** Enumeration (single-select)
**Status:** Needs to be created in HubSpot

This field provides granular classification within each main segment.

| Main Segment (`customer_segment`) | Valid Sub-Segments | HubSpot `customer_sub_segment` Value |
|---|---|---|
| `Data Center Colo Provider` | Standard Colocation | `Standard` |
| `Data Center Colo Provider` | AI Infrastructure (GPU tenants, liquid cooling, 30kW+) | `AI Infrastructure` |
| `NeoCloud` | Large-Scale GPU NeoClouds | `Large-Scale GPU NeoClouds` |
| `NeoCloud` | Tier 1 Inference Providers | `Tier 1 Inference Providers` |
| `NeoCloud` | AI Infrastructure Providers | `AI Infrastructure Providers` |
| `NeoCloud` | Sovereign AI Clouds | `Sovereign AI Clouds` |
| `NeoCloud` | Crypto-to-AI Pivots | `Crypto-to-AI Pivots` |
| `Fiber Operator` | Regional CLEC | `Regional CLEC` |
| `Fiber Operator` | Long-Haul / Backbone | `Long-Haul / Backbone` |
| `Fiber Operator` | Dark Fiber Specialist | `Dark Fiber Specialist` |
| `Network Operator(Tier 1 / VNO)` | Track A - External Extension | `Track A - External Extension` |
| `Network Operator(Tier 1 / VNO)` | Track B - Internal + External Unification | `Track B - Internal + External Unification` |
| `Enterprise` (MSP) | Telecom Aggregator | `Telecom Aggregator` |
| `Enterprise` (MSP) | Managed Network Services | `Managed Network Services` |

### Sub-Segment Assignment Rules

- **Colocation:** `AI Infrastructure` if STRONG AI signals (confirmed GPU tenants OR liquid cooling). Otherwise `Standard`.
- **Neocloud:** Classify based on primary business model. See neocloud-cheatsheet.md for detailed profiles.
- **Fiber:** `Regional CLEC` if <5 states and CLEC-licensed. `Long-Haul / Backbone` if 10K+ route miles or multi-state backbone. `Dark Fiber Specialist` if primarily dark fiber/wavelength sales.
- **Network Operator:** `Track A` if evidence of portal/API/self-service. `Track B` if no evidence of internal automation. Default `Track A` if unclear.
- **MSP:** `Telecom Aggregator` if aggregates carrier circuits for wholesale. `Managed Network Services` if primarily managed WAN/MPLS services.

## infrastructure_profile (Multi-select)

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
- Data Centers: 50+ → Enterprise, 20-49 → Large, 5-19 → Mid-Size, <5 → Small
- Fiber Route Miles: 50K+ → Enterprise, 10K-50K → Large, 1K-10K → Mid-Size, <1K → Small
- POPs: 100+ → Enterprise, 50-99 → Large, 10-49 → Mid-Size, <10 → Small
- No metrics found → `None Identified`

## fabric_provisioning_approach (Multi-select)

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

## hyperscaler_proximity (Dropdown)

```
Announced: <50 miles
Announced: 50-200 miles
Existing Facility Nearby
None Known
```

## account_tier (Dropdown)

| Score | HubSpot Value |
|---|---|
| 70-100 | `Tier 1 - High Priority` |
| 45-69 | `Tier 2 - Standard Priority` |
| 0-44 | `Tier 3 - Low Priority` |
| Excluded | `Tier 4 - Disqualify` |

## segmentation_confidence (Dropdown)

| Confidence | HubSpot Value |
|---|---|
| 90%+ clear signals | `High (90%+)` |
| 70-89% mostly clear | `Medium (70-89%)` |
| 50-69% conflicting signals | `Low (50-69%)` |
| Cannot determine | `Manual Review Required` |

## HubSpot Import Rules
- Multi-select: Semicolons with NO spaces (`Megaport;PacketFabric` not `Megaport; PacketFabric`)
- Dropdown: Must match exactly (case-sensitive)
- Date: YYYY-MM-DD
- Text: Respect character limits (account_brief 400, geographic_focus 150, recent_trigger 250, provisioning_landscape 500, maiaedge_value_proposition 500)
- Company matching: HubSpot matches on `domain` — no http://, no trailing slashes
