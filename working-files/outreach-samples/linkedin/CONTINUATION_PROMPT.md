# LinkedIn Message Rewrite — ITW 2026 — Continuation Prompt

## Context

You are rewriting 225 LinkedIn connection messages for ITW 2026 pre-event outreach. These have been attempted 4 times and failed due to quality issues. This prompt exists because agents kept producing generic, formulaic garbage instead of reading each contact's Email 1 and writing a message specific to that company's situation.

**Do not use agents or parallelize message writing.** Process sequentially, one contact at a time, reading their Email 1 carefully before writing.

---

## The Pattern (Exact, Non-Negotiable)

```
coming to itw? [one lowercase human sentence about why talking makes sense based on their Email 1 angle]
```

That's the entire message. Nothing else.

- Opens with `coming to itw?` — lowercase, every message, zero variation
- No sender intro. No "Tim from MaiaEdge." No name. Nothing before `coming to itw?`
- One sentence after the opener. Sometimes two very short ones if needed for flow. But one tight idea.
- All lowercase (company names can go either way)
- Under 300 characters total. Hard limit.

---

## 15 Approved Messages (These Passed QA)

Study these. This is the quality bar. Every message you write should feel like it belongs in this list.

```
coming to itw? summit broadband's fiber buildout is moving but i'd guess the gap between routes lit and revenue flowing is where the real bottleneck lives. we help operators close that gap.

coming to itw? as edgeuno adds sites across latam, the operational question is who controls the tenant connectivity layer at each facility. we help operators keep that in-house.

coming to itw? edgeuno's growth is real but every new site means deciding whether the connectivity layer belongs to you or a third-party fabric. that decision compounds fast.

coming to itw? firstlight's speed advantage is real but i'd guess it doesn't extend past your own footprint yet. cross-carrier provisioning is a different animal. worth a conversation.

coming to itw? i'd guess firstlight's revenue side is moving faster than delivery as you expand into new markets. wholesale deals close but provisioning holds up the revenue. we solve that.

coming to itw? when airespring is competing for managed services deals, i'd guess your delivery timeline depends on whichever upstream carrier moves slowest. that's solvable.

coming to itw? integrating the telstra international portfolio means onboarding a whole new set of carrier connections across apac. i'd imagine the provisioning side of that is a heavy lift.

coming to itw? 1547 is scaling fast with greenfield builds and acquisitions. the question is how quickly each new facility starts generating connectivity revenue, not just filling cabinets.

coming to itw? globalinx isn't just a colo, it's a subsea landing station connecting international cables in virginia beach. that's a unique position and i think what we do is directly relevant.

coming to itw? 40 miles of dark fiber along the i-95 corridor between baltimore and nova is a serious asset. the question is how fast you monetize it. we help operators with exactly that.

coming to itw? at 60 hudson with 300+ carriers, the differentiator isn't who's in the building. it's how fast tenants can provision cross-connects and get services live. that's what we solve.

coming to itw? accelecom's expansion into eastern kentucky means new fiber where revenue sits idle until carrier interconnections go live. i'd guess that timeline is still months. we fix that.

coming to itw? south reach is expanding across florida and i'd guess the pressure isn't just building, it's monetizing fast. every new nni along those routes is still weeks before revenue flows.

coming to itw? gold data's 250 tbps capacity across the gulf of mexico is a serious asset. but the return depends on how fast carriers can provision onto those cables once they're lit. we help with that.

coming to itw? the clearwave combination is the right strategic move but the competitive advantage only shows up when you can deliver across the combined footprint. provisioning unification is the key.
```

### What makes these work:

1. **Company-specific.** Each one names the company and references something real about their situation (expansion, geography, acquisition, asset, competitive position).
2. **Email 1 angle distilled.** The message captures the CORE problem from Email 1, not a generic segment pain.
3. **Natural flow.** The sentence after `coming to itw?` reads like a thought someone actually had, not a template with variables swapped.
4. **Role-aware.** CEO messages lean revenue/competitive. CTO messages lean architecture/control. Ops messages lean visibility/speed.
5. **"i'd guess" / "i'd imagine"** used naturally when inferring, not asserting.
6. **Light close.** Some end with "we help with that" or "worth a conversation" — but it's woven into the thought, not bolted on.

---

## What Failed (4 Attempts — Do Not Repeat)

### Attempt 1: Broken pattern
```
Tim from MaiaEdge. Heading to ITW and saw New Horizon Communications.
```
WRONG: Has sender intro. Has "saw" (banned). Two disconnected sentence fragments.

### Attempt 2: Em dashes everywhere
```
ITW's coming up — provisioning timelines determine revenue velocity.
```
WRONG: Doesn't start with `coming to itw?`. Uses em dashes (banned). Generic.

