# CRM Guardian Improvement Plan — 2026-04-27

Source: review of the 5 actual runs in `enterprise/crm-guardian/` and `enterprise/crm-guardian/reports/` against the routine prompts in `Claude routine prompts/`.

The runs we have (Hygiene 2026-04-24, Job 2 2026-04-24, Territory 2026-04-24, Job 5 2026-04-24, Manual enrichment 2026-04-27) are mostly pre-split (legacy monolithic job 1/2/3/5) and one post-split manual run. The 9 numbered routines exist as prompts but most haven't done a full production cycle yet. This plan strengthens them BEFORE the first full week of scheduled runs so we don't bake in the pre-split pattern of "find work, list work, defer work."

---

## Themes from the runs

1. **Routines find work but don't act.** Hygiene found 47 high-confidence merges → wrote 0. Job 5 found 5 Apollo-verified persona candidates → created 0 contacts. Job 2 had 184 candidates → enriched 6.
2. **Bad import data is treated as salvageable.** "BCN" at `bcnhouston.com` (restaurant), "EXA" at `exabeauty.com` (insect farm), "Deutsche Telekom NA" at `dtna.com` (Daimler Trucks). Enrichment renames them downstream rather than blocking upstream.
3. **Apollo fallback gives up too early.** 3/3 state-fills returned null → "manual research" without trying website footer / LinkedIn About / WHOIS.
4. **ROI inversion.** Cooper had to manually exclude 78 already-classified-as-Other records (Cisco, Meta, Dell, IBM Cloud) before the 2026-04-27 run — routines don't pre-score the candidate pool.
5. **No carry-forward.** The same 9 hard-delete records, 47 unmerged dupes, 5 Apollo persona candidates show up in successive reports unactioned.

---

## Six changes, sequenced by risk × leverage

| # | Change | Touches | Risk | Leverage |
|---|--------|---------|------|----------|
| 1 | Persona Fill auto-create on HIGH-confidence Apollo+LinkedIn match | Routine 8 | Low | High (5+ contacts/week shipped, currently 0) |
| 2 | Apollo→website→LinkedIn→WHOIS fallback ladder | Routines 1, 2, 6 | Low | Medium (recovers 70%+ of Apollo nulls) |
| 3 | Routine 0 — Import Validator (new) | New routine + crm-guardian SKILL.md + build.sh | Medium | High (kills the upstream leak) |
| 4 | Pre-score triage on Routines 1 + 2 candidate pools | Routines 1, 2 | Low | High (doubles effective Apollo budget) |
| 5 | Routine 6 actually drains hygiene findings (stale NEW leads, orphaned contacts, 9.8K aged leads) | Routine 6 | Medium | Medium (one-time cleanup of 9.8K + 995) |
| 6 | Slack canvas as cross-routine ledger | All routines + crm-guardian SKILL.md | Medium | Medium (accountability, not throughput) |

---

## Phase 1 — Persona Fill auto-create (Change 1)

**Goal:** Routine 8 ships 5-15 verified Apollo+LinkedIn contacts per Friday run instead of zero.

**Diff to `Claude routine prompts/crm-guardian-routine-8-weekly-persona-fill.md`:**

- The routine spec already authorizes Tier 2 auto-create on `verified email + current employment + LinkedIn confirms current at target`. It's correct on paper. The 2026-04-24 run punted because the Apollo `mixed_people_api_search` returned **obfuscated last names** and **no LinkedIn URLs** — and the routine treated that as "needs Cooper review."
- **Fix:** explicitly chain the two-step Apollo flow in step 3: (a) `apollo_mixed_people_api_search` to find candidates (free, returns obfuscated names), then (b) `apollo_people_match` (1 credit each) to reveal email + LinkedIn URL on each shortlisted candidate. Reveal is the credit cost the routine was avoiding — but at 5-15 reveals/week × 4 weeks × ~4 credits = ~250 credits/month, well under the 1,075/month sub-cap.
- Add explicit text: *"Apollo `mixed_people_api_search` results with obfuscated names are NOT a Tier 3 trigger — they are the EXPECTED first step. Reveal via `apollo_people_match` is part of the Tier 2 auto-create path, not Cooper review."*
- Update step 3 sub-flow:
  1. `mixed_people_api_search` → top 3 candidates per persona slot
  2. `apollo_people_match` on the top candidate → reveal email + LinkedIn URL
  3. `web_fetch` LinkedIn URL → confirm current employment
  4. Apply suppression check (existing)
  5. Auto-create at Tier 2 if all green; fall through to candidate #2 only if LinkedIn says departed/private

