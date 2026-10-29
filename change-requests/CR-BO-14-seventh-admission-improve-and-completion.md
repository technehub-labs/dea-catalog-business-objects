# CR-BO-14: Seventh Admission (Improve-Stage Records and Taxonomy-Completion Records, 6 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-14 |
| **Title** | Seventh Admission (Improve-Stage Records and Taxonomy-Completion Records, 6 Records) |
| **Status** | Proposed (this PR) |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-10 (BO-STG-01), CR-BO-13 (VER/XREF gates; first admission under version integrity) |
| **Companion to** | — |

## 1. Purpose

Lands the improve stage — the last unpopulated ECF stage — with four
stage-native records, plus two taxonomy-completion records answering standing
scope questions: **Configuration Item** (the change-control unit) and
**Transformation Plan** (the portfolio-level strategic vehicle between Goal
and Project). With this admission, **all seven ECF stages are populated** and
the improve-stage open thread in project-status closes.

This is also the first admission under CR-BO-13's version discipline: the
version manifest is regenerated in the same CR, and the XREF gate's live-CI
resolution applies to every new reference.

## 2. Changes

### 2.1 Six Business Object records

| id | object_class | ECF (domain, stage) | Placement |
|---|---|---|---|
| `objects:object-audit-finding-jd44zy` | work-item / audit-finding | governance-existence · improve | stage-native — **first improve record** |
| `objects:object-performance-review-k3k7n6` | work-item / performance-review | strategy-direction · improve | stage-native |
| `objects:object-improvement-proposal-cwcz6m` | work-item / improvement-proposal | enablement-operations · improve | stage-native |
| `objects:object-lessons-learned-pvcj26` | work-item / lessons-learned | agency-organization · improve | stage-native |
| `objects:object-configuration-item-tsn3ex` | technology-control / configuration-item | enablement-operations · operate | dominant-stage |
| `objects:object-transformation-plan-mpsz65` | work-item / transformation-plan | strategy-direction · operate | dominant-stage (steered throughout its life) |

### 2.2 Taxonomy decisions recorded (from the CR-BO-14 review questions)

1. **Configuration Item** is admitted as a distinct `technology-control`
   subclass covering the un-modeled remainder (middleware, network segments,
   runbooks, integrations). Application and Environment are already CIs in
   substance and **stay as their own subclasses** — no re-parenting, per
   BO-TAX-01 (a re-placement would be a separate migration CR, and none is
   proposed).
2. **Transformation Plan** fills the strategic work-item gap between Goal
   (outcome) and Project (execution); placed at `strategy-direction ·
   operate` under BO-STG-01's dominant-stage rule (steered throughout its
   life).
3. Improve-stage candidates were selected under BO-STG-01's stage-native
   test: only types whose whole life is the improve moment (Audit Finding,
   Performance Review, Improvement Proposal, Lessons Learned). Improve-stage
   *activity on existing types* (e.g. policy revisions) continues to be
   expressed through `processes_involved[]`, never by stage duplication.
   KPI-like candidates ("Optimization Recommendation", "Cost Saving") were
   rejected as measurement artifacts, not managed types.

### 2.3 Cross-catalog enrichment (resolved references only, IDM-003)

All anchors resolve against the sibling catalog HEADs (verified against live
clones); every improve record carries at least one improve-stage process
(AC-08):

- Audit Finding: `ge-improve-axtq3b` (Score Audit Findings),
  `ge-improve-mgkw59` (Review Governance Effectiveness).
- Performance Review: `sd-improve-duwd64`, `pv-improve-27r7r7`,
  `eo-improve-g3ngp3` — three-domain improve anchoring.
- Improvement Proposal: `eo-improve-us272s` (Lean Six Sigma),
  `fa-improve-emqpgr` (Cost Optimization Review).
- Lessons Learned: `ao-improve-edjyha` (Engagement and Alignment Review).
- Configuration Item: `eo-operate-4njp7b` (Operate Technology Platforms).
- Transformation Plan: `sd-operate-u6xgu5` (Steer Initiative Portfolio),
  `sd-build-7n4prh` (Build Strategic Roadmap).

### 2.4 Version manifest (first admission under CR-BO-13)

`reconciliation/version-manifest.yaml` regenerated: 64 records pinned. Per
the policy, an admission wave triggers a **catalog minor bump** at the next
release cut (`0.1.0 → 0.2.0`); the manifest records the current expectation.

### 2.5 Documentation refresh

Root README (58 → 64; stage coverage note: all 7 stages), entities README,
change-requests README, `docs/project-status.md` (improve thread closed;
coverage tables updated), CATALOG.yaml, ECF coverage poster regenerated.

## 3. Acceptance criteria (all verified locally)

- AC-01 All 64 records validate against `schemas/entity.schema.json`.
- AC-02 `scripts/check_id_system.py --strict` → CONFORMANT (64 records, 0 findings).
- AC-03 `scripts/check_entity_system.py --strict` → CONFORMANT.
- AC-04 `scripts/check_authorship.py --strict` → CONFORMANT.
- AC-05 `scripts/regenerate_catalog.py --check` → clean; `state: canonical` × 64.
- AC-06 `scripts/check_catalog_index.py --strict` → CONFORMANT.
- AC-07 Every `capabilities:*` / `processes:*` reference resolves against the
  sibling catalog HEADs (XREF gate: 165 refs, 0 findings).
- AC-08 Each improve record lists at least one improve-stage process.
- AC-09 `scripts/version_manifest.py check-version-integrity --strict` → CONFORMANT (64 records).

## 4. Out of scope

- Re-parenting Application/Environment under a CI umbrella (§2.2 decision 1).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population.
- Remaining T3 candidates.
