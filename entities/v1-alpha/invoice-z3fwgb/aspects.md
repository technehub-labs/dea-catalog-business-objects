# Invoice — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-invoice-z3fwgb`](objects-object-invoice-z3fwgb.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing an Invoice is

- **Kind:** a *financial-instrument* — an artifact that carries monetary claims. It is created deliberately, has legal/commercial force, and terminates when settled or written off.
- **Subclass:** *billing-invoice* — the demand-side instrument. Its sibling subclasses in the seed set are *customer-payment* (inbound settlement) and *disbursement-grant* (outbound giving); together the three cover the money-in / money-settled / money-out directions.
- **Document character:** it is both a *record* (evidence of what was delivered and priced) and a *claim* (an amount owed by a specific party).

## Relational aspect — the operations/accounting boundary

```
 Order ──fulfilled──► INVOICE ──settled by──► Payment
                        ▲
 Customer ──────────────┘ (billed party)
```

The Invoice is the **hinge between the operational chain and the financial chain**:

- Upstream it references operational reality (what was ordered, delivered, to whom).
- Downstream it creates financial reality (receivable, revenue recognition, dunning).

Removing the Invoice would break order-to-cash accounting: Orders would be operational facts with no monetary claim attached.

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `issued → due → overdue → partially-paid → settled → written-off` |

The `settled` state is the normal terminus — reached when Payments fully cover the invoiced amount; `written-off` is the exception terminus for uncollectible claims.

## Operational aspect — acting on the object

- **Created by:** billing processes when fulfilment is confirmed (invoice issue).
- **Read by:** receivables management, revenue recognition, credit control, collections.
- **Updated by:** payment application, credit notes, adjustments, dunning stages.
- **Completed by:** settlement or write-off, after which the record persists as accounting evidence.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** both financial capabilities were resolved against the live capabilities catalog before landing; owner/stakeholders/events remain unset per IDM-003.
- **Content-addressing:** the `z3fwgb` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).
- **Audit weight:** as an accounting artifact, the Invoice carries the heaviest evidentiary expectations of the seed set — its `state_history` and `provenance.change_history` are the audit trail.

## Measurement aspect (indicative KPIs an Invoice-type BO supports)

- Receivables stock and aging (current, 30/60/90+, written-off)
- DSO (days sales outstanding): issue → settlement
- Billing accuracy: credit notes and adjustments as a share of invoice volume
- Collection effectiveness: overdue share and dunning conversion
