# %% [markdown]
# # Factor Analysis vs PCA Comparison - Educational Assessment
#
# This script demonstrates the key differences between Factor Analysis (FA) and
# Principal Component Analysis (PCA) using the same synthetic educational dataset.
# This direct comparison highlights when and why to choose FA over PCA.
#
# ## Key differences explored:
# - **PCA**: Explains maximum variance, includes all variance (common + unique)
# - **Factor Analysis**: Models only common variance, estimates communalities
# - **Interpretation**: FA focuses on latent constructs, PCA on data reduction
# - **Factor Loadings**: FA loadings represent relationships to latent factors
#
# ## What to expect when you run this file:
# - Comparative factor extraction using Principal Axis Factoring
# - Communality estimates and uniquenesses interpretation
# - Factor rotation (Varimax) for improved interpretability
# - Direct comparison with PCA results from `pca_example.py`

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# %%
# Use same data generation as PCA example for direct comparison
script_dir = Path(__file__).resolve().parent
n_samples = 100
random_seed = 42
standardize = True

print(f"Factor Analysis on synthetic dataset with {n_samples} observations")
print(f"Using random seed: {random_seed}")
print(f"Standardization: {standardize}")

# %% [markdown]
# ## Generate Same Synthetic Data as PCA Example
#
# We use identical data generation to `pca_example.py` to enable direct comparison.
# This controlled dataset has **two underlying latent factors**:
# - **Intelligence Factor**: Affects MathTest, VerbalTest
# - **Personality Factor**: Affects SocialSkills, Leadership
# - **Noise Variables**: RandomVar1, RandomVar2 (no latent structure)
#
# **Key for FA vs PCA comparison**: FA should better identify the true latent
# factor structure since it models common variance specifically.

# %%
# Generate identical synthetic data (same as pca_example.py)
rng = np.random.RandomState(random_seed)

# Generate two orthogonal latent factors
intelligence_factor = rng.normal(size=(n_samples, 1))  # Cognitive ability factor
personality_factor = rng.normal(size=(n_samples, 1))  # Social/emotional factor

# Define noise terms for measurement error
measurement_noise_low = rng.normal(size=(n_samples, 1))  # Low noise (σ = 0.2)
measurement_noise_med = rng.normal(size=(n_samples, 1))  # Medium noise (σ = 0.25)
pure_noise_1 = rng.normal(size=(n_samples, 1))  # Pure noise variable 1
pure_noise_2 = rng.normal(size=(n_samples, 1))  # Pure noise variable 2

# Define factor loadings (same as PCA example)
strong_loading = 0.85  # Strong relationship to latent factor
moderate_loading = 0.80  # Moderate relationship to latent factor
low_noise_level = 0.2  # Low measurement error
med_noise_level = 0.25  # Medium measurement error
noise_variance_1 = 0.6  # Variance for first noise variable
noise_variance_2 = 0.5  # Variance for second noise variable

# Create observed variables with meaningful structure
math_test = (
    strong_loading * intelligence_factor + low_noise_level * measurement_noise_low
)
verbal_test = (
    moderate_loading * intelligence_factor + med_noise_level * measurement_noise_med
)
social_skills = (
    strong_loading * personality_factor + low_noise_level * measurement_noise_low
)
leadership = (
    moderate_loading * personality_factor + med_noise_level * measurement_noise_med
)
random_var1 = noise_variance_1 * pure_noise_1  # Pure noise (no latent structure)
random_var2 = noise_variance_2 * pure_noise_2  # Pure noise (no latent structure)

# Combine into data matrix
X = np.hstack(
    [math_test, verbal_test, social_skills, leadership, random_var1, random_var2]
)

# Create meaningful variable names for interpretation
variable_names = [
    "MathTest",
    "VerbalTest",
    "SocialSkills",
    "Leadership",
    "RandomVar1",
    "RandomVar2",
]
print(f"Data shape: {X.shape} ({n_samples} observations, {X.shape[1]} variables)")
print("Variables:", variable_names)

# %% [markdown]
# ## Preprocessing and Factor Analysis Assumptions
#
# Before running Factor Analysis, we check key assumptions:
# - **Bartlett's Test of Sphericity**: Tests if correlation matrix ≠ identity
# - **KMO (Kaiser-Meyer-Olkin)**: Measures sampling adequacy (>.6 acceptable)
# - **Correlation adequacy**: Variables should be meaningfully correlated

