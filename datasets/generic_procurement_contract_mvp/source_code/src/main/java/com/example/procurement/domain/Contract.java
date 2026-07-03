package com.example.procurement.domain;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.OffsetDateTime;

public class Contract {
    private Long contractId;
    private String contractNo;
    private Long supplierId;
    private Long requestId;
    private String contractTitle;
    private BigDecimal contractAmount;
    private String contractStatus;
    private LocalDate startDate;
    private LocalDate endDate;
    private Long legalReviewerId;
    private OffsetDateTime legalApprovedAt;
    private OffsetDateTime activatedAt;
    private String terminationReason;
}
