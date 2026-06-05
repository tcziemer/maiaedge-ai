---
name: import-processor
description: "MaiaEdge file-to-HubSpot-import transform. Use ONLY when the user hands you an existing CSV/XLSX of enrichment output (e.g. a historical export, a manually-prepared spreadsheet, a partner-supplied list) and asks for an import-ready file. For any workflow that starts with company names or domains — use `company-enrichment` instead, which writes directly to HubSpot via MCP. When this skill does run: transforms all values to match HubSpot property labels, separates edge cases for deeper research, produces definitive excludes log with normalized categories. Input: 33-column enrichment output XLSX/CSV. Output: (1) Qualified accounts ready for HubSpot import, (2) Edge cases flagged for researcher skill, (3) Definitive excludes. Zero manual adjustment required — column headers match HubSpot properties, values match enums, multi-checkbox delimited correctly."
---

# MaiaEdge Enrichment Import Processor

> **File-to-import transform only.** Do not invoke unless the user has handed you an existing CSV/XLSX file and explicitly wants an import-ready spreadsheet. For any request that starts with company names or domains ("enrich these companies", "classify this list"), use `company-enrichment` instead — it writes directly to HubSpot via MCP and no import file is needed.

## Skill Name: `maiaedge-enrichment-import-processor`
## Call Action: Use when the user hands you a CSV/XLSX enrichment file and asks to "process enrichment output", "prepare for HubSpot import", "separate qualified and excluded", "clean enrichment data", or "find edge cases in enrichment results"

