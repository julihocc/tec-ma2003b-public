"""Factor Analysis Reporting - Output formatting functions

This module handles all output formatting for factor analysis results.
It takes the computational results from factor_analysis.py and formats them
into strings that can be used by the calling application.

Functions:
    - format_data_generation: Format data generation summary
    - format_correlation_analysis: Format correlation matrix and high correlations
    - format_pca_results: Format PCA analysis results
    - format_factor_analysis: Format factor analysis results
    - format_fa_vs_pca_comparison: Format comparison between FA and PCA
    - format_applications: Format factor analysis applications
    - format_summary: Format final summary and key takeaways
"""

from typing import List, Dict
import numpy as np

from factor_analysis import (
    CorrelationResults, 
    PCAResults, 
    FactorAnalysisResults
)


def format_data_generation(X: np.ndarray, variable_names: List[str]) -> str:
    """Format data generation summary.

    Args:
        X: Generated data matrix.
        variable_names: List of variable names.
        
    Returns:
        Formatted string describing the data generation.
    """
    lines = [
        "Generating Synthetic Psychology Test Data",
        "========================================",
        f"Created {X.shape[0]} observations with {X.shape[1]} variables",
        f"Variables: {variable_names}",
        "True underlying factors: Intelligence, Verbal Ability"
    ]
    return "\n".join(lines)


def format_correlation_analysis(results: CorrelationResults) -> str:
    """Format correlation matrix and high correlations.

    Args:
        results: CorrelationResults object containing correlation data.
        
    Returns:
        Formatted string with correlation analysis results.
    """
    lines = [
        "\nCorrelation Analysis",
        "===================",
        "",
        "Correlation Matrix:",
        f"Variables: {results.variable_names}"
    ]
    
    for i, var1 in enumerate(results.variable_names):
        row_str = f"{var1:10}"
        for j, var2 in enumerate(results.variable_names):
            row_str += f" {results.matrix[i,j]:6.3f}"
        lines.append(row_str)

    lines.extend([
        "",
        "High Correlations (> 0.4):"
    ])
    
    for var1, var2, corr in results.high_correlations:
        lines.append(f"{var1} - {var2}: {corr:.3f}")
    
    return "\n".join(lines)


def format_pca_results(results: PCAResults) -> str:
    """Format PCA analysis results.

    Args:
        results: PCAResults object containing PCA data.
        
    Returns:
        Formatted string with PCA results.
    """
    lines = [
        "\nPrincipal Component Analysis",
        "============================",
        "",
        "PCA Results:",
        f"Number of components: {len(results.explained_variance_ratio)}",
        "Explained variance ratio by component:"
    ]
    
    for i, var_exp in enumerate(results.explained_variance_ratio):
        lines.append(f"  PC{i+1}: {var_exp:.3f} ({var_exp*100:.1f}%)")

    lines.append(f"Cumulative variance explained by first 2 PCs: {results.cumulative_variance_2pc:.3f}")
    
    return "\n".join(lines)


def format_factor_analysis(results: FactorAnalysisResults) -> str:
    """Format factor analysis results.

    Args:
        results: FactorAnalysisResults object containing FA data.
        
    Returns:
        Formatted string with factor analysis results.
    """
    lines = [
        "\nFactor Analysis",
        "===============",
        "",
        "Factor Analysis Results (2 factors):"
    ]
    
    if results.loadings is None:
        lines.append("Factor loadings are unavailable (None). Skipping detailed loadings display.")
    else:
        lines.extend([
            "Factor Loadings:",
            "Variable       Factor 1  Factor 2",
            "-" * 35
        ])
        for i, var in enumerate(results.variable_names):
            lines.append(f"{var:12}  {results.loadings[i,0]:8.3f}  {results.loadings[i,1]:8.3f}")

    lines.extend([
        "",
        "Communalities:"
    ])
    for i, var in enumerate(results.variable_names):
        lines.append(f"{var:12}: {results.communalities[i]:.3f}")

    lines.extend([
        "",
        "Factor Interpretation:",
        "Factor 1 (high loadings): Math, Logic, Spatial → Intelligence Factor",
        "Factor 2 (high loadings): Reading, Writing, Vocabulary → Verbal Factor"
    ])
    
    return "\n".join(lines)


def format_fa_vs_pca_comparison(pca_results: PCAResults) -> str:
    """Format comparison between Factor Analysis and PCA.

    Args:
        pca_results: PCAResults object for displaying PCA loadings comparison.
        
    Returns:
        Formatted string with FA vs PCA comparison.
    """
    lines = [
        "\nComparison: Factor Analysis vs PCA",
        "==================================",
        "",
        "Factor Analysis Objectives:",
        "✓ Identify latent constructs (Intelligence, Verbal ability)",
        "✓ Explain correlations between observed variables",
        "✓ Model measurement error explicitly",
        "✓ Focus on common variance only",
        "",
        "PCA Objectives:",
        "✓ Maximize variance explained by components",
        "✓ Create uncorrelated linear combinations",
        "✓ Reduce dimensionality efficiently",
        "✓ Include all variance (common + unique)",
        "",
        "PCA Component Loadings (first 2 components):",
        "Variable       Comp 1    Comp 2",
        "-" * 35
    ]
    
    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]
    for i, var in enumerate(variable_names):
        lines.append(f"{var:12}  {pca_results.component_loadings[i,0]:8.3f}  {pca_results.component_loadings[i,1]:8.3f}")
    
    return "\n".join(lines)


def format_applications(applications_data: Dict[str, List[str]]) -> str:
    """Format factor analysis applications.

    Args:
        applications_data: Dictionary with field names as keys and applications as values.
        
    Returns:
        Formatted string with applications information.
    """
    lines = [
        "\nFactor Analysis Applications",
        "============================"
    ]

    for field, apps in applications_data.items():
        lines.append(f"\n{field}:")
        for app in apps:
            lines.append(f"  • {app}")
    
    return "\n".join(lines)


def format_summary() -> str:
    """Format final summary and key takeaways.
    
    Returns:
        Formatted string with summary and key takeaways.
    """
    lines = [
        "\nSummary",
        "=======",
        "✓ Generated data with known factor structure",
        "✓ Demonstrated correlation patterns",
        "✓ Performed both PCA and Factor Analysis",
        "✓ Compared objectives and interpretations",
        "✓ Showed practical applications across fields",
        "",
        "Key Takeaways:",
        "• Factor Analysis identifies latent variables that cause correlations",
        "• PCA creates linear combinations that maximize variance",
        "• FA is theory-driven, PCA is data-driven",
        "• Choose method based on research objectives"
    ]
    
    return "\n".join(lines)