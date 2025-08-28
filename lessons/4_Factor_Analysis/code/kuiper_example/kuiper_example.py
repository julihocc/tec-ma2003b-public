# %% [markdown]
# # Kuiper PCA example
#
# This script loads a small CSV of Kuiper Belt / trans-Neptunian object
# orbital parameters (generated from MPCORB in this repo) and runs PCA on the
# standardized variables. It follows the same concise pattern used by
# `invest_example.py`.

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
# ### Quick interpretation of the printed results (concrete)
#
# Inspect the numeric summaries above before the figures. For a typical run
# of this Kuiper example you might see:
#
# - Eigenvalues: `[1.846, 1.170, 0.900, 0.827, 0.309]`
# - Explained ratio: `[0.365, 0.232, 0.178, 0.164, 0.061]`
# - Cumulative: `[0.365, 0.597, 0.775, 0.939, 1.000]`
#
# Interpretation:
# - The variance is distributed across multiple components: PC1 explains
#   about 36.5% and the first three PCs explain ~77.5%. This suggests 2–3
#   components are useful for a compact description of orbital-parameter
#   variation.
# - Use `pca.components_` to see which variables drive each PC. For example,
#   a PC that loads on inclination and eccentricity indicates a dynamical
#   excitation mode, while a contrast between semi-major axis and H could
#   separate distant faint objects from nearer/brighter ones.
#
# Practical follow-ups:
# - After examining the scree plot, inspect loadings and consider clustering
#   on the first 2–3 PC scores to find groups of similar objects.
# - If interpretability is needed, apply a rotation (varimax) to the leading
#   components to obtain sparser, easier-to-label factors.

# %% [markdown]
# ### Scree plot — quick interpretation (Kuiper data)
#
# The scree plot below shows eigenvalues (variance explained) by component
# index. Look for an "elbow" where the curve flattens. Components left of
# the elbow capture most structured variation. Use the printed cumulative
# values to choose how many components to retain (e.g., 80% coverage).

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
# The scree plot helps decide how many components to examine. For orbital
# parameters, the first few PCs often summarize contrasts between eccentricity,
# inclination and semi-major axis. Inspect `pca.components_` to map PCs to
# these physical parameters.

# %% [markdown]
# ### Biplot (PC1 vs PC2) — interpretation notes (Kuiper data)
#
# The biplot overlays observation scores and variable loadings. Points are
# objects; arrows show how each orbital parameter loads on the first two
# principal components. Arrows that point in the same direction indicate
# positively correlated parameters; long arrows signal stronger influence.

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

# %% [markdown]
# ## Conclusion
#
# - Use the scree plot and cumulative numbers to choose how many components
#   to keep (aim for a coverage target appropriate to your goal).
# - Use the biplot and `pca.components_` to interpret which orbital
#   parameters drive the main modes of variation; consider rotation if you
#   need simpler factor-like interpretations.
# - PCA is linear and can be sensitive to outliers; for robust inference,
#   consider preprocessing and inspecting unusual observations.
