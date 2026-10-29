# Project — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-project-5hgzd3`](objects-object-project-5hgzd3.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Project is

- **Kind:** a *work-item* — the first record in the new class approved under CR-BO-06 §6.1: a unit of **non-routine work**. A Project is neither a transaction (it is not a commercial exchange) nor an instrument (it binds no value); it is a vehicle for change.
- **Subclass:** *project* — a temporary endeavor with scope, time, and resource constraints, undertaken to create change; distinct from the standing organization that runs it.
- **Temporality:** the defining property is that a Project **ends** — by delivery or by cancellation — unlike a department or a service.

## Relational aspect — how the Project relates to the catalog mesh

```
  Strategy ──funds──► PROJECT ──delivers──► change (new capability, asset, offering)
                        │
                        ├── staffed by ──► Employee
                        └── governed by ──► Budget
```

The Project is the **delivery vehicle of non-routine change**: the bridge between what the enterprise decides and what it becomes. It is the join point between:

- the **strategy-direction domain** (initiative portfolio),
- the **agency-organization domain** (temporary organization), and
- the **finance-accounting domain** (project budget consumption).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → chartered → planned → in-execution → closing → closed / cancelled` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `5hgzd3` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Project-type BO supports)

- On-time and on-budget delivery rate
- Benefits realization vs. business case
- Stage-gate pass/hold ratio
- Portfolio throughput (projects closed per period)
