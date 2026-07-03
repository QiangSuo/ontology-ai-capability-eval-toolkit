package com.example.procurement.domain;

import java.time.OffsetDateTime;

public class Supplier {
    private Long supplierId;
    private String supplierCode;
    private String supplierName;
    private String supplierStatus;
    private String riskRating;
    private String contactEmail;
    private OffsetDateTime onboardedAt;

    public boolean isEligibleForAward() {
        return "ACTIVE".equals(supplierStatus) && !"HIGH".equals(riskRating);
    }
}
