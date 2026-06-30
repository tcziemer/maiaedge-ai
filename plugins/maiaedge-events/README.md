# MaiaEdge Events Plugin

Systematic conference and event intelligence for maximum pipeline generation. Convert every attendee list into qualified leads, execute pre-event research and targeting, and run personalized post-event follow-up at scale.

## Overview

The MaiaEdge Events Plugin automates three critical conference workflows:

1. **Pre-Event Prep** – Research the event, pull exhibitor/speaker lists, identify net-new prospects, prioritize targets, and brief the team with talking points.
2. **Attendee Processing** – Ingest attendee or exhibitor lists, classify by segment, cross-reference against HubSpot, and produce enrichment-ready output.
3. **Post-Event Follow-Up** – Process booth visitors, segment by interaction warmth, draft personalized follow-ups, and sequence contacts for nurture.

All three workflows integrate with HubSpot CRM and prepare data for downstream enrichment and outreach plugins.

---

## Plugin Structure

```
maiaedge-events/
├── .claude-plugin/
│   └── plugin.json                    # Plugin metadata
├── commands/
│   ├── prep-conference.md             # Pre-event research command
│   ├── process-attendees.md           # Attendee list processing command
│   └── event-followup.md              # Post-event follow-up command
├── skills/
│   └── event-intelligence/
│       └── SKILL.md                   # Core event intelligence skill (3 modes)
└── README.md                          # This file
```

---

## Commands

### `/prep-conference` – Pre-Event Target Briefing

**Usage:**
```
/prep-conference NVIDIA GTC March 2026
/prep-conference OCP Global Summit
/prep-conference Fiber Connect
```

**What it does:**
1. Research the conference (dates, location, attendee/exhibitor profile, focus areas)
2. Pull the exhibitor and speaker list from the event website
3. Cross-reference all exhibitors against HubSpot CRM
4. Classify each company by MaiaEdge customer segment
5. Check exclusion list (competitors, do-not-contact)
6. Prioritize targets by: existing deal, segment fit, speaker/exhibitor status, recent company news
7. Identify key contacts for top 20 targets
8. Produce a pre-event target briefing with company, segment, contact, talking points, and intent signals

**Output:**
- Pre-Event Target Briefing (table of top 20 targets + detailed talking points per company)
- Conference-specific intelligence applied (relevant value propositions by event)
- Territory assignment (Tim Lieto or Ken Cunningham based on geography)

**Example output snippet:**
```
CONFERENCE: NVIDIA GTC
LOCATION: San Jose, CA
MAIAEDGE PARTICIPATION: Exhibiting
MAIAEDGE TEAM: Ken Cunningham

TOP 20 PRIORITIZED TARGETS

| Company | Segment | Contact | Intent Signal | Talking Point |
|---------|---------|---------|---------------|---------------|
| Crusoe Energy | Neocloud | VP Infrastructure | Exhibitor | Inference latency across facilities is a major bottleneck... |
| Lambda Labs | Neocloud | Co-founder | Attendee (recent Series B) | Instant inter-facility networking means you can... |

---

PER-COMPANY BRIEFING

**Crusoe Energy**
- Segment: Neocloud (GPU cloud / inference)
- HubSpot: In CRM, no active deal
- Key insight: Recently announced distributed inference platform
- Talking point: "Inference latency across facilities is a major bottleneck right now..."
- Approach: Ask for 15-min meeting to discuss multi-DC architecture
- Owner: Ken Cunningham (HQ: Denver, CO)
```

---

### `/process-attendees` – Attendee List Classification

**Usage:**
```
/process-attendees [upload attendee_list.csv]
/process-attendees OCP Global Summit [upload exhibitor_list.xlsx]
```

**What it does:**
1. Parse the uploaded file (CSV, XLSX, PDF, or pasted list)
2. Extract company names, contact info, titles
3. Cross-reference every company against HubSpot CRM
4. Classify by customer segment (Fiber, Colo, Neocloud, NetOp, MSP, Vendor)
5. Check exclusion list
6. Categorize into four buckets:
   - Already in CRM (with active deal)
   - In CRM (no active deal)
   - Net New Qualified (enrichment-ready)
   - Excluded (competitor, out of scope, do-not-contact)
