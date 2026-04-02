# Process log — 2026-03-18_LowerLR

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 13:50:41Z
- Action: Exact 8xH100 rerun completed from the record-local LowerLR snapshot.
- Command / script: records/track_10min_16mb/2026-03-18_LowerLR/train_gpt.py
- Environment notes: uv-managed .venv with torch 2.8.0+cu128 on 8xH100; source README notes historical provenance on 8xH200.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.22145208 val_loss=2.06237068 artifact=15872659 bytes steps=13261 step_avg=45.25ms.
- Next step: Launch 2026-03-18_FP16Embed_WD3600.

