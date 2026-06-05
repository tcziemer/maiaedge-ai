# MaiaEdge Contact Schema & Properties

> Last updated: March 2026
> **This is the reference for all contact-level properties, enrichment flow, and persona framework.**

---

## 1. Contact Properties Reference

### Identity & Basics

| Property | Internal Name | Type | Notes |
|----------|--------------|------|-------|
| First Name | `firstname` | String | Required for outreach |
| Last Name | `lastname` | String | Required for outreach |
| Email | `email` | String | Primary identifier for dedup |
| Job Title | `jobtitle` | String | Used for persona mapping |
| Phone | `phone` | String | Direct phone number |
| Company | `company` | String | Company name (text, not association) |
| LinkedIn URL | `linkedin_url` | String | LinkedIn profile link |
| Company HQ Phone | `company_hq_phone` | String | Company main phone (separate from direct) |

### Ownership & Lifecycle

| Property | Internal Name | Type | Notes |
|----------|--------------|------|-------|
| Contact Owner | `hubspot_owner_id` | Owner | Inherits from associated company owner |
| Lifecycle Stage | `lifecyclestage` | Enum | See hubspot-values.md for internal values |

### Hygiene & Data Quality

| Property | Internal Name | Type | Notes |
|----------|--------------|------|-------|
| Flagged for Deletion | `flagged_for_deletion` | Boolean (`"true"` / `"false"`) | Single checkbox. Set by CRM Guardian pre-deletion audit (see `skills/pre-deletion-audit`). Only `true` after all gates pass: associated company is non-ICP AND contact has no activity within 90 days AND contact is not associated to any open deal. Never set by enrichment. Never auto-archived — humans finalize deletion in Tier 3 review. |
| Marketing Contact Status | `hs_marketable_status` | Enum (`"true"` = Marketing contact / `"false"` = Non-marketing contact) | **Every contact auto-created by CRM Guardian (contact-discovery Modes 3 and 4) must be created with `hs_marketable_status = "false"` (non-marketing).** This keeps MaiaEdge's paid marketing contact tier from silently inflating as the routine fills persona gaps and job-change replacements. A rep can flip a contact to marketing (`"true"`) manually when they decide to run marketing touch. The default is sales-only. |

### Segmentation

| Property | Internal Name | Type | Notes |
|----------|--------------|------|-------|
| Customer Segment | `customer_segment` | Enum | Same values as company `customer_segment`. See property-schema.md Section 2 |

### Account Insights (Synced from Company Enrichment)

These fields are populated on contacts with the same content as their company-level equivalents. They enable per-contact outreach personalization while the company record remains the source of truth.

| Property | Internal Name | Type | Company Equivalent | Description |
|----------|--------------|------|-------------------|-------------|
| Company Brief | `company_brief` | String | `account_brief` | 3-6 sentence company overview |
| MaiaEdge Value Prop | `maiaedge_value_prop` | String | `maiaedge_value_proposition` | Copy-paste email body with prospect situation + problem + MaiaEdge solution |
| Provisioning Landscape | `provisioning_landscape` | String | `provisioning_landscape` | Narrative of fabric/provisioning approach (same field name on both objects) |
| Recent Trigger/News | `recent_triggernews` | String | `recent_news_or_trigger_event` | Recent expansion, funding, leadership change |

### Outreach Email Bodies

These are **email BODY TEXT** fields, not email addresses. They contain pre-written email content tailored to the contact's persona.

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Technical Email | `technical_email` | String | Email body for technical personas (VP Eng, Network Architect, CTO) |
| Non-Technical Email | `nontechnical_email` | String | Email body for business personas (VP Ops, COO, VP Product) |
| DM Email | `dm_email` | String | Email body for decision-maker personas (CEO, CFO) |

### MEDDPICC (Contact-Level) — AUTHORITATIVE LOCATION

**Contact-level MEDDPICC is the source of truth for all MEDDPICC data in this CRM.** Per Cooper's design (see `call-schema.md` → MEDDPICC and Call Transcripts -- Critical Rule), HubSpot's smart-property auto-fill from call transcripts only targets contacts. A property-sync workflow then propagates these contact-level values up to the corresponding deal-level MEDDPICC fields. **All routine writes target contacts; deal-level fills automatically.**

| MEDDPICC Concept | Internal Name | Type | Description |
|------------------|---------------|------|-------------|
| Identified Pain | `meddpicc_pain_contact` | String | Pain points named or implied by this contact in discovery |
| Decision Criteria | `meddpicc_criteria_contact` | String | What this contact says will drive vendor selection |
| Metrics | `meddpicc_metrics_contact` | String | Success metrics this contact uses to evaluate the buy |
| Use Case | `meddpicc_use_case` | String | Primary use case as articulated by this contact |
| Competition | `meddpicc_competition_contact` | String | Competitive alternatives this contact mentions |
| Infrastructure | `meddpicc_infrastructure_contact` | String | Infrastructure context this contact provides |
| Buying Process | `buying_process___meddpicc` | String | Buying process notes (3 underscores between `process` and `meddpicc`) |
| Key Stakeholders | `key_stakeholders___meddpicc` | String | Stakeholder map per this contact (3 underscores between `stakeholders` and `meddpicc`) |

