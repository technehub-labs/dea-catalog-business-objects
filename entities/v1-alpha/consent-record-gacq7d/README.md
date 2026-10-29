# Consent Record

Documentation for Business Object record [`objects:object-consent-record-gacq7d`](objects-object-consent-record-gacq7d.yaml)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-consent-record-gacq7d` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `party-relationship` · `operate` |
| Admitted by | [CR-BO-07](../../../change-requests/CR-BO-07-second-admission-wave2-t1.md) (2026-10-30) |

## Definition

The documented expression of a party's permission for the enterprise to process their data or contact them for named purposes. The Consent Record is a party-relationship compliance object: it is captured at grant, versioned on change, and its withdrawal terminates the permissions it previously carried.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `legal-instrument` | Kind of thing the business cares about |
| `object_subclass` | `consent-record` | Refinement under the class |
| `ecf_domain` | `party-relationship` | Universal ECF domain coordinate |
| `ecf_stage` | `operate` | Operated in steady state |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`

### Processes involved

- (none; processes resolved in a follow-up sweep)

## Lifecycle

Anchored at activation on 2026-10-30 (CR-BO-07); `current_state` is a domain business label distinct from the universal `ecf_stage` coordinate.

## Governance

Admitted under CR-BO-07 per the CR-BO-06 wave-2 scope; every cross-catalog reference resolves against the sibling catalog HEADs (IDM-003). Aspects prose follows the explicit-lens convention (CR-BO-06 §6.3).