7. Assign segment and sub-segment to net new contacts
8. Produce enrichment-ready batch file

**Output:**
- Classified Attendee Summary (breakdown by category with counts and percentages)
- Detailed classification tables for each category
- Net New Qualified batch (ready for enrichment pipeline with domain, segment, sub-segment, geography)
- Recommended next actions per category

**Example output snippet:**
```
ATTENDEE LIST PROCESSING SUMMARY
EVENT: OCP Global Summit
TOTAL RECORDS: 487

BREAKDOWN
| Category | Count | % |
|----------|-------|---|
| Already in CRM (with deal) | 23 | 4.7% |
| In CRM (no deal) | 89 | 18.3% |
| Net New Qualified | 312 | 64.1% |
| Excluded | 63 | 12.9% |

NET NEW QUALIFIED (enrichment-ready)
| Company | Domain | Segment | Sub-Segment | Contact Title |
|---------|--------|---------|-------------|----------------|
| Equinix Expansion LLC | equinix-new.com | Colocation | Hyperscale | Director Infrastructure |
```

---

### `/event-followup` – Post-Event Follow-Up Package

**Usage:**
```
/event-followup NVIDIA GTC [upload booth_visitors.csv]
/event-followup Fiber Connect [upload follow-up_notes.txt]
/event-followup OCP Global Summit
```

**What it does:**
1. Parse the follow-up list (booth visitor scans, business cards, notes)
2. Cross-reference every contact against HubSpot
3. Categorize by interaction warmth:
   - **Hot:** Requested demo, specific conversation, agreed to meeting
   - **Warm:** Engaged conversation, showed interest, took materials
   - **Cool:** Badge scan only, brief interaction
4. Draft personalized follow-up emails scaled to warmth:
   - Hot: Propose next step (meeting, demo)
   - Warm: Soft CTA (share resource, webinar)
   - Cool: Very light touch (stay connected)
5. Reference the specific event and conversation notes
6. Use MaiaEdge messaging standards (peer tone, no vendor language, anonymize customer names)
7. Assign sender based on territory (Tim Lieto East, Ken Cunningham West)
8. Flag new contacts for HubSpot entry
9. Suggest sequence enrollment for warm/cool contacts

**Output:**
- Post-Event Follow-Up Summary (warmth breakdown)
- Personalized follow-up emails grouped by warmth (Hot, Warm, Cool)
- HubSpot updates needed (new accounts, new contacts, updates to existing contacts)
- Sequence enrollment recommendations
- Follow-up completion checklist

**Example output snippet:**
```
POST-EVENT FOLLOW-UP SUMMARY
EVENT: NVIDIA GTC
TOTAL CONTACTS: 47

WARMTH BREAKDOWN
| Warmth | Count | % |
|--------|-------|---|
| Hot | 12 | 25.5% |
| Warm | 23 | 48.9% |
| Cool | 12 | 25.5% |

---

HOT CONTACTS (12)

Contact: Sarah Chen
Company: Crusoe Energy
Title: VP Infrastructure
Email: s.chen@crusoe.io
Conversation: Discussed multi-facility inference platform, pain point on latency

**Email:**
```
Subject: NVIDIA GTC follow-up — multi-facility inference

Hi Sarah,

Great meeting you at GTC last week. Wanted to follow up on what you mentioned about latency across your inference facilities.

We've been working with a few of the other platforms in this space on exactly this problem—instant inter-facility networking cuts inference latency by 70%+ when you're distributing workloads.

Happy to set up a 30-min call early next week to walk through the architecture. Do Tuesday or Wednesday work better for you?

Talk soon,
Ken

---

WARM CONTACTS (23)

[Follow-up emails for warm contacts with softer CTAs...]

---

COOL CONTACTS (12)

[Follow-up emails for cool contacts with very light touches...]

---

HUBSPOT UPDATES NEEDED

