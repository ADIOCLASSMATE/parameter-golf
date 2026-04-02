# 2026-03-19_smeargate_orthoinit_muonwd

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd`
- Claimed run name: not yet recorded
- Author: not yet recorded
- Family: architecture additions
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/train_gpt_v5.py`
- `records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/train.log`

## Claimed method summary
No additional summary extracted yet.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.1556
- Claimed `val_loss`: 1.9511
- Claimed artifact bytes: not yet recorded
- Metric mode: single-run post-quant eval

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
RUN_ID=executor_2026-03-19_smeargate_orthoinit_muonwd_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_smeargate_orthoinit_muonwd/train_gpt_v5.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.18909477
- Observed `val_loss`: 2.00773671
- Observed artifact bytes: not yet recorded
- Observed completed steps: 11909
- Observed `step_avg_ms`: 50.38
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_smeargate_orthoinit_muonwd/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.03349477
- `Δ val_loss`: 0.05663671

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
