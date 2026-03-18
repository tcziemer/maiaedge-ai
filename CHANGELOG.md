# Changelog

## [1.0.0] - 2026-03-17

### Initial Repository Creation
- Consolidated all context files into `context/` (single source of truth)
- Consolidated all skills into `skills/` (21 canonical SKILL.md files)
- Created plugin packaging in `plugins/` (7 plugins with manifests)
- Created enterprise project manifests for 5 Claude.ai Projects
- Retired `maiaedge-sales` plugin (unique skills promoted to standalone)
- Fixed stale SDR Pipeline references (messaging-framework.md, email-writing-rules.md)
- Extracted unique V2 bot content into context files:
  - NEW: context/hubspot/deals-schema.md
  - NEW: context/sales/pricing-reference.md
  - NEW: context/sales/marketplace-seeding-strategy.md
  - UPDATED: sender-profiles.md (added founder voices)
  - UPDATED: maiaedge-101.md (added exec team bios)
  - UPDATED: territory-model.md (added Kyle Blackwell, Woody Acosta)
  - UPDATED: proof-points.md (added IENTC reference details)
  - UPDATED: competitive-positioning.md (added Lumen PCF/AWS threat)
- Created build.sh for automated plugin assembly
- Created CLAUDE.md for Claude Code integration
