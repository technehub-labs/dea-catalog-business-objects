# Asset — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-asset-w887xr`](objects-object-asset-w887xr.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Asset is

- **Kind:** a *financial-instrument* with a **long horizon**: value is consumed over periods via depreciation, not at once.
- **Subclass:** *fixed-asset* — the balance-sheet register of operational equipment and property; the accounting shadow of physical and legal objects.
- **Duality:** an Asset has two parallel lives — a physical one (maintained, used, worn) and a financial one (costed, depreciated, impaired).

## Relational aspect — how the Asset relates to the catalog mesh

```
  Purchase Order ──► capitalization ──► ASSET
                                        │  ├─ physical: maintenance (eo-operate)
                                        │  └─ financial: depreciation (fa-operate)
                                        ▼
                                   Journal Entry (per period)
```

The Asset is the **balance-sheet anchor of operations**: everything the enterprise durably owns flows into it. It is the join point between:

- the **finance-accounting domain** (capitalization, depreciation, impairment),
- the **enablement-operations domain** (maintenance, utilization), and
- the **strategy-direction domain** (capital allocation decisions).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `acquired → capitalized → in-service → under-maintenance → impaired → disposed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `w887xr` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Asset-type BO supports)

- Asset register value and age profile
- Utilization rate of productive assets
- Maintenance cost vs. asset value
- Return on assets (ROA)
