from __future__ import annotations

import csv
import json
from pathlib import Path

from render_record_readmes import ROOT, RECORDS_ROOT, extract_command


DOCS_ROOT = ROOT / "docs" / "track_10min_16mb"


def load_inventory() -> dict[str, dict[str, str]]:
    inventory_path = DOCS_ROOT / "inventory.csv"
    rows: dict[str, dict[str, str]] = {}
    with inventory_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows[row["record_slug"]] = row
    return rows


def list_source_logs(source_dir: Path) -> list[str]:
    patterns = ["train*.log", "train_v*.txt", "ternary_log_*.txt"]
    files: list[Path] = []
    for pattern in patterns:
        files.extend(sorted(source_dir.glob(pattern)))
    return [str(path.relative_to(ROOT)) for path in files]


def parse_required_packages(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> None:
    inventory = load_inventory()
    docs_records = DOCS_ROOT / "records"
    for record_dir in sorted(docs_records.iterdir()):
        if not record_dir.is_dir():
            continue
        repro_path = record_dir / "reproduction.json"
        if not repro_path.exists():
            continue
        data = json.loads(repro_path.read_text())
        slug = data["record_slug"]
        source_dir = RECORDS_ROOT / slug
        inv = inventory.get(slug, {})

        submission_path = None
        for name in ("submission.json", "submission_ternary.json"):
            candidate = source_dir / name
            if candidate.exists():
                submission_path = candidate
                break
        submission = {}
        if submission_path:
            submission = json.loads(submission_path.read_text())

        source_readme = source_dir / "README.md"
        data["record_dir"] = str(source_dir.relative_to(ROOT))
        data["status"] = data.get("status") or inv.get("status") or "unknown"
        data["family"] = data.get("family") or inv.get("family")
        data["metric_mode"] = data.get("metric_mode") or inv.get("metric_mode")
        data["source_readme"] = str(source_readme.relative_to(ROOT)) if source_readme.exists() else data.get("source_readme", "")
        data["source_submission"] = str(submission_path.relative_to(ROOT)) if submission_path else data.get("source_submission", "")
        if not data.get("source_script"):
            for name in ("train_gpt.py", "train_gpt_v5.py", "train_gpt_cuda_ternary.py"):
                candidate = source_dir / name
                if candidate.exists():
                    data["source_script"] = str(candidate.relative_to(ROOT))
                    break
        data["source_logs"] = list_source_logs(source_dir)
        data["author"] = data.get("author") or submission.get("author")
        data["date"] = data.get("date") or (submission.get("date") or "")[:10]
        data["claimed_run_name"] = data.get("claimed_run_name") or submission.get("name")
        data["submission_blurb"] = data.get("submission_blurb") or submission.get("blurb")
        data["claimed_method_summary"] = data.get("claimed_method_summary") or submission.get("blurb")
        data["claimed_metric_name"] = data.get("claimed_metric_name") or "val_bpb"
        if data.get("claimed_val_bpb") is None and submission.get("val_bpb") is not None:
            data["claimed_val_bpb"] = submission.get("val_bpb")
        if data.get("claimed_val_loss") is None and submission.get("val_loss") is not None:
            data["claimed_val_loss"] = submission.get("val_loss")
        if data.get("claimed_artifact_bytes") is None and submission.get("bytes_total") is not None:
            data["claimed_artifact_bytes"] = submission.get("bytes_total")
        if not data.get("required_packages"):
            data["required_packages"] = parse_required_packages(inv.get("required_packages"))
        if not data.get("exact_command") and source_readme.exists():
            data["exact_command"] = extract_command(source_readme)
        repro_path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n")


if __name__ == "__main__":
    main()
