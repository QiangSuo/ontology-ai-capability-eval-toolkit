# Known Screenshot Surrogate Conflicts

This evaluator-only file summarizes expected UI/screenshot-surrogate conflicts for optional screenshot evaluation. It must not be provided to the AI tool under evaluation.

- JSON source: `known_conflicts.screenshot.json`
- Evidence map: `gold_evidence_map.screenshot.json`
- Input mode: `surrogate_only`
- Real image/OCR coverage: not included

## Conflict Types

- `ui_vs_database_naming_mismatch`
- `screenshot_only_business_term`
- `role_permission_ui_vs_doc_mismatch`
- `button_action_ambiguity`
- `visible_status_mismatch`

## Conflict Summary

| Conflict ID | Type | Severity | Expected handling |
| --- | --- | --- | --- |
| `conflict:screenshot.naming.vendor_supplier` | `ui_vs_database_naming_mismatch` | low | Normalize Vendor to Supplier and preserve Vendor as UI alias. |
| `conflict:screenshot.naming.grn_goods_receipt` | `ui_vs_database_naming_mismatch` | low | Normalize GRN to Goods Receipt and preserve it as abbreviation. |
| `conflict:screenshot.action.return_for_revision` | `screenshot_only_business_term` | medium | Treat Return as screenshot-only candidate or uncertainty. |
| `conflict:screenshot.role.activate_contract_visibility` | `role_permission_ui_vs_doc_mismatch` | medium | Do not infer final permission only from UI button visibility. |
| `conflict:screenshot.rule.invoice_difference_percent` | `screenshot_only_business_term` | medium | Treat Difference % as UI signal; do not invent tolerance threshold. |
| `conflict:screenshot.status.payment_paid` | `visible_status_mismatch` | low | Map payment PAID carefully without merging unrelated lifecycle states. |

## Review Guidance

A strong screenshot-surrogate output should:

- declare `input_mode = surrogate_only`;
- preserve `screen:*` evidence handles;
- treat UI-only actions and status labels as candidates unless confirmed by other sources;
- record UI/database/document naming differences as aliases, mappings, conflicts or uncertainties;
- avoid claims about real screenshots, OCR, visual regions, icons or coordinates.
