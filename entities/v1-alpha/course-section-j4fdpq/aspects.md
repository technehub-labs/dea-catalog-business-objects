# Course Section — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-course-section-j4fdpq`](objects-object-course-section-j4fdpq.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `education`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`course-section`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Course Section is

- **Kind:** a *transaction* — the **delivery transaction** of education: a scheduled instance with cohort, place, and term — the Course Section is to the Study Program what the Shipment is to the Order.
- **Subclass:** *course-section* — a section — a bounded delivery instance, distinct from the standing program it instantiates.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Course Section relates to the catalog mesh

```
  STUDY PROGRAM ──scheduled──► COURSE SECTION ──completed──► grades / credits
                                  │
                                  └── capacity ──► utilization metrics
```

It is the join point between:

- the **enablement-operations domain** (scheduling, delivery),
- the **product-value domain** (the parent program), and
- resource governance (staffing and room capacity).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `scheduled → open → running → completed → closed (or cancelled)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `j4fdpq` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Course Section-type BO supports)

- Section fill rate
- Completion and pass rates
- Cost per section
- Instructor utilization
