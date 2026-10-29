"""Unit tests for the CR-BO-13 version manifest gates.

Run: python -m pytest tests/test_version_manifest.py -q
"""
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "version_manifest.py"
MANIFEST = REPO / "reconciliation" / "version-manifest.yaml"


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True, cwd=REPO,
    )


@pytest.fixture(scope="module")
def baseline():
    """The committed tree must be conformant before we mutate anything."""
    r = run("check-version-integrity", "--strict")
    assert r.returncode == 0, r.stdout + r.stderr
    return MANIFEST.read_text()


@pytest.fixture(autouse=True)
def restore(baseline):
    yield
    MANIFEST.write_text(baseline)
    subprocess.run(["git", "checkout", "--", "entities/"], cwd=REPO)


def _record_file():
    import yaml
    d = None
    for f in (REPO / "entities/v1-alpha").glob("*/objects-object-*.yaml"):
        d = yaml.safe_load(f.read_text())
        if isinstance(d, dict) and d.get("type") == "BusinessObject":
            return f, d
    raise RuntimeError("no record found")


def test_manifest_generates_and_conforms(tmp_path):
    r = run("generate", "--output", str(tmp_path / "m.yaml"))
    assert r.returncode == 0
    import yaml
    m = yaml.safe_load((tmp_path / "m.yaml").read_text())
    assert len(m["records"]) == 58
    assert m["catalog"]["version"] == "0.1.0"


def test_ver002_substance_change_without_bump():
    f, _ = _record_file()
    original = f.read_text()
    f.write_text(original.replace("lifecycle_status: active", "lifecycle_status: active-tampered", 1))
    r = run("check-version-integrity")
    assert r.returncode == 1
    assert "VER-002" in r.stdout
    assert "substance changed" in r.stdout


def test_ver002_bump_without_substance_change():
    f, _ = _record_file()
    original = f.read_text()
    f.write_text(original.replace("version: 1.0.0", "version: 9.9.9", 1))
    r = run("check-version-integrity")
    assert r.returncode == 1
    assert "VER-002" in r.stdout
    assert "version bumped" in r.stdout


def test_ver001_phantom_manifest_record():
    import yaml
    m = yaml.safe_load(MANIFEST.read_text())
    m["records"]["objects:object-phantom-zzzzzz"] = {
        "version": "1.0.0", "content_hash": "deadbeef", "file": "x"}
    MANIFEST.write_text(yaml.safe_dump(m, sort_keys=True))
    r = run("check-version-integrity")
    assert r.returncode == 1
    assert "VER-001" in r.stdout


def test_ver003_bad_catalog_version():
    import yaml
    m = yaml.safe_load(MANIFEST.read_text())
    m["catalog"]["version"] = "not-semver"
    MANIFEST.write_text(yaml.safe_dump(m, sort_keys=True))
    r = run("check-version-integrity")
    assert r.returncode == 1
    assert "VER-003" in r.stdout


def test_xref_gate_needs_siblings():
    r = run("check-cross-references", "--caps", "/nonexistent", "--procs", "/nonexistent")
    assert r.returncode == 2
