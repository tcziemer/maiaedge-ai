# LMaaS Strategy Analysis: MaiaEdge-Owned PBC Deployments in Colocation Facilities

**Date:** March 25, 2026
**Prepared for:** Timothy Ziemer, CRO & Co-Founder
**Classification:** Confidential / Internal Strategy

---

## Executive Summary

The proposal is straightforward: MaiaEdge deploys its own PBCs in colocation facilities across key metros. One cross-connect from any fiber operator in that metro creates an E-Line back to the MaiaEdge node. This accelerates federation buildout by removing the dependency on fiber operators who, despite being open-minded, are too consumed by day-to-day operations to move at the pace MaiaEdge needs. The strategy borrows from Google's early playbook: pay fiber operator partners generously so their sales teams and indirect channels actively push MaiaEdge, creating a Twilio-like platform dynamic rather than a service provider identity.

This is a potentially transformative acceleration move. It is also the single highest-risk strategic pivot MaiaEdge could make, because it touches the foundational narrative that has differentiated MaiaEdge from every competitor: "We help you build your own fabric. We're not the fabric."

This analysis evaluates the strategy across six dimensions: strategic alignment, channel conflict, competitive perception, federation dynamics, valuation implications, and operational complexity. It concludes with specific recommendations for how to capture the acceleration benefits while managing the risks.

---

## 1. The Strategic Logic: Why This Makes Sense

The current go-to-market depends on fiber operators deploying PBCs on their own networks. The marketplace seeding strategy lays out a phased geographic expansion starting with Ashburn, moving to SV/LA, then secondary hubs. The problem you have identified is real and well-documented in your own context:

**Fiber operators are slow.** They have 50-2,000 employees, $50M-$1B in revenue, and are running fragmented networks across 2-10 state footprints. Their competitive reality is manual provisioning, 60-90 day NNIs, and Type 2 visibility black holes. They know they need to change. They are open-minded about MaiaEdge. But they are bogged down in operational firefighting. Every day they delay is another day the federation marketplace lacks inventory.

**The marketplace needs inventory before it has value.** Your own iPhone analogy applies: the App Store needed apps before users showed up. The federation flywheel (Enhance, Multiply, Compound) cannot spin without PBCs deployed at interconnection points. If MaiaEdge waits for each fiber operator to go through their own internal procurement, budget approval, and deployment cycle, the marketplace seeding timeline stretches from months to years.

**Deploying your own PBCs in colos solves the cold-start problem.** One PBC in an Ashburn meet-me room, with cross-connects available, means any fiber operator in that metro can light up an E-Line and be federated in days, not months. It removes the capital risk from the fiber operator's decision. It makes the first federation experience frictionless. It is the logical extension of the "free/heavily subsidized PBC" model you already planned for Atlantec, except MaiaEdge owns and operates the node directly.

**The Google analogy is apt.** Google paid content providers, browser partners, and OEMs handsomely to distribute Chrome and Search. The goal was distribution velocity, not margin on each individual partnership. If MaiaEdge pays fiber operators well enough that their sales teams and indirect channels actively recommend MaiaEdge connectivity, the federation flywheel accelerates dramatically. This is platform economics, not carrier economics.

---

## 2. The Core Tension: Platform vs. Carrier

Everything in MaiaEdge's positioning, competitive battle cards, and messaging framework is built on a single foundational distinction: **MaiaEdge is carrier infrastructure, not a carrier.** The entire competitive positioning against Megaport, Equinix Fabric, Lumen PCF, and every NaaS platform rests on this:

- "We're not a SaaS fabric you join. We help you build your own."
- "Own the on-ramp. Equinix and Megaport become your backend infrastructure."
- "Lumen builds their empire. MaiaEdge empowers you to build yours."

The moment MaiaEdge deploys its own PBCs in colocation facilities and offers connectivity to fiber operators via cross-connect, the company is operating infrastructure. It is providing a service. The positioning distinction between MaiaEdge and Megaport narrows considerably in the eyes of any carrier evaluating whether MaiaEdge is a partner or a competitor.

This is not a hypothetical concern. Your competitive positioning document explicitly acknowledges that Megaport is the primary competitor for colocation operators, and that carriers view NaaS platforms with suspicion precisely because "they own the fabric AND your customer." If MaiaEdge owns PBCs in colos, it owns fabric. The question becomes: does it also own (or intermediate) the customer?

