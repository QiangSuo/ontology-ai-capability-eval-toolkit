# Acceptable Aliases: Generic Procurement Contract MVP

## Purpose

`acceptable_aliases.json` defines acceptable names for matching AI-generated ontology outputs to canonical ids in `gold_ontology.json`.

This file exists to avoid false negatives during future automated or semi-automated scoring when an AI tool uses a valid alternate name, abbreviation, database name, code name, Chinese name, or business term.

This round does not create known conflicts and does not create a scoring script.

## Alias Types

The alias map uses these alias types:

- `Chinese name`: Chinese business names such as `采购申请`, `供应商`, `付款申请`.
- `English name`: standard English names such as `Purchase Request`, `Supplier`, `Invoice`.
- `abbreviation`: short forms such as `PR`, `PO`, `GRN`.
- `database name`: table or column names such as `pc_purchase_request`, `request_status`.
- `code name`: Java class, method, field, or camelCase names such as `PurchaseRequest`, `requestStatus`.
- `UI/business term`: non-technical business terms such as `Payment Application`, `Agreement`, `receipt record`.

## Core Concept Alias Summary

| Canonical Concept | Main Acceptable Aliases |
|---|---|
| PurchaseRequest | 采购申请, 采购需求, PR, Purchase Request, purchase requisition, pc_purchase_request |
| PurchaseRequestItem | 采购申请行, 采购申请明细, PR line, line item, PurchaseRequestLine, pc_purchase_request_line |
| ApprovalTask | 审批任务, 审批记录, Approval Record, Approval Step, decision record, pc_approval_record |
| Supplier | 供应商, 供方, Supplier, Vendor, external provider, pc_supplier |
| Contract | 合同, 采购合同, Contract, Agreement, pc_contract |
| PurchaseOrder | 采购订单, PO, Purchase Order, PurchaseOrder, pc_purchase_order |
| GoodsReceipt | 收货单, 收货记录, 到货验收, Goods Receipt, GRN, receipt record, pc_goods_receipt |
| Invoice | 发票, 供应商发票, Invoice, supplier invoice, billing document, pc_invoice |
| Payment | 付款, 付款申请, Payment Request, Payment Application, PaymentRequest, pc_payment_request |
| Department | 部门, 业务部门, Department, business department, cost center owner, pc_department |
| Employee | 员工, 用户, 系统用户, Employee, User, requester, approver, pc_user |
| Material | 物料, 采购物料, 服务项目, Item, goods, service item, item_description, category_code |

## Easily Misleading Aliases

Some aliases are acceptable only with context:

- `request`: acceptable for `PurchaseRequest` only in procurement request context. It must not match any generic request in code or HTTP controller names.
- `订单`: acceptable for `PurchaseOrder` only when it clearly means procurement order. It must not be used for purchase request.
- `采购单`: ambiguous. It can refer to purchase order in this dataset only when source context points to PO/order release.
- `账单`: acceptable for `Invoice` only when supplier billing context is clear.
- `requester` and `approver`: acceptable aliases for `Employee` only when referring to internal actors, not roles as standalone role definitions.
- `Vendor`: acceptable for `Supplier`; it must not imply a separate Vendor concept.
- `Agreement`: acceptable for `Contract`; it must not imply Payment agreement or approval agreement.

## Explicit Non-Equivalence Boundaries

The following concepts must not be merged:

### PurchaseRequest vs PurchaseOrder

- `PurchaseRequest` / `PR` / `采购申请` is a demand and approval object before sourcing and ordering.
- `PurchaseOrder` / `PO` / `采购订单` is an operational order released after contract activation.
- They are related but not equivalent.

### PurchaseRequestItem vs Material

- `PurchaseRequestItem` is a line record with quantity, UOM, estimated price, and line amount.
- `Material` is the requested good or service semantics derived from item description/category.
- A line can describe a material, but the line is not the same thing as the material.

### ApprovalTask vs Payment

- `ApprovalTask` records a workflow decision.
- `Payment` / `Payment Request` is the finance object for paying an invoice.
- Payment approvals may create approval records, but the concepts are not equivalent.

### Supplier vs Employee

- `Supplier` / `Vendor` is an external provider.
- `Employee` / `User` is an internal actor.
- Contact fields do not make them equivalent.

### Contract vs PurchaseOrder

- `Contract` / `Agreement` is a legal agreement.
- `PurchaseOrder` / `PO` is an operational order against a contract.
- One contract may enable one or more purchase orders.

### GoodsReceipt vs Invoice

- `GoodsReceipt` / `GRN` is warehouse receiving evidence.
- `Invoice` is supplier billing evidence.
- They are matched, but they are not the same object.

### Invoice vs Payment

- `Invoice` is the billing document.
- `Payment` / `Payment Application` is the payment approval/execution object.
- A matched invoice can generate payment, but they must not be merged.

### Department vs Employee

- `Department` is an organizational unit.
- `Employee` is an internal actor that belongs to a department.

## Scoring Usage Guidance

Future scorers or human reviewers can use this file as follows:

1. Normalize AI output names against `aliases`.
2. Map matched names to `canonical_id`.
3. Reject matches that violate `non_equivalences`.
4. Treat low-confidence aliases as context-sensitive and require source context.
5. Do not score this file directly as evidence; use `gold_evidence_map.json` for evidence grounding.

## What This File Does Not Do

This file does not:

- Define known conflicts.
- Define scoring weights.
- Replace the gold ontology.
- Replace the gold evidence map.
- Authorize merging concepts listed in non-equivalence boundaries.
