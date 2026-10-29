# Purchase Order

Documentation for Business Object record [`objects:object-purchase-order-qf4tfa`](objects-object-purchase-order-qf4tfa.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-purchase-order-qf4tfa` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

A commitment from the enterprise to a supplier for goods or services at agreed prices and terms. The Purchase Order is the inbound counterpart of the Order: it drives receiving, and it is the accrual basis for the supplier invoice that follows.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `purchase-order` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-sourcing-and-procurement-esucp4`

### Processes involved

- `processes:process-eo-operate-vzcxx7`
- `processes:process-fa-operate-wkqaqp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
