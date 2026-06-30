# Europe Market Map (GM Europe reference)

> For the MaiaEdge GM Europe motion. Geography, the peering fabric, the segment landscape, the regulators that generate signals, and a starting segment-priority view. Pairs with `europe-signal-sources.md` and `sovereignty-positioning.md`.
> Market facts last verified June 2026 (sources at the foot). Company names are illustrative anchors to orient the map, NOT pre-classified accounts. Segment, sub-segment, tier, and owner are still set by enrichment + HQ, never by this list.

---

## The regional thesis in three sentences

Europe is mid-buildout and power-constrained, so new AI and capacity are spilling out of the saturated core into secondary markets. Sovereignty is shifting from a talking point to a procurement requirement as the EU Data Act, NIS2, DORA, and the AI Act land. MaiaEdge's sharpest European wedge is therefore sovereign routing sold to operators who can monetize it as a service, with the sovereign-AI buildout as a fast-growing second front.

## Geography: the core and the spill

**FLAP-D core: Frankfurt, London, Amsterdam, Paris, Dublin.** Roughly 45% of European operational capacity sits here. Combined live capacity more than doubled from about 1.8 GW (2019) to about 3.6 GW (2025), and FLAP-D colocation vacancy hit a record low near 6.3% in Q4 2025. The core is now power-constrained: Frankfurt paused some AI development pending new power, Amsterdam is limiting new builds into the 2030s, and Dublin/Ireland permitting is slow and tied to self-generation. Translation: the core is where the installed base, the interconnection density, and the latency-sensitive inference and enterprise workloads live, but it is not where the easy new megawatts are.

**The spill / emerging markets: Nordics, Spain (Madrid), Italy (Milan), Poland (Warsaw), Portugal, Belgium.** Power and land availability are pushing large-scale AI training and new capacity here. Over half of AI-driven growth is expected in Tier 2 and emerging markets. The Nordics (cheap renewable power, cold climate) draw training clusters; Madrid and Milan are the fastest-rising southern hubs; Warsaw anchors CEE. The European Data Centre Association projects roughly €176B of cumulative investment 2026-2031, with grid readiness (not capital) as the main constraint.

**What this means for sequencing.** The warm, dense relationship market is the FLAP-D core plus the national incumbents. The greenfield-and-buildout opportunity is in the spill markets. A GM has to decide how much to work each; see segment priority below.

## The peering fabric (the European interconnection layer)

Europe's internet exchanges are central infrastructure and a natural relationship and event surface, in a way that has no exact US equivalent.

- **DE-CIX (Frankfurt)** is among the largest internet exchanges in the world by traffic and the gravitational center of German and Central European interconnection. DE-CIX also runs exchanges in other metros.
- **AMS-IX (Amsterdam)**, **LINX (London)**, and **France-IX (Paris)** anchor their national markets.
- Secondary and national IXs matter for the spill markets: ESPANIX (Madrid), MIX (Milan), PLIX / Equinix IX (Warsaw), Netnod (Sweden), and others.

Why it matters for MaiaEdge: interconnection-dense operators and the members of these exchanges are the population that feels federation and handoff pain most acutely, and the exchanges themselves are where the European carrier and fiber community gathers.

## Segment landscape, weighted for Europe

The six MaiaEdge ICP segments are unchanged. What changes is the weighting, the named anchors, and the door you knock on.

### Network Operators and Carriers (likely warmest first door)
European carriers and wholesale operators own national and cross-border networks as profit centers and are under direct sovereignty pressure from government and defense customers. This is the segment that maps most closely to Markus's background and where sovereign routing is most obviously a sellable, high-margin service.
- *Incumbents / Tier 1:* Deutsche Telekom (DE), Orange (FR), Telefonica (ES), Vodafone (UK/DE), Telecom Italia / Sparkle (IT), BT (UK), Proximus (BE), Swisscom (CH), Telia and Telenor (Nordics), KPN (NL).
- *Wholesale / pan-European backbone:* Colt, euNetworks, GTT, Arelion (ex-Telia Carrier), Telxius, Sparkle, Zayo Europe.
- *Door:* operator-monetization plus sovereignty-as-a-service for defense/government/finance customers.

### Fiber Operators (broad, fragmented, buildout-heavy)
Europe's fiber market is more fragmented and earlier in the FTTP buildout than the US in many countries, often shaped by open-access and wholesale models (the "Open Access" and "Ausbau" world). Many regional and alt-net operators.
- *Anchors:* Deutsche Glasfaser (DE), CityFibre and Gigaclear (UK alt-nets), Open Dutch Fiber and Delta Fiber (NL), Open Fiber (IT), Adamo (ES), plus numerous regional and municipal builders.
- *Door:* wholesale/handoff economics and the ability to offer differentiated, policy-routed services on top of the fiber plant.

### Colocation and AI-Infrastructure Colo (dense in core, building in spill)
- *Operating heavily in Europe:* Equinix, Digital Realty / Interxion, Telehouse, Global Switch, Data4, Vantage, NorthC, maincubes, Green Mountain (Nordics), Start Campus (PT). (Several are US/global-HQ; HQ and enrichment decide ownership and classification.)
- *Door:* interconnection differentiation and AI-tenant enablement; AI-colo where liquid cooling and high-density power are present.

