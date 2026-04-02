# track_10min_16mb inventory

This index normalizes all current record folders under `records/track_10min_16mb` and links to the local documentation scaffold for later reproduction work.

| Record | Author | Claimed BPB | Family | Metric mode | Status | Local doc |
|---|---|---:|---|---|---|---|
| `2026-03-17_LoRA_TTT` | sam | 1.1929 | context length and evaluation changes | TTT-enhanced eval metric | `exact` | [doc](records/2026-03-17_LoRA_TTT/README.md) |
| `2026-03-17_NaiveBaseline` | Baseline | 1.2243657 | baseline / simple schedule tuning | final_int8_zlib_roundtrip_exact | `exact` | [doc](records/2026-03-17_NaiveBaseline/README.md) |
| `2026-03-18_FP16Embed_WD3600` | Renier Velazco | 1.21972502 | baseline / simple schedule tuning | final_int8_zlib_roundtrip_exact | `exact` | [doc](records/2026-03-18_FP16Embed_WD3600/README.md) |
| `2026-03-18_LongContextSeq2048` | Spokane Way | 1.20576485 | context length and evaluation changes | final_int8_zlib_roundtrip_exact (3-seed support) | `exact` | [doc](records/2026-03-18_LongContextSeq2048/README.md) |
| `2026-03-18_LowerLR` | Nan Liu | 1.22296644 | baseline / simple schedule tuning | final_int8_zlib_roundtrip_exact | `exact` | [doc](records/2026-03-18_LowerLR/README.md) |
| `2026-03-19_10L_MixedPrecision` | Nan Liu | 1.214745 | quantization / QAT / GPTQ | final mixed-precision post-quant eval | `exact` | [doc](records/2026-03-19_10L_MixedPrecision/README.md) |
| `2026-03-19_MLP3x_QAT_Int6_SlidingWindow` | aruniyer | 1.15015359 | quantization / QAT / GPTQ | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_MLP3x_QAT_Int6_SlidingWindow/README.md) |
| `2026-03-19_MixedQuant_Int6Int8_SlidingWindow` | aquariouseworkman | 1.16301431 | quantization / QAT / GPTQ | sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_MixedQuant_Int6Int8_SlidingWindow/README.md) |
| `2026-03-19_Seq2048_FP16Emb_TunedLR` | yahya010 | 1.15861696 | quantization / QAT / GPTQ | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_Seq2048_FP16Emb_TunedLR/README.md) |
| `2026-03-19_SlidingWindowEval` | Matthew Li | 1.19250007 | context length and evaluation changes | sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_SlidingWindowEval/README.md) |
| `2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit` | notapplica | N/A | averaging / optimizer / schedule refinements | 3-seed mean sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_SlidingWindow_FP16Emb_10L_MuonWD_OvertoneInit/README.md) |
| `2026-03-19_TrainingOptSeq4096` | Spokane Way | 1.20143417 | context length and evaluation changes | final_int8_zlib_roundtrip_exact (3-seed support) | `exact` | [doc](records/2026-03-19_TrainingOptSeq4096/README.md) |
| `2026-03-19_WarmdownQuantization` | samuellarson | 1.1574404 | quantization / QAT / GPTQ | sliding-window post-quant eval | `exact` | [doc](records/2026-03-19_WarmdownQuantization/README.md) |
| `2026-03-19_int6_STE QAT_ MLP_bigram _U_Net` | N/A | N/A | incomplete / orphaned snapshot | unknown / missing metadata | `incomplete_repo_snapshot` | [doc](records/2026-03-19_int6_STE QAT_ MLP_bigram _U_Net/README.md) |
| `2026-03-19_smeargate_orthoinit_muonwd` | N/A | 1.1556 | architecture additions | single-run post-quant eval | `exact` | [doc](records/2026-03-19_smeargate_orthoinit_muonwd/README.md) |
| `2026-03-20_10L_Int5MLP_MuonWD04_SWA50` | thwu1 | N/A | averaging / optimizer / schedule refinements | 3-seed mean post-quant eval | `exact` | [doc](records/2026-03-20_10L_Int5MLP_MuonWD04_SWA50/README.md) |
| `2026-03-20_11L_EfficientPartialXSA_FA3_SWA120` | vadim borisov (tabularis.ai) | 1.13071416 | architecture additions | single-run post-quant eval | `exact` | [doc](records/2026-03-20_11L_EfficientPartialXSA_FA3_SWA120/README.md) |
| `2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271` | Jack Princz | 1.12707468 | architecture additions | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-20_11L_XSA4_EMA_Int6_MLP3x_WD04_1.1271/README.md) |
| `2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA` | Raahil Shah | 1.14581692 | architecture additions | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-20_Int6_MLP3x_SmearGate_BigramHash_MuonWD_SWA/README.md) |
| `2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248` | Jack Princz | 1.12484502 | architecture additions | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-21_11L_XSA4_EMA_PartialRoPE_LateQAT_1.1248/README.md) |
| `2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233` | Tianhao Wu | 1.12278022 | quantization / QAT / GPTQ | 3-seed sliding-window post-quant eval | `exact` | [doc](records/2026-03-22_11L_EMA_GPTQ-lite_warmdown3500_QAT015_1.1233/README.md) |
| `2026-03-23_LeakyReLU_LegalTTT_ParallelMuon` | abaybektursun | 1.1194 | averaging / optimizer / schedule refinements | 3-seed mean with legal TTT | `exact` | [doc](records/2026-03-23_LeakyReLU_LegalTTT_ParallelMuon/README.md) |
| `2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon` | Ciprian-Florin Ifrim | 1.1565 | separate ternary / 8192-BPE branch | ternary branch metric with sliding eval + temp scaling | `exact` | [doc](records/2026-03-24_74M_Ternary_UNet_FP8_10L_8192BPE_YaRN_NeoMuon/README.md) |
| `2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072` | abaybektursun | 1.11473509 | quantization / QAT / GPTQ | 3-seed exact mean sliding BPB | `exact` | [doc](records/2026-03-25_ValCalib_GPTQ_XSA_BigramHash3072/README.md) |
