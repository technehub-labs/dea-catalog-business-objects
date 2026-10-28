# Payment

Documentation for Business Object record [`objects:object-payment-kgsvrg`](objects-object-payment-kgsvrg.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-payment-kgsvrg` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A transfer of value from a customer to the enterprise settling one or more Invoices. The Payment closes the order-to-cash loop: it reduces receivables, updates cash positions, and is the cash realization of the enterprise's value exchange.

## Business role

The Payment is the **terminal event of order-to-cash** — the moment the enterprise actually gets paid:

- It settles one or more **Invoices**, reducing or extinguishing the receivable.
- It is made by the **Customer**, closing the loop that began with their intent.
- It updates cash positions — the bridge from accrual-accounting reality (Invoice) to cash reality.

Without the Payment, the chain would be a record of claims; with it, value exchange is *realized*.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | A value-bearing financial artifact |
| `object_subclass` | `customer-payment` | The inbound settlement instrument (vs. billing invoices, grants) |
| `ecf_domain` | `finance-accounting` | Finance-and-Accounting domain |
| `ecf_stage` | `operate` | Operated in steady-state financial operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c` — financial resource management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Invoice](../invoice-z3fwgb/README.md) | The Payment settles Invoices | Payment → Invoice (settles) |
| [Customer](../customer-2qvphc/README.md) | The Customer is the payer | Customer → Payment (payer) |
| [Order](../order-bpy4g4/README.md) | The Payment cash-realizes an Order's commitment | Order ⇢ Payment (via Invoice) |
| [Grant](../grant-nhdwg9/README.md) | The opposite direction of funds: outbound vs. inbound | Payment ↔ Grant (in/out pair) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `received → applied → cleared → reconciled`, with partial-application and refund paths, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- When and how much cash entered the enterprise, against which receivables?
- Which invoices remain open, partially settled, or fully settled?
- How long is the issue-to-cash window (Invoice date → Payment date)?
- What are payment-method and settlement-pattern trends by customer segment?
