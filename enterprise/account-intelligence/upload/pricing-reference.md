# MaiaEdge Pricing Reference

> Revision Date: January 21, 2026
> All prices USD list prices
> **This is the single source of truth for all commercial pricing and discount policy.**

---

## CRITICAL: Annual Price vs. TCV Distinction

**Order Forms display Annual Price, not TCV.**

- **Annual Price** = Total Contract Value (TCV) ÷ Number of Years
- **TCV** = Actual amount a customer pays over the contract term
- **Example:** A 36-month 100G PBC costs $68,811 TCV. Annual Price = $68,811 ÷ 3 = $22,937.00

When quoting: Always show Annual Price on Order Forms. Show TCV in deal summary for pipeline tracking.

---

## Production Path Border Controllers (PBC + PCE Bundle)

### Standard Bandwidth & Term Options

| SKU | Bandwidth | Term | TCV | Annual Price |
|-----|-----------|------|-----|-------------|
| ME-PBC-PCE-100G-12M | 100G | 12 mo | $30,275 | $30,275.00 |
| ME-PBC-PCE-100G-36M | 100G | 36 mo | $68,811 | $22,937.00 |
| ME-PBC-PCE-100G-60M | 100G | 60 mo | $114,192 | $19,032.00 |
| ME-PBC-PCE-10G-12M | 10G | 12 mo | $15,325 | $15,325.00 |
| ME-PBC-PCE-10G-36M | 10G | 36 mo | $34,968 | $11,656.00 |
| ME-PBC-PCE-10G-60M | 10G | 60 mo | $58,033 | $9,672.17 |
| ME-PBC-PCE-1G-36M | 1G | 36 mo | $18,046 | $6,015.33 |
| ME-PBC-PCE-1G-60M | 1G | 60 mo | $29,954 | $4,992.33 |

**Note:** 1G bandwidth is only available in 36/60-month terms (no 12-month option).

---

## High Availability (HA) / Standby PBCs

**Pricing Rule: HA units are priced at 30% off the equivalent standard unit.**

| SKU | Bandwidth | Term | TCV | Annual Price |
|-----|-----------|------|-----|-------------|
| ME-PBC-PCE-100G-12M-HA | 100G | 12 mo | $21,193 | $21,193.00 |
| ME-PBC-PCE-100G-36M-HA | 100G | 36 mo | $48,168 | $16,056.00 |
| ME-PBC-PCE-100G-60M-HA | 100G | 60 mo | $79,934 | $13,322.33 |
| ME-PBC-PCE-10G-12M-HA | 10G | 12 mo | $10,728 | $10,728.00 |
| ME-PBC-PCE-10G-36M-HA | 10G | 36 mo | $24,478 | $8,159.33 |
| ME-PBC-PCE-10G-60M-HA | 10G | 60 mo | $40,623 | $6,770.50 |
| ME-PBC-PCE-1G-36M-HA | 1G | 36 mo | $12,632 | $4,210.67 |

**Note:** No 1G HA option for 60-month term.

**When to quote HA:** Customers requiring redundancy or failover capability. Typical colocation, fiber operators, and network operators want HA. Most POCs and test deployments do not.

---

## Maia Path Port Extender (MPP-48)

48-port tenant access switch. Paired with PBC in colocation deployments. Fans out cross-connects to tenant ports.

| SKU | Term | TCV | Annual Price | Notes |
|-----|------|-----|-------------|-------|
| ME-MPP-48-12M | 12 mo | $8,990 | $8,990.00 | Standard 12-month term |
| ME-MPP-48-12M-LAB | 12 mo | $8,990 | $8,990.00 | Lab/test deployment variant (same price) |
| ME-MPP-48-36M | 36 mo | $19,987 | $6,662.33 | 3-year commitment discount |
| ME-MPP-48-60M | 60 mo | $33,312 | $5,552.00 | 5-year commitment discount |

**When to quote MPP-48:** Only for colocation operators deploying in meet-me rooms with tenant connectivity needs. Not for fiber operators or network operators.

---

## Proof of Concept (POC) SKUs

60-day POC licenses for evaluation. Includes hardware and software access.

| SKU | Description | Term | Price | Notes |
|-----|-------------|------|-------|-------|
| ME-PBC-PCE-POC60 | PBC + PCE POC License | 60 days | $2,490 | Includes hardware and full PCE functionality |
| ME-MPP-48-POC60 | Port Extender POC License | 60 days | $749 | 48-port switch for colocation test |

**POC flow:** Quote POC license for evaluation. Upon successful validation and decision to proceed, customer signs MSA and places production order. POC pricing is NOT credited toward production orders.

---

## Discount Policy

**Default = List Price. NO discount is applied unless explicitly requested.**

**Key principles:**

1. **All prices above are list prices.** Discounts are NOT automatic.
2. **Discounts are only applied when a specific percentage or amount is stated** by leadership or explicitly negotiated.
3. **Term commitment is the PRIMARY discount lever** — customers get better per-unit pricing by committing to 36/60-month terms vs. 12-month.
4. **Secondary levers:** Volume (multiple units in initial order), strategic value (reference customers, market expansion).

**Discount approval:** Sales reps do NOT have discount authority. All discounts >5% require approval from CRO (Timothy Ziemer) or CEO (Abilash Menon).

### Historical Discount Range

Based on actual deals:
- **Standard:** 0% (list price)
- **Volume / Strategic:** 10-20% (multiple units or strategic reference)
- **Competitive displacement:** Up to 35% (documented competitive scenario)

