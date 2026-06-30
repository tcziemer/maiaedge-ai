# Sovereignty Positioning for Europe (GM Europe reference)

> How to use sovereign routing as the European wedge, by segment, mapped to the regulatory drivers that actually move buyers. Builds on `context/marketing/sovereign-routing-explainer.md` (what sovereign routing is and how MaiaEdge does it). This file is the how-to-sell-it-in-Europe layer.
> Regulatory facts verified June 2026 (foot of file).

---

## Why this is the European wedge

Sovereign routing means the network does what you tell it to do, not what BGP decides: deterministic, policy-driven paths that respect jurisdiction, carrier preference, and security, enforced even across federated partner networks. In the US that is a differentiator. In Europe it is increasingly a procurement requirement, because a stack of regulations now makes "where does the traffic flow and where does the data rest" a question buyers must answer with evidence, not intent.

That is the whole game in Europe: turn an invisible, deferred risk into a dated, named mandate the buyer already has to meet, and show that MaiaEdge is how an operator sells the answer or how an enterprise satisfies it.

## The regulatory drivers (the dated, concrete hooks)

Use these as the forward-state reason a buyer must act. Each is real and in force or imminent.

| Driver | In force | Who it hits | What it forces (the hook) |
|---|---|---|---|
| **GDPR** | 2018 (baseline) | Anyone handling EU personal data | Data residency and lawful-transfer pressure. The floor, not the story. |
| **EU Data Act** | Enforceable Sept 2025 | Anyone with connected-device / industrial / operational data | Extends sovereignty beyond personal data to machine and operational data. Widens the set of data whose path and location matter. |
| **NIS2** | Enforceable Oct 2024; first penalties 2026 | Essential and important entities (broad: energy, transport, telecom, health, digital infra and more) | Cybersecurity and supply-chain accountability. Fines up to €10M or 2% of global turnover. Makes provable control of network paths a board-level item. |
| **DORA** | Applicable Jan 2025; first real enforcement cycle 2026 | Financial entities and their critical ICT providers | Full audit rights and contractual control over data, concentration-risk management, and demonstrably sovereign incident response and recovery. The sharpest single hook for the finance vertical. |
| **EU AI Act** | Full application Aug 2026 | High-risk AI systems and their infrastructure | Data-governance obligations that flow into where and how AI data and traffic are handled. The hook for the sovereign-AI buildout. |

## Positioning by segment (pick the door that matches the buyer)

### Operators: carriers, colo, fiber (the primary European play)
An operator's network is a profit center, so sovereign routing is a product they can sell, not a cost they must bear. The pitch is monetization: package deterministic, policy-routed, jurisdiction-aware paths as a premium, high-margin service for their own regulated customers (defense, government, finance) who increasingly demand it. This is the Telstra InfraCo story from the explainer, translated to a European carrier or fiber operator that wants a differentiated service to sell into NIS2- and DORA-exposed accounts. Lead with new revenue and differentiation, not compliance-for-themselves.

### Neoclouds and sovereign AI
Drop operator-sovereignty framing here. Neoclouds ARE the customer, so lead with **data sovereignty** plus the federation and interconnect pain of stitching GPU capacity across multiple sites and jurisdictions. The hook: their regulated and public-sector customers (the entire reason "sovereign AI" exists as a category) need provable, policy-controlled data paths, and the AI Act is making that explicit. Be skeptical of the label: "sovereign AI" is also marketing, so verify the real driver per account before you lead with it.

### Enterprise (Multi-DC ICP)
An enterprise network is a cost center, so never use operator-monetization framing. Lead with cost, risk, redundancy, and audit, paired with data sovereignty and a named mandate. For the financial-services vertical, DORA is the concrete hook: full audit rights, control over data, demonstrably sovereign recovery. For others, the Data Act and NIS2 raise the same need to prove control of paths and data.

## The discipline (read every line as the buyer)

European infrastructure buyers have usually thought hard about sovereignty already, often before it was fashionable. So:

- **Assume competence.** Never imply the buyer is currently non-compliant or has not solved this. That reads as "you are doing it wrong" and ends the conversation. Frame sovereignty as a service they can now offer, or a forward mandate they are preparing for, never as a verdict on their current setup.
- **Earn the sovereignty angle per account.** Do not lead with sovereignty just because it is the loud European narrative. Lead with it when a real, dated regulatory driver applies to that specific buyer, or when they sell to customers who carry one. Otherwise lead with the segment's normal pain (federation, handoff, provisioning speed) and let sovereignty support.
- **The strongest skeptic's counter, and the answer.** A sharp European operator will say "sovereign routing is a buzzword, and we already do path control with our own MPLS and policy." The honest answer is about determinism across boundaries: policy that travels with the path through federated partner networks, computed centrally rather than re-stitched by hand at every handoff. If you cannot articulate why that is different from what they already run, you have not earned the angle yet.
- **No credibility anchors in cold.** The exits and prior companies are fair game in live calls and proposals, never in cold email or LinkedIn.

## Discovery hooks (forward-state, not accusatory)

- "As more of your customers fall under DORA, how are you thinking about offering provable data-path control as a service rather than a one-off project?"
- "When you federate with a partner network, how much control over routing policy survives the handoff today?"
- "As you scale GPU capacity across sites, where does the responsibility for provable data paths sit for your regulated customers?"

---

## Sources (regulatory facts, verified June 2026)

- EU Data Act (Sept 2025), NIS2 (Oct 2024 + 2026 penalties, €10M / 2% turnover), DORA (Jan 2025 + 2026 enforcement), EU AI Act (full application Aug 2026): [ComplianceHub, DORA + NIS2 2026 enforcement](https://compliancehub.wiki/dora-nis2-2026-enforcement-eu-financial-cyber-resilience-compliance/); [SoftwareOne, Digital sovereignty 2026 action plan](https://www.softwareone.com/en/blog/articles/2026/01/12/your-2026-digital-sovereignty-guide); [The Data Governor, Data Sovereignty under GDPR / Data Act / AI Act](https://thedatagovernor.com/data-sovereignty/); [Kensai, March 2026 security regulations](https://kensai.app/blog/security-regulations-news-nis2-dora-ai-act.html).
- Sovereign routing mechanics and the operator-monetization story: `context/marketing/sovereign-routing-explainer.md`.
