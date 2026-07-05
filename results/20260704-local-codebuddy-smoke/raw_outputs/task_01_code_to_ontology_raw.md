{
  "schema_version": "1.0.0",
  "ontology_id": "procurement-contract-mvp-code-ontology",
  "title": "Procurement Contract MVP Code Ontology Draft",
  "domain": "procurement_contract",
  "concepts": [
    {
      "id": "concept:PurchaseRequest",
      "name": "PurchaseRequest",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:PurchaseRequest.requestId",
        "attr:PurchaseRequest.requestNo",
        "attr:PurchaseRequest.requestTitle",
        "attr:PurchaseRequest.requesterUserId",
        "attr:PurchaseRequest.departmentId",
        "attr:PurchaseRequest.preferredSupplierId",
        "attr:PurchaseRequest.estimatedAmount",
        "attr:PurchaseRequest.currencyCode",
        "attr:PurchaseRequest.requestStatus",
        "attr:PurchaseRequest.businessJustification",
        "attr:PurchaseRequest.requiredByDate",
        "attr:PurchaseRequest.submittedAt",
        "attr:PurchaseRequest.approvedAt",
        "attr:PurchaseRequest.lines"
      ],
      "state_ids": [
        "state:PR_DRAFT",
        "state:PR_SUBMITTED",
        "state:PR_APPROVED",
        "state:PR_REJECTED",
        "state:PR_CANCELLED"
      ],
      "alias_ids": [
        "alias:PurchaseRequest.PR"
      ],
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:PurchaseRequestLine",
      "name": "PurchaseRequestLine",
      "type": "concept",
      "category": "document_line",
      "attribute_ids": [
        "attr:PurchaseRequestLine.lineId",
        "attr:PurchaseRequestLine.requestId",
        "attr:PurchaseRequestLine.itemDescription",
        "attr:PurchaseRequestLine.categoryCode",
        "attr:PurchaseRequestLine.quantity",
        "attr:PurchaseRequestLine.unitOfMeasure",
        "attr:PurchaseRequestLine.estimatedUnitPrice",
        "attr:PurchaseRequestLine.lineAmount"
      ],
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:Supplier",
      "name": "Supplier",
      "type": "concept",
      "category": "party",
      "attribute_ids": [
        "attr:Supplier.supplierId",
        "attr:Supplier.supplierCode",
        "attr:Supplier.supplierName",
        "attr:Supplier.supplierStatus",
        "attr:Supplier.riskRating",
        "attr:Supplier.contactEmail",
        "attr:Supplier.onboardedAt"
      ],
      "alias_ids": [
        "alias:Supplier.Vendor"
      ],
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:Contract",
      "name": "Contract",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:Contract.contractId",
        "attr:Contract.contractNo",
        "attr:Contract.supplierId",
        "attr:Contract.requestId",
        "attr:Contract.contractTitle",
        "attr:Contract.contractAmount",
        "attr:Contract.contractStatus",
        "attr:Contract.startDate",
        "attr:Contract.endDate",
        "attr:Contract.legalReviewerId",
        "attr:Contract.legalApprovedAt",
        "attr:Contract.activatedAt",
        "attr:Contract.terminationReason"
      ],
      "state_ids": [
        "state:CONTRACT_DRAFT",
        "state:CONTRACT_LEGAL_REVIEW",
        "state:CONTRACT_ACTIVE",
        "state:CONTRACT_EXPIRED",
        "state:CONTRACT_TERMINATED"
      ],
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:PurchaseOrder",
      "name": "PurchaseOrder",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:PurchaseOrder.poId",
        "attr:PurchaseOrder.poNo",
        "attr:PurchaseOrder.contractId",
        "attr:PurchaseOrder.requestId",
        "attr:PurchaseOrder.supplierId",
        "attr:PurchaseOrder.poAmount",
        "attr:PurchaseOrder.poStatus",
        "attr:PurchaseOrder.releasedAt",
        "attr:PurchaseOrder.closedAt"
      ],
      "state_ids": [
        "state:PO_RELEASED",
        "state:PO_PARTIALLY_RECEIVED",
        "state:PO_CLOSED"
      ],
      "alias_ids": [
        "alias:PurchaseOrder.PO"
      ],
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:GoodsReceipt",
      "name": "GoodsReceipt",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:GoodsReceipt.receiptId",
        "attr:GoodsReceipt.receiptNo",
        "attr:GoodsReceipt.poId",
        "attr:GoodsReceipt.receiptStatus",
        "attr:GoodsReceipt.receivedBy",
        "attr:GoodsReceipt.receivedAt",
        "attr:GoodsReceipt.inspectionResult",
        "attr:GoodsReceipt.remarks"
      ],
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:Invoice",
      "name": "Invoice",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:Invoice.invoiceId",
        "attr:Invoice.invoiceNo",
        "attr:Invoice.supplierId",
        "attr:Invoice.poId",
        "attr:Invoice.receiptId",
        "attr:Invoice.invoiceAmount",
        "attr:Invoice.invoiceDate",
        "attr:Invoice.invoiceStatus",
        "attr:Invoice.matchVarianceAmount",
        "attr:Invoice.matchedAt"
      ],
      "state_ids": [
        "state:INVOICE_PENDING",
        "state:INVOICE_MATCHED",
        "state:INVOICE_EXCEPTION"
      ],
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:PaymentRequest",
      "name": "PaymentRequest",
      "type": "concept",
      "category": "document",
      "attribute_ids": [
        "attr:PaymentRequest.paymentRequestId",
        "attr:PaymentRequest.paymentNo",
        "attr:PaymentRequest.invoiceId",
        "attr:PaymentRequest.paymentAmount",
        "attr:PaymentRequest.paymentStatus",
        "attr:PaymentRequest.dueDate",
        "attr:PaymentRequest.approvedBy",
        "attr:PaymentRequest.approvedAt",
        "attr:PaymentRequest.paidAt"
      ],
      "state_ids": [
        "state:PAYMENT_REQUESTED",
        "state:PAYMENT_APPROVED",
        "state:PAYMENT_PAID",
        "state:PAYMENT_HELD"
      ],
      "alias_ids": [
        "alias:PaymentRequest.PaymentApplication"
      ],
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "concept:ApprovalService",
      "name": "ApprovalService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "concept:ContractService",
      "name": "ContractService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.9
    },
    {
      "id": "concept:PaymentService",
      "name": "PaymentService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.9
    },
    {
      "id": "concept:PurchaseOrderService",
      "name": "PurchaseOrderService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.9
    },
    {
      "id": "concept:PurchaseRequestService",
      "name": "PurchaseRequestService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.9
    },
    {
      "id": "concept:ReceiptInvoiceMatchingService",
      "name": "ReceiptInvoiceMatchingService",
      "type": "concept",
      "category": "service",
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    }
  ],
  "attributes": [
    {
      "id": "attr:PurchaseRequest.requestId",
      "concept_id": "concept:PurchaseRequest",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.requestNo",
      "concept_id": "concept:PurchaseRequest",
      "name": "requestNo",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.requestTitle",
      "concept_id": "concept:PurchaseRequest",
      "name": "requestTitle",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.requesterUserId",
      "concept_id": "concept:PurchaseRequest",
      "name": "requesterUserId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.departmentId",
      "concept_id": "concept:PurchaseRequest",
      "name": "departmentId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.preferredSupplierId",
      "concept_id": "concept:PurchaseRequest",
      "name": "preferredSupplierId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.estimatedAmount",
      "concept_id": "concept:PurchaseRequest",
      "name": "estimatedAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.currencyCode",
      "concept_id": "concept:PurchaseRequest",
      "name": "currencyCode",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.requestStatus",
      "concept_id": "concept:PurchaseRequest",
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
      "confidence": 0.9
    },
    {
      "id": "attr:PurchaseRequest.businessJustification",
      "concept_id": "concept:PurchaseRequest",
      "name": "businessJustification",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.requiredByDate",
      "concept_id": "concept:PurchaseRequest",
      "name": "requiredByDate",
      "type": "attribute",
      "data_type": "LocalDate",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.submittedAt",
      "concept_id": "concept:PurchaseRequest",
      "name": "submittedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.approvedAt",
      "concept_id": "concept:PurchaseRequest",
      "name": "approvedAt",
      "type": "attribute",
      "data_type": "OffsetDateTime",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequest.lines",
      "concept_id": "concept:PurchaseRequest",
      "name": "lines",
      "type": "attribute",
      "data_type": "List<PurchaseRequestLine>",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.lineId",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "lineId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.requestId",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "requestId",
      "type": "attribute",
      "data_type": "Long",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.itemDescription",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "itemDescription",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.categoryCode",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "categoryCode",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.quantity",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "quantity",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.unitOfMeasure",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "unitOfMeasure",
      "type": "attribute",
      "data_type": "String",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.estimatedUnitPrice",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "estimatedUnitPrice",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:PurchaseRequestLine.lineAmount",
      "concept_id": "concept:PurchaseRequestLine",
      "name": "lineAmount",
      "type": "attribute",
      "data_type": "BigDecimal",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "attr:Supplier.supplierStatus",
      "concept_id": "concept:Supplier",
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
      "id": "attr:Supplier.riskRating",
      "concept_id": "concept:Supplier",
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
      "id": "attr:Contract.contractStatus",
      "concept_id": "concept:Contract",
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
      "confidence": 0.9
    },
    {
      "id": "attr:PurchaseOrder.poStatus",
      "concept_id": "concept:PurchaseOrder",
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
      "confidence": 0.9
    },
    {
      "id": "attr:Invoice.invoiceStatus",
      "concept_id": "concept:Invoice",
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
        "code:ProcurementStatus"
      ],
      "confidence": 0.9
    },
    {
      "id": "attr:PaymentRequest.paymentStatus",
      "concept_id": "concept:PaymentRequest",
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
      "confidence": 0.9
    },
    {
      "id": "attr:ReceiptInvoiceMatchingService.CODE_MATCH_TOLERANCE_RATE",
      "concept_id": "concept:ReceiptInvoiceMatchingService",
      "name": "CODE_MATCH_TOLERANCE_RATE",
      "type": "attribute",
      "data_type": "BigDecimal",
      "allowed_values": [
        "0.015"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    }
  ],
  "relations": [
    {
      "id": "rel:PurchaseRequest.hasLines.PurchaseRequestLine",
      "type": "relation",
      "source_concept_id": "concept:PurchaseRequest",
      "target_concept_id": "concept:PurchaseRequestLine",
      "predicate": "has_lines",
      "cardinality": "one_to_many",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "rel:PurchaseRequestLine.belongsTo.PurchaseRequest",
      "type": "relation",
      "source_concept_id": "concept:PurchaseRequestLine",
      "target_concept_id": "concept:PurchaseRequest",
      "predicate": "belongs_to_request",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:PurchaseRequest.prefers.Supplier",
      "type": "relation",
      "source_concept_id": "concept:PurchaseRequest",
      "target_concept_id": "concept:Supplier",
      "predicate": "preferred_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:Contract.references.Supplier",
      "type": "relation",
      "source_concept_id": "concept:Contract",
      "target_concept_id": "concept:Supplier",
      "predicate": "has_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:Contract.references.PurchaseRequest",
      "type": "relation",
      "source_concept_id": "concept:Contract",
      "target_concept_id": "concept:PurchaseRequest",
      "predicate": "created_from_request",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:Contract",
        "code:ContractService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:PurchaseOrder.references.Contract",
      "type": "relation",
      "source_concept_id": "concept:PurchaseOrder",
      "target_concept_id": "concept:Contract",
      "predicate": "released_for_contract",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:PurchaseOrder.references.PurchaseRequest",
      "type": "relation",
      "source_concept_id": "concept:PurchaseOrder",
      "target_concept_id": "concept:PurchaseRequest",
      "predicate": "references_request",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.85
    },
    {
      "id": "rel:PurchaseOrder.references.Supplier",
      "type": "relation",
      "source_concept_id": "concept:PurchaseOrder",
      "target_concept_id": "concept:Supplier",
      "predicate": "has_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.85
    },
    {
      "id": "rel:GoodsReceipt.references.PurchaseOrder",
      "type": "relation",
      "source_concept_id": "concept:GoodsReceipt",
      "target_concept_id": "concept:PurchaseOrder",
      "predicate": "received_for_order",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:Invoice.references.PurchaseOrder",
      "type": "relation",
      "source_concept_id": "concept:Invoice",
      "target_concept_id": "concept:PurchaseOrder",
      "predicate": "billed_for_order",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:Invoice.references.GoodsReceipt",
      "type": "relation",
      "source_concept_id": "concept:Invoice",
      "target_concept_id": "concept:GoodsReceipt",
      "predicate": "matched_with_receipt",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:Invoice",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rel:Invoice.references.Supplier",
      "type": "relation",
      "source_concept_id": "concept:Invoice",
      "target_concept_id": "concept:Supplier",
      "predicate": "issued_by_supplier",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.85
    },
    {
      "id": "rel:PaymentRequest.references.Invoice",
      "type": "relation",
      "source_concept_id": "concept:PaymentRequest",
      "target_concept_id": "concept:Invoice",
      "predicate": "created_from_invoice",
      "cardinality": "many_to_one",
      "evidence_refs": [
        "code:PaymentRequest",
        "code:PaymentService"
      ],
      "confidence": 0.9
    }
  ],
  "events": [
    {
      "id": "event:CreateDraftPR",
      "type": "event",
      "name": "CreateDraftPR",
      "trigger": "PurchaseRequestService.createDraftPR",
      "participant_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:SubmitPR",
      "type": "event",
      "name": "SubmitPR",
      "trigger": "PurchaseRequestService.submitPR",
      "participant_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "resulting_state_ids": [
        "state:PR_SUBMITTED"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "event:CancelPR",
      "type": "event",
      "name": "CancelPR",
      "trigger": "PurchaseRequestService.cancelPR",
      "participant_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "resulting_state_ids": [
        "state:PR_CANCELLED"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "event:ApproveRequest",
      "type": "event",
      "name": "ApproveRequest",
      "trigger": "ApprovalService.approveRequest",
      "participant_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:RejectRequest",
      "type": "event",
      "name": "RejectRequest",
      "trigger": "ApprovalService.rejectRequest",
      "participant_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:SubmitLegalReview",
      "type": "event",
      "name": "SubmitLegalReview",
      "trigger": "ContractService.submitLegalReview",
      "participant_concept_ids": [
        "concept:Contract"
      ],
      "resulting_state_ids": [
        "state:CONTRACT_LEGAL_REVIEW"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.75
    },
    {
      "id": "event:ActivateContract",
      "type": "event",
      "name": "ActivateContract",
      "trigger": "ContractService.activateContract",
      "participant_concept_ids": [
        "concept:Contract"
      ],
      "resulting_state_ids": [
        "state:CONTRACT_ACTIVE"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.75
    },
    {
      "id": "event:TerminateContract",
      "type": "event",
      "name": "TerminateContract",
      "trigger": "ContractService.terminateContract",
      "participant_concept_ids": [
        "concept:Contract"
      ],
      "resulting_state_ids": [
        "state:CONTRACT_TERMINATED"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:ReleasePurchaseOrder",
      "type": "event",
      "name": "ReleasePurchaseOrder",
      "trigger": "PurchaseOrderService.releasePurchaseOrder",
      "participant_concept_ids": [
        "concept:Contract",
        "concept:PurchaseOrder"
      ],
      "resulting_state_ids": [
        "state:PO_RELEASED"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.75
    },
    {
      "id": "event:ClosePurchaseOrder",
      "type": "event",
      "name": "ClosePurchaseOrder",
      "trigger": "PurchaseOrderService.closePurchaseOrder",
      "participant_concept_ids": [
        "concept:PurchaseOrder"
      ],
      "resulting_state_ids": [
        "state:PO_CLOSED"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:RecordGoodsReceipt",
      "type": "event",
      "name": "RecordGoodsReceipt",
      "trigger": "ReceiptInvoiceMatchingService.recordGoodsReceipt",
      "participant_concept_ids": [
        "concept:PurchaseOrder",
        "concept:GoodsReceipt"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:MatchInvoice",
      "type": "event",
      "name": "MatchInvoice",
      "trigger": "ReceiptInvoiceMatchingService.matchInvoice",
      "participant_concept_ids": [
        "concept:PurchaseOrder",
        "concept:GoodsReceipt",
        "concept:Invoice"
      ],
      "resulting_state_ids": [
        "state:INVOICE_MATCHED"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:CreatePaymentApplication",
      "type": "event",
      "name": "CreatePaymentApplication",
      "trigger": "PaymentService.createPaymentApplication",
      "participant_concept_ids": [
        "concept:Invoice",
        "concept:PaymentRequest"
      ],
      "resulting_state_ids": [
        "state:PAYMENT_REQUESTED"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:ApprovePayment",
      "type": "event",
      "name": "ApprovePayment",
      "trigger": "PaymentService.approvePayment",
      "participant_concept_ids": [
        "concept:PaymentRequest"
      ],
      "resulting_state_ids": [
        "state:PAYMENT_APPROVED"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.7
    },
    {
      "id": "event:MarkPaid",
      "type": "event",
      "name": "MarkPaid",
      "trigger": "PaymentService.markPaid",
      "participant_concept_ids": [
        "concept:PaymentRequest"
      ],
      "resulting_state_ids": [
        "state:PAYMENT_PAID"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.7
    }
  ],
  "rules": [
    {
      "id": "rule:PurchaseRequestEditableStatuses",
      "type": "rule",
      "name": "PurchaseRequestEditableStatuses",
      "condition": "requestStatus equals DRAFT or REJECTED",
      "effect": "PurchaseRequest.isEditable returns true",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:FinanceReviewThreshold",
      "type": "rule",
      "name": "FinanceReviewThreshold",
      "condition": "estimatedAmount is not null and estimatedAmount > 50000",
      "effect": "PurchaseRequest.requiresFinanceReview returns true and ApprovalService.requiredApproverRole returns FINANCE_MANAGER",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:SubmitPROnlyEditable",
      "type": "rule",
      "name": "SubmitPROnlyEditable",
      "condition": "PurchaseRequest.isEditable returns false",
      "effect": "submitPR throws IllegalStateException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:SubmitPRRequiresLine",
      "type": "rule",
      "name": "SubmitPRRequiresLine",
      "condition": "request.lines is null or empty",
      "effect": "submitPR throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:PurchaseRequest",
        "concept:PurchaseRequestLine"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:SubmitPRRequiresBusinessJustification",
      "type": "rule",
      "name": "SubmitPRRequiresBusinessJustification",
      "condition": "businessJustification is null or blank",
      "effect": "submitPR throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ApprovedPRCannotBeCancelledWithoutAdminReview",
      "type": "rule",
      "name": "ApprovedPRCannotBeCancelledWithoutAdminReview",
      "condition": "requestStatus equals APPROVED",
      "effect": "cancelPR throws IllegalStateException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.9
    },
    {
      "id": "rule:CancelPRRequiresReason",
      "type": "rule",
      "name": "CancelPRRequiresReason",
      "condition": "reason is null or blank",
      "effect": "cancelPR throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ApproverRoleByAmount",
      "type": "rule",
      "name": "ApproverRoleByAmount",
      "condition": "estimatedAmount > 50000",
      "effect": "required approver role is FINANCE_MANAGER; otherwise DEPARTMENT_MANAGER",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:PRApprovalRolePermission",
      "type": "rule",
      "name": "PRApprovalRolePermission",
      "condition": "approverRole is neither requiredApproverRole nor PROCUREMENT_ADMIN",
      "effect": "approveRequest throws IllegalStateException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:RejectRequestRequiresComment",
      "type": "rule",
      "name": "RejectRequestRequiresComment",
      "condition": "comment is null or length < 10",
      "effect": "rejectRequest throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:SupplierEligibleForAward",
      "type": "rule",
      "name": "SupplierEligibleForAward",
      "condition": "supplierStatus equals ACTIVE and riskRating does not equal HIGH",
      "effect": "Supplier.isEligibleForAward returns true",
      "applies_to_ids": [
        "concept:Supplier"
      ],
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:CreateContractRequiresEligibleVendor",
      "type": "rule",
      "name": "CreateContractRequiresEligibleVendor",
      "condition": "vendor is null or vendor.isEligibleForAward returns false",
      "effect": "createContractFromApprovedPR throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:Contract",
        "concept:Supplier",
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:LegalReviewOnlyDraftContract",
      "type": "rule",
      "name": "LegalReviewOnlyDraftContract",
      "condition": "contractStatus is not DRAFT",
      "effect": "submitLegalReview throws IllegalStateException",
      "applies_to_ids": [
        "concept:Contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ActivateContractRequiresLegalApproval",
      "type": "rule",
      "name": "ActivateContractRequiresLegalApproval",
      "condition": "legalApprovedAt is null",
      "effect": "activateContract throws IllegalStateException",
      "applies_to_ids": [
        "concept:Contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ActivateContractRequiresTerm",
      "type": "rule",
      "name": "ActivateContractRequiresTerm",
      "condition": "startDate is null or endDate is null",
      "effect": "activateContract throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:Contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:TerminateContractRequiresReason",
      "type": "rule",
      "name": "TerminateContractRequiresReason",
      "condition": "reason is null or blank",
      "effect": "terminateContract throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:Contract"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ReleasePOOnlyForActiveContract",
      "type": "rule",
      "name": "ReleasePOOnlyForActiveContract",
      "condition": "contractStatus is not ACTIVE",
      "effect": "releasePurchaseOrder throws IllegalStateException",
      "applies_to_ids": [
        "concept:Contract",
        "concept:PurchaseOrder"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ClosePOOnlyReleasedOrPartiallyReceived",
      "type": "rule",
      "name": "ClosePOOnlyReleasedOrPartiallyReceived",
      "condition": "poStatus is neither PARTIALLY_RECEIVED nor RELEASED",
      "effect": "closePurchaseOrder throws IllegalStateException",
      "applies_to_ids": [
        "concept:PurchaseOrder"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:GoodsReceiptRequiresReceivedAt",
      "type": "rule",
      "name": "GoodsReceiptRequiresReceivedAt",
      "condition": "receipt.receivedAt is null",
      "effect": "recordGoodsReceipt throws IllegalArgumentException",
      "applies_to_ids": [
        "concept:GoodsReceipt"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:InvoiceMatchRequiresGoodsReceipt",
      "type": "rule",
      "name": "InvoiceMatchRequiresGoodsReceipt",
      "condition": "receipt is null",
      "effect": "matchInvoice throws IllegalStateException",
      "applies_to_ids": [
        "concept:Invoice",
        "concept:GoodsReceipt"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:InvoiceMatchTolerance",
      "type": "rule",
      "name": "InvoiceMatchTolerance",
      "condition": "absolute(invoiceAmount - poAmount) <= poAmount * 0.015 rounded to scale 2 HALF_UP",
      "effect": "matchInvoice returns true",
      "applies_to_ids": [
        "concept:Invoice",
        "concept:PurchaseOrder"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:PaymentApplicationOnlyMatchedInvoice",
      "type": "rule",
      "name": "PaymentApplicationOnlyMatchedInvoice",
      "condition": "invoiceStatus is not MATCHED",
      "effect": "createPaymentApplication throws IllegalStateException",
      "applies_to_ids": [
        "concept:Invoice",
        "concept:PaymentRequest"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:ApprovePaymentRolePermission",
      "type": "rule",
      "name": "ApprovePaymentRolePermission",
      "condition": "roleCode is neither FINANCE_MANAGER nor PROCUREMENT_ADMIN",
      "effect": "approvePayment throws IllegalStateException",
      "applies_to_ids": [
        "concept:PaymentRequest"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "rule:MarkPaidOnlyApprovedPayment",
      "type": "rule",
      "name": "MarkPaidOnlyApprovedPayment",
      "condition": "paymentStatus is not APPROVED",
      "effect": "markPaid throws IllegalStateException",
      "applies_to_ids": [
        "concept:PaymentRequest"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    }
  ],
  "actions": [
    {
      "id": "action:CreateDraftPR",
      "type": "action",
      "name": "createDraftPR",
      "target_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:SubmitPR",
      "type": "action",
      "name": "submitPR",
      "target_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "preconditions": [
        "PurchaseRequest is editable",
        "PurchaseRequest has at least one line",
        "businessJustification is not blank"
      ],
      "postconditions": [
        "requestStatusGuard called with SUBMITTED"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:PurchaseRequestController"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:CancelPR",
      "type": "action",
      "name": "cancelPR",
      "target_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "preconditions": [
        "reason is not blank",
        "requestStatus is not APPROVED"
      ],
      "postconditions": [
        "requestStatusGuard called with CANCELLED"
      ],
      "evidence_refs": [
        "code:PurchaseRequestService",
        "code:PurchaseRequestController"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:ApproveRequest",
      "type": "action",
      "name": "approveRequest",
      "actor_role_ids": [
        "role:DEPARTMENT_MANAGER",
        "role:FINANCE_MANAGER",
        "role:PROCUREMENT_ADMIN"
      ],
      "target_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "action:RejectRequest",
      "type": "action",
      "name": "rejectRequest",
      "target_concept_ids": [
        "concept:PurchaseRequest"
      ],
      "preconditions": [
        "comment length is at least 10"
      ],
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.8
    },
    {
      "id": "action:CreateContractFromApprovedPR",
      "type": "action",
      "name": "createContractFromApprovedPR",
      "target_concept_ids": [
        "concept:Contract",
        "concept:PurchaseRequest",
        "concept:Supplier"
      ],
      "preconditions": [
        "vendor is eligible for award"
      ],
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:SubmitLegalReview",
      "type": "action",
      "name": "submitLegalReview",
      "target_concept_ids": [
        "concept:Contract"
      ],
      "preconditions": [
        "contractStatus equals DRAFT"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:ActivateContract",
      "type": "action",
      "name": "activateContract",
      "target_concept_ids": [
        "concept:Contract"
      ],
      "preconditions": [
        "legalApprovedAt is not null",
        "startDate and endDate are not null"
      ],
      "postconditions": [
        "activatedAt set to current OffsetDateTime"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:TerminateContract",
      "type": "action",
      "name": "terminateContract",
      "target_concept_ids": [
        "concept:Contract"
      ],
      "preconditions": [
        "reason is not blank"
      ],
      "evidence_refs": [
        "code:ContractService",
        "code:ContractController"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:ReleasePurchaseOrder",
      "type": "action",
      "name": "releasePurchaseOrder",
      "target_concept_ids": [
        "concept:PurchaseOrder",
        "concept:Contract"
      ],
      "preconditions": [
        "contractStatus equals ACTIVE"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:ClosePurchaseOrder",
      "type": "action",
      "name": "closePurchaseOrder",
      "target_concept_ids": [
        "concept:PurchaseOrder"
      ],
      "preconditions": [
        "poStatus equals RELEASED or PARTIALLY_RECEIVED"
      ],
      "evidence_refs": [
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:RecordGoodsReceipt",
      "type": "action",
      "name": "recordGoodsReceipt",
      "target_concept_ids": [
        "concept:PurchaseOrder",
        "concept:GoodsReceipt"
      ],
      "preconditions": [
        "receivedAt is not null"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:MatchInvoice",
      "type": "action",
      "name": "matchInvoice",
      "target_concept_ids": [
        "concept:PurchaseOrder",
        "concept:GoodsReceipt",
        "concept:Invoice"
      ],
      "preconditions": [
        "receipt is not null"
      ],
      "evidence_refs": [
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:CreatePaymentApplication",
      "type": "action",
      "name": "createPaymentApplication",
      "target_concept_ids": [
        "concept:Invoice",
        "concept:PaymentRequest"
      ],
      "preconditions": [
        "invoiceStatus equals MATCHED"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:ApprovePayment",
      "type": "action",
      "name": "approvePayment",
      "actor_role_ids": [
        "role:FINANCE_MANAGER",
        "role:PROCUREMENT_ADMIN"
      ],
      "target_concept_ids": [
        "concept:PaymentRequest"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "action:MarkPaid",
      "type": "action",
      "name": "markPaid",
      "target_concept_ids": [
        "concept:PaymentRequest"
      ],
      "preconditions": [
        "paymentStatus equals APPROVED"
      ],
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    }
  ],
  "states": [
    {
      "id": "state:PR_DRAFT",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept:PurchaseRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PR_SUBMITTED",
      "type": "state",
      "name": "SUBMITTED",
      "owner_concept_id": "concept:PurchaseRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PR_APPROVED",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept:PurchaseRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PR_REJECTED",
      "type": "state",
      "name": "REJECTED",
      "owner_concept_id": "concept:PurchaseRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PR_CANCELLED",
      "type": "state",
      "name": "CANCELLED",
      "owner_concept_id": "concept:PurchaseRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:CONTRACT_DRAFT",
      "type": "state",
      "name": "DRAFT",
      "owner_concept_id": "concept:Contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:CONTRACT_LEGAL_REVIEW",
      "type": "state",
      "name": "LEGAL_REVIEW",
      "owner_concept_id": "concept:Contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:CONTRACT_ACTIVE",
      "type": "state",
      "name": "ACTIVE",
      "owner_concept_id": "concept:Contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:CONTRACT_EXPIRED",
      "type": "state",
      "name": "EXPIRED",
      "owner_concept_id": "concept:Contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:CONTRACT_TERMINATED",
      "type": "state",
      "name": "TERMINATED",
      "owner_concept_id": "concept:Contract",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PO_RELEASED",
      "type": "state",
      "name": "RELEASED",
      "owner_concept_id": "concept:PurchaseOrder",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PO_PARTIALLY_RECEIVED",
      "type": "state",
      "name": "PARTIALLY_RECEIVED",
      "owner_concept_id": "concept:PurchaseOrder",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PO_CLOSED",
      "type": "state",
      "name": "CLOSED",
      "owner_concept_id": "concept:PurchaseOrder",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:INVOICE_PENDING",
      "type": "state",
      "name": "PENDING_MATCH",
      "owner_concept_id": "concept:Invoice",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:INVOICE_MATCHED",
      "type": "state",
      "name": "MATCHED",
      "owner_concept_id": "concept:Invoice",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:INVOICE_EXCEPTION",
      "type": "state",
      "name": "EXCEPTION",
      "owner_concept_id": "concept:Invoice",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PAYMENT_REQUESTED",
      "type": "state",
      "name": "REQUESTED",
      "owner_concept_id": "concept:PaymentRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PAYMENT_APPROVED",
      "type": "state",
      "name": "APPROVED",
      "owner_concept_id": "concept:PaymentRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PAYMENT_PAID",
      "type": "state",
      "name": "PAID",
      "owner_concept_id": "concept:PaymentRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    },
    {
      "id": "state:PAYMENT_HELD",
      "type": "state",
      "name": "HELD",
      "owner_concept_id": "concept:PaymentRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.95
    }
  ],
  "roles": [
    {
      "id": "role:REQUESTER",
      "type": "role",
      "name": "REQUESTER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:DEPARTMENT_MANAGER",
      "type": "role",
      "name": "DEPT_MANAGER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:PROCUREMENT_SPECIALIST",
      "type": "role",
      "name": "PROCUREMENT_SPECIALIST",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:FINANCE_MANAGER",
      "type": "role",
      "name": "FINANCE_MANAGER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:LEGAL_REVIEWER",
      "type": "role",
      "name": "LEGAL_REVIEWER",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:WAREHOUSE_CLERK",
      "type": "role",
      "name": "WAREHOUSE_CLERK",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:AP_CLERK",
      "type": "role",
      "name": "AP_CLERK",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    },
    {
      "id": "role:PROCUREMENT_ADMIN",
      "type": "role",
      "name": "PROCUREMENT_ADMIN",
      "evidence_refs": [
        "code:RoleCode"
      ],
      "confidence": 0.95
    }
  ],
  "permissions": [
    {
      "id": "perm:DEPARTMENT_MANAGER.ApproveRequest",
      "type": "permission",
      "role_id": "role:DEPARTMENT_MANAGER",
      "action_id": "action:ApproveRequest",
      "resource_concept_id": "concept:PurchaseRequest",
      "effect": "conditional",
      "condition": "requiredApproverRole(request) equals DEPARTMENT_MANAGER",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "perm:FINANCE_MANAGER.ApproveRequest",
      "type": "permission",
      "role_id": "role:FINANCE_MANAGER",
      "action_id": "action:ApproveRequest",
      "resource_concept_id": "concept:PurchaseRequest",
      "effect": "conditional",
      "condition": "requiredApproverRole(request) equals FINANCE_MANAGER",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "perm:PROCUREMENT_ADMIN.ApproveRequest",
      "type": "permission",
      "role_id": "role:PROCUREMENT_ADMIN",
      "action_id": "action:ApproveRequest",
      "resource_concept_id": "concept:PurchaseRequest",
      "effect": "allow",
      "evidence_refs": [
        "code:ApprovalService"
      ],
      "confidence": 0.9
    },
    {
      "id": "perm:FINANCE_MANAGER.ApprovePayment",
      "type": "permission",
      "role_id": "role:FINANCE_MANAGER",
      "action_id": "action:ApprovePayment",
      "resource_concept_id": "concept:PaymentRequest",
      "effect": "allow",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "perm:PROCUREMENT_ADMIN.ApprovePayment",
      "type": "permission",
      "role_id": "role:PROCUREMENT_ADMIN",
      "action_id": "action:ApprovePayment",
      "resource_concept_id": "concept:PaymentRequest",
      "effect": "allow",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    }
  ],
  "aliases": [
    {
      "id": "alias:Supplier.Vendor",
      "type": "alias",
      "canonical_id": "concept:Supplier",
      "alias": "Vendor",
      "language": "en",
      "source_context": "ContractService.createContractFromApprovedPR parameter name vendor has type Supplier",
      "evidence_refs": [
        "code:ContractService",
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias:PurchaseRequest.PR",
      "type": "alias",
      "canonical_id": "concept:PurchaseRequest",
      "alias": "PR",
      "language": "en",
      "source_context": "PurchaseRequestService comment says PR is the code abbreviation for Purchase Request",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias:PurchaseOrder.PO",
      "type": "alias",
      "canonical_id": "concept:PurchaseOrder",
      "alias": "PO",
      "language": "en",
      "source_context": "PurchaseOrder fields and service messages use poId, poNo, poAmount, poStatus and PO abbreviation",
      "evidence_refs": [
        "code:PurchaseOrder",
        "code:PurchaseOrderService"
      ],
      "confidence": 0.95
    },
    {
      "id": "alias:PaymentRequest.PaymentApplication",
      "type": "alias",
      "canonical_id": "concept:PaymentRequest",
      "alias": "PaymentApplication",
      "language": "en",
      "source_context": "PaymentService.createPaymentApplication returns PaymentRequest",
      "evidence_refs": [
        "code:PaymentService",
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    }
  ],
  "mappings": [
    {
      "id": "map:concept:PurchaseRequest",
      "type": "mapping",
      "ontology_element_id": "concept:PurchaseRequest",
      "source_element": "src/main/java/com/example/procurement/domain/PurchaseRequest.java#PurchaseRequest",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:PurchaseRequestLine",
      "type": "mapping",
      "ontology_element_id": "concept:PurchaseRequestLine",
      "source_element": "src/main/java/com/example/procurement/domain/PurchaseRequestLine.java#PurchaseRequestLine",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestLine"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:Supplier",
      "type": "mapping",
      "ontology_element_id": "concept:Supplier",
      "source_element": "src/main/java/com/example/procurement/domain/Supplier.java#Supplier",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Supplier"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:Contract",
      "type": "mapping",
      "ontology_element_id": "concept:Contract",
      "source_element": "src/main/java/com/example/procurement/domain/Contract.java#Contract",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Contract"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:PurchaseOrder",
      "type": "mapping",
      "ontology_element_id": "concept:PurchaseOrder",
      "source_element": "src/main/java/com/example/procurement/domain/PurchaseOrder.java#PurchaseOrder",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseOrder"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:GoodsReceipt",
      "type": "mapping",
      "ontology_element_id": "concept:GoodsReceipt",
      "source_element": "src/main/java/com/example/procurement/domain/GoodsReceipt.java#GoodsReceipt",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:Invoice",
      "type": "mapping",
      "ontology_element_id": "concept:Invoice",
      "source_element": "src/main/java/com/example/procurement/domain/Invoice.java#Invoice",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:Invoice"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:concept:PaymentRequest",
      "type": "mapping",
      "ontology_element_id": "concept:PaymentRequest",
      "source_element": "src/main/java/com/example/procurement/domain/PaymentRequest.java#PaymentRequest",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PaymentRequest"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:action:SubmitPR",
      "type": "mapping",
      "ontology_element_id": "action:SubmitPR",
      "source_element": "src/main/java/com/example/procurement/service/PurchaseRequestService.java#submitPR",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PurchaseRequestService"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:action:ActivateContract",
      "type": "mapping",
      "ontology_element_id": "action:ActivateContract",
      "source_element": "src/main/java/com/example/procurement/service/ContractService.java#activateContract",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:action:ApprovePayment",
      "type": "mapping",
      "ontology_element_id": "action:ApprovePayment",
      "source_element": "src/main/java/com/example/procurement/service/PaymentService.java#approvePayment",
      "source_type": "code",
      "mapping_type": "exact",
      "evidence_refs": [
        "code:PaymentService"
      ],
      "confidence": 0.95
    },
    {
      "id": "map:states:ProcurementStatus",
      "type": "mapping",
      "ontology_element_id": "state:PR_DRAFT",
      "source_element": "src/main/java/com/example/procurement/common/ProcurementStatus.java#ProcurementStatus",
      "source_type": "code",
      "mapping_type": "partial",
      "transform_note": "ProcurementStatus contains states for PurchaseRequest, Contract, PurchaseOrder, Invoice, and PaymentRequest",
      "evidence_refs": [
        "code:ProcurementStatus"
      ],
      "confidence": 0.9
    }
  ],
  "conflicts": [
    {
      "id": "conflict:SupplierVendorNaming",
      "type": "conflict",
      "description": "ContractService uses parameter name vendor for an object typed Supplier, indicating internal naming variation between Supplier and Vendor.",
      "involved_ids": [
        "concept:Supplier",
        "alias:Supplier.Vendor"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "evidence_refs": [
        "code:ContractService",
        "code:Supplier"
      ],
      "confidence": 0.9
    },
    {
      "id": "conflict:PaymentRequestApplicationNaming",
      "type": "conflict",
      "description": "PaymentService method createPaymentApplication returns PaymentRequest and error text says payment application, indicating naming variation between PaymentRequest and PaymentApplication.",
      "involved_ids": [
        "concept:PaymentRequest",
        "alias:PaymentRequest.PaymentApplication"
      ],
      "severity": "low",
      "resolution_status": "accepted",
      "evidence_refs": [
        "code:PaymentService",
        "code:PaymentRequest"
      ],
      "confidence": 0.9
    },
    {
      "id": "conflict:RoleCodeLiteralMismatch",
      "type": "conflict",
      "description": "RoleCode.DEPARTMENT_MANAGER constant name maps to value DEPT_MANAGER, while ApprovalService returns RoleCode.DEPARTMENT_MANAGER; role id and role value naming are not identical.",
      "involved_ids": [
        "role:DEPARTMENT_MANAGER"
      ],
      "severity": "low",
      "resolution_status": "needs_human_review",
      "evidence_refs": [
        "code:RoleCode",
        "code:ApprovalService"
      ],
      "confidence": 0.85
    },
    {
      "id": "conflict:DomainMethodsReferencedButNotDefinedInReadClasses",
      "type": "conflict",
      "description": "Services call getters and setters such as getEstimatedAmount, getContractStatus, setActivatedAt, and getPoStatus, but the read domain class source shows private fields and no explicit accessor methods.",
      "involved_ids": [
        "concept:PurchaseRequest",
        "concept:Contract",
        "concept:PurchaseOrder",
        "concept:Invoice",
        "concept:PaymentRequest",
        "concept:GoodsReceipt"
      ],
      "severity": "medium",
      "resolution_status": "needs_human_review",
      "evidence_refs": [
        "code:PurchaseRequest",
        "code:Contract",
        "code:PurchaseOrder",
        "code:Invoice",
        "code:PaymentRequest",
        "code:GoodsReceipt"
      ],
      "confidence": 0.9
    }
  ],
  "uncertainties": [
    {
      "id": "uncertainty:StatusTransitionsIncomplete",
      "type": "uncertainty",
      "description": "ProcurementStatus declares multiple states, but service methods do not implement complete state transition assignments for approval, rejection, legal review, termination, PO release/close, invoice match, or payment approval/paid.",
      "reason": "Most methods validate preconditions or return new objects without setting the corresponding status field.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:ProcurementStatus",
        "code:PurchaseRequestService",
        "code:ApprovalService",
        "code:ContractService",
        "code:PurchaseOrderService",
        "code:PaymentService",
        "code:ReceiptInvoiceMatchingService"
      ],
      "confidence": 0.9
    },
    {
      "id": "uncertainty:CreateContractFromApprovedPRApprovalCheck",
      "type": "uncertainty",
      "target_id": "action:CreateContractFromApprovedPR",
      "description": "Method name says create contract from approved PR, but code only accepts requestId and vendor and does not verify a PurchaseRequest status is APPROVED.",
      "reason": "Business meaning is partially inferred from function name.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:ContractService"
      ],
      "confidence": 0.7
    },
    {
      "id": "uncertainty:GoodsReceiptStateModelMissing",
      "type": "uncertainty",
      "target_id": "concept:GoodsReceipt",
      "description": "GoodsReceipt has receiptStatus field but ProcurementStatus does not define GoodsReceipt-specific statuses.",
      "reason": "No receipt status constants or transition rules are present in the provided source code.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:GoodsReceipt",
        "code:ProcurementStatus"
      ],
      "confidence": 0.85
    },
    {
      "id": "uncertainty:NoGRNAliasInCode",
      "type": "uncertainty",
      "target_id": "concept:GoodsReceipt",
      "description": "No GRN name or abbreviation appears in the provided source code for GoodsReceipt.",
      "reason": "Alias requested for consideration, but evidence is absent in allowed input.",
      "needs_human_review": false,
      "evidence_refs": [
        "code:GoodsReceipt"
      ],
      "confidence": 0.95
    },
    {
      "id": "uncertainty:ControllerActorRolesAbsent",
      "type": "uncertainty",
      "description": "Controllers expose create, submit, cancel, activate, and terminate methods but do not include role checks or actor parameters beyond service-specific roleCode and approverRole checks.",
      "reason": "Permission matrix cannot be fully extracted from the provided source code.",
      "needs_human_review": true,
      "evidence_refs": [
        "code:PurchaseRequestController",
        "code:ContractController",
        "code:ApprovalService",
        "code:PaymentService"
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
  "confidence": 0.9,
  "provenance