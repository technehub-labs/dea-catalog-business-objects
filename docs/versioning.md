# Versioning Policy

## Status: Active (CR-BO-13)

How versions move in this catalog: per-record versions, the catalog-level
version, the version manifest that pins both, and the CI gates that enforce
the discipline. Modeled on the processes catalog's CR-BP-116 policy, adapted
to a content-addressed record catalog.

## Record versions (per-record SemVer)

Every record carries its own `version` field. The manifest's content hash
covers the record's *substance* — everything except `version`, `provenance`,
`state_history`, and `metadata` — so the two cannot silently drift apart:

| Change | Bump |
|---|---|
| Substance change to the record (classification, references, description semantics) | **patch** (`1.0.0 → 1.0.1`); minor/major reserved for taxonomy-level re-placement (new ECF cell requires CR-BO-10-style sign-off anyway) |
| Reference added or removed (a capability/process binding change) | **patch**, in the same CR as the reference change |
| Administrative change (`state_history` entry, `provenance.change_history`, `metadata`) | no bump — these fields are excluded from the content hash |
| New record admitted | starts at `1.0.0` (or `0.x.y` while a draft candidate); manifest gains its row in the same CR |

## Catalog version (release cuts)

The catalog-level version (in `reconciliation/version-manifest.yaml`,
`catalog.version`) moves on **release cuts**, not per-CR. The `[Unreleased]`
section of CHANGELOG.md accumulates CRs between cuts; a cut fixes the version
at that snapshot. Following the sibling catalogs' reset discipline, the first
cut will be a fresh `0.x.y`:

| Event | Bump |
|---|---|
| Admission wave lands (canonical records added) | **minor** (`0.1.0 → 0.2.0`) |
| Documentation / governance-artifact reconciliation | **patch** |
| Upstream ECF or metamodel breaking change absorbed | **major-to-`1.0.0`-track** (not yet applicable pre-1.0) |

## The version manifest

`reconciliation/version-manifest.yaml` is generated — never hand-edited — by
`scripts/version_manifest.py generate`. It pins, per record: the version, the
substance content hash, and the file path; plus the catalog version.
Regenerate it in the same CR as any record change that carries a version bump.

## CI gates (CR-BO-13)

`.github/workflows/validate-versioning.yml` runs two gates on every PR:

1. **Version Integrity (VER-001..003)** — manifest presence and coverage
   (VER-001: every record in the manifest, no phantoms); substance/version
   coherence (VER-002: a substance change requires a bump, a bump requires a
   substance change); catalog-version shape (VER-003: SemVer `N.M.P`).
2. **Cross-Reference (XREF-001..002)** — clones the capabilities and
   processes catalogs at HEAD and verifies every `capabilities_consumed[]` /
   `processes_involved[]` reference resolves. A sibling-catalog change that
   removes or renames an id breaks this gate here, catching drift at the
   consumer rather than at the producer.

### What each gate does *not* do

- The XREF gate does not track sibling *content* changes (only existence of
  the referenced id); semantic coupling is governed by the ECF conformance
  chain in the metamodel, not by this catalog.
- The VER gate does not version `README.md`/`aspects.md` docs; record-docs
  drift is covered by the CST suite and review.

## Release-cut procedure

1. All CI gates green on `main` at the cut SHA (the pre-release verification
   contract, per the sibling catalogs' hardening A).
2. Move `[Unreleased]` → `[vN.M.P] - YYYY-MM-DD` in CHANGELOG.md; add a fresh
   empty `[Unreleased]` on top.
3. `python scripts/version_manifest.py generate --catalog-version N.M.P`;
   commit the manifest with the cut.
4. Tag `vN.M.P` at the SHA; push the tag. Record the row in the prior-cut
   history table below.

## Prior-cut history

| version | date | cut by CR | commit SHA | gates |
| ------- | ---- | --------- | ---------- | ----- |
| _none yet — first cut pending_ | | | | |
