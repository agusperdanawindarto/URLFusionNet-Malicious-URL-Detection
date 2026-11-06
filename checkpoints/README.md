# Model checkpoints (not committed)

Training checkpoint files are available in the researcher's local full evidence
archive; they are intentionally excluded from Git version control because there
are twelve ~18 MB binary files.

See provenance/checkpoint_manifest.csv for the original file names, SHA-256
checksums, and sizes. Do not upload every checkpoint into a normal Git commit.

For a downloadable pretrained model, the authors may optionally publish the
three selected balanced_kl005 seed checkpoints separately as GitHub Release
assets or through Git LFS. Restore the matching model architecture, feature
vocabulary and preprocessing from the training notebook; raw weights alone
are insufficient to reproduce tokenization and inference.
