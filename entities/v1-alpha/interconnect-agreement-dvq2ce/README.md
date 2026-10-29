# Interconnect Agreement

Documentation for Business Object record [`objects:object-interconnect-agreement-dvq2ce`](objects-object-interconnect-agreement-dvq2ce.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-interconnect-agreement-dvq2ce` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | governance-existence · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

The contract between operators governing traffic exchange: termination and transit terms, settlement rates, and technical handover points. The Interconnect Agreement is the carrier-to-carrier instrument of a telecom lens — a partner contract whose settlement runs on usage records, and whose terms are typically notified to the regulator.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `legal-instrument` | Kind of thing the business cares about |
| `object_subclass` | `interconnect-agreement` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-partner-management-cp3vdb`

### Processes involved

- `processes:process-eo-operate-2jnz85`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
