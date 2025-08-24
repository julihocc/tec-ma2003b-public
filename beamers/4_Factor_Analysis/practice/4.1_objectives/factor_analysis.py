"""Factor Analysis - Core computational functions

This module provides pure computational functions for factor analysis without
any output formatting or display. Used by the objectives_factor_analysis_practice.py
demonstration script.

Functions:
    - generate_psychology_data: Create synthetic test data with known factor structure
    - compute_correlation_matrix: Calculate correlation matrix and identify high correlations
    - perform_pca_computation: Execute PCA and return results
    - perform_factor_analysis_computation: Execute factor analysis and return results
    - get_applications_data: Return structured data about FA applications
"""

import numpy as np
from typing import Tuple, List, Dict, Any, Optional
from dataclasses import dataclass

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer


@dataclass
class CorrelationResults:
    """Results from correlation analysis."""
    matrix: np.ndarray
    high_correlations: List[Tuple[str, str, float]]
    variable_names: List[str]


@dataclass
class PCAResults:
    """Results from PCA analysis."""
    pca_model: PCA
    explained_variance_ratio: np.ndarray
    cumulative_variance_2pc: float
    component_loadings: np.ndarray
    scaled_data: np.ndarray


@dataclass
class FactorAnalysisResults:
    """Results from factor analysis."""
    fa_model: FactorAnalyzer
    loadings: Optional[np.ndarray]
    communalities: np.ndarray
    variable_names: List[str]


def generate_psychology_data(n_samples: int = 200) -> Tuple[np.ndarray, List[str]]:
    """Generate synthetic psychology test data with known underlying factors.

    The synthetic dataset contains six observed variables influenced by two
    latent factors (Intelligence and Verbal ability).

    Args:
        n_samples: Number of observations to generate.

    Returns:
        A tuple (X, variable_names) where X is an (n_samples x 6) numpy array
        and variable_names is a list of 6 strings.
    """
    np.random.seed(42)
    
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
    X = np.column_stack([
        math_score, logic_score, spatial_score,
        reading_score, writing_score, vocabulary_score
    ])

    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]
    
    return X, variable_names


def compute_correlation_matrix(X: np.ndarray, variable_names: List[str], 
                             threshold: float = 0.4) -> CorrelationResults:
    """Calculate correlation matrix and identify high correlations.

    Args:
        X: 2D data array with shape (n_samples, n_variables).
        variable_names: List of variable names matching columns in X.
        threshold: Minimum absolute correlation to be considered "high".

    Returns:
        CorrelationResults object containing the correlation matrix and 
        high correlation pairs.
    """
    # Calculate correlation matrix
    corr_matrix = np.corrcoef(X.T)

    # Identify high correlations
    high_correlations = []
    for i in range(len(variable_names)):
        for j in range(i + 1, len(variable_names)):
            if abs(corr_matrix[i, j]) > threshold:
                high_correlations.append((
                    variable_names[i], 
                    variable_names[j], 
                    corr_matrix[i, j]
                ))

    return CorrelationResults(
        matrix=corr_matrix,
        high_correlations=high_correlations,
        variable_names=variable_names
    )


def perform_pca_computation(X: np.ndarray) -> PCAResults:
    """Run PCA on standardized data and return results.

    Args:
        X: 2D data array (n_samples, n_features).

    Returns:
        PCAResults object containing PCA model, explained variance ratios,
        and component loadings.
    """
    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform PCA
    pca = PCA()
    pca.fit(X_scaled)

    # Calculate cumulative variance for first 2 components
    cumulative_variance_2pc = sum(pca.explained_variance_ratio_[:2])
    
    # Get component loadings (first 2 components)
    component_loadings = pca.components_[:2].T

    return PCAResults(
        pca_model=pca,
        explained_variance_ratio=pca.explained_variance_ratio_,
        cumulative_variance_2pc=cumulative_variance_2pc,
        component_loadings=component_loadings,
        scaled_data=X_scaled
    )


def perform_factor_analysis_computation(X: np.ndarray, variable_names: List[str], 
                                      n_factors: int = 2, 
                                      rotation: str = "varimax") -> FactorAnalysisResults:
    """Perform factor analysis and return results.

    Args:
        X: 2D data array (n_samples, n_features).
        variable_names: List of variable names.
        n_factors: Number of factors to extract.
        rotation: Rotation method to use.

    Returns:
        FactorAnalysisResults object containing the fitted model, loadings,
        and communalities.
    """
    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform factor analysis
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation)
    fa.fit(X_scaled)

    # Get results
    loadings = fa.loadings_
    communalities = fa.get_communalities()

    return FactorAnalysisResults(
        fa_model=fa,
        loadings=loadings,
        communalities=communalities,
        variable_names=variable_names
    )


def get_applications_data() -> Dict[str, List[str]]:
    """Return structured data about factor analysis applications.

    Returns:
        Dictionary with field names as keys and lists of applications as values.
    """
    return {
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