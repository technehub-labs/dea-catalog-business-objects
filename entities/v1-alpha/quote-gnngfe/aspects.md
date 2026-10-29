# Quote — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-quote-gnngfe`](objects-object-quote-gnngfe.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Quote is

- **Kind:** a *transaction* — but a **pre-commitment** one: a Quote is an offer of terms, revocable and expiring, with no fulfilment obligation until accepted.
- **Subclass:** *sales-quote* — outbound offer to a customer (distinct from purchase-side commitments like the Purchase Order).
- **Binding semantics:** the defining behavior is **conversion** — acceptance transforms the Quote into an Order; expiry or withdrawal ends it with no residue.

## Relational aspect — how the Quote relates to the catalog mesh

```
  Customer ──requests──► QUOTE ──accepted──► Order ──► Invoice ──► Payment
                          │
                          └── expires / withdrawn / lost
```

The Quote is the **commercial negotiation stage** of the order-to-cash chain — the only stage where terms can still move freely. It is the join point between:

- the **party-relationship domain** (demand signal, negotiation),
- the **product-value domain** (prices resolved from the Price List), and
- the **enablement-operations domain** (conversion into executable work).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → sent → under-negotiation → accepted / lost / expired` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `gnngfe` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Quote-type BO supports)

- Quote-to-order conversion rate
- Quote cycle time (send to decision)
- Win/loss ratio and lost-reason distribution
- Average discount granted at quote stage