# %%
# Standardize data (same preprocessing as PCA)
Xs = StandardScaler().fit_transform(X)

# Check Factor Analysis assumptions
chi_square_value, p_value = calculate_bartlett_sphericity(Xs)
kmo_all, kmo_model = calculate_kmo(Xs)

print("--- Factor Analysis Assumptions ---")
print("Bartlett's Test of Sphericity:")
print(f"  Chi-square: {chi_square_value:.3f}")
print(f"  p-value: {p_value:.6f}")
print(
    f"  Interpretation: {'✓ Reject null - suitable for FA' if p_value < 0.05 else '✗ Fail to reject - may not be suitable'}"
)
print("\nKMO Test:")
print(f"  Overall MSA: {kmo_model:.3f}")
print(
    f"  Interpretation: {'✓ Excellent' if kmo_model > 0.9 else '✓ Good' if kmo_model > 0.8 else '✓ Acceptable' if kmo_model > 0.6 else '✗ Unacceptable'} sampling adequacy"
)

# %%
# Show individual variable KMO values
print("Individual Variable MSA values:")
print(f"{'Variable':<12} {'MSA':<8}")
print("-" * 20)
for i, var_name in enumerate(variable_names):
    print(f"{var_name:<12} {kmo_all[i]:<8.3f}")

# %% [markdown]
# ## Factor Extraction: Principal Axis Factoring
#
# We use Principal Axis Factoring (PAF), a common factor analysis method that:
# - Estimates communalities iteratively
# - Extracts factors from the correlation matrix with communalities on diagonal
# - Focuses on shared variance among variables
#
# We'll compare 2-factor (theory-driven) and data-driven solutions.

# %%
# Fit Factor Analysis with 2 factors (theory-driven: Intelligence + Personality)
n_factors_theory = 2
fa_theory = FactorAnalyzer(
    n_factors=n_factors_theory, rotation=None, method="principal"
)
fa_theory.fit(Xs)

# Check if fit was successful
if fa_theory.loadings_ is None:
    raise ValueError("Factor analysis fit failed - no loadings produced")

print(f"--- Factor Analysis: {n_factors_theory} Factors (Theory-Driven) ---")
print(f"Eigenvalues: {np.round(fa_theory.get_eigenvalues()[0][:n_factors_theory], 3)}")

# Extract communalities and uniquenesses
communalities = fa_theory.get_communalities()
uniquenesses = 1 - communalities

print("\nCommunalities and Uniquenesses:")
print(f"{'Variable':<12} {'h²':<8} {'u²':<8}")
print("-" * 28)
for i, var_name in enumerate(variable_names):
    print(f"{var_name:<12} {communalities[i]:<8.3f} {uniquenesses[i]:<8.3f}")

# Calculate variance explained by factors
factor_variance = np.sum(communalities)
total_variance = len(variable_names)  # For standardized data
variance_explained = factor_variance / total_variance

print("\nVariance Analysis:")
print(f"Total variance (standardized): {total_variance:.1f}")
print(f"Common variance (sum of h²): {factor_variance:.3f}")
print(f"Proportion explained by factors: {variance_explained:.1%}")

# %% [markdown]
# ### Interpretation: Communalities
#
# **Communalities (h²)** represent the proportion of each variable's variance
# explained by the common factors. Compare these values:
# - **MathTest & VerbalTest**: Should have high h² (driven by Intelligence factor)
# - **SocialSkills & Leadership**: Should have high h² (driven by Personality factor)
# - **RandomVar1 & RandomVar2**: Should have low h² (mostly unique variance)

# %% [markdown]
# ## Factor Rotation: Varimax for Simple Structure
#
# Unrotated factors may be difficult to interpret. Varimax rotation:
# - Maximizes variance of squared loadings within each factor
# - Seeks "simple structure" where variables load highly on one factor
# - Maintains orthogonality (factors remain uncorrelated)

# %%
# Apply Varimax rotation for better interpretability
fa_rotated = FactorAnalyzer(
    n_factors=n_factors_theory, rotation="varimax", method="principal"
)
fa_rotated.fit(Xs)

loadings_unrotated = fa_theory.loadings_
loadings_rotated = fa_rotated.loadings_

# Add safety check: If rotated loadings failed, fall back to unrotated
if loadings_rotated is None:
    print("Warning: Varimax rotation failed or produced no loadings. Using unrotated loadings for comparison.")
    loadings_rotated = loadings_unrotated

