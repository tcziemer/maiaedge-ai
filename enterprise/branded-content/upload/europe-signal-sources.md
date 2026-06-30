# Europe Signal Sources (GM Europe reference)

> The US signal fleet keys off US-only sources (BEAD broadband awards, FCC Broadband Data Collection, US peering data). None of those exist in Europe. This file supplies the European equivalents so the same signal framework (`context/signals/`) and the same scoring, codes, and 14-day freshness rules apply, just pointed at European sources.
> Sources verified June 2026 (foot of file). Verify a specific program's current status before it anchors a customer-facing claim.

---

## How to use this

The signal *framework* does not change: same score floor, same heat enum (Hot / Warm / Cool / Cold), same rule that a signal earns a DIRECT outreach opener only when it is fresh (event date <=90 days, ideally <=60). What changes is WHERE you look. Use the mapping below to translate a US-source habit into its European counterpart, then scan the source registry.

## US source to EU source mapping

| US signal source | What it tells you | European equivalent |
|---|---|---|
| BEAD broadband awards | Who just got funded to build | National broadband programs + EU funds: Germany Gigabitforderung 2.0, the UK gigabit program, France THD, Italy PNRR broadband; EU-level CEF2 Digital, the Connecting Europe Broadband Fund, and promotional banks (KfW, Caisse des Depots, Cassa Depositi e Prestiti, EIB) |
| FCC Broadband Data Collection / filings | Who operates where, licensing | National regulators: BNetzA (DE), Ofcom (UK), ARCEP (FR), AGCOM (IT), CNMC (ES), ACM (NL), PTS (SE), Nkom (NO), Traficom (FI); BEREC at EU level |
| (no US analog at this scale) | State-backed AI infrastructure | EuroHPC JU AI gigafactory awards, InvestAI, national sovereign-AI and sovereign-cloud programs |
| US peering / PeeringDB | Interconnection footprint | PeeringDB (global, covers Europe), plus the European IXs directly (DE-CIX, AMS-IX, LINX, France-IX and national IXs) |
| US data-center trackers | New builds, capacity | DataCenterMap, datacenters.com, plus the EMEA trade press below |

## Signal types that matter most in Europe

- **AI / sovereign-AI buildout:** EuroHPC AI gigafactory selections, neocloud funding rounds and site announcements (Nscale, Nebius and peers), hyperscaler and sovereign-cloud capacity announcements in spill markets (Nordics, Spain, Italy, Poland).
- **Fiber and gigabit buildout:** national-program awards, alt-net funding and consolidation, open-access wholesale launches, FTTP rollout milestones ("Ausbau").
- **Carrier / wholesale moves:** new subsea or terrestrial routes, NNI and interconnection launches, managed-service launches, M&A among carriers and aggregators.
- **Regulatory triggers (Europe-specific and powerful):** DORA supervisory actions and deadlines, NIS2 enforcement and first penalties, EU Data Act obligations, EU AI Act milestones (full application Aug 2026). These create concrete, dated reasons a regulated buyer must act, which is the strongest kind of forward-state hook.
- **Executive moves:** buying-persona hires (VP Network, Head of Infrastructure, CTO, CISO under DORA pressure) at target accounts.
- **Anchor leases and power deals:** capacity and PPA announcements in the emerging markets, which front-run the network buildout.

## Source registry

**EU bodies and funding programs**
- European Commission DG CONNECT and "Shaping Europe's digital future" (policy, broadband, funding calls).
- EuroHPC JU (AI gigafactories, supercomputing) and the InvestAI initiative (€20B for up to 4-5 gigafactories).
- CEF2 Digital (Connecting Europe Facility) and the Connecting Europe Broadband Fund.
- European Investment Bank and the national promotional banks (KfW, Caisse des Depots, Cassa Depositi e Prestiti).

**National regulators (telecom / spectrum / connectivity)**
- Germany: Bundesnetzagentur (BNetzA). UK: Ofcom. France: ARCEP. Italy: AGCOM. Spain: CNMC. Netherlands: ACM. Sweden: PTS. Norway: Nkom. Finland: Traficom. EU-level coordination: BEREC.

**National broadband programs**
- Germany: Gigabitstrategie (gigabit + 5G by 2030, ~€17B) and Gigabitforderung 2.0.
- UK: the national gigabit program plus the alt-net buildout (track via Ofcom and ISPreview).
- France: Plan France Tres Haut Debit. Italy: PNRR broadband measures. Verify current program names and budgets before quoting.

**Interconnection and data-center data**
- PeeringDB; the IXs (DE-CIX, AMS-IX, LINX, France-IX, ESPANIX, MIX, Netnod and others); DataCenterMap; datacenters.com.

**Trade press (EMEA)**
- Capacity Media, Data Centre Dynamics (DCD), Data Center Knowledge, Light Reading, Total Telecom, Broadband World/ISPreview (UK). National tech press: Heise / Golem (DE) and equivalents.

**Events (signal and relationship surface)**
- Capacity Europe, International Telecoms Week (ITW), MWC Barcelona, Datacloud Global Congress, DCD Connect (regional editions), FTTH Council Europe Conference, and national fiber and telco shows. Use the `event-intelligence` skill for prep and follow-up.

## Automation status (flag for RevOps)

The scheduled `weekly-signal-scan` fleet currently scans US-tilted sources and the per-segment catalogs in `context/signals/` are US-anchored. Until RevOps extends the catalogs and the scan to the European sources above, treat European signals as a manual / `account-sourcing`-assisted motion: pull from these sources directly, and feed net-new European accounts to RevOps for enrichment. Do not assume the Monday brief is covering Europe yet.

---

## Sources (verified June 2026)

- EU and national broadband funding (CEF2 Digital, CEBF, Gigabitstrategie / Gigabitforderung 2.0, promotional banks): [European Commission, Connecting Europe Broadband Fund](https://digital-strategy.ec.europa.eu/en/library/connecting-europe-broadband-fund); [White & Case, Funding Europe's broadband ambitions](https://www.whitecase.com/insight-our-thinking/funding-europes-broadband-ambitions); [Business Sweden, Germany digital expansion (Sep 2025)](https://www.business-sweden.com/insights/blogs/germany-a-new-era-for-investment/germany-accelerates-digital-expansion-as-of-12-september-2025/).
- EuroHPC AI gigafactories / InvestAI: [STL Partners](https://stlpartners.com/articles/data-centres/eu-ai-gigafactory-initiative/); [EuroHPC JU mandate amendment (Jan 2026)](https://eurohpc-ju.europa.eu/eurohpc-jus-mandate-expanded-under-new-regulation-amendment-2026-01-20_en).
- Regulatory enforcement timelines (DORA, NIS2, Data Act, AI Act): see `sovereignty-positioning.md` sources.
