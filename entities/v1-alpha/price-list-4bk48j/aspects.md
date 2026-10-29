# Price List — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-price-list-4bk48j`](objects-object-price-list-4bk48j.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Price List is

- **Kind:** an *offering*-class object that is **structural rather than sold**: nobody buys a Price List; it is the frame in which prices exist.
- **Subclass:** *price-list* — a scoped, versioned set of prices (by market, channel, segment, or agreement).
- **Composition semantics:** a container object — its instances hold price entries that Quote and Order pricing resolves against.

## Relational aspect — how the Price List relates to the catalog mesh

```
  PRODUCT / SERVICE
        │ priced via
        ▼
  PRICE LIST ──governs──► Quote ──accepted──► Order ──► Invoice
```

The Price List is the **pricing point of the commercial chain**: every monetized object downstream (Quote, Order, Invoice) traces its amounts back to a price-list resolution. It is the join point between:

- the **product-value domain** (offering value expressed as price),
- the **party-relationship domain** (segment- and customer-scoped pricing), and
- the **finance-accounting domain** (realized price = revenue basis).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `draft → approved → published → superseded → archived` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `4bk48j` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Price List-type BO supports)

- Price realization vs. list price (discount leakage)
- Price-list coverage of the active catalogue
- Margin by price list / segment
- Price change frequency and effect
