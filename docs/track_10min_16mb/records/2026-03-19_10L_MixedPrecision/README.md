# 2026-03-19_10L_MixedPrecision

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_10L_MixedPrecision`
- Claimed run name: 10L Mixed Precision
- Author: Nan Liu
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_10L_MixedPrecision/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_10L_MixedPrecision/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_10L_MixedPrecision/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_10L_MixedPrecision/train.log`

## Claimed method summary
10-layer 512-dim model with lower LR (MATRIX_LR=0.02) and mixed int8/int6 compression: full int8 for first/last 3 layers, int6 (step=4 rounding) for middle layers 3-6. Fits 16MB via better compression while gaining an extra transformer layer over baseline.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.214745
- Claimed `val_loss`: 2.05104604
- Claimed artifact bytes: 15928974
- Metric mode: final mixed-precision post-quant eval

## Metric semantics / evaluation mode
- Single-run metric.
- Standard post-quant roundtrip evaluation is authoritative.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-19_10L_MixedPrecision_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
VAL_LOSS_EVERY=200 \
TRAIN_LOG_EVERY=50 \
NUM_LAYERS=10 \
MATRIX_LR=0.02 \
SCALAR_LR=0.02 \
TIED_EMBED_LR=0.03 \
INT4_LAYERS=3,4,5,6 \
INT4_STEP=4 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_10L_MixedPrecision/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.21453105
- Observed `val_loss`: 2.05068481
- Observed artifact bytes: 15927713
- Observed completed steps: 12085
- Observed `step_avg_ms`: 49.65
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_10L_MixedPrecision/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.00021395
- `Δ val_loss`: -0.00036123

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
