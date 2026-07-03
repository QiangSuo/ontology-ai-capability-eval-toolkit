# Generic Procurement Contract MVP Dataset

## Purpose

This is the MVP dataset for testing whether an AI tool can extract an ontology from a small but complete enterprise procurement approval and contract fulfillment system.

The dataset is fictional and can be used offline. It is designed for Smoke Test and Standard Test runs.

## Business Domain

Enterprise procurement approval and contract fulfillment:

- Purchase request creation and approval
- Supplier selection
- Contract lifecycle management
- Purchase order release
- Goods receipt
- Invoice matching
- Payment request approval and payment execution
- Contract performance tracking

## Directory Roles

This dataset directory contains both **input materials** and **reference/scoring materials**. They must not be mixed during an evaluation.

### Inputs That May Be Provided To The AI Tool

Only these paths are evaluation inputs:

1. Source code: simplified Java Spring Boot-style source files under `source_code/`
2. Database DDL: SQL schema under `database/ddl.sql`
3. Sample data CSV: database-like sample rows under `database/sample_data/`
4. Business documents: Markdown process and policy documents under `documents/`
5. Dataset metadata/manifest when the operator needs file inventory: `metadata/dataset_manifest.json`

### Reference / Scoring Materials Not To Provide To The AI Tool

The following files exist in the repository but are **not** input materials for the AI under evaluation:

- `gold/gold_ontology.json` and `gold/gold_ontology.md`
- `gold/gold_evidence_map.json` and `gold/gold_evidence_map.md`
- `gold/acceptable_aliases.json` and `gold/acceptable_aliases.md`
- `gold/known_conflicts.json` and `gold/known_conflicts.md`
- Any files under `results/demo_baseline/`
- Any scoring output such as `machine_score.json` or `machine_score.md`

These files are used only by the evaluator for scoring, review, consistency checks and demo explanation. Providing them to the AI tool would leak the answer key.

## Suggested Test Scope

### Smoke Test

Use this exact smoke subset unless the evaluation lead approves a change.

#### DDL

- `database/ddl.sql` — full file

#### Documents

- `documents/business_overview.md` — full file
- `documents/procurement_process.md` — full file

#### Source Code

- `source_code/src/main/java/com/example/procurement/service/PurchaseRequestService.java` — full file
- `source_code/src/main/java/com/example/procurement/service/ApprovalService.java` — full file

#### CSV Slice

If the tool can read local files, the operator may provide whole CSV files. If the operator must copy/paste, use header + first 5 data rows and record `sample_is_partial = true`.

| CSV | Smoke slice |
| --- | --- |
| `database/sample_data/pc_purchase_request.csv` | header + rows 1-5 |
| `database/sample_data/pc_purchase_request_line.csv` | header + rows 1-5 |
| `database/sample_data/pc_approval_record.csv` | header + rows 1-5 |
| `database/sample_data/pc_contract.csv` | header + rows 1-5 |
| `database/sample_data/pc_invoice.csv` | header + rows 1-5 |
| `database/sample_data/pc_payment_request.csv` | header + rows 1-5 |

Expected duration: 1-2 hours.

### Standard Test

Use the full input dataset:

- All Java source files under `source_code/`
- Full `database/ddl.sql`
- All CSV files under `database/sample_data/`
- All business documents under `documents/`
- Dataset manifest for file inventory only

Expected duration: 0.5-1 day.

## Fictional Data Statement

All departments, people, suppliers, contract numbers, purchase request numbers, purchase order numbers, invoice numbers, payment numbers, amounts, dates, and notes are fictional. They do not describe real companies, real people, real customers, or real transactions.

## Input Design Notes

The input materials contain mild naming differences and a few documented source conflicts. These are intended to test multi-source fusion, alias handling, uncertainty expression and conflict handling. They are not standard answers.

Examples include:

- Business documents usually say `Supplier`; some source code methods say `Vendor`.
- Business documents use `Purchase Request`; code and CSV sometimes use `PR`.
- Business documents use `Goods Receipt` and `GRN`; DDL uses `goods_receipt`.
- Business documents say `Payment Application`; DDL uses `payment_request`.
- Approval threshold language is intentionally close but not identical across sources.
- Invoice matching tolerance is described differently in policy and code.

Operators should not manually resolve these differences before giving inputs to the AI. The AI tool should detect and explain them as aliases, conflicts or uncertainties.
