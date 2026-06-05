# MaiaEdge POC Ticket Schema & Properties

> Last updated: March 2026
> **This is the reference for the POC Pipeline, all 98 ticket properties, conditional logic, workflows, and sidebar layout.**

A POC (Proof of Concept) is a trial run of MaiaEdge PBC devices in a prospect's network to prove use cases before purchase. POCs are managed as Tickets in HubSpot using a dedicated POC Pipeline.

---

## 1. POC Pipeline

**Pipeline Name:** POC Pipeline
**Object:** Tickets

### Stages (10 stages)

| # | Internal Value | Display Label | Status | Description |
|---|---|---|---|---|
| 1 | `1` | POC Requested | Open | New POC request submitted |
| 2 | `2` | Scoping | Open | Defining success criteria and site requirements |
| 3 | `2203327170` | Criteria Approved | Open | Success criteria submitted for leadership approval |
| 4 | `2203327171` | Configuration Locked | Open | Hardware config finalized, build tasks pushed to engineering |
| 5 | `2611948268` | Building & Preparing for Shipment | Open | Hardware being built and prepared |
| 6 | `3329075934` | Shipped | Open | Hardware shipped to customer site(s) |
| 7 | `3329085138` | Customer Testing | Open | Customer actively running POC tests |
| 8 | `3329075912` | On Hold | Open | POC paused (blocked, customer delay, etc.) |
| 9 | `2203327172` | POC Successful | Closed | POC met success criteria, proceed to deal |
| 10 | `2203327173` | POC Unsuccessful | Closed | POC did not meet success criteria |

### Stage Flow

```
POC Requested → Scoping → Criteria Approved → Configuration Locked
→ Building & Preparing for Shipment → Shipped → Customer Testing
→ POC Successful (closed) or POC Unsuccessful (closed)

On Hold can be entered from any open stage
```

---

## 2. Property Groups & Properties (98 Total)

### Group: POC Status (4 properties)

| Property | Internal Name | Type | Options / Description |
|----------|--------------|------|----------------------|
| POC Trend | `poc_trend` | Dropdown | On Track, Needs Attention, At Risk, Blocked, On Hold. Default: On Track |
| Last Next Step | `poc_next_step` | Multi-line text | Current most critical action with inline dates |
| Feature Requests | `poc_feature_requests` | Multi-line text | Running log of product feature requests during POC |
| Bugs | `poc_bugs` | Multi-line text | Running log of bugs/issues discovered during POC |

### Group: POC General Info (4 properties)

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| CS Assignment | `poc_cs_assignment` | HubSpot user | Customer Success contact if assigned |
| Start Date | `poc_start_date` | Date | Target POC start date |
| End Date | `poc_end_date` | Date | Target POC end date |
| Design Doc Link | `poc_design_doc_link` | Single-line text | URL to SE design document |

### Group: POC Success Criteria (4 properties)

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Success Criteria | `poc_success_criteria` | Multi-line text | What the POC needs to prove (POC-wide, not per-site) |
| Approval Status | `poc_approval_status` | Dropdown | Pending, Approval Requested, Approved, Conditional Approval, Denied. Default: Pending |
| Approval Notes | `poc_conditional_notes` | Multi-line text | Required when Approval Status = Conditional Approval |
| Denied Notes | `poc_denied_notes` | Multi-line text | Required when Approval Status = Denied |

### Group: POC Sites (1 property)

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Number of Sites | `poc_number_of_sites` | Dropdown | 1-5. Controls which site sections are visible. Default: 2 |

### Groups: Site 1-5 Configuration (12 properties each, 60 total)

Each site follows the same pattern. Replace `N` with site number (1-5). Group name: "Site N - Configuration".

