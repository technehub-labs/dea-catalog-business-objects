# Service Number

Documentation for Business Object record [`objects:object-service-number-6axyb2`](objects-object-service-number-6axyb2.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-service-number-6axyb2` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | governance-existence · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

A subscriber-facing identifier allocated to a subscriber or service: a directory number or its equivalent addressing resource. The Service Number is the addressing resource of a telecom lens — allocated from regulator-governed numbering ranges, portable between operators, and attached to exactly one subscriber at a time.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `resource` | Kind of thing the business cares about |
| `object_subclass` | `service-number` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-information-management-6vjgdh`

### Processes involved

- `processes:process-ge-operate-hs7wf3`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
