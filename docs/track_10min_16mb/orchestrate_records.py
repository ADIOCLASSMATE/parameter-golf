from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "docs" / "track_10min_16mb"
RECORDS_DOC_ROOT = DOCS_ROOT / "records"

SP1024_DATA = str(ROOT / "data" / "datasets" / "fineweb10B_sp1024")
SP1024_TOKENIZER = str(ROOT / "data" / "tokenizers" / "fineweb_1024_bpe.model")
SP8192_DATA = str(ROOT / "data" / "datasets" / "fineweb10B_sp8192")
TERNARY_TOKENIZER = str(
    ROOT
    / "records"
    / "track_10min_16mb"
    / "2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon"
    / "fineweb_8192_bpe.model"
)


CONFIGS = {
    "2026-03-17_LoRA_TTT": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-17_LoRA_TTT/train_gpt.py",
        "env": {
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "MAX_WALLCLOCK_SECONDS": "600",
        },
    },
    "2026-03-19_10L_MixedPrecision": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_10L_MixedPrecision/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_10L_MixedPrecision_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "MAX_WALLCLOCK_SECONDS": "600",
            "VAL_LOSS_EVERY": "200",
            "TRAIN_LOG_EVERY": "50",
            "NUM_LAYERS": "10",
            "MATRIX_LR": "0.02",
            "SCALAR_LR": "0.02",
            "TIED_EMBED_LR": "0.03",
            "INT4_LAYERS": "3,4,5,6",
            "INT4_STEP": "4",
        },
    },
    "2026-03-19_MixedQuant_Int6Int8_SlidingWindow": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_MixedQuant_Int6Int8_SlidingWindow_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "MAX_WALLCLOCK_SECONDS": "600",
            "VAL_LOSS_EVERY": "2000",
            "TRAIN_LOG_EVERY": "200",
        },
    },
    "2026-03-19_WarmdownQuantization": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_WarmdownQuantization/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_WarmdownQuantization_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "WARMDOWN_ITERS": "20000",
            "MATRIX_LR": "0.06",
            "TIED_EMBED_LR": "0.07",
            "SCALAR_LR": "0.06",
            "GRAD_CLIP_NORM": "1.0",
            "MUON_BACKEND_STEPS": "5",
            "EVAL_SEQ_LEN": "1408",
            "MLP_HIDDEN": "992",
            "MAX_WALLCLOCK_SECONDS": "600",
        },
    },
    "2026-03-19_Seq2048_FP16Emb_TunedLR": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_Seq2048_FP16Emb_TunedLR_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "MLP_HIDDEN": "1344",
            "MAX_WALLCLOCK_SECONDS": "600",
            "EVAL_STRIDE": "64",
        },
    },
    "2026-03-19_MLP3x_QAT_Int6_SlidingWindow": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_MLP3x_QAT_Int6_SlidingWindow_exact",
            "SEED": "1337",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
            "NUM_LAYERS": "11",
            "MLP_MULT": "3",
            "MATRIX_LR": "0.025",
            "SCALAR_LR": "0.025",
            "TIED_EMBED_LR": "0.035",
            "FP16_EMBED_EXPORT": "1",
            "INT6_LAYER_START": "0",
            "INT6_LAYER_END": "10",
            "QAT_ENABLED": "1",
            "QAT_INT6": "1",
            "MUON_WEIGHT_DECAY": "0.04",
            "ADAM_WEIGHT_DECAY": "0.04",
            "MUON_MOMENTUM": "0.99",
            "MUON_MOMENTUM_WARMUP_START": "0.92",
            "MUON_MOMENTUM_WARMUP_STEPS": "1500",
            "WARMDOWN_ITERS": "3000",
            "USE_ZSTD": "1",
            "EVAL_STRIDE": "64",
            "MAX_WALLCLOCK_SECONDS": "600",
        },
    },
    "2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "VOCAB_SIZE": "1024",
        },
    },
    "2026-03-19_smeargate_orthoinit_muonwd": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/train_gpt_v5.py",
        "env": {
            "RUN_ID": "executor_2026-03-19_smeargate_orthoinit_muonwd_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
        },
    },
    "2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
        },
    },
    "2026-03-20_10L_Int5MLP_MuonWD04_SWA50": {
        "venv": ".venv",
        "script": "records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-20_10L_Int5MLP_MuonWD04_SWA50_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
        },
    },
    "2026-03-20_11L_EfficientPartialXSA_FA3_SWA120": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-20_11L_EfficientPartialXSA_FA3_SWA120_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "NUM_LAYERS": "11",
            "BIGRAM_VOCAB_SIZE": "2048",
            "MUON_WD": "0.04",
            "ADAM_WD": "0.04",
            "MATRIX_LR": "0.025",
            "SCALAR_LR": "0.025",
            "TIED_EMBED_LR": "0.035",
            "MUON_MOMENTUM": "0.99",
            "MUON_MOMENTUM_WARMUP_START": "0.92",
            "MUON_MOMENTUM_WARMUP_STEPS": "1500",
            "WARMDOWN_ITERS": "3000",
            "ITERATIONS": "9000",
            "MAX_WALLCLOCK_SECONDS": "600",
            "EVAL_STRIDE": "64",
            "SWA_EVERY": "120",
            "SWA_ENABLED": "1",
            "MTP_NUM_HEADS": "0",
            "SEED": "1337",
            "WARMUP_STEPS": "30",
            "VAL_LOSS_EVERY": "2000",
            "XSA_LAST_N": "3",
        },
    },
    "2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "NUM_LAYERS": "11",
            "BIGRAM_VOCAB_SIZE": "2048",
            "XSA_LAST_N": "4",
            "EMA_ENABLED": "1",
            "EMA_DECAY": "0.997",
            "SWA_ENABLED": "0",
            "MUON_WD": "0.04",
            "ADAM_WD": "0.04",
            "MATRIX_LR": "0.025",
            "SCALAR_LR": "0.025",
            "TIED_EMBED_LR": "0.035",
            "MUON_MOMENTUM": "0.99",
            "MUON_MOMENTUM_WARMUP_START": "0.92",
            "MUON_MOMENTUM_WARMUP_STEPS": "1500",
            "WARMDOWN_ITERS": "3000",
            "ITERATIONS": "9000",
            "MAX_WALLCLOCK_SECONDS": "600",
            "EVAL_STRIDE": "64",
            "SEED": "1337",
        },
    },
    "2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "NUM_LAYERS": "11",
            "BIGRAM_VOCAB_SIZE": "2048",
            "XSA_LAST_N": "4",
            "EMA_ENABLED": "1",
            "EMA_DECAY": "0.997",
            "SWA_ENABLED": "0",
            "ROPE_DIMS": "16",
            "LN_SCALE": "1",
            "LATE_QAT": "1",
            "QAT_THRESHOLD": "0.1",
            "MUON_WD": "0.04",
            "ADAM_WD": "0.04",
            "MATRIX_LR": "0.025",
            "SCALAR_LR": "0.025",
            "TIED_EMBED_LR": "0.035",
            "MUON_MOMENTUM": "0.99",
            "MUON_MOMENTUM_WARMUP_START": "0.92",
            "MUON_MOMENTUM_WARMUP_STEPS": "1500",
            "WARMDOWN_ITERS": "3000",
            "ITERATIONS": "9000",
            "MAX_WALLCLOCK_SECONDS": "600",
            "EVAL_STRIDE": "64",
            "SEED": "2025",
        },
    },
    "2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233_exact",
            "SEED": "1337",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
        },
    },
    "2026-03-23_LeakyReLU_LegalTTT_ParallelMuon": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-23_LeakyReLU_LegalTTT_ParallelMuon_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "NUM_LAYERS": "11",
            "BIGRAM_VOCAB_SIZE": "1536",
            "XSA_LAST_N": "4",
            "EMA_ENABLED": "1",
            "EMA_DECAY": "0.997",
            "SWA_ENABLED": "1",
            "SWA_EVERY": "50",
            "ROPE_DIMS": "16",
            "LN_SCALE": "1",
            "LATE_QAT": "1",
            "LATE_QAT_THRESHOLD": "0.15",
            "VE_ENABLED": "1",
            "VE_DIM": "128",
            "VE_LAYERS": "9,10",
            "TTT_ENABLED": "1",
            "TTT_LR": "0.002",
            "TTT_EPOCHS": "3",
            "TTT_CHUNK_TOKENS": "32768",
            "TTT_FREEZE_BLOCKS": "0",
            "TTT_MOMENTUM": "0.9",
            "TTT_BATCH_SEQS": "32",
            "TTT_GRAD_CLIP": "1.0",
            "MUON_WD": "0.04",
            "ADAM_WD": "0.04",
            "MATRIX_LR": "0.025",
            "SCALAR_LR": "0.025",
            "TIED_EMBED_LR": "0.035",
            "MUON_MOMENTUM": "0.99",
            "MUON_MOMENTUM_WARMUP_START": "0.92",
            "MUON_MOMENTUM_WARMUP_STEPS": "1500",
            "WARMDOWN_ITERS": "3500",
            "ITERATIONS": "9000",
            "MAX_WALLCLOCK_SECONDS": "600",
            "EVAL_STRIDE": "64",
            "SEED": "1337",
        },
    },
    "2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/train_gpt_cuda_ternary.py",
        "env": {
            "RUN_ID": "executor_2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon_exact",
            "DATA_PATH": SP8192_DATA,
            "TOKENIZER_PATH": TERNARY_TOKENIZER,
            "ATTN_PROJ_TYPE": "standard",
            "LOGIT_HEAD_TYPE": "standard",
            "TVERSKY_MEMBERSHIP": "sigmoid",
            "TVERSKY_NUM_FEATURES": "0",
            "TVERSKY_FEATURE_POOLS": "0",
            "VOCAB_SIZE": "8192",
            "BITNET_GROUP_SIZE": "128",
            "BIGRAM_HASH": "0",
            "EMBED_DIM": "254",
            "TRAINING_DEPTH_RECURRENCE": "0",
            "EVAL_DEPTH_RECURRENCE": "0",
            "NUM_LAYERS": "10",
            "MODEL_DIM": "768",
            "NUM_KV_HEADS": "4",
            "NUM_HEADS": "8",
            "DIFF_ATTN": "0",
            "MLP_MULT": "4",
            "MLP_GROUPS": "0",
            "MATRIX_OPTIMIZER": "muon",
            "ADAM_LR": "0.05",
            "ADAM_WD": "0.05",
            "MUON_BACKEND_STEPS": "3",
            "MUON_MOMENTUM": "0.95",
            "MUON_MOMENTUM_WARMUP_START": "0.85",
            "MUON_MOMENTUM_WARMUP_STEPS": "500",
            "MUON_WD": "0.0",
            "MATRIX_LR": "0.04",
            "SCALAR_LR": "0.02",
            "TIED_EMBED_LR": "0.02",
            "WARMDOWN_FRACTION": "0.2",
            "LOGIT_SOFTCAP": "10",
            "QK_GAIN_INIT": "2.25",
            "ROPE_TYPE": "yarn",
            "YARN_MAX_LEN": "2048",
            "ROPE_BASE": "5000",
            "BATCH_TOKENS_START": "0",
            "BATCH_SCHEDULE_FRACTION": "0.33",
            "TRAIN_BATCH_TOKENS": "524288",
            "SEQ_LEN_START": "0",
            "SEQ_SCHEDULE_FRACTION": "0.0",
            "TRAIN_SEQ_LEN": "1024",
            "SMEAR": "0",
            "ITERATIONS": "10000",
            "WARMUP_STEPS": "5",
            "MAX_WALLCLOCK_SECONDS": "599",
            "VAL_LOSS_EVERY": "0",
            "TRAIN_LOG_EVERY": "1000",
            "CHURN_LOG_EVERY": "0",
            "VAL_MAX_TOKENS": "0",
            "TIE_EMBEDDINGS": "1",
            "UNTIE_AT_FRACTION": "0.00",
            "HEAD_LR": "0.02",
            "CORR_WEIGHT_LR": "0.02",
            "ACTIVATION": "relu2",
            "SOFTCAP_TYPE": "poly",
            "MTP_HEADS": "0",
            "REFINER": "0",
            "REFINER_KERNEL": "3",
            "SLIDING_EVAL": "1",
            "SLIDING_EVAL_STRIDE": "16",
            "SLIDING_BATCH_SIZE": "256",
            "TEMP_SCALING": "1",
            "FP_STORAGE": "FP8",
            "SEED": "42",
            "COMPILE_MODE": "default",
            "OMP_NUM_THREADS": "1",
        },
    },
    "2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072": {
        "venv": ".venv-fa3",
        "script": "records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_gpt.py",
        "env": {
            "RUN_ID": "executor_2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072_exact",
            "DATA_PATH": SP1024_DATA,
            "TOKENIZER_PATH": SP1024_TOKENIZER,
            "BIGRAM_VOCAB_SIZE": "3072",
            "BIGRAM_DIM": "112",
            "WARMDOWN_ITERS": "4000",
            "TARGET_MB": "15.9",
            "SEED": "314",
        },
    },
}


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")


