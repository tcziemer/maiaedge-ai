CRM Guardian - Stale Re-Enrichment - 2026-06-16 - 0 Tier 2 flagged, 0 Tier 3 held (new)

Run summary: 39/100 processed · Filter C pre-spread (A=0 / B=0 / C=39 of 45 pulled) · LIGHT re-stamp x39 · Tier 1: 0 / Tier 2: 0 / Tier 3 new: 0 · Apollo: 0/50 used (W25 2/850, 848 remaining) · Freshness: GREEN

What needs Cooper's attention:
- 6 standing Tier 3 holds carried, all R3/Cooper/D7 scope (NOT R2-owned) - see table below. No drift since 2026-06-15; none resolved by Cooper this run.
- WATCH: MMR Fiber (175221473010) + team.telstra (316598423243) were last enriched 2026-02-24, so they cross the 120-day line into Filter A on 2026-06-24 (~8 days out). Both are blocked on dedup / entity-split decisions R2 cannot make autonomously. If R3/Cooper don't act, they will surface as genuinely-stale next week and R2 still won't be able to action them - recommend resolving the dedup/split before 06-24.
- 0 eviction Tier 2, 0 segment transitions, 0 partial enrichments (gate failures), 0 recent-news staleness clears.

Run health: GREEN

Errors: None.
Operational note: the bash sandbox mount served a STALE, truncated snapshot of weekly-reports/apollo-budget.json (205 lines, history array unterminated, missing R1's 2026-06-16 10am entry). Host file verified complete + valid via the Read file tool (214 lines incl. R1 06-16). This is the known "sandbox mount stale-JSON illusion" (memory note; prior 06-04 / 06-08 "corruption" incidents). The R2 06-16 history entry was appended host-side via the Edit tool, NOT via bash, to avoid clobbering R1's entry. A junk backup apollo-budget.json.bak-20260616-r2 (copy of the stale mount view) was created by the initial bash attempt and could not be removed via the sandbox (Operation not permitted) - harmless, consistent with prior-run .bak leftovers (06-08, 06-15); cosmetic cleanup only.

---

## Context

Today=2026-06-16 (Tue), 120-day cutoff=2026-02-16. Active not-yet-stale pool = 3,390 companies. The entire active pool was enriched in the compressed May 2026 migration + Mass Re-Enrichment window, so Filter A (stale 120+) and Filter B (never-enriched + segment) remain empty in steady state; the oldest cohort is still dated 2026-02-24 (8 days from crossing 120d). Filter C rotation pre-spread is doing the real work - re-stamping the oldest not-yet-stale records to stagger their next due-date away from the late-Aug/Sept 120-day cliff. This is the 8th consecutive Filter-C pre-spread run.

## Bucket distribution (45 pulled, sorted last_enriched_date ASC)

- 6 RE_ENRICH (standing holds, carried - no action): the genuinely-oldest records (enriched 2026-02-24 to 2026-04-27), each blocked on an R3/Cooper/D7 decision R2 does not own.
- 39 RE_ENRICH_LIGHT (pre-spread re-stamp): well-briefed 2026-05-01 Partner Target / Other ecosystem references. All re-affirmed against their existing (coherent, recent) briefs; classifications stable for well-known stable entities (major SIs, OEMs, distributors, hyperscalers, REITs, power/silicon vendors). Re-stamped last_enriched_date=2026-06-16 + signal_heat=Cold backfill. tier no-op (non-ICP, compute_tier Step A0 guard). These were NOT re-researched from scratch - they are recently-enriched (6 weeks), not stale; the pre-spread's purpose is load-smoothing, not re-classification.

## Pre-spread re-stamps (39 records, last_enriched_date 2026-05-01 -> 2026-06-16, signal_heat=Cold)

| ID | Name | Segment | Tier |
|---|---|---|---|
| 301885614814 | Accenture | Partner Target | tier_5 |
| 302074641116 | ESR | Other | tier_5 |
| 301889214186 | World Wide Technology | Partner Target | tier_5 |
| 302067443441 | IBM Cloud | Other | tier_5 |
| 301889214183 | Tata Consultancy Services (TCS) | Partner Target | tier_5 |
| 302011678403 | Mapletree Industrial | Other | tier_5 |
| 277215229688 | UST | Other | tier_5 |
| 300362241756 | Marvik | Partner Target | tier_5 |
| 300408171208 | Teradata | Partner Target | tier_5 |
| 300329661170 | Check Point | Partner Target | tier_5 |
| 300347781881 | GE VERNOVA | Partner Target | tier_5 |
| 300408171215 | CDW | Partner Target | tier_5 |
| 300408171210 | onsemi | Partner Target | tier_5 |
| 301784665787 | Solidigm | Partner Target | tier_5 |
| 300724801225 | Synopsys | Partner Target | tier_5 |
| 300724801224 | Sanmina | Partner Target | tier_5 |
| 301862123197 | ASUS | Partner Target | tier_5 |
| 301862123200 | SK hynix | Partner Target | tier_5 |
| 301784665795 | EXL | Partner Target | tier_5 |
| 301784665789 | Arrow | Partner Target | tier_5 |
| 301874839280 | HPE | Partner Target | tier_5 |
| 301878429386 | Red Hat | Partner Target | tier_5 |
| 301874839279 | MSI | Partner Target | tier_5 |
| 301862123195 | Foxconn | Partner Target | tier_5 |
| 301784665790 | Ingram Micro | Partner Target | tier_5 |
| 301874839277 | Eaton | Partner Target | tier_5 |
| 311386968767 | Ornn AI | Other | tier_5 |
| 311425345220 | CloudAdvise | Other | tier_5 |
| 303873077958 | Prysmian Group | Other | tier_5 |
| 303285145294 | Meta | Other | tier_5 |
| 313765990118 | Comport Consulting | Partner Target | tier_5 |
| 175109006032 | Sangoma | Other | tier_5 |
| 314002024163 | iVedha | Other | tier_5 |
| 314029902571 | ZeroPoint Technologies | Partner Target | tier_5 |
| 314015568615 | Midokura | Partner Target | tier_5 |
| 314296904438 | Myriad360 | Partner Target | tier_5 |
| 314129906391 | Positron | Partner Target | tier_5 |
| 314194094803 | Xsight Labs | Partner Target | tier_5 |
| 314488781532 | Oxmiq Labs | Partner Target | tier_5 |

HubSpot writes: 4 batches (10/10/10/9), 39/39 updated, 0 failures. Verified via read-back on Accenture, Meta, HPE, Sangoma, Oxmiq Labs (all last_enriched_date=2026-06-16, signal_heat=Cold, segment/tier unchanged).

## Standing Tier 3 holds carried (6 - no R2 action, all cross-routine scope)

| ID | Name | Domain | last_enriched | Issue | Owner/Route |
|---|---|---|---|---|---|
| 175221473010 | MMR Fiber Solutions / SouthWestern Power Group | southwesternpower.com | 2026-02-24 | Entity-split: fiber arm mmrfiber.com is a real emerging Fiber Operator ICP, but record sits on the power-parent domain | R3 / Cooper (split or domain-correct) |
| 316598423243 | team.telstra.com | team.telstra.com | 2026-02-24 | Subdomain dedup stub of canonical Telstra | R3 dedup |
| 311326703342 | Intercontinental Exchange | ice.com | 2026-04-01 | 2 sub-segments with positive evidence (Enterprise/Financial Services vs Data Center Colo Provider), 0 deals - genuine reclassification | Cooper |
| 318223366892 | Boldyn Networks (Mobilitie) | mobilitie.com | 2026-04-27 | Duplicate of master Boldyn record 300402132682 | R3 dedup |
| 192890159856 | Confluence Research | confluenceresearch.com.au | 2026-04-27 | 2x R2 re-verification failures (domain resolves to no clear AU entity) | D7 deep-research |
| 300724801211 | FPT | fptsoftware.com | 2026-04-27 | Duplicate of FPT Software 326715774698 (Enterprise / Outsourcing ICP). FPT AI Factory 303405064912 (fpt.com, NeoCloud) is a separate legit arm - do not merge | R3 dedup |

No date bump on any of the 6 (Tier 3 hold discipline). All re-confirmed still in pool at expected state; none resolved by Cooper since 2026-06-15.

## Hard stops / safety
- MaiaEdge own (124293230301): excluded by trigger query. Not touched.
- Open deals at contractsent+: none in candidate pool (all 39 re-stamps are tier_5 non-ICP ecosystem refs with 0 associated deals).
- hs_is_target_account=true: none in the 39 (Boldyn had it explicitly false). No frozen-tier skips this run.
- Customer (closed-won) protection: not triggered (no ICP downgrades proposed).

## Cross-routine coordination
- Ran after R0 (9am) + R1 (10am, GREEN, 4/4 drained, 0 ICP writes). No collision.
- 0 HARD_DELETE feeds to R4 (12pm) this run.
- Standing holds handed to R3 (MMR Fiber, team.telstra, Boldyn, FPT), Cooper (ICE, MMR Fiber split), D7 (Confluence Research).
