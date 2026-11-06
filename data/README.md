# Dataset acquisition — not bundled

Primary source: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

Expected original CSV: malicious_phish.csv, 651,191 rows, four classes.
The original local CSV SHA-256 recorded in the final run manifest is:

    d83ce942075dd63ed4d11560cfdcd9d512caa3d680e292f22cab484e8f074d01

Local verified audit: 641,113 retained, 10,078 removed (deduplication and label conflicts).
Split: 512,890 train, 64,111 validation, 64,112 test (80:10:10; stratified).
Labels (clean): benign 428,074; defacement 95,308; phishing 94,086; malware 23,645.

Place the downloaded CSV at data/raw/malicious_phish.csv, or set the
URLFUSIONNET_DATASET_CSV environment variable to its absolute location.
The training notebooks also contain the public kagglehub download fallback.
Confirm source rights and the Kaggle dataset terms before redistribution.
