# 2026-03-19_WarmdownQuantization

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_WarmdownQuantization`
- Claimed run name: Int6 MLP3x Sliding Window
- Author: samuellarson
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_WarmdownQuantization/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_WarmdownQuantization/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_WarmdownQuantization/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_WarmdownQuantization/train.log`

## Claimed method summary
Int6 post-training quantization enables 3x MLP expansion (21.8M params in 16MB). Combined with train@2048 + sliding window eval + FP16 tied embeddings + Late-K passthrough.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.1574404
- Claimed `val_loss`: 1.95428963
- Claimed artifact bytes: 15977717
- Metric mode: sliding-window post-quant eval

## Metric semantics / evaluation mode
- Single-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: zstandard
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-19_WarmdownQuantization_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
WARMDOWN_ITERS=20000 \
MATRIX_LR=0.06 \
TIED_EMBED_LR=0.07 \
SCALAR_LR=0.06 \
GRAD_CLIP_NORM=1.0 \
MUON_BACKEND_STEPS=5 \
EVAL_SEQ_LEN=1408 \
MLP_HIDDEN=992 \
MAX_WALLCLOCK_SECONDS=600 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_WarmdownQuantization/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.22078011
- Observed `val_loss`: 2.06123489
- Observed artifact bytes: 12510294
- Observed completed steps: 13403
- Observed `step_avg_ms`: 44.77
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_WarmdownQuantization/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.06333971
- `Δ val_loss`: 0.10694526

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
