# 2026-03-18_LongContextSeq2048

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-18_LongContextSeq2048`
- Claimed run name: Long Context Seq2048 v2
- Author: Spokane Way
- Family: context length and evaluation changes
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-18_LongContextSeq2048/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-18_LongContextSeq2048/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-18_LongContextSeq2048/train_gpt.py`
- `records/track_10min_16mb/2026-03-18_LongContextSeq2048/train.log`
- `records/track_10min_16mb/2026-03-18_LongContextSeq2048/train_seed1338.log`
- `records/track_10min_16mb/2026-03-18_LongContextSeq2048/train_seed1339.log`

## Claimed method summary
SP-1024 9x512 KV4 run at TRAIN_SEQ_LEN=2048 with tuned seq2048 learning rates (0.040/0.032/0.032). This standalone record script reproduces the SXM-verified 10-minute artifact under the 16,000,000-byte cap.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.20576485
- Claimed `val_loss`: 2.03588345
- Claimed artifact bytes: 15867270
- Metric mode: final_int8_zlib_roundtrip_exact (3-seed support)

## Metric semantics / evaluation mode
- Multi-run metric.
- Standard post-quant roundtrip evaluation is authoritative.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
NCCL_IB_DISABLE=1 \
RUN_ID=executor_2026-03-18_LongContextSeq2048_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-18_LongContextSeq2048/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.20647429
- Observed `val_loss`: 2.0370813
- Observed artifact bytes: 15861715
- Observed completed steps: 11434
- Observed `step_avg_ms`: 52.48
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-18_LongContextSeq2048/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00070944
- `Δ val_loss`: 0.00119785

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the standalone record-local script with the source NCCL_IB_DISABLE=1 setting on 8xH100.
- Observed throughput was slightly slower than the source README run (52.48 ms/step vs 51.89 ms/step), which reduced completed steps from 11564 to 11434 before the 600 s cap.
- The reproduced post-quant val_bpb was therefore slightly worse than claimed by +0.00070944, but still close to the historical result.
