# Known Conflicts: Generic Procurement Contract MVP

## Purpose

`known_conflicts.json` lists lightweight, source-grounded inconsistencies and ambiguities in the MVP procurement dataset.

These conflicts are designed to test whether an AI tool can:

- Recognize naming inconsistencies across source types.
- Avoid duplicate concepts caused by aliases or abbreviations.
- Compare business rules from code, DDL, documents, and sample data.
- Detect missing structural evidence for document-only rules.
- Preserve uncertainty instead of hallucinating missing fields or forcing false precision.

This file is not a scoring script.

## Conflict Types

The known conflict set covers:

- `naming_inconsistency`
- `field_semantic_ambiguity`
- `status_definition_mismatch`
- `document_vs_database_mismatch`
- `code_vs_document_mismatch`
- `missing_evidence`

## Conflict Summary

| Conflict ID | Type | Severity | What It Tests |
|---|---|---:|---|
| `conflict:naming.supplier_vendor` | naming_inconsistency | low | Supplier/Vendor alias normalization and duplicate concept control |
| `conflict:naming.purchase_request_pr` | naming_inconsistency | low | PR abbreviation handling and PR vs PO boundary |
| `conflict:naming.goods_receipt_grn` | naming_inconsistency | low | GRN abbreviation from document and CSV identifiers |
| `conflict:naming.payment_request_application` | naming_inconsistency | low | Payment Request vs Payment Application business term normalization |
| `conflict:rule.approval_threshold_boundary` | code_vs_document_mismatch | medium | `>= 50000` vs `> 50000` approval threshold boundary |
| `conflict:rule.invoice_matching_tolerance` | code_vs_document_mismatch | medium | 2% policy tolerance vs 1.5% code tolerance |
| `conflict:contract.activation_signature_evidence` | missing_evidence | medium | Document-only signature requirement missing from DDL/code |
| `conflict:field.material_without_master_table` | missing_evidence | low | Material semantics without standalone material master table |
| `conflict:field.employee_user_role_semantics` | field_semantic_ambiguity | medium | Employee/User actor vs Role/Permission semantics |
| `conflict:status.goods_receipt_complete_closed` | status_definition_mismatch | low | Receipt COMPLETE vs PO CLOSED status ownership |
| `conflict:document_vs_database.payment_hold_reason` | document_vs_database_mismatch | low | Hold reason policy lacks DDL/CSV field support |
| `conflict:field.approval_record_polymorphic_target` | field_semantic_ambiguity | low | Approval target_type/target_id polymorphic relation inference |

## How These Conflicts Test Multi-Source Fusion

### Naming and Alias Fusion

Naming conflicts test whether an AI can merge equivalent terms without creating duplicate concepts:

- Supplier / Vendor
- Purchase Request / PR
- Goods Receipt / GRN
- Payment Request / Payment Application

A good output should map aliases to one canonical concept and preserve source mappings.

### Rule Comparison

Rule conflicts test whether an AI compares source-specific business logic:

- Approval threshold: documents and DDL use `>= 50000`, code uses `> 50000`.
- Invoice matching tolerance: policy says 2%, code uses 1.5%.

A good output should preserve both sources and mark the mismatch, especially for boundary conditions.

### Missing Evidence and Hallucination Control

Missing evidence conflicts test whether an AI avoids inventing unsupported fields:

- Contract signature requirement exists in documents but not in DDL/code fields.
- Held payment reason is documented but not stored in `pc_payment_request`.
- Material semantics exist in request lines but not in a material master table.

A good output can record these as documented rules or uncertainties without creating false schema attributes.

### Field Semantics and Relation Inference

Field ambiguity conflicts test whether an AI understands polymorphic or overloaded fields:

- `pc_user.role_code` means employee role, not separate employee instances.
- `pc_approval_record.target_type` and `target_id` create polymorphic relations to request, contract, or payment.

A good output should model these carefully and lower confidence where relations are inferred rather than explicit foreign keys.

### Status Ownership

Status mismatch conflicts test whether an AI assigns status values to the right lifecycle owner:

- Goods Receipt uses `COMPLETE`.
- Purchase Order uses `CLOSED`.

A good output should not merge all statuses into one global state machine.

## Scoring Impact Guidance

These conflicts can affect scoring in four ways:

1. **Positive credit**: AI identifies the conflict, cites both sources, and records uncertainty or conflict explicitly.
2. **Partial credit**: AI extracts both facts but does not label them as conflicting.
3. **Penalty**: AI chooses one side with high confidence and omits the other source.
4. **Red flag**: AI invents unsupported fields, concepts, states, or rules to force consistency.

Suggested review treatment:

- Low severity conflicts should not heavily penalize otherwise correct extraction, but they should reveal fusion quality.
- Medium severity conflicts should affect rule-quality and uncertainty-quality evaluation.
- Any hallucinated schema element created to hide a missing-evidence conflict should be treated as a stronger negative signal.

## What This File Does Not Do

This file does not:

- Implement scoring.
- Define acceptable aliases.
- Replace the gold ontology.
- Replace the gold evidence map.
- Require every AI output to use the exact conflict wording.

It provides reference conflicts and scoring guidance for human review or future scorer implementation.
