# SIM Profile

Documentation for Business Object record [`objects:object-sim-profile-ja8k4x`](objects-object-sim-profile-ja8k4x.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** telecom operator / digital service provider (MCSP-aligned) (CR-BO-06 §6.3 explicit-lens convention; MCSP specialization views in the capabilities catalog reference the same lens). Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary; the structure and ECF coordinates are universal.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-sim-profile-ja8k4x` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | party-relationship · activate |
| Admitted by | [CR-BO-15](../../../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) (2026-10-30) |

## Definition

The subscriber-identity module binding a subscription to its security credentials: a physical SIM or embedded profile holding the authentication keys that admit a device to the network. The SIM Profile is the identity-binding control of a telecom lens — issued at activation, bound to one subscriber and one service instance, and replaced or suspended as the subscription moves.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `subscriber-identity-module` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `activate` | Dominant-stage placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-technology-management-maus5n`

### Processes involved

- `processes:process-pr-activate-6qzuve`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-15); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-15; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003; enforced by the XREF gate). Version integrity enforced by the VER gates (CR-BO-13).
