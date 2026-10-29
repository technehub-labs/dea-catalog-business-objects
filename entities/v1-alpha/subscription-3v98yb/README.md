# Subscription

Documentation for Business Object record [`objects:object-subscription-3v98yb`](objects-object-subscription-3v98yb.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-subscription-3v98yb` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `product-value` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

An offering arrangement in which the customer receives continuing access to products or services for a recurring charge over an agreed term. The Subscription converts the one-time sale into an entitlement relationship that renewal and billing processes operate on.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | Kind of thing the business cares about |
| `object_subclass` | `subscription-plan` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`

### Processes involved

- `processes:process-pv-operate-cau4gv`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
