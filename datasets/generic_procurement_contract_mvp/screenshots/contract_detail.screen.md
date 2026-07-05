# Screenshot Surrogate: Contract Detail

## Page Metadata

- page_id: `screen:contract_detail`
- page_name: Contract Detail
- page_type: detail
- user_role: Procurement Specialist / Legal Reviewer / Finance Manager
- input_mode: surrogate_only
- source_location: `screenshots/contract_detail.screen.md#screen:contract_detail`

## Visible Layout

- Breadcrumb: Procurement > Contracts > CT-2024-001
- Header: CT-2024-001 - Office laptop framework agreement
- Status badge: ACTIVE
- Sections: Basic Information, Supplier, Contract Amount, Lifecycle Dates, Related Purchase Request, Related Purchase Order, Approval History
- Right-side action panel: Submit Legal Review, Approve Legal Review, Activate Contract, Create Purchase Order, Terminate Contract, View Source PR

## Visible Fields

| UI label | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| Contract No | CT-2024-001 | `attr:contract.contract_no` | `screen:contract_detail.field.contract_no` |
| Contract Title | Office laptop framework agreement | `attr:contract.contract_title` | `screen:contract_detail.field.contract_title` |
| Vendor | Northwind Office Supplies | `concept:supplier` / `rel:contract.signed_with_supplier` | `screen:contract_detail.field.vendor` |
| Source PR No | PR-2024-001 | `rel:contract.originates_from_purchase_request` | `screen:contract_detail.field.source_pr_no` |
| Source PO No | PO-2024-001 | `rel:purchase_order.created_from_contract` | `screen:contract_detail.field.source_po_no` |
| Contract Amount | CNY 68000.00 | `attr:contract.contract_amount` / `attr:contract.currency_code` | `screen:contract_detail.field.amount` |
| Effective Date | 2024-03-15 | `attr:contract.effective_date` | `screen:contract_detail.field.effective_date` |
| Expiry Date | 2025-03-14 | `attr:contract.expiry_date` | `screen:contract_detail.field.expiry_date` |
| Legal Approved At | 2024-03-14 17:30 | `attr:contract.legal_approved_at` | `screen:contract_detail.field.legal_approved_at` |
| Activated At | 2024-03-15 09:00 | `attr:contract.activated_at` | `screen:contract_detail.field.activated_at` |
| Owner Department | IT Operations | `concept:department` | `screen:contract_detail.field.owner_department` |
| Contract Status | ACTIVE | `state:contract.active` | `screen:contract_detail.field.status` |

## Table Columns

Approval History table:

| Column | Candidate ontology mapping | Evidence handle |
| --- | --- | --- |
| Step | `attr:approval_task.step_name` | `screen:contract_detail.approval.step` |
| Approver | `attr:approval_task.approver_user_id` / `concept:employee` | `screen:contract_detail.approval.approver` |
| Role | `role:legal_reviewer` / `role:finance_manager` | `screen:contract_detail.approval.role` |
| Decision | `attr:approval_task.approval_status` | `screen:contract_detail.approval.decision` |
| Comment | `attr:approval_task.approval_comment` | `screen:contract_detail.approval.comment` |
| Decided At | `attr:approval_task.decided_at` | `screen:contract_detail.approval.decided_at` |

Related Documents table:

| Column | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| Document Type | Purchase Request | `concept:purchase_request` | `screen:contract_detail.related.type_pr` |
| Document No | PR-2024-001 | `rel:contract.originates_from_purchase_request` | `screen:contract_detail.related.pr_no` |
| Document Type | Purchase Order | `concept:purchase_order` | `screen:contract_detail.related.type_po` |
| Document No | PO-2024-001 | `rel:purchase_order.created_from_contract` | `screen:contract_detail.related.po_no` |

## Button Actions

