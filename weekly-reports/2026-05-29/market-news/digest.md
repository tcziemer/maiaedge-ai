# MaiaEdge Market News - Week of 2026-05-22 to 2026-05-29

Hey Cooper - here's what moved across our 6 ICPs this week.

## Cross-ICP Themes

- **The neocloud capital market is bifurcating.** Data center landlords are now underwriting GPU tenants on credit strength and end-customer visibility, not just signed leases, and deals are stalling over it. Yet NVIDIA-blessed names keep getting funded: Groq lined up roughly $650M for a neocloud spin-out and a Roundhill Neocloud ETF filed May 22. Capital is flowing to the NVIDIA-backed cohort while everyone else hits a credit wall.
- **Carriers and hyperscalers are buying the cloud-connectivity control plane.** Lumen's $475M Alkira deal and the AWS Interconnect multicloud GA land the same bet: own the software layer that programs cross-cloud paths. Operators without their own answer get disintermediated at exactly the layer where margin is moving.
- **Deterministic networking went from our pitch to an industry standard.** The MRC protocol (OpenAI, Microsoft, NVIDIA, AMD, Intel, Broadcom) is built on SRv6 for deterministic path placement across 100k+ GPU backends. The market now agrees that best-effort breaks AI. That is a tailwind under every segment below.

## Colocation

