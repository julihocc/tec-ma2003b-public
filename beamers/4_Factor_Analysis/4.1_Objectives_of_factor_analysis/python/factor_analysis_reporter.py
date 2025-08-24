"""Factor Analysis Reporting - Output formatting and display functions

This module handles all output formatting and display for factor analysis results.
It takes the computational results from factor_analysis.py and presents them
in a readable format.

Functions:
    - report_data_generation: Display data generation summary
    - report_correlation_analysis: Display correlation matrix and high correlations
    - report_pca_results: Display PCA analysis results
    - report_factor_analysis: Display factor analysis results
    - report_fa_vs_pca_comparison: Display comparison between FA and PCA
    - report_applications: Display factor analysis applications
    - report_summary: Display final summary and key takeaways
"""

from typing import List, Dict
import numpy as np

from factor_analysis import (
    CorrelationResults, 
    PCAResults, 
    FactorAnalysisResults
)


def report_data_generation(X: np.ndarray, variable_names: List[str]) -> None:
    """Display data generation summary.

    Args:
        X: Generated data matrix.
        variable_names: List of variable names.
    """
    print("Generating Synthetic Psychology Test Data")
    print("========================================")
    print(f"Created {X.shape[0]} observations with {X.shape[1]} variables")
    print("Variables:", variable_names)
    print("True underlying factors: Intelligence, Verbal Ability")


def report_correlation_analysis(results: CorrelationResults) -> None:
    """Display correlation matrix and high correlations.

    Args:
        results: CorrelationResults object containing correlation data.
    """
    print("\nCorrelation Analysis")
    print("===================")
    
    print("Correlation Matrix:")
    print("Variables:", results.variable_names)
    
    for i, var1 in enumerate(results.variable_names):
        row_str = f"{var1:10}"
        for j, var2 in enumerate(results.variable_names):
            row_str += f" {results.matrix[i,j]:6.3f}"
        print(row_str)

    print("\nHigh Correlations (> 0.4):")
    for var1, var2, corr in results.high_correlations:
        print(f"{var1} - {var2}: {corr:.3f}")


def report_pca_results(results: PCAResults) -> None:
    """Display PCA analysis results.

    Args:
        results: PCAResults object containing PCA data.
    """
    print("\nPrincipal Component Analysis")
    print("============================")
    
    print("PCA Results:")
    print(f"Number of components: {len(results.explained_variance_ratio)}")
    print("Explained variance ratio by component:")
    
    for i, var_exp in enumerate(results.explained_variance_ratio):
        print(f"  PC{i+1}: {var_exp:.3f} ({var_exp*100:.1f}%)")

    print(f"Cumulative variance explained by first 2 PCs: {results.cumulative_variance_2pc:.3f}")


def report_factor_analysis(results: FactorAnalysisResults) -> None:
    """Display factor analysis results.

    Args:
        results: FactorAnalysisResults object containing FA data.
    """
    print("\nFactor Analysis")
    print("===============")
    
    print("Factor Analysis Results (2 factors):")
    
    if results.loadings is None:
        print("Factor loadings are unavailable (None). Skipping detailed loadings display.")
    else:
        print("Factor Loadings:")
        print("Variable       Factor 1  Factor 2")
        print("-" * 35)
        for i, var in enumerate(results.variable_names):
            print(f"{var:12}  {results.loadings[i,0]:8.3f}  {results.loadings[i,1]:8.3f}")

    print("\nCommunalities:")
    for i, var in enumerate(results.variable_names):
        print(f"{var:12}: {results.communalities[i]:.3f}")

    print("\nFactor Interpretation:")
    print("Factor 1 (high loadings): Math, Logic, Spatial → Intelligence Factor")
    print("Factor 2 (high loadings): Reading, Writing, Vocabulary → Verbal Factor")


def report_fa_vs_pca_comparison(pca_results: PCAResults) -> None:
    """Display comparison between Factor Analysis and PCA.

    Args:
        pca_results: PCAResults object for displaying PCA loadings comparison.
    """
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
    print("\nPCA Component Loadings (first 2 components):")
    print("Variable       Comp 1    Comp 2")
    print("-" * 35)
    
    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]
    for i, var in enumerate(variable_names):
        print(f"{var:12}  {pca_results.component_loadings[i,0]:8.3f}  {pca_results.component_loadings[i,1]:8.3f}")


def report_applications(applications_data: Dict[str, List[str]]) -> None:
    """Display factor analysis applications.

    Args:
        applications_data: Dictionary with field names as keys and applications as values.
    """
    print("\nFactor Analysis Applications")
    print("============================")

    for field, apps in applications_data.items():
        print(f"\n{field}:")
        for app in apps:
            print(f"  • {app}")


def report_summary() -> None:
    """Display final summary and key takeaways."""
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