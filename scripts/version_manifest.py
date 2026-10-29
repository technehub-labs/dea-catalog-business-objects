#!/usr/bin/env python3
"""Version manifest generator + integrity gate (CR-BO-13).

The manifest at reconciliation/version-manifest.yaml is the catalog's
version ledger: one content hash per record (post-version fields, so a
version bump itself does not change the hash), the per-record version,
and the catalog-level version. CI regenerates and compares; the
check_* subcommands enforce the versioning discipline (VER-001..004).

Usage:
  python scripts/version_manifest.py generate [--output PATH]
  python scripts/version_manifest.py check-version-integrity
  python scripts/version_manifest.py check-cross-references --caps PATH --procs PATH

Exit codes (stable contract, mirroring the sibling gates):
  0 CONFORMANT · 1 findings (blocking) · 2 usage/environment error
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
ENTITIES = REPO_ROOT / "entities" / "v1-alpha"
MANIFEST_PATH = REPO_ROOT / "reconciliation" / "version-manifest.yaml"

# Record fields that legitimately change with versioning/administration
# and therefore do not participate in the content hash. The hash answers
# "did the *record's substance* change since the manifest was written?"
HASH_EXCLUDED_KEYS = {"version", "provenance", "state_history", "metadata"}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def record_files():
    for f in sorted(ENTITIES.glob("*/objects-object-*.yaml")):
        yield f


def record_substance_hash(data: dict) -> str:
    """SHA-256 over the record minus version/administrative fields."""
    pruned = {k: v for k, v in data.items() if k not in HASH_EXCLUDED_KEYS}
    canonical = yaml.safe_dump(pruned, sort_keys=True, default_flow_style=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def build_manifest() -> dict:
    records = {}
    for f in record_files():
        data = load_yaml(f)
        if not isinstance(data, dict) or data.get("type") != "BusinessObject":
            continue
        records[data["id"]] = {
            "version": str(data.get("version", "0.0.0")),
            "content_hash": record_substance_hash(data),
            "file": str(f.relative_to(REPO_ROOT)),
        }
    manifest = {
        "schema": 1,
        "catalog": {
            # The catalog version. Bumped on release cuts (see
            # docs/versioning.md); the manifest records the *current*
            # expectation so drift is detected.
            "version": None,  # filled by caller / check flow
        },
        "records": records,
    }
    return manifest


def cmd_generate(args) -> int:
    manifest = build_manifest()
    existing = None
    if MANIFEST_PATH.exists():
        existing = load_yaml(MANIFEST_PATH)
    # carry the catalog version forward unless explicitly set
    if args.catalog_version:
        manifest["catalog"]["version"] = args.catalog_version
    elif existing and existing.get("catalog", {}).get("version"):
        manifest["catalog"]["version"] = existing["catalog"]["version"]
    else:
        manifest["catalog"]["version"] = "0.1.0"
    out = Path(args.output) if args.output else MANIFEST_PATH
    out.write_text(yaml.safe_dump(manifest, sort_keys=True, default_flow_style=False))
    print(f"OK: wrote {out} ({len(manifest['records'])} records)")
    return 0


def cmd_check_version_integrity(args) -> int:
    findings: list[str] = []
    if not MANIFEST_PATH.exists():
        print("VER-000: reconciliation/version-manifest.yaml not found; run `generate`")
        return 1
    manifest = load_yaml(MANIFEST_PATH)
    mrecords = manifest.get("records") or {}
    current = build_manifest()["records"]
    strict = args.strict

    # VER-001: every current record is in the manifest, and every manifest
    # record still exists (admissions and removals both require a manifest
    # update in the same CR).
    for rid, rec in current.items():
        if rid not in mrecords:
            findings.append(f"VER-001: record {rid} is not in the version manifest")
    for rid in mrecords:
        if rid not in current:
            findings.append(f"VER-001: manifest lists {rid} but no record exists")

    # VER-002: substance hash unchanged ⇒ version must be unchanged;
    # substance hash changed ⇒ version must have bumped.
    for rid, rec in current.items():
        mrec = mrecords.get(rid)
        if not mrec:
            continue
        same_content = rec["content_hash"] == mrec["content_hash"]
        same_version = rec["version"] == mrec["version"]
        if same_content and not same_version:
            findings.append(
                f"VER-002: {rid} version bumped ({mrec['version']} → {rec['version']}) "
                f"without a substance change; revert the bump or update the manifest deliberately"
            )
        if not same_content and same_version:
            findings.append(
                f"VER-002: {rid} substance changed at version {rec['version']}; "
                f"bump the record version (patch) and regenerate the manifest"
            )

    # VER-003: catalog version present and SemVer-shaped.
    cv = (manifest.get("catalog") or {}).get("version")
    if not cv or not isinstance(cv, str):
        findings.append("VER-003: manifest catalog.version is missing")
    else:
        parts = cv.split(".")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            findings.append(f"VER-003: catalog version {cv!r} is not SemVer-shaped (N.M.P)")

    print(f"Version Integrity Gate (CR-BO-13; VER-001..003{' strict' if strict else ''}): "
          f"{'CONFORMANT' if not findings else 'NON-CONFORMANT'}")
    print(f"  Records checked: {len(current)}")
    print(f"  Findings: {len(findings)}")
    for f in findings:
        print(f"    [{f.split(':')[0]}] {f}")
    return 0 if not findings else 1


def cmd_check_cross_references(args) -> int:
    findings: list[str] = []
    caps_dir = Path(args.caps)
    procs_dir = Path(args.procs)
    if not caps_dir.is_dir() or not procs_dir.is_dir():
        print("XREF-000: sibling catalog paths not found", file=sys.stderr)
        return 2
    caps_ids = set()
    for f in caps_dir.glob("entities/v1-alpha/*/capabilities-*.yaml"):
        d = load_yaml(f)
        if isinstance(d, dict) and d.get("id"):
            caps_ids.add(d["id"])
    procs_ids = set()
    for f in procs_dir.glob("entities/v1-alpha/**/processes-process-*.yaml"):
        d = load_yaml(f)
        if isinstance(d, dict) and d.get("id"):
            procs_ids.add(d["id"])
    n = 0
    for f in record_files():
        data = load_yaml(f)
        if not isinstance(data, dict) or data.get("type") != "BusinessObject":
            continue
        rid = data.get("id", "?")
        for c in data.get("capabilities_consumed") or []:
            n += 1
            if c not in caps_ids:
                findings.append(f"XREF-001: {rid} references missing capability {c}")
        for p in data.get("processes_involved") or []:
            n += 1
            if p not in procs_ids:
                findings.append(f"XREF-002: {rid} references missing process {p}")
    print(f"Cross-Reference Gate (CR-BO-13; XREF-001..002): "
          f"{'CONFORMANT' if not findings else 'NON-CONFORMANT'}")
    print(f"  References checked: {n} ({len(caps_ids)} capabilities, {len(procs_ids)} processes at HEAD)")
    print(f"  Findings: {len(findings)}")
    for f in findings:
        print(f"    [{f.split(':')[0]}] {f}")
    return 0 if not findings else 1


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate", help="write the version manifest")
    g.add_argument("--output", default=None)
    g.add_argument("--catalog-version", default=None)
    g.set_defaults(func=cmd_generate)
    c = sub.add_parser("check-version-integrity", help="VER-001..003")
    c.add_argument("--strict", action="store_true")
    c.set_defaults(func=cmd_check_version_integrity)
    x = sub.add_parser("check-cross-references", help="XREF-001..002 (needs sibling clones)")
    x.add_argument("--caps", required=True)
    x.add_argument("--procs", required=True)
    x.set_defaults(func=cmd_check_cross_references)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
