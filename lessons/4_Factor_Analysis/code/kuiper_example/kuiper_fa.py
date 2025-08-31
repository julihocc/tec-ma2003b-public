# %% [markdown]
# # Kuiper Factor Analysis example
#
# This script loads the Kuiper Belt / trans-Neptunian object orbital parameters
# and applies Factor Analysis instead of PCA to identify latent dynamical factors
# that govern orbital behavior. This complements the PCA analysis in `kuiper_pca.py`
# by focusing on common variance and latent construct interpretation.
#
# **Data Dictionary**: See `KUIPER_BELT_DATA_DICTIONARY.md` in this folder for detailed
# explanations of each orbital parameter and their physical significance.
#
# ## Key differences from PCA approach:
# - **Factor Analysis**: Models only common variance, estimates communalities
# - **Astronomical interpretation**: Focuses on dynamical processes and resonances
# - **Factor loadings**: Represent relationships to latent dynamical factors
# - **Rotation**: Varimax rotation for clearer astronomical interpretation

# %%
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import seaborn as sns
import sys

# %%
# Simple behaviour: expect kuiper.csv in the same folder as this script
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "kuiper.csv"
if not data_path.exists():
    print(
        f"Missing {data_path}. Run `fetch_kuiper.py` in the same folder to generate kuiper.csv"
    )
    sys.exit(2)

X = pd.read_csv(data_path)
# If the CSV has a leading index-like column (common in some exports), drop it
cols = list(X.columns)
if cols and cols[0].lower() in ("rownames", "index"):
    X = X.iloc[:, 1:]
    cols = list(X.columns)

print(f"Kuiper Belt Factor Analysis on {X.shape[0]} objects with {X.shape[1]} orbital parameters")
print("Variables:", cols)

# %% [markdown]
# ## Factor Analysis Assumptions for Orbital Data
#
# Before applying Factor Analysis, we check key assumptions for astronomical data:
# - **Bartlett's Test**: Tests if correlation matrix differs from identity
# - **KMO Test**: Measures sampling adequacy for orbital parameters
# - **Variable correlations**: Orbital elements should show meaningful relationships

# %%
# Standardize orbital parameters (different units: AU, degrees, etc.)
Xs = StandardScaler().fit_transform(X.values)

# Check Factor Analysis assumptions
chi_square_value, p_value = calculate_bartlett_sphericity(Xs)
kmo_all, kmo_model = calculate_kmo(Xs)

print("--- Factor Analysis Assumptions for Orbital Data ---")
print(f"Bartlett's Test of Sphericity:")
print(f"  Chi-square: {chi_square_value:.3f}")
print(f"  p-value: {p_value:.6f}")
print(f"  Interpretation: {'✓ Suitable for FA' if p_value < 0.05 else '✗ May not be suitable'}")
print(f"\nKMO Test:")
print(f"  Overall MSA: {kmo_model:.3f}")
print(f"  Interpretation: {'✓ Excellent' if kmo_model > 0.9 else '✓ Good' if kmo_model > 0.8 else '✓ Acceptable' if kmo_model > 0.6 else '✗ Unacceptable'} for orbital data")

# Show individual orbital parameter KMO values
print(f"\nIndividual Orbital Parameter MSA:")
print(f"{'Parameter':<15} {'MSA':<8} {'Interpretation'}")
print("-" * 40)
for i, param_name in enumerate(cols):
    msa = kmo_all[i]
    interp = "✓ Good" if msa > 0.7 else "△ Acceptable" if msa > 0.5 else "✗ Poor"
    print(f"{param_name:<15} {msa:<8.3f} {interp}")

# %% [markdown]
# ## Factor Extraction: Principal Axis Factoring
#
# We apply Principal Axis Factoring to identify latent dynamical factors.
# In orbital dynamics, common factors might represent:
# - **Excitation mechanisms**: Processes that increase eccentricity and inclination
# - **Size/distance relationships**: Correlations between orbital distance and object size
# - **Resonance effects**: Dynamical resonances affecting multiple orbital elements

