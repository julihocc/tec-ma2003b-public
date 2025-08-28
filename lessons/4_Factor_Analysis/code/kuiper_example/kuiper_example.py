# %% [markdown]
# Kuiper PCA example (py-percent style)
#
# This script loads a small CSV of Kuiper Belt / trans-Neptunian object
# orbital parameters (generated from MPCORB in this repo) and runs PCA on the
# standardized variables. It follows the same concise pattern used by
# `invest_example.py` so it can be run interactively in editors that support
# Run Cell.

# %%
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import sys

# %%
# Simple behaviour: expect kuiper.csv in the same folder as this script
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "kuiper.csv"
if not data_path.exists():
    print(
        f"Missing {data_path}. Run `fetch_kuiper.py` in the same folder to download kuiper.csv"
    )
    sys.exit(2)

X = pd.read_csv(data_path)
# If the CSV has a leading index-like column (common in some exports), drop it
cols = list(X.columns)
if cols and cols[0].lower() in ("rownames", "index"):
    X = X.iloc[:, 1:]
    cols = list(X.columns)

# %% [markdown]
# ## Preprocessing and PCA
#
# We standardize the input columns so PCA operates on a correlation-like
# matrix (each column will have mean ~0 and unit variance). This is common
# when variables have different units (e.g. AU vs degrees).

# %%
# Standardize (use correlation-like behaviour)
Xs = StandardScaler().fit_transform(X.values)

# Fit PCA and extract scores and summaries
pca = PCA()
Z = pca.fit_transform(Xs)

eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# %% [markdown]
# ## Scree plot
#
# The scree plot displays eigenvalues by component index. The script saves a
# small PNG next to the script for quick inspection.

# %%
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Kuiper example: Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
scree_out = script_dir / "kuiper_scree.png"
scree_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(scree_out, dpi=150)
print(f"Saved {scree_out}")

# %% [markdown]
# ## Biplot (PC1 vs PC2)
#
# A simple biplot showing the first two PC scores and the variable loadings.

# %%
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
plt.title("Kuiper example: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":")
plt.tight_layout()
biplot_out = script_dir / "kuiper_biplot.png"
biplot_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")
