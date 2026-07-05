# Machine Score

This report contains automatic, offline checks only. Human review is still required.

## Summary

- Evaluation ID: `20260704-local-codebuddy-smoke`
- Generated at: `2026-07-05T02:09:16Z`
- Ontology files checked: 1
- Task result files checked: 5
- Schema-valid ontology files: 1 / 1

## Coverage

- Core concepts: 91.67%
- Key attributes: 48.65%
- Key relations: 34.88%

## Missing Items

### Missing core concepts

- `concept:material`

### Missing key attributes

- `attr:approval_task.approval_id`
- `attr:approval_task.approver_user_id`
- `attr:approval_task.step_name`
- `attr:approval_task.submitted_at`
- `attr:contract.contract_id`
- `attr:contract.contract_title`
- `attr:contract.request_id`
- `attr:contract.supplier_id`
- `attr:department.department_id`
- `attr:employee.department_id`
- `attr:employee.user_id`
- `attr:goods_receipt.po_id`
- `attr:goods_receipt.receipt_id`
- `attr:goods_receipt.received_by`
- `attr:invoice.invoice_date`
- `attr:invoice.invoice_id`
- `attr:invoice.po_id`
- `attr:invoice.supplier_id`
- `attr:material.category_code`
- `attr:material.item_description`
- `attr:payment.invoice_id`
- `attr:payment.payment_request_id`
- `attr:purchase_order.contract_id`
- `attr:purchase_order.po_id`
- `attr:purchase_order.request_id`
- ... 13 more

### Missing key relations

- `rel:approval_task.performed_by_employee`
- `rel:contract.enables_purchase_order`
- `rel:contract.reviewed_by_employee`
- `rel:department.has_employee`
- `rel:department.owns_purchase_request`
- `rel:employee.approves_payment`
- `rel:employee.creates_purchase_request`
- `rel:employee.performs_approval_task`
- `rel:employee.records_goods_receipt`
- `rel:goods_receipt.recorded_by_employee`
- `rel:goods_receipt.supports_invoice_match`
- `rel:invoice.generates_payment`
- `rel:material.requested_on_item`
- `rel:payment.approved_by_employee`
- `rel:payment.has_approval_task`
- `rel:purchase_order.for_purchase_request`
- `rel:purchase_order.has_goods_receipt`
- `rel:purchase_order.has_invoice`
- `rel:purchase_request.has_approval_task`
- `rel:purchase_request.prefers_supplier`
- `rel:purchase_request.results_in_contract`
- `rel:purchase_request.results_in_purchase_order`
- `rel:purchase_request_item.belongs_to_request`
- `rel:purchase_request_item.describes_material`
- `rel:supplier.issues_invoice`
- ... 3 more


## Evidence References

- Evidence references checked: 270
- Missing evidence references: 92
- Screenshot evidence enabled: True
- Screenshot evidence refs checked: 0
- Missing screenshot evidence refs: 0
- Web evidence enabled: True
- Web evidence refs checked: 0
- Missing Web evidence refs: 0
- Invalid Web snapshot paths: 0
### Missing evidence reference details

- element_id=`department.department_code`, evidence_ref=`ddl:pc_department.department_code`
- element_id=`department.department_name`, evidence_ref=`ddl:pc_department.department_name`
- element_id=`department.cost_center`, evidence_ref=`ddl:pc_department.cost_center`
- element_id=`department.is_active`, evidence_ref=`ddl:pc_department.is_active`
- element_id=`user.user_name`, evidence_ref=`ddl:pc_user.user_name`
- element_id=`user.role_code`, evidence_ref=`ddl:pc_user.role_code`
- element_id=`user.email`, evidence_ref=`ddl:pc_user.email`
- element_id=`user.is_active`, evidence_ref=`ddl:pc_user.is_active`
- element_id=`supplier.supplier_code`, evidence_ref=`ddl:pc_supplier.supplier_code`
- element_id=`supplier.supplier_status`, evidence_ref=`ddl:pc_supplier.supplier_status`
- element_id=`supplier.risk_rating`, evidence_ref=`ddl:pc_supplier.risk_rating`
- element_id=`purchase_request.request_no`, evidence_ref=`ddl:pc_purchase_request.request_no`
- element_id=`purchase_request.request_status`, evidence_ref=`ddl:pc_purchase_request.request_status`
- element_id=`purchase_request.business_justification`, evidence_ref=`ddl:pc_purchase_request.business_justification`
- element_id=`purchase_request_line.item_description`, evidence_ref=`ddl:pc_purchase_request_line.item_description`
- element_id=`purchase_request_line.quantity`, evidence_ref=`ddl:pc_purchase_request_line.quantity`
- element_id=`purchase_request_line.line_amount`, evidence_ref=`ddl:pc_purchase_request_line.line_amount`
- element_id=`approval_record.target_type`, evidence_ref=`ddl:pc_approval_record.target_type`
- element_id=`approval_record.target_id`, evidence_ref=`ddl:pc_approval_record.target_id`
- element_id=`approval_record.approval_status`, evidence_ref=`ddl:pc_approval_record.approval_status`
- element_id=`approval_record.approval_comment`, evidence_ref=`ddl:pc_approval_record.approval_comment`
- element_id=`contract.contract_no`, evidence_ref=`ddl:pc_contract.contract_no`
- element_id=`contract.contract_amount`, evidence_ref=`ddl:pc_contract.contract_amount`
- element_id=`contract.contract_status`, evidence_ref=`ddl:pc_contract.contract_status`
- element_id=`contract.legal_approved_at`, evidence_ref=`ddl:pc_contract.legal_approved_at`
- ... 67 more


## Possible Hallucinations

### Concepts

None.

### Attributes

None.

### Relations

- id=`rel.approval_record.targets_contract`, predicate=`target`, source_concept_id=`approval_record`, target_concept_id=`contract`


## Schema Validation

- `task_01_code_to_ontology_result.json`: valid (0 errors)
- `task_02_ddl_to_ontology_result.json`: valid (0 errors)
- `task_03_sample_data_profile_result.json`: valid (0 errors)
- `task_04_document_to_ontology_result.json`: valid (0 errors)
- `task_05_multi_source_fusion_result.json`: valid (0 errors)
- `normalized_outputs/task_05_multi_source_fusion.json`: valid (0 errors)

## Human Review Fields

- Human review status: pending
- Human score: not set
- Reviewer notes: not set
