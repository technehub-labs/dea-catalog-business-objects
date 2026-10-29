# Subscription — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-subscription-3v98yb`](objects-object-subscription-3v98yb.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Subscription is

- **Kind:** an *offering* expressed as a **continuing entitlement** rather than a discrete transfer: the customer pays for access over time, not for a unit.
- **Subclass:** *subscription-plan* — the arrangement is the offering; the individual goods or services flow through it as instances.
- **Temporal semantics:** the defining property is the **term** — start, renewal, and end dates drive every downstream financial and operational consequence.

## Relational aspect — how the Subscription relates to the catalog mesh

```
  Offering ──► SUBSCRIPTION ──entitles──► Service / Product access
                  │
                  ├── billed ──► Invoice (recurring)
                  └── renewed / churned ──► Customer state
```

The Subscription is the **bridge between selling and operating**: it converts a one-time commercial event into a standing operational relationship. It is the join point between:

- the **product-value domain** (the plan as an offering),
- the **finance-accounting domain** (recurring billing, deferred revenue), and
- the **party-relationship domain** (retention and churn).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `trial → active → renewing → dunning → suspended → churned` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `3v98yb` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Subscription-type BO supports)

- Monthly recurring revenue (MRR) and growth
- Churn rate and net revenue retention
- Average subscription lifetime value (LTV)
- Dunning recovery rate
