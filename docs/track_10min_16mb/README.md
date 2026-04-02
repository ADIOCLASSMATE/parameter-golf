# track_10min_16mb reproduction workspace

This directory is the local planning and bookkeeping area for reproducing and summarizing every method under `records/track_10min_16mb`.

## Purpose
- normalize the record inventory before running anything
- document each record’s method and authoritative metric semantics
- record reproduction results in a consistent local format
- keep a durable local process log for the reproducing agent

## Required outputs
- `inventory.md` / `inventory.csv`: normalized index of all record folders
- `taxonomy.md`: method families and lineage notes
- `process_log.md`: shared chronological work log
- `records/<record-slug>/README.md`: per-record human summary and reproduction notes
- `records/<record-slug>/reproduction.json`: per-record structured metadata and results
- `records/<record-slug>/process.md`: per-record work log

## Workflow
1. Start from `inventory.md` and the source record folder.
2. Read the record README, submission metadata, logs, and script snapshot.
3. Fill the exact command and prerequisites in the local per-record README.
4. Reproduce with the exact record-local script when available.
5. Update `reproduction.json`, the per-record README, and `process.md` immediately after the run.
6. Append the high-level outcome to `process_log.md`.

## Comparison rules
- Always state whether the result is single-seed or multi-seed.
- Always state whether the metric is standard roundtrip, sliding-window, TTT, or another custom mode.
- Treat post-quant roundtrip BPB as authoritative unless the source record clearly defines a different official metric.
- Do not compare records directly when their metric semantics differ.
- If a run uses `train_gpt_wandb.py` instead of the exact historical script, mark it as an approximation or controlled reimplementation.

## Special cases
- `2026-03-19_int6_STE QAT_ MLP_bigram _U_Net` is an incomplete/orphaned snapshot and should remain documented as such unless missing files are recovered elsewhere.
- `2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon` is a separate branch with its own tokenizer, setup, and trainer; reproduce it separately from the root baseline flow.
