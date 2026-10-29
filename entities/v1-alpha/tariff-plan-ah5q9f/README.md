# Tariff Plan

Documentation for Business Object record [`objects:object-tariff-plan-ah5q9f`](objects-object-tariff-plan-ah5q9f.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-tariff-plan-ah5q9f` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | product-value · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

The published rate structure under which usage is charged: per-unit prices, bundles, allowances, and zone rules. The Tariff Plan is the pricing offering of a telecom lens — where the Price List carries commercial prices generally, the tariff governs metered usage specifically, and regulator-approved tariffs make it partly non-discretionary.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | Kind of thing the business cares about |
| `object_subclass` | `tariff-plan` | Refinement under the class |
| `ecf_domain` | `product-value` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-regulation-management-gya4d8`

### Processes involved

- `processes:process-pv-operate-zyguzp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
