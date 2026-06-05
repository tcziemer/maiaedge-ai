---
name: import-processor
description: "MaiaEdge file-to-HubSpot-import transform. Use ONLY when the user hands you an existing CSV/XLSX of enrichment output (e.g. a historical export, a manually-prepared spreadsheet, a partner-supplied list) and asks for an import-ready file. For any workflow that starts with company names or domains - use `company-enrichment` instead, which writes directly to HubSpot via MCP. When this skill does run: transforms all values to match HubSpot property labels, separates edge cases for deeper research, produces definitive excludes log with normalized categories. Input: 33-column enrichment output XLSX/CSV. Output: (1) Qualified accounts ready for HubSpot import, (2) Edge cases flagged for researcher skill, (3) Definitive excludes. Zero manual adjustment required - column headers match HubSpot properties, values match enums, multi-checkbox delimited correctly."
---

# MaiaEdge Enrichment Import Processor

> **File-to-import transform only.** Do not invoke unless the user has handed you an existing CSV/XLSX file and explicitly wants an import-ready spreadsheet. For any request that starts with company names or domains ("enrich these companies", "classify this list"), use `company-enrichment` instead - it writes directly to HubSpot via MCP and no import file is needed.

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
| `MSP/Aggregator` | `MSP/Aggregator` |
| `Enterprise` | `Enterprise-CustomerSegment` |

> ⚠️ **CHANGE:** `AI - Colocation Operator` is DEPRECATED. AI colos now use `Data Center Colo Provider` + `company_sub_segment = AI Signals - colo`.

**Sub-Segment Mapping** (bot output → HubSpot `company_sub_segment` value):

Writes are validated against the **30 active sub-segment enum values** in `context/account-tiering/sub-segment-qualification.md`. HubSpot enums are CASE-SENSITIVE - exact case must be preserved as encoded below. See §"Enum Case-Sensitivity Reference" at the bottom of this skill (and `context/hubspot/property-schema.md` Appendix) for the complete authoritative list.

**ONLY the 30 active values below are accepted. Any value not in this table is REJECTED.**

