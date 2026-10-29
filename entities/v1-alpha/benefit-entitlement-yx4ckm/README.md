# Benefit

Documentation for Business Object record [`objects:object-benefit-entitlement-yx4ckm`](objects-object-benefit-entitlement-yx4ckm.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** `government` (CR-BO-06 §6.3 explicit-lens convention). The type is universal; the subclass vocabulary carries the industry variant per rule BO-TAX-01.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-benefit-entitlement-yx4ckm` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `finance-accounting` · `operate` |
| Admitted by | [CR-BO-08](../../../change-requests/CR-BO-08-third-admission-wave2-t2.md) (2026-10-30) |

## Definition

A disbursable entitlement a party holds under an eligibility rule. The Benefit is the outbound stewardship instrument of a public-sector lens: eligibility assessment and disbursement processes create and update it, and it executes against a Budget.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `financial-instrument` | Kind of thing the business cares about |
| `object_subclass` | `benefit-entitlement` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-financial-stewardship-c7xtfk`

### Processes involved

- `processes:process-fa-operate-wkqaqp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-08); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-08 per the CR-BO-06 wave-2 scope (T2 tier); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003).
