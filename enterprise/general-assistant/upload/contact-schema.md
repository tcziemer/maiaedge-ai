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

### MEDDPICC (Contact-Level)

| Property | Internal Name | Type | Description |
|----------|--------------|------|-------------|
| Buying Process | `buying_process___meddpicc` | String | Buying process notes specific to this contact's perspective |

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