---

## 3. Channel Conflict: Detailed Risk Assessment

### 3.1 Immediate Risk: Fiber Operators Who Are Already Prospects

You currently have fiber operators in your pipeline who are evaluating deploying PBCs on their own networks. If MaiaEdge simultaneously deploys its own PBCs in the same metros, these operators face a new question: "Why would I spend $22K-$30K/year per PBC when MaiaEdge already has a node in my metro that I can cross-connect to for the cost of an E-Line?"

This creates two problems. First, it cannbalizes your own hardware subscription revenue. A fiber operator who would have deployed 3-5 PBCs across their footprint now deploys zero and instead buys cross-connects to MaiaEdge's colo node. Second, it changes the power dynamic. The fiber operator becomes a customer of MaiaEdge's infrastructure rather than a sovereign operator of their own MaiaEdge-powered fabric. This is exactly the dynamic you warn about with Megaport.

**Mitigation:** Position the colo node as a temporary on-ramp, not a permanent architecture. The colo PBC is the "starter" that gets the fiber operator into the federation immediately, with a clear upgrade path to deploying their own PBCs. Design the commercial model so that owning your own PBC is always more economically attractive at scale than paying for cross-connects to MaiaEdge's node.

### 3.2 Medium-Term Risk: "MaiaEdge Is Competing With Me"

Fiber operators talk to each other. Regional carrier communities are small. When Operator A in Dallas learns that MaiaEdge has its own PBC in the Equinix DA1 meet-me room, and Operator B in Dallas is cross-connecting to it, the narrative spreads: "MaiaEdge is building their own network." This is the Megaport perception you explicitly want to avoid.

The risk compounds in metros where MaiaEdge's colo node becomes the de facto interconnection point. If 5-10 fiber operators in a metro are all cross-connecting to MaiaEdge's PBC, MaiaEdge has become a hub. Functionally, that is a fabric. The distinction between "we provide carrier infrastructure" and "we are a carrier" becomes semantic rather than substantive.

**Mitigation:** Establish an explicit "graduation" program. Once a metro reaches a threshold of federated operators (e.g., 3-5), MaiaEdge transitions the colo node to a local operator partner and exits. This demonstrates commitment to the "infrastructure, not carrier" identity. It also creates urgency for operators to deploy their own PBCs before the hub transitions away.

### 3.3 Long-Term Risk: Structural Channel Conflict at Scale

If MaiaEdge deploys its own PBCs in 10-20 metros, the company has built a national network of interconnection nodes. Even if the intent is to accelerate federation, the structural reality is that MaiaEdge has become a national interconnection provider. This creates permanent tension with every carrier partner:

- Carriers will negotiate harder, knowing MaiaEdge has a fallback option.
- Carriers will question MaiaEdge's neutrality in routing and federation decisions.
- Carriers will view MaiaEdge's sales team as a competitor when calling on the same enterprise accounts.
- Strategic investors or acquirers will value MaiaEdge as a carrier/NaaS company rather than a platform/infrastructure company.

**Mitigation:** Cap the number of MaiaEdge-owned nodes. Define a hard policy: MaiaEdge owns PBCs only in Tier 1 hub locations (Ashburn, SV, LA, Chicago, Dallas, Seattle) and only until a local partner assumes the hub role. Never expand MaiaEdge-owned nodes beyond the initial seeding metros.

---

## 4. Competitive Perception: The Megaport Problem

Your competitive positioning document is clear: some carriers already view Megaport with suspicion. Megaport owns the fabric, owns the customer relationship, and captures the interconnection margin. MaiaEdge's entire value proposition is "don't let that happen to you."

If MaiaEdge deploys its own infrastructure in colos, competitors will exploit this immediately:

**Megaport's counter-narrative:** "MaiaEdge says they're different from us, but they're deploying their own PBCs in the same facilities we're in. They're building a competing fabric. At least with Megaport, you know what you're getting."

**Lumen's counter-narrative:** "MaiaEdge claims to empower operators, but they're deploying their own infrastructure. They're a startup version of us."

**Internal build advocates:** "If MaiaEdge is going to be in the colo anyway, and I have to cross-connect to them, how is this different from connecting to Megaport? At least with my own build, I don't depend on anyone."

These narratives are predictable and will surface in competitive deals. Every sales conversation where a prospect asks "aren't you competing with me?" costs time, trust, and deal velocity.

