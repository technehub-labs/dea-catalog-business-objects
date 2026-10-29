# Incident

Documentation for Business Object record [`objects:object-incident-wudf9s`](objects-object-incident-wudf9s.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-incident-wudf9s` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

An unplanned interruption or degradation of a technology service. The Incident is the operational exception object of technology management: it is detected, triaged, worked to restoration, and analyzed afterward for recurrence prevention.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `service-incident` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-continuity-management-v3rn6u`

### Processes involved

- `processes:process-eo-operate-4njp7b`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
