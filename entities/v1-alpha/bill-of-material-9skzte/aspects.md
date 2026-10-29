# Bill of Material — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-bill-of-material-9skzte`](objects-object-bill-of-material-9skzte.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `manufacturing`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`bill-of-material`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Bill of Material is

- **Kind:** a *resource* — a **resource** that is **structural rather than physical**: like the Price List in the commercial set, nobody makes a BOM — it is the frame in which composition exists.
- **Subclass:** *bill-of-material* — the component structure of a product: the list of parts and quantities required to make one unit.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Bill of Material relates to the catalog mesh

```
  PRODUCT ──explodes into──► BOM ──drives──► material requirements
                               │
                               └── revised via ──► engineering change
```

It is the join point between:

- the **enablement-operations domain** (planning, production),
- the **product-value domain** (the product it defines), and
- change governance (engineering revisions).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → released → in-use → revised → superseded` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `9skzte` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Bill of Material-type BO supports)

- BOM accuracy (planned vs. actual usage)
- Revision currency per product
- Component standardization rate
- Where-used coverage for recalls
