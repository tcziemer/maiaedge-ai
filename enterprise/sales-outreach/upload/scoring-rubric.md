# Copy Scoring Rubric — Detailed Criteria

This rubric is intentionally weighted toward voice and language authenticity. Mechanical compliance matters, but what separates good copy from great copy is whether it sounds like someone who's lived in the recipient's world.

The rubric has 10 dimensions. The top four (Speaks Their Language, Research as Fuel, Problem Authenticity, Human Voice) account for 61% of the total score. That's by design. An email can follow every structural rule and still fail if it sounds like a salesperson who read their website instead of a peer who understands their world.

---

## Dimension 1: Speaks Their Language (Weight: 18%)

Does the email use the recipient's industry vocabulary? Does it frame problems the way they'd frame them in a meeting with their VP?

**9-10 — Native Fluency:**
The email reads like it was written by someone who spent a decade in their industry. Uses segment-specific vocabulary naturally: NNIs, fiber islands, Type 2 circuits (fiber); meet-me rooms, attach rates, cross-connects (colo); jitter, middle mile, inference latency (neocloud). The words are their words, not ours.

> Fiber example: "Every NNI is still a 60-90 day project. Your sales team is quoting timelines that lose multi-state deals before they start."

**7-8 — Strong Industry Voice:**
Uses most of the right vocabulary. One or two word choices that feel slightly translated from our language to theirs, but the overall framing is from their world.

> "Provisioning cross-carrier circuits still takes months. That's deals walking out the door."

**5-6 — Mixed Voice:**
Some of their words, some of ours. The email shifts between sounding like a peer and sounding like a vendor. Noticeable moments where the writer is translating MaiaEdge positioning into the recipient's world instead of starting from their world.

> "Many fiber operators face challenges with NNI provisioning timelines that impact revenue opportunities."

**3-4 — Our Language, Their Industry:**
The email talks about their industry but uses our vocabulary. "Connectivity solutions," "network optimization," "enhanced capabilities." These are vendor words dressed in industry clothing.

**1-2 — Pure Vendor Speak:**
Could be from any networking vendor to any industry. No segment-specific vocabulary at all.

**What to check:**
- Read `segment-language.md`. Does the email use insider vocabulary from their segment?
- Would someone who's spent 15 years in this segment recognize the word choices as natural?
- Are problems named the way they'd name them, or the way a sales deck names them?

---

## Dimension 2: Research as Fuel (Weight: 15%)

Research should power the email's voice and angle. It should never show up as display. The reader should think "this person gets my world" — not "this person googled my company."

**9-10 — Invisible Research:**
You can't point to where the research is in the email. But the email couldn't have been written without it. The angle is so specific to this company's situation that it required deep research to find. No "I noticed" or "I saw." No dropped stats. Just a problem framed with precision that comes from knowing their business.

