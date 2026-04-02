# 2026-03-18_LowerLR

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-18_LowerLR`
- Claimed run name: Lower LR
- Author: Nan Liu
- Family: baseline / simple schedule tuning
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-18_LowerLR/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-18_LowerLR/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-18_LowerLR/train_gpt.py`
- `records/track_10min_16mb/2026-03-18_LowerLR/train.log`

## Claimed method summary
Same 9x512 SP-1024 KV4 tied-embedding baseline architecture with lower Muon/Adam learning rates (MATRIX_LR=0.02, SCALAR_LR=0.02, TIED_EMBED_LR=0.03). Systematic LR sweep showed default 0.04 was too high; optimal is ~0.02.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.22296644
- Claimed `val_loss`: 2.0649276
- Claimed artifact bytes: 15854246
- Metric mode: final_int8_zlib_roundtrip_exact

## Metric semantics / evaluation mode
- Single-run metric.
- Standard post-quant roundtrip evaluation is authoritative.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: README notes provenance on H200; compare carefully against H100-target expectations

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-18_LowerLR_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
VAL_LOSS_EVERY=200 \
TRAIN_LOG_EVERY=50 \
MATRIX_LR=0.02 \
SCALAR_LR=0.02 \
TIED_EMBED_LR=0.03 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-18_LowerLR/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.22145208
- Observed `val_loss`: 2.06237068
- Observed artifact bytes: 15872659
- Observed completed steps: 13261
- Observed `step_avg_ms`: 45.25
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-18_LowerLR/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.00151436
- `Δ val_loss`: -0.00255692

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot in the uv-managed baseline environment on 8xH100.
- The source README notes the historical run was on 8xH200. This rerun was on 8xH100 and still slightly outperformed the claimed post-quant val_bpb.
- Observed step time was slower than the H200 source log (45.25 ms/step vs 41.60 ms/step), but the final val_bpb still came in better by -0.00151436.
