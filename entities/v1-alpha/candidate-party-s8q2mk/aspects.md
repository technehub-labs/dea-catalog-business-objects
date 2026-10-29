# Candidate — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-candidate-party-s8q2mk`](objects-object-candidate-party-s8q2mk.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the ` conceive` moment; it is not an operate-stage object.

## Semantic aspect — what kind of thing a Candidate is

- **Kind:** a *party* — but a **pre-role** one: the Candidate is the same real-world party the role parties (Customer, Supplier, Member, Partner) will become, tracked before any role relationship exists.
- **Subclass:** *candidate-party* — under evaluation; its terminal transitions are conversion (into a role party) or rejection. Named `Candidate` per the CR-BO-10 §5.3 decision.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Candidate relates to the catalog mesh

```
  market signal ──qualifies──► CANDIDATE ──converts──► Customer / Supplier / Member / Partner
                                 │
                                 └── rejected / expired
```

It is the join point between:

- the **party-relationship domain** (acquisition, qualification),
- the **product-value domain** (demand signals the Candidate carries), and
- the **finance-accounting domain** (acquisition cost per convert).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | ` conceive` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `identified → qualified → in-evaluation → converted / rejected / expired` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire — the ` conceive` moment *is* their end).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-11 per the CR-BO-10 scope.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `s8q2mk` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Candidate-type BO supports)

- Candidate-to-party conversion rate
- Acquisition cost per conversion
- Qualification cycle time
- Pipeline coverage by segment
