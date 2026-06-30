---
name: event-intelligence
description: "MaiaEdge conference and event intelligence skill. Use when preparing for a conference, processing attendee or exhibitor lists, building pre-event target lists, planning booth visitor follow-up, or creating post-event outreach sequences. Also trigger when the user mentions GTC, OCP, Supercomputing, Data Centre World, Fiber Connect, MEF, INCOMPAS, PTC, trade show, conference prep, attendee list, exhibitor list, booth visitors, or post-event follow-up. Use this skill any time a conference or industry event is involved in the sales workflow."
---

## Purpose

Maximize ROI from every conference by systematically converting attendee lists into pipeline. Three phases: Pre-Event (research + target prioritization), At-Event (real-time notes), Post-Event (follow-up sequencing).

## Before Starting - Clarify

Two things that determine which mode and how deep to go:

1. **What do you have?** A list (attendee/exhibitor CSV, badge scans, business cards) or a named event you're preparing for before it happens?
2. **What's the goal?** Pre-event target briefing (who to meet), list processing and classification (segment + CRM cross-ref), or post-event follow-up drafts (personalized emails by warmth)?

If you have a list and an event name, share both and I'll start immediately. If you only have an event name with no list yet, I'll pull the exhibitor/speaker roster and build the target briefing.

## Reference Files

**Outreach and voice:**
- `context/copy-strategy/segment-language.md` - Insider vocabulary and conversational patterns per segment. Read before writing follow-up emails to sound like a peer from their world.
- `context/outreach/email-writing-rules.md` - For follow-up email drafts (angle-first, segment lock, no credibility anchors, research as fuel)
- `context/outreach/sender-profiles.md` - Per-sender voice, craft register, and signature protocol for follow-up email attribution (HIGH)
- `context/outreach/voice-gold-standard.md` - Tone and calibration exemplars; governs all written output (HIGH)
- `context/outreach/fallback-messaging.md` - Fallback angles when segment signal is thin (HIGH)
- `context/outreach/persona-targeting-blocklist.md` - Titles and roles to exclude from contact discovery and outreach targeting (HIGH)
- `context/outreach/pre-cadence-hygiene.md` - Pre-send hygiene checks before enrolling contacts in sequences (MEDIUM)

**Qualification and segmentation:**
- `context/core/icp-playbook.md` - ICP definitions and qualification criteria
- `context/core/segment-qualification.md` - Proof-based qualification gates per segment
- `context/account-tiering/d1-global-disqualifiers.md` - Global disqualifiers that block classification before segment routing (MEDIUM)
- `context/copy-strategy/segment-messaging.md` - Angle-selection logic and approved messaging per segment (MEDIUM)
- `context/copy-strategy/scoring-rubric.md` - Email quality scoring dimensions; apply when reviewing follow-up drafts (MEDIUM)

