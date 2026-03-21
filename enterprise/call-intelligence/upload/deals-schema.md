# MaiaEdge Deal Stage Schema & Properties

> Last updated: March 2026
> **This is the operational reference for deal management, MEDDPICC adoption, and pipeline tracking.**

---

## Deal Pipeline & Stages

**Pipeline Name:** "MaiaEdge Deals pipeline"

### Complete Stage Mapping (All 8 Stages)

| Stage | Internal Name | HubSpot ID | Description | Typical Activities |
|-------|---------------|-----------|-------------|-------------------|
| Appointment Scheduled | `appointmentscheduled` | — | Initial meeting booked | Calendar confirmation, pre-call research, context gathering |
| Discovery & Scoping | `qualifiedtobuy` | — | Qualification and needs assessment | Probe ICP fit, identify pain, assess budget/timeline |
| POC & Technical Validation | `presentationscheduled` | — | Proof of concept underway | Deploy POC, validate technical fit, gather performance data |
| Quote Provided | `1996673735` | `1996673735` | Formal pricing delivered | Pricing review, discount negotiation, commercial terms |
| Price Agreement & Final Config | `decisionmakerboughtin` | — | Commercial negotiation | Close on price, finalize term/quantity, get MSA signed |
| Contract Review | `contractsent` | — | Legal review in progress | Monitor signature progress, handle legal objections |
| Closed Won | `closedwon` | — | Deal signed | Onboarding kickoff, deployment scheduling |
| Closed Lost | `closedlost` | — | Deal lost | Capture lost reason, document competitive intelligence |

---

## Deal Properties — Complete Reference

### Actively Used Properties

| Property | Internal Name | Type | Fill Rate | Notes |
|----------|--------------|------|-----------|-------|
| Deal Name | `dealname` | Text | 100% | Required for all deals |
| Deal Stage | `dealstage` | Enum | 100% | Use exact internal names above |
| Pipeline | `pipeline` | Enum | 100% | All use "MaiaEdge Deals pipeline" |
| Deal Owner | `hubspot_owner_id` | Owner | 100% | Tim Lieto, Ken Cunningham, or Timothy Ziemer |
| Close Date | `closedate` | Date | 100% | Target or actual close date |
| Deal Type | `dealtype` | Enum | 70% | Use `newbusiness` when set |
| Customer Segment | `customer_segment` | Enum | 65% | Match company's segment classification |
| Amount (TCV) | `amount` | Currency | 50% | Total Contract Value in USD. Range: $2K–$400K |
| Priority | `hs_priority` | Enum | 45% | `high`, `medium`, or `low` |
| POC Status | `poc_status` | Text | 30% | Status of proof of concept phase |
| Closed Lost Reason | `closed_lost_reason` | Enum | 25% (lost deals only) | Only populate on closed-lost deals |

### MEDDPICC Fields — Adoption Status

**Current adoption: ~45% fill rate across ~20 deals.** Roughly 8-9 deals have MEDDPICC fields populated. All fields show consistent ~40-45% completion, indicating selective adoption by engaged AEs.

| Property | Internal Name | Type | Fill Rate | When to Use |
|----------|--------------|------|-----------|------------|
| Buying Process | `buying_process_meddpicc` | Text | 45% | Capture formal process: RFP, internal committee, vendor eval timeline |
| Identified Pain | `identified_pain_meddpicc` | Text | 45% | Specific pain points from discovery: provisioning delays, visibility gaps, federation challenges |
| Decision Criteria | `decision_criteria___meddpicc` | Text | 45% | What buyer will use to evaluate vendors: speed, sovereignty, federation, cost |
| Key Stakeholders | `key_stakeholders_meddpicc` | Text | 45% | Names/titles of decision-makers: CTO, VP Network, VP Sales, CEO |
| Competition | `competition_meddpicc` | Text | 45% | Competitive alternatives: status quo, Lumen, orchestration platforms, internal build |
| Infrastructure | `infrastructure_meddpicc` | Text | 45% | Current infrastructure details: fiber miles, facility count, routing approach |
| Metrics | `metrics_meddpicc` | Text | 40% | Success metrics: provisioning time reduction, revenue upside, cost savings |
| Use Case | `use_case_meddpicc` | Text | 40% | Primary use case: fiber monetization, colo automation, federation, cloud on-ramp |

