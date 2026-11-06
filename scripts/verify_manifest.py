from pathlib import Path
import csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
manifest=ROOT/'provenance'/'SHA256_UPLOAD_MANIFEST.csv'
with manifest.open(newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
for row in rows:
    p=ROOT/row['path']
    assert p.is_file(), 'Missing: '+row['path']
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest==row['sha256'], 'SHA-256 mismatch: '+row['path']
print('PASS: %d repository assets match the SHA256 manifest.'%len(rows))
