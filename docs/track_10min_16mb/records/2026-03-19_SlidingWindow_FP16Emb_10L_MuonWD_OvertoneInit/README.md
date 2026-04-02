# 2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit`
- Claimed run name: Sliding Window + FP16 Embed + 10L + Muon WD + Overtone Init
- Author: notapplica
- Family: averaging / optimizer / schedule refinements
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_gpt.py`
- `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_seed1337.log`
- `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_seed42.log`
- `records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_seed7.log`

## Claimed method summary
No additional summary extracted yet.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: not yet recorded
- Claimed `val_loss`: not yet recorded
- Claimed artifact bytes: not yet recorded
- Metric mode: 3-seed mean sliding-window post-quant eval

## Metric semantics / evaluation mode
- Multi-run metric.
- Sliding-window evaluation is authoritative for this record.
- Authoritative score is post-quant.

## Reproduction prerequisites
- Required dataset: `fineweb10B_sp1024`
- Required tokenizer: `fineweb_1024_bpe.model`
- Extra packages: none beyond the root uv environment
- Hardware notes: 8xH100 SXM target unless record README says otherwise

## Exact reproduction command
```bash
RUN_ID=executor_2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.20669782
- Observed `val_loss`: 2.03745872
- Observed artifact bytes: 15388943
- Observed completed steps: 11942
- Observed `step_avg_ms`: 50.25
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: not yet recorded
- `Δ val_loss`: not yet recorded

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
