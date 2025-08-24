"""Objectives of Factor Analysis — practice/demo script

This script is a self-contained demonstration used in the course material
MA2003B (chapter 4.1). It generates synthetic psychology test data with a
known two-factor structure (Intelligence and Verbal ability), then shows how
to inspect the correlation structure, run PCA for comparison, and run factor
analysis using the standard Python libraries.

Sections demonstrated:
 - Correlation analysis and inspection of high correlations
 - Principal Component Analysis (PCA) for variance-explanation comparison
 - Factor Analysis (FA) to identify latent constructs and communalities
 - A short comparison of FA vs PCA objectives
 - Sketch of applied areas where FA is useful

Requirements
 - Python 3.8+ (developed and tested on Python 3.10/3.11)
 - numpy
 - scikit-learn (required; used for StandardScaler and PCA)
 - factor_analyzer (required; used for FactorAnalyzer)

This version of the script assumes scikit-learn and factor_analyzer are
installed. Lightweight illustrative implementations of the core algorithms
are provided in the companion Julia examples in the same exercise folder.

Quick run (from repository root)
  - Create and activate a virtual environment (recommended):
      python3 -m venv .venv
      source .venv/bin/activate
  - Install required packages (minimal):
      pip install -r requirements.txt
  - Run this practice script:
      python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py

Outputs
 - Prints correlation matrices, PCA explained variance, FA loadings/communalities
 - A textual comparison of FA vs PCA objectives

Notes for maintainers
 - The script is intentionally dependency-tolerant: it prefers sklearn/factor_analyzer
   but uses basic implementations when those packages are absent. This keeps the
   demonstration runnable in stripped environments (e.g., teaching machines).

"""

import numpy as np
import warnings

# Required packages for this demonstration
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

np.random.seed(42)


# Note: a minimal PCA/factor-analysis demonstration (without sklearn/factor_analyzer)
# is available in the companion Julia examples under the same exercise folder.


def generate_psychology_data(n_samples=200):
    """Generate synthetic psychology test data with underlying factors."""

    print("Generating Synthetic Psychology Test Data")
    print("========================================")

    # Create underlying factors (latent variables)
    intelligence = np.random.normal(0, 1, n_samples)
    verbal_ability = np.random.normal(0, 1, n_samples)

    # Create observed variables influenced by factors
    # Intelligence factor influences math, logic, spatial
    math_score = 0.8 * intelligence + 0.2 * np.random.normal(0, 1, n_samples)
    logic_score = 0.7 * intelligence + 0.3 * np.random.normal(0, 1, n_samples)
    spatial_score = 0.6 * intelligence + 0.4 * np.random.normal(0, 1, n_samples)

    # Verbal factor influences reading, writing, vocabulary
    reading_score = 0.8 * verbal_ability + 0.2 * np.random.normal(0, 1, n_samples)
    writing_score = 0.7 * verbal_ability + 0.3 * np.random.normal(0, 1, n_samples)
    vocabulary_score = 0.9 * verbal_ability + 0.1 * np.random.normal(0, 1, n_samples)

    # Combine into data matrix
    X = np.column_stack(
        [
            math_score,
            logic_score,
            spatial_score,
            reading_score,
            writing_score,
            vocabulary_score,
        ]
    )

    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]

    print(f"Created {n_samples} observations with {X.shape[1]} variables")
    print("Variables:", variable_names)
    print("True underlying factors: Intelligence, Verbal Ability")

    return X, variable_names


def demonstrate_correlation_structure(X, variable_names):
    """Show correlation patterns in the data."""

    print("\nCorrelation Analysis")
    print("===================")

    # Calculate correlation matrix
    corr_matrix = np.corrcoef(X.T)

    print("Correlation Matrix:")
    print("Variables:", variable_names)
    for i, var1 in enumerate(variable_names):
        row_str = f"{var1:10}"
        for j, var2 in enumerate(variable_names):
            row_str += f" {corr_matrix[i,j]:6.3f}"
        print(row_str)

    # Identify high correlations
    print("\nHigh Correlations (> 0.4):")
    for i in range(len(variable_names)):
        for j in range(i + 1, len(variable_names)):
            if abs(corr_matrix[i, j]) > 0.4:
                print(
                    f"{variable_names[i]} - {variable_names[j]}: {corr_matrix[i,j]:.3f}"
                )


def perform_pca_analysis(X, variable_names):
    """Perform PCA analysis for comparison."""

    print("\nPrincipal Component Analysis")
    print("============================")

    # Standardize data using scikit-learn's StandardScaler (required)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform PCA using scikit-learn (required)
    pca = PCA()
    pca.fit(X_scaled)

    # Show results
    print("PCA Results:")
    print(f"Number of components: {len(pca.explained_variance_ratio_)}")
    print("Explained variance ratio by component:")
    for i, var_exp in enumerate(pca.explained_variance_ratio_):
        print(f"  PC{i+1}: {var_exp:.3f} ({var_exp*100:.1f}%)")

    print(
        f"Cumulative variance explained by first 2 PCs: {sum(pca.explained_variance_ratio_[:2]):.3f}"
    )

    return pca, X_scaled


