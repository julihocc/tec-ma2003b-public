# %% [markdown]
# Kuiper Belt PCA example (invest_example style)
#
# This script expects `kuiper.csv` in the same folder. If the CSV is missing
# run `fetch_kuiper.py` in the same directory to download it (keeps fetching
# and analysis separate). The script standardizes variables, runs PCA and
# saves a scree plot and a small biplot next to the script.

from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# Simple behaviour: expect kuiper.csv in the same folder as this script
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "kuiper.csv"

if not data_path.exists():
    print(
        f"Missing {data_path}. Run `fetch_kuiper.py` in the same folder to download kuiper.csv"
    )
    sys.exit(2)

df = pd.read_csv(data_path)
# If the CSV has a leading index-like column (common in some exports), drop it
cols = list(df.columns)
if cols and cols[0].lower() in ("rownames", "index"):
    df = df.iloc[:, 1:]

# Preprocess and PCA (standardize so PCA behaves like on correlation matrix)
Xs = StandardScaler().fit_transform(df.values)
pca = PCA()
Z = pca.fit_transform(Xs)

eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# Scree plot
save_path = script_dir / "kuiper_scree.png"
save_path.parent.mkdir(parents=True, exist_ok=True)
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Kuiper: Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
plt.savefig(save_path, dpi=150)
print(f"Saved {save_path}")

# Biplot (first two components) — small and optional
plt.figure(figsize=(5, 5))
xs = Z[:, 0]
ys = Z[:, 1]
plt.scatter(xs, ys, alpha=0.6, s=20)
for i, col in enumerate(cols):
    vx, vy = pca.components_[:2, i] * max(xs.std(), ys.std()) * 3
    plt.arrow(0, 0, vx, vy, color="r", head_width=0.05)
    plt.text(vx * 1.05, vy * 1.05, col, color="r")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Kuiper: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":")
plt.tight_layout()
biplot_out = script_dir / "kuiper_biplot.png"
biplot_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")
