package com.example.procurement.service;

import com.example.procurement.common.ProcurementStatus;
import com.example.procurement.domain.Contract;
import com.example.procurement.domain.PurchaseOrder;

public class PurchaseOrderService {
    public PurchaseOrder releasePurchaseOrder(Contract contract) {
        if (!ProcurementStatus.CONTRACT_ACTIVE.equals(contract.getContractStatus())) {
            throw new IllegalStateException("Purchase order can be released only for active contract");
        }
        return new PurchaseOrder();
    }

    public void closePurchaseOrder(PurchaseOrder order) {
        if (!ProcurementStatus.PO_PARTIALLY_RECEIVED.equals(order.getPoStatus())
                && !ProcurementStatus.PO_RELEASED.equals(order.getPoStatus())) {
            throw new IllegalStateException("Only released or partially received PO can be closed");
        }
    }
}
