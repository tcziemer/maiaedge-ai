---
description: Deep-dive research on edge case accounts from enrichment
argument-hint: "[edge cases file from import processor]"
---

# Research Edge Case Accounts

Perform deep-dive research on edge case accounts to determine if they should be reclassified or confirmed excluded.

Arguments provided: $ARGUMENTS

## How This Works

1. **Invoke the edge-case-researcher skill** to re-evaluate excluded accounts
2. **Parse the edge case file** from the import-processor skill
3. **Apply targeted research strategy per exclusion type**:
   - Rule 1: Retail ISP with infrastructure signals → check for wholesale/B2B division
   - Rule 2: Low employee count with infra metrics → verify with multiple sources
   - Rule 3: Insufficient data but identifiable business → deep research missed signals
   - Rule 4: Vendor/contractor with infrastructure overlap → check for operator division
   - Rule 5: Enterprise/utility with telecom-adjacent business → check for wholesale fiber
   - Rule 6: Bot processing failures → run full enrichment methodology
   - Rule 7: Neocloud edge cases → check if GPU cloud not colo or vendor
4. **Cross-reference multiple sources** for each account
5. **Determine**: **RECLASSIFY** as qualified OR **CONFIRM** excluded

## Research Approach

For each edge case:
1. Start with `web_fetch` on the company domain (read website directly)
2. Run rule-specific searches (2-4 targeted queries)
3. Check for parent/subsidiary relationships
4. Try alternate company names if needed
5. Document findings in research log

## Decision Framework

**RECLASSIFY as Qualified if:**
- Research reveals the company fits a valid segment (Colo, Fiber, Network Op, MSP, Neocloud)
- At least MEDIUM segmentation confidence
- Clear evidence from 2+ sources

**CONFIRM EXCLUDED if:**
- Research confirms the exclusion
- Document with stronger evidence and audit trail
- HIGH or MEDIUM exclusion confidence

## Expected Output

Three files:
1. **reclassified_hubspot_import.xlsx** — HubSpot-ready import for reclassified accounts (zero edits)
2. **confirmed_excludes.xlsx** — Accounts confirmed as legitimately excluded
3. **edge_case_research_log.xlsx** — Full audit trail of research and decisions

## Impact

Typical results from edge case research:
- **Rule 1 (Retail ISP + infra)**: ~20-40% reclassification rate (many are hybrid ISP+fiber operators)
- **Rule 2 (Low employee count)**: ~30-50% reclassification rate (data errors, cooperatives)
- **Rule 3 (Insufficient data)**: ~10-30% reclassification rate (bot missed signals)
- **Rules 4-5 (Vendor/Enterprise overlap)**: ~5-15% reclassification rate
- **Rule 6 (Bot failures)**: ~50%+ reclassification rate (bot didn't run)
- **Rule 7 (Neocloud)**: ~40-60% reclassification rate (common misclassification)

This is where you recover false negatives from the first-pass enrichment.
