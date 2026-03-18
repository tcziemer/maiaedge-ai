---
name: maiaedge-sales-docs
description: "MaiaEdge sales document generator for Order Forms, MSAs, POC Agreements, and NDAs. Use when creating (1) Order Forms/Quotes with SKU pricing, (2) Master Subscription Agreements, (3) Proof of Concept Agreements, or (4) Mutual NDAs. Generates standardized documents matching exact MaiaEdge templates with variable customer info, SKUs, and pricing. Handles discount calculations, multi-unit orders, and term lengths (12/36/60 months or 60-day POC). Also use when the user mentions quotes, agreements, contracts, order forms, NDAs, POC agreements, or any customer-facing sales document for MaiaEdge."
---

# MaiaEdge Sales Document Generator

Generate standardized sales documents from templates. **Documents must match exact formatting — only variable fields change.**

## Template Replication Rules

1. **NEVER modify boilerplate language** — Only populate variable fields
2. **Match exact structure** — Same rows, columns, sections as templates
3. **Preserve all formatting** — Fonts, colors, borders, merges, wrap text
4. **Copy templates directly** — Load the actual template files and only change variables
5. **Validate before generating** — Confirm all required fields are provided first

## Document Types & Templates

| Document | Template File | Default Output | Detailed Specs |
|----------|---------------|----------------|----------------|
| **Order Form** | `order_form_template_1.xlsx` | `.pdf` (+ `.xlsx` source) | `order_form_specs.md` |
| **MSA** | `msa_template.docx` | `.pdf` (+ `.docx` source) | `msa_specs.md` |
| **POC Agreement** | `poc_agreement_template.docx` | `.pdf` (+ `.docx` source) | `poc_specs.md` |
| **NDA** | `nda_template.docx` | `.pdf` (+ `.docx` source) | `nda_specs.md` |

> **Default output is PDF.** Always convert the final document to PDF using LibreOffice (`libreoffice --headless --convert-to pdf`). Deliver the PDF as the primary output and keep the editable source file (.docx/.xlsx) as a secondary deliverable. If the user specifically asks for .docx or .xlsx only, skip PDF conversion.

> **Finding files:** All templates, logos, scripts, and reference specs are uploaded to this project. Reference them by filename. If a template file isn't in the project context, ask the user to upload it.

## Logo Files

| Logo File | Use For |
|-----------|---------|
| `MaiaEdge_Logo_Horizontal_RGB.png` | Order Forms, MSAs, NDAs (dark logo) |
| `MaiaEdge_Logo_Horizontal_RevWhite.png` | POC Agreements (white logo) |

## Helper Scripts

POC Agreements and NDAs have bundled builder scripts that handle all variable replacement deterministically. Use these when available — they're faster and more reliable than writing python-docx code from scratch.

| Script | Purpose | Input |
|--------|---------|-------|
| `build_poc.py` | Generate POC Agreement | JSON with customer, equipment, locations, signers |
| `build_nda.py` | Generate NDA | JSON with date, participant, signer |

Usage: `python build_poc.py --input data.json --template poc_agreement_template.docx`

See the reference files (`poc_specs.md`, `nda_specs.md`) for the JSON input schema and manual approach.

---

## REQUIRED INFORMATION VALIDATION

**Before generating ANY document, verify ALL required fields are provided. If anything is missing, ASK the user — NEVER generate with blank or placeholder fields.**

### Order Form — Required Fields

| Field | Example |
|-------|---------|
| Customer company name | "Horizon Fiber Networks" |
| Customer full address | "4500 Innovation Pkwy, Ste 200, Austin, TX 78745" |
| Customer contact name | "Sarah Mitchell" |
| Customer contact email | "smitchell@horizonfiber.net" |
| Customer phone number | "(512) 555-0198" |
| Customer website | "www.horizonfiber.net" |
| Quote number | "1024" |
| Quote date | "02_12_26" |
| Subscription start date | "3/1/2026" |
| Product SKU(s) + quantity + term | "2x ME-PBC-PCE-10G-36M" |
| MSA reference date | "12/15/2025" |
| Discount % | **ONLY if explicitly requested by user** |

### MSA — Required Fields

| Field | Example |
|-------|---------|
| Customer legal name | "IENTC Telecom, S.A. de C.V." |
| Customer address | "Av. Insurgentes Sur 1602, Mexico City" |
| Effective date | "February 15, 2026" |