def run_shell(cmd: str, extra_env: dict[str, str] | None = None) -> None:
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    subprocess.run(cmd, shell=True, cwd=ROOT, check=True, env=env)


def append_logs(slug: str, message: str, next_step: str) -> None:
    ts = timestamp()
    per_record = RECORDS_DOC_ROOT / slug / "process.md"
    per_record.write_text(
        per_record.read_text()
        + "\n"
        + f"- Timestamp: {ts}\n- Action: {message}\n- Command / script: {CONFIGS[slug]['script']}\n"
        + f"- Environment notes: executed via {CONFIGS[slug]['venv']}.\n- Outcome: see reproduction.json and run log.\n"
        + f"- Next step: {next_step}\n\n"
    )
    shared = DOCS_ROOT / "process_log.md"
    shared.write_text(
        shared.read_text()
        + "\n"
        + f"- Timestamp: {ts}\n- Record slug: {slug}\n- Action: {message}\n- Outcome: see local run log and reproduction.json.\n"
        + f"- Next step: {next_step}\n\n"
    )


def set_command_and_notes(slug: str, command: str, notes: list[str], status: str | None = None) -> None:
    repro_path = RECORDS_DOC_ROOT / slug / "reproduction.json"
    data = json.loads(repro_path.read_text())
    data["exact_command"] = command
    data["notes"] = notes
    if status:
        data["status"] = status
    repro_path.write_text(json.dumps(data, indent=2) + "\n")


