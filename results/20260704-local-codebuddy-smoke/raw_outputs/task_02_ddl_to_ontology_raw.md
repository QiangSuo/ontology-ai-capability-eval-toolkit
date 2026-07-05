{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-ddl-ontology",
  "title": "Procurement Contract MVP DDL Ontology Draft",
  "domain": "procurement_contract",
  "concepts": [
    {
      "id": "concept:department",
      "name": "Department",
      "type": "concept",
      "category": "organization",
      "attribute_ids": [
        "attr:department.department_code",
        "attr:department.department_name",
        "attr:department.cost_center",
        "attr:department.is_active"
      ],
      "evidence_refs": [
        "ddl:pc_department"
      ],
      "confidence": 0.96
    },
    {
      "id": "concept:user",
      "name": "User",
      "type": "concept",
      "category": "actor",
      "attribute_ids": [
        "attr:user.user_name",
        "attr:user.role_code",
        "attr:user.email",
        "attr:user.is_active"
      ],
      "evidence_refs": [
        "ddl:pc_user"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:supplier",
      "name": "Supplier",
      "type": "concept",
      "category": "party",
      "attribute_ids": [
        "attr:supplier.supplier_code",
        "attr:supplier.supplier_name",
        "attr:supplier.supplier_status",
        "attr:supplier.risk_rating",
        "attr:supplier.contact_email",
        "attr:supplier.onboarded_at"
      ],
      "state_ids": [
        "state:supplier_status.active",
        "state:supplier_status.suspended",
        "state:supplier_status.pending_review",
        "state:risk_rating.low",
        "state:risk_rating.medium",
        "state:risk_rating.high"
      ],
      "evidence_refs": [
        "ddl:pc_supplier"
      ],
      "confidence": 0.96
    },
    {
      "id": "concept:purchase_request",
      "name": "Purchase Request",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:purchase_request.request_no",
        "attr:purchase_request.request_title",
        "attr:purchase_request.estimated_amount",
        "attr:purchase_request.currency_code",
        "attr:purchase_request.request_status",
        "attr:purchase_request.business_justification",
        "attr:purchase_request.required_by_date",
        "attr:purchase_request.submitted_at",
        "attr:purchase_request.approved_at"
      ],
      "state_ids": [
        "state:request_status.draft",
        "state:request_status.submitted",
        "state:request_status.approved",
        "state:request_status.rejected",
        "state:request_status.cancelled"
      ],
      "alias_ids": [
        "alias:purchase_request.pr",
        "alias:purchase_request.request"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept:purchase_request_line",
      "name": "Purchase Request Line",
      "type": "concept",
      "category": "document_line",
      "attribute_ids": [
        "attr:purchase_request_line.item_description",
        "attr:purchase_request_line.category_code",
        "attr:purchase_request_line.quantity",
        "attr:purchase_request_line.unit_of_measure",
        "attr:purchase_request_line.estimated_unit_price",
        "attr:purchase_request_line.line_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line"
      ],
      "confidence": 0.96
    },
    {
      "id": "concept:approval_record",
      "name": "Approval Record",
      "type": "concept",
      "category": "record",
      "attribute_ids": [
        "attr:approval_record.target_type",
        "attr:approval_record.target_id",
        "attr:approval_record.step_name",
        "attr:approval_record.approval_status",
        "attr:approval_record.approval_comment",
        "attr:approval_record.submitted_at",
        "attr:approval_record.decided_at"
      ],
      "state_ids": [
        "state:approval_status.pending",
        "state:approval_status.approved",
        "state:approval_status.rejected",
        "state:approval_status.skipped"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record"
      ],
      "confidence": 0.93,
      "uncertainty_refs": [
        "uncertainty:approval_target_polymorphic_no_fk"
      ]
    },
    {
      "id": "concept:contract",
      "name": "Contract",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:contract.contract_no",
        "attr:contract.contract_title",
        "attr:contract.contract_amount",
        "attr:contract.contract_status",
        "attr:contract.start_date",
        "attr:contract.end_date",
        "attr:contract.legal_approved_at",
        "attr:contract.activated_at",
        "attr:contract.termination_reason"
      ],
      "state_ids": [
        "state:contract_status.draft",
        "state:contract_status.legal_review",
        "state:contract_status.active",
        "state:contract_status.expired",
        "state:contract_status.terminated"
      ],
      "evidence_refs": [
        "ddl:pc_contract"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept:purchase_order",
      "name": "Purchase Order",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:purchase_order.po_no",
        "attr:purchase_order.po_amount",
        "attr:purchase_order.po_status",
        "attr:purchase_order.released_at",
        "attr:purchase_order.closed_at"
      ],
      "state_ids": [
        "state:po_status.released",
        "state:po_status.partially_received",
        "state:po_status.closed",
        "state:po_status.cancelled"
      ],
      "alias_ids": [
        "alias:purchase_order.po"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept:goods_receipt",
      "name": "Goods Receipt",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:goods_receipt.receipt_no",
        "attr:goods_receipt.receipt_status",
        "attr:goods_receipt.received_at",
        "attr:goods_receipt.inspection_result",
        "attr:goods_receipt.remarks"
      ],
      "state_ids": [
        "state:receipt_status.pending",
        "state:receipt_status.partial",
        "state:receipt_status.complete",
        "state:receipt_status.rejected",
        "state:inspection_result.pass",
        "state:inspection_result.fail",
        "state:inspection_result.not_required"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt"
      ],
      "confidence": 0.97
    },
    {
      "id": "concept:invoice",
      "name": "Invoice",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:invoice.invoice_no",
        "attr:invoice.invoice_amount",
        "attr:invoice.invoice_date",
        "attr:invoice.invoice_status",
        "attr:invoice.match_variance_amount",
        "attr:invoice.matched_at"
      ],
      "state_ids": [
        "state:invoice_status.pending_match",
        "state:invoice_status.matched",
        "state:invoice_status.exception",
        "state:invoice_status.cancelled"
      ],
      "evidence_refs": [
        "ddl:pc_invoice"
      ],
      "confidence": 0.97
    },
    {
      "id": "concept:payment_request",
      "name": "Payment Request",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:payment_request.payment_no",
        "attr:payment_request.payment_amount",
        "attr:payment_request.payment_status",
        "attr:payment_request.due_date",
        "attr:payment_request.approved_at",
        "attr:payment_request.paid_at"
      ],
      "state_ids": [
        "state:payment_status.requested",
        "state:payment_status.approved",
        "state:payment_status.paid",
        "state:payment_status.held",
        "state:payment_status.cancelled"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request"
      ],
      "confidence": 0.97
    }
  ],
  "attributes": [
    {
      "id": "attr:department.department_code",
      "concept_id": "concept:department",
      "name": "department_code",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Unique department code.",
      "evidence_refs": [
        "ddl:pc_department.department_code"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:department.department_name",
      "concept_id": "concept:department",
      "name": "department_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_department.department_name"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:department.cost_center",
      "concept_id": "concept:department",
      "name": "cost_center",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_department.cost_center"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:department.is_active",
      "concept_id": "concept:department",
      "name": "is_active",
      "type": "attribute",
      "data_type": "BOOLEAN",
      "required": true,
      "description": "Default TRUE.",
      "allowed_values": [
        true,
        false
      ],
      "evidence_refs": [
        "ddl:pc_department.is_active"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:user.user_name",
      "concept_id": "concept:user",
      "name": "user_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_user.user_name"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:user.role_code",
      "concept_id": "concept:user",
      "name": "role_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "allowed_values": [
        "REQUESTER",
        "DEPT_MANAGER",
        "PROCUREMENT_SPECIALIST",
        "FINANCE_MANAGER",
        "LEGAL_REVIEWER",
        "WAREHOUSE_CLERK",
        "AP_CLERK",
        "PROCUREMENT_ADMIN"
      ],
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:user.email",
      "concept_id": "concept:user",
      "name": "email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_user.email"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:user.is_active",
      "concept_id": "concept:user",
      "name": "is_active",
      "type": "attribute",
      "data_type": "BOOLEAN",
      "required": true,
      "description": "Default TRUE.",
      "allowed_values": [
        true,
        false
      ],
      "evidence_refs": [
        "ddl:pc_user.is_active"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:supplier.supplier_code",
      "concept_id": "concept:supplier",
      "name": "supplier_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique supplier code.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_code"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:supplier.supplier_name",
      "concept_id": "concept:supplier",
      "name": "supplier_name",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_supplier.supplier_name"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:supplier.supplier_status",
      "concept_id": "concept:supplier",
      "name": "supplier_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "ACTIVE",
        "SUSPENDED",
        "PENDING_REVIEW"
      ],
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:supplier.risk_rating",
      "concept_id": "concept:supplier",
      "name": "risk_rating",
      "type": "attribute",
      "data_type": "VARCHAR(20)",
      "required": true,
      "allowed_values": [
        "LOW",
        "MEDIUM",
        "HIGH"
      ],
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:supplier.contact_email",
      "concept_id": "concept:supplier",
      "name": "contact_email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_supplier.contact_email"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:supplier.onboarded_at",
      "concept_id": "concept:supplier",
      "name": "onboarded_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_supplier.onboarded_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:purchase_request.request_no",
      "concept_id": "concept:purchase_request",
      "name": "request_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique purchase request number.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_request.request_title",
      "concept_id": "concept:purchase_request",
      "name": "request_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.request_title"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_request.estimated_amount",
      "concept_id": "concept:purchase_request",
      "name": "estimated_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Must be non-negative. DDL comment says PR amount >= 50000 requires finance manager approval.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_request.currency_code",
      "concept_id": "concept:purchase_request",
      "name": "currency_code",
      "type": "attribute",
      "data_type": "CHAR(3)",
      "required": true,
      "description": "Default CNY.",
      "evidence_refs": [
        "ddl:pc_purchase_request.currency_code"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_request.request_status",
      "concept_id": "concept:purchase_request",
      "name": "request_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "DRAFT",
        "SUBMITTED",
        "APPROVED",
        "REJECTED",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_request.business_justification",
      "concept_id": "concept:purchase_request",
      "name": "business_justification",
      "type": "attribute",
      "data_type": "TEXT",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.business_justification"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_request.required_by_date",
      "concept_id": "concept:purchase_request",
      "name": "required_by_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_request.required_by_date"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:purchase_request.submitted_at",
      "concept_id": "concept:purchase_request",
      "name": "submitted_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_request.submitted_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:purchase_request.approved_at",
      "concept_id": "concept:purchase_request",
      "name": "approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_request.approved_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:purchase_request_line.item_description",
      "concept_id": "concept:purchase_request_line",
      "name": "item_description",
      "type": "attribute",
      "data_type": "VARCHAR(220)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.item_description"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_request_line.category_code",
      "concept_id": "concept:purchase_request_line",
      "name": "category_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.category_code"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:purchase_request_line.quantity",
      "concept_id": "concept:purchase_request_line",
      "name": "quantity",
      "type": "attribute",
      "data_type": "NUMERIC(12,2)",
      "required": true,
      "description": "Must be greater than zero.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.quantity"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_request_line.unit_of_measure",
      "concept_id": "concept:purchase_request_line",
      "name": "unit_of_measure",
      "type": "attribute",
      "data_type": "VARCHAR(20)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.unit_of_measure"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr:purchase_request_line.estimated_unit_price",
      "concept_id": "concept:purchase_request_line",
      "name": "estimated_unit_price",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.estimated_unit_price"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_request_line.line_amount",
      "concept_id": "concept:purchase_request_line",
      "name": "line_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Must be non-negative.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:approval_record.target_type",
      "concept_id": "concept:approval_record",
      "name": "target_type",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "allowed_values": [
        "PURCHASE_REQUEST",
        "CONTRACT",
        "PAYMENT_REQUEST"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:approval_record.target_id",
      "concept_id": "concept:approval_record",
      "name": "target_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Polymorphic target identifier without foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.82
    },
    {
      "id": "attr:approval_record.step_name",
      "concept_id": "concept:approval_record",
      "name": "step_name",
      "type": "attribute",
      "data_type": "VARCHAR(80)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_approval_record.step_name"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:approval_record.approval_status",
      "concept_id": "concept:approval_record",
      "name": "approval_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "PENDING",
        "APPROVED",
        "REJECTED",
        "SKIPPED"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:approval_record.approval_comment",
      "concept_id": "concept:approval_record",
      "name": "approval_comment",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_approval_record.approval_comment"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:approval_record.submitted_at",
      "concept_id": "concept:approval_record",
      "name": "submitted_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_approval_record.submitted_at"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr:approval_record.decided_at",
      "concept_id": "concept:approval_record",
      "name": "decided_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_approval_record.decided_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:contract.contract_no",
      "concept_id": "concept:contract",
      "name": "contract_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique contract number.",
      "evidence_refs": [
        "ddl:pc_contract.contract_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:contract.contract_title",
      "concept_id": "concept:contract",
      "name": "contract_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_contract.contract_title"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:contract.contract_amount",
      "concept_id": "concept:contract",
      "name": "contract_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Must be non-negative.",
      "evidence_refs": [
        "ddl:pc_contract.contract_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:contract.contract_status",
      "concept_id": "concept:contract",
      "name": "contract_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "DRAFT",
        "LEGAL_REVIEW",
        "ACTIVE",
        "EXPIRED",
        "TERMINATED"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:contract.start_date",
      "concept_id": "concept:contract",
      "name": "start_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.start_date"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:contract.end_date",
      "concept_id": "concept:contract",
      "name": "end_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.end_date"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:contract.legal_approved_at",
      "concept_id": "concept:contract",
      "name": "legal_approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.legal_approved_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:contract.activated_at",
      "concept_id": "concept:contract",
      "name": "activated_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.activated_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:contract.termination_reason",
      "concept_id": "concept:contract",
      "name": "termination_reason",
      "type": "attribute",
      "data_type": "VARCHAR(300)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.termination_reason"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:purchase_order.po_no",
      "concept_id": "concept:purchase_order",
      "name": "po_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique purchase order number.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_order.po_amount",
      "concept_id": "concept:purchase_order",
      "name": "po_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_order.po_amount"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:purchase_order.po_status",
      "concept_id": "concept:purchase_order",
      "name": "po_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "RELEASED",
        "PARTIALLY_RECEIVED",
        "CLOSED",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:purchase_order.released_at",
      "concept_id": "concept:purchase_order",
      "name": "released_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_order.released_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:purchase_order.closed_at",
      "concept_id": "concept:purchase_order",
      "name": "closed_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_order.closed_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:goods_receipt.receipt_no",
      "concept_id": "concept:goods_receipt",
      "name": "receipt_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique receipt number.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:goods_receipt.receipt_status",
      "concept_id": "concept:goods_receipt",
      "name": "receipt_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "PENDING",
        "PARTIAL",
        "COMPLETE",
        "REJECTED"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:goods_receipt.received_at",
      "concept_id": "concept:goods_receipt",
      "name": "received_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:goods_receipt.inspection_result",
      "concept_id": "concept:goods_receipt",
      "name": "inspection_result",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": false,
      "allowed_values": [
        "PASS",
        "FAIL",
        "NOT_REQUIRED"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:goods_receipt.remarks",
      "concept_id": "concept:goods_receipt",
      "name": "remarks",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_goods_receipt.remarks"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:invoice.invoice_no",
      "concept_id": "concept:invoice",
      "name": "invoice_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique invoice number.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:invoice.invoice_amount",
      "concept_id": "concept:invoice",
      "name": "invoice_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Must be non-negative.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:invoice.invoice_date",
      "concept_id": "concept:invoice",
      "name": "invoice_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "evidence_refs": [
        "ddl:pc_invoice.invoice_date"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:invoice.invoice_status",
      "concept_id": "concept:invoice",
      "name": "invoice_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "PENDING_MATCH",
        "MATCHED",
        "EXCEPTION",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:invoice.match_variance_amount",
      "concept_id": "concept:invoice",
      "name": "match_variance_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_invoice.match_variance_amount"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:invoice.matched_at",
      "concept_id": "concept:invoice",
      "name": "matched_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_invoice.matched_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:payment_request.payment_no",
      "concept_id": "concept:payment_request",
      "name": "payment_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique payment number.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:payment_request.payment_amount",
      "concept_id": "concept:payment_request",
      "name": "payment_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Must be non-negative.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:payment_request.payment_status",
      "concept_id": "concept:payment_request",
      "name": "payment_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "allowed_values": [
        "REQUESTED",
        "APPROVED",
        "PAID",
        "HELD",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr:payment_request.due_date",
      "concept_id": "concept:payment_request",
      "name": "due_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "evidence_refs": [
        "ddl:pc_payment_request.due_date"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr:payment_request.approved_at",
      "concept_id": "concept:payment_request",
      "name": "approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_payment_request.approved_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr:payment_request.paid_at",
      "concept_id": "concept:payment_request",
      "name": "paid_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_payment_request.paid_at"
      ],
      "confidence": 0.94
    }
  ],
  "relations": [
    {
      "id": "rel:user.department",
      "type": "relation",
      "source_concept_id": "concept:user",
      "target_concept_id": "concept:department",
      "predicate": "belongs_to_department",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_user.department_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:purchase_request.requester",
      "type": "relation",
      "source_concept_id": "concept:purchase_request",
      "target_concept_id": "concept:user",
      "predicate": "requested_by",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_request.requester_user_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:purchase_request.department",
      "type": "relation",
      "source_concept_id": "concept:purchase_request",
      "target_concept_id": "concept:department",
      "predicate": "for_department",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_request.department_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:purchase_request.preferred_supplier",
      "type": "relation",
      "source_concept_id": "concept:purchase_request",
      "target_concept_id": "concept:supplier",
      "predicate": "prefers_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_request.preferred_supplier_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "rel:purchase_request_line.purchase_request",
      "type": "relation",
      "source_concept_id": "concept:purchase_request_line",
      "target_concept_id": "concept:purchase_request",
      "predicate": "line_of",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel:approval_record.approver",
      "type": "relation",
      "source_concept_id": "concept:approval_record",
      "target_concept_id": "concept:user",
      "predicate": "approved_by",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_approval_record.approver_user_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:approval_record.purchase_request_target",
      "type": "relation",
      "source_concept_id": "concept:approval_record",
      "target_concept_id": "concept:purchase_request",
      "predicate": "targets_purchase_request",
      "cardinality": "many_to_one",
      "description": "Derived from target_type enum and target_id without a foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.72
    },
    {
      "id": "rel:approval_record.contract_target",
      "type": "relation",
      "source_concept_id": "concept:approval_record",
      "target_concept_id": "concept:contract",
      "predicate": "targets_contract",
      "cardinality": "many_to_one",
      "description": "Derived from target_type enum and target_id without a foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.72
    },
    {
      "id": "rel:approval_record.payment_request_target",
      "type": "relation",
      "source_concept_id": "concept:approval_record",
      "target_concept_id": "concept:payment_request",
      "predicate": "targets_payment_request",
      "cardinality": "many_to_one",
      "description": "Derived from target_type enum and target_id without a foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.72
    },
    {
      "id": "rel:contract.purchase_request",
      "type": "relation",
      "source_concept_id": "concept:contract",
      "target_concept_id": "concept:purchase_request",
      "predicate": "created_from_purchase_request",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_contract.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:contract.supplier",
      "type": "relation",
      "source_concept_id": "concept:contract",
      "target_concept_id": "concept:supplier",
      "predicate": "with_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_contract.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:contract.legal_reviewer",
      "type": "relation",
      "source_concept_id": "concept:contract",
      "target_concept_id": "concept:user",
      "predicate": "reviewed_by_legal_user",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_contract.legal_reviewer_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "rel:purchase_order.contract",
      "type": "relation",
      "source_concept_id": "concept:purchase_order",
      "target_concept_id": "concept:contract",
      "predicate": "issued_under_contract",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_order.contract_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:purchase_order.purchase_request",
      "type": "relation",
      "source_concept_id": "concept:purchase_order",
      "target_concept_id": "concept:purchase_request",
      "predicate": "created_from_purchase_request",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_order.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:purchase_order.supplier",
      "type": "relation",
      "source_concept_id": "concept:purchase_order",
      "target_concept_id": "concept:supplier",
      "predicate": "issued_to_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_purchase_order.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:goods_receipt.purchase_order",
      "type": "relation",
      "source_concept_id": "concept:goods_receipt",
      "target_concept_id": "concept:purchase_order",
      "predicate": "receives_against_purchase_order",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_goods_receipt.po_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:goods_receipt.received_by",
      "type": "relation",
      "source_concept_id": "concept:goods_receipt",
      "target_concept_id": "concept:user",
      "predicate": "received_by_user",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel:invoice.supplier",
      "type": "relation",
      "source_concept_id": "concept:invoice",
      "target_concept_id": "concept:supplier",
      "predicate": "issued_by_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_invoice.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:invoice.purchase_order",
      "type": "relation",
      "source_concept_id": "concept:invoice",
      "target_concept_id": "concept:purchase_order",
      "predicate": "matches_purchase_order",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_invoice.po_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:invoice.goods_receipt",
      "type": "relation",
      "source_concept_id": "concept:invoice",
      "target_concept_id": "concept:goods_receipt",
      "predicate": "matches_goods_receipt",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_invoice.receipt_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "rel:payment_request.invoice",
      "type": "relation",
      "source_concept_id": "concept:payment_request",
      "target_concept_id": "concept:invoice",
      "predicate": "pays_invoice",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_payment_request.invoice_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel:payment_request.approved_by",
      "type": "relation",
      "source_concept_id": "concept:payment_request",
      "target_concept_id": "concept:user",
      "predicate": "approved_by_user",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by"
      ],
      "confidence": 0.96
    }
  ],
  "events": [],
  "rules": [
    {
      "id": "rule:user.role_code_enum",
      "type": "rule",
      "name": "User role code must be in allowed set",
      "condition": "pc_user.role_code is set",
      "effect": "role_code must be one of REQUESTER, DEPT_MANAGER, PROCUREMENT_SPECIALIST, FINANCE_MANAGER, LEGAL_REVIEWER, WAREHOUSE_CLERK, AP_CLERK, PROCUREMENT_ADMIN",
      "applies_to_ids": [
        "concept:user",
        "attr:user.role_code"
      ],
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:supplier.status_enum",
      "type": "rule",
      "name": "Supplier status must be in allowed set",
      "condition": "pc_supplier.supplier_status is set",
      "effect": "supplier_status must be one of ACTIVE, SUSPENDED, PENDING_REVIEW",
      "applies_to_ids": [
        "concept:supplier",
        "attr:supplier.supplier_status"
      ],
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:supplier.risk_rating_enum",
      "type": "rule",
      "name": "Supplier risk rating must be in allowed set",
      "condition": "pc_supplier.risk_rating is set",
      "effect": "risk_rating must be one of LOW, MEDIUM, HIGH",
      "applies_to_ids": [
        "concept:supplier",
        "attr:supplier.risk_rating"
      ],
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:purchase_request.estimated_amount_nonnegative",
      "type": "rule",
      "name": "Purchase request estimated amount is non-negative",
      "condition": "pc_purchase_request.estimated_amount is set",
      "effect": "estimated_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "concept:purchase_request",
        "attr:purchase_request.estimated_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:purchase_request.finance_approval_threshold",
      "type": "rule",
      "name": "Finance approval required for large PR amount",
      "condition": "PR amount >= 50000",
      "effect": "Requires finance manager approval",
      "applies_to_ids": [
        "concept:purchase_request",
        "attr:purchase_request.estimated_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.9
    },
    {
      "id": "rule:purchase_request.status_enum",
      "type": "rule",
      "name": "Purchase request status must be in allowed set",
      "condition": "pc_purchase_request.request_status is set",
      "effect": "request_status must be one of DRAFT, SUBMITTED, APPROVED, REJECTED, CANCELLED",
      "applies_to_ids": [
        "concept:purchase_request",
        "attr:purchase_request.request_status"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:purchase_request_line.quantity_positive",
      "type": "rule",
      "name": "Purchase request line quantity is positive",
      "condition": "pc_purchase_request_line.quantity is set",
      "effect": "quantity must be greater than 0",
      "applies_to_ids": [
        "concept:purchase_request_line",
        "attr:purchase_request_line.quantity"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line.quantity"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:purchase_request_line.line_amount_nonnegative",
      "type": "rule",
      "name": "Purchase request line amount is non-negative",
      "condition": "pc_purchase_request_line.line_amount is set",
      "effect": "line_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "concept:purchase_request_line",
        "attr:purchase_request_line.line_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:approval_record.target_type_enum",
      "type": "rule",
      "name": "Approval target type must be in allowed set",
      "condition": "pc_approval_record.target_type is set",
      "effect": "target_type must be one of PURCHASE_REQUEST, CONTRACT, PAYMENT_REQUEST",
      "applies_to_ids": [
        "concept:approval_record",
        "attr:approval_record.target_type"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:approval_record.status_enum",
      "type": "rule",
      "name": "Approval status must be in allowed set",
      "condition": "pc_approval_record.approval_status is set",
      "effect": "approval_status must be one of PENDING, APPROVED, REJECTED, SKIPPED",
      "applies_to_ids": [
        "concept:approval_record",
        "attr:approval_record.approval_status"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:contract.amount_nonnegative",
      "type": "rule",
      "name": "Contract amount is non-negative",
      "condition": "pc_contract.contract_amount is set",
      "effect": "contract_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "concept:contract",
        "attr:contract.contract_amount"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:contract.status_enum",
      "type": "rule",
      "name": "Contract status must be in allowed set",
      "condition": "pc_contract.contract_status is set",
      "effect": "contract_status must be one of DRAFT, LEGAL_REVIEW, ACTIVE, EXPIRED, TERMINATED",
      "applies_to_ids": [
        "concept:contract",
        "attr:contract.contract_status"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:purchase_order.status_enum",
      "type": "rule",
      "name": "Purchase order status must be in allowed set",
      "condition": "pc_purchase_order.po_status is set",
      "effect": "po_status must be one of RELEASED, PARTIALLY_RECEIVED, CLOSED, CANCELLED",
      "applies_to_ids": [
        "concept:purchase_order",
        "attr:purchase_order.po_status"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:goods_receipt.status_enum",
      "type": "rule",
      "name": "Goods receipt status must be in allowed set",
      "condition": "pc_goods_receipt.receipt_status is set",
      "effect": "receipt_status must be one of PENDING, PARTIAL, COMPLETE, REJECTED",
      "applies_to_ids": [
        "concept:goods_receipt",
        "attr:goods_receipt.receipt_status"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:goods_receipt.inspection_result_enum",
      "type": "rule",
      "name": "Inspection result must be in allowed set",
      "condition": "pc_goods_receipt.inspection_result is set",
      "effect": "inspection_result must be one of PASS, FAIL, NOT_REQUIRED",
      "applies_to_ids": [
        "concept:goods_receipt",
        "attr:goods_receipt.inspection_result"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:invoice.amount_nonnegative",
      "type": "rule",
      "name": "Invoice amount is non-negative",
      "condition": "pc_invoice.invoice_amount is set",
      "effect": "invoice_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "concept:invoice",
        "attr:invoice.invoice_amount"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:invoice.status_enum",
      "type": "rule",
      "name": "Invoice status must be in allowed set",
      "condition": "pc_invoice.invoice_status is set",
      "effect": "invoice_status must be one of PENDING_MATCH, MATCHED, EXCEPTION, CANCELLED",
      "applies_to_ids": [
        "concept:invoice",
        "attr:invoice.invoice_status"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:payment_request.amount_nonnegative",
      "type": "rule",
      "name": "Payment amount is non-negative",
      "condition": "pc_payment_request.payment_amount is set",
      "effect": "payment_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "concept:payment_request",
        "attr:payment_request.payment_amount"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule:payment_request.status_enum",
      "type": "rule",
      "name": "Payment status must be in allowed set",
      "condition": "pc_payment_request.payment_status is set",
      "effect": "payment_status must be one of REQUESTED, APPROVED, PAID, HELD, CANCELLED",
      "applies_to_ids": [
        "concept:payment_request",
        "attr:payment_request.payment_status"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    }
  ],
  "actions": [],
  "states": [
    {
      "id": "state:supplier_status.active",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:supplier_status.suspended",
      "type": "state",
      "name": "SUSPENDED",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:supplier_status.pending_review",
      "type": "state",
      "name": "PENDING_REVIEW",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:risk_rating.low",
      "type": "state",
      "name": "LOW",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:risk_rating.medium",
      "type": "state",
      "name": "MEDIUM",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:risk_rating.high",
      "type": "state",
      "name": "HIGH",
      "owner_concept_id": "concept:supplier",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:request_status.draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept:purchase_request",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:request_status.submitted",
      "type": "state",
      "name": "SUBMITTED",
      "owner_concept_id": "concept:purchase_request",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:request_status.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept:purchase_request",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:request_status.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept:purchase_request",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:request_status.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept:purchase_request",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:approval_status.pending",
      "type": "state",
      "name": "PENDING",
      "owner_concept_id": "concept:approval_record",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:approval_status.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept:approval_record",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:approval_status.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept:approval_record",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:approval_status.skipped",
      "type": "state",
      "name": "SKIPPED",
      "owner_concept_id": "concept:approval_record",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:contract_status.draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept:contract",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:contract_status.legal_review",
      "type": "state",
      "name": "LEGAL_REVIEW",
      "owner_concept_id": "concept:contract",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:contract_status.active",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "concept:contract",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:contract_status.expired",
      "type": "state",
      "name": "EXPIRED",
      "owner_concept_id": "concept:contract",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:contract_status.terminated",
      "type": "state",
      "name": "TERMINATED",
      "owner_concept_id": "concept:contract",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:po_status.released",
      "type": "state",
      "name": "RELEASED",
      "owner_concept_id": "concept:purchase_order",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:po_status.partially_received",
      "type": "state",
      "name": "PARTIALLY_RECEIVED",
      "owner_concept_id": "concept:purchase_order",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:po_status.closed",
      "type": "state",
      "name": "CLOSED",
      "owner_concept_id": "concept:purchase_order",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:po_status.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept:purchase_order",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:receipt_status.pending",
      "type": "state",
      "name": "PENDING",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:receipt_status.partial",
      "type": "state",
      "name": "PARTIAL",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:receipt_status.complete",
      "type": "state",
      "name": "COMPLETE",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:receipt_status.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:inspection_result.pass",
      "type": "state",
      "name": "PASS",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:inspection_result.fail",
      "type": "state",
      "name": "FAIL",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:inspection_result.not_required",
      "type": "state",
      "name": "NOT_REQUIRED",
      "owner_concept_id": "concept:goods_receipt",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.98
    },
    {
      "id": "state:invoice_status.pending_match",
      "type": "state",
      "name": "PENDING_MATCH",
      "owner_concept_id": "concept:invoice",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:invoice_status.matched",
      "type": "state",
      "name": "MATCHED",
      "owner_concept_id": "concept:invoice",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:invoice_status.exception",
      "type": "state",
      "name": "EXCEPTION",
      "owner_concept_id": "concept:invoice",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:invoice_status.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept:invoice",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:payment_status.requested",
      "type": "state",
      "name": "REQUESTED",
      "owner_concept_id": "concept:payment_request",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:payment_status.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept:payment_request",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:payment_status.paid",
      "type": "state",
      "name": "PAID",
      "owner_concept_id": "concept:payment_request",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:payment_status.held",
      "type": "state",
      "name": "HELD",
      "owner_concept_id": "concept:payment_request",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state:payment_status.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept:payment_request",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    }
  ],
  "roles": [
    {
      "id": "role:requester",
      "type": "role",
      "name": "REQUESTER",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:dept_manager",
      "type": "role",
      "name": "DEPT_MANAGER",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:procurement_specialist",
      "type": "role",
      "name": "PROCUREMENT_SPECIALIST",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:finance_manager",
      "type": "role",
      "name": "FINANCE_MANAGER",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:legal_reviewer",
      "type": "role",
      "name": "LEGAL_REVIEWER",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:warehouse_clerk",
      "type": "role",
      "name": "WAREHOUSE_CLERK",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:ap_clerk",
      "type": "role",
      "name": "AP_CLERK",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role:procurement_admin",
      "type": "role",
      "name": "PROCUREMENT_ADMIN",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    }
  ],
  "permissions": [],
  "aliases": [
    {
      "id": "alias:prefix.pc",
      "type": "alias",
      "canonical_id": "procurement_contract",
      "alias": "pc_",
      "language": "en",
      "source_context": "Table prefix used by all DDL tables.",
      "evidence_refs": [
        "ddl:pc_department",
        "ddl:pc_user",
        "ddl:pc_supplier",
        "ddl:pc_purchase_request",
        "ddl:pc_contract"
      ],
      "confidence": 0.92
    },
    {
      "id": "alias:purchase_request.pr",
      "type": "alias",
      "canonical_id": "concept:purchase_request",
      "alias": "PR",
      "language": "en",
      "source_context": "DDL comment uses PR amount for pc_purchase_request.estimated_amount.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias:purchase_request.request",
      "type": "alias",
      "canonical_id": "concept:purchase_request",
      "alias": "request",
      "language": "en",
      "source_context": "pc_purchase_request uses request_id, request_no, request_title, request_status.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias:purchase_order.po",
      "type": "alias",
      "canonical_id": "concept:purchase_order",
      "alias": "PO",
      "language": "en",
      "source_context": "pc_purchase_order uses po_id, po_no, po_amount, po_status.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_no"
      ],
      "confidence": 0.96
    },
    {
      "id": "alias:goods_receipt.receipt",
      "type": "alias",
      "canonical_id": "concept:goods_receipt",
      "alias": "receipt",
      "language": "en",
      "source_context": "pc_goods_receipt uses receipt_id, receipt_no, receipt_status.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias:payment_request.payment",
      "type": "alias",
      "canonical_id": "concept:payment_request",
      "alias": "payment",
      "language": "en",
      "source_context": "pc_payment_request uses payment_no, payment_amount, payment_status.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.88
    }
  ],
  "mappings": [
    {
      "id": "map:concept.department",
      "type": "mapping",
      "ontology_element_id": "concept:department",
      "source_element": "table pc_department",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_department"
      ],
      "confidence": 0.98
    },
    {
      "id": "map:concept.user",
      "type": "mapping",
      "ontology_element_id": "concept:user",
      "source_element": "table pc_user",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_user"
      ],
      "confidence": 0.97
    },
    {
      "id": "map:concept.supplier",
      "type": "mapping",
      "ontology_element_id": "concept:supplier",
      "source_element": "table pc_supplier",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_supplier"
      ],
      "confidence": 0.98
    },
    {
      "id": "map:concept.purchase_request",
      "type": "mapping",
      "ontology_element_id": "concept:purchase_request",
      "source_element": "table pc_purchase_request",
      "source_type": "database",
 