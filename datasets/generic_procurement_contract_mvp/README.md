# Generic Procurement Contract MVP Dataset

## Purpose

This is an input-only MVP dataset for testing whether an AI tool can extract an ontology from a small but complete enterprise procurement approval and contract fulfillment system.

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

## Input Categories

This dataset contains only four input types:

1. Source code: simplified Java Spring Boot-style source files under `source_code/`
2. Database DDL: SQL schema under `database/ddl.sql`
3. Sample data CSV: database-like sample rows under `database/sample_data/`
4. Business documents: Markdown process and policy documents under `documents/`

## Explicitly Not Included

This MVP input bundle intentionally does not include:

- Gold ontology
- Gold evidence map
- Acceptable aliases file
- Known conflicts file
- Scoring scripts
- Screenshots
- Web crawler data
- PDF files
- Excel files
- Real customer data

## Suggested Test Scope

### Smoke Test

Use a subset of:

- `database/ddl.sql`
- `documents/business_overview.md`
- `documents/procurement_process.md`
- `source_code/src/main/java/com/example/procurement/service/PurchaseRequestService.java`
- `source_code/src/main/java/com/example/procurement/service/ApprovalService.java`
- 3-5 rows from core CSV files

Expected duration: 1-2 hours.

### Standard Test

Use the full dataset:

- All Java source files
- Full DDL
- All CSV files
- All business documents
- Dataset manifest

Expected duration: 0.5-1 day.

## Fictional Data Statement

All departments, people, suppliers, contract numbers, purchase request numbers, purchase order numbers, invoice numbers, payment numbers, amounts, dates, and notes are fictional. They do not describe real companies, real people, real customers, or real transactions.

## Input Design Notes

The dataset contains mild naming differences across sources. These are intended to test multi-source fusion, alias handling, uncertainty expression, and conflict handling. They are not standard answers.

Examples include:

- Business documents usually say `Supplier`; some source code methods say `Vendor`.
- Business documents use `Purchase Request`; code and CSV sometimes use `PR`.
- Business documents use `Goods Receipt` and `GRN`; DDL uses `goods_receipt`.
- Business documents say `Payment Application`; DDL uses `payment_request`.
- Approval threshold language is intentionally close but not identical across sources.
- Invoice matching tolerance is described differently in policy and code.
