# Machine

Documentation for Business Object record [`objects:object-production-machine-j5z9kv`](objects-object-production-machine-j5z9kv.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `manufacturing` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-production-machine-j5z9kv` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A durable physical asset that performs production operations. The Machine is the capacity resource of a manufacturing lens: production scheduling and asset-maintenance processes operate on it, and it is capitalized as an Asset.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `resource` | Kind of thing the business cares about |
| `object_subclass` | `production-machine` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-asset-management-judtwr`
- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-j9cjzz`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