assert loadings_rotated is not None

print("--- Factor Loadings Comparison: Unrotated vs Varimax ---")
print(
    f"{'Variable':<12} {'Unrot-F1':<10} {'Unrot-F2':<10} {'Vmax-F1':<10} {'Vmax-F2':<10}"
)
print("-" * 62)
for i, var_name in enumerate(variable_names):
    print(
        f"{var_name:<12} {loadings_unrotated[i, 0]:<10.3f} {loadings_unrotated[i, 1]:<10.3f} {loadings_rotated[i, 0]:<10.3f} {loadings_rotated[i, 1]:<10.3f}"
    )

# %% [markdown]
# ### Factor Loading Interpretation
#
# **Expected pattern after Varimax rotation**:
# - **Factor 1**: High loadings for MathTest, VerbalTest (Intelligence factor)
# - **Factor 2**: High loadings for SocialSkills, Leadership (Personality factor)
# - **Random variables**: Low loadings on both factors
# - **Simple structure**: Each variable loads primarily on one factor

# %%
# Visualize factor loadings with heatmap
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Unrotated loadings heatmap
sns.heatmap(
    loadings_unrotated.T,
    annot=True,
    fmt=".2f",
    xticklabels=variable_names,
    yticklabels=[f"Factor {i + 1}" for i in range(n_factors_theory)],
    cmap="RdBu_r",
    center=0,
    ax=ax1,
    cbar_kws={"shrink": 0.8},
)
ax1.set_title("Unrotated Factor Loadings")

# Rotated loadings heatmap
sns.heatmap(
    loadings_rotated.T,
    annot=True,
    fmt=".2f",
    xticklabels=variable_names,
    yticklabels=[f"Factor {i + 1}" for i in range(n_factors_theory)],
    cmap="RdBu_r",
    center=0,
    ax=ax2,
    cbar_kws={"shrink": 0.8},
)
ax2.set_title("Varimax Rotated Factor Loadings")

plt.tight_layout()
loadings_out = script_dir / "fa_loadings.png"
plt.savefig(loadings_out, dpi=150, bbox_inches="tight")
print(f"Saved {loadings_out}")
plt.show()

# %% [markdown]
# ## Factor Analysis vs PCA: Direct Comparison
#
# Now let's directly compare Factor Analysis results with PCA on the same data.
# This comparison highlights the fundamental philosophical differences.

# %%
# Run PCA on same data for direct comparison
pca = PCA()
pca_scores = pca.fit_transform(Xs)
pca_loadings = pca.components_.T * np.sqrt(pca.explained_variance_)  # Scale loadings

# Run FA and get factor scores
fa_scores = fa_rotated.transform(Xs)

print("--- Factor Analysis vs PCA: Method Comparison ---")
print("\n1. VARIANCE PERSPECTIVE:")
print(
    f"PCA - Total variance explained by first 2 components: {pca.explained_variance_ratio_[:2].sum():.1%}"
)
print(f"FA  - Common variance explained by 2 factors: {variance_explained:.1%}")
print("     Difference: PCA includes unique variance, FA models only shared variance")

print("\n2. LOADING COMPARISON (first 2 dimensions):")
print(f"{'Variable':<12} {'PCA-PC1':<10} {'PCA-PC2':<10} {'FA-F1':<10} {'FA-F2':<10}")
print("-" * 52)
for i, var_name in enumerate(variable_names):
    print(
        f"{var_name:<12} {pca_loadings[i, 0]:<10.3f} {pca_loadings[i, 1]:<10.3f} {loadings_rotated[i, 0]:<10.3f} {loadings_rotated[i, 1]:<10.3f}"
    )

# %% [markdown]
# ## Scree Plot: FA vs PCA Comparison
#
# Scree plots for FA and PCA show different eigenvalue patterns:
# - **PCA**: All eigenvalues from variance decomposition
# - **FA**: Only eigenvalues from common factor space

# %%
# Calculate eigenvalues for comparison
pca_eigenvalues = pca.explained_variance_
fa_eigenvalues = fa_theory.get_eigenvalues()[0]

plt.figure(figsize=(10, 6))

