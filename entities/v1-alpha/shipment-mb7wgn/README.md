# Shipment

Documentation for Business Object record [`objects:object-shipment-mb7wgn`](objects-object-shipment-mb7wgn.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-shipment-mb7wgn` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

The movement of goods from the enterprise to a customer or between enterprise locations under a fulfilment commitment. The Shipment carries the physical leg of the order-to-cash chain and is tracked by logistics and warehouse processes.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `shipment` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