### POC Agreement — Required Fields

| Field | Example |
|-------|---------|
| Date | "March 6, 2026" |
| Customer company name | "Datum, Inc." |
| Customer contact name | "Manish Singh" |
| POC duration | "90 days from date of first hardware delivery" |
| Equipment (SKU + description + qty) | "ME-PBC-PCE-100G, Path Border Controller + PCE License 100G, Qty 3" |
| POC fee (complimentary or amount) | "Complimentary" or "$2,490 per unit" |
| Delivery locations (contact + address) | "Manish Singh, Dallas TX" |
| MaiaEdge signer name + title | "Tim Ziemer, CRO & Co-Founder" |
| Customer signer name + title | "Manish Singh, CTO" |

### NDA — Required Fields

| Field | Example |
|-------|---------|
| Effective date | "March 6, 2026" |
| Participant company name | "Datum, Inc." |
| Participant address | "100 Main Street, Suite 400, Dallas, TX 75201" |
| Participant signer name | "Manish Singh" |
| Participant signer title | "CTO" |

---

## ORDER FORM GENERATION

For detailed formatting specs, row heights, column widths, and implementation code → read `order_form_specs.md`.

### Process

1. **Validate required fields** (see table above)
2. **Copy template** `order_form_template_1.xlsx` → working file
3. **CLEAR old template data** from buyer cells (D6:D11), signature cells (B53:B57), B27, and A50
4. **Populate** all variable fields (header, buyer, products, totals, MSA ref, signatures)
5. **Format** (borders, merges, column widths, row heights, page setup)
6. **Run recalc.py** to calculate formulas — path: `.skills/skills/xlsx/scripts/recalc.py`
7. **AFTER recalc**: Apply rich text formatting (bold section headings in merged cells)
8. **Save** `.xlsx` → **Convert to PDF** with LibreOffice (do NOT recalc again)

### Key Rules

- **Annual Price** goes on the Order Form, NOT TCV. `Annual Price = TCV ÷ Term Years`
- **Quote # in F2, Date in F3** (labels in E2/E3) — NOT columns F/G
- **Buyer info in column D (rows 6-11)**, seller in column A — NO merged cells in header
- **Signature block: seller in column A, customer in column B** — NOT A:C / D:G
- **ALWAYS clear old template data** from buyer cells (D6:D11), signature cells (B53:B57), B27, and A50 before populating
- Subscription start date: label stays in A27, date goes in B27 (two cells, not one)
- Sections 1-5 have heading rows (A29, A33...) and body rows (A31, A35...) as separate cells
- Rich text in body cells only needed AFTER recalc if formatting was stripped

---

## MSA GENERATION

For the full template structure and all 11 section headings → read `msa_specs.md`.

### Process

1. **Validate required fields** (see table above)
2. **Load template**: `msa_template.docx`
3. **Find and replace** only 3 variable fields using content-based search:
   - `______` after "dated as of" → Effective Date
   - `_________________________` → Customer legal name
   - `___________________________________` → Customer address
   - Customer name in the signature block section
4. **Save** as `[CustomerShortName]_MSA_[EffectiveDate].docx`
5. **Convert to PDF**: `libreoffice --headless --convert-to pdf [filename].docx`

Do NOT modify any numbered sections, Exhibits, or legal definitions.

---

## POC AGREEMENT GENERATION

For the complete template structure, variable field mapping, formatting reference, and python-docx implementation → read `poc_specs.md`.

### Process (Preferred — use script)

1. **Validate required fields** (see table above)
2. **Prepare JSON input** with all required fields
3. **Run**: `python build_poc.py --input data.json --template poc_agreement_template.docx`
4. **Verify output** against the checklist in `poc_specs.md`
5. **Convert to PDF**: `libreoffice --headless --convert-to pdf [filename].docx`

### Process (Manual — if script unavailable)

