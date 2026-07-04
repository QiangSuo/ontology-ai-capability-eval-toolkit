# Machine Score

This report contains automatic, offline checks only. Human review is still required.

## Summary

- Evaluation ID: `demo_web`
- Generated at: `2026-07-04T12:23:21Z`
- Ontology files checked: 2
- Task result files checked: 3
- Schema-valid ontology files: 2 / 2

## Coverage

- Core concepts: 58.33%
- Key attributes: 2.70%
- Key relations: 4.65%

## Missing Items

### Missing core concepts

- `concept:department`
- `concept:employee`
- `concept:material`
- `concept:purchase_order`
- `concept:purchase_request_item`

### Missing key attributes

- `attr:approval_task.approval_id`
- `attr:approval_task.approval_status`
- `attr:approval_task.approver_user_id`
- `attr:approval_task.step_name`
- `attr:approval_task.submitted_at`
- `attr:approval_task.target_id`
- `attr:contract.contract_amount`
- `attr:contract.contract_id`
- `attr:contract.contract_no`
- `attr:contract.contract_status`
- `attr:contract.contract_title`
- `attr:contract.request_id`
- `attr:contract.supplier_id`
- `attr:department.cost_center`
- `attr:department.department_code`
- `attr:department.department_id`
- `attr:department.department_name`
- `attr:department.is_active`
- `attr:employee.department_id`
- `attr:employee.email`
- `attr:employee.is_active`
- `attr:employee.role_code`
- `attr:employee.user_id`
- `attr:employee.user_name`
- `attr:goods_receipt.po_id`
- ... 47 more

### Missing key relations

- `rel:approval_task.approves_payment`
- `rel:approval_task.approves_purchase_request`
- `rel:approval_task.performed_by_employee`
- `rel:contract.enables_purchase_order`
- `rel:contract.from_purchase_request`
- `rel:contract.reviewed_by_employee`
- `rel:contract.with_supplier`
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
- `rel:invoice.for_purchase_order`
- `rel:invoice.generates_payment`
- `rel:invoice.issued_by_supplier`
- `rel:material.requested_on_item`
- `rel:payment.approved_by_employee`
- `rel:payment.for_invoice`
- `rel:payment.has_approval_task`
- `rel:purchase_order.for_purchase_request`
- ... 16 more


## Evidence References

- Evidence references checked: 68
- Missing evidence references: 0
- Screenshot evidence enabled: True
- Screenshot evidence refs checked: 0
- Missing screenshot evidence refs: 0
- Web evidence enabled: True
- Web evidence refs checked: 19
- Missing Web evidence refs: 0
- Invalid Web snapshot paths: 0
### Missing evidence reference details

None.


## Possible Hallucinations

### Concepts

None.

### Attributes

- id=`attr:payment_request.payment_request_no`, name=`payment_request_no`, concept_id=`concept:payment_request`
- id=`attr:payment_request.payment_request_no`, name=`payment_request_no`, concept_id=`concept:payment_request`

### Relations

None.


## Schema Validation

- `task_12_web_snapshot_to_ontology_result.json`: valid (0 errors)
- `task_13_page_map_to_business_flow_result.json`: valid (0 errors)
- `task_14_extended_multi_source_fusion_result.json`: valid (0 errors)
- `normalized_outputs/task_12_web_snapshot_to_ontology.json`: valid (0 errors)
- `normalized_outputs/task_14_extended_multi_source_fusion.json`: valid (0 errors)
- `normalized_outputs/evidence_map_web_demo.json`: valid (0 errors)

## Human Review Fields

- Human review status: pending
- Human score: not set
- Reviewer notes: not set
