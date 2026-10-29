# Environment — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-environment-npd5vt`](objects-object-environment-npd5vt.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Environment is

- **Kind:** a *technology-control* that is a **run-state separator**: an Environment holds no business function of its own — it exists to keep run-states of the same technology apart.
- **Subclass:** *environment* — production, staging, test, development contexts; the classic promotion path between them is the operational use of the concept.
- **Isolation semantics:** the defining property is separation — change proven in one Environment is not change proven in another; promotion is an explicit, controlled act.

## Relational aspect — how the Environment relates to the catalog mesh

```
  Application ──deployed into──► ENVIRONMENT (prod / stage / test)
                                   │
                                   └── promotion path (controlled change)
```

The Environment is the **safety frame of technology change**: it is what makes change auditable rather than experimental. It is the join point between:

- the **enablement-operations domain** (platform operations),
- change/technology governance (promotion control), and
- the Application lifecycle (retirement happens environment by environment).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `provisioned → configured → in-service → degraded → decommissioned` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `npd5vt` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Environment-type BO supports)

- Environment parity (prod vs. non-prod drift)
- Promotion lead time and failure rate
- Environment cost vs. production value
- Incident leakage from non-prod
