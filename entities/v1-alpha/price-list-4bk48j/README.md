# Price List

Documentation for Business Object record [`objects:object-price-list-4bk48j`](objects-object-price-list-4bk48j.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-price-list-4bk48j` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `product-value` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

The structured set of prices at which the enterprise offers its products and services, scoped by market, channel, segment, or agreement. The Price List governs quote and order pricing and is maintained through catalogue and proposition lifecycle processes.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | Kind of thing the business cares about |
| `object_subclass` | `price-list` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-marketing-xmc539`

### Processes involved

- `processes:process-pv-operate-zyguzp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
