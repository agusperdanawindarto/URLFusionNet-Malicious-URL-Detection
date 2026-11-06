# Panduan Unggah URLFusionNet ke GitHub

**Folder proyek siap unggah:** D:\RISETKOLABORASI\EPHI\URLFusionNet_GITHUB_READY

**Nama repository disarankan:** URLFusionNet-Malicious-URL-Detection

**Akun GitHub terhubung:** agusperdanawindarto

## Langkah tanpa PowerShell — GitHub Desktop

1. Buka **GitHub Desktop** dan masuk ke akun GitHub Anda.
2. Pilih **File > Add local repository**.
3. Arahkan ke folder `D:\RISETKOLABORASI\EPHI\URLFusionNet_GITHUB_READY`.
4. Jika muncul pesan belum berupa Git repository, pilih **Create a repository here**.
5. Buat commit pertama dengan pesan `Initial URLFusionNet research release`.
6. Klik **Publish repository**. Pastikan akun pemilik benar.
7. Pilih **Public** hanya jika para pemilik kode menyetujui publikasinya.
8. Buka GitHub dan pastikan README, notebook, grafik, serta CSV tampil.

## Alternatif — melalui VS Code

1. **File > Open Folder** lalu pilih URLFusionNet_GITHUB_READY.
2. Buka **Source Control** di sidebar.
3. Pilih **Initialize Repository**.
4. Pastikan tidak ada file `.weights.h5`, dataset mentah, atau kredensial.
5. Isi commit message `Initial URLFusionNet research code and evidence`.
6. Klik **Publish Branch / Publish to GitHub**.
7. Pilih akun, nama repository, dan visibilitasnya.

## Isi paket

- 5 notebook IPYNB: dua eksperimen utama, satu notebook analisis tanpa training, dua eksperimen historis.
- 89 CSV, meliputi hasil tiga seed dan evaluasi terperinci.
- 14 grafik PNG dan berkas PDF vektor.
- Script verifikasi, regenerasi grafik, dan SHA-256 untuk audit.
- README, protokol penelitian, dan petunjuk reproduksi.
- Manifest checkpoint H5; model besar tidak dimasukkan ke paket.

## Pemeriksaan di VS Code

Buka `notebooks/03_results_and_figures_NO_TRAINING.ipynb`.
Notebook ini hanya membaca hasil CSV dan tidak membutuhkan GPU.

Notebook 01 dan 02 memerlukan dataset asli serta lingkungan TensorFlow.
Jangan mengunggah data mentah Kaggle atau checkpoint tanpa memeriksa lisensi.

## Catatan ilmiah

Stabilized adaptive model menghasilkan test Macro-F1 `0.977070 ± 0.001405`,
sedangkan FixedAvg `0.975420 ± 0.000698`.
Perbedaan tidak diklaim signifikan secara statistik. Hasil robustness/efficiency
historis bukan pengukuran pada checkpoint KL-stabilized final. Test set pernah
ditinjau pada iterasi arsitektur sebelumnya.
