# Method taxonomy for `track_10min_16mb`

## 1. Baseline / simple schedule tuning
Representative records:
- `2026-03-17_NaiveBaseline`
- `2026-03-18_LowerLR`
- `2026-03-18_FP16Embed_WD3600`

These mostly keep the baseline architecture and improve learning rates, warmdown, or artifact accounting.

## 2. Context length and evaluation changes
Representative records:
- `2026-03-18_LongContextSeq2048`
- `2026-03-19_TrainingOptSeq4096`
- `2026-03-19_SlidingWindowEval`
- `2026-03-17_LoRA_TTT`

These alter sequence length, evaluation context usage, or add test-time adaptation without fully changing the architectural core.

## 3. Quantization / QAT / GPTQ
Representative records:
- `2026-03-19_10L_MixedPrecision`
- `2026-03-19_MixedQuant_Int6Int8_SlidingWindow`
- `2026-03-19_WarmdownQuantization`
- `2026-03-19_Seq2048_FP16Emb_TunedLR`
- `2026-03-19_MLP3x_QAT_Int6_SlidingWindow`
- `2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233`
- `2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072`

These records spend the 16 MB budget more aggressively through int6/int5/ternary-style compression, PTQ/QAT, GPTQ-lite, or full-Hessian GPTQ.

## 4. Architecture additions
Representative records:
- `2026-03-19_smeargate_orthoinit_muonwd`
- `2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA`
- `2026-03-20_11L_EfficientPartialXSA_FA3_SWA120`
- `2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271`
- `2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248`

These add zero- or low-parameter architectural tricks such as SmearGate, BigramHash, U-Net skips, XSA, Partial RoPE, and related capacity reallocations.

## 5. Averaging / optimizer / schedule refinements
Representative records:
- `2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit`
- `2026-03-20_10L_Int5MLP_MuonWD04_SWA50`
- `2026-03-23_LeakyReLU_LegalTTT_ParallelMuon`

These emphasize optimizer behavior, weight decay, SWA/EMA, Parameter Banking, Parallel Muon, and evaluation-time policy choices.

## 6. Separate ternary / 8192-BPE branch
Representative record:
- `2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon`

Treat this as a separate track inside the same directory because it uses its own tokenizer assets, setup scripts, and trainer.

## 7. Incomplete / orphaned snapshot
- `2026-03-19_int6_STE QAT_ MLP_bigram _U_Net`

This should be documented but not treated as faithfully reproducible from the current repository snapshot.