**Mitigation:** The messaging must be airtight before the first colo node goes live. Develop a specific talk track for "MaiaEdge-owned vs. partner-owned PBCs" that clearly articulates:
1. Why MaiaEdge is doing this (acceleration, not empire-building)
2. What the exit plan is (partner graduation)
3. How the economics are structured to favor operator-owned PBCs
4. What commitments MaiaEdge makes about not selling directly to enterprises from these nodes

---

## 5. Federation Dynamics: How Self-Deployment Complicates Multi-Carrier Sales

The federation flywheel is MaiaEdge's most defensible competitive advantage. It is the one thing competitors genuinely cannot replicate. Federation requires mutual consent, interoperability, and trust between operators. Self-deployment introduces asymmetry into this trust equation.

### 5.1 Trust Asymmetry

When two fiber operators federate through MaiaEdge, they are peers. Both deployed PBCs. Both contribute infrastructure. Both benefit from reach. The relationship is symmetric.

When a fiber operator federates by cross-connecting to a MaiaEdge-owned node, the relationship is asymmetric. MaiaEdge is both the platform provider and the infrastructure operator at the other end of the connection. The fiber operator must trust that MaiaEdge will not use its hub position to extract unfair economics, favor certain partners, or ultimately disintermediate the operator's customer relationships.

This trust concern is not theoretical. It is exactly what happened with Megaport and Equinix Fabric. Both started as neutral interconnection platforms. Both gradually shifted toward capturing customer relationships and margin. Carriers learned that lesson, and many are now specifically looking for alternatives that don't repeat it.

### 5.2 Selling Federation to New Carriers

When Tim Lieto or Ken Cunningham walks into a fiber operator's office and says "deploy MaiaEdge, federate with partners, own your fabric," the pitch is clean. The operator is the customer. MaiaEdge is the vendor. The operator keeps sovereignty.

If MaiaEdge owns nodes in key metros, the pitch changes: "Deploy MaiaEdge on your network, OR cross-connect to our node, OR do both." The simplicity is gone. The operator now has to evaluate MaiaEdge as both a vendor and a potential competitor. Deal cycles will lengthen.

Worse, the most sophisticated operators (the ones you most want in the federation) will be the first to identify the conflict. Smaller operators may not notice or care. But the Arvigs, the Atlantecs, and the regional CLECs with experienced leadership teams will ask hard questions.

### 5.3 Impact on International Expansion

International markets (IENTC in Mexico, Ecotel in Germany, CMC Networks in Europe) are critical for the federation vision. These operators are evaluating MaiaEdge specifically because it empowers them to build their own fabric without depending on US-based NaaS platforms. If MaiaEdge is simultaneously building its own node network in the US, international operators may question whether the same dynamic will eventually reach their markets.

---

## 6. Valuation and Identity: Twilio vs. Service Provider

The aspiration to be valued like Twilio rather than a service provider is strategically sound. Twilio trades at 5-8x revenue (platform multiples). Service providers trade at 1-3x revenue (carrier multiples). The difference is hundreds of millions in enterprise value at scale.

Twilio's key characteristics that command platform multiples:

- **API-first:** Developers integrate Twilio; Twilio doesn't operate the telecom infrastructure.
- **Usage-based pricing:** Revenue scales with customer success, not infrastructure deployed.
- **Network effects:** More developers using Twilio makes it more valuable for all developers.
- **Vendor-neutral:** Twilio works across carriers. It doesn't compete with them.

MaiaEdge today has strong platform characteristics: PBC/PCE architecture, API integrations, federation network effects, subscription pricing. Deploying owned infrastructure in colos moves MaiaEdge along the spectrum toward a carrier identity. Investors and acquirers will notice.

The question is whether the acceleration in federation buildout is worth the valuation haircut. If MaiaEdge-owned nodes are clearly temporary, clearly capped, and clearly designed to be transitioned to partners, the platform narrative can be preserved. If the owned nodes become a permanent part of the business (because they generate revenue and the company becomes dependent on that revenue), the Twilio aspiration becomes harder to sustain.

**Recommendation:** If you proceed, explicitly exclude MaiaEdge-owned node revenue from the "platform" revenue line in investor reporting. Track it separately as "seeding infrastructure" with a clear sunset timeline. This preserves the platform narrative even while operating temporary infrastructure.

---

## 7. The Google Playbook: Paying Partners Well

