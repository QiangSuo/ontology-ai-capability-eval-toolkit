# Web Evidence Map (Evaluator Only)

This file summarizes evaluator-only Web evidence handles for the optional C-stage HTML snapshot extension. Do not provide this file to AI tools under evaluation.

| Evidence ID | Source | Locator | Purpose |
| --- | --- | --- | --- |
| `web:home.page` | `web_snapshots/index.html` | html[data-page-id="web:home"] | Supports Web-derived UI ontology evidence. |
| `web:purchase_requests.page` | `web_snapshots/purchase_requests.html` | html[data-page-id="web:purchase_requests"] | Supports Web-derived UI ontology evidence. |
| `web:purchase_request_detail.page` | `web_snapshots/purchase_request_detail_PR-2024-001.html` | html[data-page-id="web:purchase_request_detail"] | Supports Web-derived UI ontology evidence. |
| `web:approval_tasks.page` | `web_snapshots/approval_tasks.html` | html[data-page-id="web:approval_tasks"] | Supports Web-derived UI ontology evidence. |
| `web:contracts.page` | `web_snapshots/contracts.html` | html[data-page-id="web:contracts"] | Supports Web-derived UI ontology evidence. |
| `web:contract_detail.page` | `web_snapshots/contract_detail_CT-2024-001.html` | html[data-page-id="web:contract_detail"] | Supports Web-derived UI ontology evidence. |
| `web:invoices.page` | `web_snapshots/invoices.html` | html[data-page-id="web:invoices"] | Supports Web-derived UI ontology evidence. |
| `web:payments.page` | `web_snapshots/payments.html` | html[data-page-id="web:payments"] | Supports Web-derived UI ontology evidence. |
| `web:purchase_requests.table.pr_no` | `web_snapshots/purchase_requests.html` | Purchase request search results table header: PR No | Supports Purchase Request request number field. |
| `web:purchase_requests.table.supplier` | `web_snapshots/purchase_requests.html` | Purchase request search results table header: Supplier | Supports supplier display in PR list. |
| `web:purchase_requests.status.approved` | `web_snapshots/purchase_requests.html` | Status badge in PR row | Supports Purchase Request approved state. |
| `web:purchase_requests.button.new` | `web_snapshots/purchase_requests.html` | toolbar button text | Supports create purchase request action candidate. |
| `web:purchase_request_detail.field.preferred_vendor` | `web_snapshots/purchase_request_detail_PR-2024-001.html` | Basic Information field label: Preferred Vendor | Supports Vendor/Supplier alias and PR preferred supplier relationship. |
| `web:purchase_request_detail.table.line_items` | `web_snapshots/purchase_request_detail_PR-2024-001.html` | Line Items section | Supports purchase request item fields. |
| `web:purchase_request_detail.button.create_contract` | `web_snapshots/purchase_request_detail_PR-2024-001.html` | Action Panel button text | Supports PR-to-contract action candidate. |
| `web:approval_tasks.field.target_type` | `web_snapshots/approval_tasks.html` | Selected Target Details field label: Target Type | Supports polymorphic approval target candidate. |
| `web:approval_tasks.button.approve` | `web_snapshots/approval_tasks.html` | Selected task action button | Supports approval action candidate. |
| `web:approval_tasks.button.return` | `web_snapshots/approval_tasks.html` | Selected task action button | Supports UI-only return-for-revision candidate action. |
| `web:contracts.table.vendor` | `web_snapshots/contracts.html` | Contract list table header: Vendor | Supports Vendor/Supplier UI naming difference. |
| `web:contract_detail.field.vendor` | `web_snapshots/contract_detail_CT-2024-001.html` | Basic Information field label: Vendor | Supports contract signed-with supplier relation and alias. |
| `web:contract_detail.field.source_pr_no` | `web_snapshots/contract_detail_CT-2024-001.html` | Basic Information field label: Source PR No | Supports contract-to-purchase-request relation candidate. |
| `web:contract_detail.field.source_po_no` | `web_snapshots/contract_detail_CT-2024-001.html` | Basic Information field label: Source PO No | Supports purchase order trace as UI evidence. |
| `web:contract_detail.button.activate_contract` | `web_snapshots/contract_detail_CT-2024-001.html` | Action Panel button text | Supports contract activation action candidate. |
| `web:contract_detail.status.active` | `web_snapshots/contract_detail_CT-2024-001.html` | Contract Status field | Supports active contract state. |
| `web:invoices.field.invoice_no` | `web_snapshots/invoices.html` | Selected invoice field label: Invoice No | Supports invoice number field. |
| `web:invoices.field.supplier_invoice_no` | `web_snapshots/invoices.html` | Selected invoice field label: Supplier Invoice No | Supports external supplier invoice reference candidate. |
| `web:invoices.field.grn_no` | `web_snapshots/invoices.html` | Selected invoice field label: GRN No | Supports GRN/Goods Receipt alias and invoice matching relation. |
| `web:invoices.match.difference_percent` | `web_snapshots/invoices.html` | Invoice matching table header: Difference % | Supports invoice matching tolerance candidate only. |
| `web:invoices.button.match_invoice` | `web_snapshots/invoices.html` | Actions and notes button text | Supports match invoice action candidate. |
| `web:invoices.button.create_payment_request` | `web_snapshots/invoices.html` | Actions and notes button text | Supports payment request creation action candidate. |
| `web:payments.field.payment_application_no` | `web_snapshots/payments.html` | Selected payment details field label: Payment Application No | Supports Payment Application / Payment Request alias. |
| `web:payments.field.payment_request_no` | `web_snapshots/payments.html` | Selected payment details field label: Payment Request No | Supports payment request number field. |
| `web:payments.field.hold_reason` | `web_snapshots/payments.html` | Selected payment details field label: Hold Reason | Supports held payment operational note candidate. |
| `web:payments.button.mark_paid` | `web_snapshots/payments.html` | Payment request list row action | Supports mark paid action candidate. |
| `web:payments.button.release_hold` | `web_snapshots/payments.html` | Payment request list row action | Supports UI-only release hold candidate action. |
| `web:flow.home_to_purchase_requests` | `web_map/page_map.json` | pages[web:home].outgoing_links includes web:purchase_requests | Supports navigation edge from home to PR list. |
| `web:flow.purchase_request_to_contract` | `web_map/page_map.json` | pages[web:purchase_request_detail].outgoing_links includes web:contract_detail | Supports candidate PR-to-contract page flow. |
| `web:flow.contract_to_invoice` | `web_map/page_map.json` | pages[web:contract_detail].outgoing_links includes web:invoices | Supports candidate contract-to-invoice page flow. |
| `web:flow.invoice_to_payment` | `web_map/page_map.json` | pages[web:invoices].outgoing_links includes web:payments | Supports candidate invoice-to-payment page flow. |
| `web:page_map.missing_pages` | `web_map/page_map.json` | known_broken_or_missing_pages | Supports missing-page uncertainty for Web analysis. |
