# Goal

Documentation for Business Object record [`objects:object-goal-h2zfhv`](objects-object-goal-h2zfhv.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-goal-h2zfhv` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | strategy-direction · operate |
| Admitted by | [CR-BO-09](../../../change-requests/CR-BO-09-fourth-admission-t3-ready.md) (2026-10-30) |

## Definition

A deliberate outcome the enterprise commits to achieve over a horizon, expressed so that progress can be steered and measured. The Goal is the steering object of the strategy-direction domain: strategic planning frames it, initiative steering tracks it, and the Initiative/Project portfolio executes toward it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `strategic-goal` | Refinement under the class |
| `ecf_domain` | `strategy-direction` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-enterprise-performance-management-5fxren`

### Processes involved

- `processes:process-sd-operate-u6xgu5`
- `processes:process-sd-operate-zdjchn`
- `processes:process-sd-operate-ucxpz4`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-09); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-09 per the CR-BO-06 wave-2 scope (T3-ready candidates); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
