# Partner — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-partner-cfhqx9`](objects-object-partner-cfhqx9.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Partner is

- **Kind:** a *party* engaged in a **joint value arrangement** — neither purely demand-side (Customer) nor purely supply-side (Supplier), but a co-producing counterparty.
- **Subclass:** *partner* — alliances, resellers, co-developers, and consortium members fall under this role; the arrangement, not the person, is what distinguishes it.
- **Core identity vs. instance identity:** the record documents the *type*; individual partners' handles live at the data layer.

## Relational aspect — how the Partner relates to the catalog mesh

```
  PARTNER ◄──co-sells/supplies──► Customer
     │
     ├── co-develops ──► Offering (Service, Product)
     └── governed by ──► Contract (joint terms)
```

The Partner sits **between** the two classic chains: it can appear on either side of value exchange, which is exactly why it carries its own subclass. It is the join point between:

- the **party-relationship domain** (the alliance itself),
- the **product-value domain** (co-produced offerings), and
- the **governance-existence domain** (partner contracts).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `prospect → engaged → active → under-performing → exited` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `cfhqx9` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Partner-type BO supports)

- Partner-sourced revenue share
- Active vs. exited partners by tier
- Joint initiative count and outcomes
- Partner satisfaction and enablement coverage
