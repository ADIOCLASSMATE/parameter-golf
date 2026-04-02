# 2026-03-20_11L_EfficientPartialXSA_FA3_SWA120

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120`
- Claimed run name: 11L + Efficient Partial XSA + FA3 + SWA/120 (val_bpb: 1.1307)
- Author: vadim borisov (tabularis.ai)
- Family: architecture additions
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/train_gpt.py`
- `records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/train.log`

## Claimed method summary
11 layers, int6 quant, zstd-22. Novel contribution: Efficient Partial Exclusive Self Attention (XSA, arXiv:2603.09078) applied to deepest 3 layers only. GQA-aware reshape avoids tensor duplication, adding <2ms/step overhead. XSA subtracts self-value projection from attention output, forcing deeper layers to learn from context rather than self-reference. SWA every 120 steps (13 checkpoint avg). OrthoInit + muP scaling. SmearGate + BigramHash(2048x128). FlashAttention 3 + NTK RoPE. Weight decay 0.04 (Muon+AdamW).

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.13071416
- Claimed `val_loss`: 1.90915845
- Claimed artifact bytes: 15892986
- Metric mode: single-run post-quant eval

## Metric semantics / evaluation mode
- Single-run metric.
- Standard post-quant roundtrip evaluation is authoritative.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: flash-attn-3, zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-20_11L_EfficientPartialXSA_FA3_SWA120_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
NUM_LAYERS=11 \
BIGRAM_VOCAB_SIZE=2048 \
MUON_WD=0.04 \
ADAM_WD=0.04 \
MATRIX_LR=0.025 \
SCALAR_LR=0.025 \
TIED_EMBED_LR=0.035 \
MUON_MOMENTUM=0.99 \
MUON_MOMENTUM_WARMUP_START=0.92 \
MUON_MOMENTUM_WARMUP_STEPS=1500 \
WARMDOWN_ITERS=3000 \
ITERATIONS=9000 \
MAX_WALLCLOCK_SECONDS=600 \
EVAL_STRIDE=64 \
SWA_EVERY=120 \
SWA_ENABLED=1 \
MTP_NUM_HEADS=0 \
SEED=1337 \
WARMUP_STEPS=30 \
VAL_LOSS_EVERY=2000 \
XSA_LAST_N=3 \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.15342668
- Observed `val_loss`: 1.94751263
- Observed artifact bytes: not yet recorded
- Observed completed steps: 7132
- Observed `step_avg_ms`: 84.14
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.02271252
- `Δ val_loss`: 0.03835418

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
