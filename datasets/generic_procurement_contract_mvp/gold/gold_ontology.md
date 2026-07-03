# Gold Ontology: Generic Procurement Contract MVP

## Purpose

This document explains the design of `gold_ontology.json` for the `generic_procurement_contract_mvp` input dataset.

This round creates only the gold ontology. It does not create a gold evidence map, acceptable aliases file, known conflicts file, or scoring script.

## Design Principles

1. **Input-grounded only**: every concept is supported by the generated source code, DDL, CSV sample data, or business documents.
2. **Business concepts only**: technical implementation objects such as Controller, Service, DTO, Mapper, repository, package, framework annotation, or method container are not treated as business ontology concepts.
3. **Aliases stay inside concepts**: source-level naming differences such as Supplier/Vendor, Purchase Request/PR, Goods Receipt/GRN, and Payment Request/Payment Application are represented as aliases inside the relevant concept.
4. **No separate evidence map**: `evidence_refs` are lightweight placeholders pointing to input source types or artifacts; they are not a detailed evidence map.
5. **Lifecycle-aware**: objects with state fields in DDL, code, or documents include lifecycle states.
6. **Evaluation-friendly**: core required concepts are separated from optional bonus concepts so downstream review can distinguish must-have coverage from enrichment.

## Core Concept Model

The ontology follows the main business flow:

```text
Department / Employee
  -> PurchaseRequest
  -> PurchaseRequestItem / Material
  -> ApprovalTask
  -> Supplier
  -> Contract
  -> PurchaseOrder
  -> GoodsReceipt
  -> Invoice
  -> Payment
```

## Core Concepts

| Concept | Why It Is Included |
|---|---|
| PurchaseRequest | Central procurement demand object supported by DDL, source code, CSV, and documents. |
| PurchaseRequestItem | Line-level requested item/service object supported by DDL, code, and CSV. |
| ApprovalTask | Approval workflow record for requests and payments, supported by DDL, CSV, and role documents. |
| Supplier | External provider; also appears as Vendor in code. |
| Contract | Legal agreement created from approved requests and suppliers. |
| PurchaseOrder | Operational order released against active contracts. |
| GoodsReceipt | Warehouse receipt/GRN used for fulfillment and invoice matching. |
| Invoice | Supplier billing document matched against PO and receipt. |
| Payment | Payment request/application for matched invoices. |
| Department | Organizational owner of requests and users. |
| Employee | Internal user/actor performing requester, approver, legal, warehouse, AP, or admin actions. |
| Material | Requested good/service represented through request line item description and category. |

## Core Required Items

The following concepts are core required coverage for ontology extraction:

- PurchaseRequest
- PurchaseRequestItem
- ApprovalTask
- Supplier
- Contract
- PurchaseOrder
- GoodsReceipt
- Invoice
- Payment
- Department
- Employee
- Material

These are required because they are directly present in the input dataset and necessary to reconstruct the procurement-to-payment lifecycle.

## Optional Bonus Items

No standalone optional bonus concepts are defined in this first gold ontology. Evaluators may award qualitative credit if an AI tool extracts useful substructures such as:

- Procurement category
- Cost center
- Inspection result
- Invoice matching variance
- Contract termination reason
- Approval step name

These should be treated as attributes or enrichment details unless a future dataset version adds independent business objects for them.

## Lifecycle Coverage

The gold ontology includes lifecycle states for:

- PurchaseRequest: DRAFT, SUBMITTED, APPROVED, REJECTED, CANCELLED
- ApprovalTask: PENDING, APPROVED, REJECTED, SKIPPED
- Supplier: ACTIVE, SUSPENDED, PENDING_REVIEW
- Contract: DRAFT, LEGAL_REVIEW, ACTIVE, EXPIRED, TERMINATED
- PurchaseOrder: RELEASED, PARTIALLY_RECEIVED, CLOSED, CANCELLED
- GoodsReceipt: PENDING, PARTIAL, COMPLETE, REJECTED
- Invoice: PENDING_MATCH, MATCHED, EXCEPTION, CANCELLED
- Payment: REQUESTED, APPROVED, PAID, HELD, CANCELLED

## Rule Coverage

The gold ontology covers rules visible in the input data, including:

- Purchase request requires at least one line item.
- Purchase request requires business justification before submission.
- Normal requests require department manager approval.
- High-value requests require finance approval.
- Rejection requires comment.
- Supplier must be active and not high risk for new award.
- Contract requires legal approval before activation.
- Purchase order requires active contract.
- Goods receipt requires receiving time.
- Invoice must be matched before payment.
- Invoice variance must be within allowed tolerance or become exception.
- Payment requires finance approval before being paid.

## Exclusions

The ontology intentionally excludes:

- Java controller classes
- Java service classes
- Java packages
- Framework or persistence artifacts
- DTOs, mappers, repositories, or method containers
- Gold evidence map entries
- Scoring logic
- Known conflict answer keys

## Notes on Material

The input dataset does not contain a standalone material master table. `Material` is still included because the user explicitly requires it and the input data supports it through `PurchaseRequestLine.item_description`, `category_code`, `unit_of_measure`, and CSV line item rows. Its confidence is lower than table-backed objects.
