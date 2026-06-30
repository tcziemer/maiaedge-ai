# Post-Call Leave-Behind - Build Guide ("Recap & Path Forward")

How to fill `template.md` into a partner-grade leave-behind that a champion forwards across their org to
advance the deal. `build.py` owns the LOOK (Tomorrow brand, eyebrow sections, branded tables); this guide and
`template.md` own the STRUCTURE and WORDS. Render with the main `assets/build.py`, not the one-pager renderer.

**When this goes out:** AFTER a discovery or demo call, to ADVANCE the deal. It is the seller in the room you
are not in. (Distinct from the outbound one-pager, which rides a connection-accept/reply to GET a meeting.)

**The one sentence that should govern every choice:** the person who decides was probably not on the call, so
write the document they will read on a forward, not a recap for the person who was there.

---

## 0. Specify the audience first (it shifts the whole doc)

The rep names the audience when asking for the doc. The audience decides what leads and which proof shows up.

| Audience the rep names | Lead the value framing with | Proof to pull | Stakeholder block? |
|---|---|---|---|
| The champion, to forward up | the cost-of-inaction + the one-line ROI the champion will repeat | a same-segment peer | YES - the per-lens block is the champion's ammunition |
| Economic buyer / CFO / Finance | ROI, payback, cash-flow, risk to budget | a peer with a hard payback figure | light - fold Finance lead into the summary |
| Technical / VP Eng / Network / CISO | determinism, visibility, security, integration, no rip-and-replace | a technical/uptime detail, the architecture | light - lead Technical |
| Operations / COO | one operating model, headcount-neutral scale, fewer tickets | an operational simplicity story | light - lead Ops |
| The full buying committee | the whole case, group-relevant, no single persona over-indexed | one strong peer + the value table | YES - include the full per-lens block |

**The Gartner rule behind this:** content built for the whole GROUP lifts consensus; content over-personalized
to ONE individual measurably fractures it. So even a "for the CFO" doc stays group-readable - it leads with the
finance lens, it does not strip everything else out.

---

## 1. Gather the inputs (compose on call-analysis, don't reinvent it)

Run the `call-analysis` skill (Mode 1) over the account's most recent call(s) first - it already extracts the
use cases discussed, the pain, the objections, and reads the MEDDPICC contact fields. Then pull:

| Source | What you take from it |
|---|---|
| Call engagement (`hs_call_summary`, `hs_call_body`, `hs_call_has_transcript`, `hs_call_transcript_tracked_terms`) | "What we heard," the use cases actually discussed, the objections actually raised, any next steps named on the call |
| Company record (segment, `account_brief`, enriched fields, `recent_news_or_trigger_event`) | the account framing, the segment pillar set, the why-now |
| Deal record (stage, amount, the MEDDPICC mirror) | size/stage calibration; whether to extend to the long business case (below) |
| Contacts on the deal (titles/roles) + `Champion` | who was on the call, who the stakeholder block speaks to, who forwards it |

**MEDDPICC → section router** (read the MEDDPICC contact fields per `call-analysis`'s MEDDPICC Rule - that skill
is the source of truth for the field set and currency; do not invent values, use what is populated):

| MEDDPICC field | Feeds which section |
|---|---|
| `meddpicc_pain_contact` + `meddpicc_use_case` | "What we heard" + which rows appear in the use-case table |
| `meddpicc_metrics_contact` | "Why moving now beats waiting" + the payoff column (the quantified value) |
| `meddpicc_criteria_contact` (decision criteria) | the "what it does / payoff" framing - the why-us mapping |
| `meddpicc_competition_contact` | the objection block - what to de-risk against |
| `Champion` + contact roles | the per-stakeholder block + who the doc is written to be forwarded to |

If a field is blank or the call had no transcript, do NOT fabricate - see §6 (proceed + flag VERIFY-BEFORE-SEND).

---

## 2. The structure (flexible 1-3 pages; each section earns its place)

Order is load-bearing: the case for CHANGE comes before the case for US. Drop any section that has no real input
from the call rather than padding it.

1. **Masthead / cover** - account-framed OUTCOME headline (`Cutting [Account]'s multi-region provisioning from
   weeks to minutes`), eyebrow `RECAP & PATH FORWARD`, `Prepared for [Account] · [date]`. Compact, not a brochure cover.
2. **Executive summary** - 3-4 sentences that survive being read ALONE by an exec who was not on the call. Lead
   with the conclusion (the outcome + the path), not the background.
3. **What we heard** - proof-of-listening. 3-5 bullets of their situation, goals, and constraints in THEIR words
   (from the transcript + `meddpicc_pain_contact`). Not a re-pitch; it proves you listened.
4. **Why moving now beats waiting** - the cost of the current setup, quantified from THEIR inputs and labeled
   "based on what you shared." This is the case for change and it comes before any MaiaEdge capability.
5. **The use cases we mapped** - THE CENTERPIECE. A branded table. Rows = the use cases actually raised on the
   call (classify against `context/sales/use-case-taxonomy.md`). Columns = `Use case | What it does | The payoff
   for you | Who it helps`. The payoff column is ranged + input-grounded (§5 voice). "Who it helps" carries the
   stakeholder lens (Finance / Engineering / Ops).
6. **Working through the open questions** - the objections that came up, handled NON-defensively (§4). Only the
   ones raised. This is the highest-leverage page-2 section - see the JOLT rule in §5.
7. **What operators like you have seen** - proof. A stage-matched named reference or case snippet. Post-engagement,
   so named references + credibility anchors are ALLOWED here (the inverse of cold). Woven as de-risk, not hype.