# %%
# Determine optimal number of factors using eigenvalue criterion
fa_test = FactorAnalyzer(n_factors=len(cols), method='principal')
fa_test.fit(Xs)
eigenvalues_fa = fa_test.get_eigenvalues()[0]

# Kaiser criterion: factors with eigenvalue > 1.0
n_factors_kaiser = int(np.sum(eigenvalues_fa > 1.0))
print(f"--- Factor Retention Analysis ---")
print(f"Eigenvalues: {np.round(eigenvalues_fa, 3)}")
print(f"Kaiser criterion (eigenvalue > 1.0): {n_factors_kaiser} factors")

# Use Kaiser criterion for factor extraction
n_factors = max(n_factors_kaiser, 2)  # At least 2 factors for interpretation
fa = FactorAnalyzer(n_factors=n_factors, method='principal')
fa.fit(Xs)

print(f"\nExtracting {n_factors} factors using Principal Axis Factoring")

# Extract communalities and uniquenesses
communalities = fa.get_communalities()
uniquenesses = 1 - communalities

print(f"\nCommunalities (h²) and Uniquenesses (u²):")
print(f"{'Parameter':<15} {'h²':<8} {'u²':<8} {'Interpretation'}")
print("-" * 50)
for i, param_name in enumerate(cols):
    h2 = communalities[i]
    u2 = uniquenesses[i]
    interp = "High common" if h2 > 0.6 else "Moderate" if h2 > 0.4 else "Low common"
    print(f"{param_name:<15} {h2:<8.3f} {u2:<8.3f} {interp}")

# Calculate variance explained by factors
factor_variance = np.sum(communalities)
total_variance = len(cols)  # For standardized data
variance_explained = factor_variance / total_variance

print(f"\nVariance Analysis for Orbital Data:")
print(f"Total variance (standardized): {total_variance:.1f}")
print(f"Common variance (sum of h²): {factor_variance:.3f}")
print(f"Proportion explained by factors: {variance_explained:.1%}")

# %% [markdown]
# ### Astronomical Interpretation: Communalities
#
# **Communalities (h²)** show how much of each orbital parameter's variance
# is explained by common dynamical factors:
# - **High h²**: Parameter strongly influenced by common dynamical processes
# - **Low h²**: Parameter mostly determined by object-specific properties
# - **Expected patterns**: Eccentricity and inclination often share common variance
#   (dynamical excitation), while size-related parameters may form separate factors

# %% [markdown]
# ## Varimax Rotation for Astronomical Interpretation
#
# Unrotated factors can be difficult to interpret astronomically. Varimax rotation:
# - Seeks "simple structure" where orbital parameters load on specific factors
# - Helps identify distinct dynamical processes
# - Maintains orthogonality (factors remain independent)

# %%
# Apply Varimax rotation for clearer astronomical interpretation
fa_rotated = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal')
fa_rotated.fit(Xs)

loadings_unrotated = fa.loadings_
loadings_rotated = fa_rotated.loadings_

print(f"--- Factor Loadings: Unrotated vs Varimax Rotated ---")
print(f"{'Parameter':<15} ", end="")
for i in range(n_factors):
    print(f"{'Unrot-F' + str(i+1):<10} {'Vmax-F' + str(i+1):<10} ", end="")
print()
print("-" * (15 + 20 * n_factors))

for i, param_name in enumerate(cols):
    print(f"{param_name:<15} ", end="")
    for j in range(n_factors):
        print(f"{loadings_unrotated[i,j]:<10.3f} {loadings_rotated[i,j]:<10.3f} ", end="")
    print()

# %% [markdown]
# ## Factor Loading Visualization
#
# Heatmaps show which orbital parameters load on each factor, helping identify
# the astronomical meaning of each latent dynamical factor.