**Validation:** first scheduled Friday run after deploy. Success = 3+ contacts created, 0 silent punts on candidates that had verified Apollo emails. The 5 candidates listed in `reports/job5_persona_fill_2026-04-24.html` (Inference.net, Akash Network, Lancium, CenturyLink, HTC) become the first-run check — they should land as new contacts.

---

## Phase 2 — Apollo fallback ladder (Change 2)

**Goal:** When Apollo returns null on `state` / `country` / `email`, the routine MUST try 3 fallbacks before flagging manual.

**The ladder (codify in `skills/company-enrichment/SKILL.md` Stage 1 and reference from each routine):**

1. Apollo `apollo_organizations_enrich` (or `apollo_people_match` for contacts)
2. `web_fetch` company homepage → look for footer address / Contact page / About page
3. `web_fetch` `linkedin.com/company/{slug}/about` → headquarters location
4. `web_search` `"{domain}" WHOIS registrant` → registrant address (last resort, low-confidence)

**Diff:**

- `skills/company-enrichment/SKILL.md` — add a "Field Resolution Ladder" subsection under Stage 1 documenting the four steps and their confidence levels (Apollo=HIGH, website=HIGH, LinkedIn=MEDIUM, WHOIS=LOW).
- `Claude routine prompts/crm-guardian-routine-6-territory-hygiene.md` — replace the current "Apollo state still blank → Tier 3 hold" with "Apollo blank → run Field Resolution Ladder steps 2-4. If still blank after step 4 → Tier 3 hold."
- Same edit to Routine 1 step 7 (territory derivation) and Routine 2 step where state is re-derived.

**Validation:** the 3 records that returned null in the 2026-04-24 territory run (Shaun Telecom, Surf USA Mobile, kiocompany.com) should resolve — Surf USA Mobile has a +1-866 phone number (Apollo returned), suggesting US presence; their website should disclose state.

**Cost:** ~2-4 web_fetch calls per Apollo null. No Apollo credits. Adds <30 seconds per affected record.

---

## Phase 3 — Routine 0 Import Validator (Change 3, new routine)

**Goal:** Kill records like "EXA" at `exabeauty.com` (insect farm), "BCN" at `bcnhouston.com` (Houston restaurant), "Deutsche Telekom NA" at `dtna.com` (Daimler Trucks) BEFORE Routine 1 wastes Apollo credits enriching them.

**New file: `Claude routine prompts/crm-guardian-routine-0-import-validator.md`**

