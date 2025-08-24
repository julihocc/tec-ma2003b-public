"""
MA2003B - Factor Analysis Practice: Mathematical Foundation and Equations

Topic 4.2: Understanding and implementing the fundamental factor analysis equations

Learning Objectives:
- Derive and implement the basic factor model: X = ΛF + ε
- Calculate factor loadings and communalities
- Understand variance decomposition in factor analysis
- Compare different estimation methods (PAF vs ML)

Author: Dr. Juliho Castillo
Institution: Tec de Monterrey
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from utils import setup_logger

# Configure logging
logger = setup_logger(__name__)

class FactorAnalysisEquations:
    """
    Demonstrates the mathematical foundations of factor analysis through
    implementation and visualization of key equations.
    """
    
    def __init__(self, n_samples=200, n_features=12, n_factors=3, random_state=42):
        """
        Initialize with parameters for synthetic data generation.
        
        Args:
            n_samples: Number of observations
            n_features: Number of observed variables
            n_factors: True number of underlying factors
            random_state: Random seed for reproducibility
        """
        self.n_samples = n_samples
        self.n_features = n_features
        self.n_factors = n_factors
        self.random_state = random_state
        
        logger.info(f"Initialized FactorAnalysisEquations with {n_samples} samples, "
                   f"{n_features} variables, {n_factors} factors")
    
    def generate_factor_data(self):
        """
        Generate synthetic data that follows the factor model: X = ΛF + ε
        
        Returns:
            X: Observed variables matrix (n_samples × n_features)
            F: True factor scores matrix (n_samples × n_factors)  
            Lambda: True factor loadings matrix (n_features × n_factors)
            epsilon: Unique factors matrix (n_samples × n_features)
        """
        np.random.seed(self.random_state)
        
        # Generate true factor scores F (n_samples × n_factors)
        F = np.random.normal(0, 1, (self.n_samples, self.n_factors))
        
        # Create structured factor loadings matrix Λ (n_features × n_factors)
        Lambda = np.zeros((self.n_features, self.n_factors))
        
        # Each factor loads on 4 variables with high loadings
        for factor in range(self.n_factors):
            start_var = factor * 4
            end_var = min(start_var + 4, self.n_features)
            
            # High loadings (0.6-0.8) for primary variables
            Lambda[start_var:end_var, factor] = np.random.uniform(0.6, 0.8, end_var - start_var)
            
            # Small cross-loadings (0.1-0.3) for some other variables
            other_vars = np.random.choice([i for i in range(self.n_features) 
                                         if i < start_var or i >= end_var], 
                                        size=2, replace=False)
            Lambda[other_vars, factor] = np.random.uniform(0.1, 0.3, 2)
        
        # Generate unique factors ε with varying uniqueness
        uniqueness = np.random.uniform(0.2, 0.6, self.n_features)
        epsilon = np.random.normal(0, 1, (self.n_samples, self.n_features)) * np.sqrt(uniqueness)
        
        # Generate observed variables: X = ΛF + ε
        X = F @ Lambda.T + epsilon
        
        # Standardize observed variables
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        
        logger.info("Generated synthetic factor data following X = ΛF + ε model")
        
        return X, F, Lambda, epsilon
    
    def demonstrate_factor_model(self, X, F, Lambda, epsilon):
        """
        Demonstrate the factor model equation and its components.
        
        Args:
            X: Observed variables
            F: True factor scores
            Lambda: True factor loadings
            epsilon: Unique factors
        """
        print("="*70)
        print("FACTOR MODEL DEMONSTRATION: X = ΛF + ε")
        print("="*70)
        
        # Show dimensions
        print(f"Data Dimensions:")
        print(f"  X (Observed variables): {X.shape}")
        print(f"  F (Factor scores): {F.shape}")
        print(f"  Λ (Factor loadings): {Lambda.shape}")
        print(f"  ε (Unique factors): {epsilon.shape}")
        print()
        
        # Show sample of true loadings matrix
        print("True Factor Loadings Matrix (Λ) - First 8 variables:")
        loadings_df = pd.DataFrame(Lambda[:8], 
                                 columns=[f'Factor_{i+1}' for i in range(self.n_factors)],
                                 index=[f'Var_{i+1}' for i in range(8)])
        print(loadings_df.round(3))
        print()
        
        # Calculate and display communalities
        communalities_true = np.sum(Lambda**2, axis=1)
        uniqueness_true = 1 - communalities_true
        
        print("Variance Decomposition for First 8 Variables:")
        variance_df = pd.DataFrame({
            'Communality (h²)': communalities_true[:8],
            'Uniqueness (u²)': uniqueness_true[:8],
            'Total': communalities_true[:8] + uniqueness_true[:8]
        }, index=[f'Var_{i+1}' for i in range(8)])
        
        print(variance_df.round(3))
        print()
        
        # Verify factor model equation
        X_reconstructed = F @ Lambda.T + epsilon
        reconstruction_error = np.mean((X - X_reconstructed)**2)
        print(f"Factor Model Verification:")
        print(f"  Mean squared error between X and ΛF + ε: {reconstruction_error:.6f}")
        print(f"  (Should be near 0 for perfect model fit)")
        print()
    
    def compare_estimation_methods(self, X):
        """
        Compare different factor analysis estimation methods.
        
        Args:
            X: Observed variables matrix
        """
        print("="*70)
        print("COMPARISON OF ESTIMATION METHODS")
        print("="*70)
        
        methods = {
            'Principal Axis Factoring': {'method': 'minres', 'name': 'PAF'},
            'Maximum Likelihood': {'method': 'ml', 'name': 'ML'}
        }
        
        results = {}
        
        for method_name, config in methods.items():
            print(f"\n{method_name}:")
            print("-" * 30)
            
            # Fit factor analysis
            fa = FactorAnalyzer(n_factors=self.n_factors, 
                              rotation='varimax',
                              method=config['method'])
            fa.fit(X)
            
            # Get results
            loadings = fa.loadings_
            communalities = fa.get_communalities()
            uniquenesses = fa.get_uniquenesses()
            eigenvalues, _ = fa.get_eigenvalues()
            
            results[config['name']] = {
                'loadings': loadings,
                'communalities': communalities,
                'uniquenesses': uniquenesses,
                'eigenvalues': eigenvalues[:self.n_factors]
            }
            
            # Display key statistics
            print(f"Eigenvalues: {eigenvalues[:self.n_factors].round(3)}")
            print(f"Total variance explained: {np.sum(eigenvalues[:self.n_factors]):.3f}")
            print(f"Mean communality: {np.mean(communalities):.3f}")
            print(f"Mean uniqueness: {np.mean(uniquenesses):.3f}")
        
        # Compare methods
        print("\n" + "="*50)
        print("METHOD COMPARISON")
        print("="*50)
        
        # Compare communalities
        comm_diff = np.mean(np.abs(results['PAF']['communalities'] - 
                                 results['ML']['communalities']))
        print(f"Mean absolute difference in communalities: {comm_diff:.4f}")
        
        # Compare factor loadings (using Procrustes-like alignment)
        loading_diff = np.mean(np.abs(results['PAF']['loadings'] - 
                                    results['ML']['loadings']))
        print(f"Mean absolute difference in factor loadings: {loading_diff:.4f}")
        
        print(f"\nNote: Small differences indicate similar solutions")
        print(f"Large differences may indicate:")
        print(f"  - Non-normal data (favors PAF)")
        print(f"  - Model misspecification") 
        print(f"  - Convergence issues")
        
        return results
    
    def demonstrate_communalities_calculation(self, fa_results):
        """
        Demonstrate how communalities are calculated from factor loadings.
        
        Args:
            fa_results: Results from factor analysis
        """
        print("\n" + "="*70)
        print("COMMUNALITIES CALCULATION DEMONSTRATION")
        print("="*70)
        
        loadings = fa_results['PAF']['loadings']
        computed_communalities = fa_results['PAF']['communalities']
        
        print("Formula: h²ᵢ = Σ(λᵢⱼ)² for all factors j")
        print()
        
        # Manual calculation of communalities
        manual_communalities = np.sum(loadings**2, axis=1)
        
        # Show calculation for first 5 variables
        print("Manual Calculation for First 5 Variables:")
        for i in range(5):
            squared_loadings = loadings[i]**2
            sum_squared = np.sum(squared_loadings)
            
            print(f"Variable {i+1}:")
            for j in range(self.n_factors):
                print(f"  λ²_{i+1},{j+1} = ({loadings[i,j]:.3f})² = {squared_loadings[j]:.3f}")
            print(f"  h²_{i+1} = {' + '.join([f'{val:.3f}' for val in squared_loadings])} = {sum_squared:.3f}")
            print(f"  u²_{i+1} = 1 - {sum_squared:.3f} = {1-sum_squared:.3f}")
            print()
        
        # Verify calculations match software
        calculation_error = np.mean(np.abs(manual_communalities - computed_communalities))
        print(f"Verification:")
        print(f"  Mean absolute error between manual and software calculation: {calculation_error:.6f}")
        print(f"  (Should be near 0)")
    
    def visualize_factor_structure(self, X, fa_results):
        """
        Visualize the factor structure and relationships.
        
        Args:
            X: Observed variables
            fa_results: Factor analysis results
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Factor loadings heatmap
        loadings = fa_results['PAF']['loadings']
        im1 = axes[0,0].imshow(loadings, cmap='RdBu', aspect='auto', vmin=-1, vmax=1)
        axes[0,0].set_title('Factor Loadings Matrix')
        axes[0,0].set_xlabel('Factors')
        axes[0,0].set_ylabel('Variables')
        axes[0,0].set_xticks(range(self.n_factors))
        axes[0,0].set_xticklabels([f'F{i+1}' for i in range(self.n_factors)])
        plt.colorbar(im1, ax=axes[0,0])
        
        # Plot 2: Communalities vs Uniquenesses
        communalities = fa_results['PAF']['communalities']
        uniquenesses = fa_results['PAF']['uniquenesses']
        
        axes[0,1].bar(range(len(communalities)), communalities, alpha=0.7, 
                     label='Communality (h²)', color='blue')
        axes[0,1].bar(range(len(uniquenesses)), uniquenesses, 
                     bottom=communalities, alpha=0.7, 
                     label='Uniqueness (u²)', color='red')
        axes[0,1].set_title('Variance Decomposition by Variable')
        axes[0,1].set_xlabel('Variables')
        axes[0,1].set_ylabel('Proportion of Variance')
        axes[0,1].legend()
        axes[0,1].set_xticks(range(0, len(communalities), 2))
        
        # Plot 3: Scree plot
        eigenvalues = fa_results['PAF']['eigenvalues']
        all_eigenvalues, _ = FactorAnalyzer().fit(X).get_eigenvalues()
        
        axes[1,0].plot(range(1, len(all_eigenvalues)+1), all_eigenvalues, 'o-')
        axes[1,0].axhline(y=1, color='r', linestyle='--', label='Kaiser criterion')
        axes[1,0].axvline(x=self.n_factors, color='g', linestyle='--', 
                         label=f'Retained factors ({self.n_factors})')
        axes[1,0].set_title('Scree Plot')
        axes[1,0].set_xlabel('Factor Number')
        axes[1,0].set_ylabel('Eigenvalue')
        axes[1,0].legend()
        axes[1,0].grid(True, alpha=0.3)
        
        # Plot 4: Factor correlation matrix (identity for orthogonal)
        # For demonstration, show what correlations would look like
        factor_corr = np.eye(self.n_factors)  # Identity matrix for orthogonal factors
        im4 = axes[1,1].imshow(factor_corr, cmap='RdBu', vmin=-1, vmax=1)
        axes[1,1].set_title('Factor Correlation Matrix\n(Orthogonal Rotation)')
        axes[1,1].set_xticks(range(self.n_factors))
        axes[1,1].set_yticks(range(self.n_factors))
        axes[1,1].set_xticklabels([f'F{i+1}' for i in range(self.n_factors)])
        axes[1,1].set_yticklabels([f'F{i+1}' for i in range(self.n_factors)])
        
        # Add correlation values to cells
        for i in range(self.n_factors):
            for j in range(self.n_factors):
                axes[1,1].text(j, i, f'{factor_corr[i,j]:.1f}', 
                              ha='center', va='center', fontweight='bold')
        
        plt.colorbar(im4, ax=axes[1,1])
        plt.tight_layout()
        plt.show()
    
    def run_complete_analysis(self):
        """
        Run the complete factor analysis equations demonstration.
        """
        print("MA2003B - Factor Analysis: Mathematical Foundation and Equations")
        print("=" * 70)
        
        # Generate synthetic data
        X, F, Lambda, epsilon = self.generate_factor_data()
        
        # Demonstrate factor model
        self.demonstrate_factor_model(X, F, Lambda, epsilon)
        
        # Compare estimation methods
        fa_results = self.compare_estimation_methods(X)
        
        # Demonstrate communalities calculation
        self.demonstrate_communalities_calculation(fa_results)
        
        # Create visualizations
        self.visualize_factor_structure(X, fa_results)
        
        # Summary and conclusions
        print("\n" + "="*70)
        print("SUMMARY AND KEY TAKEAWAYS")
        print("="*70)
        print("1. The factor model X = ΛF + ε decomposes observed variables into:")
        print("   - Common variance (explained by factors)")
        print("   - Unique variance (specific + error)")
        print()
        print("2. Factor loadings (λᵢⱼ) represent correlations between variables and factors")
        print()
        print("3. Communalities (h²) show proportion of variance explained by factors:")
        print(f"   - Range: 0 to 1")
        print(f"   - Higher values indicate better factor representation")
        print()
        print("4. Different estimation methods (PAF vs ML) can yield similar results")
        print("   when assumptions are met")
        print()
        print("5. Understanding these equations is crucial for:")
        print("   - Interpreting factor analysis results")
        print("   - Assessing model adequacy")
        print("   - Making decisions about number of factors")

def main():
    """Main execution function."""
    logger.info("Starting Factor Analysis Equations Practice")
    
    # Initialize the analysis
    equations_demo = FactorAnalysisEquations(
        n_samples=300,
        n_features=12, 
        n_factors=3,
        random_state=42
    )
    
    # Run complete analysis
    equations_demo.run_complete_analysis()
    
    logger.info("Factor Analysis Equations Practice completed")

if __name__ == "__main__":
    main()