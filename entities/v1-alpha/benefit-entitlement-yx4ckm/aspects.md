# Benefit — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-benefit-entitlement-yx4ckm`](objects-object-benefit-entitlement-yx4ckm.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `government`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`benefit-entitlement`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Benefit is

- **Kind:** a *financial-instrument* — an **entitlement, not money**: like the Budget on the spending side, the Benefit is a standing right on the receiving side — eligibility establishes it, disbursement executes it.
- **Subclass:** *benefit-entitlement* — the outbound stewardship instrument of the public lens, the counterpart of the Grant in the commercial set.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Benefit relates to the catalog mesh

```
  Eligibility rule ──establishes──► BENEFIT ──disbursed──► Payment
                                        │
                                        └── bounded by ──► Budget
```

It is the join point between:

- the **finance-accounting domain** (disbursement, budget control),
- the **party-relationship domain** (the entitled citizen), and
- the **governance-existence domain** (eligibility determinations, cases).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `applied → assessed → entitled → in-payment → suspended → ceased` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `yx4ckm` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Benefit-type BO supports)

- Benefit coverage of the eligible population
- Accuracy of eligibility determinations
- Disbursement cycle time
- Overpayment / fraud recovery rate
