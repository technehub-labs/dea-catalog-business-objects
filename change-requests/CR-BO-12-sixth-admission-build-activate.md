# CR-BO-12: Sixth Admission (Build and Activate Stage-Native Records, 4 Records)

| Field | Value |
|-------|-------|
| **CR** | CR-BO-12 |
| **Title** | Sixth Admission (Build and Activate Stage-Native Records, 4 Records) |
| **Status** | Merged |
| **Layer** | L2 (Business Operating Model) |
| **Owner** | Emmanuel A. Otchere |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-30 |
| **Depends on** | CR-BO-10 (BO-STG-01 adopted), CR-BO-11 (conceive/design/retire populated) |
| **Companion to** | — |

## 1. Purpose

Continues the CR-BO-10 scope under the adopted BO-STG-01 rule: populates the
two remaining empty ECF stages — `build` and `activate` — with stage-native
records. After this admission, **all seven ECF stages are populated**.

## 2. Changes

### 2.1 Four stage-native Business Object records

| id | object_class | ECF (domain, stage) | First cell populated |
|---|---|---|---|
| `objects:object-release-candidate-wed4tk` | technology-control / release-candidate | enablement-operations · build | first `build`-stage record |
| `objects:object-training-program-r8fpt3` | work-item / training-program | agency-organization · build | — |
| `objects:object-onboarding-program-mrun5r` | work-item / onboarding-program | party-relationship · activate | first `activate`-stage record |
| `objects:object-party-credential-kaqfq8` | technology-control / party-credential | party-relationship · activate | — |

Each subtree carries README.md (IDM-007) and an aspects.md deep-dive. Hash
suffixes content-derived at admission per CR-BO-05 §2.6.

### 2.2 Cross-catalog enrichment (resolved references only, IDM-003)

- Release Candidate: `eo-build-nmmmt6` (Acquire Technology Assets).
- Training Program: `ao-build-w2qurd` (Acquire Agents),
  `ao-build-9my4jr` (Build Regulated Agent Pool).
- Onboarding Program: `pr-activate-6qzuve` (Onboard Regulated Party
  Relationship).
- Party Credential: `pr-activate-6qzuve` (same process — issuance is part of
  onboarding; AC-08 stage coherence holds).

No forward references; no empty `processes_involved`.

### 2.3 Post-merge housekeeping (workflow step 8)

CR-BO-11 status → `Merged`; `CATALOG.yaml` refreshed (open CRs 5 → 4 before
this CR opens).

### 2.4 Documentation refresh

Root README (54 → 58), entities README, change-requests README, CATALOG.yaml.

## 3. Acceptance criteria (all verified locally)

- AC-01..AC-07: identical to CR-BO-11 §3.
- AC-08 (from CR-BO-10): each non-operate record lists at least one process at
  its own ECF stage — verified for all four.

## 4. Out of scope

- Improve-stage records (still deferred; processes#215).
- `owner` / `stakeholders[]` / `events[]` / `data_entities[]` population.
