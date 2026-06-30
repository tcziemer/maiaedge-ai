# Direct Seller Onboarding Guide - Cowork Prompt (FINAL)

Paste the prompt below into a new chat inside the **Direct Selling** Cowork project. Attach the screenshots first (Instructions close-ups of the customizable parts, the Context panel, the Memory panel, the chat box / skill picker, and the full-project screen). Keep effort on Max. It builds the branded seller-onboarding PowerPoint.

---

You are building an internal training deck: "The MaiaEdge Direct Seller's Guide to Claude (Cowork)." This is the single resource that teaches our entire sales team how to use Claude. Treat it as a flagship deliverable.

IMPORTANT - HIGH STAKES, TAKE YOUR TIME. Every MaiaEdge AE will learn Claude from this deck, so it must be accurate, complete, and genuinely excellent. Do NOT rush or summarize from memory. SOURCE OF TRUTH: the maiaedge-ai folder attached to THIS project is the only place to read skills from, and it is the most current version - the skill copies uploaded to claude.ai may be older, so do not use them or describe skills from memory. Before you write each skill's slide, OPEN that skill's file in the attached maiaedge-ai folder (`skills/<skill-name>/SKILL.md`) and describe it from there - confirm what it actually does and which modes it currently has, so every description is correct and up to date. Verify the project mechanics (Instructions, Context, Memory, the chat-box controls) against the screenshots I attached and against `cowork-project-instructions/Direct-Seller-Project-Instructions.md`. Build the deck carefully, then re-read the whole thing for accuracy, clarity, and brand consistency before you finish. Quality over speed.

AUDIENCE: MaiaEdge account executives who are NEW to Claude. Write for a smart beginner. Plain language, no jargon, one idea per slide, lots of concrete examples. Every time you describe an action, show the exact words a seller would type. Assume they have never used an AI tool for selling before. The tone is encouraging and confidence-building.

=== BRANDING - MAKE IT LOOK LIKE MAIAEDGE ===
Before building, read the brand system at `skills/branded-doc/assets/brand-reference.md` in the attached maiaedge-ai folder and apply it to the deck:
- Palette: Gold #FFC200 (primary), Orange #FF9400 (accent), Black, Heather #D4D0C9 and Heather Tint #F4F2EE (warm neutrals). Use dark/black section covers with a gold accent plate; gold accents on headers and table header rows; plenty of white space.
- Font: Tomorrow (the .ttf weights are in `skills/branded-doc/assets/fonts/`). Use Tomorrow for headers and body. Embed it in the .pptx if you can; if embedding isn't reliable, set the font to Tomorrow and let it fall back to a clean sans.
- Visual language: doc-style section covers, eyebrow-numbered sections (01, 02, 03...), brand-styled tables, simple component cards for the example-prompt callout boxes.
- Logo: place the MaiaEdge logo from `skills/branded-doc/assets/logos/` on the title and closing slides.
- No em dashes anywhere (a MaiaEdge brand rule). Use periods or commas.

OUTPUT: A polished, on-brand PowerPoint (.pptx), roughly 40-50 slides, clean and readable (large headers, short bullets, a callout box for every example prompt). Use the screenshots I attached - place each on the matching slide and add labeled callouts/arrows pointing at the parts I describe. Where I reference a screenshot that isn't attached, leave a clearly-labeled placeholder box ("[SCREENSHOT: Memory panel]") so I can drop it in later. End with a one-page cheat sheet. If a pixel-perfect on-brand result is easier as a PDF (Tomorrow embeds cleanly through the branded-doc pipeline), also produce a branded PDF version using the branded-doc brand.css approach, but the PowerPoint is the primary deliverable.

Build the deck with these sections and content. Do not skip anything.

=== PART 1: WELCOME + THE ONE RULE ===
- Title slide: "Your AI Selling Copilot - The Direct Seller's Guide to Claude." MaiaEdge logo, brand cover.
- What Cowork is, in one sentence: a workspace where you chat with Claude and it does real selling work for you - research, writing, call prep, follow-ups - using MaiaEdge's own playbook.
- THE ONE RULE (big, memorable slide): Do all your selling work inside the "Direct Selling" project. It is pre-built with your voice, your territory, MaiaEdge's guardrails, and the entire company brain. Outside this project, Claude is generic. Inside it, Claude sells like a trained MaiaEdge AE.
- What you can do here (preview list): research an account, find a buyer's email + LinkedIn, write a cold email or LinkedIn note, batch-write outreach for a whole list, write the follow-up after they reply, build a one-pager to hook a meeting, prep for a call, recap a call into a leave-behind, check where a deal stands, generate an order form.

