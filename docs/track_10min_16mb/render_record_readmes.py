from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "docs" / "track_10min_16mb"
RECORDS_ROOT = ROOT / "records" / "track_10min_16mb"


def extract_command(source_readme: Path) -> str:
    if not source_readme.exists():
        return ""
    text = source_readme.read_text()
    blocks = re.findall(r"```bash\n(.*?)```", text, re.DOTALL)
    candidates = [b.strip() for b in blocks if "torchrun" in b or "bash eval/eval.sh" in b or "bash run_cuda_ternary.sh" in b]
    if not candidates:
        return ""
    for block in reversed(candidates):
        if "torchrun" in block:
            return block
    return candidates[-1]


def bullets(values: list[str]) -> str:
    if not values:
        return "- none"
    return "\n".join(f"- `{value}`" for value in values)


def scalar_text(value) -> str:
    if value is None or value == "":
        return "not yet recorded"
    return str(value)


def render_metric_semantics(data: dict) -> str:
    mode = data.get("metric_mode") or "unknown"
    notes = []
    lower = mode.lower()
    if "mean" in lower or "3-seed" in lower or "4-run" in lower or "4 seed" in lower or "ttt-enhanced" in lower:
        seed_mode = "Multi-run metric."
    else:
        seed_mode = "Single-run metric."
    if "ttt" in lower:
        eval_mode = "Custom evaluation with test-time adaptation; do not compare directly against plain roundtrip metrics."
    elif "sliding" in lower:
        eval_mode = "Sliding-window evaluation is authoritative for this record."
    elif "ternary" in lower:
        eval_mode = "Separate ternary branch metric with sliding evaluation and temperature scaling."
    else:
        eval_mode = "Standard post-quant roundtrip evaluation is authoritative."
    if "post" in lower or "roundtrip" in lower or "quant" in lower:
        quant_mode = "Authoritative score is post-quant."
    else:
        quant_mode = "Quantization semantics must be checked from the record-local source."
    notes.extend([seed_mode, eval_mode, quant_mode])
    return "\n".join(f"- {note}" for note in notes)


def render_observed_results(data: dict) -> str:
    lines = [
        f"- Reproduction status: `{data.get('reproduction_kind') or data.get('status') or 'unknown'}`",
        f"- Observed `val_bpb`: {scalar_text(data.get('reproduced_val_bpb'))}",
        f"- Observed `val_loss`: {scalar_text(data.get('reproduced_val_loss'))}",
        f"- Observed artifact bytes: {scalar_text(data.get('reproduced_artifact_bytes'))}",
        f"- Observed completed steps: {scalar_text(data.get('reproduced_steps'))}",
        f"- Observed `step_avg_ms`: {scalar_text(data.get('reproduced_step_avg_ms'))}",
        f"- W&B run name/path: {scalar_text(data.get('wandb_run_name'))}",
        f"- Local run log: {scalar_text(data.get('local_log_path'))}",
    ]
    return "\n".join(lines)


def render_notes(data: dict) -> str:
    notes = data.get("notes") or []
    if not notes:
        return "- none"
    return "\n".join(f"- {note}" for note in notes)


def main() -> None:
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
        source_readme = ROOT / data["source_readme"] if data.get("source_readme") else None
        command = data.get("exact_command") or (extract_command(source_readme) if source_readme else "")
        source_logs = data.get("source_logs") or []
        if isinstance(source_logs, str):
            source_logs = [source_logs]
        source_logs = [str(Path(p)) for p in source_logs]
        markdown = f"""# {slug}

## Record identity
- Record folder: `{data.get("record_dir", source_dir)}`
- Claimed run name: {scalar_text(data.get("claimed_run_name") or data.get("name"))}
- Author: {scalar_text(data.get("author"))}
- Family: {scalar_text(data.get("family"))}
- Current review status: `{data.get("status", "unknown")}`

## Source files used
- README: `{data.get("source_readme", "")}`
- Submission metadata: `{data.get("source_submission", "")}`
- Script snapshot: `{data.get("source_script", "")}`
{bullets(source_logs)}

## Claimed method summary
{data.get("claimed_method_summary") or data.get("submission_blurb") or "No additional summary extracted yet."}

## Claimed metrics
- Claimed metric name: `{data.get("claimed_metric_name") or "val_bpb"}`
- Claimed `val_bpb`: {scalar_text(data.get("claimed_val_bpb"))}
- Claimed `val_loss`: {scalar_text(data.get("claimed_val_loss"))}
- Claimed artifact bytes: {scalar_text(data.get("claimed_artifact_bytes"))}
- Metric mode: {scalar_text(data.get("metric_mode"))}

## Metric semantics / evaluation mode
{render_metric_semantics(data)}

## Reproduction prerequisites
- Required dataset: `{scalar_text(data.get("required_dataset"))}`
- Required tokenizer: `{scalar_text(data.get("required_tokenizer"))}`
- Extra packages: {", ".join(data.get("required_packages") or ["none beyond the root uv environment"])}
- Hardware notes: {scalar_text(data.get("hardware_notes"))}

## Exact reproduction command
```bash
{command or "# command not extracted yet"}
```

## Observed reproduction results
{render_observed_results(data)}

## Delta vs claimed result
- `Δ val_bpb`: {scalar_text(data.get("delta_val_bpb"))}
- `Δ val_loss`: {scalar_text(data.get("delta_val_loss"))}

## Notes / discrepancies / legality caveats
{render_notes(data)}
"""
        (record_dir / "README.md").write_text(markdown)


if __name__ == "__main__":
    main()
