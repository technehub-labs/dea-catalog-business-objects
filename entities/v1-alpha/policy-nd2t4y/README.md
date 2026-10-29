# Policy

Documentation for Business Object record [`objects:object-policy-nd2t4y`](objects-object-policy-nd2t4y.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-policy-nd2t4y` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `governance-existence` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

A deliberate statement of the enterprise's chosen position on a matter, binding on those it covers. The Policy is the enterprise governing itself: policies are adopted, communicated, and their compliance is audited, and they bound the decisions the enterprise may take.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `legal-instrument` | Kind of thing the business cares about |
| `object_subclass` | `policy` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-regulation-management-gya4d8`

### Processes involved

- `processes:process-ge-operate-hxxyc9`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
