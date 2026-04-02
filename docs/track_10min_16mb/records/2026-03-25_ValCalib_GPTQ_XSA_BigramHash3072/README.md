# 2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072`
- Claimed run name: AR Self-Gen GPTQ + XSA-all + BigramHash 3072x112
- Author: abaybektursun
- Family: quantization / QAT / GPTQ
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_gpt.py`
- `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_seed314.log`
- `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_seed42.log`
- `records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_seed999.log`

## Claimed method summary
11L XSA-all + Full Hessian GPTQ with autoregressive self-generated calibration (no val/train data accessed during quantization) + selective-pruning stack. BigramHash(3072,112), warmdown=4000, lzma preset=9. 3-seed exact mean: 1.11473509 BPB / 1.88217853 nats, beating PR549's exact 3-seed mean 1.11937967 BPB / 1.89002068 nats by 0.00784215 nats (Welch t=-11.83, df=3.31).

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.11473509
- Claimed `val_loss`: 1.88217853
- Claimed artifact bytes: 15984850
- Metric mode: 3-seed exact mean sliding BPB

## Metric semantics / evaluation mode
- Multi-run metric.
- Sliding-window evaluation is authoritative for this record.
- Quantization semantics must be checked from the record-local source.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: flash-attn-3
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
BIGRAM_VOCAB_SIZE=3072 \
BIGRAM_DIM=112 \
WARMDOWN_ITERS=4000 \
TARGET_MB=15.9 \
SEED=314 \
uv run --python .venv-fa3/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.11516685
- Observed `val_loss`: 1.88290753
- Observed artifact bytes: not yet recorded
- Observed completed steps: 6859
- Observed `step_avg_ms`: 87.49
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00043176
- `Δ val_loss`: 0.000729

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
