package com.example.procurement.service;

import com.example.procurement.common.ProcurementStatus;
import com.example.procurement.domain.Contract;
import com.example.procurement.domain.Supplier;

import java.time.OffsetDateTime;

public class ContractService {
    public Contract createContractFromApprovedPR(Long requestId, Supplier vendor) {
        if (vendor == null || !vendor.isEligibleForAward()) {
            throw new IllegalArgumentException("Vendor must be active and not high risk");
        }
        return new Contract();
    }

    public void submitLegalReview(Contract contract) {
        if (!ProcurementStatus.CONTRACT_DRAFT.equals(contract.getContractStatus())) {
            throw new IllegalStateException("Only draft contract can enter legal review");
        }
    }

    public void activateContract(Contract contract) {
        if (contract.getLegalApprovedAt() == null) {
            throw new IllegalStateException("Legal approval is required before activation");
        }
        if (contract.getStartDate() == null || contract.getEndDate() == null) {
            throw new IllegalArgumentException("Contract term is required");
        }
        contract.setActivatedAt(OffsetDateTime.now());
    }

    public void terminateContract(Contract contract, String reason) {
        if (reason == null || reason.isBlank()) {
            throw new IllegalArgumentException("Termination reason is required");
        }
    }
}
