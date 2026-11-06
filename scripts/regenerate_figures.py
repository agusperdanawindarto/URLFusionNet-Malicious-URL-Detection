from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
T=ROOT/'results'
S=T/'stabilized'
OUT=ROOT/'outputs'/'figures_regenerated'
OUT.mkdir(parents=True, exist_ok=True)
seeds=[42,123,2025]
frame=pd.read_csv(T/'IEEE_models_by_seed.csv')
fig,ax=plt.subplots(figsize=(7,3.9))
styles=[('Original adaptive','o','--','0.3'),
        ('Fixed-average fusion','s','-.','0.65'),
        ('Stabilized adaptive','D','-','0.05')]
for name,marker,style,color in styles:
    d=frame[frame.Model==name].sort_values('Seed')
    ax.plot(d.Seed.astype(str),d.Macro_F1,marker=marker,ls=style,color=color,label=name)
ax.set(xlabel='Seed',ylabel='Held-out test Macro-F1',ylim=(0.91,0.99))
ax.legend(fontsize=8);ax.grid(axis='y',alpha=0.2)
fig.tight_layout();fig.savefig(OUT/'comparison_per_seed.png',dpi=300);plt.close(fig)
means=frame.groupby('Model')['Macro_F1'].agg(['mean','std'])
fig,ax=plt.subplots(figsize=(7,3.8))
order=[x[0] for x in styles]
ax.bar(range(3),means.loc[order,'mean'],yerr=means.loc[order,'std'],
       color=['0.85','0.65','0.25'],edgecolor='black',capsize=5)
ax.set_xticks(range(3),['Original','Fixed-average','Stabilized'])
ax.set(ylabel='Test Macro-F1, mean +/- SD (n=3)',ylim=(0.90,0.99))
fig.tight_layout();fig.savefig(OUT/'comparison_mean_std.png',dpi=300);plt.close(fig)
classes=['benign','defacement','phishing','malware']
for seed in seeds:
    cm=pd.read_csv(S/('confusion_matrix_seed%d.csv'%seed),index_col=0).loc[classes,classes]
    fig,ax=plt.subplots(figsize=(6.1,4.6))
    ax.imshow(cm.to_numpy(),cmap='Greys')
    for i in range(4):
        for j in range(4):
            n=int(cm.iloc[i,j])
            ax.text(j,i,format(n,','),ha='center',va='center',
                    color='white' if n>cm.to_numpy().max()/2 else 'black')
    ax.set_xticks(range(4),[x.title() for x in classes])
    ax.set_yticks(range(4),[x.title() for x in classes])
    ax.set(xlabel='Predicted class',ylabel='True class',title='Seed %d'%seed)
    fig.tight_layout()
    fig.savefig(OUT/('confusion_seed%d.png'%seed),dpi=300)
    plt.close(fig)
print('Figures regenerated:',OUT)
