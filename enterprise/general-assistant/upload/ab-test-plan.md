# A/B Test Plan - Q2 2026 Cold-Email Validation

**Source:** Deep Messaging Audit (2026-05-11) §9 + Cross-Audit Decisions Sidecar (2026-05-11) §5.
**Status:** Run all four tests **in parallel** during Week 4 of the messaging rollout (per Sidecar Decision 5 - Cooper override on Deep Sharpening §9's sequenced schedule).
**Owner:** Cooper (RevOps), with sender execution by Tim Lieto / Ken Cunningham / Tim Ziemer.

---

## Why parallel, not sequenced

Deep Sharpening §9 left the schedule open. Sidecar Decision 5 resolved it: run all four tests in Week 4 simultaneously on adequately sized lists. The parallel motion gets all four answers within the same 14-day window and avoids the sequencing risk where one test informs the next and the data drifts. The cost is volume - four parallel tests need ~400 sends in Week 4. The available list capacity covers this.

---

## Stat protocol (applies to every test)

- **Minimum sample:** 100 sends per variant (50 per variant for Test 4 within FS/OS sub-segments specifically - list size is the constraint there).
- **Sequence completion before evaluating:** 14-day full sequence (E1 → E2 → E3 over the 3-7-7 cadence).
- **Confidence interval:** 95% on reply-rate delta before declaring a winner.
- **Primary metric:** reply rate.
- **Secondary metric (tie-breaker if reply rates are within noise):** positive-reply share.
- **Tertiary metric (Test 3 only):** hot-reply-to-booked-meeting conversion rate, time-to-meeting.

---

## Test 1 - Colo E1 reframed (Sidecar §4.1.A) vs current operator-sovereignty E1

**What it validates:** Cross-Audit Decision 1 directionally. The colo segment is the worst-performing in the 60-day corpus (0.26% RR, 1 reply on 384 sends). The sharpened E1 leads on the interconnection-attach-rate-vs-landlord frame ("Interconnection attach rate is what separates colos from being landlords") and drops operator-sovereignty as the lead. The hypothesis: pulling the sharpened E1 forward should lift colo reply rate from 0.26% baseline to >2%, matching the call-resonance language Centra and Hudson IX echoed on calls.

**Control:** Current Tim Lieto colo E1 leading with "your brand, your portal, your invoice."
**Variant:** Sharpened E1 from `context/outreach/fallback-messaging.md` § Colocation Standard (Sidecar §4.1.A 75-word template).
**Segment:** Colocation Standard (no confirmed AI signals). AI Signals colo (Lambda/Crusoe/Nebius tenant, liquid cooling, 30kW+ racks) uses §4.1.B and is OUT of this test scope.
**List size:** 100+ sends per variant. Tim Lieto's East colo lookalike list has capacity.
**Primary metric:** Reply rate. **Secondary:** Positive-reply share.
**Senders:** Tim Lieto (East), Ken Cunningham (West). Same sender across both variants of a given recipient - split at list level, not contact level.

---

## Test 2 - Tier 1 carrier "extending L2 services" E1 (Sidecar §4.2) vs current Tier-1-with-extend-reach E1

**What it validates:** Cross-Audit Decision 2 directionally. The Tier 1 carrier E1 has been using the Tier 2/3 extend-reach lead by default. Sidecar §4.2 reframes Tier 1 around mixed-transport L2-services pain (tower backhaul, partner last-mile, enterprise drops). The hypothesis: the reframed E1 should lift Tier 1 reply rate by surfacing the actual buying-question (how to simplify L2 extension across mixed transport they don't own) that the current extend-reach framing buries.

**Control:** Current Tim Z ITW E1 leading with "internal automation works but cross-carrier still takes weeks."
**Variant:** Sharpened E1 from `context/outreach/fallback-messaging.md` § Network Operator Tier 1 (Sidecar §4.2 78-word template). Opener: "The hard part isn't the core."
**Segment:** Tier 1 Global ($10B+) and Tier 1 National ($1-10B with own backbone). Per the Tier 1 definition table in `context/copy-strategy/segment-messaging.md` §5A. Tier 2/3 Regional Wholesale is OUT of this test scope.
**List size:** 100+ sends per variant.
**Primary metric:** Reply rate. **Secondary:** Conversion to meeting.
**Senders:** Tim Ziemer (International Tier 1s), Tim Lieto / Ken Cunningham (US Tier 1s split by territory).

---

## Test 3 - CTA rotation for hot replies (booking link vs propose-three-times)

**What it validates:** The replied-thread audit isolated a pattern: hot replies (Meeting Request) consistently counter-propose specific times rather than book via calendar link. Fernando @ Start Campus ("10am Tuesday"), Marc Becker (asked to resend the link), Roland Certeza (booked his EA to coordinate booth time) all counter-proposed. The hypothesis: proposing three specific times converts hot replies to booked meetings faster than sending a calendar link.

**Control:** Current behavior after a hot reply: "Here's my calendar link."
**Variant:** Reply with three specific times: "How does Tue 10am, Wed 2pm, or Thu 9am look?" (Times shifted to actual proposed slots in the sender's calendar.)
**Trigger:** Any hot reply (Meeting Request / Demo Ask / explicit "let's meet" reply) within the test window.
**Sample:** ALL hot replies in the test window across all senders. List-size constraint does not apply since this is post-reply, not pre-send.
**Primary metric:** Hot-reply-to-booked-meeting conversion rate. **Secondary:** Time-to-meeting (calendar day count from hot reply to confirmed meeting).
**Operational note:** Senders need to know the test rules before Week 4 starts. Each sender pre-blocks 3 specific time slots per business day for the variant period. Cooper builds a quick weekly time-slot template per sender.

---

## Test 4 - Enterprise E1 anchor: M&A vs dark-fiber-redundancy

**What it validates:** Cross-Audit Decision 6 + the Sidecar §4.7 / Deep Sharpening §8.6 launch. The Enterprise playbook ships with two E1 anchors - dark-fiber-redundancy (default) and M&A network integration (FS/OS sub-segments). The hypothesis: for Financial Services + Outsourcing Services, M&A is the stronger anchor; for Retail/Distribution + Healthcare, dark-fiber is stronger. Test head-to-head within equivalent FS/OS sub-segment lists.

**Control:** Dark-fiber-redundancy E1 (Sidecar §4.7 default - 84 words, "the redundancy works on the architecture diagram, not under load").
**Variant:** M&A anchor E1 (the Sidecar Decision 6 alt - 84 words, "Every M&A event in your industry creates a network integration project").
**Segment:** Enterprise - Financial Services + Outsourcing Services sub-segments specifically. Retail/Distribution + Healthcare are NOT in scope for this test (they use the dark-fiber-redundancy default without testing).
**List size:** 50+ contacts per variant per sub-segment (Sidecar Decision 6 pilot batch size is 50-80 contacts total; this test sits inside that pilot).
**Primary metric:** Reply rate per sub-segment. **Secondary:** Reply quality (positive intent share - meeting requests + substantive engagement).
**Senders:** Tim Lieto (East FS/OS prospects), Ken Cunningham (West FS/OS prospects). Tim Ziemer (International FS/OS).

---

## Out of scope for this test plan

- **Hedge cap enforcement** is a rule, not a test. The 30% cap stays - see `context/outreach/email-writing-rules.md` § Hedge Variety Requirement.
- **Persona blocklist** is a pre-cadence gate, not a test. The 5 titles in `context/outreach/persona-targeting-blocklist.md` are blocked before send - there is no control variant where they remain.
- **Pre-cadence list hygiene** is a pre-cadence gate, not a test. The three filters in `context/outreach/pre-cadence-hygiene.md` run before any contact enters the cadence regardless of test bucket.
- **Subject-line variants for off-event lists** are a documented default (`email-writing-rules.md` § Subject Lines, Decision 10), not a formal A/B test. Senders rotate per the guidance.

---

## Schedule

- **Week 1 (current):** Universal rule changes ship (P0 commits). Fabric-in-a-box ban in cold/LinkedIn. "We built carrier infrastructure that..." retire. Persona blocklist live. Pre-cadence hygiene live.
- **Week 2:** Per-segment E1 reframes ship (Colo Standard + AI Signals, Tier 1 vs Tier 2/3 carrier, Fiber activation-velocity). Enterprise playbook launch starts (50-80 contact FS/OS pilot batch).
- **Week 3:** Enterprise playbook full launch. Healthcare + Retail/Distribution batch 2 ships using dark-fiber default.
- **Week 4 (parallel test window):** All four A/B tests fire simultaneously. 14-day sequence completion.
- **Week 6 (evaluation):** Statistical evaluation of all four tests at 95% CI. Winners declared. Production playbook updated.

---

## Verification items flagged (per Sidecar §6)

These do NOT block the rollout but should be confirmed before Week 4:

1. **Demo readiness for neocloud technical buyers (Decision 13).** Cooper or Tim Z to confirm with Kyle Blackwell or Abilash. If demo-ready, neocloud CTA stays "Open to a quick demo?" If not, soften to "Open to a 15-minute walkthrough?" until demo materials are ready. NOT in scope for A/B Test 4 (which is Enterprise, not neocloud).
2. **Wholesale-Director partner-cadence (Decision 11) - deferred.** Not in scope for this rollout. Revisit if a Konnexx-pattern engagement progresses to a real partnership.

---

## Decision history

- **2026-05-11:** Plan written from Deep Sharpening §9 (4 tests) + Sidecar §5 (parallel schedule per Decision 5) + Decision 6 (FS/OS pilot anchor for Test 4) + the replied-thread audit pattern (Test 3).
