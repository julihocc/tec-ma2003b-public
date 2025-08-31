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
# We create a controlled dataset with **two underlying latent factors** representing:
# - **Intelligence Factor**: Underlying cognitive ability affecting academic tests
# - **Personality Factor**: Underlying social/emotional traits affecting interpersonal skills
#
# Each observed variable is a linear combination of:
# - One latent factor (with different loading strengths: 0.85 strong, 0.80 moderate)
# - Measurement error (with different noise levels: 0.2 low, 0.25 medium)
# - Two additional variables contain only noise (no latent structure)
#
# **Expected outcome**: PCA should identify meaningful components that capture the
# latent factor structure, with clear separation from pure noise components.

# %%
rng = np.random.RandomState(random_seed)

# Generate two orthogonal latent factors
intelligence_factor = rng.normal(size=(n_samples, 1))  # Cognitive ability factor
personality_factor = rng.normal(size=(n_samples, 1))   # Social/emotional factor

# Define noise terms for measurement error
measurement_noise_low = rng.normal(size=(n_samples, 1))    # Low noise (σ = 0.2)  
measurement_noise_med = rng.normal(size=(n_samples, 1))    # Medium noise (σ = 0.25)
pure_noise_1 = rng.normal(size=(n_samples, 1))            # Pure noise variable 1
pure_noise_2 = rng.normal(size=(n_samples, 1))            # Pure noise variable 2

# Define factor loadings
strong_loading = 0.85  # Strong relationship to latent factor
moderate_loading = 0.80  # Moderate relationship to latent factor
low_noise_level = 0.2   # Low measurement error
med_noise_level = 0.25  # Medium measurement error
noise_variance_1 = 0.6  # Variance for first noise variable
noise_variance_2 = 0.5  # Variance for second noise variable

# Create observed variables with meaningful structure
math_test = strong_loading * intelligence_factor + low_noise_level * measurement_noise_low
verbal_test = moderate_loading * intelligence_factor + med_noise_level * measurement_noise_med
social_skills = strong_loading * personality_factor + low_noise_level * measurement_noise_low  
leadership = moderate_loading * personality_factor + med_noise_level * measurement_noise_med
random_var1 = noise_variance_1 * pure_noise_1  # Pure noise (no latent structure)
random_var2 = noise_variance_2 * pure_noise_2  # Pure noise (no latent structure)

# Combine into data matrix
X = np.hstack([math_test, verbal_test, social_skills, leadership, random_var1, random_var2])

# Create meaningful variable names for interpretation
variable_names = ["MathTest", "VerbalTest", "SocialSkills", "Leadership", "RandomVar1", "RandomVar2"]
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
# - Eigenvalues: `[2.331, 1.625, 1.088, 0.866, 0.077, 0.074]` (approximate)
# - Explained ratio: `[0.385, 0.268, 0.179, 0.143, 0.013, 0.012]` (approximate)
# - Cumulative: `[0.385, 0.653, 0.832, 0.975, 0.988, 1.000]` (approximate)
#
# **Interpretation**:
# - **PC1** (~38.5%): Likely captures a general ability factor that affects
#   both cognitive and social measures (common in psychological data)
# - **PC2** (~26.8%): May separate cognitive (MathTest, VerbalTest) from 
#   social (SocialSkills, Leadership) abilities
# - **PC3-PC4** (~32.2%): Additional structure and measurement error
# - **PC5-PC6** (~2.5%): Pure noise components (RandomVar1, RandomVar2)
# - First two components explain ~65% of variance, which is realistic
#   for psychological/educational assessment data
#
# **Validation check**: Since we know the true structure, PCA should show
# clear separation between factor-related and noise components in the scree plot.

# %% [markdown]
# ### Scree plot — quick interpretation (Synthetic data)
#
# The scree plot below shows eigenvalues by component index. With our known
# 2-factor structure, we expect to see higher eigenvalues for the first 
# several components that capture the factor structure, then a clear drop-off
# when we reach the pure noise components (PC5-PC6).

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
# The scree plot reveals the underlying structure we built into the data.
# Components 1-4 have eigenvalues above the noise floor, while
# components 5-6 represent pure noise with very low eigenvalues (~0.07).
# The clear drop after component 4 shows the transition from structure to noise.

# %% [markdown]
# ### Biplot (PC1 vs PC2) — interpretation notes (Synthetic data)
#
# The biplot overlays observation scores (points) and variable loadings (arrows).
# Since we know the true factor structure, we can validate whether PCA correctly
# identifies which variables belong to each factor.
#
# **Expected pattern**:
# - Academic tests (MathTest, VerbalTest) should show similar loading patterns
#   if they're driven by the same intelligence factor
# - Social measures (SocialSkills, Leadership) should show similar loading patterns  
#   if they're driven by the same personality factor
# - Noise variables (RandomVar1, RandomVar2) should have smaller, more random loadings

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
cognitive_loadings = np.abs(pca.components_[0, :2])  # MathTest, VerbalTest loadings on PC1
social_loadings = np.abs(pca.components_[1, 2:4])    # SocialSkills, Leadership loadings on PC2
random_max_loading = np.max(np.abs(pca.components_[:2, 4:6]))  # RandomVar1, RandomVar2 on PC1,PC2

print(f"Cognitive tests (Math,Verbal) average loading magnitude: {cognitive_loadings.mean():.3f}")
print(f"Social measures (Skills,Leadership) average loading magnitude: {social_loadings.mean():.3f}")
print(f"Random variables max loading on PC1/PC2: {random_max_loading:.3f}")

# Check if meaningful variables load more strongly than random noise
meaningful_strength = min(cognitive_loadings.mean(), social_loadings.mean())
if meaningful_strength > random_max_loading * 2:
    print("✓ SUCCESS: Meaningful variables show stronger loadings than random noise!")
    print(f"  Meaningful variable loading strength: {meaningful_strength:.3f}")
    print(f"  vs Random variable loading strength: {random_max_loading:.3f}")
else:
    print("⚠ NOTICE: Variable separation could be cleaner - this is typical for PCA")

# %% [markdown]
# ### Observation rankings by PC scores
#
# Since this is synthetic data representing student assessments, we can examine 
# which "students" score highest on each principal component to understand 
# what patterns PCA identified in abilities and performance.

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

print("Top 5 students by PC1 score (highest on general ability dimension):")
print(f"{'Student':<10} {'PC1':<10} {'PC2':<10}")
print("-" * 30)
for i in range(5):
    student_id, pc1, pc2 = pc1_rankings[i]
    print(f"Student_{int(student_id):<3} {pc1:<10.3f} {pc2:<10.3f}")

print("\nBottom 5 students by PC1 score (lowest on general ability dimension):")
for i in range(5):
    student_id, pc1, pc2 = pc1_rankings[-(i + 1)]
    print(f"Student_{int(student_id):<3} {pc1:<10.3f} {pc2:<10.3f}")

# %% [markdown]
# ## Conclusion
#
# This synthetic data example demonstrates key PCA concepts with known ground truth:
#
# - **Factor Recovery**: PCA captured the underlying factor structure,
#   though not as cleanly separated as factor analysis would (this is expected)
# - **Noise Separation**: Components 5-6 clearly capture pure noise with very
#   low eigenvalues, showing how PCA separates signal from noise
# - **Interpretation**: The biplot clearly shows which variables cluster together
#   (those driven by the same latent factor)
# - **Component Selection**: The scree plot shows the first 4 components capture
#   structure while 5-6 are pure noise, helping guide component retention
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
