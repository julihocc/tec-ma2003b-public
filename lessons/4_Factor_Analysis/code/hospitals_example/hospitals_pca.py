# %% [markdown]
# # Hospital Health Outcomes PCA Example
#
# This script loads a CSV of US hospital health outcome metrics and runs PCA on the
# standardized variables. It follows the same concise pattern used by
# `kuiper_example.py` and `invest_example.py`, focusing on healthcare quality
# indicators and performance measures.
#
# ## What to expect when you run this file:
# - Printed `eigenvalues`: the variances explained by each principal component.
# - Printed `explained_ratio`: proportion of total variance per component.
# - Printed `cumulative`: cumulative explained variance used to decide how many
#   components to retain for hospital quality assessment.
#
# The file also saves two figures: a scree plot and a biplot for the first two PCs.

# %%
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# %%
# Simple behaviour: expect hospitals.csv in the same folder as this script
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "hospitals.csv"
if not data_path.exists():
    print(
        f"Missing {data_path}. Run `fetch_hospitals.py` in the same folder to generate hospitals.csv"
    )
    sys.exit(2)

# Load data and prepare for analysis
df = pd.read_csv(data_path)
print(f"Loaded {len(df)} hospitals with {len(df.columns) - 1} health outcome metrics")

# Extract numeric columns (excluding Hospital ID)
X = df.iloc[:, 1:]  # Skip first column (Hospital names)
cols = list(X.columns)
print("Health outcome variables:", cols)

# %% [markdown]
# ## Preprocessing and PCA
#
# We standardize the input columns so PCA operates on a correlation-like
# matrix (each column will have mean ~0 and unit variance). This is essential
# when variables have different units and scales (e.g., percentages, ratios,
# minutes, days).

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
# of this hospital health outcomes example you might see:
#
# - Eigenvalues: `[4.125, 1.892, 0.876, 0.634, 0.298, 0.175]`
# - Explained ratio: `[0.516, 0.236, 0.110, 0.079, 0.037, 0.022]`
# - Cumulative: `[0.516, 0.752, 0.862, 0.941, 0.978, 1.000]`
#
# Interpretation:
# - **PC1** (~51.6%): Likely represents overall hospital quality. High-quality
#   hospitals tend to have lower mortality, readmissions, infections, and wait times,
#   but higher patient satisfaction and nurse ratios.
# - **PC2** (~23.6%): May capture a different dimension like efficiency vs. thoroughness
#   (shorter stays vs. comprehensive care).
# - First two components explain ~75% of variation, suggesting most hospital
#   quality differences can be captured in a 2D quality space.
#
# Practical follow-ups:
# - Examine `pca.components_` to see which metrics load most heavily on each PC
# - Use PC scores to identify high-performing and low-performing hospitals
# - Consider clustering hospitals based on their PC1-PC2 positions to find
#   distinct hospital quality profiles

# %% [markdown]
# ### Scree plot — quick interpretation (Hospital data)
#
# The scree plot below shows eigenvalues (variance explained) by component
# index. Look for an "elbow" where the curve flattens. Components left of
# the elbow capture most structured variation in hospital performance.

# %%
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Hospital Health Outcomes: Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
scree_out = script_dir / "hospitals_scree.png"
scree_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(scree_out, dpi=150)
print(f"Saved {scree_out}")

# %% [markdown]
# The scree plot helps decide how many components to examine. For hospital
# health outcomes, the first PC often represents overall quality (a "halo effect"),
# while subsequent PCs may capture trade-offs between different aspects of care
# (e.g., efficiency vs. thoroughness, clinical vs. service quality).

# %% [markdown]
# ### Biplot (PC1 vs PC2) — interpretation notes (Hospital data)
#
# The biplot overlays hospital scores (points) and variable loadings (arrows).
# Points are hospitals; arrows show how each health metric loads on the first
# two principal components. Hospitals in the upper-right quadrant likely have
# better overall quality if PC1 represents general performance.

# %%
plt.figure(figsize=(8, 6))
xs = Z[:, 0]
ys = Z[:, 1]

# Plot hospitals as points
plt.scatter(xs, ys, alpha=0.6, s=30, c="steelblue", edgecolors="navy", linewidth=0.5)

# Add some hospital labels for context (label a few extreme cases)
hospital_names = df["Hospital"].values
for i in [np.argmax(xs), np.argmin(xs), np.argmax(ys), np.argmin(ys)]:
    plt.annotate(
        hospital_names[i],
        (xs[i], ys[i]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8,
        alpha=0.8,
    )

# Plot variable loadings as arrows
scale_factor = max(xs.std(), ys.std()) * 3
for i, col in enumerate(cols):
    vx, vy = pca.components_[:2, i] * scale_factor
    plt.arrow(0, 0, vx, vy, color="red", head_width=0.05, alpha=0.8)
    plt.text(vx * 1.05, vy * 1.05, col, color="red", fontweight="bold", fontsize=9)

plt.xlabel(f"PC1 ({explained_ratio[0]:.1%} variance)")
plt.ylabel(f"PC2 ({explained_ratio[1]:.1%} variance)")
plt.title("Hospital Health Outcomes: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":", alpha=0.3)
plt.tight_layout()
biplot_out = script_dir / "hospitals_biplot.png"
biplot_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")

# %% [markdown]
# ### Component interpretation (Hospital-specific insights)
#
# Let's examine the loadings to understand what each component represents:

# %%
print("\nComponent loadings (first 3 components):")
loadings_df = pd.DataFrame(
    pca.components_[:3].T, columns=["PC1", "PC2", "PC3"], index=cols
)
print(loadings_df.round(3))

# Identify variables with strongest loadings on PC1
pc1_loadings = np.abs(pca.components_[0])
dominant_vars_pc1 = [cols[i] for i in np.argsort(pc1_loadings)[-3:]]
print(f"\nStrongest PC1 loadings: {dominant_vars_pc1}")

# %% [markdown]
# ### Hospital Quality Rankings
#
# Use PC1 scores to rank hospitals by overall quality (assuming PC1 captures
# general performance). Hospitals with higher PC1 scores likely have better
# outcomes across multiple metrics.

# %%
# Create hospital ranking based on PC1 scores
hospital_scores = pd.DataFrame(
    {"Hospital": df["Hospital"], "PC1_Score": Z[:, 0], "PC2_Score": Z[:, 1]}
)

# Sort by PC1 (higher is better if PC1 represents quality)
# Note: Check the sign of loadings to ensure correct interpretation
hospital_rankings = hospital_scores.sort_values("PC1_Score", ascending=False)

print("Top 5 hospitals by PC1 score:")
print(hospital_rankings.head())
print("\nBottom 5 hospitals by PC1 score:")
print(hospital_rankings.tail())

# %% [markdown]
# ## Conclusion
#
# - **PC1** likely represents overall hospital quality - use PC1 scores to rank
#   hospitals and identify high/low performers
# - **PC2** may capture specific trade-offs or care dimensions not explained by
#   general quality
# - The biplot shows which health metrics are most important for distinguishing
#   hospital performance
# - Hospitals clustering together in PC space have similar quality profiles
# - Use this analysis to identify best practices from high-performing hospitals
#   and target improvement areas for low-performing ones
#
# **Next steps for healthcare analysis:**
# - Validate PC interpretations against known hospital ratings
# - Investigate outlier hospitals for unique care models
# - Use factor rotation if interpretable factors are needed for reporting
# - Consider longitudinal analysis to track quality improvements over time
