# Procurement Process

## Purchase Request Creation

A requester creates a Purchase Request with a title, department, expected amount, required date, business justification, and at least one line item. A draft request may be edited by the requester.

## Purchase Request Status Flow

```text
DRAFT -> SUBMITTED -> APPROVED
DRAFT -> SUBMITTED -> REJECTED
DRAFT -> CANCELLED
REJECTED -> SUBMITTED
```

`APPROVED` and `CANCELLED` are terminal for the purchase request process.

## Approval Flow

- A Purchase Request under 50000 CNY requires department manager approval.
- A Purchase Request greater than or equal to 50000 CNY requires department manager approval and finance manager approval.
- A rejected request must include a rejection reason.
- A cancelled request must include a cancellation reason.

## Supplier Selection

Procurement may use a preferred Supplier from the Purchase Request, but must confirm that the Supplier is active and not high risk before award. Some technical notes use Vendor to mean Supplier.

## Purchase Order Release

A Purchase Order can be released only after the related contract is active. One Purchase Request may lead to one or more Purchase Orders if delivery is split.
