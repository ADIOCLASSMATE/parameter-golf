# Process log — 2026-03-18_FP16Embed_WD3600

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 14:05:41Z
- Action: Exact 8xH100 rerun completed from the FP16 embedding record-local snapshot.
- Command / script: records/track_10min_16mb/2026-03-18_FP16Embed_WD3600/train_gpt.py
- Environment notes: uv-managed .venv with torch 2.8.0+cu128 on 8xH100; no NCCL_IB_DISABLE in the source command.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.21952327 val_loss=2.05911395 artifact=15898280 bytes steps=13521 step_avg=44.38ms.
- Next step: Launch 2026-03-18_LongContextSeq2048.

