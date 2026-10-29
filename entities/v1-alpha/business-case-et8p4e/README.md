# Business Case

Documentation for Business Object record [`objects:object-business-case-et8p4e`](objects-object-business-case-et8p4e.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the ` conceive` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-business-case-et8p4e` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | strategy-direction · conceive |
| Admitted by | [CR-BO-11](../../../change-requests/CR-BO-11-fifth-admission-stage-native.md) (2026-10-30) |

## Definition

The structured justification for a commitment: outcomes, costs, risks, and alternatives, framed so a decision can be taken. The Business Case is stage-native to conceive — it exists to justify a decision and is closed when the decision is taken, leaving only its lessons.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `business-case` | Refinement under the class |
| `ecf_domain` | `strategy-direction` | Universal ECF domain coordinate |
| `ecf_stage` | ` conceive` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-strategic-planning-k3rz7a`

### Processes involved

- `processes:process-sd-conceive-xa4h2k`
- `processes:process-sd-conceive-ahwvp5`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-11) in the ` conceive` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-11 per the CR-BO-10 scope (§5 decisions: BO-STG-01 adopted, all five candidates, `Candidate` naming); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and each record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
