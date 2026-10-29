# Tariff Plan — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-tariff-plan-ah5q9f`](objects-object-tariff-plan-ah5q9f.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Tariff Plan is

- **Kind:** an *offering* that is a **rate structure**: nobody consumes a tariff — usage is *rated against* it. Partly non-discretionary: regulated markets require tariff approval, making this the offering where commercial freedom meets regulatory constraint.
- **Subclass:** *tariff-plan* — per-unit prices, bundles, allowances, zone rules; the telecom specialization of pricing.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Tariff Plan relates to the catalog mesh

```
  PRODUCT/SERVICE ──priced via──► TARIFF PLAN ──rates──► Usage Record ──► Invoice / Prepaid debit
                                    │
                                    └── approved by ──► regulator (regulated markets)
```

It is the join point between:

- the **product-value domain** (catalogue, proposition),
- the **finance-accounting domain** (rating, billing), and
- regulatory governance (tariff filing in regulated markets).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `drafted → filed (regulated) → published → active → superseded` |

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
- **Content-addressing:** the `ah5q9f` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Tariff Plan-type BO supports)

- Tariff-change cycle time (filing to live)
- Revenue mix by tariff
- Tariff realization vs. list (discount leakage)
- Regulatory filing pass rate