8. **What each stakeholder gets** - the per-lens block (Finance / Technical / Ops one-liners). Include when the
   audience is the committee or "to forward up" (§0). This is the consensus engine for the people who were not on the call.
9. **The path forward** - a Mutual Action Plan: ordered next steps, each with an OWNER and a DATE, on BOTH sides
   (aim for at least half the steps owned by the buyer). Confirm the next meeting. One clear next step.
10. **Footer** - `MAIAEDGE · PREPARED FOR [ACCOUNT] · [DATE]`.

---

## 3. Optional extension - the long business case (enterprise / high-ACV)

For large or enterprise deals, extend Mode B to a ~5-page business case (never bloated, always fronted by the
1-page exec summary). Add: a fuller quantified ROI model (conservative / expected scenarios), risk + mitigation,
an implementation path, and the decision criteria mapped to capabilities. Use the canonical framework at
`context/sales/business-case-framework.md` (§A 10-section structure + §D rigor rules). Same voice rules.

---

## 4. Objection handling - Concern -> Reframe -> De-risk (never defensive, never re-sell)

For each objection that actually came up on the call:
- **State the concern in their words** ("You flagged that switching cross-connects mid-contract feels risky").
  Naming the real concern IS the work - it signals you listened.
- **Reframe** the concern as the unmet need behind it. No "but," no "actually," no re-hyping the upside.
- **De-risk** with a concrete mechanism: a phased rollout, an exit clause, a peer who did the same, a single PBC
  pair to prove it. Resolve with a thing, not a feeling.

Pull the actual MaiaEdge answers from `context/core/competitive-positioning.md` and
`context/core/differentiation-naas-aggregator.md` (the canonical objection responses - "How is this different
from Megaport?", "we already have NNI partners", build-vs-buy, "isn't this expensive", "we don't have the team").
Address ONLY the objections that surfaced; do not pre-litigate ten hypotheticals.

---

## 5. Voice rules

**These flip vs. cold (because this is post-engagement, mid-cycle):**
- **Named references, case studies, and credibility anchors are ALLOWED** (RevNet / Centra / Arvig / the
  Acme Packet + 128 Technology exits). Mid-cycle is exactly where detailed proof belongs.
- **Reference the call.** "From what you shared on [date]" is the whole point - this is a recap.
- **Naming their current-state cost is fine** when THEY stated it on the call (it is their words, not us asserting a flaw).

**These are KEPT from the house style:**
- **No em dashes** anywhere. Ranges use hyphens (`60-90 days`).
- **"Carrier infrastructure"** is the only category term (never IaaS / NaaS / platform).
- **No fabricated numbers.** Every figure is labeled + ranged + input-grounded ("based on what you shared," an
  "illustrative range," or "from a comparable [segment] customer"). Any external/product number comes from the
  approved fence in `assets/onepager/facts.md`. A fabricated ROI number is the same integrity failure as a
  fabricated signal - do not present a modeled figure as a measured one.

**The new, load-bearing rule (from the JOLT research - the single biggest "don't"):**
- **The objection/de-risk section DE-RISKS; it never re-sells the upside or re-establishes urgency.** Re-hyping
  value or pushing "now is the time" statistically INCREASES the odds of losing a hesitant deal. The buyer's
  blocker at this stage is fear-of-messing-up, relieved by proof and de-risking, not by more excitement.
  BANNED in the objection block: "now is the time," "don't miss," "the window is closing," "imagine if,"
  and any restatement of the value already made on page 1.

---

## 6. VERIFY-BEFORE-SEND (this mode has no automated gate - you are the gate)

Because Mode B renders flexible markdown via `build.py` (no `qa.py`), the QA is on you. Before sending, confirm:
- [ ] **Every number** is either input-grounded ("based on what you shared") or from `facts.md`. No bare modeled $/% dressed as measured.
- [ ] **Every account claim** (their spend, their pain, their stack) traces to the call/transcript or a CRM field - not memory. Mark any inference clearly or cut it.
- [ ] **Every objection answered is one that actually came up.** No invented objections.
- [ ] **The objection block de-risks, it does not re-sell** (the JOLT rule).
- [ ] **No em dashes; "carrier infrastructure" only; named references are real** (not invented to fill the proof slot).
- [ ] **The exec summary survives being read alone** by someone who was not on the call.
- [ ] **The MAP has owners + dates on both sides** and one clear next step.
- [ ] If a research-dependent slot could not be confirmed, it is left explicitly marked for the rep to fill, not guessed.

---

## 7. Build, QA, deliver, log

1. Copy `template.md` to `leave-behind-<account>.md`; specify the audience (§0); fill every section from the
   inputs (§1), dropping any section with no real input.
2. Run the VERIFY-BEFORE-SEND checklist (§6).
3. Render via `assets/build.py`: it builds from a `DOCS` registry, so add a leave-behind entry (the md filename
   + the cover tokens: `title`, `title_accent`, `segment_tag`, `segment_sub`, `subtitle`, `icon`) and run it, OR
   call the equivalent inline render steps per the main SKILL.md workflow. Either path strips the H1, auto-numbers
   eyebrows, styles the tables, wraps the cover, and renders the branded PDF via WeasyPrint.
4. Spot-check the PDF: `pdffonts` shows Tomorrow embedded; tables don't split mid-cell; no em dashes; 1-3 pages.
5. **Deliver + log:** send to the champion (the doc is built to forward). Note on the contact:
   `leave-behind sent: [file] re [call date] for [audience] YYYY-MM-DD`. An undelivered leave-behind is an invisible one.
