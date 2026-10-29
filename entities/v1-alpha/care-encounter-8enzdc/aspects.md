# Treatment — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-care-encounter-8enzdc`](objects-object-care-encounter-8enzdc.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `healthcare`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`care-encounter`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Treatment is

- **Kind:** a *transaction* — the **delivery transaction** of care: a bounded clinical interaction from admission to discharge, with the Patient rather than a good as its payload.
- **Subclass:** *care-encounter* — the encounter — the unit of care delivery in which diagnosis, intervention, and outcome are recorded.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Treatment relates to the catalog mesh

```
  PATIENT ──admitted──► TREATMENT ──discharged──► outcome / follow-up
                          │
                          └── resource use ──► cost / billing basis
```

It is the join point between:

- the **enablement-operations domain** (care delivery),
- the **party-relationship domain** (the patient), and
- the **finance-accounting domain** (episode costing, billing).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `scheduled → admitted → in-care → discharged → closed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `8enzdc` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Treatment-type BO supports)

- Encounter volume and mix
- Length of stay / encounter duration
- Resource cost per encounter
- Clinical outcome per encounter class
