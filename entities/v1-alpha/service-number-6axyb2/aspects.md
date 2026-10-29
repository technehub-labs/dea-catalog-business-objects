# Service Number — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-service-number-6axyb2`](objects-object-service-number-6axyb2.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** telecom operator / digital service provider (MCSP-aligned). The type is universal; the subclass carries the industry variant per rule BO-TAX-01.

## Semantic aspect — what kind of thing a Service Number is

- **Kind:** a *resource* that is an **address**: a scarce, regulator-governed identifier. Unlike a credential (which authenticates), the number is how the world reaches the subscriber — and number portability makes it movable between operators.
- **Subclass:** *service-number* — allocated from governed ranges, portable, attached to one subscriber at a time.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Service Number relates to the catalog mesh

```
  Numbering range (regulator) ──allocates──► SERVICE NUMBER ──attached to──► Subscriber
                                                │
                                                └── ported in/out ──► operator changes
```

It is the join point between:

- the **governance-existence domain** (numbering regulation),
- the **party-relationship domain** (the subscriber it addresses), and
- information governance (directory data).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `operate` |
| Domain business state | `current_state` | `allocated → reserved → assigned → in-service → ported-out → returned/reclaimed` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the operating and improvement processes of its ECF domain.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-15.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003; XREF gate enforced in CI).
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces coherence (CR-BO-13).
- **Content-addressing:** the `6axyb2` hash suffix is content-derived and immutable.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2).

## Measurement aspect (indicative KPIs a Service Number-type BO supports)

- Number utilization of allocated ranges
- Porting cycle time (in/out)
- Number churn (ports out)
- Regulatory compliance of numbering records
