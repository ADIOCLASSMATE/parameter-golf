from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "docs" / "track_10min_16mb"
RECORD_DOCS = DOCS_ROOT / "records"


def load_rows() -> list[dict[str, str]]:
    path = DOCS_ROOT / "inventory.csv"
    with path.open() as f:
        return list(csv.DictReader(f))


def write_csv(rows: list[dict[str, str]]) -> None:
    path = DOCS_ROOT / "inventory.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "record_slug",
                "author",
                "claimed_val_bpb",
                "claimed_val_loss",
                "family",
                "metric_mode",
                "status",
                "submission_file",
                "script_file",
                "log_files",
                "required_packages",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    lines = [
        "# track_10min_16mb inventory",
        "",
        "This index normalizes all current record folders under `records/track_10min_16mb` and links to the local documentation scaffold for later reproduction work.",
        "",
        "| Record | Author | Claimed BPB | Family | Metric mode | Status | Local doc |",
        "|---|---|---:|---|---|---|---|",
    ]
    for row in rows:
        slug = row["record_slug"]
        lines.append(
            f"| `{slug}` | {row['author'] or 'N/A'} | {row['claimed_val_bpb'] or 'N/A'} | "
            f"{row['family'] or 'N/A'} | {row['metric_mode'] or 'N/A'} | `{row['status'] or 'unknown'}` | "
            f"[doc](records/{slug}/README.md) |"
        )
    (DOCS_ROOT / "inventory.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = load_rows()
    for row in rows:
        slug = row["record_slug"]
        repro = RECORD_DOCS / slug / "reproduction.json"
        if not repro.exists():
            continue
        data = json.loads(repro.read_text())
        row["status"] = data.get("status") or row.get("status") or "unknown"
        if not row.get("author") and data.get("author"):
            row["author"] = data["author"]
        if not row.get("claimed_val_bpb") and data.get("claimed_val_bpb") is not None:
            row["claimed_val_bpb"] = str(data["claimed_val_bpb"])
        if not row.get("claimed_val_loss") and data.get("claimed_val_loss") is not None:
            row["claimed_val_loss"] = str(data["claimed_val_loss"])
        if not row.get("family") and data.get("family"):
            row["family"] = data["family"]
        if not row.get("metric_mode") and data.get("metric_mode"):
            row["metric_mode"] = data["metric_mode"]
        if data.get("source_submission"):
            row["submission_file"] = Path(data["source_submission"]).name
        if data.get("source_script"):
            row["script_file"] = Path(data["source_script"]).name
        if data.get("source_logs"):
            row["log_files"] = ", ".join(Path(p).name for p in data["source_logs"])
        if data.get("required_packages") is not None:
            row["required_packages"] = ", ".join(data["required_packages"])
    write_csv(rows)
    write_md(rows)


if __name__ == "__main__":
    main()
