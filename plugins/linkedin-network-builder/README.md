# LinkedIn Network Builder v2.0

Strategic LinkedIn networking plugin for MaiaEdge ICP accounts. Single-pass workflow: pull companies from HubSpot, find contacts on LinkedIn, send bare connections, enrich via Apollo, push to HubSpot.

## What It Does

Cooper Kennedy builds his professional network inside MaiaEdge target accounts. Every contact worth connecting with gets added to the CRM.

**The workflow:**
1. Pull target companies from HubSpot by segment priority (Neocloud > Colo > Network/Fiber)
2. Check activity gate (skip accounts with conversations in last 14 days)
3. Flag any segment misclassifications noticed along the way
4. Search LinkedIn for GTM, RevOps, CCO, CRO, and infrastructure leaders
5. Send 20 bare connection requests (no note, no message)
6. Apollo enrich each contact (verified email + LinkedIn URL). Apollo-HubSpot sync handles contact creation automatically.
7. If misclassifications flagged, approve corrections and update HubSpot segments

## Commands

- `/build-targets [segment] [count]` -- Full workflow. Source from HubSpot, find on LinkedIn, connect, enrich, push to CRM. Defaults to neocloud + colocation, 20 targets.
- `/connect-batch [file]` -- Standalone. Send connections + enrich + push from an existing target list.

## Dependencies (MCP tools required)

- **HubSpot** -- Company search, segment validation, misclassification corrections
- **Claude in Chrome** -- LinkedIn search and connection automation
- **Apollo** -- Contact enrichment (People Match for verified email + LinkedIn). Apollo-HubSpot sync creates contacts automatically.

## Cross-Skill Architecture

References existing MaiaEdge skills for domain logic. Strategy changes cascade automatically:
- `account-sourcing` -- HubSpot search patterns
- `company-enrichment` / `segment-classification` -- classification rules
- `edge-case-researcher` -- misclassification detection
- `import-processor` -- HubSpot property values
- `contact-discovery` -- Apollo API patterns, persona mapping
- `territory-manager` -- state-to-owner assignment
- `sdr-pipeline` -- activity gate thresholds

See `skills/icp-networking/references/cross-skill-map.md` for the full reference map.

## Safety

- Max 20 connections per session
- 3-5 second delays between requests
- Stops on weekly limit warnings or CAPTCHAs
- No notes or messages (bare requests only)
- Activity gate prevents stepping on active sales conversations
- Only verified emails pushed to HubSpot
