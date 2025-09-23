# %% [markdown]
# # Factor Analysis - Hospital Health Outcomes Example
#
# This script demonstrates Factor Analysis applied to hospital quality data,
# complementing the PCA analysis in hospitals_pca.py. This allows direct comparison
# between PCA and FA on healthcare quality metrics.
#
# ## Key FA applications in healthcare:
# - **Quality Models**: Test theories about hospital quality dimensions
# - **Risk Adjustment**: Separate systematic from hospital-specific factors
# - **Policy Analysis**: Identify intervention targets
#
# ## Expected Results:
# - Dominant quality factor (organizational excellence)
# - High communalities for clinical outcomes
# - Clear factor structure supporting unidimensional quality

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
from sklearn.preprocessing import StandardScaler
from utils import setup_logger

# %%
# Setup logging and paths
script_dir = Path(__file__).resolve().parent
logger = setup_logger("hospitals_fa")

logger.info("Starting Hospital Health Outcomes Factor Analysis")
print("Hospital Health Outcomes - Factor Analysis")
print("=" * 50)

# %% [markdown]
# ## Load Hospital Quality Data

# %%
# Load the same data as PCA example
data_path = script_dir / "hospitals.csv"

if not data_path.exists():
    print(f"Missing {data_path}. Run fetch_hospitals.py first to generate the data.")
    exit(1)

df = pd.read_csv(data_path)
print(f"Loaded {len(df)} hospitals with {len(df.columns)} health outcome metrics")

# Get variable names (exclude hospital ID if present)
health_vars = [
    col
    for col in df.columns
    if col not in ["HospitalID", "hospital_id", "id", "Hospital"]
]
print(f"Health outcome variables: {health_vars}")

# Extract health metrics for analysis
X = df[health_vars].values

# %% [markdown]
# ## Factor Analysis Assumptions Testing

# %%
# Standardize the data (important for healthcare metrics with different units)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

print("\n--- Factor Analysis Assumptions for Healthcare Data ---")

# Bartlett's test of sphericity
chi_square, p_value = calculate_bartlett_sphericity(Xs)
print("Bartlett's Test of Sphericity:")
print(f"  Chi-square: {chi_square:.3f}")
print(f"  p-value: {p_value:.6f}")
print(
    f"  Interpretation: {'✓ Suitable for FA' if p_value < 0.05 else '✗ Not suitable for FA'}"
)

# Kaiser-Meyer-Olkin (KMO) test
kmo_all, kmo_model = calculate_kmo(Xs)
print("\nKMO Test:")
print(f"  Overall MSA: {kmo_model:.3f}")
if kmo_model >= 0.8:
    interpretation = "✓ Excellent"
elif kmo_model >= 0.7:
    interpretation = "✓ Good"
elif kmo_model >= 0.6:
    interpretation = "△ Acceptable"
else:
    interpretation = "✗ Poor"
print(f"  Interpretation: {interpretation}")

# Individual variable MSA
print("\nIndividual Variable MSA:")
print(f"{'Variable':<20} {'MSA':<8} {'Interpretation'}")
print("-" * 40)
for i, var_name in enumerate(health_vars):
    msa_val = kmo_all[i]
    if msa_val >= 0.8:
        msa_interp = "✓ Excellent"
    elif msa_val >= 0.7:
        msa_interp = "✓ Good"
    elif msa_val >= 0.6:
        msa_interp = "△ Acceptable"
    else:
        msa_interp = "✗ Poor"
    print(f"{var_name:<20} {msa_val:<8.3f} {msa_interp}")

# %% [markdown]
# ## Factor Retention Analysis

# %%
# Exploratory factor analysis to determine number of factors
fa_explore = FactorAnalyzer(
    n_factors=len(health_vars), rotation=None, method="principal"
)
fa_explore.fit(Xs)

eigenvalues = fa_explore.get_eigenvalues()[0]
n_factors_kaiser = sum(eigenvalues > 1.0)

print("\n--- Factor Retention Analysis ---")
print(f"{'Factor':<8} {'Eigenvalue':<12} {'% Variance':<12} {'Cumulative %':<12}")
print("-" * 44)

cumulative_var = 0
for i, eigenval in enumerate(eigenvalues):
    var_explained = (eigenval / len(eigenvalues)) * 100
    cumulative_var += var_explained
    print(
        f"Factor {i + 1:<2} {eigenval:<12.3f} {var_explained:<12.1f} {cumulative_var:<12.1f}"
    )

print("\nFactor Retention Criteria:")
print(f"  Kaiser criterion (eigenvalue > 1): {n_factors_kaiser} factors")
print("  Healthcare theory expectation: 1-2 quality factors")
print("  Practical interpretation: Focus on first 1-2 factors")

# %% [markdown]
# ## Factor Analysis: Healthcare Quality Model

