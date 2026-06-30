# CRM Guardian - Routine 6: Territory Sweep

Daily, 1:00 AM ET - runs FIRST each day so downstream routines operate on correct owners. **Single responsibility: keep account + contact OWNERSHIP correct per the territory model.** Validate HQ country/state, assign/correct `hubspot_owner_id` per the 5-region territory model (first-touch gated), and cascade the owner to associated contacts. Apollo is used only for state verification when a company is missing `state` or its enrichment is 120+ days stale.

## Revision history

- **2026-06-17 (rev. R7.1):** Territory map migrated **2-region East/West -> 5-region** (Northeast / Southeast / Central / West + Europe + International + Tier 1 SP + Unassigned) and a **first-touch owner-write gate** added so R6 matches the live keeper workflow (flow `4405143279`) and never reverts a manual rep placement. Map re-inlined from `context/hubspot/territory-model.md`. Scope unchanged from rev R7.0 (still territory-only).
- **2026-06-04 (rev. R7.0):** **Re-scoped to territory-only** (Cooper). Removed all non-territory work - deprecated-enum migration, `account_tier` fill, `company_sub_segment` surfacing, orphan-contact association, Mode 9 stale-NEW lead advancement, Mode 4/5/6 stale reporting, Mode 11 junk flagging, Step 5.5 tier + `signal_heat` recompute, and the entire Inlined Tier Compute Spec. Contact **segment** sync removed (contact **owner** cascade retained).

## Out of scope - moved OUT of R6 (rev. R7.0)

The following are **no longer performed here** and are re-homed elsewhere:

| Removed from R6 | Was doing | New home |
|---|---|---|
| Deprecated enum migration | `AI - Colocation Operator` -> `Data Center Colo Provider` | R1 / R2 |
| `account_tier` cascade fill | draining backlog @ 400/run | R-Tier-Audit (daily M-F) |
| Orphan-contact auto-association | draining backlog @ 300/run | R1 / R2 / crm-hygiene |
| Mode 9 stale NEW -> OPEN | draining backlog @ 1000/run | crm-hygiene (ad hoc) |
| Mode 4/5/6 stale + completeness score | reporting only | CRM Ops Daily Digest |
| Mode 11 junk-contact flagging | flagging hard bounces / spam | R5 / crm-hygiene |
| Step 5.5 tier + `signal_heat` recompute | per-touched-account | R-Tier-Audit covers drift |
| `company_sub_segment` surfacing | Tier 3 holds for R1/R2 | R1 / R2 |
| Contact segment sync | company segment -> contact | R1 / R2 |

**Connected tools:** HubSpot MCP, Apollo MCP (state verification only), Slack MCP (canvas Run-log append + failure ping only).

## Inlined Territory Model (2026-06-17 5-region)

Source: `context/hubspot/territory-model.md` (effective 2026-06-17, 5-region). The Claude Code runtime cannot resolve repo paths, so this map is inlined and is canonical for R6. It MUST stay in sync with `context/hubspot/territory-model.md`, the `territory-manager` skill, and the keeper workflow's `REGION_OF` / `REGION_OWNER` (flow `4405143279`). If any change, re-inline here and re-push the trigger via `RemoteTrigger.update` on `trig_01BmhnoyxFVrNXuqGcNnW6FV`. (Supersedes the old 2-region East/West map; that map, with no first-touch gate, would have reverted the 5-region migration.)

### Territory owners (the ONLY routing targets)

| Owner ID | Name | Region |
|---|---|---|
| 161889085 | Tim Lieto | Northeast + West (interim) |
| 162339176 | Ken Cunningham | Southeast |
| 165480917 | Tory Teague | Central |
| 164949459 | Markus Hendrich | Europe |
| 159350430 | Tim Ziemer | International + Tier 1 Service Provider (interim) |
| 160267902 | Cooper Kennedy | Unassigned catch-all |

### Resolution order: COUNTRY first, then US STATE

- **Europe -> Markus Hendrich `164949459`:** `country` (free-text `country` first, then `hs_country_code`) in geographic Europe ex Russia/Turkey (EU27 + EFTA/EEA + UK + microstates + non-EU Balkans incl. UA/BY/MD). A recognized foreign free-text `country` wins even if `hs_country_code = 'US'` (corrects mislabeled records).
- **International -> Tim Ziemer `159350430`:** any other non-US country, OR a US territory (PR/GU/VI/AS/MP). Russia, Turkey, the Caucasus (GE/AM/AZ), Kazakhstan, and Greenland route HERE, not Europe.
- **US state -> region -> region owner** (prefer free-text `state`, full name or 2-letter, over `hs_state_code` on conflict):
  - **Northeast (`161889085` Tim Lieto):** NY, VA, MA, NJ, OH, PA, MI, MD, CT, DC, DE, VT, WV, NH, RI, ME
  - **Southeast (`162339176` Ken Cunningham):** FL, IL, GA, NC, IN, MO, TN, KY, SC, AR, AL, MS, LA
  - **Central (`165480917` Tory Teague):** TX, CO, IA, MN, OK, KS, WI, NE, NM, ND, SD
  - **West (`161889085` Tim Lieto interim):** CA, WA, UT, OR, AZ, NV, MT, ID, WY, AK, HI
