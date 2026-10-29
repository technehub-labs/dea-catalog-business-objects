# Business Case — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-business-case-et8p4e`](objects-object-business-case-et8p4e.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the ` conceive` moment; it is not an operate-stage object.

## Semantic aspect — what kind of thing a Business Case is

- **Kind:** a *work-item* — a unit of non-routine work. The Business Case is a **decision artifact**: it is written to be consumed by a decision, not to be executed.
- **Subclass:** *business-case* — outcomes, costs, risks, and alternatives in one frame; its acceptance *is* the commitment it justifies.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Business Case relates to the catalog mesh

```
  Strategic intent ──frames──► BUSINESS CASE ──justifies──► Goal / Project
                                    │
                                    └── lessons feed ──► next cycle's cases
```

It is the join point between:

- the **strategy-direction domain** (intent, horizons, options),
- the **finance-accounting domain** (costs, benefits, budget requests), and
- the **governance-existence domain** (the decision itself and its audit trail).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | ` conceive` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `drafted → reviewed → approved / rejected → closed (post-decision)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire — the ` conceive` moment *is* their end).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-11 per the CR-BO-10 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `et8p4e` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Business Case-type BO supports)

- Business-case approval rate and cycle time
- Benefit realization vs. case projection
- Case quality (assumption survival rate)
- Rejected-case lessons captured
