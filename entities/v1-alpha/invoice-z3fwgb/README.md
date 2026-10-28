# Invoice

Documentation for Business Object record [`objects:object-invoice-z3fwgb`](objects-object-invoice-z3fwgb.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-invoice-z3fwgb` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A commercial document issued by the enterprise to a customer, itemizing products or services delivered and demanding payment. The Invoice is the financial counterpart of the Order: it converts fulfilled commitments into receivables and drives revenue recognition and collections.

## Business role

The Invoice is where **operations become accounting**. Up to the Invoice, the chain is operational (intent, commitment, delivery); from the Invoice onward, it is financial (receivable, revenue, cash):

- It converts a fulfilled **Order** into an amount owed by the **Customer**.
- It creates the receivable that the **Payment** will later settle.
- It is the trigger for revenue recognition and the basis of collections activity.

Together with Payment and Grant, it forms the finance-accounting trio of the seed set: money demanded inbound (Invoice), money received (Payment), money disbursed outbound (Grant).

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | A value-bearing financial artifact |
| `object_subclass` | `billing-invoice` | The demand-for-payment instrument (vs. payments, grants) |
| `ecf_domain` | `finance-accounting` | Finance-and-Accounting domain |
| `ecf_stage` | `operate` | Operated in steady-state financial operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c` — financial resource management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-financial-stewardship-c7xtfk` — financial stewardship ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Order](../order-bpy4g4/README.md) | The Invoice bills a fulfilled Order | Order → Invoice (billed from) |
| [Customer](../customer-2qvphc/README.md) | The Invoice demands payment from the Customer | Customer → Invoice (billed party) |
| [Payment](../payment-kgsvrg/README.md) | Payments settle Invoices | Payment → Invoice (settles) |
| [Grant](../grant-nhdwg9/README.md) | The outbound counterpart: money given rather than demanded | Invoice ↔ Grant (inbound/outbound pair) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `issued → due → overdue → partially-paid → settled → written-off`, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- What does the enterprise's receivable stock look like (issued, due, overdue, written off)?
- Which orders and customers generated which revenue demands?
- How fast do invoices convert to cash (with Payment closing the loop)?
- What is recognized as revenue, grounded in fulfilled commitments?
