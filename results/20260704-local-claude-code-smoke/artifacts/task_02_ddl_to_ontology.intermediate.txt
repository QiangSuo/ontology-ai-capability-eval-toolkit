{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-ddl-ontology",
  "title": "Procurement Contract MVP DDL Ontology Draft",
  "domain": "procurement_contract",
  "concepts": [
    {
      "id": "concept.department",
      "name": "Department",
      "type": "concept",
      "category": "organization",
      "description": "Organizational department with code, name, cost center, and active flag.",
      "alias_ids": [
        "alias.department.table_pc_department"
      ],
      "evidence_refs": [
        "ddl:pc_department"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept.user",
      "name": "User",
      "type": "concept",
      "category": "actor",
      "description": "System user associated with a department and role code.",
      "alias_ids": [
        "alias.user.table_pc_user"
      ],
      "evidence_refs": [
        "ddl:pc_user"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept.supplier",
      "name": "Supplier",
      "type": "concept",
      "category": "party",
      "description": "Supplier with status, risk rating, and onboarding/contact information.",
      "alias_ids": [
        "alias.supplier.table_pc_supplier"
      ],
      "evidence_refs": [
        "ddl:pc_supplier"
      ],
      "confidence": 0.96
    },
    {
      "id": "concept.purchase_request",
      "name": "Purchase Request",
      "type": "concept",
      "category": "document",
      "description": "Purchase request document containing requester, department, supplier preference, amount, status, and justification.",
      "alias_ids": [
        "alias.purchase_request.table_pc_purchase_request",
        "alias.purchase_request.pr"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept.purchase_request_line",
      "name": "Purchase Request Line",
      "type": "concept",
      "category": "document_line",
      "description": "Line item under a purchase request with item, category, quantity, unit, price, and amount.",
      "alias_ids": [
        "alias.purchase_request_line.table_pc_purchase_request_line"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line"
      ],
      "confidence": 0.97
    },
    {
      "id": "concept.approval_record",
      "name": "Approval Record",
      "type": "concept",
      "category": "approval",
      "description": "Approval record for purchase request, contract, or payment request targets.",
      "alias_ids": [
        "alias.approval_record.table_pc_approval_record"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record"
      ],
      "confidence": 0.94
    },
    {
      "id": "concept.contract",
      "name": "Contract",
      "type": "concept",
      "category": "document",
      "description": "Contract linked to purchase request and supplier, with amount, legal reviewer, status, and lifecycle dates.",
      "alias_ids": [
        "alias.contract.table_pc_contract"
      ],
      "evidence_refs": [
        "ddl:pc_contract"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept.purchase_order",
      "name": "Purchase Order",
      "type": "concept",
      "category": "document",
      "description": "Purchase order linked to contract, purchase request, and supplier.",
      "alias_ids": [
        "alias.purchase_order.table_pc_purchase_order",
        "alias.purchase_order.po"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept.goods_receipt",
      "name": "Goods Receipt",
      "type": "concept",
      "category": "document",
      "description": "Goods receipt linked to purchase order and receiving user, with receipt status and inspection result.",
      "alias_ids": [
        "alias.goods_receipt.table_pc_goods_receipt"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt"
      ],
      "confidence": 0.97
    },
    {
      "id": "concept.invoice",
      "name": "Invoice",
      "type": "concept",
      "category": "document",
      "description": "Supplier invoice linked to supplier, purchase order, and optionally goods receipt.",
      "alias_ids": [
        "alias.invoice.table_pc_invoice"
      ],
      "evidence_refs": [
        "ddl:pc_invoice"
      ],
      "confidence": 0.98
    },
    {
      "id": "concept.payment_request",
      "name": "Payment Request",
      "type": "concept",
      "category": "document",
      "description": "Payment request linked to invoice, with amount, status, due date, approval, and payment timestamps.",
      "alias_ids": [
        "alias.payment_request.table_pc_payment_request"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request"
      ],
      "confidence": 0.98
    }
  ],
  "attributes": [
    {
      "id": "attr.department.department_id",
      "concept_id": "concept.department",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_department.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.department.department_code",
      "concept_id": "concept.department",
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
      "id": "attr.department.department_name",
      "concept_id": "concept.department",
      "name": "department_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_department.department_name"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.department.cost_center",
      "concept_id": "concept.department",
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
      "id": "attr.department.is_active",
      "concept_id": "concept.department",
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
      "confidence": 0.97
    },
    {
      "id": "attr.department.created_at",
      "concept_id": "concept.department",
      "name": "created_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_department.created_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.user.user_id",
      "concept_id": "concept.user",
      "name": "user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.user.user_name",
      "concept_id": "concept.user",
      "name": "user_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_user.user_name"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.user.role_code",
      "concept_id": "concept.user",
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
      "id": "attr.user.department_id",
      "concept_id": "concept.user",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_department.department_id.",
      "evidence_refs": [
        "ddl:pc_user.department_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.user.email",
      "concept_id": "concept.user",
      "name": "email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_user.email"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.user.is_active",
      "concept_id": "concept.user",
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
      "confidence": 0.97
    },
    {
      "id": "attr.user.created_at",
      "concept_id": "concept.user",
      "name": "created_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_user.created_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.supplier.supplier_id",
      "concept_id": "concept.supplier",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.supplier.supplier_code",
      "concept_id": "concept.supplier",
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
      "id": "attr.supplier.supplier_name",
      "concept_id": "concept.supplier",
      "name": "supplier_name",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_supplier.supplier_name"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.supplier.supplier_status",
      "concept_id": "concept.supplier",
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
      "id": "attr.supplier.risk_rating",
      "concept_id": "concept.supplier",
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
      "id": "attr.supplier.contact_email",
      "concept_id": "concept.supplier",
      "name": "contact_email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_supplier.contact_email"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.supplier.onboarded_at",
      "concept_id": "concept.supplier",
      "name": "onboarded_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_supplier.onboarded_at"
      ],
      "confidence": 0.93
    },
    {
      "id": "attr.purchase_request.request_id",
      "concept_id": "concept.purchase_request",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.purchase_request.request_no",
      "concept_id": "concept.purchase_request",
      "name": "request_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique purchase request number.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_request.request_title",
      "concept_id": "concept.purchase_request",
      "name": "request_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.request_title"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.purchase_request.requester_user_id",
      "concept_id": "concept.purchase_request",
      "name": "requester_user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.requester_user_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_request.department_id",
      "concept_id": "concept.purchase_request",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_department.department_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.department_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_request.preferred_supplier_id",
      "concept_id": "concept.purchase_request",
      "name": "preferred_supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Optional foreign key to pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.preferred_supplier_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.purchase_request.estimated_amount",
      "concept_id": "concept.purchase_request",
      "name": "estimated_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Estimated purchase request amount. Comment states PR amount >= 50000 requires finance manager approval.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.purchase_request.currency_code",
      "concept_id": "concept.purchase_request",
      "name": "currency_code",
      "type": "attribute",
      "data_type": "CHAR(3)",
      "required": true,
      "description": "Default CNY.",
      "evidence_refs": [
        "ddl:pc_purchase_request.currency_code"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.purchase_request.request_status",
      "concept_id": "concept.purchase_request",
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
      "id": "attr.purchase_request.business_justification",
      "concept_id": "concept.purchase_request",
      "name": "business_justification",
      "type": "attribute",
      "data_type": "TEXT",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.business_justification"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.purchase_request.required_by_date",
      "concept_id": "concept.purchase_request",
      "name": "required_by_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_purchase_request.required_by_date"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.purchase_request.submitted_at",
      "concept_id": "concept.purchase_request",
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
      "id": "attr.purchase_request.approved_at",
      "concept_id": "concept.purchase_request",
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
      "id": "attr.purchase_request.created_at",
      "concept_id": "concept.purchase_request",
      "name": "created_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.created_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.purchase_request_line.line_id",
      "concept_id": "concept.purchase_request_line",
      "name": "line_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.purchase_request_line.request_id",
      "concept_id": "concept.purchase_request_line",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_request_line.item_description",
      "concept_id": "concept.purchase_request_line",
      "name": "item_description",
      "type": "attribute",
      "data_type": "VARCHAR(220)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.item_description"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.purchase_request_line.category_code",
      "concept_id": "concept.purchase_request_line",
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
      "id": "attr.purchase_request_line.quantity",
      "concept_id": "concept.purchase_request_line",
      "name": "quantity",
      "type": "attribute",
      "data_type": "NUMERIC(12,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.quantity"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_request_line.unit_of_measure",
      "concept_id": "concept.purchase_request_line",
      "name": "unit_of_measure",
      "type": "attribute",
      "data_type": "VARCHAR(20)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.unit_of_measure"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.purchase_request_line.estimated_unit_price",
      "concept_id": "concept.purchase_request_line",
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
      "id": "attr.purchase_request_line.line_amount",
      "concept_id": "concept.purchase_request_line",
      "name": "line_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_amount"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.approval_record.approval_id",
      "concept_id": "concept.approval_record",
      "name": "approval_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.approval_record.target_type",
      "concept_id": "concept.approval_record",
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
      "confidence": 0.98
    },
    {
      "id": "attr.approval_record.target_id",
      "concept_id": "concept.approval_record",
      "name": "target_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Polymorphic target identifier without a declared foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.72
    },
    {
      "id": "attr.approval_record.step_name",
      "concept_id": "concept.approval_record",
      "name": "step_name",
      "type": "attribute",
      "data_type": "VARCHAR(80)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_approval_record.step_name"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.approval_record.approver_user_id",
      "concept_id": "concept.approval_record",
      "name": "approver_user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_approval_record.approver_user_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.approval_record.approval_status",
      "concept_id": "concept.approval_record",
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
      "id": "attr.approval_record.approval_comment",
      "concept_id": "concept.approval_record",
      "name": "approval_comment",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_approval_record.approval_comment"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.approval_record.submitted_at",
      "concept_id": "concept.approval_record",
      "name": "submitted_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_approval_record.submitted_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.approval_record.decided_at",
      "concept_id": "concept.approval_record",
      "name": "decided_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_approval_record.decided_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.contract.contract_id",
      "concept_id": "concept.contract",
      "name": "contract_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_contract.contract_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.contract.contract_no",
      "concept_id": "concept.contract",
      "name": "contract_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique contract number.",
      "evidence_refs": [
        "ddl:pc_contract.contract_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.contract.request_id",
      "concept_id": "concept.contract",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_contract.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.contract.supplier_id",
      "concept_id": "concept.contract",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_contract.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.contract.contract_title",
      "concept_id": "concept.contract",
      "name": "contract_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_contract.contract_title"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.contract.contract_amount",
      "concept_id": "concept.contract",
      "name": "contract_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_contract.contract_amount"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.contract.contract_status",
      "concept_id": "concept.contract",
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
      "id": "attr.contract.start_date",
      "concept_id": "concept.contract",
      "name": "start_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.start_date"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.contract.end_date",
      "concept_id": "concept.contract",
      "name": "end_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.end_date"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.contract.legal_reviewer_id",
      "concept_id": "concept.contract",
      "name": "legal_reviewer_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Optional foreign key to pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_contract.legal_reviewer_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.contract.legal_approved_at",
      "concept_id": "concept.contract",
      "name": "legal_approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_contract.legal_approved_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.contract.activated_at",
      "concept_id": "concept.contract",
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
      "id": "attr.contract.termination_reason",
      "concept_id": "concept.contract",
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
      "id": "attr.contract.created_at",
      "concept_id": "concept.contract",
      "name": "created_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "evidence_refs": [
        "ddl:pc_contract.created_at"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr.purchase_order.po_id",
      "concept_id": "concept.purchase_order",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.purchase_order.po_no",
      "concept_id": "concept.purchase_order",
      "name": "po_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique purchase order number.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_order.contract_id",
      "concept_id": "concept.purchase_order",
      "name": "contract_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_contract.contract_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.contract_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_order.request_id",
      "concept_id": "concept.purchase_order",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_order.supplier_id",
      "concept_id": "concept.purchase_order",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.purchase_order.po_amount",
      "concept_id": "concept.purchase_order",
      "name": "po_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_purchase_order.po_amount"
      ],
      "confidence": 0.97
    },
    {
      "id": "attr.purchase_order.po_status",
      "concept_id": "concept.purchase_order",
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
      "id": "attr.purchase_order.released_at",
      "concept_id": "concept.purchase_order",
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
      "id": "attr.purchase_order.closed_at",
      "concept_id": "concept.purchase_order",
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
      "id": "attr.goods_receipt.receipt_id",
      "concept_id": "concept.goods_receipt",
      "name": "receipt_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.goods_receipt.receipt_no",
      "concept_id": "concept.goods_receipt",
      "name": "receipt_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique receipt number.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.goods_receipt.po_id",
      "concept_id": "concept.goods_receipt",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_purchase_order.po_id.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.po_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.goods_receipt.receipt_status",
      "concept_id": "concept.goods_receipt",
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
      "id": "attr.goods_receipt.received_by",
      "concept_id": "concept.goods_receipt",
      "name": "received_by",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_user.user_id; column name omits _user_id suffix.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.goods_receipt.received_at",
      "concept_id": "concept.goods_receipt",
      "name": "received_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_at"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.goods_receipt.inspection_result",
      "concept_id": "concept.goods_receipt",
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
      "id": "attr.goods_receipt.remarks",
      "concept_id": "concept.goods_receipt",
      "name": "remarks",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_goods_receipt.remarks"
      ],
      "confidence": 0.93
    },
    {
      "id": "attr.invoice.invoice_id",
      "concept_id": "concept.invoice",
      "name": "invoice_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.invoice.invoice_no",
      "concept_id": "concept.invoice",
      "name": "invoice_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique invoice number.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.invoice.supplier_id",
      "concept_id": "concept.invoice",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_invoice.supplier_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.invoice.po_id",
      "concept_id": "concept.invoice",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_purchase_order.po_id.",
      "evidence_refs": [
        "ddl:pc_invoice.po_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.invoice.receipt_id",
      "concept_id": "concept.invoice",
      "name": "receipt_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Optional foreign key to pc_goods_receipt.receipt_id.",
      "evidence_refs": [
        "ddl:pc_invoice.receipt_id"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.invoice.invoice_amount",
      "concept_id": "concept.invoice",
      "name": "invoice_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_invoice.invoice_amount"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.invoice.invoice_date",
      "concept_id": "concept.invoice",
      "name": "invoice_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "evidence_refs": [
        "ddl:pc_invoice.invoice_date"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.invoice.invoice_status",
      "concept_id": "concept.invoice",
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
      "id": "attr.invoice.match_variance_amount",
      "concept_id": "concept.invoice",
      "name": "match_variance_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": false,
      "evidence_refs": [
        "ddl:pc_invoice.match_variance_amount"
      ],
      "confidence": 0.94
    },
    {
      "id": "attr.invoice.matched_at",
      "concept_id": "concept.invoice",
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
      "id": "attr.payment_request.payment_request_id",
      "concept_id": "concept.payment_request",
      "name": "payment_request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Primary key.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "attr.payment_request.payment_no",
      "concept_id": "concept.payment_request",
      "name": "payment_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique payment request number.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.payment_request.invoice_id",
      "concept_id": "concept.payment_request",
      "name": "invoice_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Foreign key to pc_invoice.invoice_id.",
      "evidence_refs": [
        "ddl:pc_payment_request.invoice_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.payment_request.payment_amount",
      "concept_id": "concept.payment_request",
      "name": "payment_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "evidence_refs": [
        "ddl:pc_payment_request.payment_amount"
      ],
      "confidence": 0.98
    },
    {
      "id": "attr.payment_request.payment_status",
      "concept_id": "concept.payment_request",
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
      "id": "attr.payment_request.due_date",
      "concept_id": "concept.payment_request",
      "name": "due_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "evidence_refs": [
        "ddl:pc_payment_request.due_date"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.payment_request.approved_by",
      "concept_id": "concept.payment_request",
      "name": "approved_by",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Optional foreign key to pc_user.user_id; column name omits _user_id suffix.",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by"
      ],
      "confidence": 0.96
    },
    {
      "id": "attr.payment_request.approved_at",
      "concept_id": "concept.payment_request",
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
      "id": "attr.payment_request.paid_at",
      "concept_id": "concept.payment_request",
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
      "id": "rel.user.department",
      "type": "relation",
      "source_concept_id": "concept.user",
      "target_concept_id": "concept.department",
      "predicate": "belongs_to_department",
      "cardinality": "many_to_one",
      "description": "pc_user.department_id references pc_department.department_id.",
      "evidence_refs": [
        "ddl:pc_user.department_id",
        "ddl:pc_department.department_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.purchase_request.requester_user",
      "type": "relation",
      "source_concept_id": "concept.purchase_request",
      "target_concept_id": "concept.user",
      "predicate": "requested_by",
      "cardinality": "many_to_one",
      "description": "pc_purchase_request.requester_user_id references pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.requester_user_id",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.purchase_request.department",
      "type": "relation",
      "source_concept_id": "concept.purchase_request",
      "target_concept_id": "concept.department",
      "predicate": "belongs_to_department",
      "cardinality": "many_to_one",
      "description": "pc_purchase_request.department_id references pc_department.department_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.department_id",
        "ddl:pc_department.department_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.purchase_request.preferred_supplier",
      "type": "relation",
      "source_concept_id": "concept.purchase_request",
      "target_concept_id": "concept.supplier",
      "predicate": "prefers_supplier",
      "cardinality": "many_to_one",
      "description": "pc_purchase_request.preferred_supplier_id optionally references pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request.preferred_supplier_id",
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.94
    },
    {
      "id": "rel.purchase_request_line.purchase_request",
      "type": "relation",
      "source_concept_id": "concept.purchase_request_line",
      "target_concept_id": "concept.purchase_request",
      "predicate": "line_of",
      "cardinality": "many_to_one",
      "description": "pc_purchase_request_line.request_id references pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.request_id",
        "ddl:pc_purchase_request.request_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel.approval_record.approver_user",
      "type": "relation",
      "source_concept_id": "concept.approval_record",
      "target_concept_id": "concept.user",
      "predicate": "approved_by_user",
      "cardinality": "many_to_one",
      "description": "pc_approval_record.approver_user_id references pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_approval_record.approver_user_id",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.approval_record.purchase_request_target",
      "type": "relation",
      "source_concept_id": "concept.approval_record",
      "target_concept_id": "concept.purchase_request",
      "predicate": "targets_purchase_request",
      "cardinality": "many_to_one",
      "description": "target_type includes PURCHASE_REQUEST and target_id is the candidate target identifier, but no foreign key is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "rel.approval_record.contract_target",
      "type": "relation",
      "source_concept_id": "concept.approval_record",
      "target_concept_id": "concept.contract",
      "predicate": "targets_contract",
      "cardinality": "many_to_one",
      "description": "target_type includes CONTRACT and target_id is the candidate target identifier, but no foreign key is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "rel.approval_record.payment_request_target",
      "type": "relation",
      "source_concept_id": "concept.approval_record",
      "target_concept_id": "concept.payment_request",
      "predicate": "targets_payment_request",
      "cardinality": "many_to_one",
      "description": "target_type includes PAYMENT_REQUEST and target_id is the candidate target identifier, but no foreign key is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "rel.contract.purchase_request",
      "type": "relation",
      "source_concept_id": "concept.contract",
      "target_concept_id": "concept.purchase_request",
      "predicate": "created_from_purchase_request",
      "cardinality": "many_to_one",
      "description": "pc_contract.request_id references pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_contract.request_id",
        "ddl:pc_purchase_request.request_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.contract.supplier",
      "type": "relation",
      "source_concept_id": "concept.contract",
      "target_concept_id": "concept.supplier",
      "predicate": "contracted_supplier",
      "cardinality": "many_to_one",
      "description": "pc_contract.supplier_id references pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_contract.supplier_id",
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.contract.legal_reviewer",
      "type": "relation",
      "source_concept_id": "concept.contract",
      "target_concept_id": "concept.user",
      "predicate": "legal_reviewed_by",
      "cardinality": "many_to_one",
      "description": "pc_contract.legal_reviewer_id optionally references pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_contract.legal_reviewer_id",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.94
    },
    {
      "id": "rel.purchase_order.contract",
      "type": "relation",
      "source_concept_id": "concept.purchase_order",
      "target_concept_id": "concept.contract",
      "predicate": "issued_under_contract",
      "cardinality": "many_to_one",
      "description": "pc_purchase_order.contract_id references pc_contract.contract_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.contract_id",
        "ddl:pc_contract.contract_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.purchase_order.purchase_request",
      "type": "relation",
      "source_concept_id": "concept.purchase_order",
      "target_concept_id": "concept.purchase_request",
      "predicate": "issued_for_purchase_request",
      "cardinality": "many_to_one",
      "description": "pc_purchase_order.request_id references pc_purchase_request.request_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.request_id",
        "ddl:pc_purchase_request.request_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.purchase_order.supplier",
      "type": "relation",
      "source_concept_id": "concept.purchase_order",
      "target_concept_id": "concept.supplier",
      "predicate": "issued_to_supplier",
      "cardinality": "many_to_one",
      "description": "pc_purchase_order.supplier_id references pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_purchase_order.supplier_id",
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.goods_receipt.purchase_order",
      "type": "relation",
      "source_concept_id": "concept.goods_receipt",
      "target_concept_id": "concept.purchase_order",
      "predicate": "receives_against_purchase_order",
      "cardinality": "many_to_one",
      "description": "pc_goods_receipt.po_id references pc_purchase_order.po_id.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.po_id",
        "ddl:pc_purchase_order.po_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.goods_receipt.received_by_user",
      "type": "relation",
      "source_concept_id": "concept.goods_receipt",
      "target_concept_id": "concept.user",
      "predicate": "received_by_user",
      "cardinality": "many_to_one",
      "description": "pc_goods_receipt.received_by references pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.95
    },
    {
      "id": "rel.invoice.supplier",
      "type": "relation",
      "source_concept_id": "concept.invoice",
      "target_concept_id": "concept.supplier",
      "predicate": "issued_by_supplier",
      "cardinality": "many_to_one",
      "description": "pc_invoice.supplier_id references pc_supplier.supplier_id.",
      "evidence_refs": [
        "ddl:pc_invoice.supplier_id",
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.invoice.purchase_order",
      "type": "relation",
      "source_concept_id": "concept.invoice",
      "target_concept_id": "concept.purchase_order",
      "predicate": "invoices_purchase_order",
      "cardinality": "many_to_one",
      "description": "pc_invoice.po_id references pc_purchase_order.po_id.",
      "evidence_refs": [
        "ddl:pc_invoice.po_id",
        "ddl:pc_purchase_order.po_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.invoice.goods_receipt",
      "type": "relation",
      "source_concept_id": "concept.invoice",
      "target_concept_id": "concept.goods_receipt",
      "predicate": "matched_to_goods_receipt",
      "cardinality": "many_to_one",
      "description": "pc_invoice.receipt_id optionally references pc_goods_receipt.receipt_id.",
      "evidence_refs": [
        "ddl:pc_invoice.receipt_id",
        "ddl:pc_goods_receipt.receipt_id"
      ],
      "confidence": 0.94
    },
    {
      "id": "rel.payment_request.invoice",
      "type": "relation",
      "source_concept_id": "concept.payment_request",
      "target_concept_id": "concept.invoice",
      "predicate": "requests_payment_for_invoice",
      "cardinality": "many_to_one",
      "description": "pc_payment_request.invoice_id references pc_invoice.invoice_id.",
      "evidence_refs": [
        "ddl:pc_payment_request.invoice_id",
        "ddl:pc_invoice.invoice_id"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel.payment_request.approved_by_user",
      "type": "relation",
      "source_concept_id": "concept.payment_request",
      "target_concept_id": "concept.user",
      "predicate": "approved_by_user",
      "cardinality": "many_to_one",
      "description": "pc_payment_request.approved_by optionally references pc_user.user_id.",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.94
    }
  ],
  "events": [],
  "rules": [
    {
      "id": "rule.user.role_code_enum",
      "type": "rule",
      "name": "User role code must be enumerated",
      "condition": "pc_user.role_code is present",
      "effect": "role_code must be one of REQUESTER, DEPT_MANAGER, PROCUREMENT_SPECIALIST, FINANCE_MANAGER, LEGAL_REVIEWER, WAREHOUSE_CLERK, AP_CLERK, PROCUREMENT_ADMIN",
      "applies_to_ids": [
        "attr.user.role_code"
      ],
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.supplier.status_and_risk_enums",
      "type": "rule",
      "name": "Supplier status and risk rating must be enumerated",
      "condition": "pc_supplier.supplier_status and pc_supplier.risk_rating are present",
      "effect": "supplier_status must be ACTIVE, SUSPENDED, or PENDING_REVIEW; risk_rating must be LOW, MEDIUM, or HIGH",
      "applies_to_ids": [
        "attr.supplier.supplier_status",
        "attr.supplier.risk_rating"
      ],
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status",
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.purchase_request.amount_nonnegative",
      "type": "rule",
      "name": "Purchase request estimated amount cannot be negative",
      "condition": "pc_purchase_request.estimated_amount is present",
      "effect": "estimated_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "attr.purchase_request.estimated_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.purchase_request.status_enum",
      "type": "rule",
      "name": "Purchase request status must be enumerated",
      "condition": "pc_purchase_request.request_status is present",
      "effect": "request_status must be DRAFT, SUBMITTED, APPROVED, REJECTED, or CANCELLED",
      "applies_to_ids": [
        "attr.purchase_request.request_status"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.purchase_request.finance_approval_threshold",
      "type": "rule",
      "name": "High value purchase request requires finance manager approval",
      "condition": "PR amount is greater than or equal to 50000",
      "effect": "Finance manager approval is required",
      "applies_to_ids": [
        "concept.purchase_request",
        "attr.purchase_request.estimated_amount",
        "role.finance_manager"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.78
    },
    {
      "id": "rule.purchase_request_line.quantity_positive",
      "type": "rule",
      "name": "Purchase request line quantity must be positive",
      "condition": "pc_purchase_request_line.quantity is present",
      "effect": "quantity must be greater than 0",
      "applies_to_ids": [
        "attr.purchase_request_line.quantity"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line.quantity"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.purchase_request_line.amount_nonnegative",
      "type": "rule",
      "name": "Purchase request line amount cannot be negative",
      "condition": "pc_purchase_request_line.line_amount is present",
      "effect": "line_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "attr.purchase_request_line.line_amount"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.approval_record.target_type_enum",
      "type": "rule",
      "name": "Approval target type must be enumerated",
      "condition": "pc_approval_record.target_type is present",
      "effect": "target_type must be PURCHASE_REQUEST, CONTRACT, or PAYMENT_REQUEST",
      "applies_to_ids": [
        "attr.approval_record.target_type"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.approval_record.status_enum",
      "type": "rule",
      "name": "Approval status must be enumerated",
      "condition": "pc_approval_record.approval_status is present",
      "effect": "approval_status must be PENDING, APPROVED, REJECTED, or SKIPPED",
      "applies_to_ids": [
        "attr.approval_record.approval_status"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.contract.amount_nonnegative",
      "type": "rule",
      "name": "Contract amount cannot be negative",
      "condition": "pc_contract.contract_amount is present",
      "effect": "contract_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "attr.contract.contract_amount"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.contract.status_enum",
      "type": "rule",
      "name": "Contract status must be enumerated",
      "condition": "pc_contract.contract_status is present",
      "effect": "contract_status must be DRAFT, LEGAL_REVIEW, ACTIVE, EXPIRED, or TERMINATED",
      "applies_to_ids": [
        "attr.contract.contract_status"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.purchase_order.status_enum",
      "type": "rule",
      "name": "Purchase order status must be enumerated",
      "condition": "pc_purchase_order.po_status is present",
      "effect": "po_status must be RELEASED, PARTIALLY_RECEIVED, CLOSED, or CANCELLED",
      "applies_to_ids": [
        "attr.purchase_order.po_status"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.goods_receipt.status_and_inspection_enums",
      "type": "rule",
      "name": "Goods receipt status and inspection result must be enumerated",
      "condition": "pc_goods_receipt.receipt_status and pc_goods_receipt.inspection_result are present",
      "effect": "receipt_status must be PENDING, PARTIAL, COMPLETE, or REJECTED; inspection_result must be PASS, FAIL, or NOT_REQUIRED",
      "applies_to_ids": [
        "attr.goods_receipt.receipt_status",
        "attr.goods_receipt.inspection_result"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status",
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.invoice.amount_nonnegative",
      "type": "rule",
      "name": "Invoice amount cannot be negative",
      "condition": "pc_invoice.invoice_amount is present",
      "effect": "invoice_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "attr.invoice.invoice_amount"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.invoice.status_enum",
      "type": "rule",
      "name": "Invoice status must be enumerated",
      "condition": "pc_invoice.invoice_status is present",
      "effect": "invoice_status must be PENDING_MATCH, MATCHED, EXCEPTION, or CANCELLED",
      "applies_to_ids": [
        "attr.invoice.invoice_status"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.payment_request.amount_nonnegative",
      "type": "rule",
      "name": "Payment request amount cannot be negative",
      "condition": "pc_payment_request.payment_amount is present",
      "effect": "payment_amount must be greater than or equal to 0",
      "applies_to_ids": [
        "attr.payment_request.payment_amount"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.payment_request.status_enum",
      "type": "rule",
      "name": "Payment request status must be enumerated",
      "condition": "pc_payment_request.payment_status is present",
      "effect": "payment_status must be REQUESTED, APPROVED, PAID, HELD, or CANCELLED",
      "applies_to_ids": [
        "attr.payment_request.payment_status"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule.document_numbers_unique",
      "type": "rule",
      "name": "Business document numbers and codes must be unique where declared",
      "condition": "A UNIQUE constraint is declared on a code or number column",
      "effect": "department_code, supplier_code, request_no, contract_no, po_no, receipt_no, invoice_no, and payment_no values must be unique within their respective tables",
      "applies_to_ids": [
        "attr.department.department_code",
        "attr.supplier.supplier_code",
        "attr.purchase_request.request_no",
        "attr.contract.contract_no",
        "attr.purchase_order.po_no",
        "attr.goods_receipt.receipt_no",
        "attr.invoice.invoice_no",
        "attr.payment_request.payment_no"
      ],
      "evidence_refs": [
        "ddl:pc_department.department_code",
        "ddl:pc_supplier.supplier_code",
        "ddl:pc_purchase_request.request_no",
        "ddl:pc_contract.contract_no",
        "ddl:pc_purchase_order.po_no",
        "ddl:pc_goods_receipt.receipt_no",
        "ddl:pc_invoice.invoice_no",
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.99
    }
  ],
  "actions": [],
  "states": [
    {
      "id": "state.supplier.active",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed supplier_status value.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.supplier.suspended",
      "type": "state",
      "name": "SUSPENDED",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed supplier_status value.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.supplier.pending_review",
      "type": "state",
      "name": "PENDING_REVIEW",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed supplier_status value.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.supplier.risk_low",
      "type": "state",
      "name": "LOW",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed risk_rating value.",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.supplier.risk_medium",
      "type": "state",
      "name": "MEDIUM",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed risk_rating value.",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.supplier.risk_high",
      "type": "state",
      "name": "HIGH",
      "owner_concept_id": "concept.supplier",
      "description": "Allowed risk_rating value.",
      "evidence_refs": [
        "ddl:pc_supplier.risk_rating"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_request.draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept.purchase_request",
      "description": "Allowed request_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_request.submitted",
      "type": "state",
      "name": "SUBMITTED",
      "owner_concept_id": "concept.purchase_request",
      "description": "Allowed request_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_request.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept.purchase_request",
      "description": "Allowed request_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_request.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept.purchase_request",
      "description": "Allowed request_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_request.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept.purchase_request",
      "description": "Allowed request_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.approval_record.target_purchase_request",
      "type": "state",
      "name": "PURCHASE_REQUEST",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed target_type value.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.98
    },
    {
      "id": "state.approval_record.target_contract",
      "type": "state",
      "name": "CONTRACT",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed target_type value.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.98
    },
    {
      "id": "state.approval_record.target_payment_request",
      "type": "state",
      "name": "PAYMENT_REQUEST",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed target_type value.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type"
      ],
      "confidence": 0.98
    },
    {
      "id": "state.approval_record.pending",
      "type": "state",
      "name": "PENDING",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed approval_status value.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.approval_record.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed approval_status value.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.approval_record.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed approval_status value.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.approval_record.skipped",
      "type": "state",
      "name": "SKIPPED",
      "owner_concept_id": "concept.approval_record",
      "description": "Allowed approval_status value.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.contract.draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept.contract",
      "description": "Allowed contract_status value.",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.contract.legal_review",
      "type": "state",
      "name": "LEGAL_REVIEW",
      "owner_concept_id": "concept.contract",
      "description": "Allowed contract_status value.",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.contract.active",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "concept.contract",
      "description": "Allowed contract_status value.",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.contract.expired",
      "type": "state",
      "name": "EXPIRED",
      "owner_concept_id": "concept.contract",
      "description": "Allowed contract_status value.",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.contract.terminated",
      "type": "state",
      "name": "TERMINATED",
      "owner_concept_id": "concept.contract",
      "description": "Allowed contract_status value.",
      "evidence_refs": [
        "ddl:pc_contract.contract_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_order.released",
      "type": "state",
      "name": "RELEASED",
      "owner_concept_id": "concept.purchase_order",
      "description": "Allowed po_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_order.partially_received",
      "type": "state",
      "name": "PARTIALLY_RECEIVED",
      "owner_concept_id": "concept.purchase_order",
      "description": "Allowed po_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_order.closed",
      "type": "state",
      "name": "CLOSED",
      "owner_concept_id": "concept.purchase_order",
      "description": "Allowed po_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.purchase_order.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept.purchase_order",
      "description": "Allowed po_status value.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.pending",
      "type": "state",
      "name": "PENDING",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed receipt_status value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.partial",
      "type": "state",
      "name": "PARTIAL",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed receipt_status value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.complete",
      "type": "state",
      "name": "COMPLETE",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed receipt_status value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed receipt_status value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.inspection_pass",
      "type": "state",
      "name": "PASS",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed inspection_result value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.inspection_fail",
      "type": "state",
      "name": "FAIL",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed inspection_result value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.goods_receipt.inspection_not_required",
      "type": "state",
      "name": "NOT_REQUIRED",
      "owner_concept_id": "concept.goods_receipt",
      "description": "Allowed inspection_result value.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.inspection_result"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.invoice.pending_match",
      "type": "state",
      "name": "PENDING_MATCH",
      "owner_concept_id": "concept.invoice",
      "description": "Allowed invoice_status value.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.invoice.matched",
      "type": "state",
      "name": "MATCHED",
      "owner_concept_id": "concept.invoice",
      "description": "Allowed invoice_status value.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.invoice.exception",
      "type": "state",
      "name": "EXCEPTION",
      "owner_concept_id": "concept.invoice",
      "description": "Allowed invoice_status value.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.invoice.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept.invoice",
      "description": "Allowed invoice_status value.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.payment_request.requested",
      "type": "state",
      "name": "REQUESTED",
      "owner_concept_id": "concept.payment_request",
      "description": "Allowed payment_status value.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.payment_request.approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept.payment_request",
      "description": "Allowed payment_status value.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.payment_request.paid",
      "type": "state",
      "name": "PAID",
      "owner_concept_id": "concept.payment_request",
      "description": "Allowed payment_status value.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.payment_request.held",
      "type": "state",
      "name": "HELD",
      "owner_concept_id": "concept.payment_request",
      "description": "Allowed payment_status value.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    },
    {
      "id": "state.payment_request.cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept.payment_request",
      "description": "Allowed payment_status value.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.99
    }
  ],
  "roles": [
    {
      "id": "role.requester",
      "type": "role",
      "name": "REQUESTER",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.dept_manager",
      "type": "role",
      "name": "DEPT_MANAGER",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.procurement_specialist",
      "type": "role",
      "name": "PROCUREMENT_SPECIALIST",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.finance_manager",
      "type": "role",
      "name": "FINANCE_MANAGER",
      "description": "Allowed pc_user.role_code value; purchase request estimated_amount comment mentions finance manager approval threshold.",
      "evidence_refs": [
        "ddl:pc_user.role_code",
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.legal_reviewer",
      "type": "role",
      "name": "LEGAL_REVIEWER",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.warehouse_clerk",
      "type": "role",
      "name": "WAREHOUSE_CLERK",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.ap_clerk",
      "type": "role",
      "name": "AP_CLERK",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "role.procurement_admin",
      "type": "role",
      "name": "PROCUREMENT_ADMIN",
      "description": "Allowed pc_user.role_code value.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    }
  ],
  "permissions": [],
  "aliases": [
    {
      "id": "alias.schema.pc_prefix",
      "type": "alias",
      "canonical_id": "procurement-contract-mvp-ddl-ontology",
      "alias": "pc_",
      "language": "en",
      "source_context": "Common table prefix across all DDL tables.",
      "evidence_refs": [
        "ddl:pc_department",
        "ddl:pc_user",
        "ddl:pc_supplier",
        "ddl:pc_purchase_request",
        "ddl:pc_purchase_order"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias.purchase_request.table_pc_purchase_request",
      "type": "alias",
      "canonical_id": "concept.purchase_request",
      "alias": "pc_purchase_request",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_purchase_request"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.purchase_request.pr",
      "type": "alias",
      "canonical_id": "concept.purchase_request",
      "alias": "PR",
      "language": "en",
      "source_context": "Column comment uses PR amount for purchase request estimated amount.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.86
    },
    {
      "id": "alias.purchase_request.request_number",
      "type": "alias",
      "canonical_id": "attr.purchase_request.request_no",
      "alias": "pr_number",
      "language": "en",
      "source_context": "request_no is the purchase request number; PR abbreviation appears in estimated_amount comment.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_no",
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.78
    },
    {
      "id": "alias.purchase_order.table_pc_purchase_order",
      "type": "alias",
      "canonical_id": "concept.purchase_order",
      "alias": "pc_purchase_order",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_purchase_order"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.purchase_order.po",
      "type": "alias",
      "canonical_id": "concept.purchase_order",
      "alias": "PO",
      "language": "en",
      "source_context": "po_id, po_no, po_amount, and po_status columns abbreviate purchase order.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_id",
        "ddl:pc_purchase_order.po_no"
      ],
      "confidence": 0.96
    },
    {
      "id": "alias.purchase_order.po_number",
      "type": "alias",
      "canonical_id": "attr.purchase_order.po_no",
      "alias": "po_number",
      "language": "en",
      "source_context": "po_no represents purchase order number.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias.goods_receipt.receipt_number",
      "type": "alias",
      "canonical_id": "attr.goods_receipt.receipt_no",
      "alias": "receipt_number",
      "language": "en",
      "source_context": "receipt_no represents receipt number.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias.contract.contract_number",
      "type": "alias",
      "canonical_id": "attr.contract.contract_no",
      "alias": "contract_number",
      "language": "en",
      "source_context": "contract_no represents contract number.",
      "evidence_refs": [
        "ddl:pc_contract.contract_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias.invoice.invoice_number",
      "type": "alias",
      "canonical_id": "attr.invoice.invoice_no",
      "alias": "invoice_number",
      "language": "en",
      "source_context": "invoice_no represents invoice number.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias.payment_request.payment_number",
      "type": "alias",
      "canonical_id": "attr.payment_request.payment_no",
      "alias": "payment_number",
      "language": "en",
      "source_context": "payment_no represents payment request number.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.9
    },
    {
      "id": "alias.department.table_pc_department",
      "type": "alias",
      "canonical_id": "concept.department",
      "alias": "pc_department",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_department"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.user.table_pc_user",
      "type": "alias",
      "canonical_id": "concept.user",
      "alias": "pc_user",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_user"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.supplier.table_pc_supplier",
      "type": "alias",
      "canonical_id": "concept.supplier",
      "alias": "pc_supplier",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_supplier"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.purchase_request_line.table_pc_purchase_request_line",
      "type": "alias",
      "canonical_id": "concept.purchase_request_line",
      "alias": "pc_purchase_request_line",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.approval_record.table_pc_approval_record",
      "type": "alias",
      "canonical_id": "concept.approval_record",
      "alias": "pc_approval_record",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_approval_record"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.contract.table_pc_contract",
      "type": "alias",
      "canonical_id": "concept.contract",
      "alias": "pc_contract",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_contract"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.goods_receipt.table_pc_goods_receipt",
      "type": "alias",
      "canonical_id": "concept.goods_receipt",
      "alias": "pc_goods_receipt",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_goods_receipt"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.invoice.table_pc_invoice",
      "type": "alias",
      "canonical_id": "concept.invoice",
      "alias": "pc_invoice",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_invoice"
      ],
      "confidence": 0.99
    },
    {
      "id": "alias.payment_request.table_pc_payment_request",
      "type": "alias",
      "canonical_id": "concept.payment_request",
      "alias": "pc_payment_request",
      "language": "en",
      "source_context": "DDL table name.",
      "evidence_refs": [
        "ddl:pc_payment_request"
      ],
      "confidence": 0.99
    }
  ],
  "mappings": [
    {
      "id": "map.concept.department",
      "type": "mapping",
      "ontology_element_id": "concept.department",
      "source_element": "pc_department",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_department"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.user",
      "type": "mapping",
      "ontology_element_id": "concept.user",
      "source_element": "pc_user",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_user"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.supplier",
      "type": "mapping",
      "ontology_element_id": "concept.supplier",
      "source_element": "pc_supplier",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_supplier"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.purchase_request",
      "type": "mapping",
      "ontology_element_id": "concept.purchase_request",
      "source_element": "pc_purchase_request",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_purchase_request"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.purchase_request_line",
      "type": "mapping",
      "ontology_element_id": "concept.purchase_request_line",
      "source_element": "pc_purchase_request_line",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_purchase_request_line"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.approval_record",
      "type": "mapping",
      "ontology_element_id": "concept.approval_record",
      "source_element": "pc_approval_record",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_approval_record"
      ],
      "confidence": 0.98
    },
    {
      "id": "map.concept.contract",
      "type": "mapping",
      "ontology_element_id": "concept.contract",
      "source_element": "pc_contract",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_contract"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.purchase_order",
      "type": "mapping",
      "ontology_element_id": "concept.purchase_order",
      "source_element": "pc_purchase_order",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_purchase_order"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.goods_receipt",
      "type": "mapping",
      "ontology_element_id": "concept.goods_receipt",
      "source_element": "pc_goods_receipt",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_goods_receipt"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.invoice",
      "type": "mapping",
      "ontology_element_id": "concept.invoice",
      "source_element": "pc_invoice",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_invoice"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.concept.payment_request",
      "type": "mapping",
      "ontology_element_id": "concept.payment_request",
      "source_element": "pc_payment_request",
      "source_type": "database",
      "mapping_type": "exact",
      "evidence_refs": [
        "ddl:pc_payment_request"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.rel.approval_record.purchase_request_target",
      "type": "mapping",
      "ontology_element_id": "rel.approval_record.purchase_request_target",
      "source_element": "pc_approval_record.target_type IN ('PURCHASE_REQUEST',...) with pc_approval_record.target_id",
      "source_type": "database",
      "mapping_type": "candidate",
      "transform_note": "Polymorphic target relation inferred from target_type enum and target_id; no FK constraint is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "map.rel.approval_record.contract_target",
      "type": "mapping",
      "ontology_element_id": "rel.approval_record.contract_target",
      "source_element": "pc_approval_record.target_type IN (...,'CONTRACT',...) with pc_approval_record.target_id",
      "source_type": "database",
      "mapping_type": "candidate",
      "transform_note": "Polymorphic target relation inferred from target_type enum and target_id; no FK constraint is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "map.rel.approval_record.payment_request_target",
      "type": "mapping",
      "ontology_element_id": "rel.approval_record.payment_request_target",
      "source_element": "pc_approval_record.target_type IN (...,'PAYMENT_REQUEST') with pc_approval_record.target_id",
      "source_type": "database",
      "mapping_type": "candidate",
      "transform_note": "Polymorphic target relation inferred from target_type enum and target_id; no FK constraint is declared.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "map.rule.purchase_request.finance_approval_threshold",
      "type": "mapping",
      "ontology_element_id": "rule.purchase_request.finance_approval_threshold",
      "source_element": "COMMENT ON COLUMN pc_purchase_request.estimated_amount",
      "source_type": "database",
      "mapping_type": "partial",
      "transform_note": "Business rule is stated in a column comment, not enforced by a CHECK or FK.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.78
    },
    {
      "id": "map.rule.document_numbers_unique",
      "type": "mapping",
      "ontology_element_id": "rule.document_numbers_unique",
      "source_element": "UNIQUE constraints on department_code, supplier_code, request_no, contract_no, po_no, receipt_no, invoice_no, payment_no",
      "source_type": "database",
      "mapping_type": "derived",
      "evidence_refs": [
        "ddl:pc_department.department_code",
        "ddl:pc_supplier.supplier_code",
        "ddl:pc_purchase_request.request_no",
        "ddl:pc_contract.contract_no",
        "ddl:pc_purchase_order.po_no",
        "ddl:pc_goods_receipt.receipt_no",
        "ddl:pc_invoice.invoice_no",
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "map.roles.user_role_code",
      "type": "mapping",
      "ontology_element_id": "role.requester",
      "source_element": "pc_user.role_code CHECK enum",
      "source_type": "database",
      "mapping_type": "derived",
      "transform_note": "All role objects are derived from the same role_code CHECK constraint.",
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.99
    }
  ],
  "conflicts": [
    {
      "id": "conflict.approval_record.target_id_missing_fk",
      "type": "conflict",
      "description": "pc_approval_record.target_type enumerates PURCHASE_REQUEST, CONTRACT, and PAYMENT_REQUEST, but pc_approval_record.target_id has no foreign key to any of those target tables.",
      "involved_ids": [
        "concept.approval_record",
        "attr.approval_record.target_type",
        "attr.approval_record.target_id",
        "rel.approval_record.purchase_request_target",
        "rel.approval_record.contract_target",
        "rel.approval_record.payment_request_target"
      ],
      "severity": "medium",
      "resolution_status": "needs_human_review",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.9
    },
    {
      "id": "conflict.finance_approval_rule_not_enforced",
      "type": "conflict",
      "description": "The estimated_amount column comment states that PR amount >= 50000 requires finance manager approval, but the DDL only contains the comment and does not declare a constraint tying the threshold to approval records or FINANCE_MANAGER.",
      "involved_ids": [
        "rule.purchase_request.finance_approval_threshold",
        "attr.purchase_request.estimated_amount",
        "role.finance_manager",
        "concept.approval_record"
      ],
      "severity": "low",
      "resolution_status": "needs_human_review",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount",
        "ddl:pc_user.role_code",
        "ddl:pc_approval_record"
      ],
      "confidence": 0.86
    },
    {
      "id": "conflict.user_reference_naming_inconsistent",
      "type": "conflict",
      "description": "Most user references use *_user_id, but pc_goods_receipt.received_by and pc_payment_request.approved_by are BIGINT foreign keys to pc_user(user_id) without the _user_id suffix.",
      "involved_ids": [
        "attr.goods_receipt.received_by",
        "attr.payment_request.approved_by",
        "concept.user"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by",
        "ddl:pc_payment_request.approved_by",
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.82
    }
  ],
  "uncertainties": [
    {
      "id": "uncertainty.events_from_timestamps",
      "type": "uncertainty",
      "description": "Timestamp columns such as submitted_at, approved_at, released_at, received_at, matched_at, paid_at, activated_at, and closed_at suggest lifecycle moments, but the DDL does not explicitly define event objects or event semantics.",
      "reason": "DDL evidence is insufficient to extract business events beyond timestamp attributes.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.submitted_at",
        "ddl:pc_purchase_request.approved_at",
        "ddl:pc_purchase_order.released_at",
        "ddl:pc_goods_receipt.received_at",
        "ddl:pc_invoice.matched_at",
        "ddl:pc_payment_request.paid_at",
        "ddl:pc_contract.activated_at"
      ],
      "confidence": 0.35
    },
    {
      "id": "uncertainty.actions_not_defined",
      "type": "uncertainty",
      "description": "Actions such as submit, approve, release, receive, match, pay, activate, or close are implied by column names and statuses but are not explicitly modeled as action tables or action fields.",
      "reason": "No DDL table or column explicitly defines actionable operations with actors, preconditions, and postconditions.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.submitted_at",
        "ddl:pc_approval_record.approval_status",
        "ddl:pc_purchase_order.released_at",
        "ddl:pc_goods_receipt.received_by",
        "ddl:pc_payment_request.paid_at"
      ],
      "confidence": 0.32
    },
    {
      "id": "uncertainty.permissions_not_defined",
      "type": "uncertainty",
      "description": "Role codes are enumerated, but no permission table or constraint maps roles to allowed actions or resources.",
      "reason": "DDL contains role_code CHECK values but no role-permission relationship.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.42
    },
    {
      "id": "uncertainty.state_transitions_not_defined",
      "type": "uncertainty",
      "description": "Status enums define allowed status values but not valid transitions between values.",
      "reason": "CHECK constraints enumerate values only; no transition table, trigger, or constraint is present.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status",
        "ddl:pc_contract.contract_status",
        "ddl:pc_purchase_order.po_status",
        "ddl:pc_goods_receipt.receipt_status",
        "ddl:pc_invoice.invoice_status",
        "ddl:pc_payment_request.payment_status"
      ],
      "confidence": 0.45
    },
    {
      "id": "uncertainty.approval_target_cardinality",
      "type": "uncertainty",
      "target_id": "rel.approval_record.purchase_request_target",
      "description": "ApprovalRecord to target document relations are inferred from target_type and target_id, but no foreign key or cardinality constraint validates the target row.",
      "reason": "Polymorphic *_id field lacks FK constraints; relation confidence is capped below 0.75.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id"
      ],
      "confidence": 0.65
    },
    {
      "id": "uncertainty.payment_approval_role",
      "type": "uncertainty",
      "description": "pc_payment_request.approved_by references pc_user, but the DDL does not constrain the approving user's role_code.",
      "reason": "Foreign key proves a user relation, but role eligibility is not encoded.",
      "needs_human_review": true,
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by",
        "ddl:pc_user.role_code"
      ],
      "confidence": 0.55
    }
  ],
  "evidence_refs": [
    "ddl:pc_department",
    "ddl:pc_department.department_id",
    "ddl:pc_department.department_code",
    "ddl:pc_department.department_name",
    "ddl:pc_department.cost_center",
    "ddl:pc_department.is_active",
    "ddl:pc_department.created_at",
    "ddl:pc_user",
    "ddl:pc_user.user_id",
    "ddl:pc_user.user_name",
    "ddl:pc_user.role_code",
    "ddl:pc_user.department_id",
    "ddl:pc_user.email",
    "ddl:pc_user.is_active",
    "ddl:pc_user.created_at",
    "ddl:pc_supplier",
    "ddl:pc_supplier.supplier_id",
    "ddl:pc_supplier.supplier_code",
    "ddl:pc_supplier.supplier_name",
    "ddl:pc_supplier.supplier_status",
    "ddl:pc_supplier.risk_rating",
    "ddl:pc_supplier.contact_email",
    "ddl:pc_supplier.onboarded_at",
    "ddl:pc_purchase_request",
    "ddl:pc_purchase_request.request_id",
    "ddl:pc_purchase_request.request_no",
    "ddl:pc_purchase_request.request_title",
    "ddl:pc_purchase_request.requester_user_id",
    "ddl:pc_purchase_request.department_id",
    "ddl:pc_purchase_request.preferred_supplier_id",
    "ddl:pc_purchase_request.estimated_amount",
    "ddl:pc_purchase_request.currency_code",
    "ddl:pc_purchase_request.request_status",
    "ddl:pc_purchase_request.business_justification",
    "ddl:pc_purchase_request.required_by_date",
    "ddl:pc_purchase_request.submitted_at",
    "ddl:pc_purchase_request.approved_at",
    "ddl:pc_purchase_request.created_at",
    "ddl:pc_purchase_request_line",
    "ddl:pc_purchase_request_line.line_id",
    "ddl:pc_purchase_request_line.request_id",
    "ddl:pc_purchase_request_line.item_description",
    "ddl:pc_purchase_request_line.category_code",
    "ddl:pc_purchase_request_line.quantity",
    "ddl:pc_purchase_request_line.unit_of_measure",
    "ddl:pc_purchase_request_line.estimated_unit_price",
    "ddl:pc_purchase_request_line.line_amount",
    "ddl:pc_approval_record",
    "ddl:pc_approval_record.approval_id",
    "ddl:pc_approval_record.target_type",
    "ddl:pc_approval_record.target_id",
    "ddl:pc_approval_record.step_name",
    "ddl:pc_approval_record.approver_user_id",
    "ddl:pc_approval_record.approval_status",
    "ddl:pc_approval_record.approval_comment",
    "ddl:pc_approval_record.submitted_at",
    "ddl:pc_approval_record.decided_at",
    "ddl:pc_contract",
    "ddl:pc_contract.contract_id",
    "ddl:pc_contract.contract_no",
    "ddl:pc_contract.request_id",
    "ddl:pc_contract.supplier_id",
    "ddl:pc_contract.contract_title",
    "ddl:pc_contract.contract_amount",
    "ddl:pc_contract.contract_status",
    "ddl:pc_contract.start_date",
    "ddl:pc_contract.end_date",
    "ddl:pc_contract.legal_reviewer_id",
    "ddl:pc_contract.legal_approved_at",
    "ddl:pc_contract.activated_at",
    "ddl:pc_contract.termination_reason",
    "ddl:pc_contract.created_at",
    "ddl:pc_purchase_order",
    "ddl:pc_purchase_order.po_id",
    "ddl:pc_purchase_order.po_no",
    "ddl:pc_purchase_order.contract_id",
    "ddl:pc_purchase_order.request_id",
    "ddl:pc_purchase_order.supplier_id",
    "ddl:pc_purchase_order.po_amount",
    "ddl:pc_purchase_order.po_status",
    "ddl:pc_purchase_order.released_at",
    "ddl:pc_purchase_order.closed_at",
    "ddl:pc_goods_receipt",
    "ddl:pc_goods_receipt.receipt_id",
    "ddl:pc_goods_receipt.receipt_no",
    "ddl:pc_goods_receipt.po_id",
    "ddl:pc_goods_receipt.receipt_status",
    "ddl:pc_goods_receipt.received_by",
    "ddl:pc_goods_receipt.received_at",
    "ddl:pc_goods_receipt.inspection_result",
    "ddl:pc_goods_receipt.remarks",
    "ddl:pc_invoice",
    "ddl:pc_invoice.invoice_id",
    "ddl:pc_invoice.invoice_no",
    "ddl:pc_invoice.supplier_id",
    "ddl:pc_invoice.po_id",
    "ddl:pc_invoice.receipt_id",
    "ddl:pc_invoice.invoice_amount",
    "ddl:pc_invoice.invoice_date",
    "ddl:pc_invoice.invoice_status",
    "ddl:pc_invoice.match_variance_amount",
    "ddl:pc_invoice.matched_at",
    "ddl:pc_payment_request",
    "ddl:pc_payment_request.payment_request_id",
    "ddl:pc_payment_request.payment_no",
    "ddl:pc_payment_request.invoice_id",
    "ddl:pc_payment_request.payment_amount",
    "ddl:pc_payment_request.payment_status",
    "ddl:pc_payment_request.due_date",
    "ddl:pc_payment_request.approved_by",
    "ddl:pc_payment_request.approved_at",
    "ddl:pc_payment_request.paid_at"
  ],
  "confidence": 0.89,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "database_ddl"
  }
}