| Property | Internal Name | Type | Options / Description |
|----------|--------------|------|----------------------|
| Site N Location | `site_N_location` | Single-line text | City/facility name (e.g., "Equinix MI1, Miami FL") |
| Site N Shipping Address | `site_N_shipping_address` | Multi-line text | Full shipping address |
| Site N On-Site Contact | `site_N_onsite_contact` | Single-line text | Name and phone of on-site contact |
| Site N Configuration Type | `site_N_config_type` | Dropdown | PBC Only, PBC + Switch |
| Site N PBC Quantity | `site_N_pbc_quantity` | Number | PBCs for this site. Default: 1 |
| Site N SFP Optical Quantity | `site_N_sfp_optical_qty` | Number | Optical SFPs (switch access ports). Only when Config Type = PBC + Switch. Default: 4 |
| Site N SFP Copper Quantity | `site_N_sfp_copper_qty` | Number | Copper SFPs (switch DIA ports). Only when Config Type = PBC + Switch. Default: 2 |
| Site N Fiber Cable Quantity | `site_N_fiber_cable_qty` | Number | 3m fiber cables needed. Default: 0 |
| Site N Power Supply Type | `site_N_power_supply_type` | Dropdown | AC, DC. Default: AC |
| Site N Power Cable Type | `site_N_power_cable_type` | Dropdown | C13, C14. Only when Power Supply = AC |
| Site N Fan Direction | `site_N_fan_direction` | Dropdown | Rear-to-Front, Front-to-Back. Default: Rear-to-Front |
| Site N Hardware Notes | `site_N_hardware_notes` | Multi-line text | Special requests or deviations from defaults |

### Groups: Site 1-5 Readiness (4 properties each, 20 total)

Each site follows the same pattern. Group name: "Site N - Readiness".

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Site N Mgmt Connectivity Confirmed | `site_N_mgmt_connectivity` | Checkbox | Management outbound connectivity confirmed (DNS/NTP) |
| Site N Egress Allow-Lists Approved | `site_N_egress_allowlists` | Checkbox | Egress allow-lists to cloud endpoints approved |
| Site N DIA Confirmed | `site_N_dia_confirmed` | Checkbox | DIA (forwarding interface) confirmed |
| Site N Site Ready | `site_N_site_ready` | Checkbox | Overall site readiness confirmation |

### Group: POC Exit Criteria (5 properties)

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Proof Points Validated | `poc_proof_points_validated` | Checkbox | All defined proof points validated during testing |
| Hardware Validated | `poc_hardware_validated` | Checkbox | Hardware performed as expected |
| Customer Sign-Off Received | `poc_customer_signoff` | Checkbox | Customer formally signed off on results |
| Go/No-Go Documented | `poc_go_nogo_documented` | Checkbox | Internal go/no-go decision documented |
| Additional Proof Points Uncovered | `poc_additional_proof_points` | Multi-line text | Proof points discovered during POC not in original criteria |

### Additional Ticket Properties

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| POC Objective | `poc_type` | Dropdown | Fiber Monetization, Speed to Revenue, Network Extension, Private Connectivity Validation, Competitive Displacement |
| Infrastructure in Scope | `infrastructure_type` | Multi-select | 19 infrastructure types (same values as deal `infrastructure_in_scope`) |
| POC Scoping Document Link | `poc_scoping_document_link` | URL | Link to scoping document |
| Pilot Agreement File | `pilot_agreement_file` | File | Signed pilot agreement upload |
| Last Next Steps | `last_next_steps` | Text | Tracking next steps |
| Notion Doc Link | `notion_doc_link` | URL | Link to Notion documentation |
| POC Success Summary | `poc_success_summary` | Text | Summary when POC succeeds |
| POC Unsuccessful Summary | `poc_unsuccessful_summary` | Text | Summary when POC is unsuccessful |
| POC Unsuccessful Reasons | `poc_unsuccessful_reasons` | Multi-select | Reasons for POC failure |

---

## 3. Conditional Logic (12 Rules)

### Config Type Rules (10 rules, 2 per site)

For each site 1-5:
- **When** `site_N_config_type` = `PBC + Switch` **show** `site_N_sfp_optical_qty` and `site_N_sfp_copper_qty` (both required)
- **When** `site_N_power_supply_type` = `AC` **show** `site_N_power_cable_type` (required)

### Approval Notes Rules (2 rules)

- **When** `poc_approval_status` = `Conditional Approval` **show** `poc_conditional_notes` (required)
- **When** `poc_approval_status` = `Denied` **show** `poc_denied_notes` (required)

---