| Bot `customer_sub_segment` (incoming) | -> HubSpot `company_sub_segment` Value (exact, case-sensitive) |
|---|---|
| **Data Center Colo Provider (4 + Greenfield)** | |
| `Standard` / `Standard Colo` | `Standard - colo` *(FRAMEWORK DEFAULT - see §"Framework Default Flagging" below)* |
| `AI Signals` / `AI Infrastructure` | `AI Signals - colo` |
| `Modular` / `Modular Colo` / `Edge Pod` | `Modular - colo` |
| `Hyperscale Wholesale` / `Wholesale Colo` | `Hyperscale Wholesale - colo` |
| `Greenfield Colo` | `Greenfield` (pairs with `customer_segment = Data Center Colo Provider`) |
| **NeoCloud (5 + Greenfield)** | |
| `Large-Scale GPU NeoClouds` / `Large Scale GPU` | `Large Scale GPU - Neocloud` |
| `Tier 1 Inference Providers` / `Tier 1 Inference` | `Tier 1 Inference - Neocloud` |
| `AI Infrastructure Providers` / `AI Infra Providers` | `AI Infrastructure providers - Neocloud` (lowercase "p" on providers) |
| `Sovereign AI Clouds` | `Sovereign AI Clouds - Neocloud` |
| `Crypto-to-AI Pivots` / `Crypto to AI` | `Crypto to AI - Neoclouds` (trailing "s" on Neoclouds; INCLUSIVE of operator AND landlord per Cooper 2026-05-14) |
| `Greenfield NeoCloud` | `Greenfield` (pairs with `customer_segment = NeoCloud`) |
| **Fiber Operator (6)** | |
| `Regional CLEC` | `Regional CLEC - Fiber operator` *(FRAMEWORK DEFAULT - see §"Framework Default Flagging" below)* |
| `Long-Haul / Backbone` / `Long Haul Backbone` | `Long Haul / Backbone - Fiber operator` |
| `Dark Fiber Specialist` | `Dark Fiber Specialist - Fiber Operator` (capital "O" on Operator - the ONLY Fiber sub-segment that capitalizes "Operator") |
| `Tier 2 National Wholesale` / `Tier 2 Wholesale Fiber` | `Tier 2 National Wholesale - Fiber operator` |
| `Regional Cable Operator` | `Regional Cable Operator - Fiber operator` |
| `Municipal / Cooperative` / `Muni Coop` | `Municipal / Cooperative - Fiber operator` |
| **Network Operator(Tier 1 / VNO) (5)** | |
| `Tier 1 Carrier` | `Tier 1 Carrier - Network Op` |
| `Pure Wholesale Carrier` / `Pure Wholesale` | `Pure Wholesale Carrier - Network Op` |
| `Cable MSO Enterprise Division` | `Cable MSO Enterprise Division - Network Op` |
| `International Backbone Specialist` | `International Backbone Specialist - Network Op` |
| `Subsea Cable Operator` / `Subsea` | `Subsea cable operator` (lowercase "c" and "o"; NO `- Network Op` suffix; NEW 2026-05-14, 30th active value) |
| **MSP/Aggregator (5)** | |
| `Telecom Aggregator` | `Telecom Aggregator - MSP` *(FRAMEWORK DEFAULT - see §"Framework Default Flagging" below)* |
| `Managed Network Services` / `Managed Net Services` | `Managed Network Services - MSP` (post-Phase 1.7c.1; `- Network Operator` legacy suffix archived 2026-05-13) |
| `TSD` / `Technology Services Distributor` | `TSD Technology Services Distributor - MSP` |
| `Master Agent` | `Master Agent - MSP` |
| `Cloud + Telecom Hybrid MSP` / `Cloud Telecom Hybrid` | `Cloud + Telecom Hybrid MSP - MSP` |
| **Enterprise-CustomerSegment (4)** | |
| `Financial Services - Enterprise` | `Financial Services - Enterprise` |
| `Healthcare Systems - Enterprise` | `Healthcare Systems - Enterprise` |
| `Retail and Distribution - Enterprise` | `Retail and Distribution - Enterprise` |
| `Outsourcing Services - Enterprise` | `Outsourcing Services - Enterprise` |

**REJECT (not active, never write):** `Hyperscaler - colo`, `Wholesale - colo`, `Metro Fiber - Fiber operator`, `Tier 2 Carrier - Network Op`, `Wholesale carrier - Network Op`, `Satellite operator - Network Op`, `Cloud Connectivity Specialist - MSP`, `SD-WAN Specialist - MSP`. These were not in the live HubSpot enum verified 2026-05-14. Any write attempt with these values must error with: `"Invalid sub-segment 'X' - not one of the 30 active values. See context/account-tiering/sub-segment-qualification.md."`

> The `customer_segment = "Enterprise-CustomerSegment"` parent uses the internal value `Enterprise-CustomerSegment` (the display label is `Enterprise`). `Standard - colo` includes the framework-default flagging rule too - see §"Framework Default Flagging" below.

### 2B.1: REJECTED Sub-Segment Values (Retired - Hard Error)

Three values were retired 2026-05-13 (Phase 1.6), and a fourth pre-Phase-1.7c.1 form was retired the same date. Any write request targeting these MUST be rejected with the error message shown:

| Retired Value | Error to Raise |
|---|---|
| `Co-op/consortium` | `"Retired enum value 'Co-op/consortium' - archived 2026-05-13 Phase 1.6. Replacement: 'Municipal / Cooperative - Fiber operator'"` |
| `External Extension - Network operator` | `"Retired enum value 'External Extension - Network operator' - archived 2026-05-13 Phase 1.6. Replacement: set network_op_track = external_extension"` |
| `Internal + external unification - Network Operator` | `"Retired enum value 'Internal + external unification - Network Operator' - archived 2026-05-13 Phase 1.6. Replacement: set network_op_track = internal_external_unification"` |
| `Managed Network Services - Network Operator` | `"Pre-Phase 1.7c.1 suffix - use 'Managed Network Services - MSP' instead"` |

