# 2026-03-19_MLP3x_QAT_Int6_SlidingWindow

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow`
- Claimed run name: not yet recorded
- Author: aruniyer
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/train.log`

## Claimed method summary
No additional summary extracted yet.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.15015359
- Claimed `val_loss`: not yet recorded
- Claimed artifact bytes: not yet recorded
- Metric mode: 3-seed sliding-window post-quant eval

## Metric semantics / evaluation mode
- Multi-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-19_MLP3x_QAT_Int6_SlidingWindow_exact \
SEED=1337 \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
NUM_LAYERS=11 \
MLP_MULT=3 \
MATRIX_LR=0.025 \
SCALAR_LR=0.025 \
TIED_EMBED_LR=0.035 \
FP16_EMBED_EXPORT=1 \
INT6_LAYER_START=0 \
INT6_LAYER_END=10 \
QAT_ENABLED=1 \
QAT_INT6=1 \
MUON_WEIGHT_DECAY=0.04 \
ADAM_WEIGHT_DECAY=0.04 \
MUON_MOMENTUM=0.99 \
MUON_MOMENTUM_WARMUP_START=0.92 \
MUON_MOMENTUM_WARMUP_STEPS=1500 \
WARMDOWN_ITERS=3000 \
USE_ZSTD=1 \
EVAL_STRIDE=64 \
MAX_WALLCLOCK_SECONDS=600 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.15077266
- Observed `val_loss`: 1.94302974
- Observed artifact bytes: not yet recorded
- Observed completed steps: 9863
- Observed `step_avg_ms`: 60.84
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00061907
- `Δ val_loss`: not yet recorded

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
