"""
Synthetic 'invest' example: generates an investment allocation-style dataset,
runs PCA, saves scree plot and a simple biplot.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Prefer a provided dataset to avoid regenerating synthetic data each run
import os

data_path = os.path.join("..", "data", "invest.csv")
if os.path.exists(data_path):
    X = pd.read_csv(data_path)
    cols = list(X.columns)
    print(f"Loaded dataset from {data_path}, shape={X.shape}")
else:
    # Create a synthetic invest-like dataset: 8 asset returns with correlation structure
    rng = np.random.RandomState(1)
    n = 150
    # Create two market factors and some idiosyncratic noise
    m1 = rng.normal(size=(n, 1))
    m2 = rng.normal(size=(n, 1))
    assets = np.hstack(
        [
            0.8 * m1 + 0.2 * rng.normal(size=(n, 1)),
            0.7 * m1 + 0.3 * rng.normal(size=(n, 1)),
            0.6 * m1 + 0.4 * rng.normal(size=(n, 1)),
            0.5 * m2 + 0.5 * rng.normal(size=(n, 1)),
            0.4 * m2 + 0.6 * rng.normal(size=(n, 1)),
            0.3 * m2 + 0.7 * rng.normal(size=(n, 1)),
            0.2 * m1 + 0.2 * m2 + 0.6 * rng.normal(size=(n, 1)),
            rng.normal(size=(n, 1)),
        ]
    )

    cols = ["USst", "USb", "Dst", "Alt", "Cash", "GS", "BoA", "Other"]
    X = pd.DataFrame(assets, columns=cols)

# Standardize
Xs = StandardScaler().fit_transform(X)

pca = PCA()
Z = pca.fit_transform(Xs)

eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# Scree
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Invest example: Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
plt.savefig("lessons/4_Factor_Analysis/code/invest_scree.png", dpi=150)
print("Saved invest_scree.png")

# Biplot (first two components)
plt.figure(figsize=(5, 5))
xs = Z[:, 0]
ys = Z[:, 1]
plt.scatter(xs, ys, alpha=0.6, s=20)
for i, col in enumerate(cols):
    # arrow from origin to loading vector (scaled)
    vx, vy = pca.components_[:2, i] * max(xs.std(), ys.std()) * 3
    plt.arrow(0, 0, vx, vy, color="r", head_width=0.05)
    plt.text(vx * 1.05, vy * 1.05, col, color="r")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Invest example: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":")
plt.tight_layout()
plt.savefig("lessons/4_Factor_Analysis/code/invest_biplot.png", dpi=150)
print("Saved invest_biplot.png")
