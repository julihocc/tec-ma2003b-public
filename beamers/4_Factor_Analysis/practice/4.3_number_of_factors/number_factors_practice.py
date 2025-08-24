"""
MA2003B - Factor Analysis Practice: Choosing Number of Factors

Topic 4.3: Determining the appropriate number of factors using multiple criteria

Learning Objectives:
- Apply Kaiser criterion (eigenvalue > 1) and understand its limitations
- Create and interpret scree plots for factor retention
- Implement and understand parallel analysis procedure
- Use goodness-of-fit measures to guide factor retention decisions
- Compare multiple approaches and make informed decisions

Author: Dr. Juliho Castillo
Institution: Tec de Monterrey
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from scipy.stats import chi2
from utils import setup_logger

# Configure logging
logger = setup_logger(__name__)

class FactorRetentionAnalysis:
    """
    Comprehensive analysis of factor retention methods including Kaiser criterion,
    scree plot, parallel analysis, and goodness-of-fit measures.
    """
    
    def __init__(self, random_state=42):
        """
        Initialize factor retention analysis.
        
        Args:
            random_state: Random seed for reproducibility
        """
        self.random_state = random_state
        logger.info("Initialized FactorRetentionAnalysis")
    
    def generate_test_datasets(self):
        """
        Generate multiple test datasets with different factor structures.
        
        Returns:
            dict: Dictionary containing different test datasets
        """
        np.random.seed(self.random_state)
        datasets = {}
        
        # Dataset 1: Clear 3-factor structure
        print("Generating Test Datasets...")
        print("=" * 50)
        
        # Create 3-factor structure with high loadings
        n_samples = 250
        n_vars_per_factor = 4
        n_factors = 3
        n_total_vars = n_vars_per_factor * n_factors
        
        # Generate factor scores
        factors = np.random.normal(0, 1, (n_samples, n_factors))
        
        # Create loading matrix with clear structure
        loadings = np.zeros((n_total_vars, n_factors))
        for i in range(n_factors):
            start_idx = i * n_vars_per_factor
            end_idx = (i + 1) * n_vars_per_factor
            loadings[start_idx:end_idx, i] = np.random.uniform(0.7, 0.9, n_vars_per_factor)
        
        # Add some cross-loadings
        for i in range(n_total_vars):
            for j in range(n_factors):
                if loadings[i, j] == 0:
                    if np.random.random() < 0.3:  # 30% chance of small cross-loading
                        loadings[i, j] = np.random.uniform(0.1, 0.3)
        
        # Generate unique factors
        uniqueness = np.random.uniform(0.2, 0.5, n_total_vars)
        unique_factors = np.random.normal(0, 1, (n_samples, n_total_vars)) * np.sqrt(uniqueness)
        
        # Generate observed variables: X = ΛF + ε
        X_clear = factors @ loadings.T + unique_factors
        X_clear = StandardScaler().fit_transform(X_clear)
        
        datasets['clear_structure'] = {
            'data': X_clear,
            'true_factors': 3,
            'description': 'Clear 3-factor structure',
            'variables': [f'Var_{i+1:02d}' for i in range(n_total_vars)]
        }
        
        # Dataset 2: Ambiguous structure (could be 2 or 4 factors)
        n_factors_ambiguous = 4
        factors_amb = np.random.normal(0, 1, (n_samples, n_factors_ambiguous))
        
        # Create more complex loading pattern
        loadings_amb = np.random.uniform(0.3, 0.8, (12, n_factors_ambiguous))
        # Make some factors weaker
        loadings_amb[:, 2] *= 0.6  # Weaker third factor
        loadings_amb[:, 3] *= 0.5  # Very weak fourth factor
        
        uniqueness_amb = np.random.uniform(0.3, 0.7, 12)
        unique_factors_amb = np.random.normal(0, 1, (n_samples, 12)) * np.sqrt(uniqueness_amb)
        
        X_ambiguous = factors_amb @ loadings_amb.T + unique_factors_amb
        X_ambiguous = StandardScaler().fit_transform(X_ambiguous)
        
        datasets['ambiguous_structure'] = {
            'data': X_ambiguous,
            'true_factors': 2,  # True underlying factors, despite 4 in generation
            'description': 'Ambiguous structure (2 vs 4 factors)',
            'variables': [f'Item_{i+1:02d}' for i in range(12)]
        }
        
        print(f"Generated {len(datasets)} test datasets")
        for name, dataset in datasets.items():
            print(f"  {dataset['description']}: {dataset['data'].shape}")
        print()
        
        return datasets
    
    def apply_kaiser_criterion(self, data, dataset_name):
        """
        Apply Kaiser criterion (eigenvalue > 1) for factor retention.
        
        Args:
            data: Data matrix
            dataset_name: Name of dataset for reporting
            
        Returns:
            dict: Kaiser criterion results
        """
        print(f"Kaiser Criterion Analysis - {dataset_name}")
        print("-" * 40)
        
        # Get eigenvalues
        fa_temp = FactorAnalyzer()
        fa_temp.fit(data)
        eigenvalues, _ = fa_temp.get_eigenvalues()
        
        # Apply Kaiser criterion
        n_factors_kaiser = np.sum(eigenvalues > 1.0)
        
        print(f"Eigenvalues:")
        for i, eigenval in enumerate(eigenvalues[:8]):  # Show first 8
            status = "RETAIN" if eigenval > 1.0 else "drop"
            print(f"  Factor {i+1:2d}: {eigenval:6.3f} ({status})")
        
        if len(eigenvalues) > 8:
            print(f"  ... and {len(eigenvalues)-8} more factors with eigenvalues < 1.0")
        
        print(f"\nKaiser Criterion Result: {n_factors_kaiser} factors")
        print(f"Total variance explained by retained factors: {np.sum(eigenvalues[:n_factors_kaiser]):.3f}")
        print(f"Percentage of variance explained: {100 * np.sum(eigenvalues[:n_factors_kaiser]) / len(eigenvalues):.1f}%")
        print()
        
        return {
            'n_factors': n_factors_kaiser,
            'eigenvalues': eigenvalues,
            'variance_explained': np.sum(eigenvalues[:n_factors_kaiser])
        }
    
    def create_scree_plot_analysis(self, data, dataset_name, true_factors=None):
        """
        Create and analyze scree plot for factor retention.
        
        Args:
            data: Data matrix
            dataset_name: Name of dataset
            true_factors: True number of factors (if known)
            
        Returns:
            dict: Scree plot analysis results
        """
        print(f"Scree Plot Analysis - {dataset_name}")
        print("-" * 40)
        
        # Get eigenvalues
        fa_temp = FactorAnalyzer()
        fa_temp.fit(data)
        eigenvalues, _ = fa_temp.get_eigenvalues()
        
        # Create scree plot
        plt.figure(figsize=(12, 8))
        
        # Main scree plot
        plt.subplot(2, 2, 1)
        factors_range = range(1, min(len(eigenvalues) + 1, 16))  # Show up to 15 factors
        plt.plot(factors_range, eigenvalues[:15], 'bo-', linewidth=2, markersize=8)
        plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Kaiser criterion')
        
        if true_factors:
            plt.axvline(x=true_factors, color='green', linestyle='--', alpha=0.7, 
                       label=f'True factors ({true_factors})')
        
        plt.title(f'Scree Plot - {dataset_name}')
        plt.xlabel('Factor Number')
        plt.ylabel('Eigenvalue')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Zoomed scree plot (first 8 factors)
        plt.subplot(2, 2, 2)
        plt.plot(range(1, 9), eigenvalues[:8], 'bo-', linewidth=2, markersize=8)
        plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Kaiser criterion')
        
        if true_factors and true_factors <= 8:
            plt.axvline(x=true_factors, color='green', linestyle='--', alpha=0.7, 
                       label=f'True factors ({true_factors})')
        
        plt.title('Scree Plot - Detail View (First 8 Factors)')
        plt.xlabel('Factor Number')
        plt.ylabel('Eigenvalue')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Differences plot (to identify elbow more clearly)
        plt.subplot(2, 2, 3)
        differences = np.diff(eigenvalues[:10])
        plt.plot(range(1, len(differences)+1), differences, 'ro-', linewidth=2, markersize=8)
        plt.title('Eigenvalue Differences (Elbow Detection)')
        plt.xlabel('Factor Number')
        plt.ylabel('Eigenvalue Difference')
        plt.grid(True, alpha=0.3)
        
        # Cumulative variance explained
        plt.subplot(2, 2, 4)
        cumulative_var = np.cumsum(eigenvalues[:10]) / np.sum(eigenvalues) * 100
        plt.plot(range(1, len(cumulative_var)+1), cumulative_var, 'go-', linewidth=2, markersize=8)
        plt.axhline(y=70, color='orange', linestyle='--', alpha=0.7, label='70% variance')
        plt.axhline(y=80, color='red', linestyle='--', alpha=0.7, label='80% variance')
        plt.title('Cumulative Variance Explained')
        plt.xlabel('Factor Number')
        plt.ylabel('Cumulative Variance (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Identify potential elbow points
        differences = np.diff(eigenvalues[:8])
        max_diff_idx = np.argmax(differences) + 1  # +1 because diff reduces length by 1
        
        print(f"Scree Plot Analysis:")
        print(f"  Largest eigenvalue drop: Between factor {max_diff_idx} and {max_diff_idx+1}")
        print(f"  Drop magnitude: {differences[max_diff_idx-1]:.3f}")
        print(f"  Suggested factors (visual elbow): {max_diff_idx}")
        print(f"  Factors for 70% variance: {np.argmax(cumulative_var >= 70) + 1}")
        print(f"  Factors for 80% variance: {np.argmax(cumulative_var >= 80) + 1}")
        print()
        
        return {
            'suggested_factors': max_diff_idx,
            'eigenvalues': eigenvalues,
            'differences': differences,
            'cumulative_variance': cumulative_var
        }
    
    def parallel_analysis(self, data, dataset_name, n_iterations=1000):
        """
        Perform Horn's parallel analysis for factor retention.
        
        Args:
            data: Data matrix
            dataset_name: Name of dataset
            n_iterations: Number of random datasets to generate
            
        Returns:
            dict: Parallel analysis results
        """
        print(f"Parallel Analysis - {dataset_name}")
        print("-" * 40)
        
        n_samples, n_variables = data.shape
        
        # Get eigenvalues from real data
        fa_real = FactorAnalyzer()
        fa_real.fit(data)
        real_eigenvalues, _ = fa_real.get_eigenvalues()
        
        # Generate random datasets and compute eigenvalues
        random_eigenvalues = []
        
        print(f"Generating {n_iterations} random datasets... ", end="")
        
        for i in range(n_iterations):
            if (i + 1) % 100 == 0:
                print(f"{i+1}...", end="")
            
            # Generate random normal data with same dimensions
            random_data = np.random.normal(0, 1, (n_samples, n_variables))
            
            # Compute eigenvalues
            fa_random = FactorAnalyzer()
            fa_random.fit(random_data)
            random_eigenvals, _ = fa_random.get_eigenvalues()
            random_eigenvalues.append(random_eigenvals)
        
        print(" Done!")
        
        # Calculate percentile eigenvalues from random data
        random_eigenvalues = np.array(random_eigenvalues)
        mean_random_eigenvalues = np.mean(random_eigenvalues, axis=0)
        percentile_95_eigenvalues = np.percentile(random_eigenvalues, 95, axis=0)
        
        # Apply parallel analysis criterion
        n_factors_parallel = np.sum(real_eigenvalues > percentile_95_eigenvalues)
        
        # Results table
        print(f"\nParallel Analysis Results:")
        print(f"{'Factor':<8} {'Real Data':<12} {'Random Mean':<12} {'Random 95%':<12} {'Decision':<10}")
        print("-" * 60)
        
        decisions = []
        for i in range(min(10, len(real_eigenvalues))):  # Show first 10
            real_eigen = real_eigenvalues[i]
            random_mean = mean_random_eigenvalues[i]
            random_95 = percentile_95_eigenvalues[i]
            decision = "RETAIN" if real_eigen > random_95 else "drop"
            decisions.append(decision)
            
            print(f"{i+1:<8} {real_eigen:<12.3f} {random_mean:<12.3f} {random_95:<12.3f} {decision:<10}")
        
        print(f"\nParallel Analysis Result: {n_factors_parallel} factors")
        print(f"(Factors where real eigenvalue > 95th percentile of random eigenvalues)")
        
        # Create visualization
        plt.figure(figsize=(12, 6))
        
        # Plot comparison
        plt.subplot(1, 2, 1)
        factors_range = range(1, min(len(real_eigenvalues) + 1, 11))  # First 10 factors
        
        plt.plot(factors_range, real_eigenvalues[:10], 'bo-', linewidth=2, 
                label='Real Data', markersize=8)
        plt.plot(factors_range, mean_random_eigenvalues[:10], 'ro-', linewidth=2, 
                label='Random Data (Mean)', markersize=8)
        plt.plot(factors_range, percentile_95_eigenvalues[:10], 'r--', linewidth=2, 
                label='Random Data (95th %ile)', alpha=0.7)
        
        plt.axvline(x=n_factors_parallel, color='green', linestyle=':', linewidth=3,
                   label=f'Parallel Analysis ({n_factors_parallel} factors)')
        
        plt.title('Parallel Analysis')
        plt.xlabel('Factor Number')
        plt.ylabel('Eigenvalue')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Distribution of first eigenvalue from random data
        plt.subplot(1, 2, 2)
        plt.hist(random_eigenvalues[:, 0], bins=30, alpha=0.7, color='red', 
                label='Random Data 1st Eigenvalue')
        plt.axvline(x=real_eigenvalues[0], color='blue', linewidth=3, 
                   label=f'Real Data 1st Eigenvalue ({real_eigenvalues[0]:.3f})')
        plt.axvline(x=percentile_95_eigenvalues[0], color='orange', linewidth=2,
                   label=f'95th Percentile ({percentile_95_eigenvalues[0]:.3f})')
        
        plt.title('Distribution of 1st Eigenvalue (Random Data)')
        plt.xlabel('Eigenvalue')
        plt.ylabel('Frequency')
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        print()
        
        return {
            'n_factors': n_factors_parallel,
            'real_eigenvalues': real_eigenvalues,
            'random_mean_eigenvalues': mean_random_eigenvalues,
            'random_95_percentile': percentile_95_eigenvalues
        }
    
    def goodness_of_fit_analysis(self, data, dataset_name, max_factors=6):
        """
        Analyze goodness-of-fit measures for different numbers of factors.
        
        Args:
            data: Data matrix
            dataset_name: Name of dataset
            max_factors: Maximum number of factors to test
            
        Returns:
            dict: Goodness-of-fit results
        """
        print(f"Goodness-of-Fit Analysis - {dataset_name}")
        print("-" * 40)
        
        n_samples, n_variables = data.shape
        fit_results = []
        
        print(f"Testing 1 to {max_factors} factors...")
        print(f"{'Factors':<8} {'Chi-square':<12} {'df':<6} {'p-value':<10} {'RMSEA':<8} {'CFI':<8}")
        print("-" * 60)
        
        for n_factors in range(1, max_factors + 1):
            try:
                # Fit factor analysis with ML estimation
                fa = FactorAnalyzer(n_factors=n_factors, method='ml', rotation='varimax')
                fa.fit(data)
                
                # Calculate degrees of freedom
                df = (n_variables * (n_variables - 1) // 2) - (n_variables * n_factors) + (n_factors * (n_factors - 1) // 2)
                
                # Get chi-square (for ML estimation, this would be available)
                # Note: factor_analyzer doesn't directly provide chi-square
                # This is a simplified implementation
                
                # Calculate reproduced correlations
                loadings = fa.loadings_
                reproduced_corr = loadings @ loadings.T
                np.fill_diagonal(reproduced_corr, 1.0)
                
                # Original correlation matrix
                original_corr = np.corrcoef(data.T)
                
                # Calculate residuals
                residuals = original_corr - reproduced_corr
                residuals_off_diag = residuals[np.triu_indices_from(residuals, k=1)]
                
                # Simplified fit measures (approximations)
                chi_square = n_samples * np.sum(residuals_off_diag**2)  # Simplified
                p_value = 1 - chi2.cdf(chi_square, df) if df > 0 else np.nan
                
                # RMSEA approximation
                rmsea = np.sqrt(max(0, (chi_square - df) / (df * (n_samples - 1)))) if df > 0 else np.nan
                
                # CFI approximation (simplified)
                baseline_chi_square = n_samples * np.sum(np.triu(original_corr, k=1)**2)
                cfi = 1 - max(0, chi_square - df) / max(baseline_chi_square - (n_variables * (n_variables - 1) // 2), 1)
                
                fit_results.append({
                    'n_factors': n_factors,
                    'chi_square': chi_square,
                    'df': df,
                    'p_value': p_value,
                    'rmsea': rmsea,
                    'cfi': cfi,
                    'residual_rmsr': np.sqrt(np.mean(residuals_off_diag**2))
                })
                
                print(f"{n_factors:<8} {chi_square:<12.2f} {df:<6} {p_value:<10.3f} {rmsea:<8.3f} {cfi:<8.3f}")
                
            except Exception as e:
                print(f"{n_factors:<8} Error: {str(e)}")
                continue
        
        if fit_results:
            # Plot fit indices
            plt.figure(figsize=(15, 5))
            
            factors = [r['n_factors'] for r in fit_results]
            
            # Plot 1: Chi-square and p-values
            plt.subplot(1, 3, 1)
            chi_squares = [r['chi_square'] for r in fit_results]
            p_values = [r['p_value'] for r in fit_results if not np.isnan(r['p_value'])]
            
            plt.plot(factors, chi_squares, 'bo-', linewidth=2, label='Chi-square')
            plt.title('Chi-square Test')
            plt.xlabel('Number of Factors')
            plt.ylabel('Chi-square')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            # Plot 2: RMSEA
            plt.subplot(1, 3, 2)
            rmseas = [r['rmsea'] for r in fit_results if not np.isnan(r['rmsea'])]
            factors_rmsea = [r['n_factors'] for r in fit_results if not np.isnan(r['rmsea'])]
            
            if rmseas:
                plt.plot(factors_rmsea, rmseas, 'ro-', linewidth=2, label='RMSEA')
                plt.axhline(y=0.05, color='green', linestyle='--', label='Good fit (<0.05)')
                plt.axhline(y=0.08, color='orange', linestyle='--', label='Adequate fit (<0.08)')
                plt.axhline(y=0.10, color='red', linestyle='--', label='Poor fit (>0.10)')
            
            plt.title('RMSEA (Root Mean Square Error of Approximation)')
            plt.xlabel('Number of Factors')
            plt.ylabel('RMSEA')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            # Plot 3: CFI
            plt.subplot(1, 3, 3)
            cfis = [r['cfi'] for r in fit_results if not np.isnan(r['cfi'])]
            factors_cfi = [r['n_factors'] for r in fit_results if not np.isnan(r['cfi'])]
            
            if cfis:
                plt.plot(factors_cfi, cfis, 'go-', linewidth=2, label='CFI')
                plt.axhline(y=0.95, color='green', linestyle='--', label='Good fit (>0.95)')
                plt.axhline(y=0.90, color='orange', linestyle='--', label='Adequate fit (>0.90)')
            
            plt.title('CFI (Comparative Fit Index)')
            plt.xlabel('Number of Factors')
            plt.ylabel('CFI')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.show()
        
        print("\nFit Index Interpretation:")
        print("  Chi-square: Lower is better, non-significant preferred")
        print("  RMSEA: <0.05 good, <0.08 adequate, >0.10 poor")
        print("  CFI: >0.95 good, >0.90 adequate")
        print()
        
        return fit_results
    
    def comprehensive_comparison(self, dataset, dataset_name):
        """
        Perform comprehensive factor retention analysis using all methods.
        
        Args:
            dataset: Dataset dictionary containing data and metadata
            dataset_name: Name of dataset
        """
        data = dataset['data']
        true_factors = dataset.get('true_factors')
        
        print("="*80)
        print(f"COMPREHENSIVE FACTOR RETENTION ANALYSIS: {dataset['description']}")
        print("="*80)
        print(f"Dataset: {dataset_name}")
        print(f"Dimensions: {data.shape}")
        if true_factors:
            print(f"True number of factors: {true_factors}")
        print()
        
        # Apply all methods
        kaiser_results = self.apply_kaiser_criterion(data, dataset_name)
        scree_results = self.create_scree_plot_analysis(data, dataset_name, true_factors)
        parallel_results = self.parallel_analysis(data, dataset_name, n_iterations=500)
        fit_results = self.goodness_of_fit_analysis(data, dataset_name, max_factors=6)
        
        # Summary comparison
        print("="*50)
        print("FACTOR RETENTION SUMMARY")
        print("="*50)
        
        methods_summary = {
            'Kaiser Criterion': kaiser_results['n_factors'],
            'Scree Plot (Visual)': scree_results['suggested_factors'],
            'Parallel Analysis': parallel_results['n_factors']
        }
        
        if true_factors:
            methods_summary['True Factors'] = true_factors
        
        print("Method Recommendations:")
        for method, n_factors in methods_summary.items():
            status = "✓" if method == 'True Factors' else ""
            print(f"  {method:<20}: {n_factors} factors {status}")
        
        print()
        
        # Best fit from goodness-of-fit
        if fit_results:
            # Find model with best RMSEA (if available)
            valid_fits = [r for r in fit_results if not np.isnan(r['rmsea']) and r['rmsea'] < 0.08]
            if valid_fits:
                best_rmsea = min(valid_fits, key=lambda x: x['rmsea'])
                print(f"  Best fit (RMSEA)     : {best_rmsea['n_factors']} factors (RMSEA = {best_rmsea['rmsea']:.3f})")
            
            # Find model with best CFI (if available)
            valid_cfis = [r for r in fit_results if not np.isnan(r['cfi']) and r['cfi'] > 0.90]
            if valid_cfis:
                best_cfi = max(valid_cfis, key=lambda x: x['cfi'])
                print(f"  Best fit (CFI)       : {best_cfi['n_factors']} factors (CFI = {best_cfi['cfi']:.3f})")
        
        # Recommendations
        print("\nRecommendations:")
        
        # Count votes for each number of factors
        votes = {}
        for method, n_factors in methods_summary.items():
            if method != 'True Factors':
                votes[n_factors] = votes.get(n_factors, 0) + 1
        
        if votes:
            most_common = max(votes.items(), key=lambda x: x[1])
            print(f"  Most commonly suggested: {most_common[0]} factors ({most_common[1]} methods)")
        
        # Practical recommendations
        print(f"  Conservative approach: Use parallel analysis result ({parallel_results['n_factors']} factors)")
        print(f"  Liberal approach: Use Kaiser criterion result ({kaiser_results['n_factors']} factors)")
        
        if true_factors:
            print(f"  Accuracy assessment:")
            for method, n_factors in methods_summary.items():
                if method != 'True Factors':
                    accuracy = "Exact" if n_factors == true_factors else f"Off by {abs(n_factors - true_factors)}"
                    print(f"    {method:<20}: {accuracy}")
        
        print()
        return {
            'kaiser': kaiser_results,
            'scree': scree_results, 
            'parallel': parallel_results,
            'fit': fit_results,
            'summary': methods_summary
        }
    
    def run_complete_analysis(self):
        """
        Run complete factor retention analysis on multiple datasets.
        """
        print("MA2003B - Factor Analysis: Choosing the Number of Factors")
        print("=" * 70)
        
        # Generate test datasets
        datasets = self.generate_test_datasets()
        
        results = {}
        
        # Analyze each dataset
        for dataset_name, dataset in datasets.items():
            results[dataset_name] = self.comprehensive_comparison(dataset, dataset_name)
        
        # Final summary and recommendations
        print("="*80)
        print("OVERALL CONCLUSIONS AND BEST PRACTICES")
        print("="*80)
        
        print("1. METHOD RELIABILITY:")
        print("   - Parallel Analysis: Most reliable, accounts for chance")
        print("   - Scree Plot: Good visual method, requires experience")
        print("   - Kaiser Criterion: Simple but often over-extracts")
        print("   - Fit Indices: Useful with ML estimation, complex interpretation")
        print()
        
        print("2. DECISION STRATEGY:")
        print("   - Use multiple methods for triangulation")
        print("   - Parallel analysis as primary criterion")
        print("   - Consider theoretical meaningfulness")
        print("   - Evaluate interpretability of solutions")
        print()
        
        print("3. SAMPLE SIZE CONSIDERATIONS:")
        print("   - n < 100: Parallel analysis most reliable")
        print("   - n > 250: Most methods work well")
        print("   - Large n: Kaiser criterion more accurate")
        print()
        
        print("4. PRACTICAL GUIDELINES:")
        print("   - Start with parallel analysis")
        print("   - Examine scree plot for obvious breaks")
        print("   - Test neighboring solutions (n ± 1 factors)")
        print("   - Choose most interpretable solution")
        print("   - Document decision rationale")

def main():
    """Main execution function."""
    logger.info("Starting Factor Retention Analysis Practice")
    
    # Initialize analysis
    retention_analysis = FactorRetentionAnalysis(random_state=42)
    
    # Run complete analysis
    retention_analysis.run_complete_analysis()
    
    logger.info("Factor Retention Analysis Practice completed")

if __name__ == "__main__":
    main()