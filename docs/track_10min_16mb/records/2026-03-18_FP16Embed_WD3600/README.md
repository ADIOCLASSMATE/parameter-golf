# 2026-03-18_FP16Embed_WD3600

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600`
- Claimed run name: FP16 Tied Embedding + LR/Warmdown Tuning
- Author: Renier Velazco
- Family: baseline / simple schedule tuning
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/train_gpt.py`
- `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/train.log`
- `records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/train_seed42.log`

## Claimed method summary
Keep tok_emb.weight in fp16 during int8 quantization to eliminate the output-head quantization gap (0.007 -> 0.0005 BPB). Slightly reduce MLP hidden (992 vs 1024) to fit within 16MB. Tune warmdown (3600 vs 1200) and matrix LR (0.06 vs 0.04) for better convergence under the 10-min wallclock cap.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.21972502
- Claimed `val_loss`: 2.0594546
- Claimed artifact bytes: 15896222
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
RUN_ID=executor_2026-03-18_FP16Embed_WD3600_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
MLP_HIDDEN=992 \
WARMDOWN_ITERS=3600 \
MATRIX_LR=0.06 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.21952327
- Observed `val_loss`: 2.05911395
- Observed artifact bytes: 15898280
- Observed completed steps: 13521
- Observed `step_avg_ms`: 44.38
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-18_FP16Embed_WD3600/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.00020175
- `Δ val_loss`: -0.00034065

## Notes / discrepancies / legality caveats
- Fill after reproduction.
- State clearly whether the reproduction used the exact record-local script or an approximation.
