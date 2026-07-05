{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-code-ontology",
  "title": "Procurement Contract MVP Code Ontology Draft",
  "domain": "procurement_contract",
  "concepts": [
    {
      "id": "purchase_request",
      "name": "Purchase Request",
      "type": "concept",
      "description": "A purchase request business object with requester, department, supplier preference, amount, status, justification, dates, and request lines.",
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
        "purchase_request.approved_at",
        "purchase_request.lines"
      ],
      "state_ids": [
        "pr_draft",
        "pr_submitted",
        "pr_approved",
        "pr_rejected",
        "pr_cancelled"
      ],
      "alias_ids": [
        "alias_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:PurchaseRequestService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line",
      "name": "Purchase Request Line",
      "type": "concept",
      "description": "A line item belonging to a purchase request.",
      "category": "line_item",
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
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier",
      "name": "Supplier",
      "type": "concept",
      "description": "Supplier business object with status, risk rating, contact, and onboarding timestamp.",
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
        "alias_vendor"
      ],
      "evidence_refs": [
        "code:Supplier",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract",
      "name": "Contract",
      "type": "concept",
      "description": "Contract business object linked to supplier and purchase request, with amount, term, legal review, activation, and termination data.",
      "category": "document",
      "attribute_ids": [
        "contract.contract_id",
        "contract.contract_no",
        "contract.supplier_id",
        "contract.request_id",
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
        "contract_draft",
        "contract_legal_review",
        "contract_active",
        "contract_expired",
        "contract_terminated"
      ],
      "evidence_refs": [
        "code:Contract",
        "code:ContractService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order",
      "name": "Purchase Order",
      "type": "concept",
      "description": "Purchase order business object linked to contract, purchase request, and supplier.",
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
        "po_released",
        "po_partially_received",
        "po_closed"
      ],
      "alias_ids": [
        "alias_po"
      ],
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:PurchaseOrderService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt",
      "name": "Goods Receipt",
      "type": "concept",
      "description": "Goods receipt business object linked to a purchase order and containing receipt status, receiver, receipt time, inspection result, and remarks.",
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
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice",
      "name": "Invoice",
      "type": "concept",
      "description": "Invoice business object linked to supplier, purchase order, and goods receipt, with matching status and variance data.",
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
        "invoice_pending_match",
        "invoice_matched",
        "invoice_exception"
      ],
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request",
      "name": "Payment Request",
      "type": "concept",
      "description": "Payment request business object linked to an invoice, with payment amount, status, due date, approval, and paid timestamps.",
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
        "payment_requested",
        "payment_approved",
        "payment_paid",
        "payment_held"
      ],
      "alias_ids": [
        "alias_payment_application"
      ],
      "evidence_refs": [
        "code:PaymentRequest",
        "code:PaymentService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "approval_service",
      "name": "Approval Service",
      "type": "concept",
      "description": "Service object containing purchase request approver role selection, approval permission check, and rejection validation.",
      "category": "service",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "contract_service",
      "name": "Contract Service",
      "type": "concept",
      "description": "Service object containing contract creation, legal review submission, activation, and termination logic.",
      "category": "service",
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.9
    },
    {
      "id": "purchase_order_service",
      "name": "Purchase Order Service",
      "type": "concept",
      "description": "Service object containing purchase order release and close logic.",
      "category": "service",
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.9
    },
    {
      "id": "payment_service",
      "name": "Payment Service",
      "type": "concept",
      "description": "Service object containing payment application creation, payment approval, and paid marking logic.",
      "category": "service",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "receipt_invoice_matching_service",
      "name": "Receipt Invoice Matching Service",
      "type": "concept",
      "description": "Service object containing goods receipt recording and purchase order, receipt, and invoice matching logic.",
      "category": "service",
      "attribute_ids": [
        "receipt_invoice_matching_service.code_match_tolerance_rate"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    }
  ],
  "attributes": [
    {
      "id": "purchase_request.request_id",
      "concept_id": "purchase_request",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.request_no",
      "concept_id": "purchase_request",
      "name": "requestNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.request_title",
      "concept_id": "purchase_request",
      "name": "requestTitle",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.requester_user_id",
      "concept_id": "purchase_request",
      "name": "requesterUserId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.department_id",
      "concept_id": "purchase_request",
      "name": "departmentId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.preferred_supplier_id",
      "concept_id": "purchase_request",
      "name": "preferredSupplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.estimated_amount",
      "concept_id": "purchase_request",
      "name": "estimatedAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.currency_code",
      "concept_id": "purchase_request",
      "name": "currencyCode",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.request_status",
      "concept_id": "purchase_request",
      "name": "requestStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "DRAFT",
        "SUBMITTED",
        "APPROVED",
        "REJECTED",
        "CANCELLED"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.business_justification",
      "concept_id": "purchase_request",
      "name": "businessJustification",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.required_by_date",
      "concept_id": "purchase_request",
      "name": "requiredByDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.submitted_at",
      "concept_id": "purchase_request",
      "name": "submittedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.approved_at",
      "concept_id": "purchase_request",
      "name": "approvedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request.lines",
      "concept_id": "purchase_request",
      "name": "lines",
      "type": "attribute",
      "data_type": "List<PurchaseRequestLine>",
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.line_id",
      "concept_id": "purchase_request_line",
      "name": "lineId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.request_id",
      "concept_id": "purchase_request_line",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.item_description",
      "concept_id": "purchase_request_line",
      "name": "itemDescription",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.category_code",
      "concept_id": "purchase_request_line",
      "name": "categoryCode",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.quantity",
      "concept_id": "purchase_request_line",
      "name": "quantity",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.unit_of_measure",
      "concept_id": "purchase_request_line",
      "name": "unitOfMeasure",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.estimated_unit_price",
      "concept_id": "purchase_request_line",
      "name": "estimatedUnitPrice",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.line_amount",
      "concept_id": "purchase_request_line",
      "name": "lineAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier.supplier_id",
      "concept_id": "supplier",
      "name": "supplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier.supplier_code",
      "concept_id": "supplier",
      "name": "supplierCode",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier.supplier_name",
      "concept_id": "supplier",
      "name": "supplierName",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier.supplier_status",
      "concept_id": "supplier",
      "name": "supplierStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "ACTIVE"
      ],
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.85
    },
    {
      "id": "supplier.risk_rating",
      "concept_id": "supplier",
      "name": "riskRating",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "HIGH"
      ],
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.85
    },
    {
      "id": "supplier.contact_email",
      "concept_id": "supplier",
      "name": "contactEmail",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "supplier.onboarded_at",
      "concept_id": "supplier",
      "name": "onboardedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.contract_id",
      "concept_id": "contract",
      "name": "contractId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.contract_no",
      "concept_id": "contract",
      "name": "contractNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.supplier_id",
      "concept_id": "contract",
      "name": "supplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.request_id",
      "concept_id": "contract",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.contract_title",
      "concept_id": "contract",
      "name": "contractTitle",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.contract_amount",
      "concept_id": "contract",
      "name": "contractAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.contract_status",
      "concept_id": "contract",
      "name": "contractStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "DRAFT",
        "LEGAL_REVIEW",
        "ACTIVE",
        "EXPIRED",
        "TERMINATED"
      ],
      "evidence_refs": [
        "code:Contract",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.start_date",
      "concept_id": "contract",
      "name": "startDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.end_date",
      "concept_id": "contract",
      "name": "endDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.legal_reviewer_id",
      "concept_id": "contract",
      "name": "legalReviewerId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.legal_approved_at",
      "concept_id": "contract",
      "name": "legalApprovedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.activated_at",
      "concept_id": "contract",
      "name": "activatedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.termination_reason",
      "concept_id": "contract",
      "name": "terminationReason",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.po_id",
      "concept_id": "purchase_order",
      "name": "poId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.po_no",
      "concept_id": "purchase_order",
      "name": "poNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.contract_id",
      "concept_id": "purchase_order",
      "name": "contractId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.request_id",
      "concept_id": "purchase_order",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.supplier_id",
      "concept_id": "purchase_order",
      "name": "supplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.po_amount",
      "concept_id": "purchase_order",
      "name": "poAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.po_status",
      "concept_id": "purchase_order",
      "name": "poStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "RELEASED",
        "PARTIALLY_RECEIVED",
        "CLOSED"
      ],
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.released_at",
      "concept_id": "purchase_order",
      "name": "releasedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.closed_at",
      "concept_id": "purchase_order",
      "name": "closedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.receipt_id",
      "concept_id": "goods_receipt",
      "name": "receiptId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.receipt_no",
      "concept_id": "goods_receipt",
      "name": "receiptNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.po_id",
      "concept_id": "goods_receipt",
      "name": "poId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.receipt_status",
      "concept_id": "goods_receipt",
      "name": "receiptStatus",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.received_by",
      "concept_id": "goods_receipt",
      "name": "receivedBy",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.received_at",
      "concept_id": "goods_receipt",
      "name": "receivedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.inspection_result",
      "concept_id": "goods_receipt",
      "name": "inspectionResult",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "goods_receipt.remarks",
      "concept_id": "goods_receipt",
      "name": "remarks",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.invoice_id",
      "concept_id": "invoice",
      "name": "invoiceId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.invoice_no",
      "concept_id": "invoice",
      "name": "invoiceNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.supplier_id",
      "concept_id": "invoice",
      "name": "supplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.po_id",
      "concept_id": "invoice",
      "name": "poId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.receipt_id",
      "concept_id": "invoice",
      "name": "receiptId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.invoice_amount",
      "concept_id": "invoice",
      "name": "invoiceAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.invoice_date",
      "concept_id": "invoice",
      "name": "invoiceDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.invoice_status",
      "concept_id": "invoice",
      "name": "invoiceStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "PENDING_MATCH",
        "MATCHED",
        "EXCEPTION"
      ],
      "evidence_refs": [
        "code:Invoice",
        "code:ProcurementStatus",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.match_variance_amount",
      "concept_id": "invoice",
      "name": "matchVarianceAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.matched_at",
      "concept_id": "invoice",
      "name": "matchedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.payment_request_id",
      "concept_id": "payment_request",
      "name": "paymentRequestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.payment_no",
      "concept_id": "payment_request",
      "name": "paymentNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.invoice_id",
      "concept_id": "payment_request",
      "name": "invoiceId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.payment_amount",
      "concept_id": "payment_request",
      "name": "paymentAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.payment_status",
      "concept_id": "payment_request",
      "name": "paymentStatus",
      "type": "attribute",
      "data_type": "String",
      "allowed_values": [
        "REQUESTED",
        "APPROVED",
        "PAID",
        "HELD"
      ],
      "evidence_refs": [
        "code:PaymentRequest",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.due_date",
      "concept_id": "payment_request",
      "name": "dueDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.approved_by",
      "concept_id": "payment_request",
      "name": "approvedBy",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.approved_at",
      "concept_id": "payment_request",
      "name": "approvedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.paid_at",
      "concept_id": "payment_request",
      "name": "paidAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "receipt_invoice_matching_service.code_match_tolerance_rate",
      "concept_id": "receipt_invoice_matching_service",
      "name": "CODE_MATCH_TOLERANCE_RATE",
      "type": "attribute",
      "data_type": "BigDecimal",
      "allowed_values": [
        "0.015"
      ],
      "description": "Invoice matching tolerance rate constant used to compare invoice amount variance against purchase order amount.",
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    }
  ],
  "relations": [
    {
      "id": "purchase_request.has_lines",
      "type": "relation",
      "source_concept_id": "purchase_request",
      "target_concept_id": "purchase_request_line",
      "predicate": "has_lines",
      "cardinality": "one_to_many",
      "description": "PurchaseRequest has a List<PurchaseRequestLine> lines field.",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_request_line.belongs_to_purchase_request",
      "type": "relation",
      "source_concept_id": "purchase_request_line",
      "target_concept_id": "purchase_request",
      "predicate": "belongs_to",
      "cardinality": "many_to_one",
      "description": "PurchaseRequestLine has requestId.",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.9
    },
    {
      "id": "purchase_request.prefers_supplier",
      "type": "relation",
      "source_concept_id": "purchase_request",
      "target_concept_id": "supplier",
      "predicate": "prefers_supplier",
      "cardinality": "many_to_one",
      "description": "PurchaseRequest has preferredSupplierId.",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.9
    },
    {
      "id": "contract.references_supplier",
      "type": "relation",
      "source_concept_id": "contract",
      "target_concept_id": "supplier",
      "predicate": "references_supplier",
      "cardinality": "many_to_one",
      "description": "Contract has supplierId and ContractService receives Supplier vendor when creating a contract.",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract.created_from_purchase_request",
      "type": "relation",
      "source_concept_id": "contract",
      "target_concept_id": "purchase_request",
      "predicate": "created_from",
      "cardinality": "many_to_one",
      "description": "Contract has requestId and ContractService.createContractFromApprovedPR accepts requestId.",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.9
    },
    {
      "id": "purchase_order.references_contract",
      "type": "relation",
      "source_concept_id": "purchase_order",
      "target_concept_id": "contract",
      "predicate": "references_contract",
      "cardinality": "many_to_one",
      "description": "PurchaseOrder has contractId and PurchaseOrderService releases a purchase order from a Contract.",
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "purchase_order.references_purchase_request",
      "type": "relation",
      "source_concept_id": "purchase_order",
      "target_concept_id": "purchase_request",
      "predicate": "references_purchase_request",
      "cardinality": "many_to_one",
      "description": "PurchaseOrder has requestId.",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.9
    },
    {
      "id": "purchase_order.references_supplier",
      "type": "relation",
      "source_concept_id": "purchase_order",
      "target_concept_id": "supplier",
      "predicate": "references_supplier",
      "cardinality": "many_to_one",
      "description": "PurchaseOrder has supplierId.",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.9
    },
    {
      "id": "goods_receipt.references_purchase_order",
      "type": "relation",
      "source_concept_id": "goods_receipt",
      "target_concept_id": "purchase_order",
      "predicate": "references_purchase_order",
      "cardinality": "many_to_one",
      "description": "GoodsReceipt has poId and recordGoodsReceipt receives PurchaseOrder and GoodsReceipt.",
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.references_supplier",
      "type": "relation",
      "source_concept_id": "invoice",
      "target_concept_id": "supplier",
      "predicate": "references_supplier",
      "cardinality": "many_to_one",
      "description": "Invoice has supplierId.",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.9
    },
    {
      "id": "invoice.references_purchase_order",
      "type": "relation",
      "source_concept_id": "invoice",
      "target_concept_id": "purchase_order",
      "predicate": "references_purchase_order",
      "cardinality": "many_to_one",
      "description": "Invoice has poId and matchInvoice receives PurchaseOrder.",
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice.references_goods_receipt",
      "type": "relation",
      "source_concept_id": "invoice",
      "target_concept_id": "goods_receipt",
      "predicate": "references_goods_receipt",
      "cardinality": "many_to_one",
      "description": "Invoice has receiptId and matchInvoice requires a non-null GoodsReceipt.",
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_request.references_invoice",
      "type": "relation",
      "source_concept_id": "payment_request",
      "target_concept_id": "invoice",
      "predicate": "references_invoice",
      "cardinality": "many_to_one",
      "description": "PaymentRequest has invoiceId and PaymentService.createPaymentApplication receives Invoice.",
      "evidence_refs": [
        "code:PaymentRequest",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "receipt_invoice_matching_service.matches_invoice_to_order_and_receipt",
      "type": "relation",
      "source_concept_id": "receipt_invoice_matching_service",
      "target_concept_id": "invoice",
      "predicate": "matches",
      "cardinality": "unknown",
      "description": "ReceiptInvoiceMatchingService.matchInvoice receives PurchaseOrder, GoodsReceipt, and Invoice and compares invoice amount to PO amount within tolerance.",
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    }
  ],
  "events": [
    {
      "id": "event_pr_draft_created",
      "type": "event",
      "name": "Purchase Request Draft Created",
      "trigger": "PurchaseRequestService.createDraftPR",
      "participant_concept_ids": [
        "purchase_request"
      ],
      "resulting_state_ids": [
        "pr_draft"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_pr_submitted",
      "type": "event",
      "name": "Purchase Request Submitted",
      "trigger": "PurchaseRequestService.submitPR",
      "participant_concept_ids": [
        "purchase_request"
      ],
      "resulting_state_ids": [
        "pr_submitted"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.85
    },
    {
      "id": "event_pr_cancelled",
      "type": "event",
      "name": "Purchase Request Cancelled",
      "trigger": "PurchaseRequestService.cancelPR",
      "participant_concept_ids": [
        "purchase_request"
      ],
      "resulting_state_ids": [
        "pr_cancelled"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.85
    },
    {
      "id": "event_pr_approved",
      "type": "event",
      "name": "Purchase Request Approved",
      "trigger": "ApprovalService.approveRequest",
      "participant_concept_ids": [
        "purchase_request"
      ],
      "resulting_state_ids": [
        "pr_approved"
      ],
      "evidence_refs": [
        "code:ApprovalService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_pr_rejected",
      "type": "event",
      "name": "Purchase Request Rejected",
      "trigger": "ApprovalService.rejectRequest",
      "participant_concept_ids": [
        "purchase_request"
      ],
      "resulting_state_ids": [
        "pr_rejected"
      ],
      "evidence_refs": [
        "code:ApprovalService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_contract_created",
      "type": "event",
      "name": "Contract Created From Approved PR",
      "trigger": "ContractService.createContractFromApprovedPR",
      "participant_concept_ids": [
        "contract",
        "purchase_request",
        "supplier"
      ],
      "resulting_state_ids": [
        "contract_draft"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:Contract",
        "code:Supplier"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_contract_legal_review_submitted",
      "type": "event",
      "name": "Contract Legal Review Submitted",
      "trigger": "ContractService.submitLegalReview",
      "participant_concept_ids": [
        "contract"
      ],
      "resulting_state_ids": [
        "contract_legal_review"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.75
    },
    {
      "id": "event_contract_activated",
      "type": "event",
      "name": "Contract Activated",
      "trigger": "ContractService.activateContract",
      "participant_concept_ids": [
        "contract"
      ],
      "resulting_state_ids": [
        "contract_active"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.75
    },
    {
      "id": "event_contract_terminated",
      "type": "event",
      "name": "Contract Terminated",
      "trigger": "ContractService.terminateContract",
      "participant_concept_ids": [
        "contract"
      ],
      "resulting_state_ids": [
        "contract_terminated"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_po_released",
      "type": "event",
      "name": "Purchase Order Released",
      "trigger": "PurchaseOrderService.releasePurchaseOrder",
      "participant_concept_ids": [
        "purchase_order",
        "contract"
      ],
      "resulting_state_ids": [
        "po_released"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.75
    },
    {
      "id": "event_po_closed",
      "type": "event",
      "name": "Purchase Order Closed",
      "trigger": "PurchaseOrderService.closePurchaseOrder",
      "participant_concept_ids": [
        "purchase_order"
      ],
      "resulting_state_ids": [
        "po_closed"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.75
    },
    {
      "id": "event_goods_receipt_recorded",
      "type": "event",
      "name": "Goods Receipt Recorded",
      "trigger": "ReceiptInvoiceMatchingService.recordGoodsReceipt",
      "participant_concept_ids": [
        "purchase_order",
        "goods_receipt"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService",
        "code:GoodsReceipt"
      ],
      "confidence": 0.7
    },
    {
      "id": "event_invoice_matched",
      "type": "event",
      "name": "Invoice Matched",
      "trigger": "ReceiptInvoiceMatchingService.matchInvoice",
      "participant_concept_ids": [
        "purchase_order",
        "goods_receipt",
        "invoice"
      ],
      "resulting_state_ids": [
        "invoice_matched"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_payment_application_created",
      "type": "event",
      "name": "Payment Application Created",
      "trigger": "PaymentService.createPaymentApplication",
      "participant_concept_ids": [
        "payment_request",
        "invoice"
      ],
      "resulting_state_ids": [
        "payment_requested"
      ],
      "evidence_refs": [
        "code:PaymentService",
        "code:PaymentRequest",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_payment_approved",
      "type": "event",
      "name": "Payment Approved",
      "trigger": "PaymentService.approvePayment",
      "participant_concept_ids": [
        "payment_request"
      ],
      "resulting_state_ids": [
        "payment_approved"
      ],
      "evidence_refs": [
        "code:PaymentService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "event_payment_paid",
      "type": "event",
      "name": "Payment Paid",
      "trigger": "PaymentService.markPaid",
      "participant_concept_ids": [
        "payment_request"
      ],
      "resulting_state_ids": [
        "payment_paid"
      ],
      "evidence_refs": [
        "code:PaymentService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    }
  ],
  "rules": [
    {
      "id": "rule_pr_editable_status",
      "type": "rule",
      "name": "Purchase Request Editable Status",
      "condition": "requestStatus equals DRAFT or REJECTED",
      "effect": "PurchaseRequest.isEditable returns true; submitPR allows submission only when isEditable is true.",
      "applies_to_ids": [
        "purchase_request",
        "action_submit_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_finance_review_threshold",
      "type": "rule",
      "name": "Finance Review Threshold",
      "condition": "PurchaseRequest.estimatedAmount is greater than 50000",
      "effect": "ApprovalService.requiredApproverRole returns FINANCE_MANAGER; otherwise it returns DEPARTMENT_MANAGER.",
      "applies_to_ids": [
        "purchase_request",
        "role_finance_manager",
        "role_department_manager"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:ApprovalService",
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_pr_submit_requires_line",
      "type": "rule",
      "name": "Purchase Request Submission Requires Lines",
      "condition": "request.getLines is null or empty",
      "effect": "submitPR throws IllegalArgumentException.",
      "applies_to_ids": [
        "purchase_request",
        "purchase_request_line",
        "action_submit_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_pr_submit_requires_business_justification",
      "type": "rule",
      "name": "Purchase Request Submission Requires Business Justification",
      "condition": "businessJustification is null or blank",
      "effect": "submitPR throws IllegalArgumentException.",
      "applies_to_ids": [
        "purchase_request",
        "action_submit_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_approved_pr_cancel_requires_admin_review",
      "type": "rule",
      "name": "Approved Purchase Request Cancellation Requires Admin Review",
      "condition": "requestStatus equals APPROVED",
      "effect": "cancelPR throws IllegalStateException stating approved PR cannot be cancelled without procurement admin review.",
      "applies_to_ids": [
        "purchase_request",
        "role_procurement_admin",
        "action_cancel_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.85
    },
    {
      "id": "rule_pr_cancel_requires_reason",
      "type": "rule",
      "name": "Purchase Request Cancellation Requires Reason",
      "condition": "reason is null or blank",
      "effect": "cancelPR throws IllegalArgumentException.",
      "applies_to_ids": [
        "purchase_request",
        "action_cancel_pr"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_pr_approver_must_match_required_role_or_admin",
      "type": "rule",
      "name": "Purchase Request Approver Must Match Required Role Or Admin",
      "condition": "approverRole is neither requiredApproverRole(request) nor PROCUREMENT_ADMIN",
      "effect": "approveRequest throws IllegalStateException.",
      "applies_to_ids": [
        "purchase_request",
        "role_finance_manager",
        "role_department_manager",
        "role_procurement_admin",
        "action_approve_request"
      ],
      "evidence_refs": [
        "code:ApprovalService",
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_rejection_comment_minimum_length",
      "type": "rule",
      "name": "Rejection Comment Minimum Length",
      "condition": "comment is null or comment length is less than 10",
      "effect": "rejectRequest throws IllegalArgumentException.",
      "applies_to_ids": [
        "purchase_request",
        "action_reject_request"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_supplier_eligible_for_award",
      "type": "rule",
      "name": "Supplier Eligible For Award",
      "condition": "supplierStatus equals ACTIVE and riskRating does not equal HIGH",
      "effect": "Supplier.isEligibleForAward returns true.",
      "applies_to_ids": [
        "supplier"
      ],
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_contract_creation_requires_eligible_vendor",
      "type": "rule",
      "name": "Contract Creation Requires Eligible Vendor",
      "condition": "vendor is null or vendor.isEligibleForAward is false",
      "effect": "createContractFromApprovedPR throws IllegalArgumentException.",
      "applies_to_ids": [
        "contract",
        "supplier",
        "action_create_contract_from_approved_pr"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_only_draft_contract_enters_legal_review",
      "type": "rule",
      "name": "Only Draft Contract Enters Legal Review",
      "condition": "contractStatus is not DRAFT",
      "effect": "submitLegalReview throws IllegalStateException.",
      "applies_to_ids": [
        "contract",
        "action_submit_legal_review"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_contract_activation_requires_legal_approval",
      "type": "rule",
      "name": "Contract Activation Requires Legal Approval",
      "condition": "legalApprovedAt is null",
      "effect": "activateContract throws IllegalStateException.",
      "applies_to_ids": [
        "contract",
        "action_activate_contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_contract_activation_requires_term",
      "type": "rule",
      "name": "Contract Activation Requires Term",
      "condition": "startDate is null or endDate is null",
      "effect": "activateContract throws IllegalArgumentException.",
      "applies_to_ids": [
        "contract",
        "action_activate_contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_contract_termination_requires_reason",
      "type": "rule",
      "name": "Contract Termination Requires Reason",
      "condition": "reason is null or blank",
      "effect": "terminateContract throws IllegalArgumentException.",
      "applies_to_ids": [
        "contract",
        "action_terminate_contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_po_release_requires_active_contract",
      "type": "rule",
      "name": "Purchase Order Release Requires Active Contract",
      "condition": "contractStatus is not ACTIVE",
      "effect": "releasePurchaseOrder throws IllegalStateException.",
      "applies_to_ids": [
        "purchase_order",
        "contract",
        "action_release_purchase_order"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_po_close_allowed_statuses",
      "type": "rule",
      "name": "Purchase Order Close Allowed Statuses",
      "condition": "poStatus is neither PARTIALLY_RECEIVED nor RELEASED",
      "effect": "closePurchaseOrder throws IllegalStateException.",
      "applies_to_ids": [
        "purchase_order",
        "action_close_purchase_order"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_goods_receipt_requires_time",
      "type": "rule",
      "name": "Goods Receipt Requires Receipt Time",
      "condition": "receivedAt is null",
      "effect": "recordGoodsReceipt throws IllegalArgumentException.",
      "applies_to_ids": [
        "goods_receipt",
        "action_record_goods_receipt"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_invoice_match_requires_goods_receipt",
      "type": "rule",
      "name": "Invoice Match Requires Goods Receipt",
      "condition": "receipt is null",
      "effect": "matchInvoice throws IllegalStateException.",
      "applies_to_ids": [
        "invoice",
        "goods_receipt",
        "action_match_invoice"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_invoice_match_tolerance",
      "type": "rule",
      "name": "Invoice Match Tolerance",
      "condition": "absolute invoiceAmount minus poAmount is less than or equal to poAmount multiplied by CODE_MATCH_TOLERANCE_RATE and rounded to scale 2 HALF_UP",
      "effect": "matchInvoice returns true.",
      "applies_to_ids": [
        "invoice",
        "purchase_order",
        "receipt_invoice_matching_service.code_match_tolerance_rate",
        "action_match_invoice"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_payment_application_requires_matched_invoice",
      "type": "rule",
      "name": "Payment Application Requires Matched Invoice",
      "condition": "invoiceStatus is not MATCHED",
      "effect": "createPaymentApplication throws IllegalStateException.",
      "applies_to_ids": [
        "invoice",
        "payment_request",
        "action_create_payment_application"
      ],
      "evidence_refs": [
        "code:PaymentService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_payment_approval_role",
      "type": "rule",
      "name": "Payment Approval Role",
      "condition": "roleCode is neither FINANCE_MANAGER nor PROCUREMENT_ADMIN",
      "effect": "approvePayment throws IllegalStateException.",
      "applies_to_ids": [
        "payment_request",
        "role_finance_manager",
        "role_procurement_admin",
        "action_approve_payment"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule_mark_paid_requires_approved_payment",
      "type": "rule",
      "name": "Mark Paid Requires Approved Payment",
      "condition": "paymentStatus is not APPROVED",
      "effect": "markPaid throws IllegalStateException.",
      "applies_to_ids": [
        "payment_request",
        "action_mark_paid"
      ],
      "evidence_refs": [
        "code:PaymentService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    }
  ],
  "actions": [
    {
      "id": "action_create_draft_pr",
      "type": "action",
      "name": "createDraftPR",
      "target_concept_ids": [
        "purchase_request"
      ],
      "postconditions": [
        "Calls requestStatusGuard(request, null)."
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.8
    },
    {
      "id": "action_submit_pr",
      "type": "action",
      "name": "submitPR",
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [
        "Purchase request is editable.",
        "Purchase request has at least one line.",
        "Business justification is not blank."
      ],
      "postconditions": [
        "Calls requestStatusGuard(request, PR_SUBMITTED)."
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_cancel_pr",
      "type": "action",
      "name": "cancelPR",
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [
        "Reason is not blank.",
        "Approved purchase request cannot be cancelled by this method without procurement admin review."
      ],
      "postconditions": [
        "Calls requestStatusGuard(request, PR_CANCELLED)."
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_approve_request",
      "type": "action",
      "name": "approveRequest",
      "actor_role_ids": [
        "role_finance_manager",
        "role_department_manager",
        "role_procurement_admin"
      ],
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [
        "Approver role equals requiredApproverRole(request) or PROCUREMENT_ADMIN."
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_reject_request",
      "type": "action",
      "name": "rejectRequest",
      "target_concept_ids": [
        "purchase_request"
      ],
      "preconditions": [
        "Rejection comment length is at least 10."
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.85
    },
    {
      "id": "action_create_contract_from_approved_pr",
      "type": "action",
      "name": "createContractFromApprovedPR",
      "target_concept_ids": [
        "contract",
        "purchase_request",
        "supplier"
      ],
      "preconditions": [
        "Supplier vendor is not null.",
        "Supplier vendor is eligible for award."
      ],
      "postconditions": [
        "Returns new Contract."
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.85
    },
    {
      "id": "action_submit_legal_review",
      "type": "action",
      "name": "submitLegalReview",
      "target_concept_ids": [
        "contract"
      ],
      "preconditions": [
        "Contract status is DRAFT."
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_activate_contract",
      "type": "action",
      "name": "activateContract",
      "target_concept_ids": [
        "contract"
      ],
      "preconditions": [
        "legalApprovedAt is not null.",
        "startDate and endDate are not null."
      ],
      "postconditions": [
        "Sets activatedAt to OffsetDateTime.now()."
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_terminate_contract",
      "type": "action",
      "name": "terminateContract",
      "target_concept_ids": [
        "contract"
      ],
      "preconditions": [
        "Termination reason is not blank."
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.85
    },
    {
      "id": "action_release_purchase_order",
      "type": "action",
      "name": "releasePurchaseOrder",
      "target_concept_ids": [
        "purchase_order",
        "contract"
      ],
      "preconditions": [
        "Contract status is ACTIVE."
      ],
      "postconditions": [
        "Returns new PurchaseOrder."
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_close_purchase_order",
      "type": "action",
      "name": "closePurchaseOrder",
      "target_concept_ids": [
        "purchase_order"
      ],
      "preconditions": [
        "Purchase order status is RELEASED or PARTIALLY_RECEIVED."
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_record_goods_receipt",
      "type": "action",
      "name": "recordGoodsReceipt",
      "target_concept_ids": [
        "purchase_order",
        "goods_receipt"
      ],
      "preconditions": [
        "Goods receipt receivedAt is not null."
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_match_invoice",
      "type": "action",
      "name": "matchInvoice",
      "target_concept_ids": [
        "purchase_order",
        "goods_receipt",
        "invoice"
      ],
      "preconditions": [
        "Goods receipt is not null."
      ],
      "postconditions": [
        "Returns true when invoice amount variance is within tolerance."
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_create_payment_application",
      "type": "action",
      "name": "createPaymentApplication",
      "target_concept_ids": [
        "payment_request",
        "invoice"
      ],
      "preconditions": [
        "Invoice status is MATCHED."
      ],
      "postconditions": [
        "Returns new PaymentRequest."
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.85
    },
    {
      "id": "action_approve_payment",
      "type": "action",
      "name": "approvePayment",
      "actor_role_ids": [
        "role_finance_manager",
        "role_procurement_admin"
      ],
      "target_concept_ids": [
        "payment_request"
      ],
      "preconditions": [
        "roleCode is FINANCE_MANAGER or PROCUREMENT_ADMIN."
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_mark_paid",
      "type": "action",
      "name": "markPaid",
      "target_concept_ids": [
        "payment_request"
      ],
      "preconditions": [
        "Payment status is APPROVED."
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_create_purchase_request",
      "type": "action",
      "name": "PurchaseRequestController.create",
      "target_concept_ids": [
        "purchase_request"
      ],
      "postconditions": [
        "Delegates to PurchaseRequestService.createDraftPR."
      ],
      "evidence_refs": [
        "code:PurchaseRequestController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_submit_purchase_request",
      "type": "action",
      "name": "PurchaseRequestController.submit",
      "target_concept_ids": [
        "purchase_request"
      ],
      "postconditions": [
        "Delegates to PurchaseRequestService.submitPR."
      ],
      "evidence_refs": [
        "code:PurchaseRequestController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_cancel_purchase_request",
      "type": "action",
      "name": "PurchaseRequestController.cancel",
      "target_concept_ids": [
        "purchase_request"
      ],
      "postconditions": [
        "Delegates to PurchaseRequestService.cancelPR."
      ],
      "evidence_refs": [
        "code:PurchaseRequestController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_submit_contract_legal_review",
      "type": "action",
      "name": "ContractController.submitLegalReview",
      "target_concept_ids": [
        "contract"
      ],
      "postconditions": [
        "Delegates to ContractService.submitLegalReview."
      ],
      "evidence_refs": [
        "code:ContractController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_activate_contract",
      "type": "action",
      "name": "ContractController.activate",
      "target_concept_ids": [
        "contract"
      ],
      "postconditions": [
        "Delegates to ContractService.activateContract."
      ],
      "evidence_refs": [
        "code:ContractController"
      ],
      "confidence": 0.9
    },
    {
      "id": "action_api_terminate_contract",
      "type": "action",
      "name": "ContractController.terminate",
      "target_concept_ids": [
        "contract"
      ],
      "postconditions": [
        "Delegates to ContractService.terminateContract."
      ],
      "evidence_refs": [
        "code:ContractController"
      ],
      "confidence": 0.9
    }
  ],
  "states": [
    {
      "id": "pr_draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "purchase_request",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "pr_submitted",
      "type": "state",
      "name": "SUBMITTED",
      "owner_concept_id": "purchase_request",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "pr_approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "purchase_request",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "pr_rejected",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "purchase_request",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "pr_cancelled",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "purchase_request",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract_draft",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "contract",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract_legal_review",
      "type": "state",
      "name": "LEGAL_REVIEW",
      "owner_concept_id": "contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract_active",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "contract",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract_expired",
      "type": "state",
      "name": "EXPIRED",
      "owner_concept_id": "contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "contract_terminated",
      "type": "state",
      "name": "TERMINATED",
      "owner_concept_id": "contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "po_released",
      "type": "state",
      "name": "RELEASED",
      "owner_concept_id": "purchase_order",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "po_partially_received",
      "type": "state",
      "name": "PARTIALLY_RECEIVED",
      "owner_concept_id": "purchase_order",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "po_closed",
      "type": "state",
      "name": "CLOSED",
      "owner_concept_id": "purchase_order",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice_pending_match",
      "type": "state",
      "name": "PENDING_MATCH",
      "owner_concept_id": "invoice",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice_matched",
      "type": "state",
      "name": "MATCHED",
      "owner_concept_id": "invoice",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "invoice_exception",
      "type": "state",
      "name": "EXCEPTION",
      "owner_concept_id": "invoice",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_requested",
      "type": "state",
      "name": "REQUESTED",
      "owner_concept_id": "payment_request",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_approved",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "payment_request",
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_paid",
      "type": "state",
      "name": "PAID",
      "owner_concept_id": "payment_request",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "payment_held",
      "type": "state",
      "name": "HELD",
      "owner_concept_id": "payment_request",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    }
  ],
  "roles": [
    {
      "id": "role_requester",
      "type": "role",
      "name": "REQUESTER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_department_manager",
      "type": "role",
      "name": "DEPT_MANAGER",
      "description": "RoleCode constant name is DEPARTMENT_MANAGER and value is DEPT_MANAGER.",
      "evidence_refs": [
        "code:RoleCode",
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_procurement_specialist",
      "type": "role",
      "name": "PROCUREMENT_SPECIALIST",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_finance_manager",
      "type": "role",
      "name": "FINANCE_MANAGER",
      "evidence_refs": [
        "code:RoleCode",
        "code:ApprovalService",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_legal_reviewer",
      "type": "role",
      "name": "LEGAL_REVIEWER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_warehouse_clerk",
      "type": "role",
      "name": "WAREHOUSE_CLERK",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_ap_clerk",
      "type": "role",
      "name": "AP_CLERK",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role_procurement_admin",
      "type": "role",
      "name": "PROCUREMENT_ADMIN",
      "evidence_refs": [
        "code:RoleCode",
        "code:ApprovalService",
        "code:PaymentService",
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    }
  ],
  "permissions": [
    {
      "id": "permission_department_manager_approve_request_under_threshold",
      "type": "permission",
      "role_id": "role_department_manager",
      "action_id": "action_approve_request",
      "resource_concept_id": "purchase_request",
      "effect": "conditional",
      "condition": "ApprovalService.requiredApproverRole returns DEPARTMENT_MANAGER when estimatedAmount is not greater than 50000.",
      "evidence_refs": [
        "code:ApprovalService",
        "code:RoleCode"
      ],
      "confidence": 0.9
    },
    {
      "id": "permission_finance_manager_approve_request_over_threshold",
      "type": "permission",
      "role_id": "role_finance_manager",
      "action_id": "action_approve_request",
      "resource_concept_id": "purchase_request",
      "effect": "conditional",
      "condition": "ApprovalService.requiredApproverRole returns FINANCE_MANAGER when estimatedAmount is greater than 50000.",
      "evidence_refs": [
        "code:ApprovalService",
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "permission_procurement_admin_approve_request_override",
      "type": "permission",
      "role_id": "role_procurement_admin",
      "action_id": "action_approve_request",
      "resource_concept_id": "purchase_request",
      "effect": "allow",
      "condition": "approveRequest allows PROCUREMENT_ADMIN even when approverRole does not equal requiredApproverRole.",
      "evidence_refs": [
        "code:ApprovalService",
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "permission_finance_manager_approve_payment",
      "type": "permission",
      "role_id": "role_finance_manager",
      "action_id": "action_approve_payment",
      "resource_concept_id": "payment_request",
      "effect": "allow",
      "condition": "roleCode equals FINANCE_MANAGER.",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "permission_procurement_admin_approve_payment",
      "type": "permission",
      "role_id": "role_procurement_admin",
      "action_id": "action_approve_payment",
      "resource_concept_id": "payment_request",
      "effect": "allow",
      "condition": "roleCode equals PROCUREMENT_ADMIN.",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "permission_non_finance_non_admin_approve_payment_denied",
      "type": "permission",
      "role_id": "role_requester",
      "action_id": "action_approve_payment",
      "resource_concept_id": "payment_request",
      "effect": "deny",
      "condition": "PaymentService.approvePayment denies any roleCode other than FINANCE_MANAGER or PROCUREMENT_ADMIN; role_requester is representative of roles not explicitly allowed.",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.6
    }
  ],
  "aliases": [
    {
      "id": "alias_vendor",
      "type": "alias",
      "canonical_id": "supplier",
      "alias": "Vendor",
      "language": "en",
      "source_context": "ContractService.createContractFromApprovedPR uses parameter Supplier vendor and error message says Vendor.",
      "evidence_refs": [
        "code:ContractService",
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias_pr",
      "type": "alias",
      "canonical_id": "purchase_request",
      "alias": "PR",
      "language": "en",
      "source_context": "PurchaseRequestService method names use createDraftPR, submitPR, cancelPR and a comment states PR is the code abbreviation for Purchase Request.",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.98
    },
    {
      "id": "alias_po",
      "type": "alias",
      "canonical_id": "purchase_order",
      "alias": "PO",
      "language": "en",
      "source_context": "PurchaseOrder fields use poId, poNo, poAmount, poStatus; service messages use PO.",
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias_payment_application",
      "type": "alias",
      "canonical_id": "payment_request",
      "alias": "Payment Application",
      "language": "en",
      "source_context": "PaymentService.createPaymentApplication returns PaymentRequest and error message says payment application.",
      "evidence_refs": [
        "code:PaymentService",
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    }
  ],
  "mappings": [
    {
      "id": "mapping_purchase_request_class",
      "type": "mapping",
      "ontology_element_id": "purchase_request",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/PurchaseRequest.java#PurchaseRequest",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_purchase_request_line_class",
      "type": "mapping",
      "ontology_element_id": "purchase_request_line",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/PurchaseRequestLine.java#PurchaseRequestLine",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_supplier_class",
      "type": "mapping",
      "ontology_element_id": "supplier",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/Supplier.java#Supplier",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_contract_class",
      "type": "mapping",
      "ontology_element_id": "contract",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/Contract.java#Contract",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_purchase_order_class",
      "type": "mapping",
      "ontology_element_id": "purchase_order",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/PurchaseOrder.java#PurchaseOrder",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_goods_receipt_class",
      "type": "mapping",
      "ontology_element_id": "goods_receipt",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/GoodsReceipt.java#GoodsReceipt",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_invoice_class",
      "type": "mapping",
      "ontology_element_id": "invoice",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/Invoice.java#Invoice",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_payment_request_class",
      "type": "mapping",
      "ontology_element_id": "payment_request",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/PaymentRequest.java#PaymentRequest",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_procurement_status_constants",
      "type": "mapping",
      "ontology_element_id": "pr_draft",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/common/ProcurementStatus.java#ProcurementStatus",
      "source_type": "code",
      "mapping_type": "exact",
      "transform_note": "ProcurementStatus contains PR, CONTRACT, PO, INVOICE, and PAYMENT status constants; individual state elements map to corresponding constants.",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_role_code_constants",
      "type": "mapping",
      "ontology_element_id": "role_finance_manager",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/common/RoleCode.java#RoleCode",
      "source_type": "code",
      "mapping_type": "exact",
      "transform_note": "RoleCode contains requester, department manager, procurement specialist, finance manager, legal reviewer, warehouse clerk, AP clerk, and procurement admin roles.",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_purchase_request_service",
      "type": "mapping",
      "ontology_element_id": "action_submit_pr",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/PurchaseRequestService.java#submitPR",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_approval_service",
      "type": "mapping",
      "ontology_element_id": "action_approve_request",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/ApprovalService.java#approveRequest",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_contract_service",
      "type": "mapping",
      "ontology_element_id": "action_activate_contract",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/ContractService.java#activateContract",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_purchase_order_service",
      "type": "mapping",
      "ontology_element_id": "action_release_purchase_order",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/PurchaseOrderService.java#releasePurchaseOrder",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_receipt_invoice_matching_service",
      "type": "mapping",
      "ontology_element_id": "action_match_invoice",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/ReceiptInvoiceMatchingService.java#matchInvoice",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_payment_service",
      "type": "mapping",
      "ontology_element_id": "action_create_payment_application",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/PaymentService.java#createPaymentApplication",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_purchase_request_controller",
      "type": "mapping",
      "ontology_element_id": "action_api_submit_purchase_request",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/controller/PurchaseRequestController.java#submit",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestController"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_contract_controller",
      "type": "mapping",
      "ontology_element_id": "action_api_activate_contract",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/controller/ContractController.java#activate",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:ContractController"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_alias_vendor",
      "type": "mapping",
      "ontology_element_id": "alias_vendor",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/ContractService.java#createContractFromApprovedPR parameter vendor",
      "source_type": "code",
      "mapping_type": "derived",
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_alias_pr",
      "type": "mapping",
      "ontology_element_id": "alias_pr",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/PurchaseRequestService.java#createDraftPR comment",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.98
    },
    {
      "id": "mapping_alias_po",
      "type": "mapping",
      "ontology_element_id": "alias_po",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/domain/PurchaseOrder.java#poId",
      "source_type": "code",
      "mapping_type": "derived",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "mapping_alias_payment_application",
      "type": "mapping",
      "ontology_element_id": "alias_payment_application",
      "source_element": "datasets/generic_procurement_contract_mvp/source_code/src/main/java/com/example/procurement/service/PaymentService.java#createPaymentApplication",
      "source_type": "code",
      "mapping_type": "derived",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    }
  ],
  "conflicts": [
    {
      "id": "conflict_supplier_vendor_naming",
      "type": "conflict",
      "description": "Supplier is the domain class name, but ContractService.createContractFromApprovedPR names its Supplier parameter vendor and the validation message says Vendor.",
      "involved_ids": [
        "supplier",
        "alias_vendor"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "resolution_note": "Treat Vendor as an alias for Supplier because both refer to the same Supplier-typed object.",
      "evidence_refs": [
        "code:Supplier",
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "conflict_payment_request_payment_application_naming",
      "type": "conflict",
      "description": "PaymentRequest is the domain class name, while PaymentService exposes createPaymentApplication and uses the phrase payment application in an exception message.",
      "involved_ids": [
        "payment_request",
        "alias_payment_application",
        "action_create_payment_application"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "resolution_note": "Treat Payment Application as an alias for Payment Request where supported by PaymentService.",
      "evidence_refs": [
        "code:PaymentRequest",
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "conflict_department_manager_code_value",
      "type": "conflict",
      "description": "RoleCode constant is named DEPARTMENT_MANAGER but its string value is DEPT_MANAGER.",
      "involved_ids": [
        "role_department_manager"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "resolution_note": "Use the code value DEPT_MANAGER as the role name while preserving the constant-name evidence.",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.9
    },
    {
      "id": "conflict_model_accessors_not_defined_in_source",
      "type": "conflict",
      "description": "Service code calls getters and setters such as getEstimatedAmount, getContractStatus, getPaymentStatus, getLines, setActivatedAt, but the provided model classes only show private fields and no accessor methods.",
      "involved_ids": [
        "purchase_request",
        "contract",
        "purchase_order",
        "goods_receipt",
        "invoice",
        "payment_request"
      ],
      "severity": "medium",
      "resolution_status": "needs_human_review",
      "resolution_note": "Ontology extraction treats these calls as business evidence, but the provided source code is internally incomplete for accessor definitions.",
      "evidence_refs": [
        "code:ApprovalService",
        "code:PurchaseRequestService",
        "code:ContractService",
        "code:PurchaseOrderService",
        "code:ReceiptInvoiceMatchingService",
        "code:PaymentService"
      ],
      "confidence": 0.85
    }
  ],
  "uncertainties": [
    {
      "id": "uncertainty_status_transitions_incomplete",
      "type": "uncertainty",
      "description": "Status transitions are not fully implemented in the provided code. requestStatusGuard is empty, and several service methods validate preconditions without setting the corresponding status field.",
      "reason": "The code contains status constants and guard calls but omits persistence and most explicit status assignments.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:ContractService",
        "code:PurchaseOrderService",
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "uncertainty_create_draft_pr_resulting_state",
      "type": "uncertainty",
      "target_id": "event_pr_draft_created",
      "description": "createDraftPR suggests draft creation, but it calls requestStatusGuard(request, null) and does not set requestStatus to DRAFT in the provided code.",
      "reason": "Business meaning is partly inferred from method name and comment.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.65
    },
    {
      "id": "uncertainty_approval_and_rejection_state_changes",
      "type": "uncertainty",
      "target_id": "event_pr_approved",
      "description": "approveRequest and rejectRequest validate permissions/comments but do not set PR_APPROVED or PR_REJECTED in the provided code.",
      "reason": "Resulting states are inferred from method names and status constants rather than explicit assignments.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:ApprovalService",
        "code:ProcurementStatus"
      ],
      "confidence": 0.65
    },
    {
      "id": "uncertainty_contract_created_from_approved_pr",
      "type": "uncertainty",
      "target_id": "action_create_contract_from_approved_pr",
      "description": "createContractFromApprovedPR name references an approved PR, but the method only accepts requestId and Supplier vendor; it does not load or validate a PurchaseRequest status.",
      "reason": "Approved PR requirement is inferred from the function name only.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.65
    },
    {
      "id": "uncertainty_goods_receipt_grn_alias_absent",
      "type": "uncertainty",
      "target_id": "goods_receipt",
      "description": "Goods Receipt is present as GoodsReceipt, but GRN does not appear in the provided source code.",
      "reason": "No code evidence supports a GRN alias.",
      "needs_human_review": false,
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "uncertainty_unmapped_roles",
      "type": "uncertainty",
      "description": "REQUESTER, PROCUREMENT_SPECIALIST, LEGAL_REVIEWER, WAREHOUSE_CLERK, and AP_CLERK are declared as role constants, but the provided code does not define permission checks for them.",
      "reason": "Roles exist in RoleCode, but no corresponding service permission logic was found in the provided source.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:RoleCode",
        "code:ApprovalService",
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "uncertainty_controller_id_parameters_unused",
      "type": "uncertainty",
      "description": "Controller methods accept requestId or contractId parameters, but delegate using only the request or contract object and do not validate the id parameters in the provided code.",
      "reason": "API parameter semantics cannot be fully determined from the controller methods.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:PurchaseRequestController",
        "code:ContractController"
      ],
      "confidence": 0.85
    },
    {
      "id": "uncertainty_receipt_status_values_absent",
      "type": "uncertainty",
      "target_id": "goods_receipt.receipt_status",
      "description": "GoodsReceipt has a receiptStatus field, but no receipt status constants or state values are defined in the provided source code.",
      "reason": "Only the field name is present.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.9
    }
  ],
  "evidence_refs": [
    "code:ApprovalService",
    "code:Contract",
    "code:ContractController",
    "code:ContractService",
    "code:GoodsReceipt",
    "code:Invoice",
    "code:PaymentRequest",
    "code:PaymentService",
    "code:ProcurementStatus",
    "code:PurchaseOrder",
    "code:PurchaseOrderService",
    "code:PurchaseRequest",
    "code:PurchaseRequestController",
    "code:PurchaseRequestLine",
    "code:PurchaseRequestService",
    "code:ReceiptInvoiceMatchingService",
    "code:RoleCode",
    "code:Supplier"
  ],
  "confidence": 0.88,
  "provenance": {
    "created_by": "AI tool under evaluation",
    "method": "ai_generated",
    "source_system": "source_code"
  }
}
