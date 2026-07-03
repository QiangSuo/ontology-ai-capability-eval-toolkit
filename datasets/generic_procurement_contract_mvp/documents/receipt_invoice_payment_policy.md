# Receipt, Invoice, and Payment Policy

## Goods Receipt

Warehouse users record Goods Receipt when goods or services are delivered. Warehouse teams often call this record a GRN.

Goods Receipt status flow:

```text
PENDING -> PARTIAL -> COMPLETE
PENDING -> REJECTED
PARTIAL -> COMPLETE
```

A complete receipt should include received time, receiver, and inspection result.

## Invoice Matching

Accounts payable matches Invoice against Purchase Order and Goods Receipt.

Invoice status flow:

```text
PENDING_MATCH -> MATCHED
PENDING_MATCH -> EXCEPTION
EXCEPTION -> MATCHED
PENDING_MATCH -> CANCELLED
```

Invoice matching policy:

- An invoice should not be paid before matching.
- A matched invoice must reference a Purchase Order.
- A matched goods invoice should reference a Goods Receipt.
- The allowed invoice variance is 2% of the Purchase Order amount unless finance grants an exception.

## Payment Application

Finance users may call Payment Request a Payment Application.

Payment status flow:

```text
REQUESTED -> APPROVED -> PAID
REQUESTED -> HELD
HELD -> APPROVED
REQUESTED -> CANCELLED
```

Payment rules:

- A Payment Request can be created only for a matched Invoice.
- Payment approval is performed by Finance Manager.
- Paid requests must have paid time.
- Held payment requires a hold reason in operational notes, although the MVP table stores only status.
