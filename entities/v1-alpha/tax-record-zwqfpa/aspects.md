# Tax Record — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-tax-record-zwqfpa`](objects-object-tax-record-zwqfpa.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens (statutory obligations are universal). The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Tax Record is

- **Kind:** a *financial-instrument* that is **statutory**: its form, deadlines, and consequences are set by law, not by enterprise preference — the least discretionary instrument in the finance set.
- **Subclass:** *tax-record* — a filing, assessment, or position under tax law; error is not a commercial loss but a statutory consequence.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Tax Record relates to the catalog mesh

```
  Tax strategy (fa-design) ──frames──► TAX RECORD ──filed──► authority
                                         │
                                         └── defended / audited ──► rulings
```

It is the join point between:

- the **finance-accounting domain** (positions, filings, provisions),
- the **governance-existence domain** (regulatory oversight, audit), and
- the **party-relationship domain** (the tax authority as counterparty).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `prepared → reviewed → filed → assessed → settled / in-dispute` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-09 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `zwqfpa` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Tax Record-type BO supports)

- Filing timeliness and completeness
- Effective tax rate and provision accuracy
- Audit and dispute outcomes
- Position documentation coverage
