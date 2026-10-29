# Performance Review

Documentation for Business Object record [`objects:object-performance-review-k3k7n6`](objects-object-performance-review-k3k7n6.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native — this type exists only within the `improve` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-performance-review-k3k7n6` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | strategy-direction · improve |
| Admitted by | [CR-BO-14](../../../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) (2026-10-30) |

## Definition

A periodic, evidence-based assessment of performance against targets, producing conclusions and improvement decisions. The Performance Review is stage-native to improve: it is the moment the enterprise measures itself, and its output feeds strategy adaptation, portfolio rationalization, and control refinement.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `performance-review` | Refinement under the class |
| `ecf_domain` | `strategy-direction` | Universal ECF domain coordinate |
| `ecf_stage` | `improve` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-strategic-planning-k3rz7a`

### Processes involved

- `processes:process-sd-improve-duwd64`
- `processes:process-pv-improve-27r7r7`
- `processes:process-eo-improve-g3ngp3`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-14) in the `improve` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-14; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (AC-08 stage coherence). Version integrity is enforced by the VER-001..003 gate (CR-BO-13).
