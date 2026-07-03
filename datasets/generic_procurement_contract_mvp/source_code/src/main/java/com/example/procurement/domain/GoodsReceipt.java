package com.example.procurement.domain;

import java.time.OffsetDateTime;

public class GoodsReceipt {
    private Long receiptId;
    private String receiptNo;
    private Long poId;
    private String receiptStatus;
    private Long receivedBy;
    private OffsetDateTime receivedAt;
    private String inspectionResult;
    private String remarks;
}
