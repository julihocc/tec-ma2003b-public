"""Objectives of Factor Analysis — practice/demo script

This script is a self-contained demonstration used in the course material
MA2003B (chapter 4.1). It generates synthetic psychology test data with a
known two-factor structure (Intelligence and Verbal ability), then shows how
to inspect the correlation structure, run PCA for comparison, and run factor
analysis using the standard Python libraries.

This refactored version separates analysis from reporting:
 - factor_analysis.py: Pure computational functions
 - factor_analysis_reporter.py: Output formatting and display
 - This script: Orchestrates the demonstration workflow

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
 - Analysis functions are in factor_analysis.py (pure computation)
 - Reporting functions are in factor_analysis_reporter.py (output formatting)
 - This allows for easier testing and reuse of analysis components

"""

import warnings

# Local modules for separated analysis and reporting
from factor_analysis import (
    generate_psychology_data,
    compute_correlation_matrix, 
    perform_pca_computation,
    perform_factor_analysis_computation,
    get_applications_data
)

from factor_analysis_reporter import (
    report_data_generation,
    report_correlation_analysis,
    report_pca_results,
    report_factor_analysis,
    report_fa_vs_pca_comparison,
    report_applications,
    report_summary
)

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")




def main():
    """Main demonstration of factor analysis objectives."""

    print("MA2003B - Objectives of Factor Analysis")
    print("Comprehensive demonstration of factor analysis purposes and applications")

    # 1. Generate synthetic data with known factor structure
    X, variable_names = generate_psychology_data(n_samples=200)
    report_data_generation(X, variable_names)

    # 2. Analyze correlation structure
    correlation_results = compute_correlation_matrix(X, variable_names)
    report_correlation_analysis(correlation_results)

    # 3. Perform PCA for comparison
    pca_results = perform_pca_computation(X)
    report_pca_results(pca_results)

    # 4. Perform factor analysis
    fa_results = perform_factor_analysis_computation(X, variable_names)
    report_factor_analysis(fa_results)

    # 5. Compare FA vs PCA
    report_fa_vs_pca_comparison(pca_results)

    # 6. Show applications
    applications_data = get_applications_data()
    report_applications(applications_data)

    # 7. Final summary
    report_summary()


if __name__ == "__main__":
    main()
