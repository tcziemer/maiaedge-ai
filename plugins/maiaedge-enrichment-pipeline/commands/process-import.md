---
description: Process enrichment output into HubSpot-ready import files
argument-hint: "[enrichment output file]"
---

# Process Enrichment Output for HubSpot Import

Transform enrichment output into HubSpot-optimized import files with exact property mapping.

Arguments provided: $ARGUMENTS

## How This Works

1. **Invoke the import-processor skill** to transform your enrichment output
2. **Parse the enrichment output file** (XLSX or CSV from the enrichment-bot skill)
3. **Separate qualified accounts** with exact HubSpot property name and value mapping
4. **Identify edge cases** within the excluded accounts that deserve deeper research
5. **Categorize definitive excludes** with normalized exclusion reasons
6. **Produce three output files**:
   - HubSpot-ready qualified accounts import file (zero manual edits)
   - Edge cases file for the edge-case-researcher skill
   - Definitive excludes file for audit trail

## Transformations Applied

The processor handles:
- **Property name mapping**: Enrichment columns → HubSpot property internal names
- **Value mapping**: Segment names → HubSpot dropdown values (e.g., "Colocation Operator" → "Data Center Colo Provider")
- **Multi-select formatting**: Semicolon-separated values with no spaces
- **Domain cleaning**: Strip protocol and www prefix
- **Deduplication**: Remove duplicates by domain, keep highest priority score
- **Tier assignment**: Route accounts to Tier 1/2/3 based on score
- **Edge case detection**: Flag accounts for potential reclassification

## Expected Output

Three files:
1. **hubspot_import_qualified.xlsx** — Ready to upload directly to HubSpot, zero changes needed
2. **edge_cases_for_research.xlsx** — Excluded accounts flagged for manual review (input for edge-case-researcher skill)
3. **definitive_excludes.xlsx** — Companies that are definitely excluded, with normalized reasons

## Edge Case Rules

The processor identifies edge cases that may have been incorrectly excluded:
- Retail ISP with infrastructure signals (may actually be wholesale fiber operator)
- Low employee count but operates infrastructure (data error or cooperative)
- Insufficient data but domain is valid (bot missed something)
- Vendor/contractor that also operates infrastructure
- Enterprise/utility with telecom-adjacent business
- Bot processing failures (incomplete research)
- Neocloud misclassified as colo or excluded

Edge cases are flagged for the edge-case-researcher skill to deep-dive and potentially reclassify.