1. **Validate required fields**
2. **Load template**: `poc_agreement_template.docx`
3. **Replace header fields** (Date, Customer, Contact, Duration) using content-based paragraph search
4. **Replace logo** in Table 0 with white logo file (`MaiaEdge_Logo_Horizontal_RevWhite.png`)
5. **Populate equipment table** (Table 1) — clear data rows, add new rows
6. **Populate delivery table** (Table 2) — clear data rows, add new rows
7. **Update Section 1** body with customer name (replace "Datum, Inc.")
8. **Update Section 6** fees description if not complimentary
9. **Update signature table** (Table 3) with both signers
10. **Save** as `[CustomerShortName]_POC_Agreement_[Date].docx`
11. **Convert to PDF**: `libreoffice --headless --convert-to pdf [filename].docx`

---

## NDA GENERATION

For the complete template structure, content-based search patterns, and formatting reference → read `nda_specs.md`.

### Process (Preferred — use script)

1. **Validate required fields** (see table above)
2. **Prepare JSON input** with all required fields
3. **Run**: `python build_nda.py --input data.json --template nda_template.docx`
4. **Verify output** against the checklist in `nda_specs.md`
5. **Convert to PDF**: `libreoffice --headless --convert-to pdf [filename].docx`

### Process (Manual — if script unavailable)

1. **Validate required fields**
2. **Load template**: `nda_template.docx`
3. **Replace effective date** — find paragraph containing `"________, 202_"`, replace with date
4. **Replace participant name** — find paragraph containing "Participant:" tab, replace blanks
5. **Replace participant address** — find paragraph containing "Address:" tab, replace blanks (2 lines)
6. **Replace signer name** — find "Printed Name:" paragraph, replace SECOND set of blanks
7. **Replace signer title** — find "Title:" paragraph, replace SECOND set of blanks
8. **Save** as `[CustomerShortName]_NDA_[EffectiveDate].docx`
9. **Convert to PDF**: `libreoffice --headless --convert-to pdf [filename].docx`

Use content-based searching, NOT hardcoded paragraph indices. The NDA has no tables and no images.

---

## PRICING REFERENCE

Always verify prices against `price_list.md` before generating any document. That file is the authoritative source.

### Pricing Display Rule

Order Forms show **Annual Price**, not TCV:

```
Annual Price = TCV ÷ Term Years
  12-month: Annual = TCV (same)
  36-month: Annual = TCV ÷ 3
  60-month: Annual = TCV ÷ 5
  POC: Flat fee (no conversion)
```

### Discount Policy

**DO NOT apply any discount unless the user explicitly requests one.**

- Default pricing = List Price (no discount)
- Only apply a discount if the user specifically states a discount percentage
- If the user mentions a discount, confirm the percentage and which products it applies to
- HA/Standby units are always 30% off the corresponding primary unit — this is standard pricing, not a discount

---

## MaiaEdge Seller Information (All Documents)

```
MaiaEdge Inc.
77 S. Bedford St., Suite 150
Burlington, MA 01803
Email: timziemer@maiaedge.io
Contact: Tim Ziemer
Terms: Net 30
```

---

## Product Descriptions (Use Exactly in Order Forms)

**PBC 100G**: "Includes Path Border Controller and Path Computation Engine. Equipped with dual 100 Gbps uplink interfaces, licensed for up to 100 Gbps throughput. Contract term: [X] months."

**PBC 10G**: "Includes Path Border Controller, Interface Optics and Path Computation Engine. Equipped with dual 100 Gbps uplink interfaces, licensed for up to 10 Gbps throughput. Contract term: [X] months."

**PBC 1G**: "Includes Path Border Controller, Interface optics and Path Computation Engine. Equipped with dual 100 Gbps uplink interfaces, licensed for up to 1 Gbps throughput. Contract term: [X] months."

**Standby/HA PBC**: "Standby/HA unit. [Same as primary description]"

**MPP-48**: "Port extender for additional port density at aggregation or interconnect locations. Contract term: [X] months."

**POC Products**: "Licensed for POC/evaluation use only. [Base description]. POC term: 60 days."

---

## Output File Naming

All documents output as PDF by default (plus the editable source file):

- **Order Form**: `[CustomerShortName]_OrderForm_[QuoteNumber].pdf` (+ `.xlsx`)
- **MSA**: `[CustomerShortName]_MSA_[EffectiveDate].pdf` (+ `.docx`)
- **POC Agreement**: `[CustomerShortName]_POC_Agreement_[Date].pdf` (+ `.docx`)
- **NDA**: `[CustomerShortName]_NDA_[EffectiveDate].pdf` (+ `.docx`)
