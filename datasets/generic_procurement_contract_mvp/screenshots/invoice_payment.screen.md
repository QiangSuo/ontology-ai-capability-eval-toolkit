# Screenshot Surrogate: Invoice and Payment Workbench

## Page Metadata

- page_id: `screen:invoice_payment`
- page_name: Invoice and Payment Workbench
- page_type: payment
- user_role: Finance Specialist / Finance Manager
- input_mode: surrogate_only
- source_location: `screenshots/invoice_payment.screen.md#screen:invoice_payment`

## Visible Layout

- Breadcrumb: Finance > Invoice & Payment
- Page title: Invoice and Payment Workbench
- Left panel: Invoice filters and pending matching queue
- Main panel: selected invoice, purchase order and goods receipt matching details
- Right panel: payment request summary and approval status
- Footer actions: Match Invoice, Create Payment Request, Submit Payment Approval, Approve Payment, Mark Paid, View Contract

## Visible Fields

| UI label | Example value | Candidate ontology mapping | Evidence handle |
| --- | --- | --- | --- |
| Invoice No | INV-2024-001 | `attr:invoice.invoice_no` | `screen:invoice_payment.field.invoice_no` |
| Supplier Invoice No | NW-INV-7788 | `attr:invoice.supplier_invoice_no` candidate | `screen:invoice_payment.field.supplier_invoice_no` |
| Supplier | Northwind Office Supplies | `concept:supplier` | `screen:invoice_payment.field.supplier` |
| Contract No | CT-2024-001 | `rel:invoice.related_to_contract` / `concept:contract` | `screen:invoice_payment.field.contract_no` |
| PO No | PO-2024-001 | `rel:invoice.related_to_purchase_order` / `concept:purchase_order` | `screen:invoice_payment.field.po_no` |
| GRN No | GRN-2024-001 | `rel:invoice.matched_with_goods_receipt` / `concept:goods_receipt` | `screen:invoice_payment.field.grn_no` |
| Invoice Amount | CNY 68000.00 | `attr:invoice.invoice_amount` / `attr:invoice.currency_code` | `screen:invoice_payment.field.invoice_amount` |
| Tax Amount | CNY 8840.00 | `attr:invoice.tax_amount` | `screen:invoice_payment.field.tax_amount` |
| Invoice Date | 2024-03-25 | `attr:invoice.invoice_date` | `screen:invoice_payment.field.invoice_date` |
| Due Date | 2024-04-24 | `attr:invoice.due_date` | `screen:invoice_payment.field.due_date` |
| Match Status | MATCHED | `state:invoice.matched` | `screen:invoice_payment.field.match_status` |
| Payment Request No | PAY-2024-001 | `attr:payment_request.payment_request_no` | `screen:invoice_payment.field.payment_request_no` |
| Payment Amount | CNY 68000.00 | `attr:payment_request.payment_amount` / `attr:payment_request.currency_code` | `screen:invoice_payment.field.payment_amount` |
| Payment Status | APPROVED | `state:payment_request.approved` | `screen:invoice_payment.field.payment_status` |
| Paid At | 2024-04-05 15:10 | `attr:payment_request.paid_at` | `screen:invoice_payment.field.paid_at` |

## Table Columns

Invoice matching table:

| Column | Candidate ontology mapping | Evidence handle |
| --- | --- | --- |
| PO Line | `attr:purchase_order_line.line_id` candidate | `screen:invoice_payment.match.po_line` |
| Item Description | `attr:purchase_request_item.item_description` / material description | `screen:invoice_payment.match.item_description` |
| Ordered Qty | `attr:purchase_order.ordered_quantity` candidate | `screen:invoice_payment.match.ordered_qty` |
| Received Qty | `attr:goods_receipt.received_quantity` | `screen:invoice_payment.match.received_qty` |
| Invoice Qty | `attr:invoice.invoice_quantity` candidate | `screen:invoice_payment.match.invoice_qty` |
| PO Amount | purchase order amount candidate | `screen:invoice_payment.match.po_amount` |
| Invoice Amount | `attr:invoice.invoice_amount` | `screen:invoice_payment.match.invoice_amount` |
| Difference % | invoice matching tolerance candidate | `screen:invoice_payment.match.difference_percent` |
| Match Result | `state:invoice.matched` / `state:invoice.mismatched` | `screen:invoice_payment.match.result` |

Payment approval table:

| Column | Candidate ontology mapping | Evidence handle |
| --- | --- | --- |
| Step | `attr:approval_task.step_name` | `screen:invoice_payment.approval.step` |
| Approver Role | `role:finance_manager` | `screen:invoice_payment.approval.role` |
| Decision | `attr:approval_task.approval_status` | `screen:invoice_payment.approval.decision` |
| Comment | `attr:approval_task.approval_comment` | `screen:invoice_payment.approval.comment` |
| Decided At | `attr:approval_task.decided_at` | `screen:invoice_payment.approval.decided_at` |

## Button Actions

