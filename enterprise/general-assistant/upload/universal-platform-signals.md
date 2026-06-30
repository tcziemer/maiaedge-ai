# Universal Platform Signals (cross-segment)

For use by the `weekly-signal-scan` skill and any other skill that consumes signals. Read alongside [signal-framework.md](signal-framework.md).

This file documents signals that behave **identically across all 6 ICP segments** (Colo, Fiber Operator, MSP/Aggregator, Neocloud, Network Operator, **Enterprise** - Enterprise added 2026-05-11 with Multi-DC ICP promotion). They are primarily Apollo-native signals plus a handful of free cross-segment signals that don't warrant per-segment duplication.

**Production stack:** Apollo (paid, already licensed) + free sources + web search. Paid phase-2 signals (PitchBook, Structure Research, Kentik, HG Insights, LinkedIn Sales Navigator, Leadfeeder, 6sense, BuiltWith, etc.) are explicitly **out of scope** and not documented here.

---

## Apollo Signals (AP-series)

All Apollo signals are available today through the existing Apollo license. Each one applies across all 6 segments; the target-persona titles differ by segment per the segment files, but the detection mechanism is the same. (For Enterprise personas added 2026-05-11, see `context/segments/enterprise.md` persona priority by sub-segment + `routines/claude-code/r8-persona-fill/prompt.md` Step 3 for Apollo title patterns.)

### AP-1 - Job Change to Target Persona (<90 days)

**Why:** Strongest Apollo signal across all segments. New leaders have a 60-120 day window where they are most receptive to vendor conversations and have authority to scope new platform spend.

