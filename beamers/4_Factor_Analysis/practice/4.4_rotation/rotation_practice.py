"""
MA2003B - Factor Analysis Practice: Factor Rotation Methods

Topic 4.4: Understanding and applying orthogonal rotation techniques

Learning Objectives:
- Understand why rotation improves factor interpretability
- Apply and compare Varimax, Quartimax, and Equimax rotation
- Implement rotation algorithms from mathematical principles
- Evaluate rotated solutions for simple structure
- Visualize factor patterns before and after rotation

Author: Dr. Juliho Castillo
Institution: Tec de Monterrey
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import minimize_scalar
from utils import setup_logger

# Configure logging
logger = setup_logger(__name__)

class FactorRotationAnalysis:
    """
    Comprehensive analysis of orthogonal factor rotation methods including
    implementation of rotation algorithms and visualization of results.
    """
    
    def __init__(self, random_state=42):
        """
        Initialize factor rotation analysis.
        
        Args:
            random_state: Random seed for reproducibility
        """
        self.random_state = random_state
        logger.info("Initialized FactorRotationAnalysis")
    
    def generate_rotation_example_data(self):
        """
        Generate data specifically designed to demonstrate rotation benefits.
        
        Returns:
            tuple: (data, true_structure_info)
        """
        np.random.seed(self.random_state)
        
        print("Generating Factor Rotation Example Data...")
        print("=" * 50)
        
        n_samples = 300
        n_factors = 3
        
        # Create clear factor structure for demonstration
        # Factor 1: Academic performance items (math, reading, science, writing)
        # Factor 2: Social skills items (leadership, teamwork, communication, empathy)  
        # Factor 3: Physical skills items (strength, coordination, endurance, flexibility)
        
        variable_names = [
            'Mathematics', 'Reading', 'Science', 'Writing',           # Academic (Factor 1)
            'Leadership', 'Teamwork', 'Communication', 'Empathy',    # Social (Factor 2)
            'Strength', 'Coordination', 'Endurance', 'Flexibility'   # Physical (Factor 3)
        ]
        
        # Generate factor scores
        factors = np.random.normal(0, 1, (n_samples, n_factors))
        
        # Create initial loading pattern that will benefit from rotation
        # Start with oblique pattern, then rotate to make interpretation difficult
        loadings_clean = np.array([
            # Academic items load primarily on Factor 1
            [0.80, 0.10, 0.05],  # Mathematics
            [0.75, 0.15, 0.10],  # Reading
            [0.70, 0.20, 0.15],  # Science
            [0.65, 0.25, 0.10],  # Writing
            
            # Social items load primarily on Factor 2
            [0.15, 0.80, 0.10],  # Leadership
            [0.20, 0.75, 0.05],  # Teamwork
            [0.10, 0.70, 0.15],  # Communication
            [0.25, 0.65, 0.20],  # Empathy
            
            # Physical items load primarily on Factor 3
            [0.10, 0.15, 0.75],  # Strength
            [0.05, 0.20, 0.80],  # Coordination
            [0.15, 0.10, 0.70],  # Endurance
            [0.20, 0.25, 0.65],  # Flexibility
        ])
        
        # Rotate this clean structure to create a more complex initial solution
        # This simulates what we typically get from initial extraction
        rotation_angle = np.pi / 6  # 30 degrees
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle), 0],
            [np.sin(rotation_angle), np.cos(rotation_angle), 0],
            [0, 0, 1]
        ])
        
        # Create initial "complex" loadings
        loadings_complex = loadings_clean @ rotation_matrix.T
        
        # Add some noise to make it more realistic
        noise = np.random.normal(0, 0.1, loadings_complex.shape)
        loadings_complex += noise
        
        # Generate unique factors
        uniqueness = np.random.uniform(0.2, 0.4, len(variable_names))
        unique_factors = np.random.normal(0, 1, (n_samples, len(variable_names))) * np.sqrt(uniqueness)
        
        # Generate observed data: X = ΛF + ε
        X = factors @ loadings_complex.T + unique_factors
        X = StandardScaler().fit_transform(X)
        
        structure_info = {
            'variable_names': variable_names,
            'true_factors': ['Academic', 'Social', 'Physical'],
            'factor_assignments': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
            'clean_loadings': loadings_clean,
            'complex_loadings': loadings_complex
        }
        
        print(f"Generated {n_samples} samples with {len(variable_names)} variables")
        print(f"True factor structure: {n_factors} factors")
        print(f"Variables per factor: {[variable_names[i*4:(i+1)*4] for i in range(n_factors)]}")
        print()
        
        return X, structure_info
    
    def demonstrate_unrotated_solution(self, data, variable_names):
        """
        Show the unrotated factor solution and its interpretation challenges.
        
        Args:
            data: Data matrix
            variable_names: List of variable names
            
        Returns:
            FactorAnalyzer: Fitted unrotated model
        """
        print("UNROTATED FACTOR SOLUTION")
        print("=" * 40)
        
        # Fit unrotated factor analysis
        fa_unrotated = FactorAnalyzer(n_factors=3, rotation=None, method='principal')
        fa_unrotated.fit(data)
        
        loadings_unrot = fa_unrotated.loadings_
        
        # Display unrotated loadings
        loadings_df = pd.DataFrame(
            loadings_unrot,
            columns=['Factor 1', 'Factor 2', 'Factor 3'],
            index=variable_names
        )
        
        print("Unrotated Factor Loadings:")
        print(loadings_df.round(3))
        print()
        
        # Calculate complexity (number of substantial loadings per variable)
        complexity_scores = np.sum(np.abs(loadings_unrot) > 0.4, axis=1)
        
        print("Interpretation Challenges:")
        print(f"  Variables with multiple high loadings (>0.4): {np.sum(complexity_scores > 1)}")
        print(f"  Average complexity score: {np.mean(complexity_scores):.2f}")
        print(f"  Variables hard to interpret (loading on 2+ factors):")
        
        for i, (var, complexity) in enumerate(zip(variable_names, complexity_scores)):
            if complexity > 1:
                high_loadings = [f"F{j+1}({loadings_unrot[i,j]:.2f})" 
                               for j in range(3) if abs(loadings_unrot[i,j]) > 0.4]
                print(f"    {var}: {', '.join(high_loadings)}")
        
        print()
        return fa_unrotated
    
    def apply_varimax_rotation(self, data, variable_names):
        """
        Apply Varimax rotation and demonstrate its effects.
        
        Args:
            data: Data matrix
            variable_names: List of variable names
            
        Returns:
            FactorAnalyzer: Fitted Varimax rotated model
        """
        print("VARIMAX ROTATION")
        print("=" * 40)
        
        # Fit Varimax rotated factor analysis
        fa_varimax = FactorAnalyzer(n_factors=3, rotation='varimax', method='principal')
        fa_varimax.fit(data)
        
        loadings_varimax = fa_varimax.loadings_
        
        # Display Varimax loadings
        loadings_df = pd.DataFrame(
            loadings_varimax,
            columns=['Factor 1', 'Factor 2', 'Factor 3'],
            index=variable_names
        )
        
        print("Varimax Rotated Factor Loadings:")
        print(loadings_df.round(3))
        print()
        
        # Analyze simple structure achievement
        # Count high loadings per factor
        high_loadings_per_factor = np.sum(np.abs(loadings_varimax) > 0.5, axis=0)
        
        # Count variables with single high loading
        complexity_scores = np.sum(np.abs(loadings_varimax) > 0.4, axis=1)
        simple_variables = np.sum(complexity_scores == 1)
        
        print("Simple Structure Analysis:")
        print(f"  High loadings (>0.5) per factor: {high_loadings_per_factor}")
        print(f"  Variables with single high loading: {simple_variables}/{len(variable_names)}")
        print(f"  Simple structure achievement: {100*simple_variables/len(variable_names):.1f}%")
        print()
        
        # Factor interpretation
        print("Factor Interpretation (variables with |loading| > 0.5):")
        for factor in range(3):
            high_loading_vars = [variable_names[i] for i in range(len(variable_names)) 
                               if abs(loadings_varimax[i, factor]) > 0.5]
            print(f"  Factor {factor+1}: {', '.join(high_loading_vars)}")
        
        print()
        return fa_varimax
    
    def apply_quartimax_rotation(self, data, variable_names):
        """
        Apply Quartimax rotation for comparison.
        
        Args:
            data: Data matrix  
            variable_names: List of variable names
            
        Returns:
            FactorAnalyzer: Fitted Quartimax rotated model
        """
        print("QUARTIMAX ROTATION")
        print("=" * 40)
        
        # Fit Quartimax rotated factor analysis
        fa_quartimax = FactorAnalyzer(n_factors=3, rotation='quartimax', method='principal')
        fa_quartimax.fit(data)
        
        loadings_quartimax = fa_quartimax.loadings_
        
        # Display Quartimax loadings
        loadings_df = pd.DataFrame(
            loadings_quartimax,
            columns=['Factor 1', 'Factor 2', 'Factor 3'],
            index=variable_names
        )
        
        print("Quartimax Rotated Factor Loadings:")
        print(loadings_df.round(3))
        print()
        
        # Analyze for general factor tendency
        first_factor_dominance = np.mean(np.abs(loadings_quartimax[:, 0]))
        other_factors_dominance = np.mean(np.abs(loadings_quartimax[:, 1:]))
        
        print("Quartimax Characteristics:")
        print(f"  Average |loading| on Factor 1: {first_factor_dominance:.3f}")
        print(f"  Average |loading| on other factors: {other_factors_dominance:.3f}")
        
        if first_factor_dominance > other_factors_dominance * 1.2:
            print("  → Quartimax created a general factor (as expected)")
        else:
            print("  → No strong general factor emerged")
        
        print()
        return fa_quartimax
    
    def manual_varimax_implementation(self, unrotated_loadings):
        """
        Demonstrate manual implementation of Varimax rotation algorithm.
        
        Args:
            unrotated_loadings: Unrotated factor loadings matrix
            
        Returns:
            tuple: (rotated_loadings, rotation_matrix, iterations)
        """
        print("MANUAL VARIMAX IMPLEMENTATION")
        print("=" * 40)
        
        def varimax_criterion(loadings):
            """Calculate the Varimax criterion value."""
            n_vars, n_factors = loadings.shape
            criterion = 0
            for j in range(n_factors):
                loadings_j = loadings[:, j]
                criterion += np.var(loadings_j**2) * n_vars
            return criterion
        
        def rotate_two_factors(loadings, factor1_idx, factor2_idx):
            """Find optimal rotation angle for two factors."""
            A = loadings[:, factor1_idx]
            B = loadings[:, factor2_idx]
            
            # Calculate optimal rotation angle using Varimax formula
            def objective(phi):
                cos_phi, sin_phi = np.cos(phi), np.sin(phi)
                A_rot = A * cos_phi + B * sin_phi
                B_rot = -A * sin_phi + B * cos_phi
                
                # Negative because we want to maximize varimax (minimize negative)
                return -(np.var(A_rot**2) + np.var(B_rot**2))
            
            result = minimize_scalar(objective, bounds=(-np.pi/2, np.pi/2), method='bounded')
            optimal_angle = result.x
            
            return optimal_angle
        
        print("Implementing Varimax rotation algorithm...")
        
        loadings = unrotated_loadings.copy()
        n_vars, n_factors = loadings.shape
        rotation_matrix = np.eye(n_factors)
        
        max_iterations = 100
        tolerance = 1e-6
        iteration = 0
        
        print(f"{'Iter':<6} {'Varimax':<10} {'Max Angle':<12} {'Convergence'}")
        print("-" * 45)
        
        for iteration in range(max_iterations):
            old_criterion = varimax_criterion(loadings)
            max_angle = 0
            
            # Rotate each pair of factors
            for i in range(n_factors):
                for j in range(i + 1, n_factors):
                    # Find optimal rotation angle for factors i and j
                    angle = rotate_two_factors(loadings, i, j)
                    max_angle = max(max_angle, abs(angle))
                    
                    # Apply rotation if angle is significant
                    if abs(angle) > tolerance:
                        cos_angle, sin_angle = np.cos(angle), np.sin(angle)
                        
                        # Create rotation matrix
                        rotation = np.eye(n_factors)
                        rotation[i, i] = cos_angle
                        rotation[i, j] = sin_angle
                        rotation[j, i] = -sin_angle
                        rotation[j, j] = cos_angle
                        
                        # Apply rotation
                        loadings = loadings @ rotation
                        rotation_matrix = rotation_matrix @ rotation
            
            new_criterion = varimax_criterion(loadings)
            convergence = abs(new_criterion - old_criterion)
            
            print(f"{iteration+1:<6} {new_criterion:<10.4f} {max_angle:<12.6f} {convergence:<10.2e}")
            
            if max_angle < tolerance:
                print(f"\nConverged after {iteration+1} iterations")
                break
        
        if iteration == max_iterations - 1:
            print(f"\nReached maximum iterations ({max_iterations})")
        
        print(f"Final Varimax criterion value: {varimax_criterion(loadings):.4f}")
        print()
        
        return loadings, rotation_matrix, iteration + 1
    
    def compare_rotation_methods(self, data, variable_names):
        """
        Comprehensive comparison of different rotation methods.
        
        Args:
            data: Data matrix
            variable_names: List of variable names
        """
        print("COMPREHENSIVE ROTATION COMPARISON")
        print("=" * 50)
        
        rotation_methods = {
            'None (Unrotated)': None,
            'Varimax': 'varimax',
            'Quartimax': 'quartimax',
            'Equimax': 'equimax'
        }
        
        results = {}
        
        for method_name, rotation in rotation_methods.items():
            fa = FactorAnalyzer(n_factors=3, rotation=rotation, method='principal')
            fa.fit(data)
            
            loadings = fa.loadings_
            
            # Calculate interpretability metrics
            # 1. Number of high loadings (>0.5)
            high_loadings = np.sum(np.abs(loadings) > 0.5)
            
            # 2. Simple structure index (variables with single high loading)
            complexity_scores = np.sum(np.abs(loadings) > 0.4, axis=1)
            simple_structure = np.sum(complexity_scores == 1)
            
            # 3. Hyperplane count (loadings near zero)
            hyperplane_count = np.sum(np.abs(loadings) < 0.2)
            
            # 4. Maximum loading per variable
            max_loadings = np.max(np.abs(loadings), axis=1)
            
            results[method_name] = {
                'loadings': loadings,
                'high_loadings': high_loadings,
                'simple_structure': simple_structure,
                'hyperplane_count': hyperplane_count,
                'mean_max_loading': np.mean(max_loadings),
                'variance_explained': fa.get_eigenvalues()[0][:3] if rotation else fa.get_eigenvalues()[0][:3]
            }
        
        # Display comparison table
        print(f"{'Method':<15} {'High Load':<10} {'Simple':<8} {'Hyperpl':<10} {'Mean Max':<10}")
        print("-" * 60)
        
        for method_name, result in results.items():
            print(f"{method_name:<15} {result['high_loadings']:<10} "
                  f"{result['simple_structure']:<8} {result['hyperplane_count']:<10} "
                  f"{result['mean_max_loading']:<10.3f}")
        
        print()
        print("Interpretation:")
        print("  High Load: Number of loadings > 0.5 (more is better for clarity)")
        print("  Simple: Variables loading on single factor (more is better)")  
        print("  Hyperpl: Loadings near zero < 0.2 (more is better for simple structure)")
        print("  Mean Max: Average maximum loading per variable (higher is better)")
        print()
        
        return results
    
    def visualize_rotation_effects(self, data, variable_names, structure_info):
        """
        Visualize the effects of rotation on factor structure.
        
        Args:
            data: Data matrix
            variable_names: List of variable names
            structure_info: Information about true structure
        """
        # Get unrotated and rotated solutions
        fa_unrot = FactorAnalyzer(n_factors=3, rotation=None, method='principal')
        fa_unrot.fit(data)
        
        fa_varimax = FactorAnalyzer(n_factors=3, rotation='varimax', method='principal')
        fa_varimax.fit(data)
        
        # Create visualization
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        
        # Color mapping for true factor assignments
        factor_assignments = structure_info['factor_assignments']
        colors = ['red', 'blue', 'green']
        point_colors = [colors[assignment] for assignment in factor_assignments]
        
        # Plot 1: Unrotated Factor 1 vs Factor 2
        loadings_unrot = fa_unrot.loadings_
        axes[0, 0].scatter(loadings_unrot[:, 0], loadings_unrot[:, 1], c=point_colors, s=100, alpha=0.7)
        axes[0, 0].set_xlabel('Factor 1')
        axes[0, 0].set_ylabel('Factor 2')
        axes[0, 0].set_title('Unrotated: Factor 1 vs Factor 2')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[0, 0].axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Add variable labels
        for i, name in enumerate(variable_names):
            axes[0, 0].annotate(name[:4], (loadings_unrot[i, 0], loadings_unrot[i, 1]), 
                              xytext=(5, 5), textcoords='offset points', fontsize=8)
        
        # Plot 2: Rotated Factor 1 vs Factor 2
        loadings_varimax = fa_varimax.loadings_
        axes[0, 1].scatter(loadings_varimax[:, 0], loadings_varimax[:, 1], c=point_colors, s=100, alpha=0.7)
        axes[0, 1].set_xlabel('Factor 1')
        axes[0, 1].set_ylabel('Factor 2')
        axes[0, 1].set_title('Varimax: Factor 1 vs Factor 2')
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[0, 1].axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Add variable labels
        for i, name in enumerate(variable_names):
            axes[0, 1].annotate(name[:4], (loadings_varimax[i, 0], loadings_varimax[i, 1]), 
                              xytext=(5, 5), textcoords='offset points', fontsize=8)
        
        # Plot 3: Loading comparison for each variable
        x_pos = np.arange(len(variable_names))
        width = 0.35
        
        max_unrot = np.max(np.abs(loadings_unrot), axis=1)
        max_varimax = np.max(np.abs(loadings_varimax), axis=1)
        
        axes[0, 2].bar(x_pos - width/2, max_unrot, width, label='Unrotated', alpha=0.7)
        axes[0, 2].bar(x_pos + width/2, max_varimax, width, label='Varimax', alpha=0.7)
        axes[0, 2].set_xlabel('Variables')
        axes[0, 2].set_ylabel('Maximum |Loading|')
        axes[0, 2].set_title('Maximum Loading per Variable')
        axes[0, 2].set_xticks(x_pos)
        axes[0, 2].set_xticklabels([name[:4] for name in variable_names], rotation=45)
        axes[0, 2].legend()
        axes[0, 2].grid(True, alpha=0.3)
        
        # Plot 4: Complexity scores (bottom row, left)
        complexity_unrot = np.sum(np.abs(loadings_unrot) > 0.4, axis=1)
        complexity_varimax = np.sum(np.abs(loadings_varimax) > 0.4, axis=1)
        
        axes[1, 0].bar(x_pos - width/2, complexity_unrot, width, label='Unrotated', alpha=0.7)
        axes[1, 0].bar(x_pos + width/2, complexity_varimax, width, label='Varimax', alpha=0.7)
        axes[1, 0].set_xlabel('Variables')
        axes[1, 0].set_ylabel('Complexity Score')
        axes[1, 0].set_title('Variable Complexity (# factors > 0.4)')
        axes[1, 0].set_xticks(x_pos)
        axes[1, 0].set_xticklabels([name[:4] for name in variable_names], rotation=45)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Plot 5: Factor loadings heatmaps
        im1 = axes[1, 1].imshow(loadings_unrot.T, cmap='RdBu', aspect='auto', vmin=-1, vmax=1)
        axes[1, 1].set_title('Unrotated Loadings Heatmap')
        axes[1, 1].set_xlabel('Variables')
        axes[1, 1].set_ylabel('Factors')
        axes[1, 1].set_xticks(range(len(variable_names)))
        axes[1, 1].set_xticklabels([name[:4] for name in variable_names], rotation=45)
        axes[1, 1].set_yticks([0, 1, 2])
        axes[1, 1].set_yticklabels(['F1', 'F2', 'F3'])
        plt.colorbar(im1, ax=axes[1, 1])
        
        im2 = axes[1, 2].imshow(loadings_varimax.T, cmap='RdBu', aspect='auto', vmin=-1, vmax=1)
        axes[1, 2].set_title('Varimax Loadings Heatmap')
        axes[1, 2].set_xlabel('Variables')
        axes[1, 2].set_ylabel('Factors')
        axes[1, 2].set_xticks(range(len(variable_names)))
        axes[1, 2].set_xticklabels([name[:4] for name in variable_names], rotation=45)
        axes[1, 2].set_yticks([0, 1, 2])
        axes[1, 2].set_yticklabels(['F1', 'F2', 'F3'])
        plt.colorbar(im2, ax=axes[1, 2])
        
        # Add legend for colors
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], 
                                     markersize=10, label=structure_info['true_factors'][i]) 
                          for i in range(3)]
        axes[0, 0].legend(handles=legend_elements, loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def run_complete_analysis(self):
        """
        Run the complete factor rotation analysis demonstration.
        """
        print("MA2003B - Factor Analysis: Factor Rotation Methods")
        print("=" * 70)
        
        # Generate example data
        data, structure_info = self.generate_rotation_example_data()
        variable_names = structure_info['variable_names']
        
        # Demonstrate unrotated solution problems
        fa_unrotated = self.demonstrate_unrotated_solution(data, variable_names)
        
        # Apply different rotation methods
        fa_varimax = self.apply_varimax_rotation(data, variable_names)
        fa_quartimax = self.apply_quartimax_rotation(data, variable_names)
        
        # Manual Varimax implementation
        unrotated_loadings = fa_unrotated.loadings_
        manual_loadings, rotation_matrix, iterations = self.manual_varimax_implementation(unrotated_loadings)
        
        # Compare manual vs software implementation
        print("MANUAL vs SOFTWARE VARIMAX COMPARISON")
        print("=" * 45)
        software_loadings = fa_varimax.loadings_
        
        # Account for possible sign flips and factor reordering
        correlation_matrix = np.abs(np.corrcoef(manual_loadings.T, software_loadings.T)[:3, 3:])
        mean_correlation = np.mean(np.max(correlation_matrix, axis=1))
        
        print(f"Mean correlation between manual and software solutions: {mean_correlation:.4f}")
        print(f"(Should be close to 1.0 if implementations match)")
        print()
        
        # Comprehensive method comparison
        rotation_results = self.compare_rotation_methods(data, variable_names)
        
        # Visualizations
        self.visualize_rotation_effects(data, variable_names, structure_info)
        
        # Summary and conclusions
        print("="*70)
        print("SUMMARY AND KEY TAKEAWAYS")
        print("="*70)
        print("1. ROTATION PURPOSE:")
        print("   - Improves factor interpretability without changing fit")
        print("   - Redistributes variance among factors")
        print("   - Seeks 'simple structure' with clear variable-factor relationships")
        print()
        
        print("2. VARIMAX ROTATION:")
        print("   - Most popular orthogonal rotation method")
        print("   - Maximizes variance of squared loadings within factors")
        print("   - Produces factors with few high loadings and many near-zero loadings")
        print("   - Best for identifying distinct, uncorrelated factors")
        print()
        
        print("3. QUARTIMAX ROTATION:")
        print("   - Maximizes variance of squared loadings within variables")
        print("   - Tends to create a general factor")
        print("   - Less popular than Varimax")
        print("   - Useful when general factor is theoretically expected")
        print()
        
        print("4. ROTATION BENEFITS:")
        print("   - Clearer factor interpretation")
        print("   - Higher maximum loadings per variable")
        print("   - More variables with simple structure (single high loading)")
        print("   - Better alignment with theoretical expectations")
        print()
        
        print("5. PRACTICAL GUIDELINES:")
        print("   - Start with Varimax rotation for most applications")
        print("   - Compare multiple rotation methods")
        print("   - Evaluate interpretability and theoretical meaningfulness")
        print("   - Consider oblique rotation if factors might be correlated")
        print("   - Rotation preserves total variance and communalities")

def main():
    """Main execution function."""
    logger.info("Starting Factor Rotation Analysis Practice")
    
    # Initialize analysis
    rotation_analysis = FactorRotationAnalysis(random_state=42)
    
    # Run complete analysis
    rotation_analysis.run_complete_analysis()
    
    logger.info("Factor Rotation Analysis Practice completed")

if __name__ == "__main__":
    main()