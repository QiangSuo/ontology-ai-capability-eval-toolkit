package com.example.procurement.domain;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.OffsetDateTime;

public class Invoice {
    private Long invoiceId;
    private String invoiceNo;
    private Long supplierId;
    private Long poId;
    private Long receiptId;
    private BigDecimal invoiceAmount;
    private LocalDate invoiceDate;
    private String invoiceStatus;
    private BigDecimal matchVarianceAmount;
    private OffsetDateTime matchedAt;
}
