# MaiaEdge Sender Profiles

> Last updated: March 2026
> **This is the single source of truth for all outreach sender identities.** All email and LinkedIn skills reference this file.

---

## Tim Lieto

| Field | Value |
|-------|-------|
| **Name** | Tim Lieto |
| **Title** | AVP, North America Sales |
| **HubSpot Owner ID** | `161889085` |
| **Territory** | East (30 US states) |
| **States** | AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV |
| **Location** | Greater Boston, MA |
| **Default sender?** | Yes. Use Tim unless prospect is in Ken's territory. |

---

## Ken Cunningham

| Field | Value |
|-------|-------|
| **Name** | Ken Cunningham |
| **Title** | Sales, East Region |
| **HubSpot Owner ID** | `162339176` |
| **Territory** | West (20 US states + DC) |
| **States** | AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY |
| **Default sender?** | No. Only when prospect HQ is in his territory. |

---

## Timothy Ziemer

| Field | Value |
|-------|-------|
| **Name** | Timothy Ziemer |
| **Title** | CRO / International |
| **HubSpot Owner ID** | `159350430` |
| **Territory** | All non-US countries |
| **Default sender?** | No. International accounts only. |

---

## Voice and Tone (All Senders)

All senders use the same voice. The email should read as if written by a smart industry peer who spent 10 minutes learning about the prospect's business.

**Voice characteristics:**
- Direct. Short sentences, occasional fragments.
- Problem-first. Lead with their pain, not our solution.
- Relevance over personalization. Research shapes the problem hypothesis, not the opening line.
- Uses "I'd guess" and "I'd imagine" honestly, not as filler.
- Acknowledges what we don't know. Never claims certainty about their business.
- Peer tone with technical operators. Never talks down, never talks up.

**What it should NOT sound like:**
- A marketing email
- A sequence tool output
- A mass blast with merge tags
- An overeager SDR who just discovered LinkedIn

---

## Signature Protocol

- Sign off with sender's first name only: "Tim" or "Ken"
- No full signature block. No title. No phone number. No "Best regards."
- Email platform auto-appends the formal signature block. Skills never write one.

---

---

## Abilash Menon (Founder)

| Field | Value |
|-------|-------|
| **Name** | Abilash Menon |
| **Title** | CEO & Co-Founder |
| **HubSpot Owner ID** | `159974715` |
| **Territory** | No territory restriction (founder). Strategic accounts and technical prospects. |
| **Default sender?** | No. Only for founder-level outreach, CTO/technical leaders, founder-to-founder, or when specified. |
| **Background** | Ex-Cisco MPLS, 128T SD-WAN architect, Juniper. Built the technical architecture behind MaiaEdge. |

### Abilash's Voice

Abilash writes with technical precision and dry wit. His emails should feel like they come from a CEO who spent his career solving the exact problem the prospect is facing.

**Voice characteristics (dial to 30% in cold emails):**
- Vivid, unexpected analogies — "a Rube Goldberg machine made of routers, firmware, and hope"
- Dry humor with technical authority
- Blunt observations earning credibility through specifics
- Comfortable naming the problem directly: "Federation is still diplomacy by spreadsheet"
- Technical credibility without jargon — explains complex ideas simply
- First-person narrative: "I've sat through six-month troubleshooting calls..."

**Best for:**
- CTO, VP Engineering, technical founders
- Discussions about network architecture, automation, observability
- Founder-to-founder outreach (regardless of prospect role)
- Technical skeptics or deep-dive conversations
- Neocloud technical decision-makers (Crusoe, Together.ai, RunPod CTOs)

### When to Use Abilash

| Scenario | Use Abilash? | Why |
|----------|---|---|
| CTO at a fiber operator | YES | Technical peer credibility |
| VP Engineering at neocloud | YES | Founder-to-founder + technical depth |
| CEO of a carrier (non-technical) | NO | Use Tim instead (commercial lens) |
| Product leader at enterprise | YES | Can discuss technical vision alignment |
| Network architect | YES | Deep technical conversation possible |
| Pure business decision-maker | NO | Use Tim (commercial framing) |
| Founder at any company | YES | Always founder-to-founder, regardless of their role |

---

## Timothy Ziemer (Founder & CRO)

| Field | Value |
|-------|-------|
| **Name** | Timothy Ziemer |
| **Title** | CRO & Co-Founder |
| **HubSpot Owner ID** | `159350430` |
| **Territory** | International (non-US) + strategic US accounts. Can override territory ownership. |
| **Default sender?** | No. International accounts, strategic accounts, commercial decision-makers, or when specified. |
| **Background** | Ex-Acme Packet commercial lead, Oracle, 128T sales leadership, Juniper. Deep carrier and infrastructure sales expertise. $2.55B in combined exits. |

### Timothy Ziemer's Voice

Timothy writes with business acumen and competitive insight. His emails sound like a CRO who understands P&L, board conversations, and market dynamics.

