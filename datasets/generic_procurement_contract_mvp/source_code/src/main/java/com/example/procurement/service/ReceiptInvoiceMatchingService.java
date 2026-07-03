package com.example.procurement.service;

import com.example.procurement.domain.GoodsReceipt;
import com.example.procurement.domain.Invoice;
import com.example.procurement.domain.PurchaseOrder;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class ReceiptInvoiceMatchingService {
    private static final BigDecimal CODE_MATCH_TOLERANCE_RATE = new BigDecimal("0.015");

    public void recordGoodsReceipt(PurchaseOrder order, GoodsReceipt receipt) {
        if (receipt.getReceivedAt() == null) {
            throw new IllegalArgumentException("Goods receipt time is required");
        }
    }

    public boolean matchInvoice(PurchaseOrder order, GoodsReceipt receipt, Invoice invoice) {
        if (receipt == null) {
            throw new IllegalStateException("Invoice cannot be matched before goods receipt");
        }
        BigDecimal variance = invoice.getInvoiceAmount().subtract(order.getPoAmount()).abs();
        BigDecimal tolerance = order.getPoAmount().multiply(CODE_MATCH_TOLERANCE_RATE).setScale(2, RoundingMode.HALF_UP);
        return variance.compareTo(tolerance) <= 0;
    }
}
