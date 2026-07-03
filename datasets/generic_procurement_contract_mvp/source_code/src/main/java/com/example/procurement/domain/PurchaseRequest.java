package com.example.procurement.domain;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;

public class PurchaseRequest {
    private Long requestId;
    private String requestNo;
    private String requestTitle;
    private Long requesterUserId;
    private Long departmentId;
    private Long preferredSupplierId;
    private BigDecimal estimatedAmount;
    private String currencyCode;
    private String requestStatus;
    private String businessJustification;
    private LocalDate requiredByDate;
    private OffsetDateTime submittedAt;
    private OffsetDateTime approvedAt;
    private List<PurchaseRequestLine> lines = new ArrayList<>();

    public boolean isEditable() {
        return "DRAFT".equals(requestStatus) || "REJECTED".equals(requestStatus);
    }

    public boolean requiresFinanceReview() {
        return estimatedAmount != null && estimatedAmount.compareTo(new BigDecimal("50000")) > 0;
    }
}
