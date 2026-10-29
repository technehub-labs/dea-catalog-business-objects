# Project Status

Population progress, coverage, and open threads for the Business Objects
catalog. This document answers *"where is the catalog now, and what's next?"* —
the README answers *"what is this and how do I use it?"*.

## Population progress

Phase 2 population began from an 8-record seed and has grown through five
admission waves and two scope-setting proposals. Each admission is a merged
Change Request (full register: [`change-requests/README.md`](../change-requests/README.md)).

| Admission | CR | Records | Scope |
|---|---|---|---|
| Seeds | [CR-BO-05](../change-requests/CR-BO-05-first-admission-seed-business-objects.md) | 8 | Order-to-cash core, instruments, controls |
| Wave-2 T1 | [CR-BO-07](../change-requests/CR-BO-07-second-admission-wave2-t1.md) | 22 | Commercial-core extension ([CR-BO-06](../change-requests/CR-BO-06-second-admission-wave-proposal.md) scope) |
| Wave-2 T2 | [CR-BO-08](../change-requests/CR-BO-08-third-admission-wave2-t2.md) | 16 | Cross-industry records, 8 sector lenses; `resource` + `location` classes |
| T3-ready | [CR-BO-09](../change-requests/CR-BO-09-fourth-admission-t3-ready.md) | 3 | Goal, Forecast, Tax Record; first `strategy-direction` record |
| Stage-native | [CR-BO-11](../change-requests/CR-BO-11-fifth-admission-stage-native.md) | 5 | First `conceive`/`design`/`retire` cells ([CR-BO-10](../change-requests/CR-BO-10-ecf-stage-diversification-proposal.md) scope) |
| Stage-native II | [CR-BO-12](../change-requests/CR-BO-12-sixth-admission-build-activate.md) | 4 | First `build`/`activate` cells |
| Improve stage | [CR-BO-14](../change-requests/CR-BO-14-seventh-admission-improve-and-completion.md) | 6 | Audit Finding, Performance Review, Improvement Proposal, Lessons Learned (first `improve` cells) + Configuration Item, Transformation Plan (taxonomy completion) |
| Telecom / DSP | [CR-BO-15](../change-requests/CR-BO-15-eighth-admission-telecom-dsp.md) | 10 | Telecom-operator lens: Subscriber, Tariff Plan, Service Instance, Usage Record, Network Asset, Service Number, Coverage Area, SIM Profile, Prepaid Balance, Interconnect Agreement (MCSP-aligned; `resource`/`location` proven industry-portable) |
| **Total** | | **74** | |

## Coverage

| Dimension | Coverage |
|---|---|
| Records | 74 canonical, all `lifecycle_status: active` |
| Classes | 9 of 9 in-use classes: party (8), transaction (11), offering (6), financial-instrument (12), legal-instrument (4), work-item (7), technology-control (6), resource (3), location (1) |
| ECF domains | 7 of 7 populated |
| ECF stages | 7 of 7 populated (improve landed in CR-BO-14) |
| Sector lenses | 9 industry lenses represented (healthcare, government, non-profit, insurance, banking, education, manufacturing, retail, telecom), explicitly labeled |
| Cross-references | 187, all resolved (IDM-003); enforced in CI by the XREF gate (CR-BO-13) |

**Stage coverage:** operate 53 · conceive 2 · design 1 · build 2 · activate 2 · improve 4 · retire 2.

## Open threads

Work the catalog is waiting on, each blocked by a sibling catalog or a
scope decision — none is actionable in this repo alone:

| Thread | Blocked on | Tracking |
|---|---|---|
| Quality-management capability reference (Lot/Batch record) | capabilities catalog record | [dea-catalog-business-capabilities#114](https://github.com/technehub-labs/dea-catalog-business-capabilities/issues/114) |
| Process anchors for Citizen, Partner, License, Consent Record | processes catalog records | [processes#215](https://github.com/technehub-labs/dea-catalog-business-processes/issues/215) |
| `owner[]` / `stakeholders[]` / `events[]` / `data_entities[]` population | actors, stakeholders, and data catalogs binding | CR-BO-05 §2.2 (deliberately unset) |
| Remaining T3 candidates (Dataset, Report, Task, Department, API, …) | consuming capabilities/processes existing | [CR-BO-06](../change-requests/CR-BO-06-second-admission-wave-proposal.md) §3 T3 list |
| Thin cells (`design` has one record) | candidate proposals | open |

## Maintenance conventions

- After every admission merge: mark the CR `Merged` and refresh `CATALOG.yaml` (workflow step 8; the regenerator counts non-`Merged` CRs as open).
- After editing a `docs/diagrams/*.puml` source: re-encode to the `plantuml.com` server URL and update the README embed.
- The regenerator's `last_modified` is read from git; the CI checkout sets the origin URL with a `.git` suffix — match that form locally when regenerating.
