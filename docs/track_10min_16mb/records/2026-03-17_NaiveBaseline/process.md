# Process log — 2026-03-17_NaiveBaseline

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 13:33:52Z
- Action: Exact 8xH100 rerun completed with the record-local script via uv-managed .venv and local SP-1024 data.
- Command / script: records/track_10min_16mb/2026-03-17_NaiveBaseline/train_gpt.py
- Environment notes: torch 2.8.0+cu128 inside .venv; 8xH100 detected; NCCL_IB_DISABLE=1 per source command.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.22704765 val_loss=2.07181856 artifact=15858571 bytes steps=13282 step_avg=45.18ms.
- Next step: Launch 2026-03-18_LowerLR and compare whether the H100 host reproduces the historical step budget more closely.

