# Business Objects Catalog Changelog

All notable changes to this catalog are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### CR-BO-05: First Phase-2 Admission (Seed Business Object Records, BO Profile, Early-Exit Drop)

First content admission — the catalog's population phase begins. Eight seed Business Object records land at the flat layout (`party`: Customer; `transaction`: Order; `offering`: Product; `financial-instrument`: Invoice, Payment, Grant; `legal-instrument`: Contract; `technology-control`: Feature Flag) with content-derived hash6 ids, per-record READMEs (IDM-007), and the schema-required envelope plus `lifecycle_status: active`. Every `capabilities_consumed[]` / `processes_involved[]` reference was resolved against the live sibling catalogs before landing (capabilities: 28 canonical records; processes: 3,598; owner/stakeholders/events/data_entities deliberately unset — their catalogs are empty or unbound, and IDM-003 forbids unresolved references). Integrity defects the empty tree had masked are closed: the entity-system registry's identity pattern is aligned to the org-wide `objects:object-*` form its own IDM-001 gate enforces (the two gates previously disagreed); the `BusinessObject` envelope profile is registered (ES-002 was structurally unresolvable while `profiles: {}`); `audit.author` / `audit.reviewed_by` are registered in the authorship registry per cardinal-rules R1; the `infer_state` regenerator bug (`{id}.yaml` probe, ids contain `:`) is fixed so CATALOG.yaml emits `state: canonical` x8; the stale committed CATALOG.yaml (CR-BO-03/04 landed without regeneration) is refreshed; `entities/v1-alpha/README.md`'s non-conformant id form is corrected; the `ci.yml` empty-tree early-exit is dropped; and the metaframework CI checkout is pinned to `v2.6.0` (CST-013/014 require a release-tag pin; main was failing both). All gates pass against real records for the first time: IDM-001..007 CONFORMANT (8 records), ES gate CONFORMANT, AUT gate CONFORMANT, CST 16/16, index `state: canonical` x8. Carrier: `change-requests/CR-BO-05-first-admission-seed-business-objects.md`.

### CR-BO-04: Entity System Stage 5-6 (BO slice of the General Entity System institutionalisation. The BO catalog has 0 entity records at the time of CR landing; the gate is vacuously CONFORMANT. Slice)

Business Objects

### CR-BO-03: Authorship Cardinal Rule (R1, R2) - Org-Wide Propagation Slice

User directive 2026-10-13: "no `Coder` / `Agent` / agent or tool names in any
authorship field of any published artifact". The CR-BP-118 cardinal rules (R1
and R2) are propagated to this repo. New blocking gate
`scripts/check_authorship.py` (CR-BP-118 / AUT-001..003), data-driven from
`reconciliation/authorship-fields.yaml` (allowlist
`{Emmanuel A. Otchere, TechNeHub Labs}`; denylist
`{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}`).
A retroactive sweep rewrites every authorship-metadata hit in the repo: 2
files (CR-BO-01, CR-BO-02), 2 textual replacements (one per file). 0 entity
content changes; 0 id changes; 0 cross-reference changes. The BO repo shares
the 118a field shape (CR-doc metadata only) and uses the same registry
fields; no per-repo extension is needed. CI wiring: new workflow
`.github/workflows/validate-authorship.yml` runs the gate in `--strict` mode
on every push and PR. 21/21 `test_check_authorship` pass. Carrier:
`change-requests/CR-BO-03-authorship-cardinal-rule.md`.

## [v2.5.0-migration] - 2026-09-08

CR-BO-02 implementation: ECF Domain enum migration to the v2.5.0 canonical Domain set (carried by `technehub-labs/dea-metaframework` v2.5.0; CR-ECF-008 + ADR-ECF-003). One of seven Domains renamed: Domain 6 `operations-enablement` → `enablement-operations` (kebab-case), driven by the Domain/Stage Orthogonality Stress Test. 4 files re-keyed (1 schema, 1 README, 1 entities README, 1 CHANGELOG entry). See `change-requests/CR-BO-02-ecf-domain-enum-migration-v250.md` for the full mapping.

**Unchanged**: Domain number (6), matrix position, semantic anchor (`Execution`), seven-Domain partition, seven lifecycle Stages, Stage 5 name (`Operate`), and the `ECF = Domain × Stage = 49 coordinates` construction.

## [v2.4.0-migration] - 2026-09-07

CR-BO-01 implementation: bundled ECF Domain enum migration to the v2.4.0
canonical Domain set (carried by `technehub-labs/dea-metaframework` v2.4.0;
CR-ECF-006 + CR-ECF-007, governed by ADR-ECF-001 + ADR-ECF-002). This repo
was missed by the v2.3.0 wave ground-truth scan and was still carrying the
v2.2.0 Domain enum; both waves applied in a single step. `supply-resources`
-> `strategy-direction`; `people-organization` -> `agency-organization`;
`customer-demand` -> `party-relationship`; `product-offering` ->
`product-value`; `operations-delivery` -> `enablement-operations`;
`finance-value` -> `finance-accounting`. 3 files re-keyed (README,
entity.schema.json, entities/v1-alpha/README.md). No entity YAMLs exist yet;
nothing to migrate at the entity level.
