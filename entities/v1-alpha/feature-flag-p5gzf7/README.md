# Feature Flag

Documentation for Business Object record [`objects:object-feature-flag-p5gzf7`](objects-object-feature-flag-p5gzf7.yaml) · [Aspects deep-dive](aspects.md)

## Identity

| Field | Value |
|---|---|
| id | `objects:object-feature-flag-p5gzf7` |
| Type | `BusinessObject` |
| Version | 1.0.0 |
| Lifecycle status | `active` |
| ECF cell | `enablement-operations` · `operate` |
| Admitted by | [CR-BO-05](../../../change-requests/CR-BO-05-first-admission-seed-business-objects.md) (2026-10-28) |

## Definition

A configuration switch controlling the runtime visibility or behavior of a product feature. The Feature Flag decouples deployment from release: technology-enablement capabilities act on it, and its state governs what customers experience without a redeployment.

## Business role

The Feature Flag is the **operational control surface of the product** — the one seed object whose *state itself* is the business lever:

- It gates what **Customers** experience of a **Product** — on, off, percentage, cohort.
- It decouples *deployment* (code shipped) from *release* (customers see it), turning release into a reversible business decision rather than an engineering event.
- It is the enablement-operations companion of the **Order**: both live in the same domain, but where the Order is the commercial transaction, the Feature Flag is the technology control that shapes delivery.

This makes it the most operationally "live" object in the seed set: its value is not in existing, but in being flipped — safely, reversibly, auditable.

## Classification

| Axis | Value | Meaning |
|---|---|---|
| `object_class` | `technology-control` | A configuration control rather than a party, transaction, or instrument |
| `object_subclass` | `release-feature-flag` | The release/deployment decoupling switch |
| `ecf_domain` | `enablement-operations` | Enablement-and-Operations domain |
| `ecf_stage` | `operate` | Operated in steady-state technology operations |
| `current_state` | `active` | Domain-specific business state |

## Relationships

### Capabilities acting on this object

- `capabilities:capability-technology-enablement-y6nkws` — technology enablement ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))
- `capabilities:capability-technology-management-maus5n` — technology management ([dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities))

### Related Business Objects

| Object | Relationship | Direction |
|---|---|---|
| [Product](../product-dkf9gb/README.md) | The flag controls a Product feature's runtime behavior | Feature Flag → Product (controls) |
| [Customer](../customer-2qvphc/README.md) | Flag targeting decides what Customers experience | Feature Flag → Customer (targets) |
| [Order](../order-bpy4g4/README.md) | Same domain sibling: the control vs. the transaction | Feature Flag ↔ Order (EO pair) |

Owner, stakeholders, events, and data entities are deliberately unset: their source catalogs are empty or unbound, and IDM-003 forbids unresolved references.

## Lifecycle

| State | ECF stage | Entered | Note |
|---|---|---|---|
| `active` | `activate` | 2026-10-28 | First admission (CR-BO-05); lifecycle anchored at activation. |

Typical domain lifecycle (informational): `created → enabled-off → canary → fully-on → cleanup-removed`, mirrored in the free-form `current_state` label.

## Key business questions this object answers

- What is the enterprise's release-control inventory — which switches exist, in which state?
- What are customers currently experiencing, independent of what has been deployed?
- Which capabilities own flag governance (enablement vs. management)?
- What is the flag hygiene picture (stale flags, orphaned toggles awaiting cleanup)?