- **Cadence:** Daily, 12:30 AM ET (runs first, before Routine 6 at 1 AM so territory/hygiene doesn't waste cycles on garbage)
- **Scope:** Companies created in the last 24h where `last_enriched_date IS EMPTY` (i.e., haven't been touched yet)
- **Workflow per record:**
  1. `web_fetch` the domain root + `/about` + `/contact`
  2. LLM check: does the entity at the domain plausibly match the HubSpot company name? (e.g., "Deutsche Telekom NA" vs domain showing "Daimler Trucks NA" = MISMATCH)
  3. Three outcomes:
     - **Match (HIGH confidence):** no action, fall through to Routine 1's normal enrichment path
     - **Name mismatch but legitimate business at domain (HIGH confidence):** auto-rename HubSpot record to the domain entity's name (Tier 1) + log
     - **Domain serves a non-business or completely-unrelated business (HIGH confidence):** auto-set `customer_segment = "Flagged for deletion"` + write `account_brief` reason field with the discovered entity (Tier 2 auto + flag)
     - **Unclear (MEDIUM/LOW confidence):** Tier 3, leave for Cooper
- **Hard categories that auto-flag for deletion** (no Cooper review needed): apparel/retail, restaurants, churches, schools, government tribes, blockchain/crypto unless explicitly NeoCloud-adjacent, agriculture/farming, healthcare clinics, law firms, real estate brokerages, automotive/trucking manufacturers, consumer electronics distributors
- **Caps:** 100 records/run (typical import volume is 0-30/day; spike absorption built in)
- **No Apollo:** website-only, free
- **Slack DM:** `:warning: *CRM Guardian — Import Validator* — [date] — [N] renamed, [M] flagged for deletion, [K] held for review`

**Diffs to existing files:**

- `skills/crm-guardian/SKILL.md` — add Routine 0 to the Execution Model table (line ~17), update daily run order to `0 (12:30 AM) → 6 (1 AM) → 3 (2 AM) → 4 (3 AM) → 1 (6 AM) → 2 (8 AM)`. Update Apollo budget table (Routine 0 uses 0 credits).
- `CLAUDE.md` — add Routine 0 row to the CRM Guardian section
- `build.sh` — no change (routine prompts aren't built; they're scheduled via the routine platform)
- Routine 1 prompt — add note: "Records flagged by Routine 0 earlier this morning are out of scope (covered by the `customer_segment != 'Flagged for deletion'` filter already in the trigger query)."

**Validation:** seed test by manually running on the 9 hard-delete candidates from the 2026-04-27 run (`littlecrusoe.com`, `crusoesurvival.com`, `exabeauty.com`, `bcnhouston.com`, `t-shirtwholesaler.com`, `vibrantchurchcommunications.com`, `dtna.com`, `toptel.pl`, `ledgerofearth.com`). All 9 should auto-flag.

---

## Phase 4 — Pre-score triage on Routines 1 + 2 (Change 4)

**Goal:** Stop spending Apollo credits on records that the LLM can classify as non-ICP from name+domain alone.

**Diff to Routines 1 and 2 (insert as new step 0 in the workflow):**

```
0. Pre-score triage:
   - For the candidate batch (up to 100 records), run a single LLM pass with
     name + domain only.
   - Bucket each record:
     - LIKELY_ICP: continue to full enrichment pipeline (steps 1-7)
     - LIKELY_NON_ICP: skip Apollo entirely; classify via segment-classification
       qualification gates using domain-only signals; write segment + tier 5
       at MEDIUM confidence; consume 0 Apollo credits
     - LIKELY_JUNK: defer to Routine 0 (will pick up tomorrow)
   - Surface bucket distribution in the Slack DM hero so Cooper sees the
     triage decisions.
```

**LIKELY_NON_ICP heuristics (domain-only):**
- TLDs: `.gov`, `.edu`, `.mil`, `.org` for non-telecom non-profits
- Keywords in domain: `church`, `school`, `university`, `clinic`, `dental`, `realestate`, `restaurant`, `apparel`, `consulting` (most cases), `lawfirm`
- Apollo industries (if available from prior partial enrichment): retail, hospitality, agriculture, religious organizations

**LIKELY_JUNK heuristics:**
- Domain TLD `.tk` `.ml` `.ga` (free domain TLDs, rarely real businesses)
- Spoofed brand domains (e.g., `littlecrusoe.com`, `crusoesurvival.com` — domain doesn't resolve to a known org but contains a brand name)
- Domain is parked / for-sale page

**Validation:** re-run Routine 1 against the 184 candidates from 2026-04-24. Expected: ~120 LIKELY_NON_ICP fast-classified at 0 Apollo credits, ~50 LIKELY_ICP enriched, ~14 LIKELY_JUNK deferred to Routine 0. Compare to actual run which only enriched 6.

---

## Phase 5 — Routine 6 drain mode (Change 5)

**Goal:** The 2026-04-24 hygiene run found 9,811 stale-NEW contacts, 995 orphaned contacts, 1,451 records missing `account_tier`, 748 missing `company_sub_segment`. None acted on. Routine 6 needs an explicit drain mode.

**Diff to `Claude routine prompts/crm-guardian-routine-6-territory-hygiene.md`:**

- **Stale NEW leads:** Tier 1 auto-advance `hs_lead_status` from `NEW` to `OPEN` for any contact where `createdate > 14 days ago AND hs_lead_status = NEW AND no sales activity`. Cap 500/run (drains 9.8K backlog in ~20 days).
- **Orphaned contacts:** Tier 2 — for contacts with no company association and email domain matching an existing HubSpot company, auto-associate. Cap 200/run. The remaining (995 - matched) stays in Tier 3 report.
- **Missing `account_tier` (1,451 records):** these are records where segment is set but tier wasn't derived. Tier 1 auto-fill via segment-classification cascade rules. Cap 200/run (drains 1,451 in ~8 days).
- **Missing `company_sub_segment` (748 records):** same Tier 1 cascade fill. Cap 200/run.
- All four drains share a combined 1,000 writes/run cap (well under HubSpot's 250K/day rate limit).

**Validation:** day 1 should ship ~1,000 writes; subsequent days drain steadily until the backlogs are 0.

---

## Phase 6 — Slack canvas ledger (Change 6)

**Goal:** Stop the same items showing up unactioned across multiple reports. One persistent surface every routine reads at start and writes to at end.

**Approach:** A single Slack canvas in Cooper's DM, named `CRM Guardian — Open Items Ledger`. Use `slack_create_canvas` once (manual seed), then `slack_read_canvas` + `slack_update_canvas` from each routine.

**Canvas structure:**
```
# CRM Guardian Open Items — Updated [timestamp]

## Tier 3 Holds (need Cooper)
- [routine] [date_first_surfaced] [record_id] — [reason]
- ...

## Apollo Reveals Pending (Routine 8)
- [account] [persona_slot] [apollo_id] [date_first_surfaced]
- ...

## Hard-Delete Recommendations (Routine 0)
- [record_id] [domain] [discovered_entity] [date]
- ...

## Cooper-Decided Divergent Dupes (Routine 3)
- [primary_id] vs [other_id] — [domain] — [recommendation]
- ...
```

**Each routine's contract:**
1. **At start:** read the canvas, drain its own previously-surfaced items first (they're the priority pool, not new work)
2. **At end:** append any new items it can't auto-resolve, with `[date_first_surfaced]`
3. **Auto-cleanup:** items older than 30 days get demoted to a "Stale — Cooper, decide or close" section

**Diffs:**
- `skills/crm-guardian/SKILL.md` — new section "Cross-Routine Ledger" describing the canvas contract, after "Cascade Logic"
- Each routine prompt — add step "0a. Read ledger, drain any items belonging to this routine first" and "Final step: append new Tier 3 holds to ledger"

**One-time setup:** Cooper runs `mcp__claude_ai_Slack__slack_create_canvas` to seed the canvas, captures the canvas ID, and Cooper updates each routine prompt with the canvas ID.

**Validation:** after 1 week of scheduled runs, the canvas should show open items decreasing day over day rather than accumulating.

---

## Rollout sequence

| Week | Phase | Files changed | How to verify |
|------|-------|---------------|---------------|
| 1 | Phase 1 (persona auto-create) | `crm-guardian-routine-8-weekly-persona-fill.md` | Friday run creates 3+ contacts |
| 1 | Phase 2 (Apollo fallback ladder) | `skills/company-enrichment/SKILL.md`, Routines 1/2/6 | Daily territory run resolves 70%+ of Apollo nulls via fallback |
| 2 | Phase 3 (Routine 0) | NEW routine prompt, `skills/crm-guardian/SKILL.md`, `CLAUDE.md` | First daily run flags 5-15 import-leaked records |
| 2 | Phase 4 (pre-score triage) | Routines 1, 2 | Routine 1 enriches 50+/day instead of 6/day |
| 3 | Phase 5 (Routine 6 drain mode) | Routine 6 | Stale NEW backlog drops from 9.8K to <5K within 7 days |
| 3 | Phase 6 (Slack ledger) | All routines, `skills/crm-guardian/SKILL.md` | Canvas exists, all routines read/write, items decrease w-o-w |

**Sequencing rationale:**
- Phase 1 + 2 first: lowest-risk, both are within-routine tweaks, both ship measurable scale immediately
- Phase 3 next: needs new scheduling but no other routine changes — isolated risk
- Phase 4 builds on Phase 3 (LIKELY_JUNK routes to Routine 0)
- Phase 5 is the heaviest lift (5 modes touched) — saved for after the Apollo improvements have proven the routines fire reliably
- Phase 6 is last because it depends on routines being mature enough that what they surface is trustworthy

---

## What this plan does NOT change

- **Routine 3 (duplicate accounts):** already does Tier 1 auto-flag-after-reassociation correctly per its prompt. The 47 unmerged dupes from the 2026-04-24 hygiene run were from the legacy monolithic job, which is no longer the production path. Routine 3's first scheduled run should drain them. **Validation step before Phase 1:** confirm Routine 3 ran cleanly at least once and the 2026-04-24 dupe list is mostly resolved. If not, reopen Phase 0.
- **Routine 4 (flagged consolidation):** existing logic is sound, no change needed.
- **Apollo monthly cap (6,000 credits):** stays. The improvements above shift WHERE credits are spent (high-ROI ICP records, persona reveals) without raising the ceiling.
- **HubSpot-native company merge:** still out of scope. MCP doesn't expose a merge endpoint. Reassociate-and-flag-loser is the correct pattern.

---

## Open questions for Cooper

1. **Routine 0 placement:** 12:30 AM ET (before everything) vs 5:30 AM ET (after dedup, before enrichment)? My recommendation is 12:30 AM because Routine 6's Apollo state-verifications would otherwise burn credits on junk records. Confirm.
2. **Phase 5 drain caps:** I proposed 500 stale NEW leads/run and 200 each for orphaned/tier/sub-segment fills. Want more aggressive (drain in 3-5 days) or more conservative (drain in 30 days)?
3. **Slack canvas seed:** want me to run `slack_create_canvas` to seed the ledger now, or wait until Phase 6?
4. **Routine 0 hard-flag categories:** the list above (apparel, restaurants, churches, etc.) is a starting set. Any categories I should add or remove based on what's been showing up in your import sources?
