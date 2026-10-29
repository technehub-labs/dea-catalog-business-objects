# Environment

Documentation for Business Object record [`objects:object-environment-npd5vt`](objects-object-environment-npd5vt.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-environment-npd5vt` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

A configured deployment context in which applications run, such as production, staging, or testing. The Environment separates run-states of the same technology so change can be promoted safely, and platform operations processes keep it provisioned and healthy.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `environment` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-technology-enablement-y6nkws`

### Processes involved

- `processes:process-eo-operate-4njp7b`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
