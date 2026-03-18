---
description: Find new prospect companies by ICP segment
argument-hint: "[segment name or 'all'] [optional: region/state]"
---

# Source New MaiaEdge Accounts

Source new MaiaEdge prospect accounts by customer segment.

Arguments provided: $ARGUMENTS

## How This Works

1. **Invoke the account-sourcing skill** to find new companies in your target segment
2. If a segment is specified, focus sourcing on that segment
3. If no segment is specified, recommend which segment has the biggest coverage gap and start there

## Always

1. **Check HubSpot first** using MCP tools (`search_crm_objects`) to understand current coverage
2. **Recommend sources ranked by expected hit rate** for the target segment
3. **Generate ready-to-use search queries** the user can copy to Apollo, ZoomInfo, LinkedIn, or other platforms
4. **Estimate batch size and expected qualification rate** based on source type and hit rate
5. **Output a sourcing plan the user can approve** before executing queries and enrichment

## Segment Priority Order

Unless the user specifies otherwise, recommend in this order:
1. **Colocation Operators** (highest product fit, fastest sales cycle)
2. **Fiber Operators** (largest TAM gap)
3. **Network Operators** (good fit, longer sales cycle)
4. **Neoclouds** (emerging, high strategic value)
5. **MSP/Aggregators** (depends on carrier infra)

## Expected Output

A sourcing plan with:
- Current CRM snapshot (if available)
- Coverage gaps identified
- Recommended sources ranked by hit rate
- Specific search queries ready to use
- Estimated yield (raw records × hit rate = ICP companies)
- Deduplication needs flagged
- Next steps the user can approve
