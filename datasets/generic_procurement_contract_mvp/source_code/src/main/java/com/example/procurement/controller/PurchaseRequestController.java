package com.example.procurement.controller;

import com.example.procurement.domain.PurchaseRequest;
import com.example.procurement.service.PurchaseRequestService;

public class PurchaseRequestController {
    private final PurchaseRequestService purchaseRequestService;

    public PurchaseRequestController(PurchaseRequestService purchaseRequestService) {
        this.purchaseRequestService = purchaseRequestService;
    }

    public PurchaseRequest create(PurchaseRequest request) {
        return purchaseRequestService.createDraftPR(request);
    }

    public void submit(Long requestId, PurchaseRequest request) {
        purchaseRequestService.submitPR(request);
    }

    public void cancel(Long requestId, String reason, PurchaseRequest request) {
        purchaseRequestService.cancelPR(request, reason);
    }
}
