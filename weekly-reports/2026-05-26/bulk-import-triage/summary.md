# Bulk Import Triage - 2026-05-26

## Trigger

Cooper accidentally bulk-uploaded 653 records into HubSpot today and asked for a light-touch review to flag obvious non-ICP records for deletion. Source file: `hubspot-crm-exports-my-companies-2026-05-26.csv`.

## Method

Pattern-matching classifier applied to name + domain + existing brief. No deep web research per Cooper's "light not deep" constraint. Aggression level: flag all non-ICP per Cooper's selection.

## Outcome

| Bucket | Count | Action |
|---|---|---|
| Protected ICP (5 records already classified ICP) | 5 | Left untouched. Includes ResetData (NeoCloud, hs_is_target_account=true), Xyntac (Network Op), 2 MSP/Aggregator, 1 Fiber Operator |
| Already Flagged for deletion | 11 | Left untouched |
| Tier 3 hold (brief indicates Cooper review pending) | 4 | Left untouched. Synnap + 3 others. R0/D7 will handle |
| **Flagged for deletion (written)** | **354** | `customer_segment = "Flagged for deletion"` via HubSpot MCP |
| Keep for research (R0/R1 will process tomorrow) | 279 | Left as blank-segment. Routines will classify |

## Guardrail audit (all clear)

- 0 records had `hs_is_target_account = true` in the today's-created cohort except ResetData (which was already in PROTECTED_ICP)
- 0 records had any associated deals
- 0 records = MaiaEdge own (124293230301)
- No closed-won customer protection triggers fired

## Delete bucket breakdown

| Reason | Count |
|---|---|
| Equipment / hardware vendor | 134 |
| Consultancy / professional services / integrator | 84 |
| UCaaS / CCaaS / CPaaS | 49 |
| Media / publishing / non-IT vertical | 28 |
| Telecom OSS/BSS software vendor | 24 |
| Consumer brand / MVNO retail / device retail | 14 |
| SaaS / non-telecom platform | 13 |
| Other-segment + brief confirms non-ICP | 4 |
| Gov / edu / mil domain | 4 |

## Execution

- 36 HubSpot MCP batches (10 records each, last batch 4). All returned `failed: 0`.
- Confirmation waived for session per Cooper's approval.
- No retries needed. No errors logged.

## Files

- `delete_candidates.csv` - 354 records flagged (record_id, name, domain, country, current_segment, delete_reason)
- `keep_for_research.csv` - 279 records left for R0/R1 to process

## Round 2 (deeper scan) - 2026-05-26 evening

Cooper asked for a second pass on the 279 "keep for research" bucket. Used industry knowledge + tighter heuristics + targeted manual classification.

### Round 2 outcome

| Bucket | Count | Action |
|---|---|---|
| Pattern-match DELETE (vendors, UCaaS, integrators, etc. I missed first pass) | 111 | Flagged via MCP |
| Manual DELETE after closer look at unknowns | 62 | Flagged via MCP |
| KEEP - genuine ICP (carriers, fiber operators, colos, rural telcos) | 21 | Left blank-segment for R1 |
| Stragglers (NOT_FOUND - already deleted/missing in HubSpot) | 2 | Skipped |

**Round 2 net: 173 additional flags written.**

### Round 2 KEEPs (21 confirmed ICPs - will be classified by R1 tomorrow)

Hilliary Communications, VERO Broadband, N+ONE DATACENTERS (Morocco), Phoenix Communications, S-NET Communications, TCT (Tri-County), TelePacific/TPx, Commnet Broadband, YouFibre (UK FTTH), Pineland Telco, Giant Communications (x2), Vero Fiber, SRT Communications, Home Telecom (SC ILEC), Grande Communications, Vyve Broadband, Glo Fiber Business, Mediacom Communications, KNET (Korea), Blue Mountain Networks.

### Round 2 DELETE highlights

- Defunct/legacy carriers (tw telecom, Broadwing, Advanced Fibre Communications)
- Equipment vendors I missed (Comba, Comtech Telecom, Tait, Intracom, BATM, Belden subs)
- VRS sign language services (Convo, Purple, Sorenson) - regulated relay, not MaiaEdge ICP
- LMR/public safety radios (Day Wireless, Mobile Communications America)
- Mobile retail/dealers (Planet Cellular, Cellular Advantage, Talk4less, Mobilelink dups)
- Defunct equipment (Carrier Access Inc, Hose McCann marine intercoms)
- CPaaS/UCaaS (Bird, Momentum Telecom, Vertical, White Label, Star2Star)
- Construction/staffing (Cannon Companies, BSB, ITG, Kelly Telecom)
- Non-profits (Telecom Infra Project, AOS, NCTA)

### Cumulative outcome (rounds 1 + 2)

| Bucket | Count |
|---|---|
| Round 1 flagged | 354 |
| Round 2 flagged | 173 |
| **Total flagged this session** | **527** |
| Already flagged before session | 11 |
| Confirmed ICP (rounds 1 + 2) | 5 + 21 = 26 |
| Tier 3 hold (Cooper review pending) | 4 |
| Remaining blank-segment (R1 will process) | ~85 (genuine telecom-named records without enough signal to classify) |
| **Total records in HubSpot ready to archive (Flagged for deletion)** | **~538** |

## Cooper's manual step

In HubSpot UI: Filter Companies by `customer_segment = "Flagged for deletion"` and archive. Should show ~538 records ready (354 round 1 + 173 round 2 + 11 pre-existing = 538).
