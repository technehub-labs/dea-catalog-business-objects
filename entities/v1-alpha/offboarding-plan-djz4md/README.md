# Offboarding Plan

Documentation for Business Object record [`objects:object-offboarding-plan-djz4md`](objects-object-offboarding-plan-djz4md.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the ` retire` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-offboarding-plan-djz4md` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | party-relationship · retire |
| Admitted by | [CR-BO-11](../../../change-requests/CR-BO-11-fifth-admission-stage-native.md) (2026-10-30) |

## Definition

The managed exit of a party relationship: obligations settled, access withdrawn, data retained or erased on terms, and the relationship closed deliberately. The Offboarding Plan is stage-native to retire — it exists to make the exit orderly rather than accidental.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `offboarding-plan` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | ` retire` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb`

### Processes involved

- `processes:process-pr-retire-bd3asa`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-11) in the ` retire` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-11 per the CR-BO-10 scope (§5 decisions: BO-STG-01 adopted, all five candidates, `Candidate` naming); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and each record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
