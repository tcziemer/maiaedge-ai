CRM Guardian - Flagged Consolidation - 2026-06-02 - 1 contact flagged, 3 reassociated, 15 Tier 3 held

Run summary: 150 flagged companies processed (of 246 in queue; company cap 150, 96 off-page deferred to next run) · 73 companies had associated contacts · 77 zero-contact (archive-ready) · 361 contacts evaluated · 1 Tier 1 Mode B flag · 3 Tier 1-2 Mode A reassociations (+ owner/segment sync) · 15 Tier 3 holds · 0 protected-skips · 0 errors · 4 HubSpot writes, 0 failures

Hard stops: 0 fresh-record holds (Invariant E — none created within 14 days) · 0 open-deal blocks · 0 closed-won customer-history blocks (zero deals associated to any company in scope) · 0 Enterprise pre-Phase-1 mis-flags (all 73 contact-bearing companies carry post-2026-05-11 eviction rationales, already evaluated under the Enterprise-inclusive framework)

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs stale associations from the 3 reassociated contacts)

- 15 Tier 3 holds in the tables below (13 preserved contacts with no ICP primary + 2 company-level mis-flag investigations). 4 of the holds are mis-flag investigations where the account_brief contradicts the Flagged-for-deletion segment (Yondr, HyperLink, MTA | Alasconnect, Sify Technologies) — Cooper to verify/reclassify in HubSpot UI before archival.

Run health: YELLOW
- Writes succeeded; Tier 3 holds present and 4 mis-flag investigations flagged.

Errors: None

---

## Mode A Reassociations (preserved contact -> canonical ICP primary)

```
| Contact | Contact ID | Source flagged company | -> ICP primary | Primary ID | Segment synced | Owner synced |
|---------|-----------|------------------------|----------------|-----------|----------------|--------------|
| Frank Scandariato (edged.us)    | 451559667429 | Edged Data Centers (251566704352)       | Edged Energy   | 251592703686 | Data Center Colo Provider | 161889085 (Tim Lieto) |
| Jacob Hinton (hivelocity.net)   | 476512699073 | ColoHouse / Steadfast (254570392308 / 264355635947) | Hivelocity     | 254575820474 | Data Center Colo Provider | 161889085 (Tim Lieto) |
| Chris Melloway (bluebirdfiber.com) | 486362106616 | Everstream (193867595511)            | Bluebird Network (bluebirdfiber.com) | 323821758151 | Fiber Operator | 161889085 (Tim Lieto) |
```
Note: reassociation is add-only (HubSpot MCP cannot remove the old association). The old association to the flagged company persists until Cooper archives the company, which cleans it up.

## Mode B Flags (not-preserved, not-protected -> flagged_for_deletion = true)

```
| Contact | Contact ID | Flagged company | Reason |
|---------|-----------|-----------------|--------|
| Vinay Nagpal (vnagpal@everstream.net) | 426016365276 | Everstream (193867595511, defunct -> Bluebird Fiber) | No activity 96d, no open deal, lifecyclestage lead, not opted out |
```
(344 other not-preserved contacts on the 73 companies were already at flagged_for_deletion = true from prior runs — idempotent, no write.)

## Tier 3 Held

```
| # | Contact | Contact ID | Company | Company ID | Reason |
|---|---------|-----------|---------|-----------|--------|
| 1  | Macatoci Kanashiro | 261906818770 | Sumauma                | 167113651945 | Preserved (contacted 4d); company is non-ICP telecom software/consulting vendor (D1) — no ICP primary to reassociate |
| 2  | Paulo Machado      | 261906818771 | Sumauma                | 167113651945 | Preserved (contacted 18d); same non-ICP company — no ICP primary |
| 3  | Rami Yaron         | 297261432562 | FlowSec                | 193865438923 | Preserved (contacted 63d); non-ICP security vendor — no ICP primary |
| 4  | Michael Honeycutt  | 314701034216 | Corero                 | 209237307100 | Preserved (updated 82d); non-ICP DDoS security vendor — no ICP primary |
| 5  | Steven Garvin      | 441467623152 | Essextel               | 303896262390 | Preserved (updated 40d); non-ICP VoIP reseller — no ICP primary |
| 6  | Colin Sharkey      | 451518850806 | FPX AI                 | 311392963281 | Preserved (contacted 49d); non-ICP GPU marketplace — no ICP primary |
| 7  | Niraj Yagnik       | 451588830920 | FPX AI                 | 311392963281 | Preserved (updated 78d); same non-ICP company — no ICP primary |
| 8  | Sebastian Metti    | 451588831988 | Saturn Cloud           | 297918677722 | Preserved (updated 78d); non-ICP MLOps platform — no ICP primary |
| 9  | Jason Scandrol     | 455480763107 | LS Power               | 311418164947 | Preserved (updated 78d); non-ICP independent power company — no ICP primary |
| 10 | Ryan Sabia         | 464779318976 | Yondr                  | 316194606814 | Preserved (updated 42d); MIS-FLAG INVESTIGATION — brief describes hyperscale DC developer (878MW, DigitalBridge-owned) that reads as Colo/Greenfield ICP, yet segment = Flagged for deletion. Recommend Cooper verify/reclassify |
| 11 | Michael Hall       | 476652573403 | HyperLink Infrastructure | 316164220626 | Preserved (updated 42d); MIS-FLAG INVESTIGATION — brief describes vertically-integrated fiber carrier (dark fiber for hyperscalers) that reads as Fiber Operator ICP, yet flagged. Recommend Cooper verify/reclassify |
| 12 | Lynn Bruns         | 486369299174 | ISG                    | 194005222095 | Preserved (contacted 39d); non-ICP architecture/engineering firm (D1) — no ICP primary |
| 13 | Rob Schumann       | 487432186604 | Truepacket             | 132996276936 | Preserved (contacted 28d); non-ICP thin/insufficient footprint (D1) — no ICP primary |
| 14 | (company-level)    | -          | MTA \| Alasconnect      | 253675894488 | MIS-FLAG INVESTIGATION — account_brief asserts "Tier 3 Fiber Op... ICP fit" (Alaska coop + AlasConnect fiber subsidiary) yet segment = Flagged for deletion. Recommend Cooper verify/reclassify to Fiber Operator |
| 15 | (company-level)    | -          | Sify Technologies Ltd. | 251651866344 | MIS-FLAG INVESTIGATION — account_brief asserts "Tier 1 maintained" (major Indian DCCP + MSP + network operator) yet segment = Flagged for deletion. Recommend Cooper verify/reclassify |
```

## Notes
- Pagination sorted by hs_object_id ASC. 246 total flagged companies; first 150 processed this run.
- No Apollo, web_search, or web_fetch used (HubSpot-internal routine).
- Prior-run Tier 3 holds on canvas F0B0AFSB9LN were not drained this run (best-effort; the canvas is large and draining requires per-section edits — the new holds above were appended).