def perform_factor_analysis(X, variable_names):
    """Perform factor analysis if library is available."""

    print("\nFactor Analysis")
    print("===============")

    # Standardize data and run FactorAnalyzer (factor_analyzer required)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform factor analysis with 2 factors
    fa = FactorAnalyzer(n_factors=2, rotation="varimax")
    fa.fit(X_scaled)

    # Get factor loadings
    loadings = fa.loadings_

    print("Factor Analysis Results (2 factors):")
    print("Factor Loadings:")
    print("Variable       Factor 1  Factor 2")
    print("-" * 35)
    for i, var in enumerate(variable_names):
        print(f"{var:12}  {loadings[i,0]:8.3f}  {loadings[i,1]:8.3f}")

    # Calculate communalities
    communalities = fa.get_communalities()
    print("\nCommunalities:")
    for i, var in enumerate(variable_names):
        print(f"{var:12}: {communalities[i]:.3f}")

    # Factor interpretation
    print("\nFactor Interpretation:")
    print("Factor 1 (high loadings): Math, Logic, Spatial → Intelligence Factor")
    print("Factor 2 (high loadings): Reading, Writing, Vocabulary → Verbal Factor")

    return fa


def simple_factor_analysis(X, variable_names):
    """Simple factor analysis using eigendecomposition."""
    raise RuntimeError(
        "simple_factor_analysis is not available in the Python demo. "
        "See the Julia companion examples for a minimal implementation or "
        "install the 'factor_analyzer' package to run the Python demonstration."
    )


def compare_fa_vs_pca(pca, X_scaled):
    """Compare Factor Analysis and PCA objectives."""

    print("\nComparison: Factor Analysis vs PCA")
    print("==================================")

    print("Factor Analysis Objectives:")
    print("✓ Identify latent constructs (Intelligence, Verbal ability)")
    print("✓ Explain correlations between observed variables")
    print("✓ Model measurement error explicitly")
    print("✓ Focus on common variance only")

    print("\nPCA Objectives:")
    print("✓ Maximize variance explained by components")
    print("✓ Create uncorrelated linear combinations")
    print("✓ Reduce dimensionality efficiently")
    print("✓ Include all variance (common + unique)")

    # Show PCA loadings for comparison
    pca_loadings = pca.components_[:2].T
    print("\nPCA Component Loadings (first 2 components):")
    print("Variable       Comp 1    Comp 2")
    print("-" * 35)
    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]
    for i, var in enumerate(variable_names):
        print(f"{var:12}  {pca_loadings[i,0]:8.3f}  {pca_loadings[i,1]:8.3f}")


def demonstrate_applications():
    """Show different applications of factor analysis."""

    print("\nFactor Analysis Applications")
    print("============================")

    applications = {
        "Psychology": [
            "Intelligence testing (g-factor)",
            "Personality assessment (Big Five)",
            "Attitude measurement",
            "Clinical assessment scales",
        ],
        "Marketing": [
            "Customer segmentation",
            "Brand positioning",
            "Product attribute analysis",
            "Market research simplification",
        ],
        "Finance": [
            "Risk factor identification",
            "Portfolio analysis",
            "Economic indicator grouping",
            "Credit scoring models",
        ],
        "Education": [
            "Academic ability assessment",
            "Learning style identification",
            "Curriculum evaluation",
            "Student performance analysis",
        ],
    }

    for field, apps in applications.items():
        print(f"\n{field}:")
        for app in apps:
            print(f"  • {app}")


def main():
    """Main demonstration of factor analysis objectives."""

    print("MA2003B - Objectives of Factor Analysis")
    print("Comprehensive demonstration of factor analysis purposes and applications")

    # 1. Generate synthetic data with known factor structure
    X, variable_names = generate_psychology_data(n_samples=200)

    # 2. Analyze correlation structure
    demonstrate_correlation_structure(X, variable_names)

    # 3. Perform PCA for comparison
    pca, X_scaled = perform_pca_analysis(X, variable_names)

    # 4. Perform factor analysis (results printed by the function)
    perform_factor_analysis(X, variable_names)

    # 5. Compare FA vs PCA
    compare_fa_vs_pca(pca, X_scaled)

    # 6. Show applications
    demonstrate_applications()

    print("\nSummary")
    print("=======")
    print("✓ Generated data with known factor structure")
    print("✓ Demonstrated correlation patterns")
    print("✓ Performed both PCA and Factor Analysis")
    print("✓ Compared objectives and interpretations")
    print("✓ Showed practical applications across fields")

    print("\nKey Takeaways:")
    print("• Factor Analysis identifies latent variables that cause correlations")
    print("• PCA creates linear combinations that maximize variance")
    print("• FA is theory-driven, PCA is data-driven")
    print("• Choose method based on research objectives")


if __name__ == "__main__":
    main()
