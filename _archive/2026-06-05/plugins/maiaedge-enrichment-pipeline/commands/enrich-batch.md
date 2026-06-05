---
description: Research and classify a batch of companies for HubSpot
argument-hint: "[company names, CSV file, or paste a list]"
---

# Enrich a Batch of Companies

Research and classify a batch of companies through the full MaiaEdge enrichment pipeline.

Arguments provided: $ARGUMENTS

## How This Works

1. **Invoke the company-enrichment skill** to process your company list
2. **Parse the input** (company names, CSV file, or pasted list)
3. **Research each company** using the website-first adaptive strategy
4. **Classify into customer_segment and customer_sub_segment** for each company
5. **Score and tier each account** for outreach prioritization
6. **Produce two output files**:
   - Qualified accounts in HubSpot-ready XLSX format (Tab 1: Import, Tab 2: Companion Data)
   - Excludes log documenting why companies were excluded

## What Gets Researched

For each company, the skill will:
1. Verify or discover the company domain
2. Check HubSpot for duplicates (skip if already enriched)
3. Read the company's website (homepage + services page)
4. Run segment-specific research queries (5-8 searches per company)
5. Verify exclusions with targeted follow-up research
6. Compile into a structured research profile
7. Classify into appropriate segment and sub-segment
8. Score on 4 dimensions: Strategic Fit, Problem Awareness, Timing/Urgency, Outreach Quality
9. Generate synthesis copy for outreach (account brief, provisioning landscape, value prop)

## Expected Output

Three files:
1. **Enriched Accounts XLSX** — Import-ready, zero manual editing needed
2. **Excludes Log** — Companies that didn't qualify and why
3. **Summary report** — Qualified count, tier breakdown, data quality metrics

## Cost & Time Estimate

- 50 companies: ~50 min, ~$18-20
- 150 companies: ~2.5 hrs, ~$53-60
- 500 companies: ~8 hrs, ~$175-200

Weighted average: **~$0.35-0.40 per company** (more accurate than the legacy $0.08 pipeline)
