#!/usr/bin/env python3
"""
customer_satisfaction_analysis_template.py

Template script for Factor Analysis of TechnoServe Solutions customer satisfaction data.
Students should modify and extend this template to complete their business case analysis.

Usage:
    python customer_satisfaction_analysis_template.py

"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set up logging (following project conventions)
try:
    from utils.logger import setup_logger

    logger = setup_logger(__name__)
except ImportError:
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


def load_data():
    """Load the customer satisfaction dataset"""
    script_dir = Path(__file__).resolve().parent
    data_file = script_dir / "customer_satisfaction_data.csv"

    if not data_file.exists():
        logger.error(f"Data file not found: {data_file}")
        logger.info("Please run fetch_customer_data.py first to generate the dataset")
        return None

    df = pd.read_csv(data_file)
    logger.info(f"Loaded {len(df)} observations from {data_file}")
    return df


def exploratory_analysis(df):
    """Perform initial exploratory data analysis"""
    logger.info("Starting exploratory data analysis...")

    # Basic dataset information
    print("\n=== DATASET OVERVIEW ===")
    print(f"Shape: {df.shape}")
    print(f"Customers: {df['customer_id'].nunique()}")
    print(f"Quarters: {df['quarter'].nunique()}")
    print(f"Date range: {df['survey_date'].min()} to {df['survey_date'].max()}")

    # Identify satisfaction variables (1-7 scale)
    satisfaction_cols = [
        col
        for col in df.columns
        if col
        not in [
            "customer_id",
            "quarter",
            "survey_date",
            "overall_satisfaction",
            "nps_score",
            "renewal_likelihood",
            "revenue_growth_pct",
            "referrals_generated",
        ]
    ]

    print(f"\nSatisfaction items: {len(satisfaction_cols)}")

    # Missing data analysis
    print("\n=== MISSING DATA ANALYSIS ===")
    missing_counts = df[satisfaction_cols].isnull().sum()
    missing_pct = (missing_counts / len(df) * 100).round(2)

    print("Variables with missing data:")
    for var, count, pct in zip(
        missing_counts.index, missing_counts.values, missing_pct.values
    ):
        if count > 0:
            print(f"  {var}: {count} ({pct}%)")

    # Basic descriptive statistics
    print("\n=== DESCRIPTIVE STATISTICS ===")
    print("Satisfaction items (1-7 scale):")
    print(df[satisfaction_cols].describe().round(2))

    # TODO for students: Add more sophisticated EDA
    # - Distribution plots for key variables
    # - Correlation matrix visualization
    # - Quarterly trends analysis
    # - Customer segment analysis

    return satisfaction_cols


def assess_factorability(df, satisfaction_cols):
    """Assess whether data is suitable for Factor Analysis"""
    logger.info("Assessing data suitability for Factor Analysis...")

    # Remove rows with missing data for this assessment
    clean_data = df[satisfaction_cols].dropna()
    print(
        f"\nUsing {len(clean_data)} complete observations for factorability assessment"
    )

    # Correlation matrix
    corr_matrix = clean_data.corr()
    print(f"Correlation matrix shape: {corr_matrix.shape}")

    # Basic correlation checks
    print("\n=== CORRELATION ANALYSIS ===")

    # Count significant correlations
    significant_corrs = (corr_matrix.abs() > 0.3).sum().sum() - len(
        corr_matrix
    )  # Exclude diagonal
    total_corrs = len(corr_matrix) * (len(corr_matrix) - 1)
    print(
        f"Correlations > 0.3: {significant_corrs} of {total_corrs} ({significant_corrs/total_corrs*100:.1f}%)"
    )

    # TODO for students: Implement statistical tests
    # - Kaiser-Meyer-Olkin (KMO) test
    # - Bartlett's test of sphericity
    # - Anti-image correlation matrix
    # - Individual variable MSA values

    print("\nTODO: Implement KMO and Bartlett's tests")
    print("Recommendation: KMO should be > 0.6, preferably > 0.8")
    print("Recommendation: Bartlett's test should be significant (p < 0.05)")

    return corr_matrix


def factor_extraction_demo(df, satisfaction_cols):
    """Demonstrate factor extraction methods"""
    logger.info("Demonstrating factor extraction approaches...")

    print("\n=== FACTOR EXTRACTION ===")
    print("TODO: Implement factor extraction methods:")
    print("1. Principal Component Analysis (PCA)")
    print("2. Maximum Likelihood Factor Analysis")
    print("3. Principal Axis Factoring")

    print("\nFactor selection criteria to implement:")
    print("- Eigenvalue > 1 (Kaiser criterion)")
    print("- Scree plot inspection")
    print("- Parallel analysis")
    print("- Explained variance thresholds")

    # TODO for students: Implement extraction methods
    # Using scikit-learn for PCA
    # Using factor_analyzer package for ML factor analysis

    return None


def create_output_directory():
    """Create output directory for plots and reports"""
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir / "analysis_output"
    output_dir.mkdir(exist_ok=True, parents=True)
    return output_dir


def main():
    """Main analysis workflow"""
    logger.info("Starting TechnoServe Customer Satisfaction Analysis")

    # Create output directory
    output_dir = create_output_directory()

    # Load data
    df = load_data()
    if df is None:
        return 1

    # Exploratory analysis
    satisfaction_cols = exploratory_analysis(df)

    # Assess factorability
    corr_matrix = assess_factorability(df, satisfaction_cols)

    # Factor extraction demonstration
    factor_extraction_demo(df, satisfaction_cols)

    # TODO for students: Complete the analysis pipeline
    print("\n=== ANALYSIS PIPELINE TO COMPLETE ===")
    print("1. ✓ Data loading and exploration")
    print("2. ✓ Missing data assessment")
    print("3. TODO: Implement factorability tests (KMO, Bartlett's)")
    print("4. TODO: Factor extraction and selection")
    print("5. TODO: Factor rotation and interpretation")
    print("6. TODO: Factor scoring")
    print("7. TODO: Business interpretation and recommendations")
    print("8. TODO: Predictive modeling with factor scores")
    print("9. TODO: Generate executive summary report")

    logger.info(f"Analysis outputs will be saved to: {output_dir}")
    logger.info("Analysis template completed. Students should extend this script.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