# %%
# Based on eigenvalues and healthcare theory, extract 1-2 factors
n_factors = max(1, n_factors_kaiser) if n_factors_kaiser <= 2 else 2

print(f"\n--- Factor Analysis: {n_factors}-Factor Healthcare Quality Model ---")

# Unrotated factor analysis
fa_unrotated = FactorAnalyzer(n_factors=n_factors, rotation=None, method="principal")
fa_unrotated.fit(Xs)

# Rotated factor analysis (if more than 1 factor)
if n_factors > 1:
    fa_rotated = FactorAnalyzer(
        n_factors=n_factors, rotation="varimax", method="principal"
    )
    fa_rotated.fit(Xs)
    loadings_rotated = fa_rotated.loadings_
    rotation_label = "Varimax Rotated"
else:
    fa_rotated = fa_unrotated
    loadings_rotated = fa_unrotated.loadings_
    rotation_label = "Unrotated (Single Factor)"

# Get results
eigenvalues_fa = fa_unrotated.get_eigenvalues()[0][:n_factors]
loadings_unrotated = fa_unrotated.loadings_
communalities = fa_rotated.get_communalities()
uniquenesses = 1 - communalities

print(f"Eigenvalues: {np.round(eigenvalues_fa, 3)}")

print("\nCommunalities (h²) and Uniquenesses (u²):")
print(f"{'Variable':<20} {'h²':<8} {'u²':<8} {'Interpretation'}")
print("-" * 48)
for i, var_name in enumerate(health_vars):
    h2_interp = (
        "High"
        if communalities[i] > 0.6
        else "Medium" if communalities[i] > 0.3 else "Low"
    )
    print(
        f"{var_name:<20} {communalities[i]:<8.3f} {uniquenesses[i]:<8.3f} {h2_interp} common"
    )

# Calculate variance explained by factors
factor_variance = np.sum(communalities)
total_variance = len(health_vars)
variance_explained = factor_variance / total_variance

print(f"\nCommon variance (sum of h²): {factor_variance:.3f}")
print(f"Proportion explained by factors: {variance_explained:.1%}")

# %% [markdown]
# ## Factor Loadings and Interpretation

# %%
print(f"\n--- Factor Loadings: {rotation_label} ---")
if n_factors == 1:
    print(f"{'Variable':<20} {'Factor 1':<10} {'|Loading|':<10}")
    print("-" * 40)
    for i, var_name in enumerate(health_vars):
        loading = loadings_rotated[i, 0]
        abs_loading = abs(loading)
        print(f"{var_name:<20} {loading:<10.3f} {abs_loading:<10.3f}")
else:
    print(f"{'Variable':<20} {'Factor 1':<10} {'Factor 2':<10}")
    print("-" * 40)
    for i, var_name in enumerate(health_vars):
        print(
            f"{var_name:<20} {loadings_rotated[i, 0]:<10.3f} {loadings_rotated[i, 1]:<10.3f}"
        )

# %% [markdown]
# ## Healthcare Factor Interpretation

# %%
print("\n--- Healthcare Factor Interpretation ---")

if n_factors == 1:
    print("Single Factor Model: General Hospital Quality")
    print("  Factor 1: Organizational Excellence")

    # Identify strongest loadings
    abs_loadings = np.abs(loadings_rotated[:, 0])
    sorted_indices = np.argsort(abs_loadings)[::-1]

    print("  Strongest factor indicators:")
    for i in range(min(5, len(sorted_indices))):
        idx = sorted_indices[i]
        var_name = health_vars[idx]
        loading = loadings_rotated[idx, 0]
        direction = "negatively" if loading < 0 else "positively"
        print(f"    {var_name}: {loading:.3f} (loads {direction})")

    print("  Clinical interpretation:")
    print("    - Hospitals with high Factor 1 scores: excellent across all metrics")
    print("    - Hospitals with low Factor 1 scores: poor performance across domains")
    print(
        f"    - Single quality dimension explains {variance_explained:.1%} of variation"
    )

else:
    print("Multi-Factor Model: Specific Quality Dimensions")
    # Add interpretation for multiple factors if extracted
    for factor_idx in range(n_factors):
        print(f"  Factor {factor_idx + 1}:")
        factor_loadings = loadings_rotated[:, factor_idx]
        high_loading_vars = []

        for var_idx, var_name in enumerate(health_vars):
            loading = factor_loadings[var_idx]
            if abs(loading) > 0.4:  # Threshold for meaningful loading
                direction = "+" if loading > 0 else "-"
                high_loading_vars.append(f"{var_name}({direction}{abs(loading):.2f})")

        print(
            f"    High loadings: {', '.join(high_loading_vars) if high_loading_vars else 'None above threshold'}"
        )

# %% [markdown]
# ## Visualization: Factor Structure

