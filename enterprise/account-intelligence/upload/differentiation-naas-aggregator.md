# Differentiation Doctrine: MaiaEdge vs NaaS Fabrics vs Aggregators

**Single source of truth** for drawing the line against what MaiaEdge RESEMBLES (a NaaS platform, an aggregator, an exchange) in the prospect's own mental model. Built 2026-06-12 from verified product truth plus a sourced market deep-dive (evidence and URLs: `outputs/segment-refresh/2026-06-12-gap-report.md`). Consumers: `competitive-intel` skill, cold-email/linkedin-outreach/sdr-pipeline (cold-safe register only), account-brief, call-prep, segment cheatsheets.

**Register rules:**
- **COLD-SAFE** lines: no competitor names ever ("third-party fabric" / "aggregator's paper"), craft voice, concrete objects, no em dashes. Usable in E1/E2/E3 bodies and LinkedIn.
- **LIVE-CALL** lines: names allowed, per competitive-intel rules. Discovery, demos, proposals, objection handling.
- **ONE-LINER**: what a rep says without notes, live register.

---

## 1. The operator's mental map (what they think we are, and why)

When an operator hears "extend Ethernet beyond your footprint," they slot the pitch into one of four boxes they already know:

| Box | What lives there (their view) | Why we trigger it |
|---|---|---|
| **Off-net the hard way** | Type 2 buys, partner NNIs/ENNIs, E-Access (MEF 33), LOA/CFA, FOC dates, 30-90 day install intervals. Painful but theirs. | "Extension" sounds like another access supplier to quote from |
| **A fabric to join** | Megaport / Equinix Fabric / Console Connect class: a port, a portal, click-to-provision VXCs, instant global reach. Genuinely useful at edge points, structurally someone else's middle | "Instant paths anywhere" is exactly the fabric promise |
| **An aggregator** | Someone who marks up their wholesale routes, owns the end customer, and adds a support hop. A buyer to feed, or a competitor. Low-status word at a wholesale desk | "Reach through partners" sounds like aggregation |
| **An exchange (failed)** | The 2009-2012 carrier Ethernet exchange wave: CENX, Equinix CEE, Telx, Neutral Tandem. "The pure exchange model has been difficult to monetize" (trade press, 2011). CENX pivoted and sold for ~$40M; the survivors won by owning the port and the customer | "Interconnect operators with each other" is the exchange pitch verbatim |

The positional fact that breaks all four pattern-matches: **a fabric, an aggregator, and an exchange all sit BETWEEN the operator and the customer. MaiaEdge is deployed INSIDE the operator's network.** The operator racks the PBC on their own boundary, sells from their own portal, invoices on their own paper, and keeps the margin. Nothing sits in the middle.

## 2. The mechanical truth table (the spine - every claim verified)

