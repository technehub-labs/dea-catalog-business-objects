# Project

Documentation for Business Object record [`objects:object-project-5hgzd3`](objects-object-project-5hgzd3.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-project-5hgzd3` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `agency-organization` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

A temporary endeavor undertaken by the enterprise to create a change within constraints of scope, time, and resources. The Project is the delivery vehicle of choice for non-routine work: it is chartered, planned, executed, and closed, and it consumes resources the permanent organization provides.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `work-item` | Kind of thing the business cares about |
| `object_subclass` | `project` | Refinement under the class |
| `ecf_domain` | `agency-organization` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-strategic-planning-k3rz7a`

### Processes involved

- `processes:process-sd-operate-u6xgu5`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
