from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


FINAL_PATTERNS = [
    re.compile(r"^(?P<name>final_[A-Za-z0-9_]+_exact) val_loss:(?P<val_loss>[0-9.]+) val_bpb:(?P<val_bpb>[0-9.]+)"),
    re.compile(r"^(?P<name>legal_ttt_exact) val_loss:(?P<val_loss>[0-9.]+) val_bpb:(?P<val_bpb>[0-9.]+)"),
    re.compile(r"^(?P<name>final_ttt_lora) val_loss:(?P<val_loss>[0-9.]+) val_bpb:(?P<val_bpb>[0-9.]+)"),
    re.compile(r"^(?P<name>final_int8_ttt_lora) val_loss:(?P<val_loss>[0-9.]+) val_bpb:(?P<val_bpb>[0-9.]+)"),
    re.compile(r"^(?P<name>final_sliding) val_loss:(?P<val_loss>[0-9.]+) val_bpb:(?P<val_bpb>[0-9.]+)"),
]


def pick_metric(metric_mode: str, finals: dict[str, dict[str, float]]) -> tuple[str, dict[str, float]] | tuple[None, None]:
    lower = (metric_mode or "").lower()
    preferences: list[str]
    if "legal ttt" in lower:
        preferences = ["legal_ttt_exact"]
    elif "ttt" in lower:
        preferences = ["final_int8_ttt_lora", "final_ttt_lora", "legal_ttt_exact"]
    elif "ternary" in lower:
        preferences = ["final_sliding"]
    elif "sliding" in lower:
        preferences = [
            "final_sliding_window_eval_exact",
            "final_sliding_window_exact",
            "final_int6_sliding_window_exact",
            "final_int8_zlib_roundtrip_exact",
            "final_int6_roundtrip_exact",
        ]
    else:
        preferences = [
            "final_int8_zlib_roundtrip_exact",
            "final_int6_roundtrip_exact",
            "final_ternary_roundtrip_exact",
        ]
    for key in preferences:
        if key in finals:
            return key, finals[key]
    if finals:
        key = next(iter(finals))
        return key, finals[key]
    return None, None


def parse_log(log_path: Path) -> dict[str, object]:
    text = log_path.read_text(errors="replace")
    finals: dict[str, dict[str, float]] = {}
    for line in text.splitlines():
        for pattern in FINAL_PATTERNS:
            match = pattern.search(line.strip())
            if match:
                finals[match.group("name")] = {
                    "val_loss": float(match.group("val_loss")),
                    "val_bpb": float(match.group("val_bpb")),
                }
                break
    stop_match = None
    for match in re.finditer(r"stopping_early: wallclock_cap train_time:(?P<train_ms>\d+)ms step:(?P<step>\d+)/", text):
        stop_match = match
    step_avg_match = None
    for match in re.finditer(r"step_avg:(?P<step_avg>[0-9.]+)ms", text):
        step_avg_match = match
    artifact_bytes = None
    bytes_patterns = [
        r"bytes_total[:=](?P<bytes>\d+)",
        r"Total submission size int8\+zlib: (?P<bytes>\d+) bytes",
        r"total_submission_size[^0-9]*(?P<bytes>\d+)",
        r"artifact:[^|]*\|?[^0-9]*(?P<bytes>\d{7,})",
    ]
    for pattern in bytes_patterns:
        matches = list(re.finditer(pattern, text))
        if matches:
            artifact_bytes = int(matches[-1].group("bytes"))
    budget_total_match = None
    for match in re.finditer(r"budget:(?P<total>\d+)/(?:\d+)", text):
        budget_total_match = match
    code_bytes_match = None
    for match in re.finditer(r"code:(?P<code>\d+)", text):
        code_bytes_match = match
    if budget_total_match and code_bytes_match:
        artifact_bytes = int(budget_total_match.group("total")) - int(code_bytes_match.group("code"))
    return {
        "finals": finals,
        "steps": int(stop_match.group("step")) if stop_match else None,
        "step_avg_ms": float(step_avg_match.group("step_avg")) if step_avg_match else None,
        "artifact_bytes": artifact_bytes,
    }


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: update_reproduction_from_log.py <record-slug> <run-log> [reproduction-kind]")
    slug = sys.argv[1]
    run_log = Path(sys.argv[2]).resolve()
    reproduction_kind = sys.argv[3] if len(sys.argv) > 3 else "exact"
    repro_path = ROOT / "docs" / "track_10min_16mb" / "records" / slug / "reproduction.json"
    data = json.loads(repro_path.read_text())
    parsed = parse_log(run_log)
    metric_name, metric = pick_metric(data.get("metric_mode", ""), parsed["finals"])
    if not metric:
        raise SystemExit(f"no final metric line parsed from {run_log}")
    data["reproduction_kind"] = reproduction_kind
    data["status"] = reproduction_kind
    data["local_log_path"] = str(run_log.relative_to(ROOT))
    data["authoritative_observed_metric"] = metric_name
    data["reproduced_val_bpb"] = metric["val_bpb"]
    data["reproduced_val_loss"] = metric["val_loss"]
    data["reproduced_artifact_bytes"] = parsed["artifact_bytes"]
    data["reproduced_steps"] = parsed["steps"]
    data["reproduced_step_avg_ms"] = parsed["step_avg_ms"]
    claimed_bpb = data.get("claimed_val_bpb")
    claimed_loss = data.get("claimed_val_loss")
    data["delta_val_bpb"] = round(data["reproduced_val_bpb"] - claimed_bpb, 8) if claimed_bpb is not None else None
    data["delta_val_loss"] = round(data["reproduced_val_loss"] - claimed_loss, 8) if claimed_loss is not None else None
    repro_path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n")


if __name__ == "__main__":
    main()
