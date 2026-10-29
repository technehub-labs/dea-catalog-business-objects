# Service

Documentation for Business Object record [`objects:object-service-q8w4ce`](objects-object-service-q8w4ce.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-service-q8w4ce` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `product-value` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

An intangible offering the enterprise delivers to the market as an activity performed for the customer rather than a good transferred to the customer. The Service is catalogued and delivered alongside the Product, and offering management capabilities act on it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | Kind of thing the business cares about |
| `object_subclass` | `service` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`

### Processes involved

- `processes:process-pv-operate-zyguzp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