# %%
# Create factor loadings heatmap
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Unrotated loadings heatmap
sns.heatmap(loadings_unrotated.T, annot=True, fmt='.2f',
           xticklabels=cols, yticklabels=[f'Factor {i+1}' for i in range(n_factors)],
           cmap='RdBu_r', center=0, ax=ax1, cbar_kws={'shrink': 0.8})
ax1.set_title('Unrotated Factor Loadings\n(Kuiper Belt Orbital Parameters)')
ax1.tick_params(axis='x', rotation=45)

# Rotated loadings heatmap
sns.heatmap(loadings_rotated.T, annot=True, fmt='.2f',
           xticklabels=cols, yticklabels=[f'Factor {i+1}' for i in range(n_factors)],
           cmap='RdBu_r', center=0, ax=ax2, cbar_kws={'shrink': 0.8})
ax2.set_title('Varimax Rotated Factor Loadings\n(Kuiper Belt Orbital Parameters)')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
loadings_out = script_dir / "kuiper_fa_loadings.png"
plt.savefig(loadings_out, dpi=150, bbox_inches='tight')
print(f"Saved {loadings_out}")
plt.show()

# %% [markdown]
# ## Astronomical Factor Interpretation
#
# Let's interpret the factors in terms of known orbital dynamics:

# %%
print("--- Astronomical Factor Interpretation ---")

# Identify high-loading parameters for each factor (threshold: |loading| > 0.4)
loading_threshold = 0.4

for factor_idx in range(n_factors):
    factor_name = f"Factor {factor_idx + 1}"
    print(f"\n{factor_name}:")
    
    high_loadings = []
    moderate_loadings = []
    
    for param_idx, param_name in enumerate(cols):
        loading = loadings_rotated[param_idx, factor_idx]
        abs_loading = abs(loading)
        
        if abs_loading > loading_threshold:
            sign = "+" if loading > 0 else "-"
            high_loadings.append(f"{sign}{param_name}({abs_loading:.2f})")
        elif abs_loading > 0.25:  # Moderate loadings
            sign = "+" if loading > 0 else "-"
            moderate_loadings.append(f"{sign}{param_name}({abs_loading:.2f})")
    
    if high_loadings:
        print(f"  Primary loadings: {', '.join(high_loadings)}")
    if moderate_loadings:
        print(f"  Secondary loadings: {', '.join(moderate_loadings)}")
    
    # Astronomical interpretation based on loading patterns
    if not high_loadings:
        print(f"  Interpretation: Weak factor - mostly noise or specific variance")
    else:
        print(f"  Astronomical interpretation: [Examine parameter combinations above]")

# %% [markdown]
# ### Common Orbital Factor Patterns
#
# **Typical factors in Kuiper Belt dynamics**:
# - **Dynamical Excitation Factor**: High loadings on eccentricity and inclination
#   (objects excited by gravitational perturbations)
# - **Distance-Size Factor**: Correlations between semi-major axis and absolute magnitude
#   (observational bias effects or formation processes)
# - **Resonance Factor**: Specific combinations of orbital elements for resonant objects

# %% [markdown]
# ## Factor Scores and Object Classification
#
# Factor scores help classify Kuiper Belt objects by their dynamical properties:

# %%
# Calculate factor scores for all objects
factor_scores = fa_rotated.transform(Xs)

# Create factor score scatter plot (first two factors)
plt.figure(figsize=(10, 8))

# Color points by one of the original variables for interpretation
if len(cols) > 0:
    # Use first column for coloring (often semi-major axis or similar)
    color_var = X.iloc[:, 0]
    scatter = plt.scatter(factor_scores[:, 0], factor_scores[:, 1], 
                         c=color_var, cmap='viridis', alpha=0.7, s=50, edgecolors='black', linewidth=0.5)
    plt.colorbar(scatter, label=f'{cols[0]}')
else:
    plt.scatter(factor_scores[:, 0], factor_scores[:, 1], alpha=0.7, s=50)

