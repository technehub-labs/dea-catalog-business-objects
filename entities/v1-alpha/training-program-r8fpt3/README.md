# Training Program

Documentation for Business Object record [`objects:object-training-program-r8fpt3`](objects-object-training-program-r8fpt3.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the `build` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-training-program-r8fpt3` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | agency-organization · build |
| Admitted by | [CR-BO-12](../../../change-requests/CR-BO-12-sixth-admission-build-activate.md) (2026-10-30) |

## Definition

A structured development effort that builds workforce or agent capability: curriculum, cohorts, and completion criteria. The Training Program is stage-native to build — its output is competence, and it closes when the cohort is qualified.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `training-program` | Refinement under the class |
| `ecf_domain` | `agency-organization` | Universal ECF domain coordinate |
| `ecf_stage` | `build` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-workforce-planning-b43rhm`

### Processes involved

- `processes:process-ao-build-w2qurd`
- `processes:process-ao-build-9my4jr`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-12) in the `build` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-12 per the CR-BO-10 scope continuation (BO-STG-01); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
