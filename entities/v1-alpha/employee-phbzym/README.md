# Employee

Documentation for Business Object record [`objects:object-employee-phbzym`](objects-object-employee-phbzym.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-employee-phbzym` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `party-relationship` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

An individual engaged by the enterprise under an employment relationship. The Employee is the workforce party: hiring, payroll, time, and development processes create and update it, and workforce capabilities act on it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | Kind of thing the business cares about |
| `object_subclass` | `employee` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-workforce-management-9e8d8s`

### Processes involved

- `processes:process-ao-operate-38qyc6`
- `processes:process-fa-operate-zpmxzp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