def build_command(slug: str) -> str:
    cfg = CONFIGS[slug]
    venv = cfg["venv"]
    env_parts = [f'{key}={value}' for key, value in cfg["env"].items()]
    script = cfg["script"]
    return " \\\n".join(
        env_parts
        + [
            f"uv run --python {venv}/bin/python torchrun --standalone --nproc_per_node=8",
            script,
        ]
    )


def run_record(slug: str) -> None:
    cfg = CONFIGS[slug]
    log_path = RECORDS_DOC_ROOT / slug / "run_exact.log"
    command = build_command(slug)
    append_logs(slug, "Started exact reproduction run.", "Wait for local run completion.")
    shell_cmd = command.replace(" \\\n", " ") + f" > {log_path} 2>&1"
    try:
        run_shell(shell_cmd)
        run_shell(
            f"uv run --python .venv/bin/python python docs/track_10min_16mb/update_reproduction_from_log.py {slug} {log_path} exact"
        )
        notes = [
            "Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.",
            "Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.",
            "See the local run log for the concrete throughput and final metric lines on this host.",
        ]
        set_command_and_notes(slug, command, notes)
        append_logs(slug, "Completed exact reproduction run.", "Refresh rendered README and inventory.")
    except subprocess.CalledProcessError as exc:
        notes = [
            f"Attempted exact current-session rerun failed with exit code {exc.returncode}.",
            "See the local run log for the failure details.",
        ]
        set_command_and_notes(slug, command, notes, status="blocked")
        append_logs(slug, f"Exact reproduction run failed with exit code {exc.returncode}.", "Keep the record documented as blocked.")
    finally:
        run_shell("uv run --python .venv/bin/python python docs/track_10min_16mb/render_record_readmes.py")
        run_shell("uv run --python .venv/bin/python python docs/track_10min_16mb/update_inventory.py")


def main() -> None:
    if len(sys.argv) > 1:
        slugs = sys.argv[1:]
    else:
        slugs = list(CONFIGS)
    for slug in slugs:
        run_record(slug)


if __name__ == "__main__":
    main()