### Attempt 3: Cookie-cutter agent output
```
coming to itw? provisioning timelines determine revenue velocity.
```
WRONG: Correct opener but GENERIC. This exact message appeared for multiple contacts at different companies. The agent didn't read Email 1s. There is zero company-specific content.

### Attempt 4: Ran out of context doing it right
Batches 1-2 (30 messages) were done manually and approved. Quality was correct. Session ran out of context before finishing.

**The lesson: the only approach that works is reading each Email 1 individually and writing a message that references the specific company situation described in that Email 1. No shortcuts. No batch-templating. No agents writing 75 messages in one shot.**

---

## Hard Rules

- No em dashes. Ever. Use commas or periods.
- No "I noticed" / "I saw" / "I came across"
- No flattery. No "impressive growth." No "love what you're building."
- No competitor names. "third-party fabric" not "Megaport"
- No customer names. Anonymize references.
- No credibility anchors. No company history.
- No MaiaEdge feature pitching. The sentence is about THEIR world. You can say "we help operators solve X" or "we solve that" but keep it about them.
- No sign-offs. No "best" or "cheers."
- Different contacts at the same company MUST get different messages. The CEO cares about revenue/competitive position. The CTO cares about architecture. The VP Ops cares about visibility/control. Even at the same company, the angle shifts by role.

---

## Input Files

Three JSON files in `/sessions/elegant-fervent-cray/`:

| File | Sender | Count |
|------|--------|-------|
| `rewrite_tim_contacts.json` | Tim Lieto | 75 |
| `rewrite_ken_contacts.json` | Ken Cunningham | 75 |
| `rewrite_timothy_contacts.json` | Timothy Ziemer | 75 |

Each contact object:
```json
{
  "row": 2,
  "first_name": "Kurt",
  "last_name": "Van Wagenen",
  "title": "CEO",
  "company": "Summit Broadband",
  "email": "kurt.vanwagenen@summitbb.com",
  "email1": "[full Email 1 text — THIS IS YOUR SOURCE FOR THE ANGLE]",
  "current_message": "[ignore this — it's the bad message being replaced]"
}
```

**The `email1` field is the ONLY thing that matters.** Read it. Find the company-specific angle. Distill it into one sentence.

---

## Already Completed (Do Not Redo)

Tim contacts rows 2-31 (contacts 1-30) are DONE. Approved messages saved in:
- `/sessions/elegant-fervent-cray/tim_batch1.json` (rows 2-16)
- `/sessions/elegant-fervent-cray/tim_batch2.json` (rows 17-31)

**Start with Tim row 32 (contact 31).**

---

## Processing Instructions

### Batch size: 15 contacts

Process 15 contacts at a time. For each contact:

1. **Read their `email1` field.** Actually read it. The whole thing.
2. **Identify the angle.** What is the ONE specific thing about this company that Email 1 is built around? (expansion, acquisition, new facilities, subsea cables, multi-carrier management, fabric ownership, etc.)
3. **Consider their role.** How does their title change what matters? CEO = revenue/competitive. CTO = architecture/control. VP Ops = visibility/speed. Sales = ability to deliver.
4. **Write the message.** `coming to itw? [one sentence distilling the angle through the lens of their role]`
5. **Check:** Under 300 chars? All lowercase? No em dashes? No banned phrases? Company-specific? Different from other contacts at same company?

### After each batch of 15:

Save the batch to a JSON file:
```
/sessions/elegant-fervent-cray/[sender]_batch[N].json
```

Format:
```json
[
  {"row": 32, "msg": "coming to itw? ..."},
  {"row": 33, "msg": "coming to itw? ..."}
]
```

### Processing order:

1. Tim contacts 31-75 (rows 32-76) — 3 batches of 15
2. Ken contacts 1-75 (rows 2-76) — 5 batches of 15
3. Timothy contacts 1-75 (rows 2-76) — 5 batches of 15

That's 13 batches total, 195 new messages.

### After ALL messages are written:

Update the 3 XLSX output files in:
`/sessions/elegant-fervent-cray/mnt/ITW/final contact lists/cold contacts/emails processed/final smartlead imports/linkedin targets/`

- `Tim_Lieto_LinkedIn_Outreach.xlsx` — Column G ("Connection Message"), rows matched by row number
- `Ken_Cunningham_LinkedIn_Outreach.xlsx` — same
- `Timothy_Ziemer_LinkedIn_Outreach.xlsx` — same

Tim's file needs ALL 75 messages written (batches 1-2 from the saved files + batches 3-5 from this session).

### Final quality check:

Pull 15 random messages (5 from each sender file) and display them. Verify the pattern, character count, and company-specificity.

---

## The Quality Test

For every message, ask yourself: **"If I removed the company name, could this message have been sent to any other company?"**

If yes, the message fails. Rewrite it.

The whole point is that each message makes the recipient think: "this person actually knows what my company is dealing with right now." That only happens when the message references their specific situation, not generic segment pain.
