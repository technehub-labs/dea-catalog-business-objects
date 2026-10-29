# Usage Record — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-usage-record-nax3b6`](objects-object-usage-record-nax3b6.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Usage Record is

- **Kind:** a *transaction* that is a **metered event**: the atomic unit of consumption evidence — a call detail record, data session, or message event. Its defining property is volume: millions per day, and each one is money.
- **Subclass:** *usage-record* — rated against the tariff; the atomic input to billing and to interconnect settlement.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Usage Record relates to the catalog mesh

```
  Service Instance ──generates──► USAGE RECORD ──rated via──► Tariff Plan
                                   │
                                   ├──► Invoice (postpaid) / Prepaid Balance debit (real-time)
                                   └──► Interconnect settlement (off-net traffic)
```

It is the join point between:

- the **finance-accounting domain** (rating, billing, settlement),
- the **enablement-operations domain** (generation in service delivery), and
- interconnect governance (settlement against the agreement).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `generated → collected → rated → billed/settled → archived (retention-mandated)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-15.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003; XREF gate enforced in CI).
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces coherence (CR-BO-13).
- **Content-addressing:** the `nax3b6` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Usage Record-type BO supports)

- Rating accuracy (unrated/errored records)
- Usage latency (event to rated)
- Settlement reconciliation break rate
- Data completeness (missing CDRs)