**Voice characteristics:**
- Speaks the language of competitive dynamics and market timing
- Direct about business implications: revenue at risk, deals lost, margin erosion
- References patterns across the industry: "Every operator I talk to..."
- Can speak to board-level conversations and investor narratives
- First-person credibility: "After two exits in this space, this is what I'm convinced about"
- Understands the political/commercial landscape, not just technical

**Best for:**
- CEO, CFO, COO, VP Sales/CRO (commercial leaders)
- Discussions about competitive positioning, market strategy, revenue models
- Large/strategic accounts requiring C-suite credibility
- International market expansion
- Investors or board-level conversations
- Operators concerned about Tier 1 competition (Lumen)

### When to Use Timothy

| Scenario | Use Timothy? | Why |
|----------|---|---|
| CEO at colocation operator | YES | Business strategy + founder credibility |
| CFO evaluating investment | YES | P&L and business model discussion |
| VP Sales at fiber operator | YES | Can discuss competitive dynamics + commercial terms |
| CTO (non-founder) | NO | Use Abilash (technical credibility) |
| Board member / investor | YES | Founder + commercial background |
| Founder (any background) | MAYBE | If commercial angle needed. Otherwise Abilash. |
| VP Product | NO | Use Abilash (product vision) |

---

## Founder Sender Selection Logic

```
Prospect is a founder (any role) → Use Abilash Menon (founder-to-founder)
Prospect is CTO/VP Engineering → Use Abilash Menon (technical peer)
Prospect is CEO (non-technical background) → Use Timothy Ziemer (business peer)
Prospect is CFO/COO/VP Sales → Use Timothy Ziemer (commercial peer)
Prospect is Product leader → Use Abilash Menon (technical vision)
Prospect is network architect / Sr. engineer → Use Abilash Menon (technical depth)
Prospect is decision-maker (strategic account) → Use Timothy Ziemer (founder + business credibility)
Unknown persona or multi-stakeholder → Ask user which founder / which angle
```

---

## Founder vs. AE Sender Selection

**When to use a founder (Abilash or Timothy) instead of an AE (Tim or Ken):**

1. **Strategic/high-touch accounts:** Requires founder-level credibility to break through
2. **CEO-to-CEO conversations:** Founder adds weight that AE cannot
3. **Founder-to-founder outreach:** Always founders talking to founders
4. **Technical skepticism:** Abilash can credibly say "I built this architecture"
5. **Competitive displacement:** Timothy can credibly say "We've seen this movie before"
6. **Board/investor level:** Timothy adds institutional credibility
7. **Stalled deals needing escalation:** Founder involvement signals high interest

**When AEs are appropriate:**
- Standard prospecting (majority of emails)
- Territory-based accounts (Tim/Ken's natural domain)
- Follow-up and qualification
- Ongoing relationships

**Coordination rule:** If a founder is emailing an account, the territory AE must be looped in (CC'd or informed). Founders supplement, not replace, territory owners.

---

## Founder Outreach Tone Rules

These rules apply ONLY to founder emails (Abilash or Timothy). AE emails follow the standard tone rules in the main section above.

### The Founder Advantage (How Founders Write Differently)

**Founders can:**
- Use first-person experience: "I've seen this problem at a dozen operators" (not "MaiaEdge serves operators")
- Be more direct: "Your provisioning is the bottleneck" (more credible from founder who built the solution)
- Name the problem bluntly: "The industry has duct-taped this for 30 years" (candor sounds earned)
- Skip hedging when research confirms the pain: "That takes weeks" (not "I'd imagine that takes weeks")
- Weave credibility into narrative: "After Acme Packet and 128T, this is the problem we solved" (not a separate credibility line)
- Have informed opinions: "Lumen's vertical integration is exactly the wrong move" (founder POV)
- Be brief and confident: Short emails signal they're sharing something relevant, not trying to convince

### The Human Test for Founder Emails

Before sending: **"Would this founder who actually built this product write this email?"**

If it reads like a sales sequence with a founder's name, rewrite it. Should feel like someone with skin in the game, not someone executing a playbook.

### Signature Protocol for Founders

Same as AEs:
- Sign off with first name only: "Abilash" or "Tim" (Timothy Ziemer signs as "Tim" in founder context, but to avoid confusion with Tim Lieto, may sign "Timothy")
- No full signature block, no title
- Email platform auto-appends formal signature

---

## Sender Selection Logic

```
Prospect HQ in Tim Lieto's 30 states → Tim Lieto (AE)
Prospect HQ in Ken Cunningham's 20 states + DC → Ken Cunningham (AE)
Prospect HQ outside US → Timothy Ziemer (CRO/Founder)
Prospect HQ unknown → Tim Lieto (default AE)

FOUNDER OVERRIDE:
Prospect is a founder → Abilash Menon (founder-to-founder)
Prospect is CTO/technical leader → Abilash Menon
Prospect is CEO/CFO (commercial) → Timothy Ziemer (can override territory)
Prospect is strategic account → Timothy Ziemer or specify in request
```
