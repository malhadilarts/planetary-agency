#!/usr/bin/env python3
"""Validate submission metadata; does not check mathematical soundness."""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1] / "research" / "submissions"
REQUIRED = ("id", "date", "track", "author", "model", "title", "claim", "status", "evidence")
STATUSES = {"proposed", "testing", "replicated", "refuted", "independently-reviewed"}
seen = set()
errors = []
for path in sorted(ROOT.glob("*.json")):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("not a JSON object")
        for key in REQUIRED:
            if key not in data or not isinstance(data[key], str):
                errors.append(f"{path}: missing/non-string {key}")
        if data.get("track") not in ("A", "B", "C", "D"):
            errors.append(f"{path}: invalid track")
        if data.get("status") not in STATUSES:
            errors.append(f"{path}: invalid status")
        try:
            date.fromisoformat(data.get("date", ""))
        except ValueError:
            errors.append(f"{path}: invalid ISO date")
        if data.get("id") in seen:
            errors.append(f"{path}: duplicate id")
        seen.add(data.get("id"))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: {exc}")
print("\n".join(errors) if errors else "All research records structurally valid.")
raise SystemExit(bool(errors))
