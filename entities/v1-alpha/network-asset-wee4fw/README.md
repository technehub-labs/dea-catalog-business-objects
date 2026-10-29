# Network Asset

Documentation for Business Object record [`objects:object-network-asset-wee4fw`](objects-object-network-asset-wee4fw.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-network-asset-wee4fw` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | enablement-operations · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

A physical or logical component of the operator's network that carries or enables service: radio units, transmission links, switches, and the logical capacity they provide. The Network Asset is the capacity resource of a telecom lens — maintained as an asset, loaded by service instances, and its utilization and coverage drive both investment and quality.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `resource` | Kind of thing the business cares about |
| `object_subclass` | `network-asset` | Refinement under the class |
| `ecf_domain` | `enablement-operations` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-asset-management-judtwr`
- `capabilities:capability-operations-management-pm3w8k`

### Processes involved

- `processes:process-eo-operate-j9cjzz`
- `processes:process-eo-improve-q58ecg`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
