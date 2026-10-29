# Citizen

Documentation for Business Object record [`objects:object-citizen-2xqsse`](objects-object-citizen-2xqsse.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `government` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-citizen-2xqsse` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `party-relationship` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

An individual in the jurisdiction the enterprise serves. The Citizen is the public-sector counterpart of the Customer: service intake, case, and benefit processes create and update it, and party-management capabilities act on it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | Kind of thing the business cares about |
| `object_subclass` | `citizen` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb`

### Processes involved

- (none yet; natural process anchors are not yet present in the processes catalog — populated in a follow-up sweep per IDM-003)

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
