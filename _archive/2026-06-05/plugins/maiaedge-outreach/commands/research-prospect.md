---
description: Research a company and contact for MaiaEdge outreach without writing the email
argument-hint: "[company name] [contact name (optional)]"
---

# Research a MaiaEdge Prospect

Research the company and optionally the contact. Produce a research summary with segment classification and recommended angle, but don't write the email yet.

Arguments provided: $ARGUMENTS

## Workflow

1. **Check Exclusion List** - Verify this isn't an excluded category before researching
2. **Check HubSpot First** - Search HubSpot for existing company record using MCP tools (`search_crm_objects`). If complete classification exists and data is recent, skip to Step 5.
3. **Company Research** - Run all 4 mandatory web searches
4. **AI Signal Check** - If colocation or fiber in AI corridor, run all 3 AI searches
5. **Contact Research** - If contact name provided, search LinkedIn for background
6. **Segment Classification** - Determine segment and assign `customer_sub_segment`. Check exclusion list first.
7. **Document Findings** - Produce full research summary with recommended angle and fit score

## Output

Deliver the complete research summary in the standard format, including:
- Segment classification with reasoning
- Key findings that would drive the email angle
- Recommended messaging track
- Any red flags or exclusion concerns
- Fit score: EXCELLENT | STRONG | MODERATE | WEAK
