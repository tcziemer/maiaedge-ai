---
description: Process multiple contacts for MaiaEdge outreach. Research each individually and write personalized emails.
argument-hint: "[list of companies/contacts or paste a CSV]"
---

# Batch MaiaEdge Outreach

Process multiple contacts with full individual research for each. Never reuse research across different companies.

Arguments provided: $ARGUMENTS

## Rules

- **Every contact gets individual research.** No shortcuts, no reusing research across companies.
- **Confirm sender** (Tim or Ken) once for the batch unless different senders are specified per contact.
- **Check exclusions first** for each company before full research.
- **Process sequentially.** Complete one contact fully before starting the next.

## Workflow Per Contact

1. Check exclusion list
2. Check HubSpot for existing company record using MCP tools (`search_crm_objects`). If complete classification exists and data is recent, skip to Step 5.
3. Full company research (4 mandatory searches)
4. AI signal check (if applicable)
5. Contact research
6. Document research summary
7. Classify segment and assign `customer_sub_segment`
8. Write email + subject line
9. Write LinkedIn connection request
10. Run quality checklist

## Output

For each contact, deliver:
- Research summary (abbreviated)
- Email with subject line
- LinkedIn connection request (under 300 characters)
- Segment classification
- Any flags or notes

If a company is excluded, note why and skip to the next contact.
