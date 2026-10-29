# Store

Documentation for Business Object record [`objects:object-retail-store-6kzkfj`](objects-object-retail-store-6kzkfj.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `retail` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-retail-store-6kzkfj` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A physical outlet where the enterprise offers goods to customers. The Store is the customer-facing location of a retail lens: replenishment, sales, and inventory processes operate in it, and its performance is measured as a unit.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `location` | Kind of thing the business cares about |
| `object_subclass` | `retail-store` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-facility-management-tx73hb`

### Processes involved

- `processes:process-eo-operate-zwzmbd`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
