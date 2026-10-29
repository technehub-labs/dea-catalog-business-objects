# Bill of Material

Documentation for Business Object record [`objects:object-bill-of-material-9skzte`](objects-object-bill-of-material-9skzte.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `manufacturing` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-bill-of-material-9skzte` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

The structured list of components and quantities required to make a product. The Bill of Material is the composition resource of a manufacturing lens: production planning and execution processes read it, and engineering-change processes revise it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `resource` | Kind of thing the business cares about |
| `object_subclass` | `bill-of-material` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-operate-xud3hs`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
