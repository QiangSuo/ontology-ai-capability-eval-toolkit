# Gold Evidence Map: Generic Procurement Contract MVP

## Purpose

`gold_evidence_map.json` maps the gold ontology to concrete input artifacts in the MVP dataset.

This file is intended to help reviewers and future automated checks answer questions such as:

- Which source supports a concept, attribute, relation, event, rule, or action?
- Is an AI-generated ontology grounded in code, DDL, sample data, and documents?
- Did the AI tool cite enough sources for high-confidence conclusions?
- Did the AI tool over-infer business facts that are not present in the input dataset?

This round does not create acceptable aliases, known conflicts, or scoring scripts.

## Evidence Item Structure

Each evidence item contains:

- `evidence_id`: stable identifier for reference.
- `source_type`: one of `code`, `database_ddl`, `sample_data`, or `document`.
- `source_file`: relative path to an existing input file.
- `source_location`: table, column, class, method, document section, row range, or similar locator.
- `evidence_text` or `evidence_summary`: human-readable source excerpt or summary.
- `supports`: ontology element ids supported by this evidence.
- `confidence`: confidence that this source supports the listed element ids.

## How Evidence Chain Supports Scoring

The evidence map can support scoring without being a scoring script:

1. **Source grounding**: verify that an AI output does not invent concepts, fields, rules, or states absent from the dataset.
2. **Recall review**: compare AI-extracted elements against gold ontology ids and inspect whether expected evidence exists.
3. **Evidence quality**: reward outputs that cite the right source type and source location for each conclusion.
4. **Multi-source fusion**: reward concepts supported by multiple source types when the AI correctly combines them.
5. **Hallucination control**: flag outputs with high-confidence claims that lack corresponding evidence items.
6. **Uncertainty handling**: concepts or rules with weaker or narrower evidence can be reviewed manually instead of over-scored automatically.

## Source Type Roles

### Code Evidence

Code evidence is strongest for:

- Actions and business methods.
- Runtime validation rules.
- Status constants.
- Role constants.
- Service-level process logic.

Examples:

- `code.PurchaseRequestService.submitPR`
- `code.ApprovalService.requiredApproverRole`
- `code.ContractService.activateContract`
- `code.ReceiptInvoiceMatchingService.matchInvoice`
- `code.PaymentService.approvePayment`

### Database DDL Evidence

DDL evidence is strongest for:

- Concepts represented as tables.
- Attributes represented as columns.
- Relations represented as foreign keys.
- Status values represented by check constraints.
- Amount and timestamp fields.

Examples:

- `db.table.pc_purchase_request`
- `db.table.pc_contract`
- `db.table.pc_invoice`
- `db.column.pc_purchase_request.request_status`
- `db.column.pc_payment_request.payment_status`

### Sample Data Evidence

Sample data evidence is strongest for:

- Confirming observed statuses and enum-like values.
- Showing example relationships between records.
- Demonstrating realistic rows for lifecycle cases.
- Revealing partial/exception/held/cancelled states.

Examples:

- `csv.pc_purchase_request.rows`
- `csv.pc_approval_record.rows`
- `csv.pc_invoice.rows`
- `csv.pc_payment_request.rows`

### Document Evidence

Document evidence is strongest for:

- Business object definitions.
- Process flow.
- Role and permission semantics.
- Business rules and lifecycle descriptions.
- Glossary terms and source terminology.

Examples:

- `doc.business_overview.core_objects`
- `doc.procurement_process.approval_flow`
- `doc.contract_lifecycle.rules`
- `doc.role_permission_matrix.permissions`
- `doc.business_rules.invoice_payment`

## Multi-Source Cross Validation

A concept is multi-source validated when at least two source types support it. In this dataset, most core concepts have multi-source validation from DDL, code, sample data, and/or documents.

Examples:

- `concept:purchase_request`: DDL, code, sample data, documents.
- `concept:supplier`: DDL, code, sample data, documents.
- `concept:contract`: DDL, code, sample data, documents.
- `concept:purchase_order`: DDL, code, sample data, documents.
- `concept:invoice`: DDL, code, sample data, documents.
- `concept:payment`: DDL, code, sample data, documents.

## Single-Source Support

Single-source support is not automatically wrong, but it should lower confidence or require manual review.

In the generated evidence map, no core concept is intentionally limited to one source type. Some fine-grained attributes, rules, actions, or permissions may depend primarily on one source type, especially role-permission mappings from `documents/role_permission_matrix.md` or implementation-specific validation rules from service code.

## Reviewer Guidance

When reviewing an AI tool output:

- Treat exact wording differences as acceptable if the output maps to the same supported concept.
- Require stronger evidence for rules than for simple attributes.
- Prefer multi-source evidence for core concepts.
- Do not require every output to cite every evidence item; a correct concise evidence chain can be sufficient.
- Do not use this file as a rigid scoring script; use it as reference data for manual review or future scorer design.