**Segment cheatsheets:**
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/neocloud.md`
- `context/segments/network-operator.md`
- `context/segments/msp-aggregator.md`
- `context/segments/enterprise.md` - Enterprise Multi-DC ICP; 4 sub-segments + hard scale gate (HIGH - required for Enterprise conference processing)
- `context/segments/enterprise-use-cases.md` - Enterprise use-case details and objection handling (MEDIUM)

**Territory and CRM:**
- `context/hubspot/territory-model.md` - Canonical 5-region sender routing map. Read at runtime to assign follow-up sender by HQ state/country.
- `context/hubspot/contact-schema.md` - Contact field set; governs HubSpot contact creation and update from event contacts (HIGH)
- `context/hubspot/deals-schema.md` - Deal fields and stage values for cross-referencing pipeline status (MEDIUM)
- `context/hubspot/property-schema.md` - Company property schema including signal_heat enum and target-account freeze rule (MEDIUM)

**Product and signal:**
- `context/product/proof-points.md` - Verified customer proof points for follow-up personalization (MEDIUM)
- `context/signals/outreach-signal-pushback.md` - Signal push-back write semantics; run as final step when writing follow-up outreach (MEDIUM)

**Enrichment:**
- `context/enrichment/output-schemas.md` - Output schema for enrichment-ready batches produced in Mode 2 (MEDIUM)

**Compliance:**
- `context/europe/europe-email-compliance.md` - Hard legal gate for DE/AT/IT and other EU markets; LinkedIn-first required in those countries (MEDIUM)

## Conference Tiers

**Tier 1 (MaiaEdge attends/exhibits):**
- NVIDIA GTC
- OCP Global Summit
- MEF
- Fiber Connect
- INCOMPAS

**Tier 2 (MaiaEdge monitors/sends reps):**
- SC/Supercomputing
- Data Centre World
- Datacloud Global Congress
- PTC

**Tier 3 (Intelligence gathering only):**
- Regional/niche events
- Webinars with published attendee lists

**Enterprise-relevant conferences (added 2026-05-11 with Enterprise ICP promotion - currently low priority for booth attendance, but flag for future planning + use for attendee processing when Cooper or reps attend):**

By Enterprise sub-segment:

| Conference | Sub-segment | Why Enterprise-relevant | Tier |
|---|---|---|---|
| **Sibos** (annual SWIFT financial-services event) | Financial Services - Enterprise | Where bank CIOs / VP Network Infrastructure converge; DORA + NY DFS Part 500 panels live here | Tier 3 (intel) |
| **Money 20/20** | Financial Services - Enterprise | Payment networks, fintech infra; Visa/Mastercard adjacent | Tier 3 (intel) |
| **AFP Annual Conference** | Financial Services - Enterprise | Corporate treasury + IT - broader than just FS-services BPOs | Tier 3 (intel) |
| **HIMSS** (Healthcare Information & Management Systems Society) | Healthcare Systems - Enterprise | Premier healthcare IT event; CIO + CISO + VP Network Eng at every multi-hospital IDN | Tier 3 (intel) |
| **CHIME** (College of Healthcare Information Management Executives) | Healthcare Systems - Enterprise | Healthcare CIO peer network; HIPAA NPRM + Cal AB 749 panels | Tier 3 (intel) |
| **Becker's Hospital Review IT** | Healthcare Systems - Enterprise | IT-leadership-focused hospital conference; broader than HIMSS | Tier 3 (intel) |
| **ViVE** (HLTH spinoff) | Healthcare Systems - Enterprise | Digital health innovation; AI infrastructure conversations | Tier 3 (intel) |
| **NRF Big Show** (National Retail Federation) | Retail and Distribution - Enterprise | Premier retail-IT event; Walmart / Kroger / Meijer / Target IT leadership; Sparky / WIBEY / Mylow demos | Tier 3 (intel) |
| **Shoptalk** | Retail and Distribution - Enterprise | Retail innovation + tech; smaller than NRF but more architecture-focused | Tier 3 (intel) |
| **RILA Retail CIO Forum** | Retail and Distribution - Enterprise | Retail CIO peer network | Tier 3 (intel) |
| **CCW (Customer Contact Week)** | Outsourcing Services - Enterprise | BPO + contact center industry event; Concentrix / TaskUs / Teleperformance leadership | Tier 3 (intel) |
| **NASSCOM Technology & Leadership Forum** | Outsourcing Services - Enterprise | India IT services + BPO premier event; Cognizant / Infosys / TCS / Wipro / HCL leadership | Tier 3 (intel) |
| **BPO Connect** (Everest Group) | Outsourcing Services - Enterprise | BPO industry roundtable; specifically operational delivery focus | Tier 3 (intel) |

**Default mode for Enterprise conferences:** Intelligence-gathering only (attendee list processing + post-event follow-up to identified Enterprise prospects). Do NOT plan booth presence at Enterprise conferences in 2026 - MaiaEdge GTM bandwidth is reserved for operator-segment events (GTC, OCP, MEF, Fiber Connect, INCOMPAS). Re-evaluate booth presence at HIMSS / NRF / Sibos for 2027 once Meijer-class anchor account references are deployable.

## MODE 1: PRE-CONFERENCE PREP

**Trigger:** "Prep for [conference]" or "Build target list for [event]"

### Steps

1. **Research the event:** Gather dates, location, focus areas, expected attendee/exhibitor profile
2. **Pull exhibitor/speaker list:** Access event website to extract exhibitor and speaker rosters
3. **Cross-reference in HubSpot:** Use `search_crm_objects` to identify which exhibitors are already in the system
4. **Classify by segment:** Apply MaiaEdge customer segment taxonomy:
   - Fiber Operators
   - Colocation/Data Center Providers
   - Neoclouds (GPU cloud)
   - Network Operators/Carriers
   - MSP/Aggregators
   - Vendors/Ecosystem
5. **Check exclusion list:** Filter out competitors, non-targets, and accounts marked "do not contact"
6. **Prioritize targets** by:
   - (a) Existing deal in pipeline (highest signal)
   - (b) Segment/sub-segment fit to MaiaEdge value prop
   - (c) Speaker or exhibitor status (higher intent than attendee-only)
   - (d) Recent company news (expansion, funding, new service launch)
7. **Identify best contact:** For top 20 targets, use HubSpot to find champion contact or Apollo enrichment
8. **Produce target briefing:** Company name, segment, sub-segment, key contact, relevant talking points, any existing relationship status

### Output Format: Pre-Event Target Briefing

```
CONFERENCE: [Event Name]
DATE: [Dates]
LOCATION: [City]
MAIAEDGE PARTICIPATION: [Attending/Exhibiting/Monitoring]
MAIAEDGE TEAM: [Names]
TOTAL EXHIBITORS/SPEAKERS IDENTIFIED: [X]
ALREADY IN CRM: [Y]
NET NEW QUALIFIED TARGETS: [Z]

