package com.example.procurement.service;

import com.example.procurement.common.RoleCode;
import com.example.procurement.domain.PurchaseRequest;

import java.math.BigDecimal;

public class ApprovalService {
    public String requiredApproverRole(PurchaseRequest request) {
        if (request.getEstimatedAmount().compareTo(new BigDecimal("50000")) > 0) {
            return RoleCode.FINANCE_MANAGER;
        }
        return RoleCode.DEPARTMENT_MANAGER;
    }

    public void approveRequest(PurchaseRequest request, String approverRole) {
        String requiredRole = requiredApproverRole(request);
        if (!requiredRole.equals(approverRole) && !RoleCode.PROCUREMENT_ADMIN.equals(approverRole)) {
            throw new IllegalStateException("Approver does not have permission for this PR amount");
        }
    }

    public void rejectRequest(PurchaseRequest request, String comment) {
        if (comment == null || comment.length() < 10) {
            throw new IllegalArgumentException("Rejection comment must explain the reason");
        }
    }
}
