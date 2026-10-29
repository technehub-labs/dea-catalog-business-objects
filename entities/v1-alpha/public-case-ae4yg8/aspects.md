# Case — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-public-case-ae4yg8`](objects-object-public-case-ae4yg8.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `government`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`public-case`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Case is

- **Kind:** a *transaction* — a **service-matter transaction** in the governance domain: the Case is the vehicle by which the enterprise reaches a determination for a party — the public-sector counterpart of the commercial Ticket, but with legally binding outcomes.
- **Subclass:** *public-case* — the case — intake, investigation, decision, closure; a matter tracked to determination.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Case relates to the catalog mesh

```
  CITIZEN ──opens──► CASE ──investigated──► decision ──► Benefit / refusal
                       │
                       └── appealed ──► reconsideration
```

It is the join point between:

- the **governance-existence domain** (determinations, appeals),
- the **party-relationship domain** (the citizen), and
- the **finance-accounting domain** (where outcomes disburse benefits).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `opened → in-investigation → determined → in-appeal → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `ae4yg8` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Case-type BO supports)

- Case volume by type
- Determination cycle time
- Appeal and overturn rate
- Backlog and ageing