## Purpose
Take a CSV/XLSX enrichment output file (from an external system, a historical export, a partner-supplied list, or the `company-enrichment` skill's optional XLSX fallback) and produce HubSpot-optimized import files. This skill:
1. **Separates qualified accounts** → transforms all values to match HubSpot property labels exactly, ready for drag-and-drop import
2. **Identifies edge cases** within the excludes → accounts that may have been incorrectly excluded and deserve deeper research
3. **Separates definitive excludes** → clean list with normalized exclusion categories

The HubSpot import file should require ZERO manual adjustment  -  column headers match HubSpot property names, values match HubSpot enum labels, multi-checkbox fields are properly delimited, and domains are cleaned for matching.

## Input
An XLSX or CSV file with the 33-column enrichment output format. Key columns:
- `classification_status` (QUALIFIED / EXCLUDED / REVIEW)
- `customer_segment` (segment name or EXCLUDE: reason)
- `customer_sub_segment` (Standard / AI Infrastructure / Track A - External Extension / Track B - Internal + External Unification / Large-Scale GPU NeoClouds / etc.)
- All other enrichment fields

---

## STEP 1: Parse and Separate Records

### Three Categories
1. **QUALIFIED**: `classification_status` = "QUALIFIED"
2. **EDGE CASES**: `classification_status` = "EXCLUDED" BUT matches edge case criteria (see Step 3)
3. **DEFINITIVE EXCLUDES**: `classification_status` = "EXCLUDED" AND does NOT match edge case criteria

---

## STEP 2: Transform Qualified Accounts for HubSpot Import

### 2A: Column Mapping  -  Enrichment Output → HubSpot Property

The HubSpot import file must use HubSpot property names as column headers. Only include columns that map to actual HubSpot properties.

| # | Enrichment Column | HubSpot Column Header | HubSpot Type | Transform Required |
|---|---|---|---|---|
| 1 | `company_domain` | `domain` | String | Clean domain (strip protocol, www) |
| 2 | `company_name` | `name` | String | Direct |
| 3 | `customer_segment` | `customer_segment` | Enumeration | **Value mapping  -  see 2B** |
| 3.5 | `customer_sub_segment` | `company_sub_segment` | Enumeration | **Value mapping  -  see 2B** |
| 4 | `state` | `state` | String | 2-letter state abbreviation for US HQs |
| 5 | `country` | `country` | String | Country name for all accounts |
| 6 | *(derived from state)* | `hubspot_owner_id` | Owner | **Territory lookup  -  see 2F** |
| 7 | `infrastructure_profile` | `infrastructure_profile` | Multi-checkbox | Direct (values already match) |
| 8 | `fabric_provisioning_approach` | `fabric_provisioning_approach` | Multi-checkbox | **Value substitution  -  see 2C** |
| 9 | `geographic_focus` | `geographic_focus` | String | Direct |
| 10 | `hyperscaler_proximity` | `hyperscaler_proximity` | Enumeration | Direct (values already match) |
| 11 | `key_tenant_segments` | `key_tenant_segments__cloned_` | Multi-checkbox | Direct, semicolon-separated. Colo only. |
| 12 | `account_tier` | `account_tier` | Enumeration | **Value mapping  -  see 2D** |
| 13 | `account_brief` | `account_brief` | String | Trim whitespace |
| 14 | `provisioning_landscape` | `provisioning_landscape` | String | Trim whitespace |
| 15 | `maiaedge_value_proposition` | `maiaedge_value_proposition` | String | Trim whitespace |
| 16 | `recent_trigger` | `recent_news_or_trigger_event` | String | Direct |
| 17 | `segmentation_confidence` | `segmentation_confidence` | Enumeration | **Value mapping  -  see 2E** |
| 18 | *(static)* | `lifecyclestage` | Enumeration | Set to `subscriber` for all new accounts |
| 19 | *(static)* | `hs_lead_status` | Enumeration | Set to `NEW` for all new accounts |
| 20 | *(static)* | `type` | Enumeration | Set to `PROSPECT` for all new accounts |
| 21 | *(static)* | `hs_is_target_account` | Boolean | Set to `true` for all qualified accounts |
| 22 | *(generated)* | `last_enriched_date` | Date | Set to today: YYYY-MM-DD |

**Reference-only columns** (append at end, prefix with `_ref_`  -  HubSpot will skip unrecognized column names during import):

| `_ref_priority_score` | For sorting/review | priority_score value |
| `_ref_account_tier_label` | For context | account_tier_label value |
| `_ref_tier_top_reasons` | For context | tier_top_reasons value |

### 2B: Customer Segment + Sub-Segment Mapping (CRITICAL)

The enrichment bot outputs `customer_segment` and `customer_sub_segment` as TWO SEPARATE fields. Both get imported into HubSpot. The HubSpot property for sub-segment is `company_sub_segment` (not `customer_sub_segment`).

**Segment Mapping:**

| Bot `customer_segment` | → HubSpot `customer_segment` Value |
|---|---|
| `Colocation Operator` | `Data Center Colo Provider` |
| `Neocloud` | `NeoCloud` |
| `Fiber Operator` | `Fiber Operator` |
| `Network Operator` | `Network Operator(Tier 1 / VNO)` |
| `MSP/Aggregator` | `Enterprise` |

> ⚠️ **CHANGE:** `AI - Colocation Operator` is DEPRECATED. AI colos now use `Data Center Colo Provider` + `company_sub_segment = AI Signals - colo`.

**Sub-Segment Mapping** (bot output → HubSpot `company_sub_segment` value):

| Bot `customer_sub_segment` | → HubSpot `company_sub_segment` Value |
|---|---|
| `Standard` | `Standard - colo` |
| `AI Infrastructure` | `AI Signals - colo` |
| `Large-Scale GPU NeoClouds` | `Large Scale GPU - Neocloud` |
| `Tier 1 Inference Providers` | `Tier 1 Inference - Neocloud` |
| `AI Infrastructure Providers` | `AI Infrastructure providers - Neocloud` |
| `Sovereign AI Clouds` | `Sovereign AI Clouds - Neocloud` |
| `Crypto-to-AI Pivots` | `Crypto to AI - Neoclouds` |
| `Regional CLEC` | `Regional CLEC - Fiber operator` |
| `Long-Haul / Backbone` | `Long Haul / Backbone - Fiber operator` |
| `Dark Fiber Specialist` | `Dark Fiber Specialist - Fiber Operator` |
| `Track A - External Extension` | `External Extension - Network operator` |
| `Track B - Internal + External Unification` | `Internal + external unification - Network Operator` |
| `Telecom Aggregator` | `Telecom Aggregator - MSP` |
| `Managed Network Services` | `Managed Network Services - Network Operator` |

### 2C: Fabric Provisioning Approach Value Mapping

The bot outputs values that are close but not exact matches to HubSpot labels. Apply these substitutions to each semicolon-separated value:

| Bot Output Value | → HubSpot Label (exact) | Change? |
|---|---|---|
| `Megaport` | `Megaport` | No |
| `PacketFabric` | `PacketFabric` | No |
| `Equinix ECX Fabric` | `Equinix ECX Fabric` | No |
| `Console Connect` | `Console Connect` | No |
| `Lumen Private Connect` | `Lumen Private Connectivity Fabric` | **YES** |
| `Homegrown/Proprietary` | `Homegrown/Proprietary Platform` | **YES** |
| `Manual/Legacy Processes` | `Manual/Legacy Processes` | No |

### 2D: Account Tier Value Mapping

| Bot `account_tier` | → HubSpot `account_tier` Internal Value |
|---|---|
| `TIER_1_STRATEGIC` | `tier_1` |
| `TIER_2_CORE` | `tier_2` |
| `TIER_3_EMERGING` | `tier_3` |
| `UNRANKED` | `tier_4` |

> HubSpot has 5 tiers (`tier_1` through `tier_5`). Tier 1 = highest priority, Tier 5 = lowest. The enrichment pipeline uses 4 output labels that map to `tier_1` through `tier_4`. `tier_5` is reserved for manual assignment.

### 2E: Segmentation Confidence Value Mapping

| Bot `segmentation_confidence` | → HubSpot `segmentation_confidence` Internal Value |
|---|---|
| `HIGH` | `high_90` |
| `MEDIUM` | `medium_7089` |
| `LOW` | `low_5069` |
| `MANUAL_REVIEW` | `manual_review_required` |

### 2F: Owner Assignment from State (Territory Lookup)

Derive `hubspot_owner_id` from `state` using the territory map in property-schema.md:

| State | Owner ID | Owner |
|---|---|---|
| AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV | `161889085` | Tim Lieto (East) |
| AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY | `162339176` | Ken Cunningham (West) |
| Non-US (any `country` that is not "United States" or "US") | `159350430` | Tim Ziemer (International) |
| State unknown or blank | *(leave blank)* | Manual routing required |

### 2G: Hyperscaler Proximity Values

Values pass through directly from enrichment. Valid values:
- `Announced: <50 miles`
- `Announced: 50-200 miles`
- `Existing Facility Nearby`
- `None Known`

If the enrichment output is blank or missing, set to `None Known`.

### 2H: Key Tenant Segments (Colo Only)

Multi-select, semicolon-separated. Only populate for colo operators. Valid values:
`cloud_providers`, `enterprises`, `carriers`, `content__hyperscale`, `financial_services`, `other`

Example: `cloud_providers;enterprises;carriers`

If the enrichment output is blank for a colo operator, leave blank (do not guess).
If the account is not a colo operator, leave blank.

---

## STEP 3: Identify Edge Cases Within Excludes

**Edge cases are accounts that were excluded BUT have characteristics suggesting they might qualify.** Flag these for the edge-case-researcher skill to perform deeper investigation.

### Edge Case Rules

| Rule | Trigger | Recommended Research |
|------|---------|----------------------|
| **Retail ISP with Infrastructure Signals** | `customer_employee_count < 100` AND has "fiber", "wavelength", "dark fiber" in research notes AND state is not blank | Check for wholesale/B2B division |
| **Low Employee Count with Infrastructure Metrics** | `customer_employee_count < 50` AND website mentions "data center", "POPs", "network", OR company name contains "cooperative" | Employee count data error? Check infrastructure reality. |
| **Insufficient Data** | `segmentation_confidence = LOW` AND has partial segment signals OR company name is generic/ambiguous | Try deeper searches with state/domain context |
| **Vendor/Contractor with Infrastructure Overlap** | Company classified as vendor/contractor BUT research notes mention "fiber network", "colo", "owns operates" | Dual business model? May operate real infrastructure. |

For each edge case identified, output to `edge_cases_for_research.xlsx`:
- All original fields from qualified batch
- `edge_case_rule` (the rule that triggered)
- `edge_case_reason` (specific finding that triggered it)
- `recommended_research` (what to investigate further)

---

## STEP 4: Produce Definitive Excludes Log

All other excluded records (that don't match edge case rules):
- `company_name`, `company_domain`, `exclusion_reason`
- `exclusion_category` (normalized, standardized labels)
- Audit trail  -  what was researched and why excluded

Exclusion categories:
- `Non-Target Vertical`  -  Staffing, software, consulting, manufacturing (not telecom/infra)
- `Retail ISP Only`  -  Confirmed residential broadband, no wholesale
- `Insufficient Data`  -  Couldn't determine classification with available data
- `Defunct / Inactive`  -  Company no longer operating or domain parked
- `Duplicate`  -  Already in HubSpot
- `Parent/Subsidiary`  -  Not decision-maker level, subsidiary of larger company
- `Vendor/Contractor`  -  No infrastructure ownership

---

## OUTPUT FILES

### File 1: Qualified Accounts (HubSpot Import Ready)
- Filename: `qualified_accounts_[date].xlsx`
- Columns: Exact HubSpot property names
- Values: HubSpot enum labels (not bot output labels)
- Format: Ready for HubSpot drag-and-drop import
- No header row translation needed

### File 2: Edge Cases for Researcher Skill
- Filename: `edge_cases_for_research_[date].xlsx`
- Includes: Original fields + edge_case_rule + edge_case_reason + recommended_research
- For: Passing to edge-case-researcher skill for deep-dive investigation

### File 3: Definitive Excludes
- Filename: `definitive_excludes_[date].xlsx`
- Includes: company_name, domain, exclusion_reason, exclusion_category, research_notes
- For: Audit trail and occasional manual review
