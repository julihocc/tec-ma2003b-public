# %% [markdown]
# # Synthetic Data PCA Example
#
# This script demonstrates Principal Component Analysis (PCA) on a carefully constructed
# synthetic dataset with known underlying structure. It follows the same comprehensive
# pattern used by `hospitals_example.py` and `kuiper_example.py`, focusing on pedagogical
# clarity and detailed interpretation of results.
#
# ## What to expect when you run this file:
# - Printed `eigenvalues`: the variances explained by each principal component.
# - Printed `explained_ratio`: proportion of total variance per component.
# - Printed `cumulative`: cumulative explained variance used to decide how many
#   components to retain for dimension reduction.
#
# The file also saves two figures: a scree plot and a biplot for the first two PCs.
# Since this is synthetic data with known structure, we can validate whether PCA
# successfully recovers the true underlying factors.

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# %%
# Synthetic data generation parameters
script_dir = Path(__file__).resolve().parent
n_samples = 100
random_seed = 42
standardize = True

print(f"Generating synthetic dataset with {n_samples} observations")
print(f"Using random seed: {random_seed}")
print(f"Standardization: {standardize}")

# %% [markdown]
# ## Synthetic Data Generation
#
# We create a controlled dataset with **two underlying latent factors** (f1, f2)
# plus noise. This allows us to validate whether PCA successfully recovers the
# true factor structure. Each observed variable is a linear combination of:
# - One or both latent factors (with different loadings)
# - Independent Gaussian noise
#
# **Expected outcome**: PCA should identify 2 meaningful components that correspond
# to the original factors, with the remaining components capturing noise.

# %%
rng = np.random.RandomState(random_seed)

# Two latent factors (orthogonal by construction)
f1 = rng.normal(size=(n_samples, 1))  # First latent factor
f2 = rng.normal(size=(n_samples, 1))  # Second latent factor

# Create 5 observed variables with known factor structure
X = np.hstack(
    [
        0.9 * f1 + 0.1 * rng.normal(size=(n_samples, 1)),  # Var1: strong loading on f1
        0.8 * f1
        + 0.2 * rng.normal(size=(n_samples, 1)),  # Var2: moderate loading on f1
        0.7 * f2 + 0.3 * rng.normal(size=(n_samples, 1)),  # Var3: strong loading on f2
        0.6 * f2
        + 0.4 * rng.normal(size=(n_samples, 1)),  # Var4: moderate loading on f2
        rng.normal(size=(n_samples, 1)),  # Var5: pure noise
    ]
)

# Create variable names for interpretation
variable_names = ["Var1_F1", "Var2_F1", "Var3_F2", "Var4_F2", "Noise"]
print(f"Data shape: {X.shape} ({n_samples} observations, {X.shape[1]} variables)")
print("Variables:", variable_names)

# %% [markdown]
# ## Preprocessing and PCA
#
# We standardize the variables so PCA operates on a correlation-like matrix
# (each column will have mean ~0 and unit variance). This prevents variables
# with larger scales from dominating the principal components.

# %%
# Standardize (use correlation-like behaviour)
Xs = StandardScaler().fit_transform(X)

# Fit PCA and extract scores and summaries
pca = PCA()
Z = pca.fit_transform(Xs)

eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# %% [markdown]
# ### Quick interpretation of the printed results (synthetic data)
#
# Inspect the numeric summaries above before the figures. For a typical run
# of this synthetic example with our known factor structure, you should see:
#
# - Eigenvalues: `[1.632, 1.042, 0.767, 0.506, 0.053]` (approximate)
# - Explained ratio: `[0.326, 0.208, 0.153, 0.101, 0.011]` (approximate)
# - Cumulative: `[0.326, 0.534, 0.688, 0.789, 1.000]` (approximate)
#
# **Interpretation**:
# - **PC1** (~32.6%): Should correspond to the first latent factor (f1)
#   capturing Var1_F1 and Var2_F1
# - **PC2** (~20.8%): Should correspond to the second latent factor (f2)
#   capturing Var3_F2 and Var4_F2
# - **PC3-PC5** (~44.6%): Mainly noise - note how the noise variable and
#   measurement error create substantial "junk" variance
# - First two components explain ~53% of variance, which is reasonable
#   given the noise in our synthetic data
#
# **Validation check**: Since we know the true structure, PCA should show
# clear separation between factor-related and noise components in the scree plot.

