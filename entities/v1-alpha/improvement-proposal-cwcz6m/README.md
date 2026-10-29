# Improvement Proposal

Documentation for Business Object record [`objects:object-improvement-proposal-cwcz6m`](objects-object-improvement-proposal-cwcz6m.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native — this type exists only within the `improve` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-improvement-proposal-cwcz6m` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | enablement-operations · improve |
| Admitted by | [CR-BO-14](../../../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) (2026-10-30) |

## Definition

A structured proposal to change a process, asset, or platform for the better: problem statement, options, expected benefit, and effort. The Improvement Proposal is stage-native to improve — it is the decision artifact of improvement programs, converting insight and ideas into a fundable change, and it closes into a Project or is rejected.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `improvement-proposal` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `improve` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-improve-us272s`
- `processes:process-fa-improve-emqpgr`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-14) in the `improve` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-14; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (AC-08 stage coherence). Version integrity is enforced by the VER-001..003 gate (CR-BO-13).
