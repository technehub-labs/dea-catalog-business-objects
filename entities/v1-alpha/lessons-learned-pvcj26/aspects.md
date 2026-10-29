# Lessons Learned — Business Object Aspects

A deep-dive into the facets of Business Object [`objects:object-lessons-learned-pvcj26`](objects-object-lessons-learned-pvcj26.yaml). The sibling [README](README.md) holds the record-level documentation; this file elaborates the aspects around the object.

> **Sector lens (CR-BO-06 §6.3):** commercial / for-profit enterprise lens. The type is universal; subclass-level variants (per rule BO-TAX-01) adjust the vocabulary, not the structure.
>
> **Stage placement (BO-STG-01):** stage-native — this type exists only within the `improve` moment.

## Semantic aspect — what kind of thing a Lessons Learned is

- **Kind:** a *work-item* — the **knowledge artifact of improvement**: the record exists to make experience reusable; its value is realized only when a future case or plan cites it.
- **Subclass:** *lessons-learned* — stage-native to improve; distilled from engagements, projects, and reviews.
- **Core identity vs. instance identity:** the record documents the *type*; individual instances' handles live at the data layer (`identity.primary_id` / `identity.external_ids`).

## Relational aspect — how the Lessons Learned relates to the catalog mesh

```
  Engagement / Project / Review ──distills──► LESSONS LEARNED ──cited by──► Business Case / Requirement / Plan
```

It is the join point between:

- the **agency-organization domain** (engagement and alignment reviews),
- knowledge governance (where the corpus lives), and
- the **strategy-direction domain** (where the lessons feed the next case).

## Lifecycle aspect

| Lifecycle | Where it lives | Example values |
|---|---|---|
| Universal ECF stage | `ecf_stage` | `improve` |
| Domain business state | `current_state` | `captured → distilled → published → cited → archived` |

The two lifecycles deliberately do not overlap: the ECF stage is the universal catalog coordinate; `current_state` is the domain label whose transitions are recorded in `state_history`.

## Operational aspect — acting on the object

- **Created by:** the processes listed in `processes_involved[]` (resolved against the live processes catalog; at least one at this record's own stage, per AC-08).
- **Read by:** downstream objects and capabilities that reference or consume it.
- **Updated by:** the processes of its ECF domain at its stage.
- **Retired by:** its terminal transition per the domain lifecycle above.

## Governance aspect

- **Change control:** structural changes require a CR in `change-requests/`; admitted under CR-BO-14.
- **Reference integrity:** every `capabilities_consumed[]` / `processes_involved[]` entry resolves against a live sibling catalog (IDM-003); deliberately unset fields remain empty until their catalogs bind.
- **Version integrity:** substance changes require a version bump; the VER-002 gate enforces the coherence (CR-BO-13).
- **Content-addressing:** the `pvcj26` hash suffix is content-derived and immutable; renaming the slug or moving the file would break the id contract and is forbidden.
- **Authorship:** authorship-bearing fields follow the cardinal rules (R1/R2) enforced by the authorship gate.

## Measurement aspect (indicative KPIs a Lessons Learned-type BO supports)

- Capture rate per engagement/project
- Citation rate in later cases/plans
- Repeat-mistake rate
- Time from capture to publication