# PCA scree plot
plt.subplot(1, 2, 1)
components = np.arange(1, len(pca_eigenvalues) + 1)
plt.plot(
    components,
    pca_eigenvalues,
    "o-",
    lw=2,
    color="steelblue",
    markersize=8,
    label="PCA",
)
plt.axhline(y=1.0, color="red", linestyle="--", alpha=0.7, label="Kaiser criterion")
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("PCA Scree Plot")
plt.xticks(components)
plt.grid(True, ls=":", alpha=0.7)
plt.legend()

# FA scree plot
plt.subplot(1, 2, 2)
plt.plot(
    components,
    fa_eigenvalues,
    "o-",
    lw=2,
    color="darkgreen",
    markersize=8,
    label="Factor Analysis",
)
plt.axhline(y=1.0, color="red", linestyle="--", alpha=0.7, label="Kaiser criterion")
plt.xlabel("Factor")
plt.ylabel("Eigenvalue")
plt.title("Factor Analysis Scree Plot")
plt.xticks(components)
plt.grid(True, ls=":", alpha=0.7)
plt.legend()

plt.tight_layout()
scree_out = script_dir / "fa_scree.png"
plt.savefig(scree_out, dpi=150, bbox_inches="tight")
print(f"Saved {scree_out}")
plt.show()

# %% [markdown]
# ### Scree Plot Interpretation
#
# **Key differences between FA and PCA eigenvalues**:
# - FA eigenvalues are typically lower (common variance only)
# - Kaiser criterion may suggest different number of factors vs components
# - FA focuses on factor retention for latent constructs, not variance maximization

# %% [markdown]
# ## Factor Analysis Validation and Interpretation
#
# Let's validate how well FA recovered our known factor structure:

# %%
print("--- Factor Structure Recovery Validation ---")

# Identify which variables load on which factors (>.4 threshold common)
loading_threshold = 0.4

print(f"Factor loadings above {loading_threshold} threshold:")
for factor_idx in range(n_factors_theory):
    factor_name = f"Factor {factor_idx + 1}"
    high_loading_vars = []

    for var_idx, var_name in enumerate(variable_names):
        loading = abs(loadings_rotated[var_idx, factor_idx])
        if loading > loading_threshold:
            high_loading_vars.append(f"{var_name}({loading:.2f})")

    print(
        f"{factor_name}: {', '.join(high_loading_vars) if high_loading_vars else 'None'}"
    )

# Compare communalities: meaningful vs noise variables
meaningful_vars = ["MathTest", "VerbalTest", "SocialSkills", "Leadership"]
noise_vars = ["RandomVar1", "RandomVar2"]

meaningful_communalities = [
    communalities[i] for i, var in enumerate(variable_names) if var in meaningful_vars
]
noise_communalities = [
    communalities[i] for i, var in enumerate(variable_names) if var in noise_vars
]

print("\nCommunality Analysis:")
print(f"Meaningful variables average h²: {np.mean(meaningful_communalities):.3f}")
print(f"Noise variables average h²: {np.mean(noise_communalities):.3f}")

# Success metric: meaningful variables should have higher communalities
if np.mean(meaningful_communalities) > np.mean(noise_communalities) * 1.5:
    print(
        "✓ SUCCESS: Factor Analysis successfully separated meaningful variables from noise!"
    )
    print("  Meaningful variables show higher communalities than noise variables")
else:
    print(
        "⚠ NOTICE: Factor structure could be cleaner - consider more factors or different rotation"
    )

# %% [markdown]
# ## Conclusion: When to Use Factor Analysis vs PCA
#
# This direct comparison reveals key decision criteria:
#
# ### **Choose Factor Analysis when**:
# - You have theoretical hypotheses about latent constructs
# - You want to model relationships between observed variables and latent factors
# - Common variance is more important than total variance
# - You need to estimate measurement error (uniquenesses)
# - Interpreting latent psychological, social, or economic constructs
#
# ### **Choose PCA when**:
# - Primary goal is data reduction/dimensionality reduction
# - You want to maximize explained variance
# - No specific theoretical model for latent structure
# - Computational efficiency is important
# - Exploratory data analysis for unknown structure
#
# ### **Key Insights from this example**:
# - FA better identified the true 2-factor structure in our synthetic data
# - Communalities revealed which variables share common variance
# - Varimax rotation improved interpretability significantly
# - FA loadings are more theoretically meaningful for latent constructs
#
# **Next steps**: Apply these concepts to real-world datasets where the latent
# structure is unknown, using factor retention criteria and rotation methods
# to discover meaningful factor structures.
