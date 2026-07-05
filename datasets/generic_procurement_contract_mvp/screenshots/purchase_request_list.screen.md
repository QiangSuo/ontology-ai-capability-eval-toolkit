# Screenshot Surrogate: Purchase Request List

## Page Metadata

- page_id: `screen:purchase_request_list`
- page_name: Purchase Request List
- page_type: list
- user_role: Requester / Department Manager
- input_mode: surrogate_only
- source_location: `screenshots/purchase_request_list.screen.md#screen:purchase_request_list`

## Visible Layout

- Top navigation: Procurement > Purchase Requests
- Page title: Purchase Requests
- Search filters: PR No, Request Title, Requester, Department, Status, Required By Date
- Primary table: Purchase request search results
- Pagination: shown at bottom right

## Visible Fields

| UI label | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| PR No | PR-2024-001 | `attr:purchase_request.request_no` | `screen:purchase_request_list.field.pr_no` |
| Title | Office laptop refresh | `attr:purchase_request.request_title` | `screen:purchase_request_list.field.title` |
| Requester | Alice Chen | `rel:purchase_request.requested_by_employee` / `concept:employee` | `screen:purchase_request_list.field.requester` |
| Department | IT Operations | `rel:purchase_request.belongs_to_department` / `concept:department` | `screen:purchase_request_list.field.department` |
| Estimated Amount | 68000.00 CNY | `attr:purchase_request.estimated_amount` / `attr:purchase_request.currency_code` | `screen:purchase_request_list.field.amount` |
| Status | SUBMITTED | `state:purchase_request.submitted` | `screen:purchase_request_list.field.status` |
| Required By | 2024-04-30 | `attr:purchase_request.required_by_date` | `screen:purchase_request_list.field.required_by` |

## Table Columns

| Column | Notes | Evidence handle |
| --- | --- | --- |
| PR No | Human-readable purchase request number | `screen:purchase_request_list.column.pr_no` |
| Title | Request title | `screen:purchase_request_list.column.title` |
| Requester | Employee who raised the request | `screen:purchase_request_list.column.requester` |
| Department | Owning department | `screen:purchase_request_list.column.department` |
| Supplier | Preferred supplier display name | `screen:purchase_request_list.column.supplier` |
| Amount | Estimated amount and currency | `screen:purchase_request_list.column.amount` |
| Status | Request lifecycle status | `screen:purchase_request_list.column.status` |
| Actions | View, Edit, Submit, Cancel | `screen:purchase_request_list.column.actions` |

## Button Actions

| Button | Visibility | Candidate action | Evidence handle |
| --- | --- | --- | --- |
| New Purchase Request | Requester | `action:create_purchase_request` | `screen:purchase_request_list.button.new` |
| Search | All roles | `action:search_purchase_request` | `screen:purchase_request_list.button.search` |
| View | All roles | `action:view_purchase_request` | `screen:purchase_request_list.button.view` |
| Edit | Requester, DRAFT only | `action:edit_purchase_request` | `screen:purchase_request_list.button.edit` |
| Submit | Requester, DRAFT only | `action:submit_purchase_request` | `screen:purchase_request_list.button.submit` |
| Cancel | Requester, DRAFT / SUBMITTED | `action:cancel_purchase_request` | `screen:purchase_request_list.button.cancel` |

## Status Display

- DRAFT: grey badge, row can be edited and submitted.
- SUBMITTED: blue badge, waiting for approval.
- APPROVED: green badge, can proceed to supplier/contract handling.
- REJECTED: red badge, may require requester revision.
- CANCELLED: grey strikethrough badge.

## Page Business Terms

- Purchase Request
- PR
- Requester
- Department
- Preferred Supplier
- Estimated Amount
- Required By
- Submit
- Cancel

## Extractable Ontology Candidates

### Concepts

- `concept:purchase_request`
- `concept:employee`
- `concept:department`
- `concept:supplier`

### Attributes

- `attr:purchase_request.request_no`
- `attr:purchase_request.request_title`
- `attr:purchase_request.requester_user_id`
- `attr:purchase_request.department_id`
- `attr:purchase_request.preferred_supplier_id`
- `attr:purchase_request.estimated_amount`
- `attr:purchase_request.currency_code`
- `attr:purchase_request.request_status`
- `attr:purchase_request.required_by_date`

### Relations

- `rel:purchase_request.requested_by_employee`
- `rel:purchase_request.belongs_to_department`
- `rel:purchase_request.prefers_supplier`

### Actions

- `action:create_purchase_request`
- `action:view_purchase_request`
- `action:edit_purchase_request`
- `action:submit_purchase_request`
- `action:cancel_purchase_request`

### States

- `state:purchase_request.draft`
- `state:purchase_request.submitted`
- `state:purchase_request.approved`
- `state:purchase_request.rejected`
- `state:purchase_request.cancelled`

## Naming Differences vs DDL / Documents / Code

| UI term | Other source term | Difference |
| --- | --- | --- |
| PR No | `request_no` in DDL / code | UI abbreviation vs database field name |
| Title | `request_title` | Short UI label |
| Supplier | `preferred_supplier_id` | UI displays supplier name, DB stores supplier ID |
| Amount | `estimated_amount` + `currency_code` | UI combines amount and currency |
| Requester | `requester_user_id` / Employee | UI person label vs DB user ID |

## Evidence Source Locations

- `screen:purchase_request_list.page`: this page defines a purchase request list.
- `screen:purchase_request_list.table`: table columns show core purchase request attributes.
- `screen:purchase_request_list.button.submit`: Submit button supports purchase request submit action.
- `screen:purchase_request_list.status.submitted`: SUBMITTED badge supports submitted state.

## Limitations

This file is a screenshot surrogate. It does not test OCR quality, layout detection, icon recognition or actual visual perception. It can only support UI semantic extraction from text representation.