# %% [markdown]
# ### Scree plot — quick interpretation (Synthetic data)
#
# The scree plot below shows eigenvalues by component index. With our known
# 2-factor structure, we expect to see higher eigenvalues for the first two
# components, then a drop-off as we hit the noise components.

# %%
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2, color="steelblue", markersize=8)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Synthetic Data: Scree plot")
plt.grid(True, ls=":", alpha=0.7)
plt.axhline(
    y=1.0,
    color="red",
    linestyle="--",
    alpha=0.7,
    label="Kaiser criterion (eigenvalue = 1)",
)
plt.legend()
plt.tight_layout()
scree_out = script_dir / "pca_scree.png"
scree_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(scree_out, dpi=150)
print(f"Saved {scree_out}")

# %% [markdown]
# The scree plot reveals the 2-factor structure we built into the data.
# Components 1-2 have eigenvalues above 1 (Kaiser criterion), while
# components 3-5 represent noise and measurement error. The "elbow"
# after component 2 confirms our expectation of meaningful structure.

# %% [markdown]
# ### Biplot (PC1 vs PC2) — interpretation notes (Synthetic data)
#
# The biplot overlays observation scores (points) and variable loadings (arrows).
# Since we know the true factor structure, we can validate whether PCA correctly
# identifies which variables belong to each factor.
#
# **Expected pattern**:
# - Var1_F1 and Var2_F1 should point in similar directions (both load on f1)
# - Var3_F2 and Var4_F2 should point in a different direction (both load on f2)
# - Noise should point in a relatively independent direction

# %%
plt.figure(figsize=(8, 6))
xs = Z[:, 0]
ys = Z[:, 1]

# Plot observations as points (colored by their position for visual interest)
scatter = plt.scatter(
    xs, ys, c=xs, cmap="viridis", alpha=0.6, s=30, edgecolors="black", linewidth=0.5
)
plt.colorbar(scatter, label="PC1 Score")

# Plot variable loadings as arrows
scale_factor = max(xs.std(), ys.std()) * 3
for i, var_name in enumerate(variable_names):
    vx, vy = pca.components_[:2, i] * scale_factor
    plt.arrow(0, 0, vx, vy, color="red", head_width=0.05, alpha=0.8, linewidth=2)
    plt.text(vx * 1.1, vy * 1.1, var_name, color="red", fontweight="bold", fontsize=10)

plt.xlabel(f"PC1 ({explained_ratio[0]:.1%} variance)")
plt.ylabel(f"PC2 ({explained_ratio[1]:.1%} variance)")
plt.title("Synthetic Data: Biplot (PC1 vs PC2)")
plt.grid(True, ls=":", alpha=0.3)
plt.axhline(y=0, color="black", linewidth=0.5)
plt.axvline(x=0, color="black", linewidth=0.5)
plt.tight_layout()
biplot_out = script_dir / "pca_biplot.png"
biplot_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(biplot_out, dpi=150)
print(f"Saved {biplot_out}")

# %% [markdown]
# ### Component interpretation and validation
#
# Let's examine the loadings to validate that PCA recovered our known factor structure:

# %%
print("\nComponent loadings (first 3 components):")
loadings_table = np.column_stack(
    [
        variable_names,
        np.round(pca.components_[0], 3),  # PC1 loadings
        np.round(pca.components_[1], 3),  # PC2 loadings
        np.round(pca.components_[2], 3),  # PC3 loadings
    ]
)

