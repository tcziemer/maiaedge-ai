---
description: Classify and prioritize an attendee or exhibitor list
argument-hint: "[upload CSV/XLSX/PDF of attendees]"
---

Process a conference attendee or exhibitor list.

Arguments provided: $ARGUMENTS

Invoke the event-intelligence skill in Mode 2 (Process Attendee/Exhibitor List). Parse the uploaded file, cross-reference every company against HubSpot, classify by segment, and produce a prioritized, enrichment-ready output.

The output should clearly separate:
- Already in CRM (with deal status)
- In CRM (no active deal)
- Net New Qualified (ready for enrichment pipeline)
- Excluded (competitors, out of scope, do-not-contact)

Produce both a detailed classification table and a summary with counts/percentages. The Net New Qualified output should be enrichment-ready (domain, company name, segment, sub-segment, city, state).
