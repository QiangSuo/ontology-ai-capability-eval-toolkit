package com.example.procurement.service;

import com.example.procurement.common.ProcurementStatus;
import com.example.procurement.domain.Invoice;
import com.example.procurement.domain.PaymentRequest;

public class PaymentService {
    public PaymentRequest createPaymentApplication(Invoice invoice) {
        if (!ProcurementStatus.INVOICE_MATCHED.equals(invoice.getInvoiceStatus())) {
            throw new IllegalStateException("Only matched invoice can create payment application");
        }
        return new PaymentRequest();
    }

    public void approvePayment(PaymentRequest request, String roleCode) {
        if (!"FINANCE_MANAGER".equals(roleCode) && !"PROCUREMENT_ADMIN".equals(roleCode)) {
            throw new IllegalStateException("Only finance manager or admin can approve payment");
        }
    }

    public void markPaid(PaymentRequest request) {
        if (!ProcurementStatus.PAYMENT_APPROVED.equals(request.getPaymentStatus())) {
            throw new IllegalStateException("Only approved payment request can be paid");
        }
    }
}