## 4. Sidebar Layout (15 Sections)

Sections appear on the POC ticket record sidebar in this order:

| # | Section Name | Properties | Conditional? |
|---|---|---|---|
| 1 | Status and Next Steps | poc_trend, poc_next_step, poc_feature_requests, poc_bugs | Always visible |
| 2 | General Info | poc_cs_assignment, poc_start_date, poc_end_date, poc_design_doc_link | Always visible |
| 3 | Success Criteria and Approval | poc_success_criteria, poc_approval_status, poc_conditional_notes, poc_denied_notes | Always visible (notes fields use conditional property logic) |
| 4 | Number of Sites | poc_number_of_sites | Always visible |
| 5 | Site 1 - Config and Hardware | All 12 site_1_ config properties | Always visible |
| 6 | Site 2 - Config and Hardware | All 12 site_2_ config properties | Show when Number of Sites >= 2 |
| 7 | Site 3 - Config and Hardware | All 12 site_3_ config properties | Show when Number of Sites >= 3 |
| 8 | Site 4 - Config and Hardware | All 12 site_4_ config properties | Show when Number of Sites >= 4 |
| 9 | Site 5 - Config and Hardware | All 12 site_5_ config properties | Show when Number of Sites = 5 |
| 10 | Site 1 - Readiness | All 4 site_1_ readiness properties | Always visible |
| 11 | Site 2 - Readiness | All 4 site_2_ readiness properties | Show when Number of Sites >= 2 |
| 12 | Site 3 - Readiness | All 4 site_3_ readiness properties | Show when Number of Sites >= 3 |
| 13 | Site 4 - Readiness | All 4 site_4_ readiness properties | Show when Number of Sites >= 4 |
| 14 | Site 5 - Readiness | All 4 site_5_ readiness properties | Show when Number of Sites = 5 |
| 15 | POC Exit Criteria | poc_proof_points_validated, poc_hardware_validated, poc_customer_signoff, poc_go_nogo_documented, poc_additional_proof_points | Always visible |

---

## 5. Workflows

### Workflow 1: POC Approval Request Notification

- **Trigger:** Ticket enters "Criteria Approved" stage
- **Action:** Send internal email to Abhilash (CEO) and Dragan with ticket name, owner, and success criteria
- **Re-enrollment:** OFF (triggers once per ticket)

### Workflow 2: POC Approval Decision Notification

- **Trigger:** `poc_approval_status` changes to Approved, Conditional Approval, or Denied
- **Action:** If/then branch on approval status:
  - **Approved:** Notify ticket owner, deal contact owner, Tim Ziemer
  - **Conditional Approval:** Same recipients + include conditional notes
  - **Denied:** Same recipients + include denied notes
- **Re-enrollment:** ON (re-triggers if status changes again)

### Workflows 3-7: Site SFP Defaults (Optional, one per site)

- **Trigger:** `site_N_config_type` is set to any value
- **Action:** Auto-populate SFP quantities based on config type

---

## 6. Default Values

| Property | Default Value |
|----------|--------------|
| `poc_trend` | On Track |
| `poc_number_of_sites` | 2 |
| `poc_approval_status` | Pending |
| `site_1-5_pbc_quantity` | 1 (each site) |
| `site_1-5_power_supply_type` | AC (each site) |
| `site_1-5_fan_direction` | Rear-to-Front (each site) |

Total: 18 default values (3 POC-level + 15 site-level at 3 per site)

---

## 7. Relationships

| Association | Direction | Notes |
|-------------|-----------|-------|
| Ticket → Company | Many-to-one | POC is for one company |
| Ticket → Contact | Many-to-many | Primary contact(s) for the POC |
| Ticket → Deal | Many-to-one | POC supports one deal (deal stage should be "POC & Technical Validation") |

### POC Lifecycle in the Sales Process

```
Deal created → Appointment Scheduled → Discovery & Scoping
→ POC ticket created (linked to deal)
→ Deal moves to "POC & Technical Validation" stage
→ POC runs through ticket pipeline
→ POC Successful → Deal moves to "Quote Provided"
→ POC Unsuccessful → Deal may close lost or pivot
```