**New Accounts to Create**
| Company | Domain | Segment | Contact to add |
|---------|--------|---------|----------------|
| Crusoe Energy | crusoe.io | Neocloud | Sarah Chen, VP Infrastructure |

**New Contacts to Add**
| Account | Name | Title | Email | Source |
|---------|------|-------|-------|--------|
| Crusoe Energy | Sarah Chen | VP Infrastructure | s.chen@crusoe.io | GTC Booth |

**Sequence Enrollment Recommendations**
1. Mark Chen – Crusoe Energy (hot) – Enroll in "Post-Event Demo Follow-Up"
2. James Park – Lambda Labs (warm) – Enroll in "Post-Event Nurture — Infrastructure"
```

---

## Workflow: From Conference to Pipeline

### Before the Conference

1. **Run `/prep-conference`** for the target event
   - Get the top 20 target list with talking points
   - Assign Tim/Ken as account owner based on geography
   - Brief the team on intent signals and conversation starters

2. *Optional: Run `/process-attendees`** if you have the full attendee/exhibitor list early
   - Identify net new qualified prospects
   - Run enrichment pipeline to populate contact details
   - Add warm leads to nurture sequences before the event

### At the Conference

- Use the pre-event target briefing as a floor guide
- Note which companies/contacts you speak with
- If you collect business cards or booth scans, track the warmth of conversation (hot/warm/cool)
- Capture any specific topics or pain points mentioned

### After the Conference

1. **Run `/event-followup`** with your booth visitor list or follow-up notes
   - Get personalized follow-up emails ready to send
   - Identify new contacts to add to HubSpot
   - Get sequence enrollment recommendations

2. **Execute the follow-ups**
   - Send hot emails within 1–2 days
   - Sequence warm/cool contacts into nurture tracks
   - Add new contacts/accounts to HubSpot

3. **Monitor and measure**
   - Track which events drive the highest-quality pipeline
   - Measure hot/warm/cool conversion rates
   - Use data to prioritize which conferences to attend next year

---

## Integration with Other Plugins

The Events Plugin integrates seamlessly with two other RevOps plugins:

### Enrichment Pipeline (`maiaedge-enrichment`)

After running `/process-attendees`, the Net New Qualified batch output is ready to feed into the enrichment pipeline:

```
Input: Net New Qualified batch (company name, domain, segment, sub-segment, geography)
↓
Process through enrichment pipeline (populate contact details, company intelligence, etc.)
↓
Output: Enriched contact records ready for outreach
```

### Outreach Pipeline (`maiaedge-outreach`)

After running `/event-followup`, use the follow-up email outputs and sequence recommendations to:

1. Create personalized follow-up sequences in Apollo or HubSpot
2. Enroll warm/cool contacts into nurture sequences
3. Monitor open rates and engagement
4. Use engagement signals to trigger sales team follow-up

---

## HubSpot Field Requirements

The Events Plugin works best when HubSpot accounts and contacts have these fields populated:

**Account fields:**
- Company Name
- Domain
- HQ State (for territory assignment)
- Customer Segment (Fiber, Colo, Neocloud, NetOp, MSP, Vendor)
- Customer Sub-Segment
- Deal Pipeline (to check for existing deals)
- Owner (Tim Lieto / Ken Cunningham / other)

**Contact fields:**
- First Name, Last Name
- Job Title
- Email
- Phone
- Account ID (linked to company)

---

## Key Features

### Segment-Specific Messaging

Each command applies conference-specific intelligence and talking points tailored to the event:

- **NVIDIA GTC:** Focus on GPU cloud, inference federation, multi-DC resource access
- **OCP Global Summit:** Open hardware, disaggregated infrastructure, federation alignment
- **Fiber Connect / INCOMPAS:** Provisioning speed, cross-carrier federation, enterprise service enablement
- **MEF:** LSO Sonata compatibility, network automation, service velocity
- **Data Centre World:** Multi-site elasticity, customer service velocity
- **SC/Supercomputing:** Research federation, inter-facility HPC networking

See the event-intelligence skill for full conference profiles.

### Territory-Based Sender Assignment

Follow-up emails are automatically assigned the correct sender based on company HQ state:

- **Tim Lieto (East):** CT, DE, MA, MD, ME, NH, NJ, NY, PA, RI, VT, VA, WV, DC, OH, IN, KY, TN
- **Ken Cunningham (West):** CA, OR, WA, NV, UT, CO, AZ, NM, TX, OK, KS, WY, MT, ID
- **International:** Tim Ziemer

### Interaction Warmth Segmentation

Post-event follow-ups are scaled to the warmth of the interaction:

- **Hot** (demo request, specific use case discussion): Propose next step immediately
- **Warm** (interested, engaged): Share relevant resource or insight
- **Cool** (badge scan): Keep it light, focus on relevance to their role

### Quality Checklist

Every command output includes a completion checklist to ensure quality:

- Every company cross-referenced against HubSpot
- Correct segment and sub-segment assigned
- Exclusion list checked
- Territory assignment correct (HQ state → owner)
- Follow-up emails meet quality standards (peer tone, no vendor language)
- New contacts flagged for HubSpot
- Conference-specific intelligence applied

---

## Best Practices

### Pre-Conference

1. Run `/prep-conference` at least 1 week before the event
2. Review the top 20 targets and talking points as a team
3. If you have the full attendee list, run `/process-attendees` and identify net-new qualified leads
4. Enrich net-new leads in advance so you can do targeted outreach on the show floor
5. Assign Tim/Ken as point person based on territory

### At the Conference

1. Use the pre-event briefing as a guide for prioritized conversations
2. Note the names and companies of people you speak with
3. Capture the warmth of interaction and key topics discussed
4. Collect business cards or booth scans

### Post-Conference

1. Run `/event-followup` within 1–2 days of the event
2. Send hot follow-ups immediately (same day or next morning)
3. Enroll warm/cool contacts into sequences
4. Add new accounts/contacts to HubSpot within 48 hours
5. Monitor open rates and engagement to prioritize sales follow-up

### Measurement

Track these metrics to understand which conferences drive the best ROI:

- **Attendee-to-Contact conversion:** % of attendees who become HubSpot contacts
- **Contact-to-Opportunity conversion:** % of contacts who enter the pipeline within 60 days
- **Warmth distribution:** % hot/warm/cool interactions at the event
- **Follow-up email engagement:** Open rates, click rates, reply rates by warmth level
- **Sequence conversion:** % of warm/cool contacts who advance through nurture sequence

---

## FAQ

**Q: Can I use this for virtual conferences?**
A: Yes. The same three modes apply to virtual events. Just upload the attendee list and follow the same process.

**Q: What if I don't have the full exhibitor/attendee list before the event?**
A: Run `/prep-conference` anyway—you'll get research on the event, key segments likely to attend, and a framework for prioritizing conversations on the floor. Then use `/event-followup` after the event with the booth visitors you collected.

**Q: How do I decide who counts as "hot" vs. "warm" vs. "cool"?**
A: **Hot** = they asked for a demo, discussed a specific use case, or agreed to a meeting. **Warm** = they engaged in conversation and expressed interest. **Cool** = they scanned a badge or had a brief chat with no specific commitment.

**Q: Can I customize the follow-up email templates?**
A: The email templates are generated per the MaiaEdge messaging framework (peer tone, no vendor language, anonymized proof points). You can edit them before sending, but the framework ensures consistency.

**Q: What if a contact is already in HubSpot?**
A: The skill will flag existing contacts and recommend next actions (e.g., update last activity, add to sequence, alert deal owner if there's an active deal).

**Q: How do I enroll contacts in sequences after the event?**
A: The `/event-followup` command will recommend sequence enrollment by warmth. Use the outreach plugin or HubSpot directly to add them to the sequences.

---

## Support

For questions about this plugin, contact the MaiaEdge RevOps team.

For questions about MaiaEdge customer segments, sales territories, or messaging, consult the Sales team or the MaiaEdge Messaging Framework documentation.

---

**Version:** 1.0.0
**Last Updated:** March 2026
**Maintained by:** MaiaEdge RevOps
