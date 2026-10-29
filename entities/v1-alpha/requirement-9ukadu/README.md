# Requirement

Documentation for Business Object record [`objects:object-requirement-9ukadu`](objects-object-requirement-9ukadu.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the ` design` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-requirement-9ukadu` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | product-value · design |
| Admitted by | [CR-BO-11](../../../change-requests/CR-BO-11-fifth-admission-stage-native.md) (2026-10-30) |

## Definition

A specification of what an offering or feature must satisfy: a statement of need with acceptance criteria, traceable to its origin and to the thing that will satisfy it. The Requirement is stage-native to design — it is superseded by the built thing it specifies.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `requirement` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | ` design` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-technology-management-maus5n`

### Processes involved

- `processes:process-pv-design-8v4k89`
- `processes:process-pv-design-a4c76s`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-11) in the ` design` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-11 per the CR-BO-10 scope (§5 decisions: BO-STG-01 adopted, all five candidates, `Candidate` naming); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and each record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
