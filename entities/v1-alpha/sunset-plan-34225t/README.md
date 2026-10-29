# Sunset Plan

Documentation for Business Object record [`objects:object-sunset-plan-34225t`](objects-object-sunset-plan-34225t.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the ` retire` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-sunset-plan-34225t` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | product-value · retire |
| Admitted by | [CR-BO-11](../../../change-requests/CR-BO-11-fifth-admission-stage-native.md) (2026-10-30) |

## Definition

The managed exit of an offering: migration paths for existing customers, run-off of inventory and commitments, and communication of the withdrawal. The Sunset Plan is stage-native to retire — it converts an offering's end from a cliff into a slope.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `sunset-plan` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | ` retire` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`

### Processes involved

- `processes:process-pv-retire-6us5am`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-11) in the ` retire` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-11 per the CR-BO-10 scope (§5 decisions: BO-STG-01 adopted, all five candidates, `Candidate` naming); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and each record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
