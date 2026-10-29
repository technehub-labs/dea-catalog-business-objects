# Candidate

Documentation for Business Object record [`objects:object-candidate-party-s8q2mk`](objects-object-candidate-party-s8q2mk.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the ` conceive` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-candidate-party-s8q2mk` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | party-relationship · conceive |
| Admitted by | [CR-BO-11](../../../change-requests/CR-BO-11-fifth-admission-stage-native.md) (2026-10-30) |

## Definition

A prospective party under evaluation before it becomes a Customer, Supplier, Member, or Partner. The Candidate is stage-native to conceive — acquisition and qualification processes work it, and its outcome is conversion into a role party or rejection.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | Kind of thing the business cares about |
| `object_subclass` | `candidate-party` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | ` conceive` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb`

### Processes involved

- `processes:process-pr-conceive-emfgju`
- `processes:process-pr-conceive-tvst8u`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-11) in the ` conceive` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-11 per the CR-BO-10 scope (§5 decisions: BO-STG-01 adopted, all five candidates, `Candidate` naming); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and each record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
