# MaiaEdge Territory Model

> Effective 2026-06-17 | 5-Region North America + Europe + International
> Supersedes the Jan 2026 two-region (East/West) model. The live HubSpot keeper workflow "Territory Assignment (Go-Forward)" (Company-based, flow `4405143279`, go-forward enrollment + first-touch owner gate) is the executable implementation of this map. Keep this doc, the `territory-manager` skill, R1 Fresh Enrichment, and R6 Territory & Hygiene's inlined map all in sync with it and with the keeper's `REGION_OF` / `REGION_OWNER`.
> Questions -> Cooper (RevOps)

---

## Territory Assignments

| Region | Owner | HubSpot Owner ID | Coverage |
|--------|-------|------------------|----------|
| **Northeast** | Tim Lieto | `161889085` | 16 US states (incl. DC) |
| **Southeast** | Ken Cunningham | `162339176` | 13 US states |
| **Central** | Tory Teague | `165480917` | 11 US states |
| **West** | Tim Lieto (interim) | `161889085` | 11 US states |
| **Europe** | Markus Hendrich | `164949459` | Geographic Europe ex Russia/Turkey |
| **International** | Tim Ziemer | `159350430` | All other non-US (Canada, LATAM, APAC, MEA, ANZ) + US territories |
| **Tier 1 Service Provider** | Tim Ziemer (interim) | `159350430` | Named strategic carriers (manual tag, not geo-derived) |
| **Unassigned** | Cooper Kennedy | `160267902` | Catch-all: no usable HQ geography |

> **Interim owners:** West is covered by Tim Lieto until the West hire lands; Tier 1 Service Provider is co-covered (Tim Ziemer primary). When either is filled, change ONE line in (a) the region->owner map below, (b) the keeper workflow's `REGION_OWNER`, (c) the `territory-manager` skill, and (d) R6's inlined map.

---

## State -> Region Map (50 states + DC, authoritative)

**Northeast -> Tim Lieto (16):** NY, VA, MA, NJ, OH, PA, MI, MD, CT, DC, DE, VT, WV, NH, RI, ME
**Southeast -> Ken Cunningham (13):** FL, IL, GA, NC, IN, MO, TN, KY, SC, AR, AL, MS, LA
**Central -> Tory Teague (11):** TX, CO, IA, MN, OK, KS, WI, NE, NM, ND, SD
**West -> Tim Lieto interim (11):** CA, WA, UT, OR, AZ, NV, MT, ID, WY, AK, HI

> Realignment vs the old two-region model: OH + MI moved into Northeast; IL + IN + MO moved into Southeast; Central is a NEW region (TX, CO, IA, MN, OK, KS, WI, NE, NM, ND, SD) owned by Tory Teague.

---

## Europe Country Set -> Markus Hendrich (`164949459`)

All of geographic Europe EXCEPT Russia and Turkey.

- **EU27:** AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE
- **EFTA/EEA + UK:** NO IS LI CH GB
- **Microstates / territories:** MC AD SM VA (Vatican) GI (Gibraltar) FO (Faroe) AX (Aland)
- **Non-EU Eastern Europe / Balkans:** AL BA RS ME MK XK MD UA BY

**Explicitly NOT Europe (-> International / Tim Ziemer):** Russia (RU), Turkey (TR), the Caucasus (Georgia GE, Armenia AM, Azerbaijan AZ), Kazakhstan (KZ), and Greenland (GL, geographically North America).

> Country-code collisions with US state codes (AL, AZ, ME, MD, VA, GE) are harmless: routing resolves COUNTRY first, then applies US-state logic only when the country is US or blank (see Routing Rules).

---

## International -> Tim Ziemer (`159350430`)

All non-US countries outside Europe (Canada, LATAM, APAC, Middle East, Africa, ANZ), PLUS US territories (Puerto Rico PR, Guam GU, US Virgin Islands VI, American Samoa AS, Northern Mariana Islands MP) per Cooper's rule.

---

## Routing Rules

### Resolution order: COUNTRY first, then US STATE

This mirrors the keeper workflow's code so the doc and the automation never diverge.

1. **Normalize country** (free-text `country` first, then ISO `hs_country_code`):
   - Recognized European country -> **Europe** (Markus). A recognized foreign free-text `country` wins even if `hs_country_code` says `US` (corrects mislabeled records).
   - Recognized non-Europe non-US country, OR a US territory -> **International** (Ziemer).
   - United States -> continue to state logic.
   - Unrecognized country BUT a valid US state is present -> treat as US.
2. **Normalize US state** (free-text `state` first - full name or 2-letter - then `hs_state_code`):
   - Valid US state -> region per the State -> Region map -> region owner.
   - US but no usable state -> **Unassigned** (Cooper).
3. **Tier 1 Service Provider** is a manual region tag for named strategic carriers (owner Tim Ziemer interim). Not auto-derived from geography.

| Scenario | Resolution |
|----------|------------|
| HQ in known US state | State -> region -> owner |
| HQ in US, state blank/unusable | Unassigned (Cooper `160267902`) |
| HQ in Europe (ex RU/TR) | Markus Hendrich `164949459` |
| HQ non-US outside Europe, or US territory | Tim Ziemer `159350430` |
| Neither country nor state usable | Unassigned (Cooper `160267902`) |
| Strategic exception | Leadership reassigns; the keeper's first-touch gate preserves any manual (non-Cooper) owner |

