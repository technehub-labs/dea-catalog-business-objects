# CR-BO-10: ECF Stage Diversification Proposal (First Non-Operate Cells)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-10 |
| **Title** | ECF Stage Diversification Proposal (First Non-Operate Cells) |
| **Status** | Proposed (this PR) |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-06 (scope-setting precedent), CR-BO-09 (all seven domains populated at operate) |
| **Companion to** | — |

## 1. Purpose

Every one of the catalog's 49 records sits in the `operate` ECF stage. The
catalog is therefore a snapshot of the *run* the business — its `conceive`,
`design`, `build`, `activate`, `improve`, and `retire` cells are empty, even
though the sibling processes catalog already has `process-*` records at every
stage (e.g. `sd-conceive-xa4h2k`, `pv-design-8v4k89`, `eo-build-awy8dz`,
`ge-retire-mjq5hg`). This CR proposes the admission scope for the first
non-`operate` records and pins the stage-placement rule. It admits no records;
the admission CR follows once the §5 decisions land.

## 2. Design decision: what a non-operate cell means for a Business Object

The ECF cell answers *"where in the lifecycle does the business operate on
this kind of thing?"* — not *"how old is this instance?"* (that is
`current_state`). Two placements are both legitimate and must not be
confused:

- **Dominant-stage placement.** Most types live where they are principally
  created and managed: the Customer is principally managed at `operate`,
  so its cell is `party-relationship · operate` even though customers are
  first conceived and designed elsewhere.
- **Stage-native placement.** Some types exist *only* in a lifecycle moment:
  a Business Case is consumed at the decision and has no operate life; a
  Retirement Plan for an offering exists only as the offering exits.

> **BO-STG-01 (proposed cardinal rule).** A Business Object is placed at the
> stage where the business *principally manages the type*. Types whose whole
> life is inside a single non-operate moment are placed at that stage
> (stage-native); types with a cross-stage life are placed at their dominant
> stage, and their other-stage activity is expressed through
> `processes_involved[]` at those stages — never by duplicating the record
> per stage. One record, one cell, at all times (per the README's
> "exactly one cell" invariant).

## 3. Proposed candidates

### Stage-native types (new records at non-operate cells)

| Candidate | object_class / subclass | ECF cell | Rationale |
|---|---|---|---|
| Business Case | work-item / business-case | strategy-direction · conceive | Exists to justify a commitment; consumed at the decision, then closed. Anchors: `sd-conceive-*` processes, strategic-planning capability. |
| Requirement | transaction / requirement | product-value · design | The specification of what an offering/feature must satisfy; superseded by the built thing. Anchors: `pv-design-8v4k89`, offering/technology capabilities. |
| Candidate | party / candidate-party | party-relationship · conceive | The prospective party under evaluation before it becomes a Customer/Supplier/Member. Anchors: `pr-conceive-*` processes, customer-management. |
| Offboarding Plan | work-item / offboarding-plan | party-relationship · retire | The managed exit of a party relationship. Anchors: retire-stage party processes. |
| Sunset Plan | work-item / sunset-plan | product-value · retire | The managed exit of an offering. Anchors: `pv-retire-6us5am`, offering-management. |

### Improve-stage candidates (deferred pending better process anchors)

Post-Implementation Review, Improvement Proposal — natural `improve`-cell
types; the processes catalog's improve-stage anchors are thin. Deferred.

## 4. Placement audit of existing records (no action proposed)

Existing records stay at `operate` under BO-STG-01's dominant-stage rule.
Their non-operate activity is already expressed through
`processes_involved[]` (e.g. Product lists `pv-design-8v4k89`). No migration
is proposed; re-placement would be a per-record CR.

## 5. Open decisions requested from review

1. **Adopt BO-STG-01** as a cardinal admission rule (stage placement =
   principally-managed stage; one record, one cell)?
2. **Admission size** — all five stage-native candidates in one CR, or the
   three with the strongest anchors first (Business Case, Requirement,
   Candidate)?
3. **Naming** — `Candidate` vs `Prospect` for the pre-acquisition party
   (Prospect is the more common commercial term; Candidate collides with the
   candidate-file concept in other catalogs' subtrees).

## 6. Acceptance criteria (for the admission CR this proposal authorizes)

- AC-01..AC-07: identical to CR-BO-09 §3 (schema, IDM, ES, AUT gates;
  resolved references; CATALOG.yaml freshness).
- AC-08: each admitted non-operate record's `processes_involved[]` includes
  at least one process at its own ECF stage (stage coherence).

## 7. Out of scope

- Record admission (follow-up CR once §5 decisions land).
- Re-placement of existing operate-stage records (§4; none proposed).
- `resource`/`location` class variants at non-operate stages.
