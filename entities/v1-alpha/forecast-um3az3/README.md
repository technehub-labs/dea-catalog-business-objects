# Forecast

Documentation for Business Object record [`objects:object-forecast-um3az3`](objects-object-forecast-um3az3.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-forecast-um3az3` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | finance-accounting · operate |
| Admitted by | [CR-BO-09](../../../change-requests/CR-BO-09-fourth-admission-t3-ready.md) (2026-10-30) |

## Definition

A forward-looking estimate of financial position and performance over a horizon, distinct from the Budget's authority: the Forecast predicts; the Budget permits. The Forecast is revised continuously as actuals land, and its divergence from the Budget is a steering signal.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | Kind of thing the business cares about |
| `object_subclass` | `forecast` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-enterprise-performance-management-5fxren`

### Processes involved

- `processes:process-fa-build-92v24c`
- `processes:process-fa-operate-ycba3k`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-09); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-09 per the CR-BO-06 wave-2 scope (T3-ready candidates); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
