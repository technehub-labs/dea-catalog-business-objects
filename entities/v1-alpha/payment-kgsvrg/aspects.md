# Payment — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-payment-kgsvrg`](objects-object-payment-kgsvrg.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Payment is

- **Kind:** a *financial-instrument* — but with a distinctly **transactional character** compared to its sibling Invoice: a Payment is an *event of value transfer*, not a standing claim. It is created, applied, and cleared in quick succession.
- **Subclass:** *customer-payment* — money flowing **inbound** (customer → enterprise). Together with *billing-invoice* (claim created) and *disbursement-grant* (money outbound), it completes the three money directions of the seed set.
- **Allocation semantics:** the defining behavior is *application* — one Payment may settle several Invoices, and one Invoice may be settled by several partial Payments (a many-to-many allocation).

## Relational aspect — closing order-to-cash

```
 Order ──► Invoice ──settled by──► PAYMENT
                                     ▲
 Customer ───────────────────────────┘ (payer)
```

The Payment is the **only object that converts receivables into cash**. It is also the reconciliation point between:

- accrual accounting (revenue recognized at Invoice),
- cash accounting (value realized at Payment), and
- treasury operations (cash positions, bank reconciliation).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `received → applied → cleared → reconciled` (plus `partially-applied`, `refunded`) |

`reconciled` — matching the bank's view of the cash movement to the enterprise's books — is the true terminus; an unreconciled payment is an open operational item even after application.

## Operational aspect — acting on the object

- **Created by:** payment capture (bank feed, gateway, manual entry).
- **Read by:** cash application, receivables aging, treasury positions, forecasting.
- **Updated by:** allocation to invoices, reversals, refunds, reconciliation matches.
- **Completed by:** reconciliation, after which it is accounting evidence.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** the financial-resource-management capability was resolved against the live capabilities catalog before landing; owner/stakeholders/events remain unset per IDM-003.
- **Content-addressing:** the `kgsvrg` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).
- **Financial audit:** like the Invoice, the Payment is accounting evidence; its `state_history` and `provenance.change_history` are the audit trail.

## Measurement aspect (indicative KPIs a Payment-type BO supports)

- Collections: cash received vs. invoiced (collection effectiveness index)
- DSO reduction: Invoice date → Payment clearing date
- Unapplied/unallocated cash (received but not yet applied to invoices)
- Payment-method mix and failed/reversed payment rates
