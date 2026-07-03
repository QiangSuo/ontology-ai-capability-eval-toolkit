package com.example.procurement.service;

import com.example.procurement.common.ProcurementStatus;
import com.example.procurement.domain.PurchaseRequest;

public class PurchaseRequestService {
    public PurchaseRequest createDraftPR(PurchaseRequest request) {
        requestStatusGuard(request, null);
        // PR is the code abbreviation for Purchase Request.
        return request;
    }

    public void submitPR(PurchaseRequest request) {
        if (!request.isEditable()) {
            throw new IllegalStateException("Only draft or rejected PR can be submitted");
        }
        if (request.getLines() == null || request.getLines().isEmpty()) {
            throw new IllegalArgumentException("Purchase request must contain at least one line");
        }
        if (request.getBusinessJustification() == null || request.getBusinessJustification().isBlank()) {
            throw new IllegalArgumentException("Business justification is required before submission");
        }
        requestStatusGuard(request, ProcurementStatus.PR_SUBMITTED);
    }

    public void cancelPR(PurchaseRequest request, String reason) {
        if (ProcurementStatus.PR_APPROVED.equals(request.getRequestStatus())) {
            throw new IllegalStateException("Approved PR cannot be cancelled without procurement admin review");
        }
        if (reason == null || reason.isBlank()) {
            throw new IllegalArgumentException("Cancellation reason is required");
        }
        requestStatusGuard(request, ProcurementStatus.PR_CANCELLED);
    }

    private void requestStatusGuard(PurchaseRequest request, String nextStatus) {
        // This sample omits persistence; the status change is the business event being modeled.
    }
}