---

TOP 20 PRIORITIZED TARGETS

| Company | Segment | Sub-Segment | Contact | Title | Email | Phone | Existing Deal? | Talking Point | Intent Signal |
|---------|---------|-------------|---------|-------|-------|-------|----------------|---------------|---------------|
| [Company] | [e.g., Fiber Operator] | [e.g., MSO] | [Name] | [Title] | [Email] | [Phone] | [Yes/No - deal name] | [Segment-specific value] | [Exhibitor/Speaker/Expansion news] |

---

PER-COMPANY BRIEFING NOTES

**[Company 1]**
- HubSpot status: [In CRM / Net New / Excluded]
- Deal stage: [If applicable]
- Key insight: [Recent news, footprint expansion, etc.]
- Talking point: [Peer-to-peer value statement]
- Approach: [Ask for 15-min meeting to discuss infrastructure automation]
- Owner: [Assigned sender per territory-model.md]

---

CONFERENCE-SPECIFIC INTELLIGENCE
[Applied conference-specific context below]
```

## MODE 2: PROCESS ATTENDEE/EXHIBITOR LIST

**Trigger:** "Process this attendee list" or "Classify these exhibitors" (with uploaded file)

### Steps

1. **Parse the file:** Ingest CSV, XLSX, PDF, or pasted list; extract company names, contact info, titles
2. **Cross-reference HubSpot:** For each company, query `search_crm_objects` to check existing accounts
3. **Classify segment:** Apply MaiaEdge segment taxonomy
4. **Check exclusion list:** Remove competitors, non-targets, do-not-contact accounts
5. **Categorize:**
   - **Already in CRM (with active deal):** Company + deal stage + owner
   - **In CRM (no deal):** Company + last activity + next action
   - **Net New Qualified:** Company + segment + assigned customer_segment and customer_sub_segment
   - **Excluded:** Company + reason (competitor, out of scope, etc.)
6. **Produce enrichment-ready batch:** Output file ready for enrichment pipeline (domain, company name, segment)
7. **Summary stats:** Total | Already in CRM | Net New Qualified | Excluded

### Output Format: Classified Attendee Summary

```
ATTENDEE LIST PROCESSING SUMMARY
EVENT: [Name]
DATE PROCESSED: [Date]
TOTAL RECORDS: [X]

---

BREAKDOWN

| Category | Count | % of Total |
|----------|-------|-----------|
| Already in CRM (with deal) | [X] | [%] |
| In CRM (no deal) | [X] | [%] |
| Net New Qualified | [X] | [%] |
| Excluded | [X] | [%] |

---

DETAILED CLASSIFICATION

**ALREADY IN CRM (WITH ACTIVE DEAL)**
| Company | Deal Name | Stage | Owner | Existing Contact |
|---------|-----------|-------|-------|------------------|
| [Company] | [Deal] | [Stage] | [Owner] | [Contact name] |

**IN CRM (NO ACTIVE DEAL)**
| Company | Last Activity | Last Contact | Segment | Next Action |
|---------|---------------|--------------|---------|-------------|
| [Company] | [Date] | [Contact] | [Segment] | [Suggested next step] |

**NET NEW QUALIFIED** (enrichment-ready)
| Company | Domain | Segment | Sub-Segment | City | State | Country | Contact Title Inferred | Contact Name (if available) |
|---------|--------|---------|------------|------|-------|---------|------------------------|---------------------------|
| [Company] | [domain.com] | [Fiber Operator] | [ISP/MSO] | [City] | [State] | [Country] | [VP Infrastructure / CTO] | [Name if available] |

