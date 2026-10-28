# Product

Documentation for Business Object record [`objects:object-product-dkf9gb`](objects-object-product-dkf9gb.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-product-dkf9gb` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `product-value` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A product or service the enterprise offers to the market. The Product carries the value proposition: it is designed as a proposition, built as market readiness, operated through the product catalogue, and evolved through the portfolio lifecycle.

## Business role

The Product is the **supply-side anchor of the commercial model** — the thing the enterprise actually exchanges for value:

- **Orders** are placed *for* Products; order lines reference catalogue entries.
- **Invoices** price fulfilled Products; the Product's pricing gives the Invoice its monetary content.
- **Customers** buy Products; the value proposition is why the relationship exists at all.

The Product lives through the fullest ECF journey of the seed set: it is the one object whose description explicitly names four stages — design (proposition), build (market readiness), operate (catalogue), and improve/retire (portfolio evolution).

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `offering` | What the enterprise offers to the market |
| `object_subclass` | `catalogue-product` | A formal catalogue entry (vs. ad-hoc or bespoke offerings) |
| `ecf_domain` | `product-value` | Product-and-Value domain |
| `ecf_stage` | `operate` | Operated through the product catalogue |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-offering-management-6egkc8` — offering management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-marketing-xmc539` — marketing ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Processes creating / updating this object

- `processes:process-pv-operate-zyguzp` — product-value operate-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))
- `processes:process-pv-design-8v4k89` — product-value design-stage process ([dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Order](../order-bpy4g4/README.md) | Orders are placed for Products | Order → Product (subject) |
| [Customer](../customer-2qvphc/README.md) | Customers consume Products | Customer → Product (consumer) |
| [Invoice](../invoice-z3fwgb/README.md) | Invoices price fulfilled Products | Product ⇢ Invoice (via Order) |
| [Feature Flag](../feature-flag-p5gzf7/README.md) | Feature Flags control runtime product behavior | Feature Flag → Product (controls) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `proposed → designed → launched → active → end-of-sale → retired`, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- What does the enterprise offer, in what configurations, and at what catalogue position?
- Which capabilities manage offerings and market them?
- Which products are carried by which orders, and how do they roll into revenue?
- What is the portfolio shape (active vs. retiring) at any point in time?