- **Unassigned -> Cooper `160267902`:** US with no usable state, OR neither country nor state usable.
- **Tier 1 Service Provider** is a manual region tag (owner Tim Ziemer `159350430` interim); never auto-derived from geography - leave Tier 1 SP / Ziemer-on-US owners alone (treat as a strategic exception).

### FIRST-TOUCH GATE (matches the keeper - Cooper's locked decision 2026-06-17: respect manual placements)

R6 WRITES `hubspot_owner_id` ONLY when the current owner is **unknown OR Cooper (`160267902`)**. If a rep already owns the record, R6 does NOT overwrite it, even if the record's geography maps to a different region owner - that record is SURFACED as a MISMATCH (rep-owned, geography disagrees) for human review, never auto-reverted. (Apollo/ladder state-fill below still runs regardless of the gate - filling a blank `state` is always safe and feeds both R6 and the keeper.)

### Non-territory members - R6 NEVER writes these as owner

Cooper Kennedy `160267902` (RevOps; also the unassigned catch-all per the gate), Kyle Blackwell `159701452` (Sales Engineering), Woody Acosta `162281129` (Sales Support). **Patrick Timmons `162774801`** and **Hannah Roberts `159875488`** are not territory owners - if either is found as an existing owner, treat as a strategic exception and SKIP.

## Run-Time Invariants

- **A. Timezone:** America/New_York.
- **B. Skip already-flagged:** exclude `customer_segment = "Flagged for deletion"` companies (Routine 4 owns them).
- **C. Customer protection:** closed-won companies are still re-routed if their owner is unknown OR Cooper (the first-touch gate still applies - a rep-owned closed-won record is left alone and surfaced as a MISMATCH, never auto-reverted).
- **D. Error containment:** per-record try/except. **Field Resolution Ladder web_fetch failure modes:** proxy block (HTTP 403 `host_not_allowed`) -> skip to ladder step 3 (not "unresolvable"); DNS NXDOMAIN / dead site -> continue ladder steps 3-4; timeout -> retry once w/ 5s backoff then skip; captcha/Cloudflare -> skip to step 3.
- **E. Default when uncertain:** state still blank after Apollo + ladder -> assign Cooper (`160267902`, Unassigned) and surface; never guess a territory owner.
- **F. Idempotency:** all writes idempotent; a second same-day run finds clean state.
- **G. Hard stops:** MaiaEdge's own record (ID 124293230301) - never modify. Strategic/named-account owners - skip.
- **H. Write authorization:** `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`. **Pre-authorized writes - ONLY these:** company `hubspot_owner_id` (first-touch gated), `state`, `country`; contact `hubspot_owner_id` (owner cascade). **Write nothing else.** Do NOT bump `last_enriched_date`. Do NOT touch `customer_segment`, `account_tier`, `company_sub_segment`, `signal_heat`, or `flagged_for_deletion`.
- **I. Dates via Bash:** compute the 120-day stale-enrichment boundary with the Bash tool (`date -d '120 days ago' +%s%3N`) - do NOT hand-compute epochs. No `git` commands.

## Workflow

### Step 0: Preflight

1. Call `apollo_users_api_profile` once. If `monthly_consumed >= 6000` or no headroom for >=5 credits, or the call fails -> set `apollo_skip = true` (state-resolution falls through to the Field Resolution Ladder), log it, continue.
2. Confirm HubSpot MCP is connected. If not -> send the hard-failure ping (`:red_circle: CRM Guardian - Territory Sweep ABORTED - HubSpot MCP unreachable.`), write the X Run-log row, exit.

NO `git pull` / `git fetch` / `git status`. Cross-run Apollo state lives in the on-disk run reports + Apollo's native `apollo_users_api_profile.monthly_consumed`. The Bash tool is available for non-git uses (e.g. date math).

### Step 1: Territory Audit (5-region, first-touch gated)

