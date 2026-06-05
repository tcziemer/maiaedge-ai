# MaiaEdge Sales Documents Plugin

Generate standardized sales documents from templates. Documents must match exact formatting — only variable fields change.

## Document Types

| Document | Template | Helper Script | Specs |
|----------|----------|---------------|-------|
| **Order Form** | `templates/order_form_template_1.xlsx` | — | `references/order_form_specs.md` |
| **MSA** | `templates/msa_template.docx` | — | `references/msa_specs.md` |
| **POC Agreement** | `templates/poc_agreement_template.docx` | `scripts/build_poc.py` | `references/poc_specs.md` |
| **NDA** | `templates/nda_template.docx` | `scripts/build_nda.py` | `references/nda_specs.md` |

## Skills

- `sales-docs` — Main document generation skill (covers all 4 doc types)

## References

- `price_list.md` — Authoritative SKU pricing (rev 1.21.2026)
- `order_form_specs.md` — Order Form cell positions and layout
- `msa_specs.md` — MSA template structure and variable fields
- `poc_specs.md` — POC Agreement template structure
- `nda_specs.md` — NDA template structure

## Commands

- `/generate-order-form` — Create an Order Form with SKU pricing
- `/generate-msa` — Create a Master Subscription Agreement
- `/generate-poc` — Create a Proof of Concept Agreement
- `/generate-nda` — Create a Mutual Non-Disclosure Agreement

## Logos

- `MaiaEdge_Logo_Horizontal_RGB.png` — For Order Forms, MSAs, NDAs
- `MaiaEdge_Logo_Horizontal_RevWhite.png` — For POC Agreements

## Default Output

PDF (primary) + editable source file (.docx/.xlsx). Use `libreoffice --headless --convert-to pdf` for conversion.
