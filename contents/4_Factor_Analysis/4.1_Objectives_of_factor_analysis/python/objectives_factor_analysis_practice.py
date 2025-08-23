"""4.1 Objectives of Factor Analysis

Practice script: demonstrate the key objectives and applications of factor analysis,
comparing it with PCA and showing practical examples.

This demonstrates the key concepts from the presentation:
- Factor analysis vs PCA comparison
- Dimensionality reduction objectives
- Latent variable identification
- Practical applications
"""

import numpy as np
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Try to import sklearn components, fall back if not available
try:
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Note: sklearn not available, using basic implementations")

# Try to import factor_analyzer, fall back to basic implementation if not available
try:
    from factor_analyzer import FactorAnalyzer
    FACTOR_ANALYZER_AVAILABLE = True
except ImportError:
    FACTOR_ANALYZER_AVAILABLE = False
    print("Note: factor_analyzer not available, using basic implementation")

np.random.seed(42)


def standardize_data(X):
    """Standardize data to have mean 0 and std 1."""
    return (X - np.mean(X, axis=0)) / np.std(X, axis=0)


class SimplePCA:
    """Basic PCA implementation using eigendecomposition."""
    
    def __init__(self):
        self.explained_variance_ratio_ = None
        self.components_ = None
        
    def fit(self, X):
        # Calculate covariance matrix
        cov_matrix = np.cov(X.T)
        
        # Eigendecomposition
        eigenvals, eigenvecs = np.linalg.eigh(cov_matrix)
        
        # Sort by eigenvalues (descending)
        idx = np.argsort(eigenvals)[::-1]
        eigenvals = eigenvals[idx]
        eigenvecs = eigenvecs[:, idx]
        
        # Store results
        self.explained_variance_ratio_ = eigenvals / np.sum(eigenvals)
        self.components_ = eigenvecs.T
        
        return self


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
    X = np.column_stack([math_score, logic_score, spatial_score, 
                        reading_score, writing_score, vocabulary_score])
    
    variable_names = ['Math', 'Logic', 'Spatial', 'Reading', 'Writing', 'Vocabulary']
    
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
        for j in range(i+1, len(variable_names)):
            if abs(corr_matrix[i,j]) > 0.4:
                print(f"{variable_names[i]} - {variable_names[j]}: {corr_matrix[i,j]:.3f}")


def perform_pca_analysis(X, variable_names):
    """Perform PCA analysis for comparison."""
    
    print("\nPrincipal Component Analysis")
    print("============================")
    
    # Standardize data
    if SKLEARN_AVAILABLE:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = standardize_data(X)
    
    # Perform PCA
    if SKLEARN_AVAILABLE:
        pca = PCA()
        pca.fit(X_scaled)
    else:
        pca = SimplePCA()
        pca.fit(X_scaled)
    
    # Show results
    print("PCA Results:")
    print(f"Number of components: {len(pca.explained_variance_ratio_)}")
    print("Explained variance ratio by component:")
    for i, var_exp in enumerate(pca.explained_variance_ratio_):
        print(f"  PC{i+1}: {var_exp:.3f} ({var_exp*100:.1f}%)")
    
    print(f"Cumulative variance explained by first 2 PCs: {sum(pca.explained_variance_ratio_[:2]):.3f}")
    
    return pca, X_scaled


def perform_factor_analysis(X, variable_names):
    """Perform factor analysis if library is available."""
    
    print("\nFactor Analysis")
    print("===============")
    
    if not FACTOR_ANALYZER_AVAILABLE:
        print("Factor analysis library not available. Using correlation-based approach.")
        return simple_factor_analysis(X, variable_names)
    
    # Standardize data
    if SKLEARN_AVAILABLE:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = standardize_data(X)
    
    # Perform factor analysis with 2 factors
    fa = FactorAnalyzer(n_factors=2, rotation='varimax')
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
    
    # Standardize data
    if SKLEARN_AVAILABLE:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = standardize_data(X)
    
    # Calculate correlation matrix
    R = np.corrcoef(X_scaled.T)
    
    # Eigendecomposition
    eigenvals, eigenvecs = np.linalg.eigh(R)
    
    # Sort by eigenvalues (descending)
    idx = np.argsort(eigenvals)[::-1]
    eigenvals = eigenvals[idx]
    eigenvecs = eigenvecs[:, idx]
    
    # Take first 2 factors
    loadings = eigenvecs[:, :2] * np.sqrt(eigenvals[:2])
    
    print("Simple Factor Analysis Results (2 factors):")
    print("Eigenvalues:", eigenvals[:3])
    print("Factor Loadings:")
    print("Variable       Factor 1  Factor 2")
    print("-" * 35)
    for i, var in enumerate(variable_names):
        print(f"{var:12}  {loadings[i,0]:8.3f}  {loadings[i,1]:8.3f}")
    
    return loadings


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
    variable_names = ['Math', 'Logic', 'Spatial', 'Reading', 'Writing', 'Vocabulary']
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
            "Clinical assessment scales"
        ],
        "Marketing": [
            "Customer segmentation",
            "Brand positioning",
            "Product attribute analysis",
            "Market research simplification"
        ],
        "Finance": [
            "Risk factor identification",
            "Portfolio analysis",
            "Economic indicator grouping",
            "Credit scoring models"
        ],
        "Education": [
            "Academic ability assessment",
            "Learning style identification",
            "Curriculum evaluation",
            "Student performance analysis"
        ]
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
    
    # 4. Perform factor analysis
    fa_results = perform_factor_analysis(X, variable_names)
    
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