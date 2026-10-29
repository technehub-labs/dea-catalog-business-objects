# Transformation Plan

Documentation for Business Object record [`objects:object-transformation-plan-mpsz65`](objects-object-transformation-plan-mpsz65.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** dominant-stage — steered throughout its life; principally managed at `operate` (BO-STG-01).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-transformation-plan-mpsz65` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | strategy-direction · operate |
| Admitted by | [CR-BO-14](../../../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) (2026-10-30) |

## Definition

A multi-year, portfolio-level vehicle that sequences initiatives toward a strategic target state. The Transformation Plan sits between the Goal (the committed outcome) and the Projects (the executions): it converts intent into a staged roadmap with dependencies, funding phases, and checkpoints, and is steered throughout its life.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `transformation-plan` | Refinement under the class |
| `ecf_domain` | `strategy-direction` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-enterprise-performance-management-5fxren`

### Processes involved

- `processes:process-sd-operate-u6xgu5`
- `processes:process-sd-build-7n4prh`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-14) in the `operate` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-14; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (AC-08 stage coherence). Version integrity is enforced by the VER-001..003 gate (CR-BO-13).
