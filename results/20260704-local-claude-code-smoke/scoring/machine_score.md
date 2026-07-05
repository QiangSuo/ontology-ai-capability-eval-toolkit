# Machine Score

This report contains automatic, offline checks only. Human review is still required.

## Summary

- Evaluation ID: `20260704-local-claude-code-smoke`
- Generated at: `2026-07-05T02:09:16Z`
- Ontology files checked: 1
- Task result files checked: 5
- Schema-valid ontology files: 1 / 1

## Coverage

- Core concepts: 91.67%
- Key attributes: 97.30%
- Key relations: 46.51%

## Missing Items

### Missing core concepts

- `concept:material`

### Missing key attributes

- `attr:material.category_code`
- `attr:material.item_description`

### Missing key relations

- `rel:contract.enables_purchase_order`
- `rel:department.has_employee`
- `rel:department.owns_purchase_request`
- `rel:employee.approves_payment`
- `rel:employee.belongs_to_department`
- `rel:employee.creates_purchase_request`
- `rel:employee.performs_approval_task`
- `rel:employee.records_goods_receipt`
- `rel:goods_receipt.supports_invoice_match`
- `rel:invoice.generates_payment`
- `rel:material.requested_on_item`
- `rel:payment.has_approval_task`
- `rel:purchase_order.has_goods_receipt`
- `rel:purchase_order.has_invoice`
- `rel:purchase_request.has_approval_task`
- `rel:purchase_request.results_in_contract`
- `rel:purchase_request.results_in_purchase_order`
- `rel:purchase_request_item.belongs_to_request`
- `rel:purchase_request_item.describes_material`
- `rel:supplier.issues_invoice`
- `rel:supplier.party_to_contract`
- `rel:supplier.preferred_by_request`
- `rel:supplier.receives_purchase_order`


## Evidence References

- Evidence references checked: 954
- Missing evidence references: 177
- Screenshot evidence enabled: True
- Screenshot evidence refs checked: 0
- Missing screenshot evidence refs: 0
- Web evidence enabled: True
- Web evidence refs checked: 0
- Missing Web evidence refs: 0
- Invalid Web snapshot paths: 0
### Missing evidence reference details

- element_id=`attr.department.department_code`, evidence_ref=`ddl:pc_department.department_code`
- element_id=`attr.department.department_name`, evidence_ref=`ddl:pc_department.department_name`
- element_id=`attr.department.cost_center`, evidence_ref=`ddl:pc_department.cost_center`
- element_id=`attr.department.is_active`, evidence_ref=`ddl:pc_department.is_active`
- element_id=`attr.user.user_name`, evidence_ref=`ddl:pc_user.user_name`
- element_id=`attr.user.role_code`, evidence_ref=`ddl:pc_user.role_code`
- element_id=`attr.user.department_id`, evidence_ref=`ddl:pc_user.department_id`
- element_id=`attr.user.email`, evidence_ref=`ddl:pc_user.email`
- element_id=`attr.user.is_active`, evidence_ref=`ddl:pc_user.is_active`
- element_id=`attr.supplier.supplier_code`, evidence_ref=`ddl:pc_supplier.supplier_code`
- element_id=`attr.supplier.supplier_name`, evidence_ref=`ddl:pc_supplier.supplier_name`
- element_id=`attr.supplier.supplier_status`, evidence_ref=`ddl:pc_supplier.supplier_status`
- element_id=`attr.supplier.risk_rating`, evidence_ref=`ddl:pc_supplier.risk_rating`
- element_id=`attr.supplier.contact_email`, evidence_ref=`ddl:pc_supplier.contact_email`
- element_id=`attr.supplier.onboarded_at`, evidence_ref=`ddl:pc_supplier.onboarded_at`
- element_id=`attr.purchase_request.request_no`, evidence_ref=`ddl:pc_purchase_request.request_no`
- element_id=`attr.purchase_request.request_title`, evidence_ref=`ddl:pc_purchase_request.request_title`
- element_id=`attr.purchase_request.requester_user_id`, evidence_ref=`ddl:pc_purchase_request.requester_user_id`
- element_id=`attr.purchase_request.department_id`, evidence_ref=`ddl:pc_purchase_request.department_id`
- element_id=`attr.purchase_request.preferred_supplier_id`, evidence_ref=`ddl:pc_purchase_request.preferred_supplier_id`
- element_id=`attr.purchase_request.currency_code`, evidence_ref=`ddl:pc_purchase_request.currency_code`
- element_id=`attr.purchase_request.request_status`, evidence_ref=`ddl:pc_purchase_request.request_status`
- element_id=`attr.purchase_request.business_justification`, evidence_ref=`ddl:pc_purchase_request.business_justification`
- element_id=`attr.purchase_request.required_by_date`, evidence_ref=`ddl:pc_purchase_request.required_by_date`
- element_id=`attr.purchase_request.submitted_at`, evidence_ref=`ddl:pc_purchase_request.submitted_at`
- ... 152 more


## Possible Hallucinations

### Concepts

None.

### Attributes

None.

### Relations

- id=`rel.approval_record.contract_target`, predicate=`targets_contract`, source_concept_id=`concept.approval_record`, target_concept_id=`concept.contract`


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
