# %% [markdown]
# # Invest PCA example
#
# This script loads a small CSV of asset returns and runs PCA on the
# correlation-like matrix (by standardizing returns first). It contains
# py-percent cells and detailed comments so you can run it interactively
# and read the explanation of the outputs inline.
#
# ## What to expect when you run this file:
# - Printed `eigenvalues`: the variances explained by each principal component.
# - Printed `explained_ratio`: proportion of total variance per component.
# - Printed `cumulative`: cumulative explained variance used to decide how many
#   components to retain.
#
# The file also saves two figures next to the script: a scree plot and a
# biplot for the first two PCs.

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
# ## Preprocessing and PCA
#
# We standardize the input columns so PCA operates on a correlation-like
# matrix (each column will have mean ~0 and unit variance). This is common
# when variables are on different scales or when you want components to be
# scale-invariant (e.g., asset returns).

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
# ### Quick interpretation of the printed results (concrete)
#
# The printed eigenvalues and explained ratios are the primary numeric
# summaries you should inspect before looking at the plots. For example, a
# typical run of this file produced:
#
# - Eigenvalues: `[3.895, 0.092, 0.011, 0.004]`
# - Explained ratio: `[0.973, 0.023, 0.003, 0.001]`
#
# Interpretation:
# - A single dominant component (PC1 ≈ 97.3%): this indicates nearly all
#   variance is captured by one linear combination of the input variables.
#   In finance, this commonly corresponds to a market factor that moves
#   most instruments together.
# - Remaining components explain minimal variance and will often reflect
#   idiosyncratic noise. Use them cautiously in downstream models.
#
# Practical actions:
# - Inspect `pca.components_[0]` to see which variables have the largest
#   loadings on PC1 (these are the instruments most aligned with the market
#   factor).
# - If you require interpretable factors despite a dominant PC, consider
#   rotating a small set of leading components or building a one-factor model
#   based on PC1.

# %% [markdown]
# ### Scree plot — quick interpretation
#
# The scree plot below shows eigenvalues (variance explained) by component
# index. Look for an "elbow" where the curve flattens. Components left of
# the elbow capture most structured variation. Complement the visual check
# with the printed cumulative explained-variance numbers above.

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

# %% [markdown]
# ### Biplot (first two components) — interpretation notes
#
# The biplot overlays observation scores (points) with variable loadings
# (arrows). Arrows pointing together indicate correlated variables; longer
# arrows indicate stronger contribution to the plotted PCs. Use the biplot to
# see which variables drive separation among observations.

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

# %% [markdown]
# ## Conclusion
#
# - Use the scree plot to choose a small set of components that explain most
#   variance; check the cumulative numbers for a quantitative threshold.
# - Use the biplot or the `pca.components_` matrix to map retained components
#   back to the original variables and form interpretations or factor
#   constructions.
# - Remember PCA is linear and sensitive to outliers — preprocess accordingly.

# %% [markdown]
# ## Detailed interpretation of example outputs
#
# The printed numbers and the figures above are the starting point for a
# practical interpretation. Below we walk through how to read the concrete
# quantities you just saw and what they imply for downstream analysis.
#
# - Example numbers observed when you run this file:
#   - Eigenvalues: e.g. `[3.895, 0.092, 0.011, 0.004]` (these are the variances
#     of the PCs when variables are standardized).
#   - Explained ratio: e.g. `[0.973, 0.023, 0.003, 0.001]` meaning PC1 explains
#     ~97.3% of the total variance.
#
# Interpretation and implications:
# - Highly dominant PC1 (97% explained)
#   - A single dimension captures almost all variation. For asset returns this
#     commonly corresponds to a market-wide factor. Actions:
#     - You can often summarize the dataset with PC1 alone for visualization
#       or for constructing simple one-factor models.
#     - Check `pca.components_[0]` to inspect which variables have large loadings
#       on PC1; these are the instruments that move most with the market factor.
# - Very small remaining eigenvalues
#   - PCs 2..n capture very little variance and are likely dominated by noise
#     or idiosyncratic effects. Actions:
#     - Avoid over-interpreting small PCs; instead, if you need interpretable
#       factors, consider rotating the first few components or using a
#       targeted factor model.
#
# Suggested follow-ups (practical next steps):
# - Print a compact table of loadings:
#  - Transform `pca.components_[:k]` into a DataFrame (index=PC, columns=vars)
#    and sort by absolute loading within each PC to identify driving variables.
# - If you need factor interpretability:
#  - Consider orthogonal or oblique rotations (varimax, promax) on the first
#    few components and inspect rotated loadings.
# - For forecasting or risk-modeling:
#  - Use PC1 as an aggregate factor in regressions; test whether adding PC2
#    materially improves predictive power despite its small variance share.
#
# Caveat:
# - When one PC dominates, downstream statistical estimators (e.g., covariance
#   inverses) can be unstable; use shrinkage or factor-based covariance
#   estimation when building portfolio models.