The instinct to pay fiber operator partners generously is correct and potentially the most important part of this strategy. If fiber operators' sales teams and indirect channels are actively pushing MaiaEdge, the federation builds itself. The question is how to structure these economics.

### 7.1 What "Paying Well" Looks Like

Google paid browser OEMs and mobile carriers to pre-install Chrome and set Google as default search. The economics were simple: Google paid a share of search revenue generated by users acquired through those channels. The payment was ongoing, not one-time. Partners were incentivized to keep distributing.

For MaiaEdge, the equivalent structure could be:

- **Revenue share on federated services:** When a fiber operator's customer uses a path that touches MaiaEdge's colo node, the fiber operator receives a percentage of the MaiaEdge subscription revenue associated with that path.
- **Sales incentive payments:** Direct SPIFs to fiber operator sales reps who close deals that result in cross-connects to MaiaEdge nodes.
- **Indirect channel commissions:** Pay fiber operators' reseller networks for referrals that result in MaiaEdge deployments (either cross-connects or full PBC sales).
- **Marketing development funds:** Co-fund marketing campaigns with fiber operator partners, MaiaEdge's brand alongside the operator's brand.

### 7.2 The Risk of Paying Too Well

If the economics are too generous, MaiaEdge creates a dependency. Partners optimize for cross-connect revenue (easy, low-effort) rather than deploying their own PBCs (harder, but strategically better for both parties). The Google comparison is instructive here: Google paid so well for distribution that many partners became dependent on Google payments, which gave Google enormous leverage over them later.

**Recommendation:** Structure partner payments with a declining schedule. Year 1 payments are generous (incentivize adoption). Year 2 payments decline by 30-40%. Year 3, the fiber operator should be on their own PBC deployment, generating their own margin. The declining payment schedule is the economic mechanism that drives partners from "cross-connect to MaiaEdge's node" to "deploy your own PBC."

---

## 8. Specific Concerns and Recommendations

### 8.1 Medium-Term Concerns (6-18 Months)

| Concern | Severity | Recommendation |
|---------|----------|----------------|
| Carrier perception of MaiaEdge as competitor | HIGH | Develop explicit "MaiaEdge Infrastructure Charter" committing to partner graduation, no direct enterprise sales from owned nodes, capped metro count |
| Cannibalization of PBC subscription revenue | MEDIUM | Price cross-connects to MaiaEdge nodes at a premium vs. operator-owned PBC economics. Make owning your own PBC always cheaper at 3+ customers |
| Sales team confusion (selling against own nodes) | MEDIUM | Create clear rules of engagement: Tim/Ken never sell cross-connects to MaiaEdge nodes as the primary offer. Always lead with operator-owned PBC. Colo node is the fallback for operators who can't deploy quickly |
| Megaport/Equinix competitive counter-messaging | HIGH | Pre-brief key accounts before first colo node goes live. Control the narrative before competitors do |
| Partner dependency on revenue share | LOW (now), HIGH (later) | Build declining payment schedule into every partner agreement from day one |

### 8.2 Long-Term Concerns (18+ Months)

| Concern | Severity | Recommendation |
|---------|----------|----------------|
| MaiaEdge becomes structurally a carrier | CRITICAL | Hard cap on owned metros (6-8 max). Board-level policy. Written into investor materials |
| Federation trust erosion | HIGH | Establish an independent "Federation Governance Council" with operator representatives who have input on federation policies, routing neutrality, and pricing fairness |
| Valuation reclassification from platform to carrier | HIGH | Track owned-node revenue separately. Publish "platform revenue" metric excluding infrastructure revenue. Show declining infrastructure mix over time |
| International operators refuse to join due to US self-deployment | MEDIUM | Never deploy MaiaEdge-owned nodes in international markets. International expansion is 100% partner-deployed. Use US experience as proof of demand, not as a model to replicate |
| Regulatory scrutiny (common carrier classification) | LOW | Consult telecom regulatory counsel. MaiaEdge-owned nodes providing connectivity could trigger state or federal regulatory obligations depending on how services are classified |

### 8.3 Structural Recommendations

1. **Create a "MaiaEdge Infrastructure Charter"** -- a public-facing document that commits MaiaEdge to:
   - Maximum 6-8 owned metros, defined by name
   - Partner graduation timeline (24 months max per metro)
   - No direct enterprise sales from owned nodes
   - Transparent federation economics (published rate card for cross-connects)
   - Annual third-party audit of federation routing neutrality

