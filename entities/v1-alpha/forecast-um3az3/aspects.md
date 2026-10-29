# Forecast — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-forecast-um3az3`](objects-object-forecast-um3az3.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Forecast is

- **Kind:** a *financial-instrument* that is **predictive rather than authoritative**: the Forecast holds no permission and no value — it is the enterprise's best current statement of where it is heading.
- **Subclass:** *forecast* — the rolling estimate over a horizon; revised continuously, never approved once.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Forecast relates to the catalog mesh

```
  Budget (authority) ─┐
                     ├─compared──► steering signal
  FORECAST (estimate)┘
       ▲
       └── revised from ──► Journal Entries (actuals)
```

It is the join point between:

- the **finance-accounting domain** (actuals, close, reporting),
- the **strategy-direction domain** (performance steering), and
- the **party-relationship domain** (guidance to investors and stakeholders).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → baseline → in-revision → published → superseded by next cycle` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-09 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `um3az3` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Forecast-type BO supports)

- Forecast accuracy (vs. actuals at horizon)
- Revision frequency and drift
- Forecast-vs-budget divergence trend
- Guidance hit rate