| Dimension | DIY Type 2 + NNI | Join/resell a NaaS fabric | Sell through an aggregator | Deploy MaiaEdge |
|---|---|---|---|---|
| **Who owns the customer** | You | Split. Reselling keeps your paper, but in marketplace mode the buyer transacts in the fabric's portal and is billed for the connection by the fabric as connection initiator | The aggregator. You are an anonymous wholesale input | You. White-label portal, your invoice, your pricing |
| **The brand the customer sees** | Yours (plus the partner's paperwork) | Theirs, or theirs-inside-yours | Theirs | Yours; partner topology stays hidden (Q-in-Q isolation) |
| **The portal** | Your OSS + the partner's quote desk | Their portal / their API | Their quoting engine | Operator-branded PCE portal |
| **Margin shape** | Retail minus wholesale, quote by quote | You arbitrage above published port + VXC rates the buyer can also see; the platform captures the interconnection economics | Wholesale rate only; the buyer pays a 25-30% aggregation premium the aggregator keeps | Flat subscription per PBC (bandwidth tier x term); you set retail; shared-port cloud on-ramp runs ~47-75% gross margin at utilization |
| **SLA** | You hold it; enforcement over the Type 2 leg is contractual and mostly blind | Platform SLA to you; you re-wrap it | Aggregator fronts the customer SLA; you owe wholesale SLA to the aggregator | You hold it, with hop-by-hop telemetry as data-backed proof, including across Type 2 |
| **Visibility** | Dies at the ENNI; ticket ping-pong | Their telemetry, their granularity | Two hops of blindness (customer calls aggregator, aggregator calls carrier) | Hop-by-hop latency/jitter/loss across owned AND partner segments |
| **The installed asset** | NNI ports, tails, OSS glue | A port in their fabric; cancel and nothing remains | Nothing | PBCs on your network boundaries (title with MaiaEdge, OpEx subscription, full operational control) |
| **How the off-net leg is established** | Serviceability check, manual quote (5-7 days is the documented norm), order, FOC date, LOA/CFA, cross-connect, turn-up and test; 30-90+ days; published examples: 33 working-day standard Ethernet lead times, 90-day LOA expiry windows | Click-to-provision VXC where the fabric has reach; minutes | The aggregator sources from its carrier list on its own clock | Mutual-consent federation (seller approves, partner topology hidden); PCE computes the path across both networks in minutes; dynamic NNI can come up over plain DIA while a physical build waits |
| **Structural cost** | Capex + per-circuit wholesale; physical NNIs held "just in case" | Port MRC + per-VXC by distance/speed/term; usage-shaped opex forever | Permanent margin leak | Fixed per-PBC subscription; scales by box count, not by path count |

**MaiaEdge column sources:** PBC/PCE mechanics, white-label portal, multi-tenant isolation, federation consent flow, fabric-as-backend API integration, shared-port economics, and the commercial model are documented in `context/partner-assets/maiaedge-101.md`, `context/product/pbc-pce-datasheet.md`, `context/product/cloud-onramp-business-case.md`, `context/core/competitive-positioning.md` §3.4, and maiaedge.io. Mechanics NOT yet documented (inter-operator settlement, far-leg provisioning workflow detail, federated SLA recourse, pre-partner quotability) are listed in §7 - do not improvise them.

## 3. Concede what the fabrics do well (assume competence - they have all evaluated one)

Operators genuinely value fabrics at **edge points beyond footprint**: instant reach into markets with no NNI build, cloud on-ramps without a hyperscale presence, and a clean portal. An operator on a live call put it plainly: "we use our own network as much as possible, but when we get to edge points, that's where the fabrics have really added value." Do not argue against that experience. Two honest moves instead:

1. **MaiaEdge uses them underneath.** The PCE integrates Equinix Fabric and Megaport by API as backend for cloud on-ramps; multiple customers share one fabric port under the operator's brand. The line is "use them underneath, do not live inside them."
2. **The concession sets up the real line:** the fabric is excellent AS A SERVICE. The question is what compounds: every customer they put on the fabric's portal builds the fabric's relationship, and (since June 2026) the fabric's compute business. Every customer on their OWN fabric compounds theirs.

## 4. The sanctioned market catalyst (June 2026 - what it lets us truthfully say)

**The facts (verified, dual-currency):** On June 3, 2026 Megaport announced a fully underwritten **A$827.3M raise (about US$594M)** at A$14.30/share to build a globally distributed **AI inference cloud** across its 1,100+ connected data centers, alongside four AI compute contracts worth A$458.9M TCV commencing H1 2027 and an ~A$350M GPU pool. This followed the Latitude.sh bare-metal acquisition (~A$425M, closed Nov 2025), GPU instances live since Jan 2026, a storage product, and the CEO's own framing: "Megaport is evolving into a unified platform that gives customers instant access to scalable global infrastructure." Their stated rationale: "the economics shift from training to serving, and serving rewards proximity and distribution." Internally we say "close to $600M" (USD) or "an $830M Australian raise" - never bare "$800M," which conflates the currencies.

**What it truthfully licenses:**
- The fabric layer is **no longer a neutral middle**. The flagship interconnection platform now sells compute, storage, and network against the same enterprise and AI customers its operator partners serve. (Same pattern up-stack: Lumen is buying a multicloud NaaS control plane outright - Alkira, $475M, announced May 2026 - and extends on-demand services off-net into regional operators' territory; Equinix sells sovereignty as a premium Fabric tier as of May 2026.)
- For neoclouds: the network has visibly become part of the AI product (this is Campaign A's catalyst; calibrate to seat per the Tier 1 Inference correction).
- For operators: "every tenant or customer you send to a third-party fabric portal now discovers a compute competitor" is structurally true and dateable.

**What it does NOT license:** claiming Megaport is abandoning networking, failing, or raising defensively (their network ARR grew; the raise was oversubscribed and the stock rose). The catalyst is repositioning, not distress. Cold copy: anti-position only ("the third-party fabric layer is moving into compute"); names live in calls and this file.

## 5. Objection doctrine (three registers each)

### 5.1 "How is this not Megaport?" / "Aren't you just a Megaport?"

- **COLD-SAFE:** "A third-party fabric is a network you join: their port, their portal, their pricing page. This is infrastructure your team racks at your own boundaries, so the same instant paths come up on your portal, your rate card, your invoice."
- **LIVE-CALL:** "Megaport runs an excellent fabric, and we actually integrate with it by API for cloud on-ramps. The difference is positional. On Megaport you are a tenant: their port, their portal, their published pricing, and since June they also sell GPU compute to the same customers. With MaiaEdge you deploy PBCs on your own network, the PCE computes the paths, and everything the customer touches is yours. One colo VP told us: with a fabric 'you basically turn the customer over to them'; with this 'we get control over our destiny.' And a fiber customer's words: imagine having that capability BETWEEN providers who also have PBCs, over private fiber or plain DIA."
- **ONE-LINER:** "Megaport is a fabric you join. We are how you build your own, and we can even use theirs underneath for cloud reach."

### 5.2 "We already have NNI partners for off-net."

- **COLD-SAFE:** "Most operators do, and the partner side works. The cost sits in the workflow: a 5 to 7 day off-net quote, an FOC date set by the vendor's queue, and a circuit that goes dark to your tools the moment it turns up. The leg I work on is the same partner handoff coming up in minutes over transport you already buy, with hop-by-hop telemetry you keep."
- **LIVE-CALL:** "Keep the partners; this is not a replacement for the relationships. Today each partner is an ENNI project: LOA/CFA, FOC dates, 30 to 90 day intervals, and once it is a Type 2 you hold the SLA blind. With a PBC at each side, the same partner leg activates in minutes (over DIA if the physical build is still queued), encrypted end to end, and you can see every hop. The commercial agreement between you and the partner stays exactly as it was."
- **ONE-LINER:** "We do not replace your NNI partners. We make the partner leg turn up in minutes instead of quarters, and stop it going dark to your tools."

### 5.3 "So you're an aggregator?" / aggregator-desk misread ("send this to carrier relations/procurement")

- **COLD-SAFE:** "No supplier slot needed. An aggregator sits between you and the customer and keeps the spread. This is hardware on your boundaries and software computing your paths, so the customer, the invoice, and the margin never leave your house."
- **LIVE-CALL:** "An aggregator resells your routes on their paper: they own the end customer, you get the wholesale rate, and the buyer pays a 25 to 30 percent premium for the privilege. We are the opposite end of the table. You deploy MaiaEdge inside your network and YOU become the one selling reach, under your brand. We are not asking to be supplier number 401 on a line card; this is a business-model conversation, not a sourcing one."
- **ONE-LINER:** "An aggregator sits between you and your customer. We sit inside your network. Opposite ends of the table."

### 5.4 "Whose network does the extension ride?"

- **COLD-SAFE:** "Yours, or a partner operator's you choose, with both sides agreeing first. Each leg rides transport somebody at the table owns or already buys, fiber, wave, or plain DIA, and never a third network in the middle."
- **LIVE-CALL:** "Three options, all yours to pick. One: your own transport, anywhere you have fiber, waves, or DIA. Two: a partner operator's network, by mutual consent - the seller approves the federation, their topology stays hidden, and your customer sees only your service. Three: for cloud on-ramps, Equinix Fabric or Megaport as API backend behind your brand, on a port multiple customers share. What never happens: your traffic riding a network MaiaEdge operates, because we do not operate one. We sell the infrastructure; the operators own the paths."
- **ONE-LINER:** "Your network or a consenting partner's. We do not have a network, and that is the point."

### 5.5 "Why not just join a fabric?"

- **COLD-SAFE:** "Joining works on day one, and the bill and the relationship both compound on someone else's side. Every customer who learns their portal is a customer you re-win later. The version that compounds for you is the one where the port, the portal, and the rate card are yours."
- **LIVE-CALL:** "If you only need reach and never want connectivity as a product, joining a fabric is rational, and we will say so. The trade is structural: port fees plus per-circuit charges forever, published pricing your buyers can see around you, the customer transacting in their marketplace, and a platform that now sells compute up the same stack. Joining also leaves nothing behind if you exit. Deploying leaves you with a fabric of your own that every new customer makes more valuable. And the build-it-yourself alternative just got priced: a Tier 1 paid $475M for a fabric control plane this May, before integration."
- **ONE-LINER:** "Join one and you rent reach forever. Deploy this and you own the thing you sell."

### 5.6 "What do you cost vs a port on a fabric?"

- **COLD-SAFE (cold copy never quotes prices):** "The cost shapes differ more than the totals. A fabric bills a port plus every circuit, forever, priced by distance and speed. This is a flat subscription on hardware at your boundary, so the hundredth path costs what the first one did."
- **LIVE-CALL:** "Structurally: a fabric is port MRC plus per-VXC charges that scale with usage and distance, on their published rate card. MaiaEdge is a flat per-PBC subscription by bandwidth tier and term - the 100G unit lands around nineteen hundred dollars a month on a multi-year term - and it is multi-tenant, so you sell as many customer paths across it as you can win, at prices you set. On cloud on-ramps the shared-port model breaks even around four customers on a 10G port and runs toward 75 percent gross margin at utilization, because the port cost is fixed and every added customer is margin."
- **ONE-LINER:** "A fabric meters you per path. We charge for the box; the paths are your margin."

### 5.7 "Carrier Ethernet exchanges failed before. Why does this work now?"

- **LIVE-CALL (this objection only surfaces live):** "Right, and the history is instructive: CENX, the Equinix Ethernet Exchange, Telx, Neutral Tandem, all 2009 to 2012, and the pure exchange model never monetized. They failed because a neutral broker still could not remove the physical NNI or the bilateral commercial agreement, and carriers would not commoditize routes through a middleman. We are not a broker and there is no middleman: the infrastructure sits in each operator's network, the commercial agreements stay bilateral, and what got removed is the 90-day physical build and the blindness, not the operator's control. The survivors of that era won by owning the port and the customer. This puts that ownership with you."
- **ONE-LINER:** "Exchanges failed because the middleman stayed. Here there is no middleman to fail."

### 5.8 "We could build this ourselves."

- **LIVE-CALL (updates the existing internal-build card with the 2026 number):** "You could, and the market just priced the shortcut: Lumen paid $475M in May for Alkira, a fabric control plane, before integration cost. The in-house version is 18 to 24 months of carrier-grade SDN work, and at the end you still face the part you cannot build alone: partner interconnection requires the partner to run the same thing. That installed base is what you are actually buying."
- **ONE-LINER:** "A Tier 1 just paid $475M to buy this capability. Your subscription is not that."

## 6. Where they win / where we win (honest routing)

**A fabric is the right answer when:** the prospect is an enterprise (not a service provider) wanting reach without ownership; the operator has no intent to sell connectivity as a product; they need 200 cities tomorrow with zero deployment. Say so, and stay credible for the rest of the call.

**An aggregator is the right answer when:** the buyer wants one throat to choke across many carriers and accepts the premium. (That buyer is not our ICP; the OPERATOR feeding that aggregator is.)

**MaiaEdge wins when:** the operator wants to own the customer, the margin, and the asset; is losing interconnection revenue or tenants to a third-party fabric; wants extension/off-net legs on their own clock with their own visibility; or operates where the 2026 catalyst bites (the fabric they resell now competes with them).

## 7. Claims to avoid until engineering confirms (the OPEN QUESTIONS guardrail)

These are the mechanics a confident rep will be tempted to improvise. Full list with detail: gap report §7. Until Kyle/Abilash confirm, do NOT claim:

1. How inter-operator **settlement** works on a federated path (who invoices whom, whether the platform meters/clears anything).
2. Who **provisions the far leg** after federation consent (A's PCE programming B's PBCs vs per-path approval).
3. Any **inter-operator SLA framework** (A's recourse against B's segment). "Data-backed SLA proof" via telemetry is claimable; contractual recourse is not.
4. That an operator can **quote a destination with no partner there yet** (serviceability across the federation is described in future tense in our materials).
5. Who holds the **fabric account and port fees** in backend cloud on-ramp models, and partner cost pass-through in Model 3.
6. Any **per-path or marketplace transaction fee** (or its absence) beyond the flat subscription.
7. The depth of **LSO Sonata conformance** (which APIs, certified vs aligned). Safe phrasing: "standards-aligned with Mplify LSO Sonata and TM Forum ODA."
8. What a **partner sees in telemetry** on transit paths, and what happens to live paths if federation consent is revoked.
9. **Oversubscribing fabric ports** as a written claim (spoken on live calls by leadership; do not put in writing until sanctioned - it implies a best-effort tier and can undercut the determinism story).

## 8. Quick reference: the vocabulary that keeps us out of the wrong box

- Say: infrastructure you deploy, your boundary, your portal, your rate card, your invoice, partner leg by consent, paths your team turns up, the box and the control plane.
- Never in cold: platform, join our network, our fabric, coverage map, marketplace (as the lead), on-demand network (as the lead), any competitor name, "NaaS" as a self-description (the category is fatigued and we are not in it: carrier infrastructure only).
- The category answer to "what are you," every register: **carrier infrastructure** (for federated private networking, where the noun phrase is allowed per the messaging rules).
