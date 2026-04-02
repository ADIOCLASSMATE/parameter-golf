# Process log — 2026-03-19_SlidingWindowEval

Use this file as the per-record work log for the reproducing agent.

## Template
- Timestamp:
- Action:
- Command / script:
- Environment notes:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 15:09:56Z
- Action: Exact 8xH100 rerun completed from the SlidingWindowEval record-local script.
- Command / script: records/track_10min_16mb/2026-03-19_SlidingWindowEval/train_gpt.py
- Environment notes: uv-managed .venv with torch 2.8.0+cu128 on 8xH100; sliding eval stride=64 and batch_seqs=1024.
- Outcome: final_int8_zlib_roundtrip_exact val_bpb=1.19342201 val_loss=2.01504050 artifact=15876349 bytes steps=13313 step_avg=45.07ms.
- Next step: Phase A exact reproductions complete; remaining work is Phase B onward.

