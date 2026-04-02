# 2026-03-19_TrainingOptSeq4096

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096`
- Claimed run name: Training Opt Seq4096 v1
- Author: Spokane Way
- Family: context length and evaluation changes
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train.log`
- `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train_seed1338.log`
- `records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train_seed1339.log`

## Claimed method summary
SP-1024 9x512 KV4 run at TRAIN_SEQ_LEN=4096 with aggressively tuned Muon optimizer: momentum 0.99, lower LR (0.020/0.020/0.030), 3/4 batch (393K tokens), warmdown 3000 steps, and extended momentum warmup (1500 steps from 0.92). Combines long-context training with training optimization to beat the naive baseline by 0.023 BPB.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.20143417
- Claimed `val_loss`: 2.02857127
- Claimed artifact bytes: 15868326
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
RUN_ID=executor_2026-03-19_TrainingOptSeq4096_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.19224339
- Observed `val_loss`: 2.01305303
- Observed artifact bytes: 15871395
- Observed completed steps: 11397
- Observed `step_avg_ms`: 52.65
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_TrainingOptSeq4096/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.00919078
- `Δ val_loss`: -0.01551824

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the standalone record-local script on 8xH100 in the uv-managed baseline environment.
- This host reproduced the script far faster than the source README run (52.65 ms/step vs 71.47 ms/step), increasing completed steps from 8394 to 11397 before the same 600 s cap.
- The faster execution produced a much better post-quant val_bpb than claimed, improving by -0.00919078. This is a major discrepancy and should be treated as a host/runtime difference rather than compared naively against the historical claim.
