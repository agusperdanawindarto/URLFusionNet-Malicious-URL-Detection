from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'results'
S = DATA / 'stabilized'
F = DATA / 'fixedavg_and_original'
seeds = {42, 123, 2025}
selected = pd.read_csv(S / 'configuration_selection_VALIDATION_ONLY.csv')
assert selected.loc[selected.Selected, 'variant'].iloc[0] == 'balanced_kl005'
a = pd.read_csv(S / 'selected_stabilized_test_results.csv')
b = pd.read_csv(F / 'fixedavg_multiseed_raw.csv')
c = pd.concat([pd.read_csv(F / ('proposed_rerun_seed%d_metrics.csv' % s))
               for s in sorted(seeds)], ignore_index=True)
for name,df in [('stabilized',a),('fixed-average',b),('original adaptive',c)]:
    assert set(map(int, df.Seed)) == seeds and len(df) == 3, name
    assert df[['Accuracy','Macro_F1','MCC']].notna().all().all(), name
    print('%s: Macro-F1 %.6f +/- %.6f' %
          (name,df.Macro_F1.mean(),df.Macro_F1.std(ddof=1)))

assert abs(a.Macro_F1.mean()-0.977070)<1e-5
assert abs(b.Macro_F1.mean()-0.975420)<1e-5
assert abs(c.Macro_F1.mean()-0.961430)<1e-5
classes = ['benign','defacement','phishing','malware']
for seed in sorted(seeds):
    path = S / ('confusion_matrix_seed%d.csv' % seed)
    cm = pd.read_csv(path,index_col=0).loc[classes,classes]
    assert int(cm.to_numpy().sum()) == 64112
    rep = pd.read_csv(S / ('classification_report_seed%d.csv' % seed),index_col=0)
    assert all(int(cm.loc[k].sum())==int(rep.loc[k,'support']) for k in classes)
    h = pd.read_csv(S / ('history_balanced_kl005_seed%d.csv' % seed))
    assert np.isfinite(h['val_macro_f1']).all()
    g = pd.read_csv(S / ('gate_diagnostic_seed%d.csv' % seed))
    assert len(g)==1 and not bool(g['collapsed'].iloc[0])
    print('Seed %d: confusion n=64112, class supports and gate diagnostics PASS' % seed)
print('PASS — source evidence verified; no training executed.')
