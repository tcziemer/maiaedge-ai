---
name: territory-manager
description: "MaiaEdge territory assignment auditor and validator. Validates and enforces territory assignments in HubSpot based on HQ geography. Use when asked to check territories, audit territory assignments, find misassigned accounts, verify state assignment, determine account ownership by state, check territory distribution, reassign accounts, or audit territory hygiene. Territory model (2026-06-17 5-region): HQ geography determines owner across 5 US regions + Europe + International (Tim Lieto = Northeast + West, Ken Cunningham = Southeast, Tory Teague = Central, Markus Hendrich = Europe, Tim Ziemer = International + Tier 1 SP, Cooper = Unassigned catch-all). Produces territory audit reports, misassignment lists, territory balance analysis, and owner correction recommendations. Source of truth: HubSpot state/country properties vs hubspot_owner_id, and the live keeper workflow flow 4405143279."
---

# MaiaEdge Territory Manager

## Purpose

Validate and enforce territory assignments in HubSpot. The territory model: a company's **HQ geography** (country first, then US state) determines its **account owner** across 5 US regions plus Europe and International. This skill audits CRM data against that mapping, identifies mismatches, and produces actionable correction lists.

**Source of truth:** `country` / `hs_country_code` and `state` / `hs_state_code` reflect HQ location. `hubspot_owner_id` determines ownership. The live keeper workflow "Territory Assignment (Go-Forward)" (flow `4405143279`) is the executable implementation; this skill audits against the same map. The canonical map doc is `context/hubspot/territory-model.md`.

## Reference Files

For the canonical territory model, see `context/hubspot/territory-model.md` (5-region, 2026-06-17). The mapping below is reproduced for quick reference and MUST stay in sync with it and with the keeper workflow's `REGION_OF` / `REGION_OWNER`.