Do NOT silently rewrite - raise the error and route the record to the edge-case-researcher skill for manual review.

### 2B.2: Framework Default Flagging

Three sub-segment values are framework defaults (the bot tends to assign them when nothing else fits). Writes to these values must be VERIFIED with positive-evidence reasoning:

- `Regional CLEC - Fiber operator`
- `Standard - colo`
- `Telecom Aggregator - MSP`

For each write to one of the above, the bot's reasoning string MUST contain positive evidence (e.g., "FCC BDC entry shows 12-county CLEC footprint" or "DataCenterMap listing confirms standalone colo with 3 DCs in TX"). Negative-exclusion reasoning ("not long-haul, not dark-fiber-specialist, not metro-fiber, therefore CLEC") is INSUFFICIENT.

If only negative-exclusion reasoning is supplied:
1. Downgrade `segmentation_confidence` to `low_5069`
2. Route the record to R2 Stale Re-Enrichment + D7 Edge Case Resolution
3. Add a `_ref_framework_default_unverified` flag column

### 2B.3: Cross-Segment Pairing Validation

- `company_sub_segment = "Greenfield"` is valid ONLY when `customer_segment IN ("Data Center Colo Provider", "NeoCloud")`. Reject any other pairing.
- `company_sub_segment = "Subsea cable operator"` is valid ONLY when `customer_segment = "Network Operator(Tier 1 / VNO)"`. Accept this pair without modification - the lowercase / no-suffix form is intentional.

### 2B.4: customer_segment Enum Validation

Writes to `customer_segment` are validated against these 10 active values (case-sensitive):

```
Network Operator(Tier 1 / VNO)
Data Center Colo Provider
Fiber Operator
MSP/Aggregator
Enterprise-CustomerSegment
NeoCloud
Partner Target
Other
Unknown
Flagged for deletion
```

Note: `Network Operator(Tier 1 / VNO)` has NO space before the open parenthesis. `MSP/Aggregator` retired its former `Enterprise` internal value 2026-05-07.

### 2B.5: network_op_track Enum Validation

Writes to `network_op_track` are validated against these 2 active values:

- `external_extension`
- `internal_external_unification`

This replaces the retired `External Extension - Network operator` and `Internal + external unification - Network Operator` sub-segment values.

### 2B.6: segmentation_confidence Enum Validation

Writes to `segmentation_confidence` are validated against these 4 active values:

- `high_90`
- `medium_7089`
- `low_5069`
- `manual_review_required`

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

> **Enterprise tier ceiling:** For `customer_segment = "Enterprise-CustomerSegment"` records, the Tier 2 enum is the maximum tier the enrichment pipeline assigns - there is no Tier 1 path for Enterprise unless an exceptional trigger emerges. If the bot output is `TIER_1_STRATEGIC` for an Enterprise record, downgrade to `tier_2` during transform and flag for review.

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
| **Enterprise Missing Scale Signals** | `customer_segment = "Enterprise-CustomerSegment"` AND any one of: `infrastructure_profile` is blank or shows only `Facilities: Small (<5)` or `None Identified`, OR no in-house network engineering signal in research notes, OR revenue evidence is missing/under $1B | Verify scale gate (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). If fails → reclassify to `Other`. If passes → confirm sub-segment matches one of the four Enterprise ICP values. |
| **Enterprise Vertical Gate Failure** | `customer_segment = "Enterprise-CustomerSegment"` AND vertical does NOT map to Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services (e.g., Manufacturing, Energy/Utilities, Logistics, Government, SaaS-only) | Reclassify to `Other` (Watch List) or `Unknown`. Do NOT assign an Enterprise sub-segment to these. |
| **Enterprise Outsourcing/Consulting Ambiguity** | `customer_sub_segment = "Outsourcing Services - Enterprise"` AND company is a known dual-arm firm (Cognizant, Accenture, etc.) OR a project-based consulting firm (Deloitte, McKinsey, BCG, Bain) | For dual-arm: classify on operational delivery revenue mix. For pure consulting: reclassify to `Other`. |

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

