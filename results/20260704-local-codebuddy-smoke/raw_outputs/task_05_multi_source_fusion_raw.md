{
  "schema_version": "1.0",
  "ontology_id": "generic_procurement_contract_mvp",
  "title": "Generic Procurement Contract MVP Ontology",
  "domain": "procurement_contract",
  "description": "Unified ontology for a procurement contract MVP covering purchase request, approval, contract, purchase order, receiving, invoice matching and payment request lifecycle.",
  "concepts": [
    {
      "id": "department",
      "name": "Department",
      "type": "concept",
      "description": "Organizational unit owning purchase requests and users.",
      "category": "organization",
      "attribute_ids": [
        "department.department_id",
        "department.department_code",
        "department.department_name",
        "department.cost_center",
        "department.is_active"
      ],
      "evidence_refs": [
        "ddl:pc_department",
        "csv:pc_department",
        "doc:business_overview"
      ],
      "confidence": 0.99
    },
    {
      "id": "user",
      "name": "User",
      "type": "concept",
      "description": "System actor belonging to a department and assigned a procurement role.",
      "category": "actor",
      "attribute_ids": [
        "user.user_id",
        "user.user_name",
        "user.role_code",
        "user.department_id",
        "user.email",
        "user.is_active"
      ],
      "evidence_refs": [
        "ddl:pc_user",
        "csv:pc_user",
        "doc:business_overview",
        "code:RoleCode"
      ],
      "confidence": 0.99
    },
    {
      "id": "supplier",
      "name": "Supplier",
      "type": "concept",
      "description": "External provider of goods or services, also called Vendor.",
      "category": "party",
      "attribute_ids": [
        "supplier.supplier_id",
        "supplier.supplier_code",
        "supplier.supplier_name",
        "supplier.supplier_status",
        "supplier.risk_rating",
        "supplier.contact_email",
        "supplier.onboarded_at"
      ],
      "alias_ids": [
        "alias_supplier_vendor"
      ],
      "evidence_refs": [
        "ddl:pc_supplier",
        "csv:pc_supplier",
        "doc:business_overview",
        "doc:glossary",
        "code:Supplier"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request",
      "name": "Purchase Request",
      "type": "concept",
      "description": "Business request for goods or services before sourcing or contracting.",
      "category": "document",
      "attribute_ids": [
        "purchase_request.request_id",
        "purchase_request.request_no",
        "purchase_request.request_title",
        "purchase_request.requester_user_id",
        "purchase_request.department_id",
        "purchase_request.preferred_supplier_id",
        "purchase_request.estimated_amount",
        "purchase_request.currency_code",
        "purchase_request.request_status",
        "purchase_request.business_justification",
        "purchase_request.required_by_date",
        "purchase_request.submitted_at",
        "purchase_request.approved_at"
      ],
      "state_ids": [
        "state_pr_draft",
        "state_pr_submitted",
        "state_pr_approved",
        "state_pr_rejected",
        "state_pr_cancelled"
      ],
      "alias_ids": [
        "alias_purchase_request_pr"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request",
        "csv:pc_purchase_request",
        "doc:business_overview",
        "doc:procurement_process",
        "code:PurchaseRequest"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line",
      "name": "Purchase Request Line",
      "type": "concept",
      "description": "Item or service line under a purchase request.",
      "category": "document_line",
      "attribute_ids": [
        "purchase_request_line.line_id",
        "purchase_request_line.request_id",
        "purchase_request_line.item_description",
        "purchase_request_line.category_code",
        "purchase_request_line.quantity",
        "purchase_request_line.unit_of_measure",
        "purchase_request_line.estimated_unit_price",
        "purchase_request_line.line_amount"
      ],
      "alias_ids": [
        "alias_material_item"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request_line",
        "csv:pc_purchase_request_line",
        "doc:business_overview",
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record",
      "name": "Approval Record",
      "type": "concept",
      "description": "Workflow decision record for purchase request, contract, or payment request; target is modeled polymorphically by target_type and target_id.",
      "category": "workflow_record",
      "attribute_ids": [
        "approval_record.approval_id",
        "approval_record.target_type",
        "approval_record.target_id",
        "approval_record.step_name",
        "approval_record.approver_user_id",
        "approval_record.approval_status",
        "approval_record.approval_comment",
        "approval_record.submitted_at",
        "approval_record.decided_at"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record",
        "csv:pc_approval_record",
        "doc:business_overview",
        "doc:glossary"
      ],
      "confidence": 0.88
    },
    {
      "id": "contract",
      "name": "Contract",
      "type": "concept",
      "description": "Legal agreement with a supplier created from an approved purchase request.",
      "category": "legal_document",
      "attribute_ids": [
        "contract.contract_id",
        "contract.contract_no",
        "contract.request_id",
        "contract.supplier_id",
        "contract.contract_title",
        "contract.contract_amount",
        "contract.contract_status",
        "contract.start_date",
        "contract.end_date",
        "contract.legal_reviewer_id",
        "contract.legal_approved_at",
        "contract.activated_at",
        "contract.termination_reason"
      ],
      "state_ids": [
        "state_contract_draft",
        "state_contract_legal_review",
        "state_contract_active",
        "state_contract_expired",
        "state_contract_terminated"
      ],
      "evidence_refs": [
        "ddl:pc_contract",
        "csv:pc_contract",
        "doc:contract_lifecycle",
        "code:Contract"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order",
      "name": "Purchase Order",
      "type": "concept",
      "description": "Operational order released against an active contract.",
      "category": "document",
      "attribute_ids": [
        "purchase_order.po_id",
        "purchase_order.po_no",
        "purchase_order.contract_id",
        "purchase_order.request_id",
        "purchase_order.supplier_id",
        "purchase_order.po_amount",
        "purchase_order.po_status",
        "purchase_order.released_at",
        "purchase_order.closed_at"
      ],
      "state_ids": [
        "state_po_released",
        "state_po_partially_received",
        "state_po_closed",
        "state_po_cancelled"
      ],
      "alias_ids": [
        "alias_purchase_order_po"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order",
        "csv:pc_purchase_order",
        "doc:business_overview",
        "code:PurchaseOrder"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt",
      "name": "Goods Receipt",
      "type": "concept",
      "description": "Warehouse receiving evidence for goods or services delivered against a purchase order.",
      "category": "document",
      "attribute_ids": [
        "goods_receipt.receipt_id",
        "goods_receipt.receipt_no",
        "goods_receipt.po_id",
        "goods_receipt.receipt_status",
        "goods_receipt.received_by",
        "goods_receipt.received_at",
        "goods_receipt.inspection_result",
        "goods_receipt.remarks"
      ],
      "state_ids": [
        "state_gr_pending",
        "state_gr_partial",
        "state_gr_complete",
        "state_gr_rejected"
      ],
      "alias_ids": [
        "alias_goods_receipt_grn"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt",
        "csv:pc_goods_receipt",
        "doc:receipt_invoice_payment_policy",
        "code:GoodsReceipt"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice",
      "name": "Invoice",
      "type": "concept",
      "description": "Supplier billing document matched against purchase order and goods receipt.",
      "category": "document",
      "attribute_ids": [
        "invoice.invoice_id",
        "invoice.invoice_no",
        "invoice.supplier_id",
        "invoice.po_id",
        "invoice.receipt_id",
        "invoice.invoice_amount",
        "invoice.invoice_date",
        "invoice.invoice_status",
        "invoice.match_variance_amount",
        "invoice.matched_at"
      ],
      "state_ids": [
        "state_invoice_pending_match",
        "state_invoice_matched",
        "state_invoice_exception",
        "state_invoice_cancelled"
      ],
      "evidence_refs": [
        "ddl:pc_invoice",
        "csv:pc_invoice",
        "doc:receipt_invoice_payment_policy",
        "code:Invoice"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request",
      "name": "Payment Request",
      "type": "concept",
      "description": "Finance request to pay a matched invoice, also called Payment Application.",
      "category": "document",
      "attribute_ids": [
        "payment_request.payment_request_id",
        "payment_request.payment_no",
        "payment_request.invoice_id",
        "payment_request.payment_amount",
        "payment_request.payment_status",
        "payment_request.due_date",
        "payment_request.approved_by",
        "payment_request.approved_at",
        "payment_request.paid_at"
      ],
      "state_ids": [
        "state_payment_requested",
        "state_payment_approved",
        "state_payment_paid",
        "state_payment_held",
        "state_payment_cancelled"
      ],
      "alias_ids": [
        "alias_payment_request_payment_application"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request",
        "csv:pc_payment_request",
        "doc:receipt_invoice_payment_policy",
        "code:PaymentRequest"
      ],
      "confidence": 0.99
    }
  ],
  "attributes": [
    {
      "id": "department.department_id",
      "concept_id": "department",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Department primary key.",
      "evidence_refs": [
        "ddl:pc_department.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "department.department_code",
      "concept_id": "department",
      "name": "department_code",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Unique department code.",
      "evidence_refs": [
        "ddl:pc_department.department_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "department.department_name",
      "concept_id": "department",
      "name": "department_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "description": "Department name.",
      "evidence_refs": [
        "ddl:pc_department.department_name"
      ],
      "confidence": 0.99
    },
    {
      "id": "department.cost_center",
      "concept_id": "department",
      "name": "cost_center",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Cost center for department.",
      "evidence_refs": [
        "ddl:pc_department.cost_center"
      ],
      "confidence": 0.98
    },
    {
      "id": "department.is_active",
      "concept_id": "department",
      "name": "is_active",
      "type": "attribute",
      "data_type": "BOOLEAN",
      "required": true,
      "description": "Active flag.",
      "allowed_values": [
        true,
        false
      ],
      "evidence_refs": [
        "ddl:pc_department.is_active"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.user_id",
      "concept_id": "user",
      "name": "user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "User primary key.",
      "evidence_refs": [
        "ddl:pc_user.user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.user_name",
      "concept_id": "user",
      "name": "user_name",
      "type": "attribute",
      "data_type": "VARCHAR(120)",
      "required": true,
      "description": "User display name.",
      "evidence_refs": [
        "ddl:pc_user.user_name"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.role_code",
      "concept_id": "user",
      "name": "role_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Assigned role code.",
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
        "ddl:pc_user.role_code",
        "code:RoleCode"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.department_id",
      "concept_id": "user",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Department foreign key.",
      "evidence_refs": [
        "ddl:pc_user.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.email",
      "concept_id": "user",
      "name": "email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "description": "User email address.",
      "evidence_refs": [
        "ddl:pc_user.email"
      ],
      "confidence": 0.99
    },
    {
      "id": "user.is_active",
      "concept_id": "user",
      "name": "is_active",
      "type": "attribute",
      "data_type": "BOOLEAN",
      "required": true,
      "description": "Active flag.",
      "allowed_values": [
        true,
        false
      ],
      "evidence_refs": [
        "ddl:pc_user.is_active"
      ],
      "confidence": 0.99
    },
    {
      "id": "supplier.supplier_id",
      "concept_id": "supplier",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Supplier primary key.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "supplier.supplier_code",
      "concept_id": "supplier",
      "name": "supplier_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique supplier code.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "supplier.supplier_name",
      "concept_id": "supplier",
      "name": "supplier_name",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": true,
      "description": "Supplier name.",
      "evidence_refs": [
        "ddl:pc_supplier.supplier_name"
      ],
      "confidence": 0.99
    },
    {
      "id": "supplier.supplier_status",
      "concept_id": "supplier",
      "name": "supplier_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Supplier lifecycle status.",
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
      "id": "supplier.risk_rating",
      "concept_id": "supplier",
      "name": "risk_rating",
      "type": "attribute",
      "data_type": "VARCHAR(20)",
      "required": true,
      "description": "Supplier risk rating.",
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
      "id": "supplier.contact_email",
      "concept_id": "supplier",
      "name": "contact_email",
      "type": "attribute",
      "data_type": "VARCHAR(160)",
      "required": false,
      "description": "Supplier contact email.",
      "evidence_refs": [
        "ddl:pc_supplier.contact_email"
      ],
      "confidence": 0.98
    },
    {
      "id": "supplier.onboarded_at",
      "concept_id": "supplier",
      "name": "onboarded_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Supplier onboarding timestamp.",
      "evidence_refs": [
        "ddl:pc_supplier.onboarded_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "purchase_request.request_id",
      "concept_id": "purchase_request",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Purchase request primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.request_no",
      "concept_id": "purchase_request",
      "name": "request_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique request number.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.request_title",
      "concept_id": "purchase_request",
      "name": "request_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "description": "Request title.",
      "evidence_refs": [
        "ddl:pc_purchase_request.request_title"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.requester_user_id",
      "concept_id": "purchase_request",
      "name": "requester_user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "User who requested the purchase.",
      "evidence_refs": [
        "ddl:pc_purchase_request.requester_user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.department_id",
      "concept_id": "purchase_request",
      "name": "department_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Owning department.",
      "evidence_refs": [
        "ddl:pc_purchase_request.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.preferred_supplier_id",
      "concept_id": "purchase_request",
      "name": "preferred_supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Preferred supplier if provided.",
      "evidence_refs": [
        "ddl:pc_purchase_request.preferred_supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.estimated_amount",
      "concept_id": "purchase_request",
      "name": "estimated_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Estimated request amount; must be non-negative.",
      "evidence_refs": [
        "ddl:pc_purchase_request.estimated_amount",
        "code:PurchaseRequest",
        "code:ApprovalService"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.currency_code",
      "concept_id": "purchase_request",
      "name": "currency_code",
      "type": "attribute",
      "data_type": "CHAR(3)",
      "required": true,
      "description": "Currency code, default CNY.",
      "evidence_refs": [
        "ddl:pc_purchase_request.currency_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.request_status",
      "concept_id": "purchase_request",
      "name": "request_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Purchase request status.",
      "allowed_values": [
        "DRAFT",
        "SUBMITTED",
        "APPROVED",
        "REJECTED",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_request.request_status",
        "code:ProcurementStatus"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.business_justification",
      "concept_id": "purchase_request",
      "name": "business_justification",
      "type": "attribute",
      "data_type": "TEXT",
      "required": true,
      "description": "Business justification required before submission.",
      "evidence_refs": [
        "ddl:pc_purchase_request.business_justification",
        "doc:business_rules",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request.required_by_date",
      "concept_id": "purchase_request",
      "name": "required_by_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "description": "Required delivery date.",
      "evidence_refs": [
        "ddl:pc_purchase_request.required_by_date"
      ],
      "confidence": 0.98
    },
    {
      "id": "purchase_request.submitted_at",
      "concept_id": "purchase_request",
      "name": "submitted_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Submission timestamp.",
      "evidence_refs": [
        "ddl:pc_purchase_request.submitted_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "purchase_request.approved_at",
      "concept_id": "purchase_request",
      "name": "approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Approval timestamp.",
      "evidence_refs": [
        "ddl:pc_purchase_request.approved_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "purchase_request_line.line_id",
      "concept_id": "purchase_request_line",
      "name": "line_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Line primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.request_id",
      "concept_id": "purchase_request_line",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Parent purchase request key.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.item_description",
      "concept_id": "purchase_request_line",
      "name": "item_description",
      "type": "attribute",
      "data_type": "VARCHAR(220)",
      "required": true,
      "description": "Item or service description.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.item_description"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.category_code",
      "concept_id": "purchase_request_line",
      "name": "category_code",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Procurement category code.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.category_code"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.quantity",
      "concept_id": "purchase_request_line",
      "name": "quantity",
      "type": "attribute",
      "data_type": "NUMERIC(12,2)",
      "required": true,
      "description": "Quantity; must be greater than zero.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.quantity"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.unit_of_measure",
      "concept_id": "purchase_request_line",
      "name": "unit_of_measure",
      "type": "attribute",
      "data_type": "VARCHAR(20)",
      "required": true,
      "description": "Unit of measure.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.unit_of_measure"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.estimated_unit_price",
      "concept_id": "purchase_request_line",
      "name": "estimated_unit_price",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Estimated unit price.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.estimated_unit_price"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_request_line.line_amount",
      "concept_id": "purchase_request_line",
      "name": "line_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Line amount; must be non-negative.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.line_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record.approval_id",
      "concept_id": "approval_record",
      "name": "approval_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Approval record primary key.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record.target_type",
      "concept_id": "approval_record",
      "name": "target_type",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Polymorphic approval target type.",
      "allowed_values": [
        "PURCHASE_REQUEST",
        "CONTRACT",
        "PAYMENT_REQUEST"
      ],
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "csv:pc_approval_record"
      ],
      "confidence": 0.9
    },
    {
      "id": "approval_record.target_id",
      "concept_id": "approval_record",
      "name": "target_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Polymorphic target identifier.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_id",
        "csv:pc_approval_record"
      ],
      "confidence": 0.88
    },
    {
      "id": "approval_record.step_name",
      "concept_id": "approval_record",
      "name": "step_name",
      "type": "attribute",
      "data_type": "VARCHAR(80)",
      "required": true,
      "description": "Approval step name.",
      "evidence_refs": [
        "ddl:pc_approval_record.step_name"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record.approver_user_id",
      "concept_id": "approval_record",
      "name": "approver_user_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Approver user foreign key.",
      "evidence_refs": [
        "ddl:pc_approval_record.approver_user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record.approval_status",
      "concept_id": "approval_record",
      "name": "approval_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Approval decision status.",
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
      "id": "approval_record.approval_comment",
      "concept_id": "approval_record",
      "name": "approval_comment",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "description": "Decision comment or rejection reason.",
      "evidence_refs": [
        "ddl:pc_approval_record.approval_comment",
        "code:ApprovalService"
      ],
      "confidence": 0.98
    },
    {
      "id": "approval_record.submitted_at",
      "concept_id": "approval_record",
      "name": "submitted_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": true,
      "description": "Approval step submitted time.",
      "evidence_refs": [
        "ddl:pc_approval_record.submitted_at"
      ],
      "confidence": 0.99
    },
    {
      "id": "approval_record.decided_at",
      "concept_id": "approval_record",
      "name": "decided_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Approval decision time.",
      "evidence_refs": [
        "ddl:pc_approval_record.decided_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "contract.contract_id",
      "concept_id": "contract",
      "name": "contract_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Contract primary key.",
      "evidence_refs": [
        "ddl:pc_contract.contract_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.contract_no",
      "concept_id": "contract",
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
      "id": "contract.request_id",
      "concept_id": "contract",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced approved purchase request.",
      "evidence_refs": [
        "ddl:pc_contract.request_id",
        "doc:contract_lifecycle"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.supplier_id",
      "concept_id": "contract",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced supplier.",
      "evidence_refs": [
        "ddl:pc_contract.supplier_id",
        "doc:contract_lifecycle"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.contract_title",
      "concept_id": "contract",
      "name": "contract_title",
      "type": "attribute",
      "data_type": "VARCHAR(180)",
      "required": true,
      "description": "Contract title.",
      "evidence_refs": [
        "ddl:pc_contract.contract_title"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.contract_amount",
      "concept_id": "contract",
      "name": "contract_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Contract amount; must be non-negative.",
      "evidence_refs": [
        "ddl:pc_contract.contract_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.contract_status",
      "concept_id": "contract",
      "name": "contract_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Contract lifecycle status.",
      "allowed_values": [
        "DRAFT",
        "LEGAL_REVIEW",
        "ACTIVE",
        "EXPIRED",
        "TERMINATED"
      ],
      "evidence_refs": [
        "ddl:pc_contract.contract_status",
        "code:ProcurementStatus"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.start_date",
      "concept_id": "contract",
      "name": "start_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "description": "Contract start date; required by code for activation.",
      "evidence_refs": [
        "ddl:pc_contract.start_date",
        "code:ContractService"
      ],
      "confidence": 0.97
    },
    {
      "id": "contract.end_date",
      "concept_id": "contract",
      "name": "end_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": false,
      "description": "Contract end date; required by code for activation.",
      "evidence_refs": [
        "ddl:pc_contract.end_date",
        "code:ContractService"
      ],
      "confidence": 0.97
    },
    {
      "id": "contract.legal_reviewer_id",
      "concept_id": "contract",
      "name": "legal_reviewer_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Legal reviewer user key.",
      "evidence_refs": [
        "ddl:pc_contract.legal_reviewer_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "contract.legal_approved_at",
      "concept_id": "contract",
      "name": "legal_approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Legal approval timestamp required before activation.",
      "evidence_refs": [
        "ddl:pc_contract.legal_approved_at",
        "code:ContractService"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.activated_at",
      "concept_id": "contract",
      "name": "activated_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Activation timestamp.",
      "evidence_refs": [
        "ddl:pc_contract.activated_at"
      ],
      "confidence": 0.99
    },
    {
      "id": "contract.termination_reason",
      "concept_id": "contract",
      "name": "termination_reason",
      "type": "attribute",
      "data_type": "VARCHAR(300)",
      "required": false,
      "description": "Reason required when contract is terminated.",
      "evidence_refs": [
        "ddl:pc_contract.termination_reason",
        "code:ContractService"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.po_id",
      "concept_id": "purchase_order",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Purchase order primary key.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.po_no",
      "concept_id": "purchase_order",
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
      "id": "purchase_order.contract_id",
      "concept_id": "purchase_order",
      "name": "contract_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced contract.",
      "evidence_refs": [
        "ddl:pc_purchase_order.contract_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.request_id",
      "concept_id": "purchase_order",
      "name": "request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced purchase request.",
      "evidence_refs": [
        "ddl:pc_purchase_order.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.supplier_id",
      "concept_id": "purchase_order",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced supplier.",
      "evidence_refs": [
        "ddl:pc_purchase_order.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.po_amount",
      "concept_id": "purchase_order",
      "name": "po_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Purchase order amount.",
      "evidence_refs": [
        "ddl:pc_purchase_order.po_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.po_status",
      "concept_id": "purchase_order",
      "name": "po_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Purchase order status.",
      "allowed_values": [
        "RELEASED",
        "PARTIALLY_RECEIVED",
        "CLOSED",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_purchase_order.po_status",
        "code:ProcurementStatus"
      ],
      "confidence": 0.99
    },
    {
      "id": "purchase_order.released_at",
      "concept_id": "purchase_order",
      "name": "released_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Release timestamp.",
      "evidence_refs": [
        "ddl:pc_purchase_order.released_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "purchase_order.closed_at",
      "concept_id": "purchase_order",
      "name": "closed_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Closure timestamp.",
      "evidence_refs": [
        "ddl:pc_purchase_order.closed_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "goods_receipt.receipt_id",
      "concept_id": "goods_receipt",
      "name": "receipt_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Goods receipt primary key.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt.receipt_no",
      "concept_id": "goods_receipt",
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
      "id": "goods_receipt.po_id",
      "concept_id": "goods_receipt",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced purchase order.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.po_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt.receipt_status",
      "concept_id": "goods_receipt",
      "name": "receipt_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Goods receipt status.",
      "allowed_values": [
        "PENDING",
        "PARTIAL",
        "COMPLETE",
        "REJECTED"
      ],
      "evidence_refs": [
        "ddl:pc_goods_receipt.receipt_status",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt.received_by",
      "concept_id": "goods_receipt",
      "name": "received_by",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Receiver user key.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt.received_at",
      "concept_id": "goods_receipt",
      "name": "received_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Received timestamp, required by code when recording receipt.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_at",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.99
    },
    {
      "id": "goods_receipt.inspection_result",
      "concept_id": "goods_receipt",
      "name": "inspection_result",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": false,
      "description": "Inspection result.",
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
      "id": "goods_receipt.remarks",
      "concept_id": "goods_receipt",
      "name": "remarks",
      "type": "attribute",
      "data_type": "VARCHAR(500)",
      "required": false,
      "description": "Receipt remarks.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.remarks"
      ],
      "confidence": 0.98
    },
    {
      "id": "invoice.invoice_id",
      "concept_id": "invoice",
      "name": "invoice_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Invoice primary key.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.invoice_no",
      "concept_id": "invoice",
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
      "id": "invoice.supplier_id",
      "concept_id": "invoice",
      "name": "supplier_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Invoice supplier.",
      "evidence_refs": [
        "ddl:pc_invoice.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.po_id",
      "concept_id": "invoice",
      "name": "po_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced purchase order.",
      "evidence_refs": [
        "ddl:pc_invoice.po_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.receipt_id",
      "concept_id": "invoice",
      "name": "receipt_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Referenced goods receipt for goods invoice matching.",
      "evidence_refs": [
        "ddl:pc_invoice.receipt_id",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.97
    },
    {
      "id": "invoice.invoice_amount",
      "concept_id": "invoice",
      "name": "invoice_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Invoice amount; must be non-negative.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.invoice_date",
      "concept_id": "invoice",
      "name": "invoice_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "description": "Invoice date.",
      "evidence_refs": [
        "ddl:pc_invoice.invoice_date"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.invoice_status",
      "concept_id": "invoice",
      "name": "invoice_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Invoice matching status.",
      "allowed_values": [
        "PENDING_MATCH",
        "MATCHED",
        "EXCEPTION",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_invoice.invoice_status",
        "code:ProcurementStatus"
      ],
      "confidence": 0.99
    },
    {
      "id": "invoice.match_variance_amount",
      "concept_id": "invoice",
      "name": "match_variance_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": false,
      "description": "Recorded amount variance from matching.",
      "evidence_refs": [
        "ddl:pc_invoice.match_variance_amount",
        "csv:pc_invoice"
      ],
      "confidence": 0.98
    },
    {
      "id": "invoice.matched_at",
      "concept_id": "invoice",
      "name": "matched_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Invoice matched timestamp.",
      "evidence_refs": [
        "ddl:pc_invoice.matched_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "payment_request.payment_request_id",
      "concept_id": "payment_request",
      "name": "payment_request_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Payment request primary key.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.payment_no",
      "concept_id": "payment_request",
      "name": "payment_no",
      "type": "attribute",
      "data_type": "VARCHAR(40)",
      "required": true,
      "description": "Unique payment request number.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_no"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.invoice_id",
      "concept_id": "payment_request",
      "name": "invoice_id",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": true,
      "description": "Referenced invoice.",
      "evidence_refs": [
        "ddl:pc_payment_request.invoice_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.payment_amount",
      "concept_id": "payment_request",
      "name": "payment_amount",
      "type": "attribute",
      "data_type": "NUMERIC(14,2)",
      "required": true,
      "description": "Payment amount; must be non-negative.",
      "evidence_refs": [
        "ddl:pc_payment_request.payment_amount"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.payment_status",
      "concept_id": "payment_request",
      "name": "payment_status",
      "type": "attribute",
      "data_type": "VARCHAR(30)",
      "required": true,
      "description": "Payment request status.",
      "allowed_values": [
        "REQUESTED",
        "APPROVED",
        "PAID",
        "HELD",
        "CANCELLED"
      ],
      "evidence_refs": [
        "ddl:pc_payment_request.payment_status",
        "code:ProcurementStatus"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.due_date",
      "concept_id": "payment_request",
      "name": "due_date",
      "type": "attribute",
      "data_type": "DATE",
      "required": true,
      "description": "Payment due date.",
      "evidence_refs": [
        "ddl:pc_payment_request.due_date"
      ],
      "confidence": 0.99
    },
    {
      "id": "payment_request.approved_by",
      "concept_id": "payment_request",
      "name": "approved_by",
      "type": "attribute",
      "data_type": "BIGINT",
      "required": false,
      "description": "Approver user key.",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by"
      ],
      "confidence": 0.98
    },
    {
      "id": "payment_request.approved_at",
      "concept_id": "payment_request",
      "name": "approved_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Payment approval timestamp.",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_at"
      ],
      "confidence": 0.98
    },
    {
      "id": "payment_request.paid_at",
      "concept_id": "payment_request",
      "name": "paid_at",
      "type": "attribute",
      "data_type": "TIMESTAMP",
      "required": false,
      "description": "Paid timestamp required for paid payment applications.",
      "evidence_refs": [
        "ddl:pc_payment_request.paid_at",
        "doc:business_rules"
      ],
      "confidence": 0.99
    }
  ],
  "relations": [
    {
      "id": "rel_user_belongs_to_department",
      "source_concept_id": "user",
      "target_concept_id": "department",
      "type": "relation",
      "predicate": "belongs_to",
      "cardinality": "many_to_one",
      "description": "Each user belongs to one department.",
      "evidence_refs": [
        "ddl:pc_user.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_request_has_lines",
      "source_concept_id": "purchase_request",
      "target_concept_id": "purchase_request_line",
      "type": "relation",
      "predicate": "has_lines",
      "cardinality": "one_to_many",
      "description": "A purchase request has one or more line items before submission.",
      "evidence_refs": [
        "ddl:pc_purchase_request_line.request_id",
        "doc:business_rules",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_request_requested_by_user",
      "source_concept_id": "purchase_request",
      "target_concept_id": "user",
      "type": "relation",
      "predicate": "requested_by",
      "cardinality": "many_to_one",
      "description": "A purchase request is requested by a user.",
      "evidence_refs": [
        "ddl:pc_purchase_request.requester_user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_request_belongs_to_department",
      "source_concept_id": "purchase_request",
      "target_concept_id": "department",
      "type": "relation",
      "predicate": "belongs_to",
      "cardinality": "many_to_one",
      "description": "A purchase request belongs to a department.",
      "evidence_refs": [
        "ddl:pc_purchase_request.department_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_request_prefers_supplier",
      "source_concept_id": "purchase_request",
      "target_concept_id": "supplier",
      "type": "relation",
      "predicate": "prefers",
      "cardinality": "many_to_one",
      "description": "A purchase request may name a preferred supplier.",
      "evidence_refs": [
        "ddl:pc_purchase_request.preferred_supplier_id",
        "doc:procurement_process"
      ],
      "confidence": 0.97
    },
    {
      "id": "rel_purchase_request_approved_by_approval_record",
      "source_concept_id": "purchase_request",
      "target_concept_id": "approval_record",
      "type": "relation",
      "predicate": "approved_by",
      "cardinality": "one_to_many",
      "description": "Purchase request approval is represented by approval records where target_type is PURCHASE_REQUEST and target_id is request_id.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id",
        "csv:pc_approval_record"
      ],
      "confidence": 0.8
    },
    {
      "id": "rel_approval_record_approved_by_user",
      "source_concept_id": "approval_record",
      "target_concept_id": "user",
      "type": "relation",
      "predicate": "approved_by",
      "cardinality": "many_to_one",
      "description": "An approval record references the approver user.",
      "evidence_refs": [
        "ddl:pc_approval_record.approver_user_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_contract_references_purchase_request",
      "source_concept_id": "contract",
      "target_concept_id": "purchase_request",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A contract references one approved purchase request.",
      "evidence_refs": [
        "ddl:pc_contract.request_id",
        "doc:contract_lifecycle"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_contract_references_supplier",
      "source_concept_id": "contract",
      "target_concept_id": "supplier",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A contract references one supplier.",
      "evidence_refs": [
        "ddl:pc_contract.supplier_id",
        "doc:contract_lifecycle"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_contract_reviewed_by_user",
      "source_concept_id": "contract",
      "target_concept_id": "user",
      "type": "relation",
      "predicate": "reviewed_by",
      "cardinality": "many_to_one",
      "description": "A contract may reference a legal reviewer user.",
      "evidence_refs": [
        "ddl:pc_contract.legal_reviewer_id"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel_purchase_order_references_contract",
      "source_concept_id": "purchase_order",
      "target_concept_id": "contract",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A purchase order references a contract.",
      "evidence_refs": [
        "ddl:pc_purchase_order.contract_id",
        "doc:procurement_process"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_order_references_purchase_request",
      "source_concept_id": "purchase_order",
      "target_concept_id": "purchase_request",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A purchase order references a purchase request.",
      "evidence_refs": [
        "ddl:pc_purchase_order.request_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_purchase_order_references_supplier",
      "source_concept_id": "purchase_order",
      "target_concept_id": "supplier",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A purchase order references the supplier.",
      "evidence_refs": [
        "ddl:pc_purchase_order.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_goods_receipt_references_purchase_order",
      "source_concept_id": "goods_receipt",
      "target_concept_id": "purchase_order",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A goods receipt references a purchase order.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.po_id",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_goods_receipt_received_by_user",
      "source_concept_id": "goods_receipt",
      "target_concept_id": "user",
      "type": "relation",
      "predicate": "received_by",
      "cardinality": "many_to_one",
      "description": "A goods receipt is recorded by a warehouse user.",
      "evidence_refs": [
        "ddl:pc_goods_receipt.received_by"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_invoice_references_goods_receipt",
      "source_concept_id": "invoice",
      "target_concept_id": "goods_receipt",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A matched goods invoice should reference a goods receipt.",
      "evidence_refs": [
        "ddl:pc_invoice.receipt_id",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.96
    },
    {
      "id": "rel_invoice_references_supplier",
      "source_concept_id": "invoice",
      "target_concept_id": "supplier",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "An invoice references a supplier.",
      "evidence_refs": [
        "ddl:pc_invoice.supplier_id"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_invoice_references_purchase_order",
      "source_concept_id": "invoice",
      "target_concept_id": "purchase_order",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "An invoice references a purchase order.",
      "evidence_refs": [
        "ddl:pc_invoice.po_id",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_payment_request_references_invoice",
      "source_concept_id": "payment_request",
      "target_concept_id": "invoice",
      "type": "relation",
      "predicate": "references",
      "cardinality": "many_to_one",
      "description": "A payment request references one invoice.",
      "evidence_refs": [
        "ddl:pc_payment_request.invoice_id",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.99
    },
    {
      "id": "rel_payment_request_approved_by_user",
      "source_concept_id": "payment_request",
      "target_concept_id": "user",
      "type": "relation",
      "predicate": "approved_by",
      "cardinality": "many_to_one",
      "description": "A payment request may reference the approving user.",
      "evidence_refs": [
        "ddl:pc_payment_request.approved_by"
      ],
      "confidence": 0.98
    },
    {
      "id": "rel_approval_record_polymorphic_target",
      "source_concept_id": "approval_record",
      "target_concept_id": "purchase_request",
      "type": "relation",
      "predicate": "polymorphic_targets",
      "cardinality": "many_to_many",
      "description": "Approval records target purchase requests, contracts, or payment requests via target_type and target_id rather than explicit foreign keys.",
      "evidence_refs": [
        "ddl:pc_approval_record.target_type",
        "ddl:pc_approval_record.target_id",
        "csv:pc_approval_record"
      ],
      "confidence": 0.65
    }
  ],
  "events": [],
  "rules": [
    {
      "id": "rule_pr_must_have_line_before_submission",
      "name": "Purchase Request Must Have Line Before Submission",
      "type": "rule",
      "condition": "purchase_request is submitted",
      "effect": "purchase_request must contain at least one purchase_request_line",
      "applies_to_ids": [
        "purchase_request",
        "purchase_request_line"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule_pr_requires_business_justification",
      "name": "Business Justification Required",
      "type": "rule",
      "condition": "purchase_request is submitted",
      "effect": "business_justification must be present",
      "applies_to_ids": [
        "purchase_request"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule_pr_finance_approval_doc_threshold",
      "name": "Documented Finance Approval Threshold",
      "type": "rule",
      "condition": "estimated_amount >= 50000 CNY",
      "effect": "finance manager approval is required after department manager approval",
      "applies_to_ids": [
        "purchase_request",
        "approval_record",
        "role_finance_manager"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:procurement_process",
        "ddl:pc_purchase_request.estimated_amount"
      ],
      "confidence": 0.86
    },
    {
      "id": "rule_pr_finance_approval_code_threshold",
      "name": "Code Finance Approval Threshold",
      "type": "rule",
      "condition": "estimated_amount > 50000 CNY",
      "effect": "finance manager is required approver role",
      "applies_to_ids": [
        "purchase_request",
        "approval_record",
        "role_finance_manager"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:ApprovalService"
      ],
      "confidence": 0.86
    },
    {
      "id": "rule_supplier_eligible_for_award",
      "name": "Supplier Eligible For Award",
      "type": "rule",
      "condition": "supplier is selected for award or contract",
      "effect": "supplier_status must be ACTIVE and risk_rating must not be HIGH",
      "applies_to_ids": [
        "supplier",
        "contract"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:procurement_process",
        "code:Supplier",
        "code:ContractService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule_contract_activation_requires_legal_approval",
      "name": "Contract Activation Requires Legal Approval",
      "type": "rule",
      "condition": "contract is activated",
      "effect": "legal_approved_at must be present and contract term must be present",
      "applies_to_ids": [
        "contract"
      ],
      "evidence_refs": [
        "doc:contract_lifecycle",
        "code:ContractService"
      ],
      "confidence": 0.98
    },
    {
      "id": "rule_contract_activation_requires_signature_policy",
      "name": "Contract Activation Requires Signature Policy",
      "type": "rule",
      "condition": "contract is activated",
      "effect": "business policy says both parties must sign before activation",
      "applies_to_ids": [
        "contract"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:contract_lifecycle"
      ],
      "confidence": 0.68
    },
    {
      "id": "rule_po_release_requires_active_contract",
      "name": "Purchase Order Release Requires Active Contract",
      "type": "rule",
      "condition": "purchase_order is released",
      "effect": "referenced contract must be ACTIVE",
      "applies_to_ids": [
        "purchase_order",
        "contract"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:procurement_process",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule_invoice_matching_requires_goods_receipt",
      "name": "Invoice Matching Requires Goods Receipt",
      "type": "rule",
      "condition": "invoice is matched for goods purchase",
      "effect": "invoice must reference purchase order and should reference goods receipt",
      "applies_to_ids": [
        "invoice",
        "purchase_order",
        "goods_receipt"
      ],
      "evidence_refs": [
        "doc:receipt_invoice_payment_policy",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.97
    },
    {
      "id": "rule_invoice_tolerance_document_policy",
      "name": "Documented Invoice Variance Tolerance",
      "type": "rule",
      "condition": "invoice amount is matched to purchase order amount",
      "effect": "variance up to 2% of purchase_order amount is allowed unless finance grants exception",
      "applies_to_ids": [
        "invoice",
        "purchase_order"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.86
    },
    {
      "id": "rule_invoice_tolerance_code_policy",
      "name": "Code Invoice Variance Tolerance",
      "type": "rule",
      "condition": "invoice amount is matched to purchase order amount",
      "effect": "variance up to 1.5% of purchase_order amount is accepted by code",
      "applies_to_ids": [
        "invoice",
        "purchase_order"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.86
    },
    {
      "id": "rule_payment_request_requires_matched_invoice",
      "name": "Payment Request Requires Matched Invoice",
      "type": "rule",
      "condition": "payment_request is created or approved",
      "effect": "related invoice must be MATCHED",
      "applies_to_ids": [
        "payment_request",
        "invoice"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:receipt_invoice_payment_policy",
        "code:PaymentService"
      ],
      "confidence": 0.99
    },
    {
      "id": "rule_paid_payment_must_have_paid_time",
      "name": "Paid Payment Must Have Paid Time",
      "type": "rule",
      "condition": "payment_status is PAID",
      "effect": "paid_at must be stored",
      "applies_to_ids": [
        "payment_request"
      ],
      "evidence_refs": [
        "doc:business_rules",
        "doc:receipt_invoice_payment_policy"
      ],
      "confidence": 0.98
    },
    {
      "id": "rule_held_payment_requires_hold_reason",
      "name": "Held Payment Requires Hold Reason",
      "type": "rule",
      "condition": "payment_status is HELD",
      "effect": "hold reason is required in operational notes, but MVP table stores only status",
      "applies_to_ids": [
        "payment_request"
      ],
      "evidence_refs": [
        "doc:receipt_invoice_payment_policy",
        "ddl:pc_payment_request"
      ],
      "confidence": 0.7
    }
  ],
  "actions": [
    {
      "id": "action_create_purchase_request",
      "name": "Create Purchase Request",
      "type": "action",
      "actor_role_ids": [
        "role_requester",
        "role_department_manager",
        "role_procurement_specialist",
        "role_procurement_admin"
      ],
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [],
      "postconditions": [
        "purchase_request status may be DRAFT"
      ],
      "evidence_refs": [
        "doc:role_permission_matrix",
        "doc:procurement_process"
      ],
      "confidence": 0.98
    },
    {
      "id": "action_submit_purchase_request",
      "name": "Submit Purchase Request",
      "type": "action",
      "actor_role_ids": [
        "role_requester",
        "role_department_manager",
        "role_procurement_specialist",
        "role_procurement_admin"
      ],
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [
        "purchase_request is editable",
        "business_justification is present",
        "at least one line exists"
      ],
      "postconditions": [
        "purchase_request status becomes SUBMITTED"
      ],
      "evidence_refs": [
        "doc:role_permission_matrix",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.99
    },
    {
      "id": "action_approve_normal_purchase_request",
      "name": "Approve Normal Purchase Request",
      "type": "action",
      "actor_role_ids": [
        "role_department_manager",
        "role_procurement_admin"
      ],
      "target_concept_ids": [
        "purchase_request",
        "approva