2. **Design the economics to push operators toward self-deployment:**
   - Cross-connect to MaiaEdge node: higher monthly cost, limited control, no white-label
   - Own PBC deployment: lower monthly cost, full control, white-label portal, federation capability
   - The choice should be obvious for any operator with 3+ customers

3. **Sequence the rollout carefully:**
   - Start with ONE metro (Ashburn). Prove the model works. Measure carrier reaction.
   - Do not expand to metro #2 until you have data on: carrier sentiment, cross-connect uptake, PBC conversion rate (cross-connect customers who later deploy own PBCs)
   - If carrier sentiment turns negative in Ashburn, you can course-correct before the narrative spreads

4. **Build the "graduation" story into every conversation:**
   - Every fiber operator who cross-connects to a MaiaEdge node should have a documented path to deploying their own PBC within 12-18 months
   - Make the graduation story part of the sales narrative: "This is how you start. This is where you go."

5. **Never sell to enterprises directly from MaiaEdge-owned nodes:**
   - This is the bright line. If MaiaEdge ever takes an enterprise customer directly through its colo nodes, the carrier infrastructure identity is permanently compromised.
   - All enterprise connectivity through MaiaEdge nodes must flow through a fiber operator partner. MaiaEdge is wholesale only from its own infrastructure.

6. **Scope the operational and regulatory footprint early:**
   - Determine which specific colo facilities in each metro (e.g., Equinix DC2 vs. DC5 in Ashburn). If multiple operators want different meet-me rooms, MaiaEdge could end up operating multiple PBCs per metro, compounding the "carrier" perception.
   - Define who manages cross-connect provisioning, SLA troubleshooting, and E-Line activation. If MaiaEdge handles these end-to-end, the operational profile is indistinguishable from a carrier. If the fiber operator handles their side, the delineation is cleaner.
   - Engage telecom regulatory counsel before the first node goes live. Providing connectivity via cross-connects in a colo facility may trigger state-level telecom licensing requirements. The difference between "infrastructure tenant" and "service provider" varies by jurisdiction.
   - Address routing asymmetry in the PCE: when Operator A cross-connects to a MaiaEdge node and Operator B deploys their own PBC, and both need to reach the same destination, ensure MaiaEdge's PCE does not have special routing privileges through its own nodes. Routing neutrality is essential to federation trust.

7. **Establish a hard graduation policy with consequences:**
   - Graduation timeline: 18 months per metro. If a metro has not transitioned to a local operator hub by month 18, MaiaEdge begins an active exit process (6-month wind-down).
   - If multiple metros fail to graduate, the 6-8 metro cap prevents indefinite expansion. MaiaEdge cannot add a new metro until one graduates. This creates a natural forcing function.
   - For international markets: MaiaEdge-owned nodes are never deployed outside the US. International federation paths must always route through a local operator's PBC, even if the path is technically longer. This proves geographic neutrality and prevents the US self-deployment model from spreading.

---

## 9. Bottom Line

The strategy has strong logic. The cold-start problem is real. Fiber operators are slow. The federation flywheel needs inventory. Paying partners well to accelerate distribution is proven platform strategy. Deploying your own PBCs in colos is the fastest path to marketplace viability.

But the risks are equally real. Channel conflict is not a theoretical concern; it is an existential threat to the federation model if mismanaged. The moment carriers view MaiaEdge as a competitor rather than an enabler, the federation flywheel reverses: operators refuse to federate with (or through) a company they view as competitive. Megaport's experience with carrier resistance is your cautionary tale.

The path forward is to execute this strategy with explicit, enforceable constraints that preserve the platform identity:

- **Temporary by design.** Every MaiaEdge-owned node has a graduation date.
- **Capped by policy.** Maximum 6-8 metros, named in advance, approved at board level.
- **Wholesale only.** MaiaEdge never sells to enterprises from its own nodes.
- **Economically self-defeating.** The pricing makes it always cheaper for operators to deploy their own PBCs at modest scale.
- **Transparently governed.** Federation routing, pricing, and policies are auditable.

If you can hold these lines, the acceleration benefit is real and the Twilio aspiration remains achievable. If the lines blur, as they will under revenue pressure and growth targets, MaiaEdge becomes another Megaport. And Megaport already exists.

---

*End of Analysis*
