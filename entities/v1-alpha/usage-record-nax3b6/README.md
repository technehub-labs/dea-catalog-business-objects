# Usage Record

Documentation for Business Object record [`objects:object-usage-record-nax3b6`](objects-object-usage-record-nax3b6.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-usage-record-nax3b6` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | finance-accounting · operate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

A metered event of service consumption: a call detail record, data session, or message event with parties, duration, volume, and tariff basis. The Usage Record is the metering transaction of a telecom lens — generated in service delivery, aggregated and rated, and the atomic input to billing and interconnect settlement.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `transaction` | Kind of thing the business cares about |
| `object_subclass` | `usage-record` | Refinement under the class |
| `ecf_domain` | `finance-accounting` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-resource-management-cd3c7c`

### Processes involved

- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-sdppmp`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
