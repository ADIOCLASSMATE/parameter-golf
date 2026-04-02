# 2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon`
- Claimed run name: 73.7M Ternary U-Net — BitNet b1.58 + NeoMuon + 4x relu² MLP + FP8 QAT + Base-3 LZMA
- Author: Ciprian-Florin Ifrim
- Family: separate ternary / 8192-BPE branch
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/submission_ternary.json`
- Script snapshot: `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/train_gpt_cuda_ternary.py`
- `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/ternary_log_1337.txt`
- `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/ternary_log_42.txt`
- `records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/ternary_log_7.txt`

## Claimed method summary
10L 768d ternary U-Net transformer with relu² 4x MLP, factored tied embedding (254-dim), FP8 QAT, poly5 softcap, YaRN 2048, NeoMuon optimizer (3 Newton-Schulz steps), base-3+LZMA compression. Sliding eval stride=16 with temperature scaling T=0.90. 3-seed mean 1.1570 bpb (std 0.0007).

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.1565
- Claimed `val_loss`: 2.9869
- Claimed artifact bytes: 15993853
- Metric mode: ternary branch metric with sliding eval + temp scaling

## Metric semantics / evaluation mode
- Single-run metric.
- Sliding-window evaluation is authoritative for this record.
- Quantization semantics must be checked from the record-local source.

## Reproduction prerequisites
- Required dataset: `record-local ternary assets / custom tokenizer workflow`
- Required tokenizer: `record-local 8192-BPE tokenizer files`
- Extra packages: zstandard, custom ternary setup.sh, 8192-BPE tokenizer assets
- Hardware notes: Separate branch with custom setup, tokenizer, and script; do not treat as root-trainer-compatible

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp8192 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/fineweb_8192_bpe.model \
ATTN_PROJ_TYPE=standard \
LOGIT_HEAD_TYPE=standard \
TVERSKY_MEMBERSHIP=sigmoid \
TVERSKY_NUM_FEATURES=0 \
TVERSKY_FEATURE_POOLS=0 \
VOCAB_SIZE=8192 \
BITNET_GROUP_SIZE=128 \
BIGRAM_HASH=0 \
EMBED_DIM=254 \
TRAINING_DEPTH_RECURRENCE=0 \
EVAL_DEPTH_RECURRENCE=0 \
NUM_LAYERS=10 \
MODEL_DIM=768 \
NUM_KV_HEADS=4 \
NUM_HEADS=8 \
DIFF_ATTN=0 \
MLP_MULT=4 \
MLP_GROUPS=0 \
MATRIX_OPTIMIZER=muon \
ADAM_LR=0.05 \
ADAM_WD=0.05 \
MUON_BACKEND_STEPS=3 \
MUON_MOMENTUM=0.95 \
MUON_MOMENTUM_WARMUP_START=0.85 \
MUON_MOMENTUM_WARMUP_STEPS=500 \
MUON_WD=0.0 \
MATRIX_LR=0.04 \
SCALAR_LR=0.02 \
TIED_EMBED_LR=0.02 \
WARMDOWN_FRACTION=0.2 \
LOGIT_SOFTCAP=10 \
QK_GAIN_INIT=2.25 \
ROPE_TYPE=yarn \
YARN_MAX_LEN=2048 \
ROPE_BASE=5000 \
BATCH_TOKENS_START=0 \
BATCH_SCHEDULE_FRACTION=0.33 \
TRAIN_BATCH_TOKENS=524288 \
SEQ_LEN_START=0 \
SEQ_SCHEDULE_FRACTION=0.0 \
TRAIN_SEQ_LEN=1024 \
SMEAR=0 \
ITERATIONS=10000 \
WARMUP_STEPS=5 \
MAX_WALLCLOCK_SECONDS=599 \
VAL_LOSS_EVERY=0 \
TRAIN_LOG_EVERY=1000 \
CHURN_LOG_EVERY=0 \
VAL_MAX_TOKENS=0 \
TIE_EMBEDDINGS=1 \
UNTIE_AT_FRACTION=0.00 \
HEAD_LR=0.02 \
CORR_WEIGHT_LR=0.02 \
ACTIVATION=relu2 \
SOFTCAP_TYPE=poly \
MTP_HEADS=0 \
REFINER=0 \
REFINER_KERNEL=3 \
SLIDING_EVAL=1 \
SLIDING_EVAL_STRIDE=16 \
SLIDING_BATCH_SIZE=256 \
TEMP_SCALING=1 \
FP_STORAGE=FP8 \
SEED=42 \
COMPILE_MODE=default \
OMP_NUM_THREADS=1 \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/train_gpt_cuda_ternary.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.1555
- Observed `val_loss`: 2.9842
- Observed artifact bytes: 15925540
- Observed completed steps: 6570
- Observed `step_avg_ms`: not yet recorded
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: -0.001
- `Δ val_loss`: -0.0027

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