| Button | Visibility | Candidate action | Evidence handle |
| --- | --- | --- | --- |
| Submit Legal Review | Procurement Specialist, DRAFT contract | `action:submit_contract_legal_review` | `screen:contract_detail.button.submit_legal_review` |
| Approve Legal Review | Legal Reviewer, pending legal step | `action:approve_contract_legal_review` | `screen:contract_detail.button.approve_legal_review` |
| Activate Contract | Procurement Admin, legal approved and in valid date range | `action:activate_contract` | `screen:contract_detail.button.activate_contract` |
| Create Purchase Order | Procurement Specialist, ACTIVE contract | `action:create_purchase_order` | `screen:contract_detail.button.create_po` |
| Terminate Contract | Procurement Admin, ACTIVE contract | `action:terminate_contract` | `screen:contract_detail.button.terminate_contract` |
| View Source PR | All roles | `action:view_purchase_request` | `screen:contract_detail.button.view_source_pr` |

## Status Display

- DRAFT: contract can be edited and submitted for legal review.
- PENDING_LEGAL_REVIEW: legal reviewer action is required.
- LEGAL_APPROVED: contract can be activated when dates are valid.
- ACTIVE: purchase order release is allowed.
- TERMINATED: contract is no longer available for new purchase orders.

## Page Business Terms

- Contract
- Contract No
- Vendor
- Supplier
- Legal Review
- Activate Contract
- Source PR
- Purchase Order
- Effective Date
- Expiry Date

## Extractable Ontology Candidates

### Concepts

- `concept:contract`
- `concept:supplier`
- `concept:purchase_request`
- `concept:purchase_order`
- `concept:approval_task`
- `concept:employee`
- `concept:department`

### Attributes

- `attr:contract.contract_no`
- `attr:contract.contract_title`
- `attr:contract.contract_amount`
- `attr:contract.currency_code`
- `attr:contract.effective_date`
- `attr:contract.expiry_date`
- `attr:contract.legal_approved_at`
- `attr:contract.activated_at`
- `attr:contract.contract_status`
- `attr:approval_task.step_name`
- `attr:approval_task.approval_status`
- `attr:approval_task.decided_at`

### Relations

- `rel:contract.signed_with_supplier`
- `rel:contract.originates_from_purchase_request`
- `rel:contract.has_approval_task`
- `rel:purchase_order.created_from_contract`
- `rel:contract.owned_by_department`

### Actions

- `action:submit_contract_legal_review`
- `action:approve_contract_legal_review`
- `action:activate_contract`
- `action:create_purchase_order`
- `action:terminate_contract`
- `action:view_purchase_request`

### States

- `state:contract.draft`
- `state:contract.pending_legal_review`
- `state:contract.legal_approved`
- `state:contract.active`
- `state:contract.terminated`

## Naming Differences vs DDL / Documents / Code

| UI term | Other source term | Difference |
| --- | --- | --- |
| Vendor | Supplier / `supplier_id` | UI uses Vendor while documents prefer Supplier and DB stores supplier ID |
| Contract No | `contract_no` | UI label vs database field name |
| Source PR | Purchase Request / `request_id` | UI displays business number while DDL stores numeric request ID |
| Source PO | Purchase Order / `purchase_order_id` | UI displays business number while backend may store internal ID |
| Legal Review | `legal_approved_at` / legal approval rule | UI workflow label vs timestamp field |
| Activate Contract | contract activation service behavior | UI button vs backend lifecycle operation |

## Evidence Source Locations

- `screen:contract_detail.page`: detail page supports contract as primary concept.
- `screen:contract_detail.field.vendor`: Vendor field supports supplier relationship and alias difference.
- `screen:contract_detail.field.source_pr_no`: Source PR field supports contract-to-purchase-request relation.
- `screen:contract_detail.related.po_no`: related document table supports contract-to-purchase-order trace.
- `screen:contract_detail.button.activate_contract`: Activate Contract button supports contract activation action candidate.
- `screen:contract_detail.status.active`: ACTIVE badge supports active contract state.

## Limitations

This file is a screenshot surrogate. It does not test OCR quality, layout detection, icon recognition, pixel-level region identification or actual visual perception. Button visibility is UI evidence only and must be fused with source code, DDL and business documents before becoming a final executable rule.