**EXCLUDED**
| Company | Reason |
|---------|--------|
| [Company] | [Competitor / Out of scope / Do Not Contact] |

---

NEXT STEPS
1. Run Net New Qualified batch through enrichment pipeline to populate contact details
2. For "In CRM (no deal)" companies: Add to warm nurture sequence
3. For "Already in CRM (with deal)" companies: Alert deal owner to conference opportunity
```

## MODE 3: POST-EVENT FOLLOW-UP

**Trigger:** "Follow up from [event]" or "Process booth visitors" or "Write follow-ups for [event]"

### Steps

1. **Parse the follow-up list:** Ingest booth visitor scans, business cards, handwritten notes, or contact list
2. **Cross-reference HubSpot:** For each contact, check if account/contact exists in system
3. **Categorize by interaction warmth** (if notes provided):
   - **Hot:** Requested demo, specific conversation about use case, agreed to meeting
   - **Warm:** Engaged conversation, showed interest, took materials
   - **Cool:** Badge scan only, brief interaction, no specific conversation notes
4. **Determine follow-up approach:**
   - **Hot:** Personalized email referencing specific conversation topic + timeline for next step
   - **Warm:** Reference event + one problem relevant to their role/segment (not a company observation or flattery) + soft CTA (webinar, check out resource)
   - **Cool:** Brief "nice meeting you" + one relevant problem their peers are facing + very soft CTA (stay in touch)
5. **Draft follow-up emails** using MaiaEdge messaging framework (see rules below)
6. **Suggest sequence enrollment:** For warm/cool contacts, recommend 3-touch email sequence for nurture
7. **Flag new contacts:** Identify which contacts should be added to HubSpot (and at which account)

### Follow-Up Email Rules

- **Relevance principle:** Even in follow-ups, lead with problems, not observations or flattery. No "I noticed your company..." or "Impressive growth..." Research informs which problem to reference, but the research is fuel, not content.
- **Event reference:** Always include specific event name and dates
- **Conversation reference (if notes exist):** "You mentioned you're scaling GPU capacity..." or "Great discussion about multi-facility connectivity"
- **Writing standards:** Same as cold outreach: no em dashes, no vendor language, peer tone, no "solution" speak, no "I noticed" / "I saw" / "Congratulations on"
- **Subject line:** "[Event Name] follow-up" or "[Event]  -  [specific topic]"
- **CTA intensity:** Scaled to interaction warmth
  - Hot: "Let's set up a 30-min call to walk through the architecture"
  - Warm: "Curious if this resource might be relevant to your team: [link]"
  - Cool: "If you're thinking about infrastructure connectivity, happy to connect offline"
- **Sender:** Determined by HQ state/country - load `context/hubspot/territory-model.md` at runtime to assign the correct sender
- **Customer name anonymization:** Use "a major fiber operator" not "Lumen" in any proof points
- **Length:** 3–5 sentences max

### Territory Assignment Model

Load `context/hubspot/territory-model.md` at runtime to assign follow-up sender by HQ state or country. Do not rely on hardcoded state lists - the territory model is the canonical 5-region map.

### Output Format: Post-Event Follow-Up Package

```
POST-EVENT FOLLOW-UP SUMMARY
EVENT: [Name]
EVENT DATES: [Dates]
LOCATION: [City/Virtual]
TOTAL CONTACTS: [X]

---

INTERACTION WARMTH BREAKDOWN
| Warmth | Count | % |
|--------|-------|---|
| Hot | [X] | [%] |
| Warm | [X] | [%] |
| Cool | [X] | [%] |

---

FOLLOW-UP EMAILS (BY WARMTH)

**HOT CONTACTS ([Count])**

*Contact 1*
- Name: [Name]
- Title: [Title]
- Company: [Company]
- Email: [Email]
- HubSpot status: [Existing contact / New / Account only]
- Territory: [Sender per territory-model.md]
- Conversation summary: [Key topics discussed]
- Next step: [What was agreed to]

**Email:**
```
Subject: [Event Name] follow-up

Hi [Name],

Great meeting you at [Event] last week. I wanted to follow up on [specific topic you discussed].

[1-2 sentence that references the conversation directly]

[Specific next step or timeline]

Talk soon,
[Sender]
```

---

*Contact 2* [repeat for each hot contact]

---

**WARM CONTACTS ([Count])**

