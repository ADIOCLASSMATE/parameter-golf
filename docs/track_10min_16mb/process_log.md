# Shared process log

Append one entry per major action during reproduction work.

## Template
- Timestamp:
- Record slug:
- Action:
- Outcome:
- Next step:

- Timestamp: 2026-04-01 13:33:52Z
- Record slug: 2026-03-17_NaiveBaseline
- Action: Ran exact 8xH100 rerun from the record-local script in the uv-managed environment.
- Outcome: Reproduced final_int8_zlib_roundtrip_exact val_bpb=1.22704765, worse than claimed by +0.00268195, with slower step time and fewer steps before the 600s cap.
- Next step: Continue Phase A with 2026-03-18_LowerLR.


- Timestamp: 2026-04-01 13:50:41Z
- Record slug: 2026-03-18_LowerLR
- Action: Ran exact 8xH100 rerun from the record-local script in the uv-managed baseline env.
- Outcome: Reproduced final_int8_zlib_roundtrip_exact val_bpb=1.22145208, beating the claimed 1.22296644 despite slower step throughput than the source H200 run.
- Next step: Continue Phase A with 2026-03-18_FP16Embed_WD3600.


- Timestamp: 2026-04-01 14:05:41Z
- Record slug: 2026-03-18_FP16Embed_WD3600
- Action: Ran exact 8xH100 rerun from the record-local script in the uv-managed baseline env.
- Outcome: Reproduced final_int8_zlib_roundtrip_exact val_bpb=1.21952327, essentially matching and slightly beating the claimed 1.21972502.
- Next step: Continue Phase A with 2026-03-18_LongContextSeq2048.


- Timestamp: 2026-04-01 14:28:18Z
- Record slug: 2026-03-18_LongContextSeq2048
- Action: Ran exact 8xH100 rerun from the standalone record script in the uv-managed baseline env.
- Outcome: Reproduced final_int8_zlib_roundtrip_exact val_bpb=1.20647429, slightly worse than the claimed 1.20576485 because the run completed fewer steps before the 600 s cap.
- Next step: Continue Phase A with 2026-03-19_TrainingOptSeq4096.


- Timestamp: 2026-04-01 14:49:13Z
- Record slug: 2026-03-19_TrainingOptSeq4096
- Action: Ran exact 8xH100 rerun from the standalone record script in the uv-managed baseline env.
- Outcome: Reproduced final_int8_zlib_roundtrip_exact val_bpb=1.19224339, much better than the claimed 1.20143417 because this host executed the script far faster and completed thousands more steps before the wallclock cap.
- Next step: Continue Phase A with 2026-03-19_SlidingWindowEval.


- Timestamp: 2026-04-01 15:09:56Z
- Record slug: 2026-03-19_SlidingWindowEval
- Action: Ran exact 8xH100 rerun from the record-local script in the uv-managed baseline env.
- Outcome: Reproduced sliding-window post-quant val_bpb=1.19342201, slightly worse than the claimed 1.19250007 because of slower step time and fewer steps before the wallclock cap.
- Next step: Phase A exact runs are complete; move on to Phase B if continuing execution in this session.


- Timestamp: 2026-04-01 16:20:26Z
- Record slug: 2026-03-17_LoRA_TTT
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 16:33:55Z
- Record slug: 2026-03-17_LoRA_TTT
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 16:33:55Z
- Record slug: 2026-03-19_10L_MixedPrecision
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 16:47:07Z
- Record slug: 2026-03-19_10L_MixedPrecision
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 16:47:07Z
- Record slug: 2026-03-19_MixedQuant_Int6Int8_SlidingWindow
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 17:01:21Z
- Record slug: 2026-03-19_MixedQuant_Int6Int8_SlidingWindow
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 17:01:21Z
- Record slug: 2026-03-19_WarmdownQuantization
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 17:13:16Z
- Record slug: 2026-03-19_WarmdownQuantization
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 17:13:17Z
- Record slug: 2026-03-19_Seq2048_FP16Emb_TunedLR
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 17:30:35Z
- Record slug: 2026-03-19_Seq2048_FP16Emb_TunedLR
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 17:30:35Z
- Record slug: 2026-03-19_MLP3x_QAT_Int6_SlidingWindow
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 17:45:34Z
- Record slug: 2026-03-19_MLP3x_QAT_Int6_SlidingWindow
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 17:45:34Z
- Record slug: 2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 17:56:53Z
- Record slug: 2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 17:56:53Z
- Record slug: 2026-03-19_smeargate_orthoinit_muonwd
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 18:10:10Z
- Record slug: 2026-03-19_smeargate_orthoinit_muonwd
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 18:10:10Z
- Record slug: 2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 18:25:59Z
- Record slug: 2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 18:25:59Z
- Record slug: 2026-03-20_10L_Int5MLP_MuonWD04_SWA50
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 18:41:59Z
- Record slug: 2026-03-20_10L_Int5MLP_MuonWD04_SWA50
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 18:42:08Z
- Record slug: 2026-03-20_11L_EfficientPartialXSA_FA3_SWA120
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 18:57:06Z
- Record slug: 2026-03-20_11L_EfficientPartialXSA_FA3_SWA120
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 18:57:06Z
- Record slug: 2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 19:11:03Z
- Record slug: 2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 19:11:03Z
- Record slug: 2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 19:26:10Z
- Record slug: 2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 19:26:10Z
- Record slug: 2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 19:40:20Z
- Record slug: 2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 19:40:20Z
- Record slug: 2026-03-23_LeakyReLU_LegalTTT_ParallelMuon
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 20:01:43Z
- Record slug: 2026-03-23_LeakyReLU_LegalTTT_ParallelMuon
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-01 20:01:44Z
- Record slug: 2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 20:14:18Z
- Record slug: 2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon
- Action: Exact reproduction run failed with exit code 1.
- Outcome: see local run log and reproduction.json.
- Next step: Keep the record documented as blocked.


- Timestamp: 2026-04-01 20:14:18Z
- Record slug: 2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-01 20:33:32Z
- Record slug: 2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.


- Timestamp: 2026-04-02 01:54:04Z
- Record slug: 2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon
- Action: Started exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Wait for local run completion.


- Timestamp: 2026-04-02 02:12:48Z
- Record slug: 2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon
- Action: Completed exact reproduction run.
- Outcome: see local run log and reproduction.json.
- Next step: Refresh rendered README and inventory.