**Informational refs (territory logic does NOT depend on these - they're for context when audit reports surface segment / sub-segment / tier data alongside owner data):**
- `context/account-tiering/tier-compute-spec.md`  -  Canonical `account_tier` function. **Territory changes do NOT affect tier.** Tier reads via this spec; territory-manager never writes tier.
- `context/account-tiering/sub-segment-qualification.md`  -  Canonical 30-value list of active `company_sub_segment` enums (case-sensitive) - informational only when audit output displays sub-segments alongside owners. Territory-manager does not classify, gate, or modify sub-segments.
- `context/account-tiering/sub-segment-qualification-full.md`  -  upstream consolidated source for sub-segment qualification. This file wins if it diverges from the pointer file above.
- `context/hubspot/hubspot-values.md`  -  Canonical HubSpot enum values, including `closedwon` / `closedlost` deal-stage strings used in deal-protection checks.
- `context/hubspot/deals-schema.md`  -  Deal properties and stage model; required for correct deal-protection awareness when auditing accounts with open deals.
- `context/hubspot/property-schema.md`  -  Company and contact property definitions. Use for property keys and field structures only; note that its §1 territory section is stale - the canonical territory map is `context/hubspot/territory-model.md`.
- `context/hubspot/contact-schema.md`  -  Contact property definitions; used when cascading owner changes to associated contacts.

### Independence rule

**Territory assignment is independent of `customer_segment` and `company_sub_segment`.** The territory function takes inputs (`country`, `hs_country_code`, `state`, `hs_state_code`) and returns an owner - full stop. It does NOT branch on segment / sub-segment / tier. A Tier 1 NeoCloud in California routes to its region owner the same way a Tier 5 Other in California does. Strategic exceptions are the only override path (see Routing Rules below).

**Territory changes do NOT cascade to tier.** A correction writes `hubspot_owner_id` and cascades to associated contacts' `hubspot_owner_id`, but never touches `account_tier`. The tier value is owned by R1 / R2 / Signal Scan Stage 5b / R-Tier-Audit per `context/account-tiering/tier-compute-spec.md`. Territory-manager and tier-compute have non-overlapping write domains.

---

## Territory Model (Effective 2026-06-17, 5-region)

> Supersedes the Jan 2026 two-region (East/West) model.

### Owner Assignments

| Region | Owner | HubSpot Owner ID | Coverage |
|--------|-------|------------------|----------|
| **Northeast** | Tim Lieto | `161889085` | 16 US states (incl. DC) |
| **Southeast** | Ken Cunningham | `162339176` | 13 US states |
| **Central** | Tory Teague | `165480917` | 11 US states |
| **West** | Tim Lieto (interim) | `161889085` | 11 US states |
| **Europe** | Markus Hendrich | `164949459` | Geographic Europe ex Russia/Turkey |
| **International** | Tim Ziemer | `159350430` | All other non-US + US territories |
| **Tier 1 Service Provider** | Tim Ziemer (interim) | `159350430` | Named strategic carriers (manual tag) |
| **Unassigned** | Cooper Kennedy | `160267902` | Catch-all: no usable HQ geography |

> Interim: West = Tim Lieto until the West hire; Tier 1 SP = Tim Ziemer (co-covered). When filled, update one line here, in territory-model.md, in the keeper's `REGION_OWNER`, and in R6's inlined map.

### State-to-Region Mapping

**Northeast -> Tim Lieto (`161889085`) - 16:**
```
NY, VA, MA, NJ, OH, PA, MI, MD, CT, DC, DE, VT, WV, NH, RI, ME
```

**Southeast -> Ken Cunningham (`162339176`) - 13:**
```
FL, IL, GA, NC, IN, MO, TN, KY, SC, AR, AL, MS, LA
```

**Central -> Tory Teague (`165480917`) - 11:**
```
TX, CO, IA, MN, OK, KS, WI, NE, NM, ND, SD
```

**West -> Tim Lieto interim (`161889085`) - 11:**
```
CA, WA, UT, OR, AZ, NV, MT, ID, WY, AK, HI
```

### Europe -> Markus Hendrich (`164949459`)

Geographic Europe ex Russia/Turkey: EU27 + EFTA/EEA + UK + microstates + non-EU Balkans/Eastern Europe (incl. UA, BY, MD). **NOT Europe (-> International):** Russia, Turkey, Caucasus (Georgia/Armenia/Azerbaijan), Kazakhstan, Greenland.

### International -> Tim Ziemer (`159350430`)

All non-US countries outside Europe, PLUS US territories (PR, GU, VI, AS, MP).

### Routing Rules

Resolve COUNTRY first, then US STATE (mirrors the keeper code so the audit and the automation never diverge).

| Scenario | Resolution |
|----------|------------|
| HQ European country (ex RU/TR) | Markus Hendrich `164949459` |
| HQ non-US outside Europe, or US territory | Tim Ziemer `159350430` |
| HQ in known US state | State -> region -> region owner |
| HQ in US, state blank/unusable | Unassigned (Cooper `160267902`) |
| Neither country nor state usable | Unassigned (Cooper `160267902`) |
| Strategic exception | Leadership reassigns; first-touch gate preserves any manual (non-Cooper) owner. Document reason in HubSpot notes. |

> **First-touch policy (keeper workflow):** `hubspot_owner_id` is written only when the current owner is unknown OR Cooper (`160267902`). A human reassignment to a rep persists and is never auto-reverted. Free-text `state` beats `hs_state_code` (verified-wrong codes exist). Country-code/US-state collisions (AL, AZ, ME, MD, VA, GE) are harmless because country resolves first.

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

## Clarification

Before running, two things that change the output:
1. **Scope** - full CRM audit, a specific owner's accounts, a single company lookup, or a batch of new imports?
2. **Write or report** - should corrections be written to HubSpot now, or produce a recommendation list for review first?

Coach: if you only have a company name or "check territories," default to read-only report mode and ask for write permission before touching any records.

---

## Task Routing

### MODE 1: FULL TERRITORY AUDIT
**Trigger:** "Audit territories" or "Check all account assignments" or "Territory hygiene"

**Steps:**

1. **Pull all companies with owner data** from HubSpot:
   - Properties needed: `name`, `domain`, `state`, `hs_state_code`, `country`, `hs_country_code`, `city`, `hubspot_owner_id`, `territory_region`, `customer_segment`
   - Page through all results (100 per page, track total)

2. **Normalize geography** for each record:
   - Country first: recognized European country -> Europe; recognized non-US/non-Europe country or US territory -> International; United States -> continue to state.
   - State: if `hs_state_code` is a valid 2-letter US state, use it; if `state` is a full name, convert to 2-letter; if `state` is already a 2-letter code, use it; prefer free-text `state` over `hs_state_code` on conflict.
   - Handle variations: "Washington, D.C." / "District of Columbia" -> DC.
   - US with no usable state -> Unassigned. Neither country nor state -> Unassigned.

3. **Look up correct owner** (country first, then US state):
   - European country (ex Russia/Turkey) -> Markus Hendrich (`164949459`)
   - Non-US, non-Europe country, or US territory (PR/GU/VI/AS/MP) -> Tim Ziemer (`159350430`)
   - US state found -> map state -> region -> region owner: Northeast or West -> Tim Lieto (`161889085`); Southeast -> Ken Cunningham (`162339176`); Central -> Tory Teague (`165480917`)
   - US but no usable state -> Unassigned (Cooper `160267902`)
   - No state AND no country -> Unassigned (Cooper `160267902`)

4. **Compare actual vs. expected owner** for each record:
   - Match -> Correctly assigned
   - Mismatch -> Flag with current owner, expected owner, and region/state
   - No owner assigned -> Flag as "Unassigned" (expected = Cooper catch-all unless geography routes it)

5. **Special owner detection:**
   - Cooper-owned (`160267902`) WITH a known US state or routable country -> flag as misassignment with recommended region owner (Cooper should only retain genuinely no-geo records).
   - Markus (`164949459`) on a record whose country is NOT European -> flag as "Possible misassignment - verify HQ" (Markus is Europe-only).
   - Tim Ziemer (`159350430`) on a US-state record -> do NOT auto-correct; this may be a Tier 1 Service Provider strategic assignment. Flag as "Verify: International/Tier 1 SP owner on US account."
   - Abilash (`159974715`) on any account -> "Possible strategic exception - do not auto-correct without verification."
   - Account has a HubSpot note containing "strategic exception" or "leadership assigned" -> skip entirely, note in report as "Skipped - strategic exception."

6. **Apollo state verification** (when running under CRM Guardian):
   - For records flagged "Unassigned" (no usable state) in step 4: call `apollo_organizations_enrich` with the company's `domain`. Extract HQ state/country. If Apollo returns a US state -> write it to `state` (Tier 1 auto-fix), then re-run steps 3-5. If Apollo returns a non-US country -> set `country` and route per step 3 (Tier 1). If Apollo returns nothing or low confidence -> leave blank, hold for manual review (Tier 3).
   - For records where HubSpot `state` disagrees with Apollo's HQ state AND `last_enriched_date` is blank or 120+ days old: trust Apollo (HubSpot value is stale). Overwrite `state` (Tier 1 if no open deals, Tier 2 if open deals - owner routing still takes priority per deal protection rules).
   - Never overwrite `state` based on Apollo when the account has a "strategic exception" / "leadership assigned" note.

7. **Produce audit report** (see Output Formats below)

**Output:**
```
TERRITORY AUDIT REPORT  -  [Date]
==================================

CORRECTLY ASSIGNED
| Count | Owner | Region |
|-------|-------|--------|

MISASSIGNED (current owner wrong for HQ geography)
| Company | Region/State | Current Owner | Expected Owner |
|---------|--------------|---------------|----------------|

COOPER-OWNED WITH KNOWN GEOGRAPHY (should route to a region)
| Company | Region/State | Recommended Owner |
|---------|--------------|-------------------|

STRATEGIC EXCEPTIONS (skipped  -  leadership assigned / Tier 1 SP / Ziemer-on-US)
| Company | Owner | Note |
|---------|-------|------|

UNASSIGNED / CATCH-ALL (no usable geography  -  Cooper)
| Company | Domain | Country | State |
|---------|--------|---------|-------|

SUMMARY: [N] correct, [N] misassigned, [N] Cooper-with-geo, [N] strategic exceptions, [N] unassigned catch-all
```

---

## Contact Owner Cascade

When a company owner is corrected (whether by territory audit or CRM Guardian):
1. Pull all contacts associated with the company via HubSpot associations
2. Update each contact's `hubspot_owner_id` to match the new company owner
3. Report: "Cascaded owner change to N contacts at [company]"

This cascade applies when running under CRM Guardian (Tier 1 auto-fix). In standalone mode, produce the cascade recommendation without writing:
```
RECOMMENDED CONTACT OWNER CASCADES
| Company | New Owner | Contacts to Update | Contact Names |
|---------|-----------|-------------------|---------------|
```

> Note: in this HubSpot instance contact owner auto-assigns off the company owner, so the company `hubspot_owner_id` write is usually sufficient and the cascade is a backstop. Verify contacts re-own when a company owner changes.

---

## Deal Protection Awareness

When auditing accounts, check for open deals (dealstage not `closedwon` or `closedlost`). Owner corrections on accounts with open deals are still safe  -  reps need correct routing regardless of deal status. The deal's own `hubspot_owner_id` is NOT changed by territory corrections. Note deal-affected corrections in the report:
```
ACCOUNTS WITH OPEN DEALS (owner corrected, deal owner unchanged)
| Company | Deal Name | Deal Stage | Owner Corrected To |
|---------|-----------|------------|-------------------|
```

When running under CRM Guardian, the Guardian's safety tier system and deal protection rule apply. See crm-guardian skill for the authoritative tier definitions.

---

## Common Patterns

- **Northeast (Tim Lieto):** NoVA colo (#1 US market), NYC/NJ carriers, the Northeast fiber + cable corridor; plus OH/MI (moved in from the old East split).
- **Southeast (Ken Cunningham):** Atlanta colo, Florida + Carolinas, plus IL/IN/MO (Chicago corridor moved in from the old East split) and TN.
- **Central (Tory Teague):** Dallas (#2) + Austin colo, Texas CLECs, the Plains/Mountain-Central states (CO, NM, the Dakotas, NE, KS, MN, IA, WI, OK).
- **West (Tim Lieto interim):** Silicon Valley + Phoenix colo, west-coast neoclouds and carriers; interim under Tim Lieto pending the West hire.
- **Europe (Markus Hendrich):** EU/EEA/UK operators and DC builders; Europe-only - flag Markus-owned non-European records.
- **International (Tim Ziemer):** EMEA (non-Europe), APAC, LATAM, Canada, ANZ, US territories; also the interim Tier 1 Service Provider book.
