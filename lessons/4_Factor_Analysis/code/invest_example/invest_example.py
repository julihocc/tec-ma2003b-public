# %% [markdown]
"""
Invest PCA example

This script loads a small CSV of asset returns and runs PCA on the
correlation-like matrix (by standardizing returns first). It contains
py-percent cells and detailed comments so you can run it interactively
and read the explanation of the outputs inline.

What to expect when you run this file:
- Printed `eigenvalues`: the variances explained by each principal component.
- Printed `explained_ratio`: proportion of total variance per component.
- Printed `cumulative`: cumulative explained variance used to decide how many
    components to retain.

The file also saves two figures next to the script: a scree plot and a
biplot for the first two PCs.
"""

# %%
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# %%
# Simple behaviour: expect invest.csv in the same folder as this script
# Use Path to make paths robust regardless of current working directory.
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "invest.csv"
X = pd.read_csv(data_path)
# If the CSV has a leading index-like column (common in some exports), drop it
cols = list(X.columns)
if cols and cols[0].lower() in ("rownames", "index"):
    X = X.iloc[:, 1:]
    cols = list(X.columns)

# %% [markdown]
# Preprocessing and PCA
"""
We standardize the input columns so PCA operates on a correlation-like
matrix (each column will have mean ~0 and unit variance). This is common
when variables are on different scales or when you want components to be
scale-invariant (e.g., asset returns).
"""

# %%
# Standardize (use correlation-like behavior)
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
"""
Interpreting the printed results (example and guidance):

- `eigenvalues`: these are the variances of the principal components.
    Larger eigenvalues mean the component explains more variance in the data.
    Example output: `[3.895, 0.092, 0.011, 0.004]` indicates the first
    component explains most of the variance.

- `explained_ratio`: fraction of total variance explained by each component.
    If the first entry is ~0.97, then PC1 explains 97% of the variance and a
    one-component summary may be adequate for many purposes (dimensionality
    reduction, visualization, or constructing a single-factor model).

- `cumulative`: shows how variance accumulates across components. Common
    decision rules: choose the smallest number of components that reach a
    target (e.g., 80-95%) of cumulative variance, or use the scree plot elbow.

Notes on this dataset and outputs:
- Financial return matrices often have one dominant component (market), so
    it's common to see a very large first eigenvalue and small remaining ones.
- PCA here is descriptive — further steps (rotation, factor models,
    or supervised dimension reduction) may be required depending on your goal.
"""

# %%
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
# Ensure output directory exists and write the figure using Path
scree_out = script_dir / "invest_scree.png"
scree_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(scree_out, dpi=150)
print(f"Saved {scree_out}")

# %%
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
biplot_out = script_dir / "invest_biplot.png"
biplot_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")
