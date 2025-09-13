#!/usr/bin/env python3
"""
Patch the downloaded ESI OpenAPI JSON to fit our generator needs.

Usage:
  - Overwrite in-place (default):
      python scripts/patch_openapi.py --in pyesi-openapi/openapi.json
  - Write to a different file:
      python scripts/patch_openapi.py --in pyesi-openapi/openapi.json --out pyesi-openapi/openapi.patched.json

Idempotent: Running multiple times yields the same result.

What it changes:
  1) info.contact -> sets name/url/email
  2) info.license -> sets name/identifier
  3) info.title   -> "PyESI (OpenAPI) - EVE Stable Infrastructure (ESI)"
  4) info.summary -> generated concise summary
  5) info.description -> generated description
  6) components.parameters.CompatibilityDate.required -> false

How to run:
`uv run python scripts/patch_openapi.py --in openapi.json`

Notes:
- We intentionally do NOT change enums or defaults for CompatibilityDate here,
  because our generator template handles defaulting to "2025-08-26" at codegen time.
- We only rely on Python stdlib.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

# Contact constants
CONTACT_NAME = "arxbombus"
CONTACT_URL = "https://github.com/arxbombus"
CONTACT_EMAIL = "arxbombus@gmail.com"

# License constants
LICENSE_NAME = "MIT"
LICENSE_IDENTIFIER = "MIT"

# Info constants
TITLE = "PyESI (OpenAPI) - EVE Stable Infrastructure (ESI)"
# Generated content (short and long)
SUMMARY = "Type-safe Python SDK generated with openapi-generator (https://openapi-generator.tech/) using OpenAPI specification for EVE Online's ESI. Predictable client generation and stable typing in Python."
DESCRIPTION = (
    "This python SDK was generated with openapi-generator (https://openapi-generator.tech/) using OpenAPI specification for EVE Stable Infrastructure / EVE Swagger Interface (ESI) (https://developers.eveonline.com/api-explorer) "
    "and is lightly normalized to improve client generation via our custom templates. It preserves endpoint coverage "
    "from CCP's published specification while adjusting metadata and select parameter shapes "
    "for a more ergonomic, type-safe Python SDK."
)


def _ensure_dict(node: Dict[str, Any], key: str) -> Dict[str, Any]:
    child = node.get(key)
    if not isinstance(child, dict):
        child = {}
        node[key] = child
    return child


def patch_openapi(doc: Dict[str, Any]) -> Dict[str, Any]:
    # Ensure "info" exists and is a dict
    info = _ensure_dict(doc, "info")

    # 1) info.contact
    contact = _ensure_dict(info, "contact")
    contact["name"] = CONTACT_NAME
    contact["url"] = CONTACT_URL
    contact["email"] = CONTACT_EMAIL

    # 2) info.license
    license_obj = _ensure_dict(info, "license")
    license_obj["name"] = LICENSE_NAME
    license_obj["identifier"] = LICENSE_IDENTIFIER
    if "url" in license_obj:
        license_obj.pop("url")

    # 3) info.title
    info["title"] = TITLE

    # 4) info.summary
    info["summary"] = SUMMARY

    # 5) info.description
    info["description"] = DESCRIPTION

    # 6) components.parameters.CompatibilityDate.required = false
    components = doc.get("components")
    if isinstance(components, dict):
        parameters = components.get("parameters")
        if isinstance(parameters, dict):
            comp_date = parameters.get("CompatibilityDate")
            if isinstance(comp_date, dict):
                # Only flip to False if it exists; do not add otherwise.
                comp_date["required"] = False

    return doc


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch ESI OpenAPI JSON for our generator.")
    parser.add_argument(
        "--in",
        dest="in_path",
        required=True,
        help="Path to the downloaded openapi.json",
    )
    parser.add_argument(
        "--out",
        dest="out_path",
        default=None,
        help="Optional output path. If omitted, overwrites the input file in-place.",
    )
    parser.add_argument(
        "--indent",
        dest="indent",
        type=int,
        default=2,
        help="Pretty-print JSON with this indent (default: 2)",
    )
    args = parser.parse_args()

    in_path = Path(args.in_path)
    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    with in_path.open("r", encoding="utf-8") as f:
        try:
            doc = json.load(f)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse JSON from {in_path}: {e}")

    patched = patch_openapi(doc)

    out_path = Path(args.out_path) if args.out_path else in_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Write with stable key ordering for deterministic diffs
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(patched, f, ensure_ascii=False, indent=args.indent, sort_keys=True)
        f.write("\n")

    print(f"Patched OpenAPI written to: {out_path}")


if __name__ == "__main__":
    main()
