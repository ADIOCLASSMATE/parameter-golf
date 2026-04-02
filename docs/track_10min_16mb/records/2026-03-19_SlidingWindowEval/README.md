# 2026-03-19_SlidingWindowEval

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_SlidingWindowEval`
- Claimed run name: Sliding Window Eval (stride=64)
- Author: Matthew Li
- Family: context length and evaluation changes
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_SlidingWindowEval/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_SlidingWindowEval/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_SlidingWindowEval/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_SlidingWindowEval/train.log`

## Claimed method summary
Baseline 9x512 SP-1024 architecture with sliding window evaluation at stride=64. Each token is scored with 960+ tokens of context instead of the baseline's 0-1023. Training is identical to the naive baseline; the improvement comes entirely from the evaluation strategy. Post-quant int8+zlib roundtrip under the 16,000,000-byte cap.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.19250007
- Claimed `val_loss`: 2.01348383
- Claimed artifact bytes: 15874829
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
RUN_ID=executor_2026-03-19_SlidingWindowEval_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
NUM_LOOPS=1 \
LORA_RANK=0 \
QAT=0 \
EVAL_STRIDE=64 \
EVAL_BATCH_SEQS=1024 \
MAX_WALLCLOCK_SECONDS=600 \
TRAIN_LOG_EVERY=200 \
VAL_LOSS_EVERY=1000 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_SlidingWindowEval/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.19342201
- Observed `val_loss`: 2.0150405
- Observed artifact bytes: 15876349
- Observed completed steps: 13313
- Observed `step_avg_ms`: 45.07
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_SlidingWindowEval/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00092194
- `Δ val_loss`: 0.00155667

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot with the source sliding-eval flags on 8xH100.
- Observed training throughput was slightly slower than the source README run (45.07 ms/step vs 44.61 ms/step), which reduced completed steps from 13450 to 13313 before the 600 s cap.
- The authoritative sliding-window post-quant val_bpb was therefore slightly worse than claimed by +0.00092194, while preserving the same metric semantics.
