# Web Page Map

## Scope

This page map describes the optional offline Web HTML snapshot bundle for `generic_procurement_contract_mvp`. It is an input-side navigation aid, not a gold ontology, scoring file, or evaluator-only answer key.

- Input mode: `html_snapshot`
- Snapshot root: `web_snapshots/`
- Machine-readable map: `web_map/page_map.json`
- Evidence convention: use `web:*` evidence IDs and cite the snapshot file or page map path that supports the observation.

## Recommended Crawl Order

1. Start at `web_snapshots/index.html` (`web:home`) to identify the major modules and role hints.
2. Open `web_snapshots/purchase_requests.html` (`web:purchase_requests`) to capture the PR list, filters, lifecycle states, and PR abbreviation.
3. Open `web_snapshots/purchase_request_detail_PR-2024-001.html` (`web:purchase_request_detail`) to inspect line items, approval history, preferred vendor wording, and downstream document links.
4. Open `web_snapshots/approval_tasks.html` (`web:approval_tasks`) to inspect the generic approval target pattern across Purchase Request, Contract and Payment Request.
5. Open `web_snapshots/contracts.html` (`web:contracts`) and then `web_snapshots/contract_detail_CT-2024-001.html` (`web:contract_detail`) to inspect contract lifecycle, legal review, activation and Vendor/Supplier alias clues.
6. Open `web_snapshots/invoices.html` (`web:invoices`) to inspect Invoice, PO, GRN, matching and payment creation links.
7. Open `web_snapshots/payments.html` (`web:payments`) to inspect Payment Application / Payment Request aliases, finance approval, held payment and paid status.

## Core Business Flow Pages

| Flow step | Primary page | Supporting pages | Notes |
| --- | --- | --- | --- |
| Purchase request creation and tracking | `web:purchase_requests` | `web:purchase_request_detail` | List and detail expose PR fields, statuses and requester/department/supplier links. |
| Purchase request approval | `web:approval_tasks` | `web:purchase_request_detail` | Generic Target Type / Target No pattern should be treated as candidate polymorphic approval evidence. |
| Contract drafting and activation | `web:contracts` | `web:contract_detail` | Uses Vendor in UI while documents prefer Supplier. Activation buttons are UI evidence only. |
| Invoice matching | `web:invoices` | `web:contract_detail` | GRN appears as a UI abbreviation for Goods Receipt. Difference % is a candidate signal. |
| Payment request approval and execution | `web:payments` | `web:approval_tasks`, `web:invoices` | Payment Applications and Payment Request are both visible terms. Held payment includes a hold reason clue. |

## Repeated Page Templates

- List pages: `web:purchase_requests`, `web:contracts`, `web:payments`.
- Detail pages: `web:purchase_request_detail`, `web:contract_detail`.
- Workbench pages: `web:approval_tasks`, `web:invoices`.

Tools should avoid over-counting concepts when the same object appears in a list, detail page and related-document table.

## Role and Permission Clues

The HTML pages include role hints in page headers and button labels. Treat these as UI visibility evidence, not final authorization rules.

- Requester: creates and submits Purchase Requests.
- Department Manager: sees PR approval tasks.
- Procurement Specialist: drafts contracts and manages supplier/contract work.
- Legal Reviewer: reviews contract legal steps.
- AP Clerk / Finance Specialist: matches invoices and creates payment requests.
- Finance Manager: approves high-value PRs and payment applications.
- Procurement Admin: may see activation and override-style actions.

## Recursive Analysis Test Points

- `web:approval_tasks` has a generic `Target Type` and `Target No` pattern that links to multiple business objects.
- `web:purchase_request_detail` links to contract and approval pages, then `web:contract_detail` links back to PR and onward to invoice.
- `web:invoices` links to both contract and payment pages, while `web:payments` links back to invoice and approval pages.
- Some business objects are visible without standalone pages: Purchase Order and Goods Receipt / GRN.
- Some labels intentionally differ from DDL, code or documents: Vendor/Supplier, PR/Purchase Request, GRN/Goods Receipt, Payment Application/Payment Request.

## Missing or Limited Pages

- Supplier Master has no snapshot file.
- Purchase Order Detail has no standalone snapshot file.
- Goods Receipt Detail has no standalone snapshot file.
- Search, approval and action buttons are static and do not prove backend execution.
- No live login, dynamic JavaScript DOM, API call or real browser automation is represented.

## Evidence Reference Check

All page-level evidence references in `page_map.json` point to files that are part of this bundle:

- `web_snapshots/index.html`
- `web_snapshots/purchase_requests.html`
- `web_snapshots/purchase_request_detail_PR-2024-001.html`
- `web_snapshots/approval_tasks.html`
- `web_snapshots/contracts.html`
- `web_snapshots/contract_detail_CT-2024-001.html`
- `web_snapshots/invoices.html`
- `web_snapshots/payments.html`
- `web_map/page_map.json`
- `web_map/page_map.md`
