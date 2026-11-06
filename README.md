# URLFusionNet: Stabilized Adaptive Multi-Scale Character–Token Fusion

Research code and archived evaluation evidence for:

**URLFusionNet: Adaptive Multi-Scale Character–Token Fusion for Multiclass
Malicious URL Detection** (IEEE Access manuscript under preparation).

URLFusionNet combines multi-scale character CNNs with contextual URL token
representations and an input-dependent two-weight fusion gate. The evaluated
stabilization uses balanced gate initialization and a lightweight KL penalty.

## Key evaluation results

| Model | Test Macro-F1 (mean ± SD, 3 seeds) |
|---|---:|
| Original adaptive (CUDA rerun) | 0.961430 ± 0.024708 |
| Fixed-average fusion | 0.975420 ± 0.000698 |
| **Stabilized adaptive (KL=0.005)** | **0.977070 ± 0.001405** |

The gain over fixed averaging is **0.001650 absolute Macro-F1 (0.165 percentage point)**,
based on three seeds. It is not established as statistically significant.
Fixed-average fusion had a smaller seed-to-seed standard deviation.
The selected gate did not collapse on the three evaluated seeds.

**Important scientific scope:** prior development had already consulted this test
partition; independent out-of-source and temporal validation has not been done.
Robustness and efficiency results stored in `results/historical_baseline` belong
to an earlier model, **not** the KL-stabilized selected checkpoint.

## Reproducible evidence

- Dataset: [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset).
- Raw URL rows: 651,191; deduplicated and label-audited rows: 641,113.
- Train/validation/test: 512,890 / 64,111 / 64,112 (stratified).
- Labels: benign, defacement, phishing, malware.
- Seeds: 42, 123, 2025.
- Selection criterion: mean validation Macro-F1 across seeds.
- Original experiment: Python 3.11.18, TensorFlow 2.20.0, NVIDIA RTX 3070 Ti Laptop GPU (WSL2).

## Repository layout

    notebooks/
      01_train_stabilization.ipynb
      02_fixed_average_comparison.ipynb
      03_results_and_figures_NO_TRAINING.ipynb
      historical/
    results/
      stabilized/
      fixedavg_and_original/
      historical_baseline/
      IEEE_models_mean_sd.csv
      IEEE_models_by_seed.csv
      IEEE_class_metrics.csv
    figures/
      Fig_01_... through Fig_11_...
      architecture/
    scripts/
      verify_results.py
      regenerate_figures.py
    docs/
    data/README.md
    provenance/
    references/
    checkpoints/README.md

## Quick start — results, no GPU required

    python -m pip install -r requirements.txt
    python scripts/verify_manifest.py
    python scripts/verify_results.py
    python scripts/regenerate_figures.py

Open `notebooks/03_results_and_figures_NO_TRAINING.ipynb` in VS Code/Jupyter for
the full results walkthrough. It does not fit new models.

To rerun training, see [Reproduction instructions](docs/reproduction.md).
For the research setup and limitations, see [Experiment protocol](docs/experimental_protocol.md).

## Attribution, reuse, and data policy

Raw Kaggle data are **not** committed; retrieve them from the source and respect
its terms. Pretrained weights are omitted from Git history; see
[checkpoint notes](checkpoints/README.md).

This repository does not include an automatically selected software license.
The authors should choose a license and verify contributor consent before
publishing source code for reuse.

Citation metadata: [CITATION.cff](CITATION.cff). The manuscript is a
work in preparation; no publication DOI is asserted.