**Per-contact attribution:** when 3 prospects are on the same call, each contact's MEDDPICC is updated independently against its own lifetime call count. The transcript evidence is shared across the call but the populated/empty state is per-contact.

**Don't confuse with deal-level mirror fields:** the deal object has fields with similar names (e.g. `identified_pain_meddpicc`, `decision_criteria___meddpicc`) — those are the auto-synced mirrors and should never be written directly. See `deals-schema.md` → "MEDDPICC Fields" for the full mirror list.

### Standard HubSpot Properties (Key Ones)

| Property | Internal Name | Type | Notes |
|----------|--------------|------|-------|
| Create Date | `createdate` | DateTime | Auto-populated on creation |
| Last Contacted | `notes_last_contacted` | DateTime | Last activity timestamp |
| Last Activity Date | `notes_last_updated` | DateTime | Last record update |

---

## 2. Company-to-Contact Field Deduplication

The enrichment pipeline populates BOTH company-level and contact-level fields with identical content. This table maps corresponding fields:

| Context | Company Field | Contact Field | Notes |
|---------|--------------|---------------|-------|
| Company overview | `account_brief` | `company_brief` | Use company for deal context, contact for individual outreach |
| Value proposition | `maiaedge_value_proposition` | `maiaedge_value_prop` | Same content. Company for deal narrative, contact for email |
| Provisioning | `provisioning_landscape` | `provisioning_landscape` | Same field name on both objects |
| Trigger events | `recent_news_or_trigger_event` | `recent_triggernews` | Same content, different field names |
| Email bodies | `technical_email` / `nontechnical_email` / `dm_email` | Same field names | Exist on both objects. These are email BODY TEXT, not addresses |

**Best practice:** Reference company-level fields for account-wide strategy. Use contact-level fields for individual outreach (emails, calls, LinkedIn).

---

## 3. Contact Enrichment Flow

Contacts are **NOT independently enriched**. The enrichment pipeline only touches company records. Contact-level fields are populated through:

1. **Company enrichment sync** -- When a company is enriched, the account_brief/value_prop/trigger content is copied to associated contacts
2. **SDR pipeline output** -- The `sdr-pipeline` skill generates persona-specific email bodies (technical_email, nontechnical_email, dm_email) that get applied to contacts
3. **Manual entry** -- MEDDPICC fields, buying role, and other deal-specific context are entered by AEs during sales engagement

### Contact Sources

Contacts typically enter HubSpot from:
- **Apollo.io** -- Contact discovery and prospecting
- **LinkedIn** -- Manual import or Sales Navigator
- **Inbound** -- Form submissions, event registrations
- **Import** -- Bulk CSV imports from enrichment or event processing

---

## 4. Persona Framework

Target personas by buying committee role. Used by the `contact-discovery` skill for persona gap analysis.

### Buying Committee Roles

| Role | Typical Titles | Function |
|------|---------------|----------|
| **Technical Champion** | VP Engineering, Director Network Ops, Network Architect, CTO | Evaluates technical fit, drives internal adoption |
| **Business Sponsor** | VP Operations, COO, VP Product, VP Sales | Owns business case, budget alignment |
| **Economic Buyer** | CFO, CEO (early-stage), VP Finance | Final budget approval |
| **Procurement** | Director of Procurement, Vendor Management | Contract negotiation, compliance |

### Persona Coverage by Segment

| Segment | Priority Personas | Typical Multi-Thread Target |
|---------|-------------------|---------------------------|
| **Colocation** | VP Network Ops, VP Sales, CFO | 2-3 contacts minimum |
| **Fiber Operator** | VP Engineering, VP Operations, CEO | 2-3 contacts minimum |
| **NeoCloud** | CTO, VP Infrastructure, CEO | 2 contacts minimum |
| **Network Operator** | VP Network, VP Product, CFO | 3+ contacts for large orgs |
| **MSP/Aggregator** | VP Operations, CEO | 2 contacts minimum |

### Contact Coverage Health

| Contacts per Company | Assessment |
|---------------------|------------|
| 0 | No coverage -- needs prospecting |
| 1 | Single-threaded -- at risk |
| 2-3 | Healthy -- multi-threaded |
| 4+ | Strong -- deep engagement |

---

## 5. Contact Import Template

For HubSpot contact imports, use these exact column headers:

```csv
First Name,Last Name,Email,Job Title,Phone,Company Domain Name,Contact owner,Lifecycle Stage,Customer segment
```

### Default Values for New Contacts

| Property | Default Value | Notes |
|----------|--------------|-------|
| `lifecyclestage` | `lead` | New contacts from prospecting |
| `hubspot_owner_id` | Inherit from company | Match company territory owner |

---

## 6. Contact Ownership Rules

- Contact owner should match the associated company owner (territory-based)
- When a contact is created via import, set `hubspot_owner_id` based on the associated company's territory assignment
- See `territory-model.md` for state-to-owner mapping
- Strategic exceptions: Leadership can reassign individual contacts with documented reason
