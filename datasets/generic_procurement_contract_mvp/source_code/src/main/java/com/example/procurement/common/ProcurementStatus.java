package com.example.procurement.common;

public final class ProcurementStatus {
    private ProcurementStatus() {}

    public static final String PR_DRAFT = "DRAFT";
    public static final String PR_SUBMITTED = "SUBMITTED";
    public static final String PR_APPROVED = "APPROVED";
    public static final String PR_REJECTED = "REJECTED";
    public static final String PR_CANCELLED = "CANCELLED";

    public static final String CONTRACT_DRAFT = "DRAFT";
    public static final String CONTRACT_LEGAL_REVIEW = "LEGAL_REVIEW";
    public static final String CONTRACT_ACTIVE = "ACTIVE";
    public static final String CONTRACT_EXPIRED = "EXPIRED";
    public static final String CONTRACT_TERMINATED = "TERMINATED";

    public static final String PO_RELEASED = "RELEASED";
    public static final String PO_PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED";
    public static final String PO_CLOSED = "CLOSED";

    public static final String INVOICE_PENDING = "PENDING_MATCH";
    public static final String INVOICE_MATCHED = "MATCHED";
    public static final String INVOICE_EXCEPTION = "EXCEPTION";

    public static final String PAYMENT_REQUESTED = "REQUESTED";
    public static final String PAYMENT_APPROVED = "APPROVED";
    public static final String PAYMENT_PAID = "PAID";
    public static final String PAYMENT_HELD = "HELD";
}