**Adoption recommendation:** Prioritize Identified Pain, Key Stakeholders, and Competition as minimum viable MEDDPICC. Add Metrics and Use Case for deals >$50K.

### Deal Info Properties

| Property | Internal Name | Type | Options | Notes |
|----------|--------------|------|---------|-------|
| Deal Source | `deal_source` | Enum | `trade_show`, `founder_network`, `inbound`, `outbound` (Email), `Outbound - Call`, `partner_referral`, `other` | Origin channel |
| Bandwidth Tier | `bandwidth_tier` | Enum | `p_10_gbps` (10 Gbps), `p_100_gbps` (100 Gbps), `tbd` (TBD) | Network capacity |
| Deployment Timeline | `deployment_timeline` | Enum | `all_at_once_30_days`, `phased_13_months`, `phased_36_months`, `phased_612_months`, `ongoing_as_sites_added` | Rollout schedule |
| Target Locations | `target_facilities_for_deployment` | Text | — | Multi-line: facility names and locations |
| Infrastructure in Scope | `infrastructure_in_scope` | Multi-select | 19 options (see hubspot-values.md) | All infrastructure types in the deal |
| Expected PBC Count | `expected_pbc_count` | Number | — | Number of PBC devices expected |
| Wholesale vs Retail Mix | `wholesale_vs_retail_mix__cloned___cloned_` | Enum | `mostly_wholesale_70`, `balanced`, `mostly_retail_70`, `unknown` | Business mix |
| POC Objective | `poc_objective` | Enum | `Fiber Monetization`, `Speed to Revenue`, `Network Extension`, `Private Connectivity Validation`, `Competitive Displacement` | Type of POC |

### Completed Agreements

File upload fields tracking signed legal documents. All are string type (file attachment path).

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Completed NDA | `completed_nda` | String (file) | Signed NDA document |
| Completed Pilot Agreement | `poc_pilot_agreement_signed` | String (file) | Signed POC pilot agreement |
| Completed MSA | `completed_msa` | String (file) | Signed Master Service Agreement |
| Completed Order Form | `completed_order_form` | String (file) | Signed Order Form |

### Quote Approval

| Property | Internal Name | Type | Options / Notes |
|----------|--------------|------|-----------------|
| Quote Number | `quote_number` | Text | — |
| Quote Status | `quote_status` | Enum | `request_approval` (Approval request), `approved`, `changes_requested`, `sent` |
| Amount | `amount` | Currency | Total Contract Value in USD |
| Discount Percentage | `discount_percentage` | Number | Percentage discount applied |
| Discount Reason | `discount_reason` | Text | Justification for discount |
| Contract Term | `contract_term` | Text | Term length (10% fill) |

### Legacy POC Properties (Deprecated)

These deal-level POC fields exist but are **no longer used**. POC tracking has moved to the dedicated POC Pipeline on Tickets. See `poc-schema.md` for the current POC system.

`poc_status`, `poc_start_date`, `poc_end_date`, `poc_pbc_count`, `poc_success_summary`, `poc_unsuccessful_reasons`, `poc_scoping_doc_link`

### Other Low-Usage Properties

`notion_doc_link` (0% fill), `quote_amount` (0%), `quote_sent_date` (0%)

---

## Activity Gate — Deal-Specific Rules

When assessing deal health and activity readiness:

| Last Activity | Gate | Action |
|---|---|---|
| Within 14 days | **🔴 STOP** | Deal is active. Do NOT manually trigger new outreach. Coordinate with deal owner. |
| 15-30 days | **🟡 WARNING** | Recent activity. Check context for pending deliverables (quotes, POC data, legal review). |
| 31-60 days | **🟠 CAUTION** | Going stale. Check deal for blockers. May need executive escalation or deal review. |
| 60+ days | **🟢 CLEAR** | Stale deal. Investigate abandonment or lost reason. Assess re-engagement viability. |

---

## Deal-to-POC Ticket Relationship

