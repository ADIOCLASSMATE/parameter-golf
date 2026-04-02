# 2026-03-20_10L_Int5MLP_MuonWD04_SWA50

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50`
- Claimed run name: 10L Int5-MLP + BigramHash(10240) + SWA(frac=0.4) + WD=0.04
- Author: thwu1
- Family: averaging / optimizer / schedule refinements
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_gpt.py`
- `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_seed1337.log`
- `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_seed2024.log`
- `records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_seed42.log`

## Claimed method summary
10 layers with mixed int5/int6 quantization. BigramHash 10240 buckets (up from 4096). SWA start_frac=0.4 (24 converged checkpoints). WD=0.04 global, warmdown=3000. Mean of 3 seeds: 1.14276 (std 0.00016). SmearGate + OrthoInit + zstd-22.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: not yet recorded
- Claimed `val_loss`: 1.14276
- Claimed artifact bytes: 15900000
- Metric mode: 3-seed mean post-quant eval

## Metric semantics / evaluation mode
- Multi-run metric.
- Standard post-quant roundtrip evaluation is authoritative.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-20_10L_Int5MLP_MuonWD04_SWA50_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.14312659
- Observed `val_loss`: 1.93011626
- Observed artifact bytes: 15721886
- Observed completed steps: 6543
- Observed `step_avg_ms`: 91.71
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: not yet recorded
- `Δ val_loss`: 0.78735626

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
