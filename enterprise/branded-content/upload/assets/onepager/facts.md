# One-Pager Facts Block (single source of truth)

**CREDIBILITY RULE (non-negotiable).** A brief states ONLY what is verified. If you cannot point to a primary
source for a claim THIS run, it does not go in the brief. One verified fact beats three shaky ones, and a
single wrong or unprovable claim costs the meeting and the credibility behind it. When in doubt, leave it out,
or state it qualitatively / forward-state ("as the platform widens") instead of as a hard fact.

`qa.py` enforces the mechanical half of this: every number in the brief (stat strip AND body prose) must
appear in the APPROVED fence below, and currency / percent signs are blocked from the body. The non-numeric
half (claims about the account's stack, footprint, customers, plans, and any market claim) is on the writer:
research it this run, do not assert it from memory.

RevOps owns this file. To approve a new number, verify it against a primary source, then add it to the fence
below with its source + date.

<!-- QA-APPROVED-STAT-TOKENS  (qa.py reads between these markers. Add a token ONLY after you have verified it.)
minutes
zero
hop by hop
60-90 days
line rate
1ru
2c vs 9c
<2 microsec
aes-256
100g
dual 100g
APPROVED-NUMBERS: 1 2 9 60 90 100 256
QA-APPROVED-STAT-TOKENS-END -->

---

## 1. Approved stat-strip tokens (MaiaEdge product, verified internal)

The only big numbers allowed in the 3-up stat strip. Source: `context/product/proof-points.md`,
`context/product/ai-market-positioning.md`, `context/product/pbc-pce-datasheet.md`. Pick three that fit the
segment's pillars. For operator segments pair speed with ownership ("your team", "under your brand"); for
neoclouds and Enterprise use data-sovereignty framing, never operator resale.

| Token | Means | Pairs with |
|---|---|---|
| `Minutes` | New sites and customers on private paths in minutes, not a multi-week project | INSTANT |
| `60-90 days` | The legacy way to stand up cross-region connectivity / an NNI | INSTANT (contrast) |
| `Zero` | Zero routing protocols for the team to run (no BGP / MPLS) | INSTANT / DETERMINISTIC |
| `Hop by hop` | Hop-by-hop visibility end to end, including paths you do not own | DETERMINISTIC |
| `2c vs 9c` | Private egress economics, roughly 2c/GB vs ~9c/GB public | PRIVATE (neocloud) |
| `Line rate` | Line-rate AES-256-GCM encryption on every path, no performance penalty | PRIVATE |
| `1RU` | Single 1RU device per site, dual 100G, deploys in the meet-me room | (technical proof) |
| `<2 microsec` | Sub-2-microsecond path overhead | DETERMINISTIC (technical) |

Write number tokens with hyphens, never en dashes (`60-90 days`, not the en-dash form). No em dashes anywhere.

## 2. Approved inline proof points (verified internal; use in body / plays)

- Provision private, deterministic paths in minutes across any network (pair with ownership for operators).
- One device at each site or point of presence, plus cloud orchestration.
- Hop-by-hop telemetry across paths you do not own; prove where a problem actually lives.
- Line-rate AES-256-GCM on every path; encryption at the infrastructure layer, not a VPN overlay.
- Sovereign routing: provision paths that avoid specific regions, carriers, or untrusted segments.
- Works as an overlay; complements InfiniBand, Spectrum-X, Ultra Ethernet inside the facility.

## 3. External market facts - NOT pre-approved. Re-verify THIS run or leave out.

These are NOT MaiaEdge facts, they are NOT approved, and they go stale. They are listed only so you know what
would need RE-VERIFICATION if you ever wanted to use one. Do not paste from memory. To use one: confirm the
exact figure + date against a current primary source this run, then add the number to the fence above with the
source. **Default behavior: leave it out.** The brief must stand without it. The clean way to make a why-now
land is forward-state framing about the account's own trajectory, which needs no external stat at all.

| Claim | Last-known value (UNVERIFIED - re-check before any use) | Source to re-check |
|---|---|---|
| A connectivity provider raising to move into GPU/AI compute | a 2026 raise, figure unconfirmed | the provider's press release / filing |
| Analyst audit of neocloud networking-readiness | an analyst note, figures + quote unconfirmed | the analyst publication |
| EU AI Act application timing | a 2026 application date, scope-dependent | the EU AI Act text for the buyer's scope |
| Cloud on-ramp / wholesale economics (ACG Research) - **SP / fiber / colo ONLY; never neocloud or enterprise** | ~67% TCO savings, ~67% wholesale margin / ~6-mo payback, ~53% Ethernet-over-DIA savings | `context/product/economic-impact-acg-whitepaper.md`, then re-verify vs the ACG source |

Never name a competitor in the brief unless the prospect raised them first; "a connectivity provider" /
"third-party fabric providers" is the default.
