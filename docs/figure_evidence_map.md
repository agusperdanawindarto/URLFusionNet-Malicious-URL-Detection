# Figure-to-evidence map

| Figure | Evidence scope |
|---|---|
| Fig_01_Three_Model_Seed_Comparison | Original adaptive, fixed average, stabilized; same seeds. |
| Fig_02_Mean_SD_Comparison | Three-seed mean and sample SD on the test set. |
| Fig_03_Per_Class_F1 | Final stabilized per-class F1 from classification reports. |
| Fig_04_Confusion_Seed42/123/2025 | Final stabilized confusion matrices, 64,112 test URLs each. |
| Fig_05_Gate_By_Seed | Final selected stabilized gate mean and per-URL SD. |
| Fig_06_Validation_Selection | Model selection using validation, not test. |
| Fig_07_Training_Validation_Curves | Learning curves from saved final training histories. |
| Fig_08_Archived_Baselines | Historical one-seed models; no three-seed inference. |
| Fig_09_Archived_Robustness | Earlier adaptive variant, NOT the selected stabilized model. |
| Fig_10_Original_Stabilization | Original gate stabilization diagram. |
| Fig_11_Archived_Ablation | Earlier adaptive ablation variant, NOT the final stabilized checkpoint. |
| figures/architecture/Fig_1_... | High-resolution research framework, not an experimental plot. |

The exact supporting CSV filenames are under results/stabilized,
results/fixedavg_and_original, and results/historical_baseline.