**Detection:** Apollo People Search with filter `job_change_date < 90 days` + title-match against segment persona list (see each segment file's target-personas section).

**Scoring tier:** A. Score floor: 12. Strong alone.

**Per-segment persona hooks:**
- **Neocloud:** CTO, SVP/VP Infrastructure Engineering, CFO (at scale), Head of Platform.
- **Colo:** VP Interconnection / Head of Fabric Services, Chief Network Engineer (AI Signals colo), VP Data Center Operations.
- **Fiber Operator:** CTO / CNO, COO, CRO / VP Wholesale, CFO (PE-backed).
- **Network Operator:** CTO / CNO, Chief Product & Strategy Officer, VP Network Strategy, CTrO / CDO.
- **MSP/Aggregator:** CRO, VP Supplier Strategy, VP Platform, Head of AI Practice, VP Solutions Engineering. For NaaS Platform Operator subtype: CTO, VP Platform, VP Product.

### AP-2 - Competitor / Adjacent-Employer Lateral Hire

**Why:** When a senior technical leader moves from an incumbent or competitor (Equinix → regional colo; Ciena → neocloud; Zayo → regional CLEC; Lumen → network operator), they bring disproportionate buying intent for orchestration / federation platforms. Warm-intro potential is high.

**Detection:** Apollo Job Change API + filter on previous-employer matching a competitor / incumbent list per segment.

**Scoring tier:** A. Score floor: 12.

### AP-3 - Apollo Scoops / News Feed (segment-tuned keywords)

**Why:** Apollo aggregates press and news into per-account scoops. Overlaps with free RSS (DCD, Fierce Network, Light Reading, etc.) but Apollo's binding to account records saves manual match work.

**Detection:** Apollo Scoops filter with segment-specific keyword bundles:
- **Neocloud:** `anchor tenant, lease, Series B+, NVIDIA NCP, Blackwell allocation, sovereign AI`
- **Colo:** `campus expansion, new facility, liquid cooling, interconnection, PE recap, anchor tenant, greenfield`
- **Fiber Operator:** `automation, NaaS, dark fiber, IRU, wholesale, ABS, consortium, BEAD, merger`
- **Network Operator:** `private connectivity fabric, AI networking, NaaS, CAMARA, MEF LSO, SRv6, programmable wholesale`
- **MSP/Aggregator:** `PE recap, line card, new carrier, AI Practice, platform relaunch, recurring revenue mix`

**Scoring tier:** B. Pair with AP-1 or FR-1 for Tier A-equivalent weight.

### AP-4 - Apollo Department Headcount Growth (≥15% eng/ops / 6 months)

**Why:** Precedes platform initiative by 1-2 quarters. Lags by 4 weeks on Apollo (Apollo updates department counts monthly). Useful as a pairing signal rather than standalone trigger.

**Detection:** Apollo Company Insights + filter on department (Engineering, Operations, Network, Infrastructure) growth ≥ 15% over trailing 6 months.

**Scoring tier:** B. Pair required (AP-1 or AP-7 or segment-specific job-req surge).

### AP-5 - Apollo Technographic Change

**Why:** Medium-Weak. Apollo's tech detection is thin for networking / OSS tooling (Kentik, ThousandEyes, NSO, Itential, Blue Planet, Crosswork, Paragon Pathfinder). Coverage is inconsistent. Treat as directional only.

**Detection:** Apollo Technographics + new tool added or removed (weekly diff).

**Scoring tier:** C. **Noise alone.** Only valuable when paired with a discovery conversation to validate; never surface an account solely on AP-5.

### AP-6 - Apollo Intent (Bombora topic score)

**Why:** Accounts showing elevated topic-intent scores (≥66-70) on MaiaEdge-relevant topics are researching. But Apollo Intent alone has a >50% false-positive rate in practice across all segments.

**⚠️ Pair REQUIRED.** Never surface an account on AP-6 alone. Always pair with AP-1 (new hire), AP-7 (funding / M&A), or a segment-specific Tier A signal. Combined score then qualifies for Tier A surfacing.

**Detection:** Apollo Intent filter (requires Apollo Intent SKU) + topic bundle per segment:
- **Neocloud:** "AI infrastructure," "GPU cloud," "inference platform," "network observability"
- **Colo:** "data center interconnect," "cross-connect automation," "fabric," "AI-ready colo"
- **Fiber Operator:** "NaaS," "fiber automation," "network orchestration," "MEF LSO," "TM Forum"
- **Network Operator:** "network API," "programmable wholesale," "CAMARA," "private connectivity fabric"
- **MSP/Aggregator:** "multi-carrier orchestration," "channel platform," "SASE," "cloud on-ramp"

**Scoring tier:** B (only when paired). C alone.

### AP-7 - Apollo Funding / M&A Filter - Announcement OR Close (two-event firing added 2026-04-27)

**Why:** Overlaps with existing U2 (M&A / PE roll-up announcement OR close) and U4 (earnings / 10-Q / 8-K) signals in the framework, but Apollo's metadata is richer  -  counterparty, deal size, round stage, investor identity. Valuable for auto-enrichment of capital-event signals. Fires on BOTH announcement and close events per Cooper 2026-04-27 directive - Apollo distinguishes deal stages (Announced / Pending / Completed) so route each Apollo event to the correct freshness window.

**Detection:** Apollo Funding Events filter + target account match. Refresh weekly. Map Apollo deal-stage values: `Announced` / `Pending` → announcement event; `Completed` / `Closed` → close event. If both stages have fired on the same target within 12 months → +6 stacking auto-elevation per signal-framework.md.

**Scoring tier:** A. **Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop.

---

## Free Cross-Segment Signals (FR-series)

Signals that don't fit Apollo's structured filters but apply across all 6 segments (5 operator segments + Enterprise).

### FR-1 - SEC 8-K Material Filings (consolidated reference)

**Why:** 8-K filings are the highest-confidence capital-event + material-contract signal across Colo (anchor tenant leases), Neocloud (anchor tenant leases + GPU-backed debt), Fiber Operator (ABS / refinancing / M&A), Network Operator (13D activist + divestitures), MSP (TSD PE recaps). Each segment file documents the 8-K items most relevant to it; this is the consolidated entry point.

**Detection:** SEC EDGAR daily feed filtered to target CIKs + Item filter (1.01, 2.01, 2.03, 5.02, 5.02, 7.01).

**Scoring tier:** A.

### FR-2 - Conference Speaking Slots

**Why:** Executive speaking at a conference on "our programmable story" / "our AI networking answer" / "our monetization strategy" is narrative-building. Useful as **context**  -  confirms the operator is publicly positioning in this direction. Does NOT indicate active procurement.

**⚠️ Weak alone.** Never surface an account solely on conference-slot signal. Only elevates weight when paired with a Tier A / Tier B signal from the same account.

**Detection:** Conference agenda scrapers (PTC, DCD Connect, Datacloud, Metro Connect, ITW, Capacity, Fiber Connect, ISE EXPO, NANOG, RIPE, MWC, Channel Partners Expo, AVANT Special Forces, Telarus Partner Summit, Bridgepointe Tech Summit).

**Scoring tier:** C.

### FR-3 - Website Visitor Tracking

**Why:** Direct behavioral intent (a target account visits MaiaEdge's solution / pricing / documentation pages) is the highest-confidence real-time signal available. Catches active research before any public signal fires.

**⚠️ Availability flag:** FR-3 is only active when we have visitor-tracking wired up via Apollo Inbound Tracking (requires Apollo Professional tier + pixel deployment on maiaedge.io). If not deployed, treat FR-3 as "available if enabled." Confirm status with RevOps before building skills or workflows that depend on FR-3 firing.

**Detection:** Apollo Inbound (when live), or free-tier alternatives (Leadfeeder / Albacross) if purchased at Phase 2.

**Scoring tier:** A (when live). N/A (when not yet deployed).

---

## Scoring Overlay

Apollo + free cross-segment signals score into the existing Tier × Freshness × Confidence model from [signal-framework.md](signal-framework.md).

| Signal | Default Tier | Notes |
|---|---|---|
| AP-1 Job Change | A | Strong alone |
| AP-2 Competitor Lateral | A | Strong alone; warm-intro bonus if applicable |
| AP-3 Scoops | B | Overlaps RSS; Apollo binding saves match-work |
| AP-4 Department Headcount | B | Pair required |
| AP-5 Technographic Change | C | Context / discovery input only; noise alone |
| AP-6 Intent | B (paired) / C (alone) | **Never standalone** |
| AP-7 Funding / M&A | A | Overlaps existing U2 / U4 with richer metadata |
| FR-1 SEC 8-K | A | Highest-confidence capital-event signal |
| FR-2 Conference Slot | C | Weak alone; context only |
| FR-3 Website Tracking | A (when live) | Availability flag |

**Stacking rule:** 2+ signals within same 30-day window with ≥1 individual signal ≥ 8 → auto-elevate to score 18+ (same rule as framework).

---

## Explicitly Noise (do not productionize alone)

Per the April 2026 signal refresh, the following signals are explicitly demoted or excluded from standalone triggering. They can provide **context** to an existing qualified signal but must never surface an account on their own:

- **AP-5 Apollo Technographic Change alone** (Apollo's coverage of networking / OSS tools is too thin to rely on).
- **AP-6 Apollo Intent without pairing** (>50% false-positive rate).
- **Apollo keyword drift / description changes quarterly** (TAM context, not deal trigger; lags reality by 6-12 months).
- **Generic total-headcount growth** (function-specific growth is stronger).
- **FR-2 Conference Slot alone** (marketing signal).
- **Status page incidents** (reactive; see `neocloud-signals.md` N-C3 demotion).
- **Uptime Tier Certification** (trailing; see `colocation-signals.md` noise list).
- **Generic press releases** without tenant / build / capital specifics.

---

## Integration with `weekly-signal-scan`

The `weekly-signal-scan` skill should:

1. **Surface signals** from this universal file PLUS the relevant per-segment file (colocation-signals.md, neocloud-signals.md, etc.) for each target account.
2. **Never duplicate** Apollo signals across files  -  they live only here.
3. **Score per framework** using Tier × Freshness × Confidence, apply stacking rule.
4. **Respect the noise list** above  -  even if a noise signal fires, it cannot be the sole reason an account surfaces.
5. **Apply availability flags** on FR-3 (and any future conditional signals).
