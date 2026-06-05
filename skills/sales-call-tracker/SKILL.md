---
name: sales-call-tracker
description: "MaiaEdge sales call tracker. Processes team sales call transcripts to extract pipeline status across three columns (Pre-POC, Active POC, Expansion), assigns owners, captures next steps, produces a branded PPTX pipeline slide, updates HubSpot with call notes, and generates a structured markdown summary. Use when given a sales call transcript or recording summary and asked to track pipeline, capture notes, create a pipeline slide, or update CRM."
---

# MaiaEdge Sales Call Tracker

## Purpose

Process team sales call transcripts and produce three deliverables:
1. **Markdown summary** -- structured notes organized by pipeline stage, action items, and strategic insights
2. **Pipeline PPTX slide** -- single branded slide with three-column (or four-column) pipeline view plus key notes
3. **HubSpot updates** -- notes logged as most recent activity on every account discussed

This skill is designed for recurring weekly/biweekly sales calls where the team reviews pipeline status, discusses account progress, and assigns follow-ups.

---

## Reference Files

- **Owner IDs and territory mapping:** `territory-model.md`
- **Deal stages and pipeline mapping:** `deals-schema.md`
- **POC ticket stages:** `poc-schema.md`
- **HubSpot field values and segments:** `hubspot-values.md`
- **Company identity and messaging:** `maiaedge-101.md`

---

## Workflow

### STEP 1: EXTRACT PIPELINE DATA FROM TRANSCRIPT

Read the full transcript and extract every account/company mentioned. For each account, capture:

| Field | Description |
|-------|-------------|
| **Company name** | As mentioned in the call (normalize spelling) |
| **Pipeline stage** | Pre-POC, Active POC, or Expansion |
| **Sales owner** | Ken Cunningham, Tim Lieto, or Tim Ziemer (per territory model) |
| **Use case** | e.g., DIA, cloud on-ramp, data center fabric, Megaport replacement, Azure Local |
| **Next steps** | Specific actions discussed |
| **Priority/heat** | Hot (push now), Developing (building toward POC), Next Wave, Stalled |
| **Key context** | Any detail that matters for follow-up (contacts, blockers, financials) |

**Classification rules:**

- **Pre-POC:** Account has had conversations but no POC hardware shipped or POC ticket opened. Includes accounts in discovery, appointment scheduled, or waiting on engineering/pricing.
- **Active POC:** POC hardware deployed or POC ticket exists. Customer is testing or close to testing. Focus is converting to purchase order.
- **Expansion:** Customer has placed at least one purchase order or is in production. Focus is growing footprint (more sites, more bandwidth, new use cases).

**Stage signals in conversation:**
- "heading into POC" / "push to POC" / "not there yet" = Pre-POC
- "active POC" / "close to the boat" / "convert to order" / "target close" = Active POC
- "expansion" / "more sites" / "additional order" / "already deployed" / "in production" = Expansion
- An account can appear in multiple columns if it spans stages (e.g., first PO pending + expansion discussion)

Also extract from the transcript:

| Category | What to capture |
|----------|----------------|
| **Outbound focus areas** | Target segments, lists being built, who owns outbound |
| **Action items** | Every follow-up with owner and timing |
| **Strategic notes** | Business model changes, pricing updates, messaging shifts, competitive intel, event planning |
| **Stalled/watch accounts** | Accounts that have gone cold or are intentionally paused, with reasons |

---

### STEP 2: MATCH ACCOUNTS TO HUBSPOT

For each account extracted in Step 1:

1. Search HubSpot using `search_crm_objects` (objectType: `companies`) by name and common variations
2. Record the HubSpot company ID, current owner, and domain
3. Flag any accounts NOT found in HubSpot -- these may need to be created

**Search tips:**
- Try the exact name first, then abbreviations and alternate spellings
- Company names in transcripts are often spoken informally -- try multiple queries
- Use `CONTAINS_TOKEN` filter on `name` property as a fallback

---

### STEP 3: CREATE MARKDOWN SUMMARY

Save a structured markdown file to the output folder with this format:

```
# MaiaEdge Sales Call Notes - [Date]

**Attendees:** [names from transcript]

---

## 1. Prospects Heading into POC (Pre-POC)

| Account | Owner | Use Case | Next Steps |
|---------|-------|----------|------------|
| ... | ... | ... | ... |

## 2. Active POCs -- Converting to Orders

| Account | Owner | Status | Next Steps |
|---------|-------|--------|------------|
| ... | ... | ... | ... |

## 3. Existing Customers -- Expansion

| Account | Owner | Current State | Expansion Play |
|---------|-------|---------------|----------------|
| ... | ... | ... | ... |

## 4. Outbound Focus Areas

| Focus Area | Owner | Details |
|------------|-------|---------|
| ... | ... | ... |

## 5. Stalled / Watch List

| Account | Owner | Status | Notes |
|---------|-------|--------|-------|
| ... | ... | ... | ... |

## 6. Key Action Items

| Action | Owner | Timing |
|--------|-------|--------|
| ... | ... | ... |

## 7. Strategic Notes

[Prose capturing business model changes, pricing updates,
messaging shifts, competitive intel, event planning, etc.]
```

