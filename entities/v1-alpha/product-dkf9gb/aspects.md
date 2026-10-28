# Product — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-product-dkf9gb`](objects-object-product-dkf9gb.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

## Semantic aspect — what kind of thing a Product is

- **Kind:** an *offering* — a standing, referenceable thing the enterprise exchanges for value. It is not a party (no agency) and not a transaction (no completion state); it persists across the many transactions that reference it.
- **Subclass:** *catalogue-product* — a formally catalogued offer, with identity, pricing structure, and lifecycle governance. The catalogue is what makes an offering orderable.
- **Duality:** many products are services; the Business Object deliberately covers both goods and service offerings under one type.

## Relational aspect — supply-side anchor

```
        (designs/operates)
 Capabilities ─────────────► PRODUCT
 (offering-mgmt, marketing)      │
                                 │ ordered as
                                 ▼
 Customer ──► Order ──► Invoice ──► Payment
                                 ▲
                   Feature Flag (controls runtime behavior)
```

The Product sits at the head of the **fulfilment chain**: Customers don't buy "orders", they buy Products; the Order is just the transactional wrapper. Downstream, the Product's pricing and catalogue position flow into Invoices.

## Lifecycle aspect

The Product traverses the widest ECF span of the seed set — its own description names design, build, operate, and portfolio evolution:

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → design → build → activate → operate → improve → retire` |
| Domain business state | `current_state` | `proposed → launched → active → end-of-sale → retired` |

Portfolio-level decisions (introduce, refresh, sunset) are handled through product-value processes (`pv-design`, `pv-operate`), and every transition lands in `state_history`.

## Operational aspect — acting on the object

- **Created by:** proposition/design processes (`pv-design`).
- **Read by:** order capture (catalogue lookup), pricing, marketing campaigns, entitlement checks.
- **Updated by:** catalogue maintenance, re-pricing, portfolio reviews.
- **Retired by:** end-of-sale/sunset processes — retirement removes orderability without deleting history.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-05.
- **Reference integrity:** both capability and both process references were resolved against the live sibling catalogs before landing (IDM-003).
- **Content-addressing:** the `dkf9gb` hash suffix is content-derived and immutable (IDM-005 normalization applies to the path).
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Product-type BO supports)

- Catalogue size and mix (active vs. retiring, goods vs. services)
- Revenue and margin per product / product line (via Order → Invoice chain)
- Time-to-market: design → launch
- Product attachment and cross-sell rates by customer segment
