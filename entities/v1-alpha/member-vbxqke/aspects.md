# Member — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-member-vbxqke`](objects-object-member-vbxqke.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** `non-profit / co-operative`. Per rule BO-TAX-01 the industry variant lives in the subclass vocabulary (`member`); the structure and ECF coordinates are universal.

## Semantic aspect — what kind of thing a Member is

- **Kind:** a *party* — a party bound by **affiliation** rather than exchange: membership confers rights (vote, access, benefit) and obligations (dues, participation) defined by the enterprise's constitution.
- **Subclass:** *member* — the affiliation party — a role between Customer (pure exchange) and Employee (employment).
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Member relates to the catalog mesh

```
  MEMBER ──pays dues──► funds ──► enterprise purpose
     │ └─ votes ──► governance
     └── renewed / lapsed ──► relationship state
```

It is the join point between:

- the **party-relationship domain** (the affiliation),
- the **governance-existence domain** (member rights in governance), and
- the **finance-accounting domain** (dues, subscriptions).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `prospective → joined → active → lapsing → lapsed / resigned` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-08 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `vbxqke` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Member-type BO supports)

- Member count and growth
- Retention / renewal rate
- Engagement (participation per member)
- Revenue per member
