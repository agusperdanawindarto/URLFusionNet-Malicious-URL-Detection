# Experimental protocol

## Dataset and split

- Dataset: sid321axn/malicious-urls-dataset.
- Raw: 651,191 URLs; after audit 641,113 samples.
- Fixed stratified 80/10/10: 512,890 train, 64,111 validation, 64,112 test.
- Class IDs: benign (0), defacement (1), phishing (2), malware (3).
- Character length 200; token length 40.
- Vocabulary adaptation and class weights derive from the training partition.
- Seeds: 42, 123, 2025.

## Architecture

- Character encoder: embedding dimension 32; Conv1D kernels (3, 5, 7).
- Token encoder: embedding dimension 48; masked attention and masked mean pooling.
- Aligned latent feature dimension: 96.
- Gate input: concatenation of aligned character and token features.
- Softmax gate: two sample-dependent weights; output is their weighted sum.
- Training stabilizer: balanced output-gate initialization; KL penalty toward uniform
  weights, with selected coefficient lambda = 0.005. The KL term is training-only.
- Multiclass output and class-weighted cross-entropy objective.

## Model selection

Two candidates: balanced_init (lambda=0) and balanced_kl005 (lambda=0.005).
The selected variant maximized mean **validation** Macro-F1 across the three
prespecified seeds. The held-out test metrics were then summarized by seed.

## Evaluation and limitations

The final stabilization run provides three-seed Macro-F1/accuracy/MCC, per-class
metrics, confusion matrices, and gate diagnostics.

Archived baseline, ablation, robustness, and efficiency results originate from
earlier experimental variants. They are included for transparency but MUST NOT
be claimed as measurements of the final stabilized checkpoint.

The test partition had also been inspected during earlier architecture work.
Therefore, this dataset's test results are not independently blind validation.
There was no external cross-dataset or temporal test for the selected model.

A three-seed difference is descriptive; this package makes no significance claim.
