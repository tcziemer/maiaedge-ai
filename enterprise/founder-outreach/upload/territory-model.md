# MaiaEdge US Territory Model

> Effective January 2026 | Mississippi River Boundary
> Questions → Cooper (RevOps)

---

## Territory Assignments

| Owner | Owner ID | Location | Coverage |
|-------|---------|----------|----------|
| **Tim Lieto** | `161889085` | Boston, MA | **30 US States** (East) |
| **Ken Cunningham** | `162339176` | Nashville, TN | **20 US States + DC** (West) |
| **Tim Ziemer** | `159350430` | — | **International** (all non-US) |

---

## State-to-Owner Mapping

### Tim Lieto — East (30 States)

```
AL, AR, CT, DE, FL, GA, IA, IL, IN, KY,
LA, MA, MD, ME, MI, MN, MO, MS, NC, NH,
NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV
```

### Ken Cunningham — West (20 States + DC)

```
AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND,
NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY
```

### Tim Ziemer — International

All non-US countries.

---

## Routing Rules

### Primary Rule: HQ State Determines Owner

Account ownership is assigned based on the company's **headquarters state**, not operational footprint. A company operating in 20 states across both territories is owned by whoever owns the HQ state.

| Scenario | Resolution |
|----------|------------|
| HQ in known US state | Map HQ state → owner per lists above |
| HQ unknown | First meaningful engagement wins (must be logged in HubSpot) |
| Non-US HQ | Tim Ziemer (International) |
| Strategic exception | Leadership can reassign named accounts with documented reason |

### Example

Brightspeed operates in 20 states across both territories. HQ is Charlotte, NC → **Tim Lieto owns it** (NC is East).

### HubSpot Implementation

- A HubSpot workflow normalizes state value variations on ingest (handles abbreviations, full names, etc.)
- The `state` property reflects **HQ location** — not operational footprint
- `hubspot_owner_id` is set based on the state-to-owner mapping

---

## Key Markets

### Tim Lieto (East)

| Segment | Key Markets |
|---------|------------|
| **Colocation** | Northern Virginia (#1 US market), Chicago (#3), Atlanta (#5) |
| **Fiber** | altafiber (OH), Hoosier Net (IN), Bluebird (MO/IL) |
| **Carrier HQs** | Verizon (NY), Lumen (LA), Frontier (CT), Windstream (AR) |

### Ken Cunningham (West)

| Segment | Key Markets |
|---------|------------|
| **Colocation** | Dallas (#2), Phoenix (#4), Austin (#6), Silicon Valley, Nashville |
| **Fiber** | Texas CLECs, SDN Communications (SD), ALLO (NE/CO) |
| **Carrier HQs** | T-Mobile (WA), AT&T (TX) |

---

## Territory Balance Rationale

State count ≠ opportunity count. The TAM is split approximately 50/50.

| Factor | Tim Lieto (30 states) | Ken Cunningham (20 + DC) |
|--------|----------------------|--------------------------|
| **TAM (companies)** | ~50% | ~50% |
| **Top Colo Markets** | #1, #3, #5 | #2, #4, #6 + Silicon Valley |
| **Growth Rate** | Mature (NoVA saturating) | DFW +30% YoY, Phoenix booming |
| **State GDP** | Many small (VT, WV, RI, ME) | TX + CA = 2 largest US economies |
| **BEAD Funding** | Distributed across 30 states | TX alone = $3.3B |
| **Travel** | Dense, easier logistics | More spread out, more flights |

---

## Quick Reference: Python Territory Lookup

```python
TERRITORY_MAP = {
    # Tim Lieto (East) — Owner ID: 161889085
    'AL': '161889085', 'AR': '161889085', 'CT': '161889085', 'DE': '161889085',
    'FL': '161889085', 'GA': '161889085', 'IA': '161889085', 'IL': '161889085',
    'IN': '161889085', 'KY': '161889085', 'LA': '161889085', 'MA': '161889085',
    'MD': '161889085', 'ME': '161889085', 'MI': '161889085', 'MN': '161889085',
    'MO': '161889085', 'MS': '161889085', 'NC': '161889085', 'NH': '161889085',
    'NJ': '161889085', 'NY': '161889085', 'OH': '161889085', 'PA': '161889085',
    'RI': '161889085', 'SC': '161889085', 'VA': '161889085', 'VT': '161889085',
    'WI': '161889085', 'WV': '161889085',

    # Ken Cunningham (West) — Owner ID: 162339176
    'AK': '162339176', 'AZ': '162339176', 'CA': '162339176', 'CO': '162339176',
    'DC': '162339176', 'HI': '162339176', 'ID': '162339176', 'KS': '162339176',
    'MT': '162339176', 'ND': '162339176', 'NE': '162339176', 'NM': '162339176',
    'NV': '162339176', 'OK': '162339176', 'OR': '162339176', 'SD': '162339176',
    'TN': '162339176', 'TX': '162339176', 'UT': '162339176', 'WA': '162339176',
    'WY': '162339176',
}

# International → Tim Ziemer: 159350430
# Unknown state → Leave unassigned for manual routing

def get_owner(state_code: str) -> str:
    """Returns HubSpot owner ID for a given 2-letter state code."""
    if not state_code or state_code.strip() == '':
        return ''  # Leave blank for manual routing
    code = state_code.strip().upper()
    return TERRITORY_MAP.get(code, '159350430')  # Default international
```

---

## Common Objections & Responses

| Objection | Response |
|-----------|----------|
| "30 vs 20 seems uneven" | Ken has Texas and California — those two alone are larger than Tim's bottom 15 states combined |
| "Why not split by state count?" | Optimized for balanced pipeline, not balanced maps. Ken's 20 states have the same TAM as Tim's 30 |
| "Is this fair to Ken?" | Ken gets the fastest-growing data center markets in the country. Tim gets more dots on a map, Ken gets more growth potential |
| "What about Nashville?" | Ken is based in Nashville — we gave him his home state so he can work local relationships |

---

## Additional Team Members (Non-Territory Sales)

| Owner | Owner ID | Role | Function |
|-------|---------|------|----------|
| Kyle Blackwell | `159701452` | Sales Engineering | Provides technical pre-sales support, POC setup, technical validation for AEs |
| Woody Acosta | `162281129` | Sales Support | Handles sales operations, pipeline management, deal administration |

**Kyle Blackwell — Sales Engineering:** Works across both US territories and international. Tim Lieto and Ken Cunningham coordinate SE support requests through Kyle. Participates in technical discovery, RFPs, and proof-of-concept validation.

**Woody Acosta — Sales Support:** Provides deal administration, contract support, and sales operations. Works with all AEs on pipeline management, pricing coordination, and order processing.
