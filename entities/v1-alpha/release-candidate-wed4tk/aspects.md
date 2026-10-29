# Release Candidate — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-release-candidate-wed4tk`](objects-object-release-candidate-wed4tk.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01, CR-BO-10 §2):** stage-native — this type exists only within the `build` moment.

## Semantic aspect — what kind of thing a Release Candidate is

- **Kind:** a *technology-control* — but a **candidate build**: the Release Candidate is not the running artifact (Application) nor the in-flight switch (Feature Flag); it is the artifact under proof.
- **Subclass:** *release-candidate* — feature-complete and under verification; its terminal transitions are promotion to release or rejection back to development.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Release Candidate relates to the catalog mesh

```
  Application ──builds──► RELEASE CANDIDATE ──verified──► promoted / rejected
                              │
                              └── gates ──► Incident prevention (pre-production)
```

It is the join point between:

- the **enablement-operations domain** (platform build and verification),
- technology governance (release authorization), and
- the **governance-existence domain** (change and risk control).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `build` (stage-native; no cross-stage drift) |
| Domain business state | `current_state` | `declared → in-verification → promoted / rejected → (post-release: superseded)` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per CR-BO-10 AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition (stage-native objects close rather than retire).

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-12 per the CR-BO-10 scope continuation.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Content-addressing:** the `wed4tk` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Release Candidate-type BO supports)

- Verification pass rate per candidate
- Defect escape rate to production
- Candidate-to-release cycle time
- Rollback rate of promoted candidates