---

## REFERENCE FILES (read before validating writes)

- `context/account-tiering/sub-segment-qualification.md` - authoritative list of the 30 active sub-segment values, parent/sub-segment pairing rules, case-sensitivity quirks
- `context/account-tiering/enrichment-protocols.md` - D5 evidence verification protocols, D2 wholesale-arm policy, D1 disqualifiers
- `context/hubspot/property-schema.md` Appendix - Enum Case-Sensitivity Reference (mirrors §"Enum Case-Sensitivity Reference" below)

---

## ENUM CASE-SENSITIVITY REFERENCE (authoritative)

HubSpot rejects writes where the value casing does not match the enum definition exactly. The following quirks have caused production write failures and must be preserved verbatim:

| Value | Quirk |
|---|---|
| `Dark Fiber Specialist - Fiber Operator` | Capital `O` on Operator (NOT `operator`) |
| `AI Infrastructure providers - Neocloud` | Lowercase `p` on providers |
| `Crypto to AI - Neoclouds` | Trailing `s` on Neoclouds (the only `Neocloud` sub-segment that ends in `s`) |
| `Network Operator(Tier 1 / VNO)` | No space before the open paren - this is the `customer_segment` value |
| `Subsea cable operator` | All lowercase, NO `- Network Op` suffix |
| `Managed Network Services - MSP` | Post-Phase 1.7c.1 (`- Network Operator` form is retired) |
| `Enterprise-CustomerSegment` | Internal value (display label is `Enterprise`); the hyphen is part of the value |

All 30 active sub-segment values, in full:

**The 30 active values (verified via HubSpot MCP `get_properties` 2026-05-14 against portal 242063281):**

```
# Data Center Colo Provider (4)
Standard - colo
AI Signals - colo
Modular - colo
Hyperscale Wholesale - colo

# NeoCloud (5)
Large Scale GPU - Neocloud
Tier 1 Inference - Neocloud
AI Infrastructure providers - Neocloud      # lowercase "p" on providers
Sovereign AI Clouds - Neocloud
Crypto to AI - Neoclouds                    # trailing "s" on Neoclouds

# Fiber Operator (6)
Regional CLEC - Fiber operator
Long Haul / Backbone - Fiber operator
Dark Fiber Specialist - Fiber Operator      # capital "O" on Operator
Tier 2 National Wholesale - Fiber operator
Regional Cable Operator - Fiber operator
Municipal / Cooperative - Fiber operator

# Network Operator(Tier 1 / VNO) (5)
Tier 1 Carrier - Network Op
Pure Wholesale Carrier - Network Op
Cable MSO Enterprise Division - Network Op
International Backbone Specialist - Network Op
Subsea cable operator                       # lowercase "c" and "o"; NO "- Network Op" suffix; 30th active value, NEW 2026-05-14

# MSP/Aggregator (5)
Telecom Aggregator - MSP
Managed Network Services - MSP              # "- MSP" suffix post-Phase 1.7c.1
TSD Technology Services Distributor - MSP
Master Agent - MSP
Cloud + Telecom Hybrid MSP - MSP

# Enterprise-CustomerSegment (4)
Financial Services - Enterprise
Healthcare Systems - Enterprise
Retail and Distribution - Enterprise
Outsourcing Services - Enterprise

# Cross-segment (1)
Greenfield                                  # pairs with Data Center Colo Provider OR NeoCloud parent
```

Total = 30. The cross-segment `Greenfield` value pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` customer_segment parent per Cooper 2026-05-14. See `context/account-tiering/sub-segment-qualification.md` for the canonical reference.

**Retired values (archived 2026-05-13 Phase 1.6 - reject with error):** `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `Managed Network Services - Network Operator` (pre-Phase 1.7c.1 suffix).
