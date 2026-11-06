# Reproducing the experiment

## A. Inspect existing results (recommended, CPU-only)

1. Install Python 3.11 and install requirements: `python -m pip install -r requirements.txt`.
2. Open `notebooks/03_results_and_figures_NO_TRAINING.ipynb` from the repository folder
   in Jupyter or VS Code; choose the Python environment that has the packages.
3. Run all notebook cells. This reads the published CSVs/figures without training.
4. Run `python scripts/verify_results.py` to validate the stored result values.
5. Run `python scripts/regenerate_figures.py` to regenerate selected evaluation charts
   in `outputs/figures_regenerated` (ignored by Git).

## B. Retrain from scratch (GPU recommended)

1. Download the dataset using the source URL in `data/README.md`.
2. Put `malicious_phish.csv` in `data/raw/` or set `URLFUSIONNET_DATASET_CSV`.
3. On Linux/WSL with working NVIDIA GPU, install dependencies and verify TensorFlow GPU.
4. Open `notebooks/01_train_stabilization.ipynb`, which contains the final stabilized
   architecture and seed-42/123/2025 training protocol. Results write to `outputs/stabilization`
   unless `URLFUSIONNET_RESULT_DIR` is set.
5. Open `notebooks/02_fixed_average_comparison.ipynb` for the fixed-fusion comparator.
6. Historical notebooks are preserved under `notebooks/historical/`; they may require
   older configurations and should not be conflated with final stabilized evaluations.

The notebook sources are derived from the actual executed research notebooks with
stored cell outputs stripped for GitHub. Only result directory portability and an
optional dataset-path override were added to the two GPU notebooks; model architecture,
experimental seeds and hyperparameters were not modified.

## CUDA environment in the completed run

- OS: Ubuntu (WSL2) on Windows.
- Python: 3.11.18.
- TensorFlow: 2.20.0.
- GPU: NVIDIA GeForce RTX 3070 Ti Laptop GPU (8 GB).
- Use a TensorFlow-supported NVIDIA driver and CUDA environment for your host.

Numerical reproducibility may vary by platform, GPU kernels, and dependency versions.
