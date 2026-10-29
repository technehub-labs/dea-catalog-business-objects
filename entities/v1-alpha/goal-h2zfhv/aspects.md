# Goal — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-goal-h2zfhv`](objects-object-goal-h2zfhv.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Goal is

- **Kind:** a *work-item* — the second record of the class approved under CR-BO-06 §6.1: a unit of non-routine work. The Goal is a commitment to an outcome, not to activity: it is what the Project portfolio exists to achieve.
- **Subclass:** *strategic-goal* — expressed so progress is measurable (horizon, target, metric), distinct from the Initiative/Project that executes toward it.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Goal relates to the catalog mesh

```
  Strategy ──frames──► GOAL ──steered──► Initiative / Project portfolio
                         │
                         └── measured by ──► strategic performance review
```

It is the join point between:

- the **strategy-direction domain** (intent and steering),
- the **agency-organization domain** (execution via the initiative portfolio), and
- the **finance-accounting domain** (goals cascade into budgets and forecasts).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → adopted → in-flight → achieved / missed → superseded` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-09 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `h2zfhv` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Goal-type BO supports)

- Goal attainment rate
- Strategic-initiative alignment coverage
- Time-to-achieve vs. horizon
- Cascade coverage (enterprise → unit goals)
