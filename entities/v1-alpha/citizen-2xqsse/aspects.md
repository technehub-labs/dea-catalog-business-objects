# Citizen — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-citizen-2xqsse`](objects-object-citizen-2xqsse.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `government`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`citizen`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Citizen is

- **Kind:** a *party* — the **served party** of a public-sector lens: the relationship is one of entitlement and obligation under law, not commercial exchange.
- **Subclass:** *citizen* — the public counterpart of the Customer — the party on whose behalf, not for whose payment, the enterprise acts.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Citizen relates to the catalog mesh

```
  CITIZEN ──opens──► Case / Benefit ──determined──► entitlement or refusal
     │                                     │
     └── identified by ──► national identifiers └── disbursed ──► Payment
```

It is the join point between:

- the **party-relationship domain** (the service relationship),
- the **governance-existence domain** (cases, determinations), and
- the **finance-accounting domain** (benefit disbursement).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `identified → engaged → in-proceeding → served → archived` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `2xqsse` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Citizen-type BO supports)

- Service transactions per citizen
- Determination cycle time
- Digital-channel adoption
- Coverage of eligible population