=== PART 2: SCREEN TOUR (use the full-project screenshot) ===
One slide that labels every part of the project screen:
- Instructions (top right): the standing brief that makes Claude act as your MaiaEdge AE. Always on.
- Context (right side): the company brain + any folders you attach.
- Memory (right side): your personal preferences Claude remembers.
- Scheduled: recurring tasks (optional, advanced).
- The chat box (center): where you type. Note the three controls - the skill picker, "Ask," and "Opus 4.8 / Max."
- Outputs: the files Claude makes for you (PDFs, docs).
- Recents: your past chats - click any to continue it.

=== PART 3: THE INSTRUCTIONS PANEL (use the Instructions screenshots) ===
- What it is: a standing set of directions, written once, that tells Claude how to be your AE copilot. You don't re-type it - it runs automatically on every chat in this project.
- What it controls: your sender identity + territory (who the email comes from), MaiaEdge's voice and writing rules, the guardrails (no em dashes, "carrier infrastructure" only, no credibility name-drops in cold outreach, the activity gate that stops you from emailing someone already in an active conversation), and which skill handles which request.
- WHAT YOU CAN CUSTOMIZE (the key slide - annotate the screenshots I attached of these sections): point at the spots where a seller sets their own preferences - e.g., name / territory / sender identity so emails write as them. Show how to edit: click the pencil icon on Instructions, change only those lines, save.
- WHAT TO LEAVE ALONE: the guardrails, the voice rules, and the skill routing. Changing those breaks the brand and the safety checks. If in doubt, don't edit - just tell Claude your preference in the chat or save it to Memory.

=== PART 4: CONTEXT - THE COMPANY BRAIN (use the Context panel screenshot) ===
- What Context is: the knowledge Claude pulls from. The "maiaedge-ai" folder = everything MaiaEdge knows - segments, messaging, product, competitive, signals, the HubSpot field setup, and all the skills.
- THE MAIN SETUP (do once): attach the maiaedge-ai folder to the project. Show: Context -> "+" -> select the maiaedge-ai folder. Once attached, every skill uses it automatically. You should see "maiaedge-ai" listed under Context (point at it in the screenshot).
- ONE-OFF PROJECTS / SPECIFIC DEALS: you can attach a SECOND folder alongside maiaedge-ai without removing it. Keep maiaedge-ai attached (the brain) AND add a folder for a specific job - a target account's documents, a prospect list, an event attendee export, an RFP. Claude uses both at once.
- How to add another folder: Context -> "+" -> pick the folder. Multiple folders can be attached at the same time. Remove the one-off folder when the job is done; keep maiaedge-ai always.
- Simple rule slide: "maiaedge-ai = always on. Extra folders = add when a specific deal or list needs them."

=== PART 5: MEMORY - YOUR PREFERENCES (use the Memory panel screenshot) ===
- What Memory is: things Claude remembers about YOU across every chat, so you don't repeat yourself.
- How to save: just tell Claude, starting with "Remember..." Show these seller examples in callout boxes:
  - "Remember I cover the Southeast region and always send as Ken Cunningham."
  - "Remember I want a LinkedIn connection note drafted alongside every cold email."
  - "Remember to keep my cold emails under 90 words."
  - "Remember my POCs run 60 days with written exit criteria."
- Where it shows: the Memory panel (point at it). It applies automatically going forward.
- Tip: use Memory for durable preferences; use the chat for one-time instructions.

=== PART 6: MODES, MODEL & EFFORT (use the chat-box screenshot) ===
- The skill picker (the dropdown by the "+"): pick a specific skill to focus the chat - OR just ask in plain English and Claude picks the right one. Beginners: just ask naturally.
- "Ask": the normal mode - you ask, Claude researches/writes/does it. This is what you'll use.
- "Opus 4.8 / Max": the model and how hard it thinks. Leave both as-is - Opus 4.8 on Max effort is the most capable setting and is right for research, writing, and call prep.
- Takeaway: "You almost never need to touch these. Type what you want; leave the settings on Opus 4.8 / Max."

