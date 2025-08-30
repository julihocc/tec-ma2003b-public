# Synthetic Data PCA Example

## Overview

This example demonstrates Principal Component Analysis (PCA) using a carefully constructed synthetic dataset with known underlying factor structure. It serves as a pedagogical tool for understanding how PCA works when the ground truth is known, allowing students to validate whether the method successfully recovers the true latent factors.

## Files

- `pca_example.py` - Main PCA analysis script with detailed explanations and validation
- `pca_scree.png` - Scree plot for component selection and factor identification  
- `pca_biplot.png` - Biplot visualization showing observations and variable loadings
- `README.md` - This documentation file

## Synthetic Data Structure

The dataset contains **100 student observations** across **6 assessment variables** with a known 2-factor structure representing educational abilities:

### True Factor Structure
- **Intelligence Factor**: Underlying cognitive ability affecting academic tests
- **Personality Factor**: Underlying social/emotional traits affecting interpersonal skills
- **Measurement Error**: Realistic noise added to meaningful variables
- **Pure Noise**: Control variables with no latent structure

### Variable Definitions
1. **MathTest** - Mathematics assessment (0.85 × Intelligence + measurement error)
2. **VerbalTest** - Verbal reasoning assessment (0.80 × Intelligence + measurement error)  
3. **SocialSkills** - Social competency rating (0.85 × Personality + measurement error)
4. **Leadership** - Leadership ability rating (0.80 × Personality + measurement error)
5. **RandomVar1** - Pure noise variable (no latent structure)
6. **RandomVar2** - Pure noise variable (no latent structure)

## Usage

```bash
# Run the PCA analysis (no data fetching needed - synthetic data generated internally)
python pca_example.py
```

## Expected Results

### Typical Output
- **Eigenvalues**: `[2.224, 1.870, 0.970, 0.862, 0.134, 0.000]` (approximate)
- **Explained variance**: PC1 (~36.7%), PC2 (~30.8%), PC3-PC4 (~30.2%), PC5-PC6 (~2.3%)
- **Cumulative variance**: First 2 components explain ~67.6% of total variance

### Factor Recovery Validation

The script includes automatic validation of whether PCA correctly identified the known factor structure:

- **PC1** captures general ability affecting all meaningful variables (Math, Verbal, Social, Leadership)
- **PC2** may separate cognitive from social abilities
- **PC3-PC4** capture additional structure and measurement error
- **PC5-PC6** are pure noise components with very low eigenvalues (~0.13)
- Random variables show weaker loadings than meaningful variables

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
3. **Factor interpretation** relies on examining variable loadings and educational/domain meaning
4. **Standardization is crucial** when variables have different scales or units
5. **General vs specific factors** emerge naturally from correlated ability measures

### For Researchers  
1. **Validation approach**: Use synthetic data to test method assumptions and behavior
2. **Expected performance**: Well-structured data should show clear factor separation
3. **Component retention**: Multiple criteria should converge on meaningful number of factors
4. **Noise effects**: Even with clean factor structure, substantial variance may be unexplained
5. **Educational measurement**: PCA reveals structure in assessment and survey data

## Comparison with Real Data

| Aspect | Synthetic Example | Real Educational Data |
|--------|------------------|----------------------|
| Factor Structure | Known (Intelligence + Personality) | Unknown ability structure |
| Noise Level | Controlled (0.2-0.25) | Variable measurement error |
| Explained Variance | ~68% (high for education) | Typically 40-70% |
| Component Interpretation | Validated against truth | Requires psychometric knowledge |
| Factor Recovery | Can be verified | Must be inferred from theory |
| Student Rankings | Based on known factors | Based on observed performance |

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
