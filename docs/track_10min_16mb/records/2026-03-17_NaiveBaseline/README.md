# 2026-03-17_NaiveBaseline

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-17_NaiveBaseline`
- Claimed run name: Naive Baseline
- Author: Baseline
- Family: baseline / simple schedule tuning
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-17_NaiveBaseline/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-17_NaiveBaseline/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-17_NaiveBaseline/train_gpt.py`
- `records/track_10min_16mb/2026-03-17_NaiveBaseline/train.log`

## Claimed method summary
SP-1024 9x512 KV4 run on pgut1 using the published Hugging Face fineweb10B_sp1024 export and the current train_gpt.py; score is the default final int8+zlib roundtrip metric under the 16,000,000-byte cap.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.2243657
- Claimed `val_loss`: 2.07269931
- Claimed artifact bytes: 15863489
- Metric mode: final_int8_zlib_roundtrip_exact

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
RUN_ID=executor_2026-03-17_NaiveBaseline_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
TRAIN_LOG_EVERY=50 \
VAL_LOSS_EVERY=200 \
NCCL_IB_DISABLE=1 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-17_NaiveBaseline/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.22704765
- Observed `val_loss`: 2.07181856
- Observed artifact bytes: 15858571
- Observed completed steps: 13282
- Observed `step_avg_ms`: 45.18
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-17_NaiveBaseline/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00268195
- `Δ val_loss`: -0.00088075

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local SP-1024 dataset/tokenizer paths.
- Observed throughput was slower than the historical source log (45.18 ms/step vs 43.54 ms/step), which reduced completed steps from 13780 to 13282 before the same 600 s cap.
- The reproduced post-quant val_bpb was therefore worse than claimed by +0.00268195.
