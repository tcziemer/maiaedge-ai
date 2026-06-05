# LinkedIn Connection Message Rewrite — ITW 2026

## The Pattern (Non-Negotiable)

Every message follows this exact structure:

```
coming to itw? [one human sentence about why talking makes sense, based on their Email 1 angle]
```

That's it. Nothing else.

- **Opens with `coming to itw?`** — lowercase, every single message, no variation
- **No sender intro.** No "Tim from MaiaEdge." No "Ken from MaiaEdge." Nothing. Just `coming to itw?` and then the sentence.
- **One sentence.** Not two. Not three. One sentence that tells them why connecting is relevant to what they have going on right now.
- **Based on Email 1.** Each contact already has a personalized Email 1 in the data. The LinkedIn message distills that Email 1 angle into one tight sentence. The angle should match — if Email 1 is about provisioning speed, the LinkedIn sentence is about provisioning speed. If Email 1 is about fabric ownership, the LinkedIn sentence is about fabric ownership.
- **Human and light.** This is a LinkedIn connection request, not a pitch. It should feel like a real person saying "hey, I think this is relevant to you." Casual. Direct. Not salesy.
- **Under 300 characters total.** Hard limit. "coming to itw?" is 14 characters. That leaves ~285 for the sentence.

## What Good Looks Like

These are the vibe. Short, human, directly relevant:

- `coming to itw? we work with fiber operators on the provisioning bottleneck between deal signed and revenue flowing. i think it's relevant to what firstlight has going on.`
- `coming to itw? we help colo operators build their own interconnection fabric instead of handing tenants to a third party. feels relevant to where databank is heading.`
- `coming to itw? we solve the cross-carrier provisioning problem for operators managing upstream partners. seems like that's the world airespring lives in.`
- `coming to itw? edgeuno's expansion across latam raises a question we help operators answer: who controls the connectivity layer at each site. would be good to connect.`

## What Bad Looks Like

- `Tim from MaiaEdge. ITW's coming up. The provisioning bottleneck...` — NO. No sender intro. No "ITW's coming up."
- `coming to itw? your company is expanding and provisioning is hard.` — NO. Too generic. Could apply to anyone.
- `coming to itw? I noticed your recent expansion into three new states and wanted to...` — NO. "I noticed" is banned. Don't display research.
- `coming to itw? we're a carrier infrastructure company that helps operators...` — NO. Don't pitch MaiaEdge. The sentence is about THEIR situation, not ours.
- `coming to itw? Worth connecting?` — NO. Way too thin. The sentence needs substance.

## Rules

1. **All lowercase after `coming to itw?`** — the whole message is lowercase. This is intentional. It reads casual and human, not templated.
2. **No em dashes.** Use commas or periods.
3. **No "I noticed" / "I saw" / "I came across"** — banned.
4. **No flattery.** No "impressive growth." No "love what you're building."
5. **No competitor names.** Say "third-party fabric" not "Megaport."
6. **No customer names.** Anonymize any references.
7. **No credibility anchors.** No company history, no exits, no logos.
8. **No MaiaEdge feature pitching.** The sentence is about their world, not ours. You can reference what we do at a high level ("we help operators solve X") but keep it about them.
9. **Different contacts at the same company get different messages.** The Email 1 for each contact has a unique angle based on their role. A CEO's message should be different from their CTO's message, even at the same company.
10. **If Email 1 references a specific company situation (expansion, acquisition, new facilities, etc.), the LinkedIn sentence should reference the same situation** — but naturally, not as a fact-drop. "edgeuno's latam expansion raises a connectivity question we solve" not "you expanded to 14 sites across 7 countries."

## Input Data

Three JSON files in `/sessions/elegant-fervent-cray/`:

- `rewrite_tim_contacts.json` — 75 contacts (Tim Lieto's territory)
- `rewrite_ken_contacts.json` — 75 contacts (Ken Cunningham's territory)
- `rewrite_timothy_contacts.json` — 75 contacts (Timothy Ziemer's territory)

Each contact has:
- `row` — row number in the output XLSX
- `first_name`, `last_name`, `company`, `title`
- `email` — contact's email address
- `email1` — the full Email 1 text (this is the source for the angle)
- `current_message` — the current LinkedIn message (ignore this, write fresh)

## Output

Three JSON files:

- `/sessions/elegant-fervent-cray/rewrite_tim_results.json`
- `/sessions/elegant-fervent-cray/rewrite_ken_results.json`
- `/sessions/elegant-fervent-cray/rewrite_timothy_results.json`

Format per contact:
```json
{"row": 2, "first_name": "Kurt", "last_name": "Van Wagenen", "company": "Summit Broadband", "new_message": "coming to itw? ...", "chars": 156}
```

## Process

1. Read the contact JSON file
2. For each contact, read their `email1` field
3. Extract the core angle from Email 1 (what's the one problem or situation being named?)
4. Write a message: `coming to itw? [one sentence distilling that angle, human and light]`
5. Verify under 300 characters
6. Verify all lowercase (except proper nouns/company names — those can be capitalized or not, your call, but the rest is lowercase)
7. Verify no banned phrases, no em dashes, no sender intro
8. Save to the results JSON file

## After Saving Results

Update the XLSX files in the linkedin targets folder:

- `Tim_Lieto_LinkedIn_Outreach.xlsx`
- `Ken_Cunningham_LinkedIn_Outreach.xlsx`
- `Timothy_Ziemer_LinkedIn_Outreach.xlsx`

Write each contact's `new_message` into the "Connection Message" column, matched by row number.

## Quality Check

After updating, pull 10 random messages across all 3 files and print them for review. Verify:
- Every message starts with `coming to itw?`
- Every message is under 300 chars
- No sender intros anywhere
- No em dashes
- Messages are all lowercase (except maybe company names)
- Each same-company group has unique messages per contact