| Button | Visibility | Candidate action | Evidence handle |
| --- | --- | --- | --- |
| Match Invoice | Finance Specialist, received invoice | `action:match_invoice_to_receipt` | `screen:invoice_payment.button.match_invoice` |
| Create Payment Request | Finance Specialist, MATCHED invoice | `action:create_payment_request` | `screen:invoice_payment.button.create_payment_request` |
| Submit Payment Approval | Finance Specialist, DRAFT payment request | `action:submit_payment_request` | `screen:invoice_payment.button.submit_payment_approval` |
| Approve Payment | Finance Manager, pending payment approval | `action:approve_payment` | `screen:invoice_payment.button.approve_payment` |
| Mark Paid | Finance Specialist, APPROVED payment request | `action:mark_payment_paid` | `screen:invoice_payment.button.mark_paid` |
| View Contract | All finance roles | `action:view_contract` | `screen:invoice_payment.button.view_contract` |

## Status Display

- Invoice RECEIVED: invoice captured but not yet matched.
- Invoice MATCHED: invoice is within matching tolerance and may create payment request.
- Invoice MISMATCHED: invoice requires review before payment request.
- Payment DRAFT: payment request created but not submitted.
- Payment SUBMITTED: waiting for finance manager approval.
- Payment APPROVED: payment can be executed.
- Payment PAID: payment execution is complete.
- Payment REJECTED: payment request must be revised or cancelled.

## Page Business Terms

- Invoice
- Supplier Invoice No
- Invoice Matching
- Goods Receipt
- GRN
- Payment Request
- Payment Application
- Finance Approval
- Mark Paid
- Matching Tolerance

## Extractable Ontology Candidates

### Concepts

- `concept:invoice`
- `concept:payment_request`
- `concept:supplier`
- `concept:contract`
- `concept:purchase_order`
- `concept:goods_receipt`
- `concept:approval_task`
- `concept:employee`

### Attributes

- `attr:invoice.invoice_no`
- `attr:invoice.supplier_invoice_no`
- `attr:invoice.invoice_amount`
- `attr:invoice.currency_code`
- `attr:invoice.tax_amount`
- `attr:invoice.invoice_date`
- `attr:invoice.due_date`
- `attr:invoice.match_status`
- `attr:payment_request.payment_request_no`
- `attr:payment_request.payment_amount`
- `attr:payment_request.currency_code`
- `attr:payment_request.payment_status`
- `attr:payment_request.paid_at`
- `attr:goods_receipt.received_quantity`
- `attr:approval_task.approval_status`

### Relations

- `rel:invoice.issued_by_supplier`
- `rel:invoice.related_to_contract`
- `rel:invoice.related_to_purchase_order`
- `rel:invoice.matched_with_goods_receipt`
- `rel:payment_request.pays_invoice`
- `rel:payment_request.has_approval_task`
- `rel:purchase_order.has_goods_receipt`

### Actions

- `action:match_invoice_to_receipt`
- `action:create_payment_request`
- `action:submit_payment_request`
- `action:approve_payment`
- `action:mark_payment_paid`
- `action:view_contract`

### States

- `state:invoice.received`
- `state:invoice.matched`
- `state:invoice.mismatched`
- `state:invoice.payment_requested`
- `state:payment_request.draft`
- `state:payment_request.submitted`
- `state:payment_request.approved`
- `state:payment_request.paid`
- `state:payment_request.rejected`

## Naming Differences vs DDL / Documents / Code

| UI term | Other source term | Difference |
| --- | --- | --- |
| Invoice & Payment | receipt invoice payment policy | UI combines invoice and payment process into one workbench |
| Supplier Invoice No | invoice external reference | UI shows supplier-facing invoice identifier in addition to internal invoice number |
| GRN | Goods Receipt / `goods_receipt` | UI abbreviation vs business and database terminology |
| Payment Application | Payment Request / `payment_request` | Document/UI synonym vs DDL term |
| Match Invoice | `ReceiptInvoiceMatchingService` | UI action vs backend service name |
| Difference % | invoice tolerance policy | UI calculated indicator vs policy/code threshold |
| Mark Paid | payment execution / payment completed | UI action label vs lifecycle state transition |

## Evidence Source Locations

- `screen:invoice_payment.page`: workbench supports invoice and payment request concepts.
- `screen:invoice_payment.field.grn_no`: GRN field supports invoice-to-goods-receipt matching relation.
- `screen:invoice_payment.match.difference_percent`: Difference % column supports matching tolerance candidate but not the canonical threshold.
- `screen:invoice_payment.field.payment_request_no`: payment request panel supports invoice-to-payment flow.
- `screen:invoice_payment.button.create_payment_request`: Create Payment Request button supports payment request creation action.
- `screen:invoice_payment.button.mark_paid`: Mark Paid button supports payment completion action candidate.

## Limitations

This file is a screenshot surrogate. It can support UI semantic extraction for invoice and payment workflow terms, but it does not test OCR quality, layout detection, icon recognition, pixel-level region identification or actual visual perception. The matching tolerance shown in the UI is a candidate signal only; the canonical tolerance must be confirmed against policy documents and source code.
