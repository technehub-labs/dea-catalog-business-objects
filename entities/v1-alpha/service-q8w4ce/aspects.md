# Service — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-service-q8w4ce`](objects-object-service-q8w4ce.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** written from a commercial / for-profit enterprise lens, consistent with the seed records. The type itself is industry-neutral; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.

## Semantic aspect — what kind of thing a Service is

- **Kind:** an *offering* — but an **intangible** one: value is delivered as an activity performed for the customer, not a good transferred to the customer.
- **Subclass:** *service* — defined by its delivery process rather than its unit of transfer; a Service cannot be stocked, only scheduled and delivered.
- **Fungibility:** unlike a catalogue Product, two instances of the same Service are never identical — quality lives in the delivery.

## Relational aspect — how the Service relates to the catalog mesh

```
  Offering ──► SERVICE ──delivered──► Ticket / Order line
                 │
                 └── priced via ──► Price List
```

The Service is the **delivery-process counterpart of the Product**. Together they complete the offering space. It is the join point between:

- the **product-value domain** (catalogue, proposition),
- the **enablement-operations domain** (service delivery processes), and
- the **finance-accounting domain** (revenue recognition over delivery, not shipment).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `conceive → … → operate → retire` |
| Domain business state | `current_state` | `proposed → designed → launched → active → deprecated → retired` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** offboarding / decommission processes (a future `retire`-stage cell).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-07 per the CR-BO-06 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `q8w4ce` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Service-type BO supports)

- Service revenue and margin per delivery
- Utilization of service capacity
- Service delivery quality (SLA attainment)
- Repeat-service rate
