package com.example.procurement.domain;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.OffsetDateTime;

public class PaymentRequest {
    private Long paymentRequestId;
    private String paymentNo;
    private Long invoiceId;
    private BigDecimal paymentAmount;
    private String paymentStatus;
    private LocalDate dueDate;
    private Long approvedBy;
    private OffsetDateTime approvedAt;
    private OffsetDateTime paidAt;
}