*Contact 1*
- Name: [Name]
- Title: [Title]
- Company: [Company]
- Email: [Email]
- HubSpot status: [Existing contact / New / Account only]
- Territory: [Sender per territory-model.md]
- Conversation summary: [Interest area, materials discussed]

**Email:**
```
Subject: [Event Name] follow-up

Hi [Name],

Enjoyed meeting you at [Event].

[One problem statement relevant to their segment/role: "I'd guess cross-carrier provisioning is still eating weeks every time you expand into a new market" or "Most colo operators I talk to are losing tenant connectivity revenue to third-party fabrics"]

[Soft CTA: "Thought this might be relevant..." or "We put together some thoughts on this specific challenge if you'd like to see them"]

Happy to connect if it's useful.

[Sender]
```

---

*Contact 2* [repeat for each warm contact]

---

**COOL CONTACTS ([Count])**

*Contact 1*
- Name: [Name]
- Title: [Title]
- Company: [Company]
- Email: [Email]
- HubSpot status: [Existing contact / New / Account only]
- Territory: [Sender per territory-model.md]

**Email:**
```
Subject: [Event Name] follow-up

Hi [Name],

Nice meeting you at [Event]. [One relevant insight about their industry/role: "Lot of talk about cross-carrier automation at this event" or "Sounds like infrastructure automation is top of mind for your peers"]

If you want to chat through anything infrastructure-related, happy to help.

[Sender]
```

---

*Contact 2* [repeat for each cool contact]

---

HUBSPOT UPDATES NEEDED

**New Accounts to Create**
| Company | Domain | Segment | City | State | Contact to add |
|---------|--------|---------|------|-------|----------------|

**New Contacts to Add** (to existing accounts)
| Account | Contact Name | Title | Email | Phone | Warmth | Source |
|---------|--------------|-------|-------|-------|--------|--------|

**Existing Contacts to Update**
| Contact Name | Company | Last Activity Date | Recommended Next Action | Sequence Enrollment? |
|--------------|---------|-------------------|-------------------------|----------------------|

---

SEQUENCE ENROLLMENT RECOMMENDATIONS

Enroll the following warm/cool contacts into 3-touch nurture sequence:
1. [Contact 1] – [Company] – [warm/cool] – [Sequence name: "Post-Event Nurture - Infrastructure"]
2. [Contact 2] – [Company] – [cool] – [Sequence name: "Post-Event Nurture - Infrastructure"]

---

