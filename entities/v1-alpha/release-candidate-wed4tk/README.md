# Release Candidate

Documentation for Business Object record [`objects:object-release-candidate-wed4tk`](objects-object-release-candidate-wed4tk.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the `build` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-release-candidate-wed4tk` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | enablement-operations · build |
| Admitted by | [CR-BO-12](../../../change-requests/CR-BO-12-sixth-admission-build-activate.md) (2026-10-30) |

## Definition

A build of an application or service proposed for release: feature-complete, under verification, and not yet authorized for production. The Release Candidate is stage-native to build — it exists to be proven, and its terminal transitions are promotion to release or rejection back to development.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `release-candidate` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `build` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-technology-enablement-y6nkws`

### Processes involved

- `processes:process-eo-build-nmmmt6`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-12) in the `build` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-12 per the CR-BO-10 scope continuation (BO-STG-01); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
