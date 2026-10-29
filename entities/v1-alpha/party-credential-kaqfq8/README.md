# Party Credential

Documentation for Business Object record [`objects:object-party-credential-kaqfq8`](objects-object-party-credential-kaqfq8.yaml) · [Aspects deep-dive](aspects.md)

> **Sector lens:** commercial / for-profit enterprise lens (CR-BO-06 §6.3 explicit-lens convention). **Stage placement:** stage-native per rule BO-STG-01 (CR-BO-10 §2) — this type's whole life is inside the `activate` moment.

## Identity

| Field | Value |
|---|---|
| id | `objects:object-party-credential-kaqfq8` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | party-relationship · activate |
| Admitted by | [CR-BO-12](../../../change-requests/CR-BO-12-sixth-admission-build-activate.md) (2026-10-30) |

## Definition

An issued technical identity bound to a party: account, key, or token that authenticates the party to the enterprise's systems. The Party Credential is stage-native to activate — it is created at provisioning, rotated in service, and revoked at exit.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | Kind of thing the business cares about |
| `object_subclass` | `party-credential` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `activate` | Stage-native placement (BO-STG-01) |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-information-management-6vjgdh`

### Processes involved

- `processes:process-pr-activate-6qzuve`

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-12) in the `activate` stage; `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-12 per the CR-BO-10 scope continuation (BO-STG-01); every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003), and the record carries at least one process at its own ECF stage (CR-BO-10 AC-08 stage coherence).
