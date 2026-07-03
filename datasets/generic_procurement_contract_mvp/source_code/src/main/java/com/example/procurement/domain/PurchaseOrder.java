package com.example.procurement.domain;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

public class PurchaseOrder {
    private Long poId;
    private String poNo;
    private Long contractId;
    private Long requestId;
    private Long supplierId;
    private BigDecimal poAmount;
    private String poStatus;
    private OffsetDateTime releasedAt;
    private OffsetDateTime closedAt;
}
