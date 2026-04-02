# 2026-03-17_LoRA_TTT

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-17_LoRA_TTT`
- Claimed run name: LoRA TTT
- Author: sam
- Family: context length and evaluation changes
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-17_LoRA_TTT/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-17_LoRA_TTT/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-17_LoRA_TTT/train_gpt.py`
- `records/track_10min_16mb/2026-03-17_LoRA_TTT/train_v0.txt`
- `records/track_10min_16mb/2026-03-17_LoRA_TTT/train_v1.txt`
- `records/track_10min_16mb/2026-03-17_LoRA_TTT/train_v2.txt`
- `records/track_10min_16mb/2026-03-17_LoRA_TTT/train_v3.txt`

## Claimed method summary
Naive baseline + per-document LoRA test-time training at eval. Rank-8 LoRA on lm_head/Q/V with Adam lr=0.01, overlapping 256-token chunks in 1024-token context windows. Same training, smarter eval.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.1929
- Claimed `val_loss`: 2.0142
- Claimed artifact bytes: 15882446
- Metric mode: TTT-enhanced eval metric

## Metric semantics / evaluation mode
- Multi-run metric.
- Custom evaluation with test-time adaptation; do not compare directly against plain roundtrip metrics.
- Quantization semantics must be checked from the record-local source.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MAX_WALLCLOCK_SECONDS=600 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-17_LoRA_TTT/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.1927
- Observed `val_loss`: 2.0138
- Observed artifact bytes: 15871675
- Observed completed steps: 13132
- Observed `step_avg_ms`: 45.69
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-17_LoRA_TTT/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.0002
- `Δ val_loss`: -0.0004

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
