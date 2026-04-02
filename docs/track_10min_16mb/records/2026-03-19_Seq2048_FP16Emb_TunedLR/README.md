# 2026-03-19_Seq2048_FP16Emb_TunedLR

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR`
- Claimed run name: 10L Int6 QAT + Zstd MLP2.6x Muon0.99 Sliding Window
- Author: yahya010
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_seed1337.log`
- `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_seed3.log`
- `records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_seed42.log`

## Claimed method summary
10-layer 512dim SP-1024, STE int6 QAT (zero quant gap), full int6 [-31,31] + zstd-22, MLP hidden=1344, fp16 tied embedding, Muon 0.99, LR 0.02, grad clip 0.3, sliding window stride=64.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.15861696
- Claimed `val_loss`: 1.95627871
- Claimed artifact bytes: 15558319
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
RUN_ID=executor_2026-03-19_Seq2048_FP16Emb_TunedLR_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MLP_HIDDEN=1344 \
MAX_WALLCLOCK_SECONDS=600 \
EVAL_STRIDE=64 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_Seq2048_FP16Emb_TunedLR/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.15827486
- Observed `val_loss`: 1.95570108
- Observed artifact bytes: not yet recorded
- Observed completed steps: 9228
- Observed `step_avg_ms`: 65.02
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_Seq2048_FP16Emb_TunedLR/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.0003421
- `Δ val_loss`: -0.00057763

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
