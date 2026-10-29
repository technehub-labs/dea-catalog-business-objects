# Subscriber

Documentation for Business Object record [`objects:object-subscriber-muj94k`](objects-object-subscriber-muj94k.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-subscriber-muj94k` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | party-relationship · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

A party holding an active service subscription with the operator: the contract-bound user of communications services, distinct from the commercial Customer who may be the payer. The Subscriber is the demand-side party of a telecom lens: subscription, activation, usage, and retention processes act on it, and its service instances and usage records attach to it.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `party` | Kind of thing the business cares about |
| `object_subclass` | `subscriber` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb`

### Processes involved

- `processes:process-pr-operate-bbe384`
- `processes:process-pr-activate-6qzuve`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
