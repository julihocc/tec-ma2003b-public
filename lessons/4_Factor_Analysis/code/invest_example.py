"""
Simple invest example: load an existing CSV dataset and run PCA.

Assumes a CSV at ../data/invest.csv with columns for assets (e.g. USst, USb, ...).
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

script_dir = os.path.dirname(__file__)
data_path = os.path.normpath(os.path.join(script_dir, "..", "data", "invest.csv"))
if not os.path.exists(data_path):
    raise SystemExit(
        f"Data file not found: {data_path}. Please place 'invest.csv' there and retry."
    )

X = pd.read_csv(data_path)
cols = list(X.columns)

# Standardize (use correlation-like behavior)
Xs = StandardScaler().fit_transform(X.values)

pca = PCA()
Z = pca.fit_transform(Xs)

eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# Scree plot
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Invest example: Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
scree_out = os.path.join(script_dir, "invest_scree.png")
plt.savefig(scree_out, dpi=150)
print(f"Saved {scree_out}")

# Biplot (first two components)
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
plt.title("Invest example: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":")
plt.tight_layout()
biplot_out = os.path.join(script_dir, "invest_biplot.png")
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")
