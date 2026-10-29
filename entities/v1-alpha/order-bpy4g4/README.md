# Order

Documentation for Business Object record [`objects:object-order-bpy4g4`](objects-object-order-bpy4g4.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-order-bpy4g4` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A request from a customer for products or services, created at commitment time and fulfilled through the enterprise's execution and fulfilment processes. The Order coordinates delivery, production, and revenue recognition and is the operational commitment of the enterprise to its customer.

## Business role

The Order is the **pivot of order-to-cash**: it converts a Customer's intent into an operational commitment, and everything downstream keys off it:

- Fulfilment processes execute against the Order (deliver, produce, provision).
- The **Invoice** monetizes it — a fulfilled Order becomes a receivable.
- The **Payment** settles the Invoice that the Order generated.
- Revenue recognition traces commitments and deliveries back to Orders.

Unlike the Customer (a party) or the Product (an offering), the Order is a *transaction*: it has a beginning, a fulfilment path, and a terminal state. Its lifecycle is the most state-rich of the seed set.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | An event-like commitment with a stateful lifecycle, not a standing entity |
| `object_subclass` | `sales-order` | The demand-side commercial transaction (vs. purchase orders, work orders) |
| `ecf_domain` | `enablement-operations` | Enablement-and-Operations domain |
| `ecf_stage` | `operate` | Operated in steady-state business operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k` — operations management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-eo-operate-2jnz85` — enablement-operations operate-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-eo-operate-xud3hs` — enablement-operations operate-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Customer](../customer-2qvphc/README.md) | The Customer places the Order | Customer → Order (initiator) |
| [Product](../product-dkf9gb/README.md) | The Order lines reference Products being bought | Order → Product (subject) |
| [Invoice](../invoice-z3fwgb/README.md) | The fulfilled Order is billed via an Invoice | Order → Invoice (billed from) |
| [Payment](../payment-kgsvrg/README.md) | Payment settles the Invoice the Order generated | Order ⇢ Payment (via Invoice) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `draft → placed → confirmed → in-fulfilment → fulfilled → closed`, with cancellation/split paths, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- What has the enterprise committed to deliver, to whom, and by when?
- Which operations capabilities and processes own order fulfilment?
- Which orders are still open, fulfilled, or exception-ridden — the operational worklist?
- How do operational commitments roll up into revenue (via Invoice/Payment)?