**Largest discount to date:** 35% (IENTC, Mexico, first international customer, 3x unit order, strategic importance).

---

## Mid-Term Expansion Pricing

When a customer adds PBCs during an active contract term:

1. **Honor existing pricing** — Expansions use the pricing from the original Purchase Agreement (no renegotiation).
2. **Co-termination** — New PBCs align to the original contract end date, not a new 12/36/60-month term.
3. **Pro-rated billing** — Customer pays for remaining months in the contract term only.

### Example

Customer signed a 36-month deal in January 2025 for 3 PBCs at $25,000/unit. In July 2025, they want to add 2 more PBCs.

- **Price per unit:** $25,000 (original pricing, no change)
- **Co-termination:** New PBCs expire January 2028 (with original units)
- **Billing:** Pro-rated for 30 months remaining (July 2025 to January 2028)
- **Total for 2 units:** $25,000 × 2 × (30 months ÷ 36 months) = ~$41,667

---

## Commercial Model Summary

| Aspect | Detail |
|--------|--------|
| **Spend Type** | OpEx (subscription, not CapEx) |
| **Hardware Ownership** | MaiaEdge retains title; customer has full operational control |
| **Billing Frequency** | Annual, quarterly, or monthly (annual preferred) |
| **Payment Terms** | Net 30 from invoice date |
| **Auto-Renewal** | Monthly auto-renew unless 30-day written termination notice |
| **Price Increases** | Capped at greater of 5% or CPI annually (60-day notice) |
| **Multi-Tenant Allowed** | Yes, customer may configure MaiaEdge for end-customer use |
| **Support SLA** | 99.9% Service Availability. Sev 1 acknowledgment within 2 hours. 24/7 support |

---

## Example Quote Scenarios

### Scenario 1: Regional Fiber Operator (Standard Deal)

- **Product:** 3x ME-PBC-PCE-100G-36M
- **Quantity:** 3 units
- **Unit TCV:** $68,811 each
- **Subtotal TCV:** $206,433
- **Discount:** 0% (list price)
- **Total TCV:** $206,433
- **Annual Price (for Order Form):** $22,937.00 per unit
- **Contract Term:** 36 months
- **Payment:** $68,811 per unit annually = $206,433/year for 3 years
- **Support:** Included. 99.9% SLA. Sev 1 within 2 hours.

### Scenario 2: Colocation with Port Extender (Colo Package)

- **Products:** 1x ME-PBC-PCE-100G-36M + 1x ME-MPP-48-36M
- **PBC TCV:** $68,811
- **MPP TCV:** $19,987
- **Subtotal TCV:** $88,798
- **Discount:** 0% (list price)
- **Total TCV:** $88,798
- **Annual Price:** PBC $22,937 + MPP $6,662.33 = $29,599.33/year
- **Contract Term:** 36 months
- **Note:** Port extender must pair with PBC; never sold standalone.

### Scenario 3: POC Pilot (Evaluation)

- **Product:** 1x ME-PBC-PCE-POC60 + 1x ME-MPP-48-POC60
- **PBC POC:** $2,490
- **MPP POC:** $749
- **Total:** $3,239
- **Duration:** 60 days
- **What's Included:** Full PBC/PCE functionality, white-label portal, API access, 24/7 support during POC
- **Next Step:** Upon success, customer signs MSA and places production order. POC pricing not credited.

---

## IENTC Quote Example (Actual Customer — Nov 2025)

**Context:** First international customer in Mexico. Mobile backhaul provider. 800+ cell towers, 20+ data centers.

| Item | Qty | Unit Price | Extended |
|------|-----|-----------|----------|
| ME-PBC-PCE-100G-36M | 3 | $68,811 | $206,433 |
| **Subtotal (List)** | | | $206,433 |
| **Discount (35%)** | | | ($72,252) |
| **Total** | | | $134,181 |

**Additional Terms:**
- **Payment:** Quarterly in advance, Net 30
- **Delivery:** FCA Burlington, MA (Incoterms 2020) — risk transfers to customer at carrier pickup
- **Importer of Record:** Customer handles all customs documentation
- **Taxes/Duties/Tariffs:** Customer responsible (not included in quote)
- **Support:** 99.9% Service Availability, 24/7 support, included in subscription
- **MSA Term:** 36 months
- **Quote Valid:** 30 days (from issuance date), subject to credit approval

---

## Discount Discussion Tips for Sales Teams

**Use this language to open price conversations without over-discounting:**

"Term commitment is the primary lever. A 36 or 60-month commitment unlocks better per-unit pricing. Volume also matters — the more PBCs in the initial order, the better the discount. What's your planning horizon, and how many units are we talking about in Year 1?"

**If customer asks for discount unprompted:**

"We price based on term commitment and volume. If you're willing to commit to 36 or 60 months, the annual price is significantly better than 12-month. That's where we see the most value alignment."

**If customer says competitor is cheaper:**

"Let's compare apples-to-apples. Are they 60-month terms? Are they carrier infrastructure or NaaS/orchestration? What support SLA are they offering? Our list price is competitive with the market, but if we align on term and volume, we can optimize the economics."

---

## Price Change History & Effective Dates

**Last updated:** January 21, 2026

**Previous pricing effective:** December 1, 2025

**Known upcoming changes:** None announced (as of Feb 2026)

**Process:** Prices are reviewed quarterly. Any changes are communicated to sales with 30-day notice.