### Neoclouds and Sovereign AI (loudest, fast-growing, second door not first by default)
Europe is in an explicit sovereign-AI push. A €20B EU AI-gigafactory program under InvestAI targets up to 4-5 gigafactories (about 100,000 advanced processors each); EuroHPC JU's mandate was expanded in Jan 2026 to build and operate them. The neocloud wave is well funded.
- *Sovereign-AI neoclouds:* Nscale (NVIDIA-backed, Stargate Norway, raised a ~$2B Series C in Mar 2026 at ~$14.6B), Nebius (NL-HQ, Nvidia-invested, multi-GW plan), Fluidstack, Sesterce, Lyceum.
- *Sovereign cloud providers:* OVHcloud (FR), Scaleway (FR, Iliad), StackIT (DE, Schwarz Group), Post Telecom (LU). Scaleway, StackIT, and Post Telecom won early EU sovereign-cloud contracts.
- *Door:* data sovereignty (NOT operator sovereignty) plus the federation/interconnect pain of stitching multi-site GPU capacity. Healthy skepticism warranted: "sovereign AI" is also a marketing label, so verify the real sovereignty driver per account.

### MSP / Aggregators
Pan-European and national aggregators and managed-network providers. More carrier-fragmentation to aggregate across than a single-country US view.
- *Anchors:* Colt (managed services arm), GTT, Expereo, and national MSPs.
- *Door:* margin on resold connectivity plus differentiated managed routing.

### Enterprise (Multi-DC ICP)
Regulated multi-DC enterprises with in-house network engineering, in the four ICP verticals (financial services, healthcare systems, retail and distribution, outsourcing services). In Europe the regulatory driver is unusually strong: DORA hits financial entities directly, and the Data Act reaches industrial/operational data.
- *Door:* cost, risk, redundancy, and audit, paired with data sovereignty and a regulatory mandate (DORA for finance especially). Never operator-monetization framing.

## Regulators and public bodies (signal sources, see europe-signal-sources.md)

National telecom/spectrum regulators generate buildout, licensing, and open-access signals:
- **Germany:** Bundesnetzagentur (BNetzA). **UK:** Ofcom. **France:** ARCEP. **Italy:** AGCOM. **Spain:** CNMC. **Netherlands:** ACM. **Nordics:** PTS (SE), Nkom (NO), Traficom (FI). **EU level:** BEREC (telecom), the European Commission (DG CONNECT), EuroHPC JU (AI gigafactories).

## Starting segment-priority view (a hypothesis to pressure-test with Markus, not a mandate)

1. **Network operators / carriers and fiber operators first.** Warmest door for this GM, clearest operator-monetization plus sovereignty-service story, and the relationships compound across the European telco ecosystem.
2. **Sovereign-AI neoclouds and AI-colo second.** Fastest-growing and well-funded, strong data-sovereignty story, but a colder relationship start and a noisier "sovereignty" label to verify.
3. **Regulated enterprise (finance under DORA) as a focused third lane** where a named regulatory mandate makes the conversation concrete.
4. **Geography:** consider going deep in one or two countries (Germany plus one of UK / France / Nordics) before spreading thin across seven.

This ordering is a starting hypothesis grounded in the market structure and Markus's background. The live relationship map and any fresh signals should override it.

---

## Sources (load-bearing facts, verified June 2026)

- European DC market structure, FLAP-D capacity, power constraints, emerging markets, €176B investment: [JLL EMEA data centre report](https://www.jll.com/en-uk/insights/emea-data-centre-report); [Datacentre Review, "Europe at an inflection point" (Jan 2026)](https://datacentrereview.com/2026/01/europe-at-an-inflection-point-why-2026-will-redefine-the-emea-data-centre-landscape/); [Data Center Knowledge, "AI Demand and Policy Shifts Redraw Europe's Data Center Map for 2026"](https://www.datacenterknowledge.com/data-center-site-selection/ai-demand-and-policy-shifts-redraw-europe-s-data-center-map-for-2026); [Rabobank, emerging markets](https://www.rabobank.com/knowledge/d011517320-data-center-growth-in-europe-expands-to-emerging-markets).
- Sovereign-AI neoclouds (Nscale Series C, Nebius, Fluidstack, Sesterce): [Fortune, "Nscale has raised billions..." (Jun 2026)](https://fortune.com/2026/06/03/nscale-raised-billions-europe-ai-ambitions/); [The Cloud Today (Mar 13 2026)](https://cloudshot.io/blogs/the-cloud-today-mar-13-2026/); [aimultiple, Cloud GPU Providers](https://aimultiple.com/cloud-gpu-providers).
- EU AI gigafactories, InvestAI €20B, EuroHPC JU mandate, €180M sovereign-cloud contracts (Scaleway / StackIT / Post Telecom): [STL Partners, EU AI Gigafactory Initiative](https://stlpartners.com/articles/data-centres/eu-ai-gigafactory-initiative/); [EuroHPC JU mandate amendment (Jan 2026)](https://eurohpc-ju.europa.eu/eurohpc-jus-mandate-expanded-under-new-regulation-amendment-2026-01-20_en); [European Economics, InvestAI](https://www.europeaneconomics.com/en/investai-initiative-ai-gigafactories/).
- IX scale (DE-CIX): widely reported; verify current rankings before quoting a number in customer-facing copy.
