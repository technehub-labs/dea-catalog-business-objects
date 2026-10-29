# Configuration Item

Documentation for Business Object record [`objects:object-configuration-item-tsn3ex`](objects-object-configuration-item-tsn3ex.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** dominant-stage — principally managed at `operate` (BO-STG-01).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-configuration-item-tsn3ex` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | enablement-operations · operate |
| Admitted by | [CR-BO-14](../../../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) (2026-10-30) |

## Definition

Any component under formal change control that supports a technology service: middleware, network segments, runbooks, integrations, and the deployed artifacts not already modeled as Application or Environment. The Configuration Item is the unit of change-control traceability: a change to it is governed, recorded, and reversible, and its relationships to other items underpin impact analysis.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `configuration-item` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-security-management-wmzc7c`

### Processes involved

- `processes:process-eo-operate-4njp7b`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-14) in the `operate` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-14; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (AC-08 stage coherence). Version integrity is enforced by the VER-001..003 gate (CR-BO-13).