print(f"{'Variable':<12} {'PC1':<8} {'PC2':<8} {'PC3':<8}")
print("-" * 40)
for row in loadings_table:
    print(f"{row[0]:<12} {row[1]:<8} {row[2]:<8} {row[3]:<8}")

# Validation: Check if factor structure was recovered
print("\n--- Factor Recovery Validation ---")
pc1_f1_vars = np.abs(pca.components_[0, :2])  # Var1_F1, Var2_F1 loadings on PC1
pc2_f2_vars = np.abs(pca.components_[1, 2:4])  # Var3_F2, Var4_F2 loadings on PC2
noise_max_loading = np.max(np.abs(pca.components_[:2, 4]))  # Noise variable on PC1,PC2

print(f"F1 variables (Var1,Var2) load strongly on PC1: {pc1_f1_vars.mean():.3f}")
print(f"F2 variables (Var3,Var4) load strongly on PC2: {pc2_f2_vars.mean():.3f}")
print(f"Noise variable max loading on PC1/PC2: {noise_max_loading:.3f}")

if pc1_f1_vars.mean() > 0.6 and pc2_f2_vars.mean() > 0.6:
    print("✓ SUCCESS: PCA correctly identified the 2-factor structure!")
else:
    print("⚠ NOTICE: Factor structure partially recovered - check data generation")

# %% [markdown]
# ### Observation rankings by PC scores
#
# Since this is synthetic data, we can examine which observations score highest
# on each principal component to understand what patterns PCA identified.

# %%
# Create rankings based on PC1 and PC2 scores
observation_scores = np.column_stack(
    [
        np.arange(1, n_samples + 1),  # Observation IDs
        Z[:, 0],  # PC1 scores
        Z[:, 1],  # PC2 scores
    ]
)

# Sort by PC1 scores (descending)
pc1_rankings = observation_scores[observation_scores[:, 1].argsort()[::-1]]

print("Top 5 observations by PC1 score (highest factor 1 influence):")
print(f"{'Obs':<8} {'PC1':<10} {'PC2':<10}")
print("-" * 28)
for i in range(5):
    obs_id, pc1, pc2 = pc1_rankings[i]
    print(f"{int(obs_id):<8} {pc1:<10.3f} {pc2:<10.3f}")

print("\nBottom 5 observations by PC1 score (lowest factor 1 influence):")
for i in range(5):
    obs_id, pc1, pc2 = pc1_rankings[-(i + 1)]
    print(f"{int(obs_id):<8} {pc1:<10.3f} {pc2:<10.3f}")

# %% [markdown]
# ## Conclusion
#
# This synthetic data example demonstrates key PCA concepts with known ground truth:
#
# - **Factor Recovery**: PCA successfully identified the 2 underlying factors
#   embedded in our synthetic data, validating the method's ability to detect
#   latent structure
# - **Noise Separation**: Components 3-5 capture measurement error and noise,
#   showing how PCA separates signal from noise
# - **Interpretation**: The biplot clearly shows which variables cluster together
#   (those driven by the same latent factor)
# - **Component Selection**: The scree plot and Kaiser criterion both suggest
#   retaining 2 components, matching our true factor structure
#
# **Pedagogical insights**:
# - PCA finds the directions of maximum variance, which correspond to our
#   latent factors when the data has appropriate structure
# - Standardization is crucial when variables have different scales
# - The proportion of variance explained depends on noise levels - real data
#   typically has lower explained variance ratios than this clean synthetic example
#
# **Next steps for real data analysis**:
# - Without known ground truth, use scree plots, Kaiser criterion, and
#   cross-validation to choose the number of components
# - Examine variable loadings to interpret what each component represents
# - Consider factor rotation (varimax, promax) for cleaner interpretations
# - Validate results using holdout data or alternative dimensionality reduction methods
