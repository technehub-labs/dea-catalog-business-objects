# Treatment

Documentation for Business Object record [`objects:object-care-encounter-8enzdc`](objects-object-care-encounter-8enzdc.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `healthcare` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-care-encounter-8enzdc` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A clinical interaction between a care provider and a Patient, from admission to discharge. The Treatment is the delivery transaction of a healthcare lens: scheduling, care delivery, and outcome-recording processes create and update it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `care-encounter` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-operate-2jnz85`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