=== PART 7: YOUR SKILLS - THE TOOLKIT ===
Intro slide: "You don't memorize commands. You ask in plain English and the right skill runs. Here's everything available, grouped by where you are in the deal." Then ONE slide per skill. Each skill slide MUST include: (a) what it does in one line, (b) when to use it, (c) its modes where relevant, and (d) a "Try saying" callout box with THREE different sample prompts a seller could type (vary the segment and situation). Confirm each description against the skill's `skills/<skill-name>/SKILL.md` in the attached maiaedge-ai folder (the current version - not any claude.ai upload) before writing. If a skill in this list isn't present in the attached folder, skip it and note it; if the folder has a seller-relevant skill not listed here, you may add a slide for it.

RESEARCH & TARGETING

- prospect-research - Fast pre-outreach research on one company + one contact (5-10 min). Pulls HubSpot + web + AI signals, and fetches the contact's verified email + LinkedIn URL from Apollo when you don't have them. Use right before writing an email or making a call.
  Try saying:
  1. "Research Equinix and their VP of Network Engineering before I reach out - get me their email and LinkedIn."
  2. "Quick research pass on a Tier 2 fiber operator I'm cold-emailing tomorrow - who's the right contact and what's my angle?"
  3. "Pull everything on CoreWeave and find me the infrastructure decision-maker's contact details."

- account-brief - The deep 10-section strategy brief for a high-value target (qualification, contact strategy, value mapping, technical fit, discovery prep). Pulls committee emails + LinkedIn URLs from Apollo.
  Try saying:
  1. "Build me a full account brief for Meijer."
  2. "Deep strategy brief on Lumen - I want the buying committee, our technical fit, and discovery prep."
  3. "Account brief for a regional colo I'm pursuing - include the value mapping and outreach drafts."

- contact-discovery - Maps the buying committee at an account and finds missing personas, pulling new contacts (with email + LinkedIn) from Apollo. Use to multi-thread.
  Try saying:
  1. "Who else should I be talking to at Lumen? Find the technical and economic buyers with their emails."
  2. "Map the buying committee at this neocloud - I only have one contact and need to multi-thread."
  3. "Audit our contact coverage at Equinix and tell me which personas we're missing."

OUTREACH (WRITE)

- cold-email - Angle-first cold email that sounds human, not templated. Needs a company + contact.
  Try saying:
  1. "Write a cold email to the VP of Infrastructure at CoreWeave."
  2. "Cold email to a fiber operator's network ops lead - lead with the off-net reach angle."
  3. "First-touch cold email to a colo provider about cloud on-ramp revenue."

- linkedin-outreach - A short LinkedIn connection note (under 300 characters).
  Try saying:
  1. "Write a LinkedIn connection note for that same person."
  2. "Short LinkedIn note to a neocloud CTO - keep it under 300 characters."
  3. "LinkedIn touch for a Tier 1 carrier exec - no pitch, just relevant."

- sdr-pipeline - End-to-end BATCH outreach for a whole LIST (not a single prospect). Give it a list of companies + contact titles; it pulls intel from HubSpot, fills gaps with web + Apollo, verifies each company's segment, checks for active conversations so you don't double-touch, writes a personalized 3-email sequence + LinkedIn note for each, and outputs a Smartlead-ready file. Use when you're working a batch.
  Try saying:
  1. "Here's a list of 20 fiber operators with target titles - run the full outreach batch and give me a Smartlead import."
  2. "Process this list of colo prospects into 3-email sequences + LinkedIn, ready for Smartlead."
  3. "Batch outreach for these 15 neocloud accounts - research, verify segment, write the sequences."

- copy-strategist - Critiques, scores, and rewrites a draft before you send it (modes: critique, score, rewrite, build a full sequence). Use when you wrote something and want it sharper.
  Try saying:
  1. "Here's my email - score it and rewrite it tighter."
  2. "Critique this 3-email sequence and tell me what's weak."
  3. "Make this cold email sound less like a template and more like me."

FOLLOW-UP & ADVANCE

- warm-follow-up - The next message after a prospect replies or accepts your connection. Paste the thread.
  Try saying:
  1. "They accepted my LinkedIn request - write the follow-up."
  2. "Here's their email reply - write my response."
  3. "A prospect said 'not right now' - write a graceful re-touch that keeps the door open."