Deals can be associated with POC Tickets (managed via the POC Pipeline on the Tickets object). The POC is a trial run of MaiaEdge PBC devices in the prospect's network to prove use cases before purchase.

- **POC management lives on Tickets**, not Deals. Site configuration, hardware specs, readiness checklists, and approval workflows are all on the ticket.
- The deal-level POC fields (`poc_status`, `poc_start_date`, etc.) are **legacy and mostly unused**. The dedicated POC Pipeline replaced them.
- A deal at the "POC & Technical Validation" stage (`presentationscheduled`) should have an associated POC ticket.
- See `poc-schema.md` for the full POC ticket property reference.

---

## Contact vs. Company Field Deduplication

MaiaEdge enrichment pipeline populates BOTH company-level and contact-level fields with identical content. This enables per-contact outreach while maintaining company-level reporting consistency.

### Deduplicated Deal-Relevant Fields

| Context | Company-Level Field | Contact-Level Field | Usage Note |
|---------|-------------------|-------------------|-----------|
| Deal company brief | `account_brief` | `company_brief` | Use company version for deal summary. Contact version for individual outreach. |
| Value proposition | `maiaedge_value_proposition` | `maiaedge_value_prop` | Same content. Use company for deal narrative, contact for email personalization. |
| Provisioning landscape | `provisioning_landscape` | `provisioning_landscape` | Identical. References to competitive fabric adoption or manual processes. |
| Recent trigger events | `recent_news_or_trigger_event` | `recent_triggernews` | Identical. Expansion, funding, leadership change, M&A. |
| Email body content | `technical_email` / `nontechnical_email` / `dm_email` | Same field names | These are email BODY TEXT, not addresses. Populated on both objects. |

**Best practice:** When dealing with a deal, reference company-level fields for account-wide context. When crafting individual contact outreach (emails, calls), use contact-level fields.

---

## Pricing Embedded in Deals

Deals reference actual SKU pricing per MaiaEdge pricing reference. See `pricing-reference.md` for complete SKU table.

When creating order forms and quotes within a deal context:

- **Annual Price** is what appears on Order Forms
- **TCV (Total Contract Value)** is the deal amount in HubSpot
- **HA/Standby units** are 30% off primary units
- **POC pricing:** ME-PBC-PCE-POC60 ($2,490), ME-MPP-48-POC60 ($749) for 60-day proof of concepts
- **Term commitment is the primary discount lever** — 36/60 month terms unlock better per-unit pricing

---

## Deal Health Assessment Framework

Use these metrics to evaluate deal quality and health:

| Metric | Healthy Range | Warning Sign |
|--------|---------------|-------------|
| MEDDPICC completion | 70%+ fields filled | <40% fields filled = low qualification conviction |
| Time in stage | 14–30 days (average) | >60 days = stalled deal |
| Contact depth | 2+ contacts at different levels | Only 1 contact = deal at risk |
| Activity frequency | 1–2 touchpoints per week | 0 touchpoints per week = dormant |
| Deal amount vs. segment | Consistent with SKU tables | <$2K or >$400K = validate pricing |
| POC status clarity | Defined start/end date, success criteria | Vague or undefined = likely to slip |

---

## HubSpot Deal Search & Reporting

### Common Deal Queries

- **Open deals by stage:** Filter by `dealstage` ≠ "closedwon" AND ≠ "closedlost"
- **High-priority deals:** Filter by `hs_priority` = "high" AND `dealstage` ≠ "closedwon"
- **Stale deals:** Filter by last activity >60 days ago AND `dealstage` ≠ "closedwon"
- **MEDDPICC incomplete:** Filter by `buying_process_meddpicc` = empty OR `identified_pain_meddpicc` = empty
- **Deals >$100K:** Filter by `amount` > 100000
- **By segment:** Filter by `customer_segment` = [segment value]
- **By owner:** Filter by `hubspot_owner_id` = [owner ID]

### Deal Pipeline Health Dashboard Metrics

Track these quarterly:

- Total open deals (count and TCV)
- Average time in stage by stage
- Win rate by segment
- Deal velocity (days from first activity to close)
- MEDDPICC adoption rate (% of deals with >70% fields filled)
- Stale deal count (>60 days no activity)
