# License

Documentation for Business Object record [`objects:object-license-na3j53`](objects-object-license-na3j53.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-license-na3j53` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `governance-existence` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

A granted legal permission under which the enterprise may conduct an activity it could not otherwise conduct. The License is granted by an external authority, expires or renews on terms, and its loss can constrain the enterprise's ability to operate.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `legal-instrument` | Kind of thing the business cares about |
| `object_subclass` | `license` | Refinement under the class |
| `ecf_domain` | `governance-existence` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-regulation-management-gya4d8`

### Processes involved

- (none; processes resolved in a follow-up sweep)

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
