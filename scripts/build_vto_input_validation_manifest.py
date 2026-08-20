#!/usr/bin/env python3
"""Build the public VTO fixture manifest from scenario specs and image bytes."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
from typing import Any

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
SUITE_ROOT = REPO_ROOT / "vto" / "input-validation" / "v1"
SCENARIOS_PATH = SUITE_ROOT / "scenarios.json"
MANIFEST_PATH = SUITE_ROOT / "manifest.json"
IMAGE_SUFFIXES = {".jpeg", ".jpg", ".png", ".webp"}


def _render_media_variant(spec: dict[str, Any]) -> bytes:
    source = SUITE_ROOT / spec["source"]
    with Image.open(source) as image:
        if spec["format"] == "JPEG":
            rendered = image.convert("RGB")
            options = {
                "quality": spec["quality"],
                "subsampling": 0,
                "progressive": True,
                "optimize": False,
            }
        elif spec["format"] == "WEBP":
            rendered = image.convert("RGBA")
            options = {
                "lossless": True,
                "quality": 100,
                "method": 6,
                "exact": True,
            }
        else:  # pragma: no cover - source schema owns the closed set
            raise ValueError(f"unsupported generated media format: {spec['format']}")
        buffer = io.BytesIO()
        rendered.save(buffer, format=spec["format"], **options)
    return buffer.getvalue()


def _sync_media_variants(source: dict[str, Any], *, check: bool) -> None:
    for spec in source.get("generated_media_variants", []):
        destination = SUITE_ROOT / spec["path"]
        expected = _render_media_variant(spec)
        if check:
            if not destination.exists() or destination.read_bytes() != expected:
                raise SystemExit(f"stale generated media variant: {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(expected)


def _image_contract(path: Path) -> dict[str, Any]:
    content = path.read_bytes()
    with Image.open(path) as image:
        image.load()
        width, height = image.size
        mode = image.mode
        image_format = image.format
        alpha_extrema = (
            image.getchannel("A").getextrema() if "A" in image.getbands() else None
        )
    contract = {
        "path": path.relative_to(SUITE_ROOT).as_posix(),
        "sha256": hashlib.sha256(content).hexdigest(),
        "bytes": len(content),
        "width": width,
        "height": height,
        "mode": mode,
        "format": image_format,
    }
    if alpha_extrema is not None:
        contract["alpha_min"] = alpha_extrema[0]
        contract["alpha_max"] = alpha_extrema[1]
        contract["has_transparency"] = alpha_extrema[0] < 255
    return contract


def build_manifest() -> dict[str, Any]:
    source = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
    cases = source["cases"]
    known_folders = {case["folder"] for case in cases}
    if len(known_folders) != len(cases):
        raise ValueError("scenario folders must be unique")

    owned_paths: set[Path] = set()
    built_cases: list[dict[str, Any]] = []
    for case in cases:
        folder = SUITE_ROOT / case["folder"]
        files = sorted(
            path
            for path in folder.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
        )
        if not files:
            raise ValueError(f"scenario has no image files: {case['id']}")
        owned_paths.update(files)
        built_cases.append({**case, "files": [_image_contract(path) for path in files]})

    discovered = {
        path
        for path in SUITE_ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    }
    unowned = sorted(
        path.relative_to(SUITE_ROOT).as_posix() for path in discovered - owned_paths
    )
    if unowned:
        raise ValueError(f"images are not owned by a scenario: {unowned}")

    return {key: value for key, value in source.items() if key != "cases"} | {
        "cases": built_cases
    }


def _serialized_case(case: dict[str, Any]) -> str:
    return json.dumps(case, indent=2, sort_keys=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
    _sync_media_variants(source, check=args.check)
    manifest = build_manifest()
    expected = json.dumps(manifest, indent=2, sort_keys=False) + "\n"
    if args.check:
        actual = MANIFEST_PATH.read_text(encoding="utf-8")
        if actual != expected:
            raise SystemExit(f"stale generated manifest: {MANIFEST_PATH}")
        for case in manifest["cases"]:
            case_path = SUITE_ROOT / case["folder"] / "case.json"
            if case_path.read_text(encoding="utf-8") != _serialized_case(case):
                raise SystemExit(f"stale generated case: {case_path}")
        return
    for case in manifest["cases"]:
        case_path = SUITE_ROOT / case["folder"] / "case.json"
        case_path.write_text(_serialized_case(case), encoding="utf-8")
    MANIFEST_PATH.write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