plt.xlabel(f'Factor 1 ({eigenvalues_fa[0]:.2f})')
plt.ylabel(f'Factor 2 ({eigenvalues_fa[1]:.2f})')
plt.title('Kuiper Belt Objects: Factor Scores\n(Classified by Dynamical Properties)')
plt.grid(True, ls=':', alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)

plt.tight_layout()
scores_out = script_dir / "kuiper_fa_scores.png"
plt.savefig(scores_out, dpi=150, bbox_inches='tight')
print(f"Saved {scores_out}")
plt.show()

# Print extreme objects in factor space
print(f"\n--- Extreme Objects in Factor Space ---")
for factor_idx in range(min(2, n_factors)):  # Show first 2 factors
    scores = factor_scores[:, factor_idx]
    
    # Highest and lowest factor scores
    high_idx = np.argmax(scores)
    low_idx = np.argmin(scores)
    
    print(f"Factor {factor_idx + 1}:")
    print(f"  Highest score: Object {high_idx} (score: {scores[high_idx]:.3f})")
    print(f"  Lowest score:  Object {low_idx} (score: {scores[low_idx]:.3f})")

# %% [markdown]
# ## Model Validation and Goodness of Fit
#
# Let's evaluate how well the factor model fits the orbital data:

# %%
print("--- Factor Analysis Model Validation ---")

# Calculate model fit statistics
n_objects = X.shape[0]
n_params = X.shape[1]

# Residual correlation matrix
predicted_corr = loadings_rotated @ loadings_rotated.T + np.diag(uniquenesses)
observed_corr = np.corrcoef(Xs.T)
residual_corr = observed_corr - predicted_corr

# Root mean square of residuals (RMSR)
rmsr = np.sqrt(np.mean(np.triu(residual_corr, k=1)**2))
print(f"Root Mean Square of Residuals (RMSR): {rmsr:.4f}")
print(f"  Interpretation: {'✓ Good fit' if rmsr < 0.05 else '△ Acceptable fit' if rmsr < 0.08 else '✗ Poor fit'}")

# Proportion of residual correlations > |0.05|
large_residuals = np.sum(np.abs(np.triu(residual_corr, k=1)) > 0.05)
total_correlations = (n_params * (n_params - 1)) // 2
prop_large_residuals = large_residuals / total_correlations

print(f"Proportion of |residual correlations| > 0.05: {prop_large_residuals:.1%}")
print(f"  Interpretation: {'✓ Good' if prop_large_residuals < 0.1 else '△ Acceptable' if prop_large_residuals < 0.2 else '✗ Poor'} model fit")

# Factor determinacy (reliability of factor scores)
factor_determinacy = np.diag(np.corrcoef(factor_scores.T, Xs.T)[:n_factors, n_factors:])
print(f"\nFactor Score Determinacy:")
for i, det in enumerate(factor_determinacy):
    print(f"  Factor {i+1}: {det:.3f} ({'✓ Good' if det > 0.8 else '△ Acceptable' if det > 0.6 else '✗ Poor'} reliability)")

# %% [markdown]
# ## Conclusion: Factor Analysis for Orbital Dynamics
#
# This Factor Analysis of Kuiper Belt orbital parameters reveals:
#
# ### **Key Insights**:
# - **Latent dynamical factors**: FA identifies common processes affecting multiple orbital elements
# - **Communalities**: Show which orbital parameters are dominated by common vs unique processes  
# - **Factor rotation**: Varimax rotation clarifies which parameters belong to each dynamical factor
# - **Model validation**: Goodness-of-fit statistics indicate how well the factor model represents orbital relationships
#
# ### **Astronomical Applications**:
# - **Population classification**: Factor scores can classify objects by dynamical properties
# - **Formation mechanisms**: Factor patterns may reveal different formation/evolution processes
# - **Observational planning**: High-communality parameters are good proxies for the factor structure
#
# # **Next steps**: Apply these factor interpretations to classify Kuiper Belt populations
# and investigate the astronomical significance of high/low factor score objects.