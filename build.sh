#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILDS_DIR="$REPO_DIR/builds"
CONTEXT_DIR="$REPO_DIR/context"
SKILLS_DIR="$REPO_DIR/skills"
PLUGINS_DIR="$REPO_DIR/plugins"
TMP_BUILD="/tmp/maiaedge-build-$$"

# Helper: convert MSYS /c/ paths to C:/ for Python on Windows
winpath() {
  local p="$1"
  # Convert MSYS /c/ paths to C:/
  p=$(echo "$p" | sed 's|^/\([a-zA-Z]\)/|\1:/|')
  # Convert /tmp to the real Windows temp path
  if [[ "$p" == /tmp* ]]; then
    local win_temp
    win_temp=$(cmd //c "echo %TEMP%" 2>/dev/null | tr -d '\r')
    p="${win_temp}${p#/tmp}"
  fi
  echo "$p"
}

echo "=== MaiaEdge AI Toolkit Build ==="
echo "Repo: $REPO_DIR"
echo ""

# Use a temp dir for zip operations (avoids FUSE filesystem limitations)
# On MSYS/Git Bash, use $TEMP or $REPO_DIR/.tmp so PowerShell can resolve the path
if [ -n "$TEMP" ]; then
  TMP_BUILD="$TEMP/maiaedge-build-$$"
else
  TMP_BUILD="/tmp/maiaedge-build-$$"
fi
rm -rf "$TMP_BUILD"
mkdir -p "$TMP_BUILD/plugins" "$TMP_BUILD/plugins-zipped" "$TMP_BUILD/skills-zipped"

# Check Python availability (only needed for plugin + standalone-skill-zip builds).
# Enterprise uploads + instance-skills bundle are pure bash and always run.
# Try python3, then python, then py — first one that actually executes wins.
HAS_PYTHON3=0
PYTHON=""
for candidate in python3 python py; do
  if command -v "$candidate" &>/dev/null && "$candidate" -c "import sys" &>/dev/null; then
    PYTHON="$candidate"
    HAS_PYTHON3=1
    break
  fi
done

if [ $HAS_PYTHON3 -eq 0 ]; then
  echo "NOTE: no working Python found — skipping plugin zips and standalone skill zips."
  echo "      Enterprise upload folders and instance-skills bundle will still build."
  echo ""
fi

# Build each plugin (python3 required for manifest JSON parsing)
if [ $HAS_PYTHON3 -eq 1 ]; then
for plugin_dir in "$PLUGINS_DIR"/*/; do
  plugin_name=$(basename "$plugin_dir")
  manifest="${plugin_dir%/}/plugin-manifest.json"

  if [ ! -f "$manifest" ]; then
    echo "SKIP: $plugin_name (no plugin-manifest.json)"
    continue
  fi

  echo "Building: $plugin_name"
  build_target="$TMP_BUILD/plugins/$plugin_name"
  mkdir -p "$build_target"

  # Copy .claude-plugin
  if [ -d "$plugin_dir/.claude-plugin" ]; then
    cp -r "$plugin_dir/.claude-plugin" "$build_target/"
  fi

  # Copy README
  if [ -f "$plugin_dir/README.md" ]; then
    cp "$plugin_dir/README.md" "$build_target/"
  fi

  # Copy CHANGELOG if exists
  if [ -f "$plugin_dir/CHANGELOG.md" ]; then
    cp "$plugin_dir/CHANGELOG.md" "$build_target/"
  fi

  # Copy commands
  if [ -d "$plugin_dir/commands" ]; then
    cp -r "$plugin_dir/commands" "$build_target/"
  fi

  # Copy skills from shared skills/ directory
  skills=$("$PYTHON" -c "import json; m=json.load(open('$(winpath "$manifest")')); print(' '.join(m.get('skills',[])))")
  if [ -n "$skills" ]; then
    mkdir -p "$build_target/skills"
    for skill in $skills; do
      if [ -d "$SKILLS_DIR/$skill" ]; then
        mkdir -p "$build_target/skills/$skill"
        cp "$SKILLS_DIR/$skill/SKILL.md" "$build_target/skills/$skill/"
      else
        echo "  WARNING: Skill $skill not found in skills/"
      fi
    done
  fi

  # Copy context files into references/
  contexts=$("$PYTHON" -c "import json; m=json.load(open('$(winpath "$manifest")')); print(' '.join(m.get('context',[])))")
  if [ -n "$contexts" ]; then
    mkdir -p "$build_target/references"
    for ctx in $contexts; do
      src="$CONTEXT_DIR/$ctx"
      if [ -f "$src" ]; then
        cp "$src" "$build_target/references/"
      else
        echo "  WARNING: Context $ctx not found"
      fi
    done
  fi

  # Copy static assets
  statics=$("$PYTHON" -c "import json; m=json.load(open('$(winpath "$manifest")')); print(' '.join(m.get('static',[])))")
  if [ -n "$statics" ]; then
    for static_path in $statics; do
      src="$plugin_dir/$static_path"
      if [ -d "$src" ]; then
        cp -r "$src" "$build_target/"
      elif [ -f "$src" ]; then
        cp "$src" "$build_target/"
      fi
    done
  fi

  # Zip in /tmp then copy to builds/ (include .claude-plugin/ — required for Cowork)
  if command -v zip &>/dev/null; then
    (cd "$TMP_BUILD/plugins" && zip -r "$TMP_BUILD/plugins-zipped/$plugin_name.zip" "$plugin_name" > /dev/null)
  else
    # PowerShell Compress-Archive writes backslash paths which Cowork rejects.
    # Use .NET ZipFile directly with forward-slash entry names.
    powershell -NoProfile -Command "
      Add-Type -AssemblyName System.IO.Compression.FileSystem
      \$src = '$(winpath "$TMP_BUILD/plugins/$plugin_name")'
      \$dst = '$(winpath "$TMP_BUILD/plugins-zipped/$plugin_name.zip")'
      if (Test-Path \$dst) { Remove-Item \$dst }
      \$zip = [System.IO.Compression.ZipFile]::Open(\$dst, 'Create')
      Get-ChildItem -Path \$src -Recurse -File | ForEach-Object {
        \$rel = \$_.FullName.Substring(\$src.Length - '$plugin_name'.Length).Replace('\\', '/')
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(\$zip, \$_.FullName, \$rel) | Out-Null
      }
      \$zip.Dispose()
    "
  fi
  echo "  -> $plugin_name.zip"
done
fi  # HAS_PYTHON3 plugin loop

echo ""
if [ $HAS_PYTHON3 -eq 1 ]; then
echo "Building standalone skill zips..."

# Build standalone skill zips
STANDALONE_SKILLS="account-brief copy-strategist sales-enablement call-prep competitive-intel"
for skill in $STANDALONE_SKILLS; do
  if [ -d "$SKILLS_DIR/$skill" ]; then
    mkdir -p "$TMP_BUILD/skill-stage/$skill"
    cp "$SKILLS_DIR/$skill/SKILL.md" "$TMP_BUILD/skill-stage/$skill/"

    # Include copy-strategy references for copy-strategist
    if [ "$skill" = "copy-strategist" ] && [ -d "$CONTEXT_DIR/copy-strategy" ]; then
      mkdir -p "$TMP_BUILD/skill-stage/$skill/references"
      cp "$CONTEXT_DIR/copy-strategy/"* "$TMP_BUILD/skill-stage/$skill/references/"
    fi

    if command -v zip &>/dev/null; then
      (cd "$TMP_BUILD/skill-stage" && zip -r "$TMP_BUILD/skills-zipped/$skill.zip" "$skill" > /dev/null)
    else
      powershell -NoProfile -Command "
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        \$src = '$(winpath "$TMP_BUILD/skill-stage/$skill")'
        \$dst = '$(winpath "$TMP_BUILD/skills-zipped/$skill.zip")'
        if (Test-Path \$dst) { Remove-Item \$dst }
        \$zip = [System.IO.Compression.ZipFile]::Open(\$dst, 'Create')
        Get-ChildItem -Path \$src -Recurse -File | ForEach-Object {
          \$rel = \$_.FullName.Substring(\$src.Length - '$skill'.Length).Replace('\\', '/')
          [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(\$zip, \$_.FullName, \$rel) | Out-Null
        }
        \$zip.Dispose()
      "
    fi
    echo "  -> $skill.zip"
  fi
done
fi  # HAS_PYTHON3 standalone-skill-zips

# Copy assembled plugins to builds/ (for browsing) and zips
echo ""
echo "Copying to builds/..."
mkdir -p "$BUILDS_DIR/plugins" "$BUILDS_DIR/plugins-zipped" "$BUILDS_DIR/skills-zipped"
cp -r "$TMP_BUILD/plugins/"* "$BUILDS_DIR/plugins/" 2>/dev/null || true
cp "$TMP_BUILD/plugins-zipped/"*.zip "$BUILDS_DIR/plugins-zipped/" 2>/dev/null || true
cp "$TMP_BUILD/skills-zipped/"*.zip "$BUILDS_DIR/skills-zipped/" 2>/dev/null || true

# Cleanup
rm -rf "$TMP_BUILD"

# ============================================
# Build enterprise upload folders
# Flattens skills + context into one folder per Project with proper .md names
# ============================================
echo ""
echo "Building enterprise upload folders..."

ENT_DIR="$REPO_DIR/enterprise"

# Pure-bash skill rename lookup — no python3 dependency so enterprise builds always run.
# Keep in sync with the standalone-skill-zips list and Cowork plugin manifests.
skill_upload_name() {
  case "$1" in
    cold-email)             echo "maiaedge-cold-outreach-writer" ;;
    linkedin-outreach)      echo "maiaedge-linkedin-outreach" ;;
    prospect-research)      echo "maiaedge-prospect-research" ;;
    segment-classification) echo "maiaedge-segment-classification" ;;
    company-enrichment)     echo "maiaedge-company-enrichment" ;;
    import-processor)       echo "maiaedge-enrichment-import-processor" ;;
    contact-discovery)      echo "maiaedge-contact-discovery" ;;
    account-brief)          echo "maiaedge-account-brief" ;;
    sdr-pipeline)           echo "maiaedge-sdr-pipeline" ;;
    copy-strategist)        echo "copystrategistskill" ;;
    edge-case-researcher)   echo "maiaedge-edge-case-researcher" ;;
    account-sourcing)       echo "maiaedge-account-sourcing" ;;
    crm-hygiene)            echo "maiaedge-crm-hygiene" ;;
    pipeline-analytics)     echo "maiaedge-pipeline-analytics" ;;
    territory-manager)      echo "maiaedge-territory-manager" ;;
    event-intelligence)     echo "maiaedge-event-intelligence" ;;
    sales-enablement)       echo "maiaedge-sales-enablement" ;;
    sales-docs)             echo "maiaedge-sales-docs" ;;
    icp-networking)         echo "maiaedge-icp-networking" ;;
    call-prep)              echo "maiaedge-call-prep" ;;
    competitive-intel)      echo "maiaedge-competitive-intel" ;;
    call-analysis)          echo "maiaedge-call-analysis" ;;
    pipeline-discipline)    echo "maiaedge-pipeline-discipline" ;;
    call-reporting)         echo "maiaedge-call-reporting" ;;
    crm-guardian)           echo "maiaedge-crm-guardian" ;;
    pre-deletion-audit)     echo "maiaedge-pre-deletion-audit" ;;
    weekly-signal-scan)     echo "maiaedge-weekly-signal-scan" ;;
    branded-doc)            echo "maiaedge-branded-doc" ;;
    *)                      echo "maiaedge-$1" ;;
  esac
}

copy_skill() {
  local skill_name="$1" dest="$2"
  local upload_name
  upload_name=$(skill_upload_name "$skill_name")
  if [ -f "$SKILLS_DIR/$skill_name/SKILL.md" ]; then
    cp "$SKILLS_DIR/$skill_name/SKILL.md" "$dest/${upload_name}.md"
  fi
}

# Strip any previously-built skill .md files from a context-only upload folder.
# Runs before each project rebuild so migrations from the old layout are clean.
strip_skills_from_upload() {
  local dest="$1"
  rm -f "$dest"/maiaedge-*.md "$dest"/copystrategistskill.md
}

# ============================================
# Instance-Skills Bundle
# Upload these ONCE at the Claude.ai instance level. Every enterprise project
# that lists a skill in its system prompt picks it up automatically — no need
# to bundle skill files into each project.
# ============================================
echo ""
echo "Building instance-skills bundle..."
INSTANCE_SKILLS_DIR="$BUILDS_DIR/instance-skills"
rm -rf "$INSTANCE_SKILLS_DIR"
mkdir -p "$INSTANCE_SKILLS_DIR"
for skill_dir in "$SKILLS_DIR"/*/; do
  skill_name=$(basename "$skill_dir")
  copy_skill "$skill_name" "$INSTANCE_SKILLS_DIR"
done
echo "  $(ls "$INSTANCE_SKILLS_DIR" | wc -l) skill files -> $INSTANCE_SKILLS_DIR"

copy_context_dir() {
  local src_dir="$1" dest="$2"
  if [ -d "$src_dir" ]; then
    find "$src_dir" -maxdepth 1 -name "*.md" -exec cp {} "$dest/" \;
  fi
}

# --- Sales Outreach ---
# Skills (upload at instance level): cold-email, linkedin-outreach, prospect-research,
# segment-classification, company-enrichment, import-processor, contact-discovery,
# account-brief, sdr-pipeline, copy-strategist
SO="$ENT_DIR/sales-outreach/upload"
mkdir -p "$SO"
strip_skills_from_upload "$SO"
copy_context_dir "$CONTEXT_DIR/core" "$SO"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$SO"
copy_context_dir "$CONTEXT_DIR/segments" "$SO"
copy_context_dir "$CONTEXT_DIR/signals" "$SO"
copy_context_dir "$CONTEXT_DIR/outreach" "$SO"
copy_context_dir "$CONTEXT_DIR/copy-strategy" "$SO"
cp "$CONTEXT_DIR/enrichment/research-routes.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/enrichment/output-schemas.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/hubspot-values.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/territory-model.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/deals-schema.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/contact-schema.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/property-schema.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/account-brief-template.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/edge-ai-thesis-montauk.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/email-bot-supplemental.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/product/proof-points.md" "$SO/" 2>/dev/null
echo "  Sales Outreach: $(ls "$SO" | wc -l) files"

# --- Founder Outreach ---
# Skills (upload at instance level): cold-email, linkedin-outreach, prospect-research,
# segment-classification, company-enrichment, contact-discovery, account-brief, copy-strategist
FO="$ENT_DIR/founder-outreach/upload"
mkdir -p "$FO"
strip_skills_from_upload "$FO"
copy_context_dir "$CONTEXT_DIR/core" "$FO"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$FO"
copy_context_dir "$CONTEXT_DIR/segments" "$FO"
copy_context_dir "$CONTEXT_DIR/signals" "$FO"
copy_context_dir "$CONTEXT_DIR/outreach" "$FO"
copy_context_dir "$CONTEXT_DIR/copy-strategy" "$FO"
cp "$CONTEXT_DIR/enrichment/research-routes.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/hubspot-values.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/territory-model.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/contact-schema.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/property-schema.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/account-brief-template.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/edge-ai-thesis-montauk.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/email-bot-supplemental.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/product/proof-points.md" "$FO/" 2>/dev/null
echo "  Founder Outreach: $(ls "$FO" | wc -l) files"

# --- Account Intelligence ---
# Skills (upload at instance level): company-enrichment, import-processor, edge-case-researcher,
# account-sourcing, crm-hygiene, pipeline-analytics, territory-manager, contact-discovery,
# event-intelligence, sales-enablement, weekly-signal-scan, account-brief
AI="$ENT_DIR/account-intelligence/upload"
mkdir -p "$AI"
strip_skills_from_upload "$AI"
copy_context_dir "$CONTEXT_DIR/core" "$AI"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$AI"
copy_context_dir "$CONTEXT_DIR/account-tiering/icp-deep-dives" "$AI"   # per-ICP B-and-C deep dives (edge-case-researcher)
copy_context_dir "$CONTEXT_DIR/segments" "$AI"
copy_context_dir "$CONTEXT_DIR/signals" "$AI"
for d in hubspot enrichment product sales; do
  copy_context_dir "$CONTEXT_DIR/$d" "$AI"
done
cp "$CONTEXT_DIR/marketing/ai-copywriting-guidelines.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/linkedin-framework.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/sovereign-routing-explainer.md" "$AI/" 2>/dev/null
copy_context_dir "$CONTEXT_DIR/marketing/media-consumption" "$AI"
# Context deps picked up by account-brief, contact-discovery, event-intelligence, sales-enablement skills
cp "$CONTEXT_DIR/outreach/email-writing-rules.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-language.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-messaging.md" "$AI/" 2>/dev/null
echo "  Account Intelligence: $(ls "$AI" | wc -l) files"

# --- Call Intelligence ---
# Transcript/summary analysis on contact records: use cases, pain points, objections, competitive intel
# Skills (upload at instance level): call-analysis, pipeline-discipline, call-reporting, pipeline-analytics
CI="$ENT_DIR/call-intelligence/upload"
mkdir -p "$CI"
strip_skills_from_upload "$CI"
# Core context (full set -- competitive and messaging needed for call classification)
copy_context_dir "$CONTEXT_DIR/core" "$CI"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$CI"
# Segments (call analysis needs segment context to classify discussions)
copy_context_dir "$CONTEXT_DIR/segments" "$CI"
# HubSpot (all schemas -- calls associate with contacts, companies, deals, tickets)
copy_context_dir "$CONTEXT_DIR/hubspot" "$CI"
# Sales context for call intelligence
cp "$CONTEXT_DIR/sales/use-case-taxonomy.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/sales/pricing-reference.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/sales/edge-ai-thesis-montauk.md" "$CI/" 2>/dev/null
# Product context (proof points referenced in calls, product knowledge for technical discussions)
cp "$CONTEXT_DIR/product/proof-points.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/product/ai-market-positioning.md" "$CI/" 2>/dev/null
# Copy strategy context (messaging baseline for Modes 5 & 6: alignment analysis + PMF signals)
cp "$CONTEXT_DIR/copy-strategy/segment-language.md" "$CI/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-messaging.md" "$CI/" 2>/dev/null
# Call report styling
cp "$CONTEXT_DIR/sales/call-report-styles.css" "$CI/" 2>/dev/null
echo "  Call Intelligence: $(ls "$CI" | wc -l) files"

# --- Revenue Reporting ---
# Skills (upload at instance level): pipeline-analytics, call-reporting, call-analysis, pipeline-discipline
RR="$ENT_DIR/revenue-reporting/upload"
mkdir -p "$RR"
strip_skills_from_upload "$RR"
cp "$CONTEXT_DIR/core/maiaedge-101.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/core/icp-playbook.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/core/segment-qualification.md" "$RR/" 2>/dev/null
copy_context_dir "$CONTEXT_DIR/segments" "$RR"
copy_context_dir "$CONTEXT_DIR/hubspot" "$RR"
cp "$CONTEXT_DIR/sales/use-case-taxonomy.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-report-styles.css" "$RR/" 2>/dev/null
# Context deps picked up by call-analysis, call-reporting, pipeline-discipline skills
cp "$CONTEXT_DIR/core/messaging-framework.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/core/competitive-positioning.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-language.md" "$RR/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-messaging.md" "$RR/" 2>/dev/null
echo "  Revenue Reporting: $(ls "$RR" | wc -l) files"

# --- CRM Guardian ---
# Skills (upload at instance level): crm-guardian, crm-hygiene, company-enrichment,
# segment-classification, territory-manager, account-sourcing, import-processor,
# edge-case-researcher, contact-discovery, pre-deletion-audit, weekly-signal-scan, account-brief
CG="$ENT_DIR/crm-guardian/upload"
mkdir -p "$CG"
strip_skills_from_upload "$CG"
copy_context_dir "$CONTEXT_DIR/core" "$CG"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$CG"
copy_context_dir "$CONTEXT_DIR/account-tiering/icp-deep-dives" "$CG"   # per-ICP B-and-C deep dives (edge-case-researcher)
copy_context_dir "$CONTEXT_DIR/segments" "$CG"
copy_context_dir "$CONTEXT_DIR/hubspot" "$CG"
copy_context_dir "$CONTEXT_DIR/enrichment" "$CG"
copy_context_dir "$CONTEXT_DIR/signals" "$CG"
cp "$CONTEXT_DIR/product/proof-points.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/product/ai-market-positioning.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/sales/edge-ai-thesis-montauk.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/sales/use-case-taxonomy.md" "$CG/" 2>/dev/null
# Context deps picked up by cold-email, segment-classification, account-brief (when Guardian triggers them)
cp "$CONTEXT_DIR/outreach/email-writing-rules.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-language.md" "$CG/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-messaging.md" "$CG/" 2>/dev/null
echo "  CRM Guardian: $(ls "$CG" | wc -l) files"

# --- Sales Docs ---
# Legal docs + sales collateral + call prep + competitive briefs
# Skills (upload at instance level): sales-docs, sales-enablement, call-prep, competitive-intel
SD="$ENT_DIR/sales-docs/upload"
mkdir -p "$SD"
strip_skills_from_upload "$SD"
copy_context_dir "$CONTEXT_DIR/core" "$SD"
copy_context_dir "$CONTEXT_DIR/account-tiering" "$SD"
copy_context_dir "$CONTEXT_DIR/segments" "$SD"
copy_context_dir "$CONTEXT_DIR/product" "$SD"
cp "$CONTEXT_DIR/hubspot/hubspot-values.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/deals-schema.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/poc-schema.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/property-schema.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/account-brief-template.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/use-case-taxonomy.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/pricing-reference.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/marketplace-seeding-strategy.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/edge-ai-thesis-montauk.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/golden-pitch-key-slides.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/sales/end-of-network-silos-blog.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/ai-copywriting-guidelines.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/linkedin-framework.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/sovereign-routing-explainer.md" "$SD/" 2>/dev/null
# Partner-facing source markdowns for the branded-doc skill (cheatsheets, MaiaEdge 101, product quick reference)
copy_context_dir "$CONTEXT_DIR/partner-assets" "$SD"
# Context deps picked up by call-prep, sales-enablement, competitive-intel skills
cp "$CONTEXT_DIR/copy-strategy/segment-language.md" "$SD/" 2>/dev/null
cp "$CONTEXT_DIR/copy-strategy/segment-messaging.md" "$SD/" 2>/dev/null
echo "  Sales Docs: $(ls "$SD" | wc -l) files"

# --- Branded Content (full repo context; branded-doc + strategy skills) ---
# Skills (upload at instance level): branded-doc, account-brief, sales-enablement,
# competitive-intel, call-prep
# Ships the FULL repo context — segment business cases and branded deliverable design
# both pull across every category (core, segments, signals, hubspot, enrichment, product,
# sales, marketing, copy-strategy, partner-assets, account-tiering).
BC="$ENT_DIR/branded-content/upload"
mkdir -p "$BC"
strip_skills_from_upload "$BC"
find "$CONTEXT_DIR" -name "*.md" -exec cp {} "$BC/" \;
# partner-assets/maiaedge-101.md collides with core/maiaedge-101.md (different content —
# partner edition vs strategy doc). Preserve both with explicit names.
cp "$CONTEXT_DIR/partner-assets/maiaedge-101.md" "$BC/maiaedge-101-partner-edition.md"
cp "$CONTEXT_DIR/core/maiaedge-101.md" "$BC/maiaedge-101.md"
# Branded-doc skill consumes the call-report-styles.css as a brand stylesheet reference
cp "$CONTEXT_DIR/sales/call-report-styles.css" "$BC/" 2>/dev/null
echo "  Branded Content: $(ls "$BC" | wc -l) files"

# --- General Assistant (every context file; all skills at instance level) ---
GA="$ENT_DIR/general-assistant/upload"
mkdir -p "$GA"
strip_skills_from_upload "$GA"
find "$CONTEXT_DIR" -name "*.md" -exec cp {} "$GA/" \;
cp "$CONTEXT_DIR/sales/call-report-styles.css" "$GA/" 2>/dev/null   # non-md asset the find above misses (call-reporting)
echo "  General Assistant: $(ls "$GA" | wc -l) files"

echo ""
echo "=== Build Complete ==="
echo "Plugins:         $(ls "$BUILDS_DIR/plugins-zipped/"*.zip 2>/dev/null | wc -l) zips"
echo "Standalone zips: $(ls "$BUILDS_DIR/skills-zipped/"*.zip 2>/dev/null | wc -l) zips"
echo "Instance skills: $(ls "$INSTANCE_SKILLS_DIR" 2>/dev/null | wc -l) files (one-time Claude.ai upload)"
echo "Enterprise:      9 context-only upload folders"
echo ""
echo "Plugin zips:      $BUILDS_DIR/plugins-zipped/"
echo "Skill zips:       $BUILDS_DIR/skills-zipped/"
echo "Instance skills:  $INSTANCE_SKILLS_DIR/"
echo "Enterprise files: $ENT_DIR/*/upload/  (context only — skills live at instance level)"
