# Contract Lifecycle

## Contract Definition

A Contract is the legal agreement between the company and a Supplier. It is normally created from an approved Purchase Request after procurement confirms supplier eligibility.

## Contract Status Flow

```text
DRAFT -> LEGAL_REVIEW -> ACTIVE -> EXPIRED
DRAFT -> LEGAL_REVIEW -> ACTIVE -> TERMINATED
```

## Contract Rules

- A contract must reference one approved Purchase Request.
- A contract must reference one Supplier.
- A high-risk or suspended Supplier should not receive a new active contract.
- Legal approval is required before activation.
- Business policy says the contract is active only after legal approval and signature by both parties.
- Contract amount should normally equal the approved purchase request amount unless procurement documents a split award.
- Terminated contracts must include a termination reason.

## Contract Events

- Contract Drafted
- Contract Submitted for Legal Review
- Contract Legal Approved
- Contract Activated
- Contract Expired
- Contract Terminated
