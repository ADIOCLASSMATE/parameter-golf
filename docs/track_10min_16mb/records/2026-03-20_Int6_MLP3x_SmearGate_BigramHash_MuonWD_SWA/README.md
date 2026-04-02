# 2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA

## Record identity
- Record folder: `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA`
- Claimed run name: Int6 MLP3x + SmearGate + BigramHash + OrthoInit + Muon WD + SWA
- Author: Raahil Shah
- Family: architecture additions
- Current review status: `exact`

## Source files used
- README: `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/README.md`
- Submission metadata: `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/submission.json`
- Script snapshot: `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_gpt.py`
- `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_seed1337.log`
- `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_seed42.log`
- `records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_seed7.log`

## Claimed method summary
Per-row int6 quantization on MLP/attention weights with zstd-22 compression, enabling 3x MLP expansion (hidden=1536). SmearGate blends adjacent token embeddings via a learned gate. BigramHash embedding (4096 buckets, dim=128) captures token-pair context. Orthogonal weight initialization with muP output scaling. Muon optimizer with decoupled weight decay (WD=0.04) and momentum warmup (0.92->0.99 over 1500 steps). Stochastic Weight Averaging every 50 steps over the last 50% of training. Trained at seq_len=2048 with batch=786432, grad_clip=0.3, warmdown=3000. Sliding window evaluation at stride=64.

## Claimed metrics
- Claimed metric name: `val_bpb`
- Claimed `val_bpb`: 1.14581692
- Claimed `val_loss`: 1.93465876
- Claimed artifact bytes: 15862650
- Metric mode: 3-seed sliding-window post-quant eval

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
RUN_ID=executor_2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA_exact \
DATA_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=/inspire/hdd/global_user/wanjiaxin-253108030048/code/bag-of-tricks-transformers/parameter-golf/data/tokenizers/fineweb_1024_bpe.model \
uv run --python .venv/bin/python torchrun --standalone --nproc_per_node=8 \
records/track_10min_16mb/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/train_gpt.py
```

## Observed reproduction results
- Reproduction status: `exact`
- Observed `val_bpb`: 1.1464501
- Observed `val_loss`: 1.93572784
- Observed artifact bytes: 15899844
- Observed completed steps: 7219
- Observed `step_avg_ms`: 83.13
- W&B run name/path: not yet recorded
- Local run log: docs/track_10min_16mb/records/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/run_exact.log

## Delta vs claimed result
- `Δ val_bpb`: 0.00063318
- `Δ val_loss`: 0.00106908

## Notes / discrepancies / legality caveats
- Exact current-session rerun used the record-local script snapshot and local dataset/tokenizer paths.
- Metric semantics were preserved from the record-local script; compare only against records with matching evaluation mode.
- See the local run log for the concrete throughput and final metric lines on this host.
