# Process log — 2026-03-18_LongContextSeq2048

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 14:28:18Z
- Action: Exact 8xH100 rerun completed from the LongContextSeq2048 standalone record script.
- Command / script: records/track_10min_16mb/2026-03-18_LongContextSeq2048/train_gpt.py
- Environment notes: uv-managed .venv with torch 2.8.0+cu128 on 8xH100; NCCL_IB_DISABLE=1 per source command.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.20647429 val_loss=2.03708130 artifact=15861715 bytes steps=11434 step_avg=52.48ms.
- Next step: Launch 2026-03-19_TrainingOptSeq4096.

