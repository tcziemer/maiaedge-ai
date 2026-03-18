---
description: Research a prospect and write a cold email + LinkedIn connection request for MaiaEdge
argument-hint: "[company name] [contact name] [contact title] [sender: Tim or Ken]"
---

# Write Outreach for a MaiaEdge Prospect

Follow this workflow exactly. Do not skip steps.

## Input

The user will provide: company name, contact name, contact title, and optionally which sender (Tim Lieto or Ken Cunningham). If sender is not specified, ask.

Arguments provided: $ARGUMENTS

## Workflow

### 1. Confirm Sender
If not specified, ask: Tim Lieto (AVP, North America Sales) or Ken Cunningham (Sales, East Region)?

### 2. Check Exclusion List
Before researching, verify this isn't an excluded category (IXP, Tower REIT, IT MSP, retail ISP, software vendor, hyperscaler, enterprise, vendor/contractor, consulting firm, trade org, defunct/acquired, under 7 employees). If excluded, flag it and stop.

### 3. Check HubSpot First
Before running web searches, search HubSpot for existing company record using MCP tools (`search_crm_objects`):
- Search by company name or domain
- If account exists, review: segment classification, customer_sub_segment, AI signal flags, territory owner, existing research notes
- If complete classification exists and data is recent, skip Steps 4-5 and go directly to Step 6 (Research the Contact)
- If new account or incomplete data, proceed to Step 4

### 4. Research the Company
Run ALL mandatory web searches:
- `[Company] cloud connectivity provisioning` or `[Company] network automation services`
- `[Company] API portal self-service provisioning`
- `[Company] cross-carrier connectivity multi-carrier`
- `[Company] expansion announcement 2025 2026`

### 5. Check AI Signals
If colocation or fiber operator in an AI corridor:
- `[Company] CoreWeave Lambda Labs Crusoe`
- `[Company] liquid cooling high-density GPU`
- `[Company] AI infrastructure 2025 2026`

### 6. Research the Contact
- `[Name] [Company] LinkedIn`
- Current title, tenure, career history
- Technical vs. business background

### 7. Document Findings
Write a research summary using the standard format:
```
RESEARCH SUMMARY: [Contact Name] at [Company]
ACCOUNT: Company, Segment, What they've built, The gap, AI signals, Recent news
CONTACT: Name, Title, Role type, Background
ANGLE: What this person probably cares about, One-sentence positioning
FIT: EXCELLENT | STRONG | MODERATE | WEAK
```

### 8. Classify Segment and Track
Determine: Fiber Operator, Colocation Operator, AI Colocation Operator, Neocloud, Network Operator, or MSP/Aggregator. For Neoclouds, also assign customer_sub_segment (Large-Scale GPU NeoClouds / Tier 1 Inference Providers / AI Infrastructure Providers / Sovereign AI Clouds / Crypto-to-AI Pivots). For Network Operators, determine Track A (has internal automation) or Track B (fragmented).

### 9. Select the Angle
Before writing, identify the ONE thing happening at this company right now that creates an urgent, MaiaEdge-relevant problem. State it: "[Company] is [doing X], which means [specific operational problem MaiaEdge solves]." If the angle could apply to any company in the segment, research deeper.

### 10. Write the Email
The angle from Step 9 drives the email. The segment messaging framework provides vocabulary and proof points to support the angle, not a template to fill in. Follow all writing rules, word count limits, and tone guidelines. No credibility anchors. Include subject line.

### 11. Write LinkedIn Connection Request
Under 300 characters. Include company-specific detail driven by the angle. No credibility anchors (no Acme Packet).

### 12. Run Quality Checklist
Verify all items pass before delivering.

### 13. Deliver
Present: Research summary, angle used, email with subject line, LinkedIn message, and any quality notes.
