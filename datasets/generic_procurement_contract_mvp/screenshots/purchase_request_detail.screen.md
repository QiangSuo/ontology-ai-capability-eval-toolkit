# Screenshot Surrogate: Purchase Request Detail

## Page Metadata

- page_id: `screen:purchase_request_detail`
- page_name: Purchase Request Detail
- page_type: detail
- user_role: Requester / Procurement Specialist / Department Manager
- input_mode: surrogate_only
- source_location: `screenshots/purchase_request_detail.screen.md#screen:purchase_request_detail`

## Visible Layout

- Breadcrumb: Procurement > Purchase Requests > PR-2024-001
- Header: PR-2024-001 - Office laptop refresh
- Status badge: APPROVED
- Sections: Basic Information, Line Items, Approval History, Related Documents
- Right-side action panel: Create Contract, Release PO, Cancel Request

## Visible Fields

| UI label | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| PR No | PR-2024-001 | `attr:purchase_request.request_no` | `screen:purchase_request_detail.field.pr_no` |
| Request Title | Office laptop refresh | `attr:purchase_request.request_title` | `screen:purchase_request_detail.field.title` |
| Requester | Alice Chen | `concept:employee` / `rel:purchase_request.requested_by_employee` | `screen:purchase_request_detail.field.requester` |
| Department | IT Operations | `concept:department` / `rel:purchase_request.belongs_to_department` | `screen:purchase_request_detail.field.department` |
| Preferred Vendor | Northwind Office Supplies | `concept:supplier` / `rel:purchase_request.prefers_supplier` | `screen:purchase_request_detail.field.preferred_vendor` |
| Estimated Amount | CNY 68000.00 | `attr:purchase_request.estimated_amount` / `attr:purchase_request.currency_code` | `screen:purchase_request_detail.field.amount` |
| Business Justification | Replace outdated laptops for operations team | `attr:purchase_request.business_justification` | `screen:purchase_request_detail.field.justification` |
| Required By Date | 2024-04-30 | `attr:purchase_request.required_by_date` | `screen:purchase_request_detail.field.required_by_date` |
| Submitted At | 2024-03-10 09:12 | `attr:purchase_request.submitted_at` | `screen:purchase_request_detail.field.submitted_at` |
| Approved At | 2024-03-12 16:20 | `attr:purchase_request.approved_at` | `screen:purchase_request_detail.field.approved_at` |

## Table Columns

Line Items table:

| Column | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| Line No | 1 | `attr:purchase_request_item.line_id` | `screen:purchase_request_detail.line.line_no` |
| Item Description | 14-inch business laptop | `attr:purchase_request_item.item_description` / `attr:material.item_description` | `screen:purchase_request_detail.line.description` |
| Category | IT-HARDWARE | `attr:purchase_request_item.category_code` / `attr:material.category_code` | `screen:purchase_request_detail.line.category` |
| Qty | 10 | `attr:purchase_request_item.quantity` | `screen:purchase_request_detail.line.quantity` |
| UOM | EA | `attr:purchase_request_item.unit_of_measure` | `screen:purchase_request_detail.line.uom` |
| Unit Price | 6800.00 | `attr:purchase_request_item.estimated_unit_price` | `screen:purchase_request_detail.line.unit_price` |
| Line Amount | 68000.00 | `attr:purchase_request_item.line_amount` | `screen:purchase_request_detail.line.amount` |

Approval History table:

| Column | Candidate ontology mapping | Evidence handle |
| --- | --- | --- |
| Step | `attr:approval_task.step_name` | `screen:purchase_request_detail.approval.step` |
| Approver | `attr:approval_task.approver_user_id` / `concept:employee` | `screen:purchase_request_detail.approval.approver` |
| Decision | `attr:approval_task.approval_status` | `screen:purchase_request_detail.approval.decision` |
| Comment | `attr:approval_task.approval_comment` | `screen:purchase_request_detail.approval.comment` |
| Decided At | `attr:approval_task.decided_at` | `screen:purchase_request_detail.approval.decided_at` |

## Button Actions

| Button | Visibility | Candidate action | Evidence handle |
| --- | --- | --- | --- |
| Create Contract | Procurement Specialist, APPROVED PR | `action:draft_contract` | `screen:purchase_request_detail.button.create_contract` |
| Release PO | Procurement Specialist, after active contract | `action:release_purchase_order` | `screen:purchase_request_detail.button.release_po` |
| Cancel Request | Requester/Admin, not after PO released | `action:cancel_purchase_request` | `screen:purchase_request_detail.button.cancel_request` |
| View Approval History | All roles | `action:view_approval_task` | `screen:purchase_request_detail.button.view_approval` |

## Status Display

- Main PR status: APPROVED, green badge.
- Approval history contains APPROVED and SKIPPED rows.
- Contract status widget shows Not Created.
- PO status widget shows Not Released.

## Page Business Terms

- Purchase Request
- PR
- Preferred Vendor
- Line Item
- Approval History
- Create Contract
- Release PO
- Approved At

## Extractable Ontology Candidates

### Concepts

- `concept:purchase_request`
- `concept:purchase_request_item`
- `concept:material`
- `concept:supplier`
- `concept:approval_task`
- `concept:contract`
- `concept:purchase_order`
- `concept:employee`
- `concept:department`

### Attributes

- `attr:purchase_request.request_no`
- `attr:purchase_request.request_title`
- `attr:purchase_request.business_justification`
- `attr:purchase_request.estimated_amount`
- `attr:purchase_request.currency_code`
- `attr:purchase_request.request_status`
- `attr:purchase_request.required_by_date`
- `attr:purchase_request.submitted_at`
- `attr:purchase_request.approved_at`
- `attr:purchase_request_item.item_description`
- `attr:purchase_request_item.quantity`
- `attr:purchase_request_item.unit_of_measure`
- `attr:purchase_request_item.line_amount`
- `attr:approval_task.approval_status`

### Relations

- `rel:purchase_request.has_item`
- `rel:purchase_request.requested_by_employee`
- `rel:purchase_request.belongs_to_department`
- `rel:purchase_request.prefers_supplier`
- `rel:purchase_request.has_approval_task`
- `rel:purchase_request.results_in_contract`
- `rel:purchase_request.results_in_purchase_order`
- `rel:purchase_request_item.describes_material`

### Actions

- `action:draft_contract`
- `action:release_purchase_order`
- `action:cancel_purchase_request`
- `action:view_approval_task`

### States

- `state:purchase_request.approved`

## Naming Differences vs DDL / Documents / Code

| UI term | Other source term | Difference |
| --- | --- | --- |
| Preferred Vendor | Supplier / `preferred_supplier_id` | UI uses Vendor while documents prefer Supplier |
| Line No | `line_id` | UI sequence label vs database ID |
| Qty | `quantity` | Abbreviation |
| UOM | `unit_of_measure` | Abbreviation |
| Create Contract | `draft_contract` / contract drafted | UI button vs backend action/event naming |
| Release PO | Purchase Order release | UI abbreviation vs document full term |

## Evidence Source Locations

- `screen:purchase_request_detail.page`: detail page supports purchase request as primary concept.
- `screen:purchase_request_detail.line_items`: line table supports purchase request item and material candidates.
- `screen:purchase_request_detail.approval_history`: approval history supports approval task relation.
- `screen:purchase_request_detail.button.create_contract`: UI action suggests PR can result in contract.
- `screen:purchase_request_detail.button.release_po`: UI action suggests PR can result in purchase order after contract.

## Limitations

This surrogate does not prove backend action availability. Button visibility is UI evidence and must be fused with code, DDL and document sources before becoming a final rule.