1. Pull all active companies (`customer_segment != "Flagged for deletion"`).
2. For each company, resolve the expected owner via the Inlined Territory Model above (COUNTRY first, then US STATE), then apply the first-touch gate:
   - **First-touch owner write:** if the current owner is **unknown OR Cooper (`160267902`)** AND geography is usable -> write the expected owner (Tier 1) and cascade contact owners (step 3). If a **rep already owns it** -> do NOT overwrite; if its geography maps to a different region owner, surface it under MISMATCH (rep-owned, geography disagrees) for human review. Never auto-revert a manual placement.
   - **Missing/blank `state` OR enrichment 120+ days stale** -> call Apollo `apollo_organizations_enrich` for `state`/`country` (skip if `apollo_skip`). Apollo is authoritative; write the refreshed `state` + `country`, then route per the model. (State-fill is always safe and runs regardless of the owner-write gate.)
   - **State still blank after Apollo -> Field Resolution Ladder (steps 2-4):**

     | Step | Source | Confidence -> Tier write | Cost |
     |---|---|---|---|
     | 2 | `web_fetch` on `https://[domain]` - footer + About + Contact page | HIGH -> Tier 1 | 1-3 web_fetch calls |
     | 3 | `web_fetch` on `https://www.linkedin.com/company/[slug]/about` Headquarters block | MEDIUM -> Tier 2 | 1 web_fetch |
     | 4 | `web_search` `"[domain] WHOIS registrant address"` -> registrant city/state | LOW -> Tier 3 surfaced | 1 web_search |

     Run in order; stop at the first HIGH/MEDIUM result. Do NOT skip step 2 to "save fetches" - the website is HIGH confidence and free of Apollo cost. Attribute the source per write in the report. Handle failure modes per Run-Time Invariant D.
   - **Still unresolved** after Apollo + ladder -> leave/assign **Cooper (`160267902`, Unassigned)**, cascade, add to the "Unassigned -> Cooper" list + ledger.
   - **Strategic/named-account exception** (incl. Tier 1 SP / Ziemer-on-US, Patrick Timmons, Hannah Roberts as existing owners) -> skip.
3. **Contact owner cascade:** for every company whose owner was set/corrected this run, write the same `hubspot_owner_id` to its associated contacts (Tier 1). Skip contacts associated to multiple companies (ambiguous - count only). Skip contacts under `Flagged for deletion` companies.

### Step 2: Coverage + Output

Compute **territory coverage** = % of active companies whose `hubspot_owner_id` matches their HQ-geography mapping (or are valid strategic exceptions / rep-owned MISMATCH-surfaced). Include in the report hero.

## Output (on-disk run report)

Write to `weekly-reports/YYYY-MM-DD/r6-territory-hygiene/run-report.md`.

- **Subject:** `CRM Guardian - Territory Sweep - [YYYY-MM-DD] - [N] owners set, [M] Unassigned -> Cooper, [K] MISMATCH surfaced` (or `All clean`).
- **Hero:** territory coverage %, first-touch owner writes, states resolved (by source: Apollo / website / LinkedIn / WHOIS), Unassigned -> Cooper count, rep-owned MISMATCH count, Apollo credits consumed (`N; monthly X / 6000`).
- **Owner writes (Tier 1):** company ID, old owner -> new owner, reason (region mapping / Apollo-refreshed state).
- **State resolutions:** company ID, resolved state, source attribution.
- **Unassigned -> Cooper:** company IDs assigned to Cooper for triage (no usable geography).
- **MISMATCH (rep-owned, geography disagrees):** company ID, current rep owner, geography-mapped owner - surfaced for human review, NOT auto-changed.
- **Strategic exceptions skipped** (for visibility).
- **Contact cascade:** count of contacts re-owned; ambiguous (multi-company) count.
- **Errors / API failures.**

## Caps & Budgets

- **Apollo:** soft 5 / hard 20 credits per run. Preflight gate per Step 0. Prioritize accounts with open deals, then unowned/Cooper-owned, then owner-mismatched. Hard-stop on `rate_limit`/`credit_exhausted` -> `apollo_skip = true`, continue with ladder.
- **HubSpot writes:** `manage_crm_objects.updateRequest`, **10 objects per call**, >=250ms between batches; split a company's contact cascade across multiple calls if >10 contacts. Backoff 1s->2s->4s on 429.
- **Deal-status checks:** use boolean `hs_is_closed_won` / `hs_is_closed_lost` (custom numeric pipeline IDs would be missed by `dealstage` string matching).
- No `git`. No tracker files. Cross-run state lives in the on-disk run reports + Apollo's native `monthly_consumed`.

## Cross-routine ledger

- **At run start:** read canvas `F0B0AFSB9LN` (`CRM Guardian - Open Items Ledger`) via `slack_read_canvas`. Drain this routine's items - resolve/remove any that now have a known owner; otherwise carry forward.
- **At run end:** append every NEW Unassigned -> Cooper hold to the ledger with `[YYYY-MM-DD]` date_first_surfaced; remove resolved ones. Persist via `slack_update_canvas`. Append ONE Run-log row:
  `| YYYY-MM-DD | CRM Guardian - Routine 6: Territory Sweep | <status emoji> | <one-sentence summary> | <artifact links> |`
  If the canvas is unreachable, log it in the run report and continue - do not abort.

## Delivery - quiet on success, ping only on hard failure

No per-run debrief DM. The record is the on-disk run report + the canvas Run-log row. The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work from HubSpot + the ledger. DM Cooper (`U0A24D9RJLS`, self-DM, `maia-edge.slack.com`) ONLY on hard failure (HubSpot/Slack/Apollo unreachable, abort, or zero records processed against a non-empty queue) as ONE line:
`:red_circle: CRM Guardian - Territory Sweep [FAILED/ABORTED] - [one-clause reason].`
Still write the matching X/warning Run-log row. Retry the ping once (1s->2s).
