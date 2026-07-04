# Machine Score

This report contains automatic, offline checks only. Human review is still required.

## Summary

- Evaluation ID: `demo_baseline`
- Generated at: `2026-07-04T12:23:21Z`
- Ontology files checked: 1
- Task result files checked: 5
- Schema-valid ontology files: 1 / 1

## Coverage

- Core concepts: 83.33%
- Key attributes: 83.78%
- Key relations: 27.91%

## Missing Items

### Missing core concepts

- `concept:goods_receipt`
- `concept:material`

### Missing key attributes

- `attr:goods_receipt.po_id`
- `attr:goods_receipt.receipt_id`
- `attr:goods_receipt.receipt_no`
- `attr:goods_receipt.receipt_status`
- `attr:goods_receipt.received_by`
- `attr:material.category_code`
- `attr:material.item_description`
- `attr:purchase_request.currency_code`
- `attr:purchase_request.request_id`
- `attr:purchase_request_item.category_code`
- `attr:purchase_request_item.estimated_unit_price`
- `attr:purchase_request_item.unit_of_measure`

### Missing key relations

- `rel:approval_task.approves_payment`
- `rel:approval_task.approves_purchase_request`
- `rel:approval_task.performed_by_employee`
- `rel:contract.enables_purchase_order`
- `rel:contract.reviewed_by_employee`
- `rel:department.has_employee`
- `rel:department.owns_purchase_request`
- `rel:employee.approves_payment`
- `rel:employee.belongs_to_department`
- `rel:employee.creates_purchase_request`
- `rel:employee.performs_approval_task`
- `rel:employee.records_goods_receipt`
- `rel:goods_receipt.for_purchase_order`
- `rel:goods_receipt.recorded_by_employee`
- `rel:goods_receipt.supports_invoice_match`
- `rel:invoice.matched_to_receipt`
- `rel:material.requested_on_item`
- `rel:payment.approved_by_employee`
- `rel:payment.has_approval_task`
- `rel:purchase_order.for_purchase_request`
- `rel:purchase_order.has_goods_receipt`
- `rel:purchase_order.has_invoice`
- `rel:purchase_request.prefers_supplier`
- `rel:purchase_request.results_in_contract`
- `rel:purchase_request.results_in_purchase_order`
- ... 6 more


## Evidence References

- Evidence references checked: 126
- Missing evidence references: 61
- Screenshot evidence enabled: True
- Screenshot evidence refs checked: 0
- Missing screenshot evidence refs: 0
- Web evidence enabled: True
- Web evidence refs checked: 0
- Missing Web evidence refs: 0
- Invalid Web snapshot paths: 0
### Missing evidence reference details

- element_id=`concept:purchase_request`, evidence_ref=`code.PurchaseRequest.domain`
- element_id=`concept:purchase_request_item`, evidence_ref=`csv.pc_purchase_request_line.rows`
- element_id=`concept:approval_task`, evidence_ref=`doc.role_permission_matrix.roles`
- element_id=`concept:supplier`, evidence_ref=`csv.pc_supplier.rows`
- element_id=`concept:contract`, evidence_ref=`code.Contract.domain`
- element_id=`concept:contract`, evidence_ref=`doc.contract_lifecycle.definition`
- element_id=`concept:purchase_order`, evidence_ref=`doc.procurement_process.purchase_order_release`
- element_id=`concept:invoice`, evidence_ref=`doc.receipt_invoice_payment.invoice_matching`
- element_id=`concept:department`, evidence_ref=`db.table.pc_department`
- element_id=`concept:department`, evidence_ref=`csv.pc_department.rows`
- element_id=`concept:employee`, evidence_ref=`db.table.pc_user`
- element_id=`concept:employee`, evidence_ref=`csv.pc_user.rows`
- element_id=`concept:budget_reservation`, evidence_ref=`doc:nonexistent_budget_policy`
- element_id=`attr:purchase_request.estimated_amount`, evidence_ref=`db.comment.pc_purchase_request.estimated_amount`
- element_id=`attr:purchase_request.request_status`, evidence_ref=`db.column.pc_purchase_request.request_status`
- element_id=`attr:purchase_request.business_justification`, evidence_ref=`code.PurchaseRequestService.submitPR`
- element_id=`attr:purchase_request_item.item_description`, evidence_ref=`csv.pc_purchase_request_line.rows`
- element_id=`attr:purchase_request_item.quantity`, evidence_ref=`csv.pc_purchase_request_line.rows`
- element_id=`attr:purchase_request_item.line_amount`, evidence_ref=`csv.pc_purchase_request_line.rows`
- element_id=`attr:approval_task.step_name`, evidence_ref=`csv.pc_approval_record.rows`
- element_id=`attr:approval_task.approval_status`, evidence_ref=`db.column.pc_approval_record.approval_status`
- element_id=`attr:supplier.supplier_status`, evidence_ref=`csv.pc_supplier.rows`
- element_id=`attr:supplier.risk_rating`, evidence_ref=`csv.pc_supplier.rows`
- element_id=`attr:contract.contract_amount`, evidence_ref=`code.Contract.domain`
- element_id=`attr:contract.contract_status`, evidence_ref=`db.column.pc_contract.contract_status`
- ... 36 more


## Possible Hallucinations

### Concepts

- id=`concept:budget_reservation`, name=`Budget Reservation`

### Attributes

- id=`attr:budget_reservation.reserved_amount`, name=`reserved_amount`, concept_id=`concept:budget_reservation`

### Relations

- id=`rel:budget_reservation.controls_purchase_request`, predicate=`controls`, source_concept_id=`concept:budget_reservation`, target_concept_id=`concept:purchase_request`


## Schema Validation

- `task_01_code_to_ontology_result.json`: valid (0 errors)
- `task_02_ddl_to_ontology_result.json`: valid (0 errors)
- `task_03_sample_data_profile_result.json`: valid (0 errors)
- `task_04_document_to_ontology_result.json`: valid (0 errors)
- `task_05_multi_source_fusion_result.json`: valid (0 errors)
- `normalized_outputs/ontology_fused_demo.json`: valid (0 errors)
- `normalized_outputs/evidence_map_demo.json`: valid (0 errors)

## Human Review Fields

- Human review status: pending
- Human score: not set
- Reviewer notes: not set