- branded-doc - Branded PDFs across the whole funnel (a core seller tool). Modes: (1) meeting-hook one-pager that rides a connection-accept or reply, (2) post-call leave-behind / recap-and-path-forward your champion can forward internally, (3) segment assets - cheat sheet, battle card, use-case brief, business case.
  Try saying:
  1. "Make a one-pager for Nscale to send after they accepted my connection."
  2. "Turn my notes from the Orchest call into a leave-behind my champion can forward internally."
  3. "Build a business case for this colo prospect with the cloud on-ramp ROI numbers."

CALLS & DEAL

- call-prep - Discovery questions, talk tracks by persona, objection handling, and proof points before a call.
  Try saying:
  1. "Prep me for my discovery call with a Tier 2 fiber operator."
  2. "I have a demo with a neocloud tomorrow - give me talk tracks and the likely objections."
  3. "Call prep for a colo CFO - focus on the economics."

- call-analysis - Pulls the use cases, pain, MEDDPICC, and signals out of a logged call. Use after a call.
  Try saying:
  1. "Analyze my last call with Crusoe and tell me what to do next."
  2. "Pull the MEDDPICC and use cases out of my Meijer call."
  3. "What signals and pain came up across my last three calls?"

- pipeline-discipline - The 3-column board (accounts->POC, POC->PO, PO->expansion) showing where your deals actually stand and what's stuck.
  Try saying:
  1. "Show me my conversion board and what needs attention this week."
  2. "Which of my deals are stalling, and why?"
  3. "Where do my POCs stand against their exit criteria?"

- competitive-intel - Competitor positioning, objection responses, and battle cards. Use when a competitor comes up.
  Try saying:
  1. "They're comparing us to Megaport - how do I respond?"
  2. "Build me a battle card vs Equinix Fabric."
  3. "Prospect raised Lumen PCF - give me the positioning."

PAPER

- sales-docs - Generates an Order Form, MSA, POC Agreement, or NDA.
  Try saying:
  1. "Draft a 60-day POC agreement for this account."
  2. "Generate an order form for 2x 10G PBC at 25% off, 36-month term."
  3. "Create a mutual NDA for a new prospect."

PLUS
- Weekly signal scan output: each Monday a list of signal-fresh accounts to work lands for your territory. Try saying: "What are my hottest accounts to work this week?"

=== PART 8: PUTTING IT TOGETHER - FUNNEL PLAYBOOKS ===
Show the deal journey as simple flows, naming the skill at each step:
- Cold to meeting (one prospect): prospect-research -> cold-email + linkedin-outreach -> (they reply/accept) warm-follow-up -> (after accept) branded-doc one-pager -> meeting booked.
- Cold to meeting (a whole list): sdr-pipeline batches the research + 3-email sequences + LinkedIn for the entire list at once and hands you a Smartlead import - then warm-follow-up + branded-doc take over as replies come in.
- High-value target prep: account-brief -> call-prep.
- Meeting to deal: call-analysis (after the call) -> branded-doc leave-behind -> pipeline-discipline -> competitive-intel (if a competitor is in play) -> sales-docs (POC/order).
- Guided runs (mention): for a batch of cold accounts, follow the "Cold Outreach" run protocol; for a conference, the "Tradeshow" protocol - just say "run cold outreach for this list" or "help me with tradeshow follow-up for [event]."

=== PART 9: GET THE MOST OUT OF IT (best practices) ===
- Always name the account and the contact. Specifics beat vague.
- Let it research - it pulls HubSpot, the web, and Apollo. You don't have to gather data first.
- Say the goal and the stage ("this is a first cold touch" vs "they replied" vs "prepping a POC").
- Iterate - "make it shorter," "more technical," "warmer," "try a different angle."
- One task per chat. Start a fresh chat for a new account so context stays clean.
- Save good preferences to Memory so you stop repeating them.
- Grab your files from Outputs.
- When unsure which skill, just describe what you want - Claude routes it.

=== PART 10: CHEAT SHEET (final slide, brand cover) ===
A two-column "I want to ___ -> just ask ___" table covering: research an account, find someone's email/LinkedIn, write a cold email, write a LinkedIn note, batch-write outreach for a whole list, polish a draft, follow up on a reply, make a one-pager, prep for a call, recap a call, see my pipeline, handle a competitor, draft a POC/order, build a deep account brief.

Make it clean, encouraging, and skimmable, fully on the MaiaEdge brand. A nervous first-time user should finish this deck feeling like they can start selling with Claude today.
