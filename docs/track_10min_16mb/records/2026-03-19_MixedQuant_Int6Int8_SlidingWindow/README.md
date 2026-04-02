# 2026-03-19_MixedQuant_Int6Int8_SlidingWindow

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow`
- Claimed run name: Mixed Quant (int6 blocks + int8 embeddings) + Sliding Window Eval, val_bpb=1.1630
- Author: aquariouseworkman
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/train.log`

## Claimed method summary
3x MLP expansion with mixed-precision quantization: int6 per-row (31 levels) on STE-protected block weights, int8 per-row (127 levels) on embedding, zlib-9 compression, sliding window evaluation at stride=64.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.16301431
- Claimed `val_loss`: 1.96369923
- Claimed artifact bytes: 15353490
- Metric mode: sliding-window post-quant eval

## Metric semantics / evaluation mode
- Single-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-19_MixedQuant_Int6Int8_SlidingWindow_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
VAL_LOSS_EVERY=2000 \
TRAIN_LOG_EVERY=200 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.19701546
- Observed `val_loss`: 2.02111046
- Observed artifact bytes: not yet recorded
- Observed completed steps: 12105
- Observed `step_avg_ms`: 49.57
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.03400115
- `Δ val_loss`: 0.05741123

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