# %%
# Create factor loadings visualization
if n_factors == 1:
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    # Single factor bar plot
    loadings_df = pd.DataFrame(
        {"Variable": health_vars, "Loading": loadings_rotated[:, 0]}
    )
    loadings_df = loadings_df.sort_values("Loading", key=abs, ascending=False)

    colors = ["red" if x < 0 else "blue" for x in loadings_df["Loading"]]
    bars = ax.barh(
        loadings_df["Variable"], loadings_df["Loading"], color=colors, alpha=0.7
    )

    ax.set_xlabel("Factor Loading")
    ax.set_title("Hospital Quality Factor Loadings")
    ax.axvline(x=0, color="black", linestyle="-", alpha=0.3)
    ax.grid(True, alpha=0.3)

    # Add loading values on bars
    for _i, (bar, loading) in enumerate(
        zip(bars, loadings_df["Loading"], strict=False)
    ):
        ax.text(
            loading + (0.02 if loading > 0 else -0.02),
            bar.get_y() + bar.get_height() / 2,
            f"{loading:.3f}",
            ha="left" if loading > 0 else "right",
            va="center",
            fontsize=8,
        )

else:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # Multiple factors heatmap
    sns.heatmap(
        loadings_rotated.T,
        annot=True,
        fmt=".3f",
        xticklabels=health_vars,
        yticklabels=[f"Factor {i+1}" for i in range(n_factors)],
        center=0,
        cmap="RdBu_r",
        ax=ax,
    )
    ax.set_title(f"Hospital Quality Factor Loadings ({rotation_label})")
    ax.set_xlabel("Health Outcome Variables")

plt.tight_layout()
loadings_out = script_dir / "hospitals_fa_loadings.png"
loadings_out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(loadings_out, dpi=150, bbox_inches="tight")
plt.close()

print(f"Saved {loadings_out}")

# %% [markdown]
# ## Factor Scores and Hospital Rankings

# %%
# Calculate factor scores for hospitals
factor_scores = fa_rotated.transform(Xs)

print("\n--- Hospital Factor Scores ---")
if n_factors == 1:
    print("Quality Factor Score Distribution:")
    print(f"  Mean: {np.mean(factor_scores[:, 0]):.3f}")
    print(f"  Std:  {np.std(factor_scores[:, 0]):.3f}")
    print(
        f"  Range: [{np.min(factor_scores[:, 0]):.3f}, {np.max(factor_scores[:, 0]):.3f}]"
    )

    # Identify best and worst hospitals
    sorted_indices = np.argsort(factor_scores[:, 0])[::-1]
    print("\nTop 5 Quality Hospitals (Factor 1 scores):")
    for i in range(min(5, len(sorted_indices))):
        idx = sorted_indices[i]
        score = factor_scores[idx, 0]
        print(f"  Hospital {idx+1}: {score:.3f}")

    print("\nBottom 5 Quality Hospitals (Factor 1 scores):")
    for i in range(min(5, len(sorted_indices))):
        idx = sorted_indices[-(i + 1)]
        score = factor_scores[idx, 0]
        print(f"  Hospital {idx+1}: {score:.3f}")

# %% [markdown]
# ## Model Validation and Quality Assessment

# %%
print("\n--- Model Validation ---")

# Factor determinacy (reliability)
if hasattr(fa_rotated, "get_factor_variance"):
    factor_variance_info = fa_rotated.get_factor_variance()
    print(f"Factor variance info available: {factor_variance_info}")

# Communality distribution
high_comm_vars = [health_vars[i] for i, comm in enumerate(communalities) if comm > 0.6]
low_comm_vars = [health_vars[i] for i, comm in enumerate(communalities) if comm < 0.3]

print(
    f"High communality variables (h² > 0.6): {', '.join(high_comm_vars) if high_comm_vars else 'None'}"
)
print(
    f"Low communality variables (h² < 0.3): {', '.join(low_comm_vars) if low_comm_vars else 'None'}"
)

# Model fit assessment
print("\nModel Assessment:")
print(f"  - Number of factors retained: {n_factors}")
print(f"  - Total variance explained: {variance_explained:.1%}")
print(f"  - Average communality: {np.mean(communalities):.3f}")
print(f"  - KMO adequacy: {kmo_model:.3f} ({interpretation})")

# Healthcare-specific insights
print("\nHealthcare Quality Insights:")
if variance_explained > 0.6:
    print("  ✓ Strong evidence for unidimensional quality structure")
    print("  ✓ Hospital rankings based on Factor 1 scores are reliable")
    print("  ✓ Quality improvement should target organizational excellence")
else:
    print("  △ Moderate quality structure, multiple dimensions may exist")
    print("  △ Consider domain-specific quality measures")

logger.info("Hospital Health Outcomes Factor Analysis completed successfully")
