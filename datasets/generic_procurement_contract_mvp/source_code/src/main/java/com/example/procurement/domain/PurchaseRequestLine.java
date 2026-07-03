package com.example.procurement.domain;

import java.math.BigDecimal;

public class PurchaseRequestLine {
    private Long lineId;
    private Long requestId;
    private String itemDescription;
    private String categoryCode;
    private BigDecimal quantity;
    private String unitOfMeasure;
    private BigDecimal estimatedUnitPrice;
    private BigDecimal lineAmount;
}
