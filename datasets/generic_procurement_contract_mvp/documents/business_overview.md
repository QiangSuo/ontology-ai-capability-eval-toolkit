# Business Overview

## System Purpose

The Generic Procurement Contract System manages the lifecycle from purchase need identification to supplier payment. It is used by requesters, department managers, procurement specialists, finance managers, legal reviewers, warehouse clerks, accounts payable clerks, and procurement administrators.

## Core Business Objects

- Purchase Request: a business request for goods or services before sourcing or contracting.
- Purchase Request Line: an item or service line under a purchase request.
- Supplier: an external vendor that provides goods or services.
- Approval Record: a decision record for purchase request, contract, or payment application approval.
- Contract: a legal agreement with a supplier.
- Purchase Order: an operational order released against an active contract.
- Goods Receipt: a receiving record, also called GRN in warehouse communication.
- Invoice: a supplier billing document matched against purchase order and goods receipt.
- Payment Request: a finance request to pay a matched invoice. Some users call it Payment Application.
- Department and User: organizational actors that own requests, approvals, receiving, and payment actions.

## End-to-End Flow

1. A requester creates a Purchase Request.
2. The Purchase Request is submitted for approval.
3. The department manager approves normal requests.
4. High-value requests require finance approval.
5. Procurement confirms an eligible supplier and prepares a contract.
6. Legal reviews the contract.
7. An active contract allows purchase order release.
8. Warehouse records goods receipt or GRN.
9. Accounts payable matches supplier invoice against PO and receipt.
10. Finance approves and executes payment.

## Scope Notes

The system is intentionally small. It excludes bidding, multi-currency settlement, tax accounting, ERP integration, budget reservation, and supplier portal functions.
