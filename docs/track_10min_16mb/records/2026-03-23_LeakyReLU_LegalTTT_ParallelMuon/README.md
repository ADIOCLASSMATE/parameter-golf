# 2026-03-23_LeakyReLU_LegalTTT_ParallelMuon

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon`
- Claimed run name: LeakyReLU² + Legal Score-First TTT + Parallel Muon
- Author: abaybektursun
- Family: averaging / optimizer / schedule refinements
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_gpt.py`
- `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_seed1337.log`
- `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_seed2025.log`
- `records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_seed42.log`

## Claimed method summary
LeakyReLU(0.5)² activation (-0.003 BPB vs relu²) + legal score-first TTT (PR #461 recipe, 3ep SGD, all blocks unfrozen) + BigramHash(1536) + Parameter Banking + Parallel Muon (PR #399). Built on PR #414 stack. 3-seed mean: 1.1194 (std 0.0006). All artifacts under 16MB, all eval under 10 min.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.1194
- Claimed `val_loss`: not yet recorded
- Claimed artifact bytes: 15990006
- Metric mode: 3-seed mean with legal TTT

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
RUN_ID=executor_2026-03-23_LeakyReLU_LegalTTT_ParallelMuon_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
NUM_LAYERS=11 \
BIGRAM_VOCAB_SIZE=1536 \
XSA_LAST_N=4 \
EMA_ENABLED=1 \
EMA_DECAY=0.997 \
SWA_ENABLED=1 \
SWA_EVERY=50 \
ROPE_DIMS=16 \
LN_SCALE=1 \
LATE_QAT=1 \
LATE_QAT_THRESHOLD=0.15 \
VE_ENABLED=1 \
VE_DIM=128 \
VE_LAYERS=9,10 \
TTT_ENABLED=1 \
TTT_LR=0.002 \
TTT_EPOCHS=3 \
TTT_CHUNK_TOKENS=32768 \
TTT_FREEZE_BLOCKS=0 \
TTT_MOMENTUM=0.9 \
TTT_BATCH_SEQS=32 \
TTT_GRAD_CLIP=1.0 \
MUON_WD=0.04 \
ADAM_WD=0.04 \
MATRIX_LR=0.025 \
SCALAR_LR=0.025 \
TIED_EMBED_LR=0.035 \
MUON_MOMENTUM=0.99 \
MUON_MOMENTUM_WARMUP_START=0.92 \
MUON_MOMENTUM_WARMUP_STEPS=1500 \
WARMDOWN_ITERS=3500 \
ITERATIONS=9000 \
MAX_WALLCLOCK_SECONDS=600 \
EVAL_STRIDE=64 \
SEED=1337 \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.12040293
- Observed `val_loss`: 1.8917484
- Observed artifact bytes: not yet recorded
- Observed completed steps: 7085
- Observed `step_avg_ms`: 84.7
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00100293
- `Δ val_loss`: not yet recorded

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
