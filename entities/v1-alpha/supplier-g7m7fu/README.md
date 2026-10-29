# Supplier

Documentation for Business Object record [`objects:object-supplier-g7m7fu`](objects-object-supplier-g7m7fu.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-supplier-g7m7fu` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `party-relationship` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

An external party that supplies goods or services to the enterprise. The Supplier is the supply-side counterpart of the Customer: sourcing, procurement, and payment processes create and update it, and supplier management capabilities act on it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | Kind of thing the business cares about |
| `object_subclass` | `supplier` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-sourcing-and-procurement-esucp4`

### Processes involved

- `processes:process-eo-operate-vzcxx7`
- `processes:process-fa-operate-wkqaqp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
