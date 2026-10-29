# Tax Record

Documentation for Business Object record [`objects:object-tax-record-zwqfpa`](objects-object-tax-record-zwqfpa.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (statutory obligations are universal) (CR-BO-06 §6.3 explicit-lens convention).

## Identity

| Field | Value |
|---|---|
| id | `objects:object-tax-record-zwqfpa` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | finance-accounting · operate |
| Admitted by | [CR-BO-09](../../../change-requests/CR-BO-09-fourth-admission-t3-ready.md) (2026-10-30) |

## Definition

A filing, position, or obligation record under tax law: returns, assessments, rulings, and supporting positions. The Tax Record is the compliance instrument of the tax function: tax strategy frames it, compliance processes file and defend it, and its errors carry statutory consequence.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | Kind of thing the business cares about |
| `object_subclass` | `tax-record` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-regulation-management-gya4d8`

### Processes involved

- `processes:process-fa-operate-8vqvkk`
- `processes:process-fa-design-ds4drw`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-09); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-09 per the CR-BO-06 wave-2 scope (T3-ready candidates); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
