# Gold Screenshot Surrogate Evidence Map

This evaluator-only file summarizes screenshot surrogate evidence handles for the optional B2/B3 screenshot lane. It must not be provided to the AI tool under evaluation.

- Evidence map JSON: `gold_evidence_map.screenshot.json`
- Screenshot manifest: `../metadata/screenshot_manifest.json`
- Input mode: `surrogate_only`
- Real image/OCR coverage: not included

## Evidence Summary

| Evidence ID | Source file | Supports | Notes |
| --- | --- | --- | --- |
| `screen:purchase_request_list.field.pr_no` | `screenshots/purchase_request_list.screen.md` | Purchase Request, request number | List page PR identifier. |
| `screen:purchase_request_list.button.submit` | `screenshots/purchase_request_list.screen.md` | Submit purchase request action, DRAFT state | UI action candidate only. |
| `screen:purchase_request_detail.line_items` | `screenshots/purchase_request_detail.screen.md` | Purchase request item, material, line attributes | Detail table evidence. |
| `screen:purchase_request_detail.button.create_contract` | `screenshots/purchase_request_detail.screen.md` | Contract creation from approved PR | UI action candidate only. |
| `screen:approval_task.field.target_type` | `screenshots/approval_task.screen.md` | Approval task polymorphic target | Supports `target_type` / `target_id`. |
| `screen:approval_task.button.approve` | `screenshots/approval_task.screen.md` | Approval actions and approver roles | Generic approval UI evidence. |
| `screen:contract_detail.field.contract_no` | `screenshots/contract_detail.screen.md` | Contract, contract number | Contract identifier evidence. |
| `screen:contract_detail.field.vendor` | `screenshots/contract_detail.screen.md` | Supplier alias Vendor, contract-supplier relation | UI naming mismatch. |
| `screen:contract_detail.button.activate_contract` | `screenshots/contract_detail.screen.md` | Contract activation action, active state | UI action candidate only. |
| `screen:contract_detail.related.po_no` | `screenshots/contract_detail.screen.md` | Purchase order from contract | Related document table evidence. |
| `screen:invoice_payment.field.invoice_no` | `screenshots/invoice_payment.screen.md` | Invoice, invoice number | Invoice identifier evidence. |
| `screen:invoice_payment.field.grn_no` | `screenshots/invoice_payment.screen.md` | Goods Receipt / GRN, invoice matching relation | UI abbreviation evidence. |
| `screen:invoice_payment.match.difference_percent` | `screenshots/invoice_payment.screen.md` | Invoice matching tolerance candidate | Does not decide canonical threshold. |
| `screen:invoice_payment.field.payment_request_no` | `screenshots/invoice_payment.screen.md` | Payment Request, payment request number, pays invoice | Payment panel evidence. |
| `screen:invoice_payment.button.mark_paid` | `screenshots/invoice_payment.screen.md` | Mark paid action, paid state | UI action candidate only. |

## Review Notes

- These handles are intended for screenshot-surrogate evidence coverage checks.
- They are not proof of real image understanding.
- Button evidence should be treated as candidate behavior until confirmed by code, DDL or business documents.
- UI-only terms such as Vendor, GRN and Payment Application should be captured as aliases or conflict candidates, not new canonical concepts by default.