> **First-touch policy:** the keeper writes `hubspot_owner_id` only when the current owner is unknown OR Cooper (`160267902`). A human reassignment to a rep persists and is never auto-reverted. Free-text `state` beats `hs_state_code` (verified-wrong codes seen during build, e.g. code TX but state Ohio).

### HubSpot Implementation

- The keeper workflow normalizes `state`/`country` and routes; it writes `territory_region`, normalized `hs_state_code`, and (first-touch only) `hubspot_owner_id`.
- The `state` property reflects **HQ location**, not operational footprint. A company operating across many states is owned by whoever owns the HQ state's region.

---

## Quick Reference: Python Territory Lookup

```python
REGION_OF = {
    # Northeast -> Tim Lieto (161889085)
    'NY': 'Northeast', 'VA': 'Northeast', 'MA': 'Northeast', 'NJ': 'Northeast',
    'OH': 'Northeast', 'PA': 'Northeast', 'MI': 'Northeast', 'MD': 'Northeast',
    'CT': 'Northeast', 'DC': 'Northeast', 'DE': 'Northeast', 'VT': 'Northeast',
    'WV': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'ME': 'Northeast',
    # Southeast -> Ken Cunningham (162339176)
    'FL': 'Southeast', 'IL': 'Southeast', 'GA': 'Southeast', 'NC': 'Southeast',
    'IN': 'Southeast', 'MO': 'Southeast', 'TN': 'Southeast', 'KY': 'Southeast',
    'SC': 'Southeast', 'AR': 'Southeast', 'AL': 'Southeast', 'MS': 'Southeast', 'LA': 'Southeast',
    # Central -> Tory Teague (165480917)
    'TX': 'Central', 'CO': 'Central', 'IA': 'Central', 'MN': 'Central', 'OK': 'Central',
    'KS': 'Central', 'WI': 'Central', 'NE': 'Central', 'NM': 'Central', 'ND': 'Central', 'SD': 'Central',
    # West -> Tim Lieto interim (161889085)
    'CA': 'West', 'WA': 'West', 'UT': 'West', 'OR': 'West', 'AZ': 'West', 'NV': 'West',
    'MT': 'West', 'ID': 'West', 'WY': 'West', 'AK': 'West', 'HI': 'West',
}

REGION_OWNER = {
    'Northeast':               '161889085',  # Tim Lieto
    'Southeast':               '162339176',  # Ken Cunningham
    'Central':                 '165480917',  # Tory Teague
    'West':                    '161889085',  # Tim Lieto (interim)
    'Europe':                  '164949459',  # Markus Hendrich
    'International':           '159350430',  # Tim Ziemer
    'Tier 1 Service Provider': '159350430',  # Tim Ziemer (interim)
    'Unassigned':              '160267902',  # Cooper (catch-all)
}

EUROPE = {  # ISO-2; geographic Europe ex Russia/Turkey
    'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU',
    'MT','NL','PL','PT','RO','SK','SI','ES','SE','NO','IS','LI','CH','GB','MC','AD','SM','VA',
    'GI','FO','AX','AL','BA','RS','ME','MK','XK','MD','UA','BY',
}
US_TERRITORIES = {'PR', 'GU', 'VI', 'AS', 'MP'}  # -> International

def get_owner(state_code: str = '', country_code: str = '') -> str:
    """Country first, then US state. Returns owner ID. Unassigned -> Cooper 160267902."""
    c = (country_code or '').strip().upper()
    if c in EUROPE:
        return REGION_OWNER['Europe']               # Markus
    if c in US_TERRITORIES:
        return REGION_OWNER['International']         # Ziemer (US territories -> Intl)
    if c and c not in ('US', 'USA'):
        return REGION_OWNER['International']         # any other non-US -> Ziemer
    region = REGION_OF.get((state_code or '').strip().upper())
    if region:
        return REGION_OWNER[region]
    return REGION_OWNER['Unassigned']               # US/unknown, no usable state -> Cooper
```

> The keeper workflow's Node.js code is the authoritative executable version (it adds the foreign free-text override, a full-name->code table, and US-territory ISO handling). This Python is the readable reference. Keep both in sync.

---

## Territory Balance

The two-region 30-vs-20 balance rationale from the Jan 2026 model is retired. Under the 5-region model, US coverage is split Northeast / Southeast / Central / West with Central carved out for Tory Teague; Europe is a dedicated region (Markus); everything else is International (Tim Ziemer). Load balance across the new regions is being re-evaluated by RevOps and is not yet codified here.

---

## Additional Team Members (Non-Territory Sales)

| Owner | Owner ID | Role | Function |
|-------|----------|------|----------|
| Kyle Blackwell | `159701452` | Sales Engineering | Technical pre-sales support, POC setup, technical validation for AEs across all territories |
| Woody Acosta | `162281129` | Sales Support | Sales operations, pipeline management, deal administration for all AEs |

**Kyle Blackwell - Sales Engineering:** Works across all US regions, Europe, and International. Reps coordinate SE support through Kyle. Participates in technical discovery, RFPs, and POC validation.

**Woody Acosta - Sales Support:** Provides deal administration, contract support, and sales operations across all AEs (pipeline management, pricing coordination, order processing).
