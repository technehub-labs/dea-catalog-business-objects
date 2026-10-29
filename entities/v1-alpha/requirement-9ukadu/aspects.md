# Requirement — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-requirement-9ukadu`](objects-object-requirement-9ukadu.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the ` design` moment; it is not an operate-stage object.

## Semantic aspect — what kind of thing a Requirement is

- **Kind:** a *transaction* — but a **specification**, not an exchange: the Requirement's payload is a statement of need, and its lifecycle runs from statement to satisfaction.
- **Subclass:** *requirement* — traceable (origin, rationale, acceptance) and superseded by the built thing; the unit of the specification chain.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Requirement relates to the catalog mesh

```
  Customer need / Goal ──elicits──► REQUIREMENT ──satisfied by──► built offering/feature
                                       │
                                       └── traced to ──► tests, acceptance criteria
```

It is the join point between:

- the **product-value domain** (propositions, packaging),
- the **enablement-operations domain** (what build will deliver), and
- the **party-relationship domain** (the need's originator).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | ` design` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `drafted → reviewed → approved → satisfied → verified → closed (or deferred / rejected)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire — the ` design` moment *is* their end).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-11 per the CR-BO-10 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `9ukadu` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Requirement-type BO supports)

- Requirement volatility (change rate post-approval)
- Traceability coverage (origin and acceptance)
- Requirement-to-delivery lead time
- Defect escape rate by requirement