---

### STEP 4: CREATE PIPELINE PPTX SLIDE

Produce a single-slide PPTX using `python-pptx`. Install if needed: `pip install python-pptx --break-system-packages -q`

**Layout rules:**

- **Slide size:** Widescreen 13.333" x 7.5"
- **Background:** Dark (#0D1117)
- **Top half (~60%):** Pipeline columns
- **Bottom half (~40%):** Key notes and action items in two-column prose layout
- **Footer:** "MaiaEdge | Carrier Infrastructure for Federated Private Networking | Confidential"

**MaiaEdge branding:**

| Element | Value |
|---------|-------|
| Logo | Use `MaiaEdge_Logo_Horizontal_RevWhite.png` from `plugins/maiaedge-sales-docs/logos/` (white logo for dark bg) |
| Primary accent | #F5A623 (MaiaEdge orange/gold) |
| Text | White (#FFFFFF) on dark background |
| Secondary text | Light gray (#CCCCCC) for descriptions, medium gray (#999999) for labels |
| Column backgrounds | Subtle tinted panels: blue-tint (#1A2332) for Pre-POC, green-tint (#1A2A1A) for POC, warm-tint (#2A1A1A) for Expansion |

**Column headers:** Colored accent bars with white bold title + subtitle. Use these accent colors:
- Pre-POC: #4DA8DA (blue)
- Active POC: #4DDA6E (green)
- Expansion: #DA6E4D (warm)

**Column sizing -- CRITICAL to avoid overlap:**

Count the accounts per column before laying out. If any single column has more than 5-6 accounts, split it into two sub-columns (e.g., "Pre-POC: Hot" and "Pre-POC: Developing") to prevent content bleeding into the notes section below.

Splitting thresholds:
- 6 or fewer accounts in a column: single column, no split needed
- 7+ accounts: split into two sub-columns by priority/heat

When splitting, use 4 columns total across the slide instead of 3. Adjust column widths proportionally:
- 3 columns: each ~4.0" wide with 0.15" gaps
- 4 columns: each ~3.05" wide with 0.12" gaps

**Account entries in columns:**
```
Company Name  (Owner)          <- orange bold + gray italic
Next step description          <- light gray, smaller font
```

Font sizes:
- Company name: 9-10pt bold, color = MaiaEdge orange
- Owner: 7-8pt, color = medium gray
- Next step: 7-8pt, color = light gray
- Column header title: 12-14pt bold white
- Column header subtitle: 7-8pt light

**Bottom notes section:**
- Separated from columns by a thin divider line (#2A2F3A)
- "KEY NOTES & ACTION ITEMS" header in orange bold
- Two-column layout: left column and right column, each with 2-3 topic blocks
- Topic heading: 9pt white bold
- Topic body: 8pt light gray

---

### STEP 5: UPDATE HUBSPOT

For each account found in HubSpot (Step 2), create a note engagement:

1. Use `manage_crm_objects` with `createRequest` to create `notes` objects
2. Set `hs_timestamp` to the call date/time
3. Set `hs_note_body` with a concise summary: "Sales Call [date]: [stage]. [key context and next steps]."
4. Associate the note with the company using `associations`

**Note format:**
```
Sales Call [MM/DD/YY]: [Pre-POC | Active POC | Expansion]. [1-2 sentence summary of what was discussed and next steps].
```

**Batching:** Create up to 10 notes per `manage_crm_objects` call. If more than 10 accounts, batch into multiple calls.

**Confirmation:** Per HubSpot tool requirements, present proposed notes in a table and get user approval before creating. After first confirmation, offer to skip confirmations for the session.

**Missing accounts:** Report any accounts not found in HubSpot so the user can decide whether to create them.

---

### STEP 6: OUTPUT

Save all deliverables to the user's output folder:

1. `Sales Call Notes - [YYYY-MM-DD].md` -- full structured summary
2. `MaiaEdge Pipeline Tracker - [YYYY-MM-DD].pptx` -- branded pipeline slide

Provide `computer://` links to both files.

Report:
- Total accounts tracked across all three columns
- Number of HubSpot notes created
- Any accounts not found in HubSpot
- Any accounts flagged as needing immediate action

---

## Edge Cases

- **Account in multiple stages:** List in the highest-priority stage first, with a cross-reference note in the other column (e.g., "Movii (post-PO)" in Expansion alongside "Movii" in Active POC)
- **No clear owner:** Default to Tim Ziemer (CRO) and flag for assignment
- **Vague next steps:** Write "Follow up needed -- no specific action identified" rather than inventing steps
- **Names hard to parse from audio:** Flag uncertain names with [?] and note the timestamp
- **Very long Pre-POC list:** Always split into Hot vs. Developing sub-columns when 7+ accounts
