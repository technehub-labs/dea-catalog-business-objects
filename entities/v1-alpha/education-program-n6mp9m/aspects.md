# Study Program — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-education-program-n6mp9m`](objects-object-education-program-n6mp9m.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `education`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`education-program`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Study Program is

- **Kind:** a *offering* — an **offering whose payload is a learning pathway**: structured, sequenced, and leading to a qualification — the curriculum counterpart of the commercial Product.
- **Subclass:** *education-program* — the program as catalogue object; its delivery instances are Course Sections.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Study Program relates to the catalog mesh

```
  STUDY PROGRAM ──delivered via──► Course Section ──enrolls──► learner
        │
        └── rationalized ──► portfolio decisions (pv processes)
```

It is the join point between:

- the **product-value domain** (catalogue, portfolio),
- the **enablement-operations domain** (delivery via sections), and
- the **party-relationship domain** (learner demand).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → accredited → offered → active → suspended → retired` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `n6mp9m` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Study Program-type BO supports)

- Program enrollment and completion rates
- Learner satisfaction and outcomes
- Program cost per learner
- Portfolio rationalization coverage