> "Fatbeam's expansion into Montana means more cross-carrier circuits. I'd guess every new NNI is still a 60-90 day project."
> (Requires knowing: Fatbeam expanded into Montana, they're a fiber operator, NNIs are their provisioning bottleneck. None of this is stated as "research.")

**7-8 — Research Powers the Framing:**
One or two company-specific details that shape the email's angle. The details aren't displayed — they're used to frame a problem more precisely than generic messaging could.

**5-6 — Research as Decoration:**
The email includes company details but they sit awkwardly. "With your 15,000 route miles across five states..." or "Given your recent expansion..." The research is visible as research, not absorbed into the voice.

**3-4 — Token Personalization:**
Company name + industry + generic pain. The email would work with any company name substituted.

**1-2 — No Research:**
Pure template. Company name is the only variable.

**Red flags:**
- "I noticed..." / "I saw your..." / "I read that..."
- Listing facts about the company (route miles, employee count, revenue)
- Referencing their LinkedIn posts or quoting them back
- Opening with company context instead of a problem
- Stats dropped in to prove you did homework rather than to build the argument

---

## Dimension 3: Problem Authenticity (Weight: 14%)

The problem named in the email must be something the recipient would recognize from their daily reality. Named in their words, not ours. A problem they'd complain about at a trade show, not one a marketing deck identifies.

**9-10 — Their Daily Pain:**
The problem is named exactly the way they'd name it in conversation. Reading it feels like someone overheard their frustrations and wrote them back. Uses the language from `segment-language.md` "How They Talk About Problems" section.

> Fiber: "Once traffic hits a Type 2 circuit, you're blind. Responsible for the SLA but can't see the path."
> MSP: "Three carriers, three tickets, three different answers. Meanwhile your customer is calling every hour."
> Neocloud: "Inference latency varies by facility and your team can't tell whether it's the carrier, the colo, or something in between."

**7-8 — Real Problem, Close to Their Words:**
The problem is authentic and relevant. Framing is close to how they'd say it but not quite their exact conversational register.

**5-6 — Real Problem, Our Framing:**
Correct pain point but described in marketing language. "Provisioning delays impact revenue" instead of "every delay is a deal at risk."

**3-4 — Generic Problem:**
The pain is real for the segment but not specific enough. Could apply to any company. "Provisioning takes too long" without the lived-in detail.

**1-2 — Wrong Problem or No Problem:**
Opens with solution instead of pain. Or names a problem this person wouldn't recognize from their daily work.

---

## Dimension 4: Human Voice (Weight: 14%)

Would a real person actually write this? Not a marketing department. Not a sequence tool. A smart industry peer who sat down and wrote a note.

**9-10 — Sounds Like a Person:**
You forget it's a cold email. Natural cadence. Short sentences. Sometimes fragments. "I'd guess" used honestly. One idea, committed to. Some personality shows through. There's a line or two that doesn't "do work" — it just sounds like how someone talks.

> "I'd guess provisioning hasn't caught up with expansion yet. Most operators in your position are still quoting 60-90 days for cross-carrier circuits. Not exactly the speed story your sales team wants to tell."

**7-8 — Professional but Warm:**
Sounds like a person, even a polished one. Mostly natural. Maybe one sentence that feels slightly structured.

**5-6 — Competent but Formulaic:**
You can see the template underneath. Every sentence serves an obvious purpose (context, pain, solution, CTA). The structure is showing.

**3-4 — Clearly Automated:**
Every paragraph does visible work. Transitions like "That's why I'm reaching out..." Perfect parallel structure throughout. Value props stacked in lists. The email is mechanically correct but has no soul.

**1-2 — Spam Adjacent:**
Marketing language, hype words, robotic structure. "I'd love to" + "I'd be happy to" + "Let me know if..."

**Human voice markers (good):**
- Short sentences. Sometimes fragments.
- "I'd guess" or "I'd imagine" used genuinely
- Acknowledging what you don't know: "Not sure if this is on your radar"
- Active voice, direct statements
- Personality in word choice

**Sequence tool markers (bad):**
- Every sentence doing obvious "work"
- "That's why I'm reaching out..."
- Perfect grammar throughout (real emails have rhythm, not perfection)
- Stacking three value propositions in one email
- "I'd love to..." / "I'd be happy to..." / "Let me know if..."

---

## Dimension 5: Segment Accuracy (Weight: 10%)

Correct ICP framing. The messaging matches the segment's fundamental value proposition and avoids segment-specific landmines.

**Instant deductions (drop to 1-3):**
- Sovereignty language for a neocloud (they ARE the customer)
- NaaS positioning ("join our fabric" instead of "build your own")
- Claiming a network operator is slow internally without checking (Track A vs Track B)
- Colo messaging for a fiber operator (or vice versa)
- "Keep your customer" language for a neocloud

**Key segment checks:**

| Segment | Must Include | Must Avoid |
|---|---|---|
| Fiber | Monetize existing fiber, dark fiber opportunity, provisioning speed + ownership | NaaS framing, infrastructure replacement |
| Colo | Build own fabric, keep customer/margin/control, compete with big players | "Join our fabric," NaaS positioning |
| AI Colo | Standard colo + AI infrastructure gap, deterministic paths for GPU tenants | Generic colo without AI angle |
| Neocloud | Observability first, deterministic paths, cost savings | ALL sovereignty language |
| Network Op | Extend automation beyond borders (Track A) or unify first (Track B) | "You're slow," criticizing internal automation |
| MSP | End-to-end visibility, asset-light model, SLA proof | CapEx messaging, "build infrastructure" |

---

## Dimension 6: Role Alignment (Weight: 8%)

Is the angle calibrated to what this specific persona cares about in their daily work?

**9-10:** The email reads like it was written for someone in this exact role. Problems, metrics, and outcomes match their worldview.

**7-8:** Generally aligned. Right domain (business vs technical) with appropriate framing.

**5-6:** Neutral. Not wrong, but not specifically calibrated.

**3-4:** Misaligned. Technical architecture for a CEO. Revenue metrics for a network engineer.

**1-2:** Completely wrong audience.

**Quick alignment check:**
- CEO: Revenue, competitive position, board-level outcomes, market timing
- CTO: Architecture, protocol simplicity, integration, technical risk
- COO: Operational efficiency, headcount, scale, automation
- VP Sales: Deal velocity, win rates, provisioning as competitive weapon
- CFO: Cost reduction, OpEx vs CapEx, cash flow, ROI
- Sr. Engineer: Time per task, tooling, troubleshooting burden, protocol elimination

---

## Dimension 7: Brevity & Density (Weight: 7%)

Every sentence earns its place. No filler. Within segment word counts.

**9-10:** Impossibly tight. Every word does work. Removing any sentence would lose something important.
**7-8:** Lean and focused. Maybe one sentence that could be tighter.
**5-6:** Within word count but has padding. A sentence or two that don't add value.
**3-4:** Over word count or noticeably padded. Multiple sentences doing the same job.
**1-2:** Wall of text. Way over word count. Redundant points.

**Word count targets (Email 1):**
- Fiber: 75-125 | Colo: 100-150 | AI Colo: 100-150
- Neocloud: 100-150 | Network Op: 125-175 | MSP: 75-125

**Common bloat patterns:**
- Two sentences making the same point differently
- Context-setting before getting to the problem
- Over-explaining what MaiaEdge does
- Stacking multiple proof points (one is enough)

---

## Dimension 8: CTA Quality (Weight: 5%)

Single question. Low friction. Conversational. Not needy.

**9-10:** Natural end to a conversation between peers. You'd reply without thinking.
> "Open to a conversation?" / "Dealing with something similar?"

**7-8:** Clean, single ask. Appropriate friction.
> "Worth a conversation?" / "On your radar?"

**5-6:** Functional but slightly off. Too formal or passive.
> "Would it make sense to schedule a brief discussion?"

**3-4:** Multiple asks, calendar link, or pressure.
> "I'd love to set up 15 minutes this week. Here's my calendar: [link]"

**1-2:** Desperate, manipulative, or absent.

**CTA rules:**
- ONE question. Never stack.
- No "I'd love to..." or "I'd be happy to..."
- No "Let me know if..." (passive, easy to ignore)
- No calendar links in first email
- No "quick call" (signals desperation)
- Rotate phrasing across a sequence

---

## Dimension 9: Credibility Integration (Weight: 5%)

Founder credibility dropped in naturally. Not staged, not over-explained.

**9-10:** So natural you almost miss it. Just a fact stated with quiet confidence.
> "We built this at MaiaEdge. Same team behind Acme Packet."

**7-8:** Present and clean. One sentence, moves on.
> "Same team that built Acme Packet."

**5-6:** Slightly forced or over-explained.
> "Our founders previously built Acme Packet, acquired by Oracle for $2.1 billion..."

**3-4:** Absent or buried in the wrong place.
**1-2:** Missing entirely, or so overblown it reads as bragging.

---

## Dimension 10: Sovereignty Thread (Weight: 4%)

Speed paired with ownership. The operator keeps the customer, the margin, the control.

**For Neoclouds: Score N/A.** Redistribute the 4% equally across other dimensions. Sovereignty language is WRONG for neoclouds.

**9-10:** Sovereignty woven throughout. Speed and ownership are inseparable.
> "Your team provisions in minutes. Your portal, your invoice, your customer."

**7-8:** Present. Speed paired with ownership at least once.
> "You deliver services yourself. 10 minutes, not 90 days."

**5-6:** Speed mentioned but ownership implicit or absent.
> "Reduce provisioning from 90 days to 10 minutes."

**3-4:** Reads like NaaS. Sounds like MaiaEdge delivers the service.
**1-2:** Actively undermines sovereignty. "Connect to our fabric."

---

## Calculating the Overall Score

```
Overall = (Language × 0.18) + (Research × 0.15) + (Problem × 0.14) + (Voice × 0.14)
        + (Segment × 0.10) + (Role × 0.08) + (Brevity × 0.07) + (CTA × 0.05)
        + (Credibility × 0.05) + (Sovereignty × 0.04)
```

Round to one decimal place.

For neoclouds, redistribute Sovereignty (4%) equally across the other 9 dimensions (~0.44% each).

**Scoring scale:**
- **9-10**: This email sounds like it was written by someone who spent 10 years in their industry. I'd reply.
- **7-8**: Strong voice, authentic framing. Minor tweaks to sharpen.
- **5-6**: Competent but sounds like a salesperson, not a peer. Missing the vocabulary or lived-in quality.
- **3-4**: Template voice. Could swap in any company name. Research displayed, not absorbed.
- **1-2**: Wrong segment, wrong language, or reads like automated outreach.

---

## Sequence-Level Scoring (Beyond Individual Emails)

When critiquing a full sequence, also evaluate:

| Dimension | What to Check |
|---|---|
| **Arc Coherence** | Does the sequence tell a story? Each touch advances the narrative. |
| **Angle Diversity** | Does each email bring a genuinely different angle? Not shorter versions of Email 1. |
| **Escalation Logic** | Does urgency build naturally? Not manufactured — earned through value. |
| **Spacing** | 3-5 days between touches. Not too aggressive, not too passive. |
| **Breakup Execution** | Does the final touch provide graceful exit while leaving the door open? |

---

## The Ultimate Test

After scoring, apply this:

**"If I forwarded this to someone who's spent 15 years in this segment, would they say 'yeah, this person gets it' — or would they say 'this is a salesperson who read our website'?"**

The score should match that gut check. If the numbers say 7 but the gut check says "salesperson," trust the gut and rescore.
