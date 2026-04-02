# 2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271`
- Claimed run name: Record: 11L XSA + EMA + Int6 MLP3x + WD=0.04
- Author: Jack Princz
- Family: architecture additions
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_gpt.py`
- `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train.log`
- `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_seed1337.log`
- `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_seed2025.log`
- `records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_seed42.log`

## Claimed method summary
11 layers with Exclusive Self Attention (XSA) on last 4 layers, EMA weight averaging (decay=0.997), int6 per-row on all MLP+attention weights, int8 tok_emb, zstd-22. Weight decay 0.04 (Muon+AdamW). OrthoInit + muP scaling. SmearGate + BigramHash(2048x128). FA3. Sliding window eval stride=64, seq=2048.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.12707468
- Claimed `val_loss`: 1.90301335
- Claimed artifact bytes: 15534645
- Metric mode: 3-seed sliding-window post-quant eval

## Metric semantics / evaluation mode
- Multi-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: flash-attn-3, zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
NUM_LAYERS=11 \
BIGRAM_VOCAB_SIZE=2048 \
XSA_LAST_N=4 \
EMA_ENABLED=1 \
EMA_DECAY=0.997 \
SWA_ENABLED=0 \
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
SEED=1337 \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.12845698
- Observed `val_loss`: 1.90534731
- Observed artifact bytes: not yet recorded
- Observed completed steps: 7055
- Observed `step_avg_ms`: 85.06
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.0013823
- `Δ val_loss`: 0.00233396

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
