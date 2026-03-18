#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILDS_DIR="$REPO_DIR/builds"
CONTEXT_DIR="$REPO_DIR/context"
SKILLS_DIR="$REPO_DIR/skills"
PLUGINS_DIR="$REPO_DIR/plugins"
TMP_BUILD="/tmp/maiaedge-build-$$"

echo "=== MaiaEdge AI Toolkit Build ==="
echo "Repo: $REPO_DIR"
echo ""

# Use /tmp for zip operations (avoids FUSE filesystem limitations)
rm -rf "$TMP_BUILD"
mkdir -p "$TMP_BUILD/plugins" "$TMP_BUILD/plugins-zipped" "$TMP_BUILD/skills-zipped"

# Build each plugin
for plugin_dir in "$PLUGINS_DIR"/*/; do
  plugin_name=$(basename "$plugin_dir")
  manifest="$plugin_dir/plugin-manifest.json"

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
  skills=$(python3 -c "import json; m=json.load(open('$manifest')); print(' '.join(m.get('skills',[])))")
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
  contexts=$(python3 -c "import json; m=json.load(open('$manifest')); print(' '.join(m.get('context',[])))")
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
  statics=$(python3 -c "import json; m=json.load(open('$manifest')); print(' '.join(m.get('static',[])))")
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
  (cd "$TMP_BUILD/plugins" && zip -r "$TMP_BUILD/plugins-zipped/$plugin_name.zip" "$plugin_name" > /dev/null)
  echo "  -> $plugin_name.zip"
done

echo ""
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

    (cd "$TMP_BUILD/skill-stage" && zip -r "$TMP_BUILD/skills-zipped/$skill.zip" "$skill" > /dev/null)
    echo "  -> $skill.zip"
  fi
done

# Copy assembled plugins to builds/ (for browsing) and zips
echo ""
echo "Copying to builds/..."
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
SKILL_RENAME='{"cold-email":"maiaedge-cold-outreach-writer","linkedin-outreach":"maiaedge-linkedin-outreach","prospect-research":"maiaedge-prospect-research","segment-classification":"maiaedge-segment-classification","company-enrichment":"maiaedge-company-enrichment","import-processor":"maiaedge-enrichment-import-processor","contact-discovery":"maiaedge-contact-discovery","account-brief":"maiaedge-account-brief","sdr-pipeline":"maiaedge-sdr-pipeline","copy-strategist":"copystrategistskill","edge-case-researcher":"maiaedge-edge-case-researcher","account-sourcing":"maiaedge-account-sourcing","crm-hygiene":"maiaedge-crm-hygiene","pipeline-analytics":"maiaedge-pipeline-analytics","territory-manager":"maiaedge-territory-manager","event-intelligence":"maiaedge-event-intelligence","sales-enablement":"maiaedge-sales-enablement","sales-docs":"maiaedge-sales-docs","icp-networking":"maiaedge-icp-networking","call-prep":"maiaedge-call-prep","competitive-intel":"maiaedge-competitive-intel"}'

copy_skill() {
  local skill_name="$1" dest="$2"
  local upload_name=$(python3 -c "import json; print(json.loads('$SKILL_RENAME').get('$skill_name','maiaedge-$skill_name'))")
  if [ -f "$SKILLS_DIR/$skill_name/SKILL.md" ]; then
    cp "$SKILLS_DIR/$skill_name/SKILL.md" "$dest/${upload_name}.md"
  fi
}

copy_context_dir() {
  local src_dir="$1" dest="$2"
  if [ -d "$src_dir" ]; then
    find "$src_dir" -maxdepth 1 -name "*.md" -exec cp {} "$dest/" \;
  fi
}

# --- Sales Outreach ---
SO="$ENT_DIR/sales-outreach/upload"
mkdir -p "$SO"
for s in cold-email linkedin-outreach prospect-research segment-classification company-enrichment import-processor contact-discovery account-brief sdr-pipeline copy-strategist; do
  copy_skill "$s" "$SO"
done
copy_context_dir "$CONTEXT_DIR/core" "$SO"
copy_context_dir "$CONTEXT_DIR/segments" "$SO"
copy_context_dir "$CONTEXT_DIR/outreach" "$SO"
copy_context_dir "$CONTEXT_DIR/copy-strategy" "$SO"
cp "$CONTEXT_DIR/enrichment/research-routes.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/enrichment/output-schemas.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/hubspot-values.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/territory-model.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/deals-schema.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/account-brief-template.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/email-bot-supplemental.md" "$SO/" 2>/dev/null
cp "$CONTEXT_DIR/product/proof-points.md" "$SO/" 2>/dev/null
echo "  Sales Outreach: $(ls "$SO" | wc -l) files"

# --- Founder Outreach ---
FO="$ENT_DIR/founder-outreach/upload"
mkdir -p "$FO"
for s in cold-email linkedin-outreach prospect-research segment-classification company-enrichment contact-discovery account-brief copy-strategist; do
  copy_skill "$s" "$FO"
done
copy_context_dir "$CONTEXT_DIR/core" "$FO"
copy_context_dir "$CONTEXT_DIR/segments" "$FO"
copy_context_dir "$CONTEXT_DIR/outreach" "$FO"
copy_context_dir "$CONTEXT_DIR/copy-strategy" "$FO"
cp "$CONTEXT_DIR/enrichment/research-routes.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/hubspot-values.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/hubspot/territory-model.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/account-brief-template.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/call-intelligence.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/neocloud-strategy-brief.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/sales/email-bot-supplemental.md" "$FO/" 2>/dev/null
cp "$CONTEXT_DIR/product/proof-points.md" "$FO/" 2>/dev/null
echo "  Founder Outreach: $(ls "$FO" | wc -l) files"

# --- Account Intelligence ---
AI="$ENT_DIR/account-intelligence/upload"
mkdir -p "$AI"
for s in company-enrichment import-processor edge-case-researcher account-sourcing crm-hygiene pipeline-analytics territory-manager contact-discovery event-intelligence sales-enablement; do
  copy_skill "$s" "$AI"
done
copy_context_dir "$CONTEXT_DIR/core" "$AI"
copy_context_dir "$CONTEXT_DIR/segments" "$AI"
for d in hubspot enrichment product sales; do
  copy_context_dir "$CONTEXT_DIR/$d" "$AI"
done
cp "$CONTEXT_DIR/marketing/ai-copywriting-guidelines.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/linkedin-framework.md" "$AI/" 2>/dev/null
cp "$CONTEXT_DIR/marketing/sovereign-routing-explainer.md" "$AI/" 2>/dev/null
copy_context_dir "$CONTEXT_DIR/marketing/media-consumption" "$AI"
echo "  Account Intelligence: $(ls "$AI" | wc -l) files"

# --- General Assistant (everything) ---
GA="$ENT_DIR/general-assistant/upload"
mkdir -p "$GA"
for skill_dir in "$SKILLS_DIR"/*/; do
  copy_skill "$(basename "$skill_dir")" "$GA"
done
find "$CONTEXT_DIR" -name "*.md" -exec cp {} "$GA/" \;
echo "  General Assistant: $(ls "$GA" | wc -l) files"

echo ""
echo "=== Build Complete ==="
echo "Plugins: $(ls "$BUILDS_DIR/plugins-zipped/"*.zip 2>/dev/null | wc -l) zips"
echo "Skills:  $(ls "$BUILDS_DIR/skills-zipped/"*.zip 2>/dev/null | wc -l) zips"
echo "Enterprise: 4 upload folders"
echo ""
echo "Plugin zips:      $BUILDS_DIR/plugins-zipped/"
echo "Skill zips:       $BUILDS_DIR/skills-zipped/"
echo "Enterprise files: $ENT_DIR/*/upload/"
