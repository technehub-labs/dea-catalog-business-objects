# Payment

Documentation for Business Object record [`objects:object-payment-kgsvrg`](objects-object-payment-kgsvrg.yaml).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-payment-kgsvrg` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A transfer of value from a customer to the enterprise settling one or more Invoices. The Payment closes the order-to-cash loop: it reduces receivables, updates cash positions, and is the cash realization of the enterprise's value exchange.

## Classification

| Axis | Value |
|---|---|
| `object_class` | `financial-instrument` |
| `object_subclass` | `customer-payment` |
| `ecf_domain` | `finance-accounting` |
| `ecf_stage` | `operate` |
| `current_state` | `active` |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c` — financial resource management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |
