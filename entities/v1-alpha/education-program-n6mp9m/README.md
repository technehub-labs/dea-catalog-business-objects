# Study Program

Documentation for Business Object record [`objects:object-education-program-n6mp9m`](objects-object-education-program-n6mp9m.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `education` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-education-program-n6mp9m` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `product-value` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A structured program of study the enterprise offers to learners, leading to a qualification or outcome. The Study Program is the curriculum offering of an education lens: program design, catalogue publication, and portfolio rationalization processes act on it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | Kind of thing the business cares about |
| `object_subclass` | `education-program` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`

### Processes involved

- `processes:process-pv-operate-zyguzp`
- `processes:process-pv-improve-9xvgat`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