**FERC orders PJM to craft large-load data center colocation rules** - [Utility Dive](https://www.utilitydive.com/news/ferc-pjm-colocation-data-center/808368/)
FERC directed PJM to develop rules for co-located data centers after Vistra, Constellation and a data center trade group attacked the grid operator's initial proposal. Power-behind-the-meter economics for AI campuses are now a federal regulatory fight.
> MaiaEdge angle: Power rules decide where AI capacity lands, and every newly greenlit campus is a fresh interconnection build. The colos that win those tenants still hand cloud on-ramps to a third-party fabric, and that attach-rate gap is the one we close.

**Build wave keeps cresting - 540MW Hale County TX campus, EdgeCore $1.5B Northern Virginia financing, Equinix $190M Kuala Lumpur** - [Data Center Knowledge](https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-may-2026)
May logged a 540MW six-building Texas campus, $1.5B single-tenant hyperscale financing in Northern Virginia, and Equinix's fourth Malaysia facility. Capacity is being committed years ahead of demand.
> MaiaEdge angle: Every one of these is a meet-me room that will eventually need instant, deterministic interconnection across sites. Selling space and power is the easy part. The connectivity layer is where they are still a landlord.

## Fiber

**NTIA approves final BEAD proposals in 18 states** - [DCD](https://www.datacenterdynamics.com/en/news/ntia-approves-final-bead-proposals-in-18-states/)
NTIA cleared final BEAD proposals in 18 states, moving them from paperwork to funded construction. 53 of 56 states and territories have now submitted final proposals, and roughly 65% of locations are fiber.
> MaiaEdge angle: Funded awards mean operators are about to trench against committed revenue, and every new market multiplies cross-carrier NNIs. Operators with portal or NaaS gaps will be cutting POs against this build. Reach extension is the lead, not provisioning speed.

**Consolidation continues - Zayo closes Crown Castle fiber** - [Broadband Breakfast](https://broadbandbreakfast.com/zayo-completes-crown-castle-fiber-acquisition/)
Zayo completed its acquisition of Crown Castle's fiber business, adding roughly 90,000 route miles and 40,000 on-net enterprise locations.
> MaiaEdge angle: Roll-ups like this inherit fiber islands - multiple OSS stacks and mismatched provisioning across the acquired plant. The 6 to 12 month post-close integration window is exactly when an automation-and-reach layer gets evaluated.

## Network Operator

**Lumen to acquire Alkira for $475M to build the cloud-connectivity control plane** - [Fierce Network](https://www.fierce-network.com/cloud/lumen-expands-its-reach-alkira-acquisition)
Lumen is buying multi-cloud networking firm Alkira for $475M all-cash, pairing Alkira's cloud-native control plane with Lumen's fiber to extend reach beyond its own North American footprint via partner networks. (Announced May 5; freshest material in a thin week for the segment.)
> MaiaEdge angle: Lumen just validated the thesis out loud - the value is the software that programs paths across networks you do not own. That is carrier infrastructure, and most Tier 2/3 operators cannot buy a $475M control plane. They need one they can stand up.

**MRC protocol standardizes SRv6 deterministic paths for AI backends** - [Cisco Blogs](https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers)
OpenAI, Microsoft, NVIDIA, AMD, Intel and Broadcom shipped MRC, built on SRv6, for deterministic path placement and full bisection bandwidth across 100k+ GPU fabrics.
> MaiaEdge angle: The hyperscalers solved deterministic paths inside the building. The unsolved problem is deterministic paths between buildings and across carrier boundaries, which is precisely where on-net stops and off-net pain begins.

## NeoCloud

**Groq lines up roughly $650M for a neocloud spin-out after $20B NVIDIA deal** - [crypto.news](https://crypto.news/groq-lines-up-650m-for-neocloud-spin-out-after-20b-nvidia-deal/)
Groq is raising about $650M from existing investors for "Groq2," pivoting from chips to building inference-optimized neoclouds, after NVIDIA agreed to acquire its inference tech and hire much of its leadership.
> MaiaEdge angle: Another inference-first neocloud that will scale facilities fast and discover the middle mile is the uncontrolled variable. Inference does not tolerate jitter, and the connectivity gap shows up as latency variance a two-person network team cannot diagnose.

**Neocloud deals stall over credit risk as GPU-backed debt tops $20B** - [Data Center Knowledge](https://www.datacenterknowledge.com/cloud/neocloud-storm-gathers-as-data-center-deals-stall-over-credit-risk)
Landlords are now underwriting neoclouds on balance-sheet durability and end-customer visibility, not just signed leases. GPU collateral loses 40 to 60% of value in three years, concentrating risk in a few hyperscaler backstops.
> MaiaEdge angle: Credit-constrained neoclouds cannot afford recompute-tax outages or stranded capacity. Deterministic, observable connectivity between facilities is utilization insurance, and it is the cheapest lever they have to protect the GPU economics lenders are now scrutinizing.

**Capital keeps flowing to NVIDIA-blessed names - Roundhill Neocloud ETF files, Aschenbrenner fund buys in** - [Crypto Briefing](https://cryptobriefing.com/roundhill-neocloud-etf-gpu-as-a-service/) / [Motley Fool](https://www.fool.com/investing/2026/05/28/leopold-aschenbrenner-s-situational-awareness-fund-just-bought-this-nvidia-backed-neocloud-stock/)
A Roundhill Neocloud ETF filed May 22 and Leopold Aschenbrenner's Situational Awareness Fund bought a Nvidia-backed neocloud, underscoring the split between funded and credit-starved operators.
> MaiaEdge angle: The funded cohort is racing to stand up sites, and speed-to-onboard a new facility is their constraint. Every site today is a multi-week connectivity project. That is the wedge.

## MSP / Aggregator

**Tech-advisor M&A keeps accelerating as PE rolls up the channel** - [Channel Futures](https://www.channelfutures.com/mergers-acquisitions/tech-advisor-m-a-is-picking-up-the-pace)
PE capital continues consolidating technology advisors and TSDs (Carlyle and Charlesbank into Bridgepointe in April, ongoing master-agency mergers), reshaping who controls the carrier line-card.
> MaiaEdge angle: As advisors consolidate, the winners differentiate on capability, not just carrier access. An aggregator that can offer deterministic, automated connectivity under its own brand stops being a reseller of the same upstream everyone else has.

## Enterprise (Multi-DC ICP)

**JPMorgan reclassifies AI as core infrastructure - $2B per year non-negotiable** - [DCD](https://www.datacenterdynamics.com/en/news/jpmorgan-global-data-center-and-ai-infra-spend-to-hit-5-trillion-demand-for-compute-remains-astronomical/)
JPMorgan put its roughly $2B annual AI budget inside its $19.8B 2026 tech budget alongside data centers and payment systems, treating compute as core infrastructure on a 5 to 10 year horizon.
> MaiaEdge angle: Financial Services buyers want to control their own destiny for business and regulatory reasons. AI traffic is pulling data between DCs in directions they did not design for, and the diverse-path, physically-verified connectivity their examiners demand is not something a third-party fabric proves for them.

**WhiteFiber signs greater than $160M five-year AI compute deal for an investment-grade customer** - [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0002042022/000121390026060135/ea029187601ex99-1.htm)
WhiteFiber will deliver NVIDIA GPU infrastructure to an investment-grade tech customer in the Paris region, with service starting July 2026.
> MaiaEdge angle: Investment-grade enterprises are now buying dedicated GPU capacity off-premises. The connectivity back to their own DCs and clouds has to be deterministic and sovereign by design. Every new GPU site is another six-month networking project unless the reach layer is already there.

## Exec Moves This Week

- Martin Dowling named CTO, Altibox Carrier (Network Operator) - 12 years at Microsoft, most recently leading network acquisition in Europe. [Fierce Network](https://www.fierce-network.com/broadband/2026-career-moves)
- Kurt Schaubach named SVP and CTO, CTIA (industry body; ex-CTO Federated Wireless). [Fierce Network](https://www.fierce-network.com/broadband/2026-career-moves)
