# Audit Finding

Documentation for Business Object record [`objects:object-audit-finding-jd44zy`](objects-object-audit-finding-jd44zy.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native — this type exists only within the `improve` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-audit-finding-jd44zy` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | governance-existence · improve |
| Admitted by | [CR-BO-14](../../../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) (2026-10-30) |

## Definition

A documented deficiency or opportunity raised by an audit or governance review, tracked to remediation. The Audit Finding is stage-native to improve: it exists to close a gap between the current and the required state of governance, and its lifecycle runs from observation through remediation to verified closure.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `audit-finding` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `improve` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-enterprise-governance-uas48u`

### Processes involved

- `processes:process-ge-improve-axtq3b`
- `processes:process-ge-improve-mgkw59`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-14) in the `improve` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-14; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (AC-08 stage coherence). Version integrity is enforced by the VER-001..003 gate (CR-BO-13).