FOLLOW-UP COMPLETION CHECKLIST
- [ ] All contacts cross-referenced against HubSpot
- [ ] Territory assignment validated (HQ state → correct owner)
- [ ] All follow-up emails reference event by name
- [ ] All follow-up emails reference conversation (if notes available)
- [ ] CTAs scale appropriately to interaction warmth
- [ ] No customer names used in proof points
- [ ] Writing style consistent (no vendor language, peer tone)
- [ ] New contact additions flagged for HubSpot entry
```

## EVENT-SPECIFIC INTELLIGENCE

### NVIDIA GTC
**Focus:** Neocloud segment (GPU cloud providers), AI Infrastructure colo sub-segment

**Key signals to watch:**
- NVIDIA partnership announcements and tier levels
- DGX/HGX deployment announcements
- Inference platform launches (vLLM, TensorRT, etc.)
- New sovereign AI announcements
- Crypto-to-AI pivots (GPU renters pivoting to AI infra)
- Multi-facility networking needs

**Talking points:**
- "Inference latency across facilities is a major bottleneck right now - cross-carrier connectivity solves it"
- "We're seeing GPU cloud operators scale from single-DC to multi-DC overnight"
- "Instant inter-facility networking let you monetize idle capacity across your footprint"

**Target segments:** Neoclouds, Colocation (with GPU focus), Network Operators building AI backbone

### OCP Global Summit
**Focus:** Colocation operators, network operators investing in open hardware

**Key signals to watch:**
- Open networking adoption and disaggregated infrastructure momentum
- Announcements of open platform deployments
- Cost optimization initiatives
- Sustainability/power efficiency focus

**Talking points:**
- "Cross-carrier automation + open infrastructure alignment - you can stitch together disaggregated resources across facilities"
- "Instant provisioning with open hardware means competitive advantage"
- "Network-on-demand is a natural fit for OCP operators"

**Target segments:** Colocation, Fiber Operators, Network Operators

### Fiber Connect / INCOMPAS
**Focus:** Fiber operators, competitive carriers, broadband service providers

**Key signals to watch:**
- Footprint expansion announcements
- Enterprise service launches (SD-WAN, IP VPN, Ethernet)
- Fiber pass announcements
- New market entries

**Talking points:**
- "Provisioning speed is your competitive edge - cross-carrier automation lets you activate NNI in hours, not weeks"
- "Cross-carrier connectivity means you can offer statewide/regional services without owning all the fiber"
- "Enterprise customers want instant multi-location connectivity - that's your play"

**Target segments:** Fiber Operators, Competitive Carriers, MSP/Aggregators

### MEF (Metro Ethernet Forum)
**Focus:** Network operators, MSP/Aggregators, service orchestration champions

**Key signals to watch:**
- LSO Sonata adoption and implementation announcements
- Network automation initiatives
- Service provider footprint expansion
- Managed service launches

**Talking points:**
- "LSO Sonata + instant NNI activation = you can automate enterprise multi-site delivery"
- "Automated partner activation is the next evolution of Mplify compatibility"
- "Operators automating service provisioning need a cross-carrier automation layer"

**Target segments:** Network Operators, MSP/Aggregators, Carriers

### Data Centre World
**Focus:** Colocation operators, data center infrastructure decision makers

**Key signals to watch:**
- Capacity expansion announcements
- Multi-site interconnection initiatives
- AI/ML infrastructure builds
- Sustainability/power announcements

**Talking points:**
- "Connecting your multi-site footprint with instant provisioning means better unit economics"
- "DC operators can now offer seamless multi-location services to enterprise customers"

**Target segments:** Colocation, Neoclouds (GPU-focused), Fiber Operators with data centers

### SC/Supercomputing
**Focus:** Research institutions, HPC centers, universities, national labs

**Key signals to watch:**
- New HPC deployments
- Multi-institution collaboration announcements
- Quantum computing initiatives
- GPU-accelerated research announcements

**Talking points:**
- "Research networks need instant inter-facility networking for data-intensive science"
- "HPC centers scaling across locations can now synchronize with zero provisioning delay"

**Target segments:** Academic institutions, Research networks, Neoclouds (research-focused)

## QUALITY CHECKLIST (All Modes)

- [ ] Every company cross-referenced against HubSpot before classification
- [ ] Segment and sub-segment assigned per standard taxonomy (Fiber, Colo, Neocloud, NetOp, MSP, Vendor)
- [ ] Exclusion list checked (no competitors, no do-not-contact accounts)
- [ ] Territory assignment validated (HQ state/country → correct sender per `context/hubspot/territory-model.md`)
- [ ] Follow-up emails pass the same quality standards as cold outreach (peer tone, no vendor speak, no em dashes)
- [ ] No customer names in follow-up emails (anonymized proof points: "a major fiber operator")
- [ ] Conference-specific intelligence applied (relevant talking points, key signals)
- [ ] HubSpot cross-reference documented (existing deal status, last activity, owner)
- [ ] New contacts flagged for HubSpot entry with correct account mapping
- [ ] Sequence enrollment recommendations included for warm/cool contacts

## MaiaEdge Segment Taxonomy

**Customer Segments:**
- Fiber Operators (sub: ISPs, MSOs, regional fiber builders)
- Colocation / Data Center Providers (sub: hyperscale, regional, niche)
- Neoclouds (sub: GPU cloud, inference platforms, emerging cloud providers)
- Network Operators / Carriers (sub: Tier-1 carriers, regional carriers, wireless operators)
- MSP / Aggregators (sub: managed service providers, VARs, systems integrators)
- **Enterprise - Multi-DC ICP (added 2026-05-11):** 4 sub-segments only - Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services. Hard scale gate per `context/segments/enterprise.md`. Anchor: Meijer.
- Vendors / Ecosystem (complementary tech, integration partners)

**Key value drivers by segment:**
- **Fiber:** Provisioning speed, cross-carrier automation, enterprise service enablement
- **Colo:** Multi-site elasticity, interconnection automation, customer service velocity
- **Neocloud:** Inference connectivity, multi-DC GPU resource access, latency optimization
- **NetOp:** Automation (LSO Sonata), service velocity, cost per bit
- **MSP:** White-label offerings, instant service activation, customer stickiness
- **Enterprise:** Dark fiber redundancy between corporate DCs, cloud on-ramp under enterprise control, hop-by-hop visibility on every path, audit-ready policy enforcement for HIPAA / PCI-DSS / SOX / GDPR / DORA / NY DFS Part 500

---

*Last updated: March 2026*
