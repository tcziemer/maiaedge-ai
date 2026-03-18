# Output Schemas

## Bot 1 Research Output Schema

Compile all research into this structure before moving to Stage 2:

```json
{
  "company_name": "string",
  "domain": "string",
  "domain_source": "provided | discovered",
  "hq_city": "string or null",
  "hq_state": "string or null",
  "employee_count": "number or null",
  "year_founded": "number or null",
  "company_description": "2-3 sentences",
  "infrastructure_metrics": {
    "data_center_count": "number or null",
    "total_square_feet": "number or null",
    "fiber_route_miles": "number or null",
    "lit_buildings": "number or null",
    "pop_count": "number or null",
    "states_served": "number or null",
    "countries_served": "number or null",
    "cabinet_count": "number or null",
    "mw_capacity": "number or null",
    "max_power_density_kw": "number or null"
  },
  "infrastructure_ownership": {
    "owns_dc_facilities": "boolean",
    "owns_fiber": "boolean",
    "owns_backbone": "boolean",
    "leases_from_carriers": "boolean",
    "carrier_neutral_facilities": "boolean"
  },
  "business_model": {
    "primary_revenue_source": "string",
    "revenue_model": "string",
    "sells_to_enterprises": "boolean",
    "sells_to_carriers": "boolean",
    "sells_to_hyperscalers": "boolean",
    "sells_wholesale": "boolean",
    "sells_retail": "boolean",
    "internal_use_only": "boolean"
  },
  "products_and_services": ["array of specific product/service names"],
  "named_customers": ["array of specific customer company names"],
  "customer_types": ["array"],
  "marketing_positioning": "their actual tagline",
  "competitive_landscape": "string",
  "recent_announcements": [
    {
      "date": "YYYY-MM (REQUIRED)",
      "headline": "string",
      "type": "expansion|acquisition|partnership|funding|product_launch|leadership|other",
      "details": "string with specific metrics"
    }
  ],
  "strategic_initiatives": ["array"],
  "leadership": {
    "ceo_name": "string or null",
    "ceo_background": "string or null",
    "cto_name": "string or null",
    "recent_leadership_changes": ["array"]
  },
  "technology_signals": {
    "has_customer_portal": "boolean",
    "has_api": "boolean",
    "has_self_service_provisioning": "boolean",
    "portal_platform_name": "EXACT branded name or null",
    "claimed_provisioning_speed": "string or null",
    "branded_products": ["array"],
    "automation_keywords_found": ["array"],
    "technology_partners": ["array"],
    "uses_megaport": "boolean",
    "uses_packetfabric": "boolean",
    "uses_equinix_fabric": "boolean",
    "uses_console_connect": "boolean",
    "uses_lumen": "boolean"
  },
  "ai_infrastructure_signals": {
    "gpu_cloud_tenants": ["SPECIFIC company names with source"],
    "ai_tenant_details": "string or null",
    "has_liquid_cooling": "boolean",
    "has_high_density_power": "boolean",
    "max_power_density_kw": "number or null",
    "uses_ai_marketing_language": "boolean",
    "in_ai_corridor": "boolean"
  },
  "directory_listings": {
    "peeringdb_type": "string or null",
    "peeringdb_asn": "string or null",
    "on_datacentermap": "boolean",
    "on_cloudscene": "boolean",
    "ntca_member": "boolean",
    "carrier_designation": "string or null"
  },
  "edge_case_resolution": {
    "was_edge_case": "boolean",
    "original_route": "string (e.g., 'Exclude Verification', 'ISP Verification', 'Broad Search')",
    "resolution": "reclassified | confirmed_exclude | flagged_for_review",
    "resolution_reasoning": "string explaining what was found and why",
    "reclassified_to": "segment name or null"
  },
  "raw_search_excerpts": ["3-5 most relevant excerpts with sources"]
}
```

## email_context Schema (Stage 4, Output 5)

This JSON goes into the Companion Data tab and serves as the handoff to the email bot skill.

```json
{
  "company_snapshot": "One sentence: what they are + key metrics",
  "what_theyve_built": "Their platform/network in one sentence with specifics",
  "portal_platform_name": "Exact branded name or null",
  "automation_boundary": "One sentence: where their automation stops",
  "the_gap": "One sentence: the specific provisioning pain point",
  "named_assets": {
    "products": ["array of product names"],
    "customers": ["array of customer names"]
  },
  "personalization_hooks": [
    "YYYY-MM: Hook with date",
    "Named customer or product reference",
    "Specific metric or achievement"
  ],
  "segment": "segment name",
  "customer_sub_segment": "sub-segment value or null",
  "ai_signals_detected": ["specific AI signals found"],
  "primary_hook": "Segment-appropriate main positioning",
  "core_problem": "Segment-appropriate pain statement",
  "avoid_claiming": "What NOT to say about this company",
  "sovereignty_language": ["Ownership phrases for this segment"],
  "discovery_questions": ["Questions for sales conversations"],
  "research_quality": "HIGH | MEDIUM | LOW",
  "fields_from_research": ["list of fields with real data"],
  "fields_from_fallback": ["list of fields using segment defaults"]
}
```
