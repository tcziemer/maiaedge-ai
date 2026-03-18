---
name: territory-manager
description: "MaiaEdge territory assignment auditor and validator. Validates and enforces territory assignments in HubSpot based on HQ state mapping. Use when asked to check territories, audit territory assignments, find misassigned accounts, verify state assignment, determine account ownership by state, check territory distribution, reassign accounts, or audit territory hygiene. Territory model: HQ state determines account owner (Tim Lieto = East 30 states, Ken Cunningham = West 20 states + DC, Tim Ziemer = International). Produces territory audit reports, misassignment lists, territory balance analysis, and owner correction recommendations. Source of truth: HubSpot state property vs hubspot_owner_id."
---

# MaiaEdge Territory Manager

## Purpose

Validate and enforce territory assignments in HubSpot. The territory model is simple: a company's **HQ state** determines its **account owner**. This skill audits CRM data against that mapping, identifies mismatches, and produces actionable correction lists.

**Source of truth:** The `state` property in HubSpot reflects HQ location. The `hubspot_owner_id` property determines account ownership. This skill checks that they align.

---

## Territory Model (Effective January 2026)

### Owner Assignments

| Owner | HubSpot Owner ID | Territory | State Count |
|-------|-----------------|-----------|-------------|
| **Tim Lieto** | `161889085` | East | 30 US states |
| **Ken Cunningham** | `162339176` | West | 20 US states + DC |
| **Tim Ziemer** | `159350430` | International | All non-US |

### State-to-Owner Mapping

**Tim Lieto (East) — Owner ID: 161889085**
```
AL, AR, CT, DE, FL, GA, IA, IL, IN, KY,
LA, MA, MD, ME, MI, MN, MO, MS, NC, NH,
NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV
```

**Ken Cunningham (West) — Owner ID: 162339176**
```
AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND,
NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY
```

**Tim Ziemer (International) — Owner ID: 159350430**
All non-US countries.

### Routing Rules

| Scenario | Resolution |
|----------|------------|
| HQ in known US state | Map state → owner per mapping above |
| HQ state unknown / blank | Flag for manual review — do NOT auto-assign |
| Non-US HQ (country ≠ United States) | Tim Ziemer (International) |
| Strategic exception | Leadership can reassign — document reason in HubSpot notes |

---

## When to Use This Skill

Trigger on any of these patterns:
- "Check territories" or "audit territory assignments"
- "Find misassigned accounts" or "wrong owner"
- "Who owns [company]?" or "Is [company] assigned correctly?"
- "Territory report" or "territory distribution"
- "Fix owner assignments" or "reassign accounts"
- "How many accounts does [owner] have?" or "territory balance"
- "Check new imports for territory" or "validate batch territory"
- "Accounts with no owner" or "unassigned accounts"
- "State is blank" or "missing state" or "no HQ state"
- Any mention of: territory, account ownership, state assignment, territory hygiene, territory audit

---

## Task Routing

### MODE 1: FULL TERRITORY AUDIT
**Trigger:** "Audit territories" or "Check all account assignments" or "Territory hygiene"

**Steps:**

1. **Pull all companies with owner data** from HubSpot:
   - Properties needed: `name`, `domain`, `state`, `hs_state_code`, `country`, `city`, `hubspot_owner_id`, `customer_segment`
   - Page through all results (100 per page, track total)

2. **Normalize state values** for each record:
   - If `hs_state_code` is a valid 2-letter US state abbreviation, use it
   - If `state` is a full state name (e.g., "California"), convert to 2-letter code
   - If `state` is already a 2-letter code, use it directly
   - If both are blank, flag as "Missing State"
   - Handle common variations: "Washington, D.C." → DC, "District of Columbia" → DC

3. **Look up correct owner** using the state-to-owner mapping:
   - US state found → map to correct owner ID
   - Non-US country → Tim Ziemer (159350430)
   - No state AND no country → flag as "Unroutable"

4. **Compare actual vs. expected owner** for each record:
   - Match → Correctly assigned
   - Mismatch → Flag with current owner, expected owner, and state
   - No owner assigned → Flag as "Unassigned"

5. **Produce audit report** (see Output Formats below)

**Output:**
```
TERRITORY AUDIT REPORT — [Date]
==================================
```

---

## Common Patterns

- **East Territory (Tim Lieto)**: Higher concentration of fiber operators and regional carriers
- **West Territory (Ken Cunningham)**: Mix of neoclouds, colo operators, and west-coast carriers
- **International (Tim Ziemer)**: Strategic accounts in EMEA, APAC, and other regions

