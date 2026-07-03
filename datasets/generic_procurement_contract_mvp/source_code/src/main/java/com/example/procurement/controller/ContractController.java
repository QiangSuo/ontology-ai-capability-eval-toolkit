package com.example.procurement.controller;

import com.example.procurement.domain.Contract;
import com.example.procurement.service.ContractService;

public class ContractController {
    private final ContractService contractService;

    public ContractController(ContractService contractService) {
        this.contractService = contractService;
    }

    public void submitLegalReview(Long contractId, Contract contract) {
        contractService.submitLegalReview(contract);
    }

    public void activate(Long contractId, Contract contract) {
        contractService.activateContract(contract);
    }

    public void terminate(Long contractId, Contract contract, String reason) {
        contractService.terminateContract(contract, reason);
    }
}
