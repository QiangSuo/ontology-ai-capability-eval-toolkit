# Business Rules

## Purchase Request Rules

- A Purchase Request must have at least one line item before submission.
- A business justification is required before submission.
- The request amount must be non-negative.
- Approved Purchase Requests cannot be cancelled by a normal requester.
- Rejected requests may be revised and resubmitted.

## Approval Rules

- Requests less than 50000 CNY require Department Manager approval.
- Requests greater than or equal to 50000 CNY require Finance Manager approval after Department Manager approval.
- Rejection comments should explain the reason.

## Supplier Rules

- A Supplier must be active before award.
- High-risk suppliers should not be selected for new contracts.
- Suspended suppliers must not receive purchase orders.

## Contract Rules

- A Contract requires legal approval before activation.
- A Contract should not be active before both parties sign.
- A terminated Contract must have a termination reason.

## Purchase Order Rules

- A Purchase Order can be released only for an active Contract.
- A Purchase Order may be closed after complete goods receipt or after procurement admin review.

## Invoice and Payment Rules

- Invoice matching compares invoice amount to purchase order amount and receiving evidence.
- Business policy allows invoice variance up to 2% of the Purchase Order amount.
- A Payment Application can be approved only when the related Invoice is matched.
- Paid payment applications must store paid time.
