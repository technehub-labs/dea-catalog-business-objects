# Case

Documentation for Business Object record [`objects:object-public-case-ae4yg8`](objects-object-public-case-ae4yg8.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `government` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-public-case-ae4yg8` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `governance-existence` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A matter opened by the enterprise on behalf of a party and tracked to a determination. The Case is the service-matter transaction of a public-sector lens: intake, investigation, decision, and closure processes create and update it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `public-case` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-legal-matter-management-zzbd2u`

### Processes involved

- `processes:process-ge-operate-hs7wf3`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
