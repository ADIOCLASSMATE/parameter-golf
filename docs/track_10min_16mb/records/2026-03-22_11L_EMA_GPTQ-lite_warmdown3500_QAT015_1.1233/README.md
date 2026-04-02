# 2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233`
- Claimed run name: Record: 11L EMA + GPTQ-lite + warmdown3500 + QAT@0.15
- Author: Tianhao Wu
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_gpt.py`
- `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train.log`
- `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_seed1337.log`
- `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_seed2024.log`
- `records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_seed42.log`

## Claimed method summary
EMA(0.997) weight averaging + GPTQ-lite optimal clip percentile search + warmdown=3500 + Late QAT threshold=0.15, built on PR#374 stack (11L, XSA4, Partial RoPE 16/64, LN Scale, VE128, Tight SWA, SmearGate, BigramHash, int6+zstd-22).

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.12278022
- Claimed `val_loss`: 1.89576235
- Claimed artifact bytes: 15555017
- Metric mode: 3-seed sliding-window post-quant eval

## Metric semantics / evaluation mode
- Multi-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: flash-attn-3, zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233_exact \
SEED=1337 \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.12316266
- Observed `val_loss`: 1.89640809
- Observed artifact bytes: 15657327
- Observed completed steps: 6942
- Observed `step_avg_ms`: 86.44
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00038244
- `Δ val_loss`: 0.00064574

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
