# Synthetic Data PCA Example

## Overview

This example demonstrates Principal Component Analysis (PCA) using a carefully constructed synthetic dataset with known underlying factor structure. It serves as a pedagogical tool for understanding how PCA works when the ground truth is known, allowing students to validate whether the method successfully recovers the true latent factors.

## Files

- `pca_example.py` - Main PCA analysis script with detailed explanations and validation
- `pca_scree.png` - Scree plot for component selection and factor identification  
- `pca_biplot.png` - Biplot visualization showing observations and variable loadings
- `README.md` - This documentation file

## Synthetic Data Structure

The dataset contains **100 observations** across **5 variables** with a known 2-factor structure:

### True Factor Structure
- **Factor 1 (f1)**: Underlying latent factor driving variables 1-2
- **Factor 2 (f2)**: Independent latent factor driving variables 3-4  
- **Noise**: Random variation not explained by the factors

### Variable Definitions
1. **Var1_F1** - Strong loading on Factor 1 (0.9 × f1 + noise)
2. **Var2_F1** - Moderate loading on Factor 1 (0.8 × f1 + noise)
3. **Var3_F2** - Strong loading on Factor 2 (0.7 × f2 + noise)
4. **Var4_F2** - Moderate loading on Factor 2 (0.6 × f2 + noise)  
5. **Noise** - Pure random noise (no factor influence)

## Usage

```bash
# Run the PCA analysis (no data fetching needed - synthetic data generated internally)
python pca_example.py
```

## Expected Results

### Typical Output
- **Eigenvalues**: `[2.267, 1.501, 0.988, 0.258, 0.036]` (approximate)
- **Explained variance**: PC1 (~44.9%), PC2 (~29.7%), PC3 (~19.6%)  
- **Cumulative variance**: First 2 components explain ~74.6% of total variance

### Factor Recovery Validation

The script includes automatic validation of whether PCA correctly identified the known factor structure:

- **PC1** should primarily load on Var1_F1 and Var2_F1 (Factor 1 variables)
- **PC2** should primarily load on Var3_F2 and Var4_F2 (Factor 2 variables)
- **PC3-PC5** should mainly capture noise and measurement error
- The noise variable should have low loadings on the first two components

## Educational Value

This example illustrates key PCA concepts:

### Factor Recovery
- **Ground Truth Validation**: Unlike real data, we know the true underlying structure
- **Method Validation**: Demonstrates that PCA can recover latent factors when they exist  
- **Noise Separation**: Shows how PCA separates systematic variation from random noise

### Component Interpretation
- **Scree Plot**: Clear elbow after 2nd component, matching our 2-factor design
- **Kaiser Criterion**: Components 1-2 have eigenvalues > 1, components 3-5 do not
- **Loading Patterns**: Variable loadings reveal which factors drive each component

### Methodological Insights
- **Standardization Importance**: All variables standardized to prevent scale dominance
- **Variance Partitioning**: ~75% explained by 2 factors, ~25% by noise/error
- **Observation Rankings**: PC scores identify observations with extreme factor values

## Key Takeaways

### For Students
1. **PCA finds directions of maximum variance** that often correspond to meaningful latent factors
2. **Component selection** uses multiple criteria (scree plots, eigenvalues, explained variance)
3. **Factor interpretation** relies on examining variable loadings and biological/domain meaning
4. **Standardization is crucial** when variables have different scales or units

### For Researchers  
1. **Validation approach**: Use synthetic data to test method assumptions and behavior
2. **Expected performance**: Well-structured data should show clear factor separation
3. **Component retention**: Multiple criteria should converge on the same number of factors
4. **Noise effects**: Even with clean factor structure, substantial variance may be unexplained

## Comparison with Real Data

| Aspect | Synthetic Example | Real Data |
|--------|------------------|-----------|
| Factor Structure | Known (2 factors) | Unknown |
| Noise Level | Controlled | Variable |
| Explained Variance | ~75% (high) | Typically 30-60% |
| Component Interpretation | Validated against truth | Requires domain knowledge |
| Factor Recovery | Can be verified | Must be inferred |

## Extensions

Consider exploring:

- **Different noise levels**: Modify noise coefficients to see effect on factor recovery
- **More complex structures**: Add factor correlations or cross-loadings
- **Sample size effects**: Vary n_samples to study estimation stability  
- **Variable selection**: Remove variables to study factor identification
- **Rotation methods**: Apply varimax/promax to improve interpretability
- **Alternative methods**: Compare with Factor Analysis, ICA, or t-SNE
- **Cross-validation**: Use train/test splits to validate component stability

## Connection to Other Examples

This synthetic example provides the foundational understanding for:
- **hospitals_example.py**: Real-world healthcare quality data  
- **kuiper_example.py**: Astronomical data with natural factor structure
- **invest_example.py**: Financial portfolio analysis

The known ground truth here helps build intuition for interpreting results from these real-world applications where the true factor structure is unknown.
