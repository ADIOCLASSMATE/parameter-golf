# Process log — 2026-03-19_TrainingOptSeq4096

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 14:49:13Z
- Action: Exact 8xH100 rerun completed from the TrainingOptSeq4096 standalone record script.
- Command / script: records/track_10min_16mb/2026-03-19_TrainingOptSeq4096/train_gpt.py
- Environment notes: uv-managed .venv with torch 2.8.0+cu128 on 8xH100; this host ran the script far faster than the source README numbers.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.19224339 val_loss=2.01305303 artifact=15871395 bytes steps=11397 step_avg=52.65ms.
- Next step: Launch 2026-03-19_SlidingWindowEval.

