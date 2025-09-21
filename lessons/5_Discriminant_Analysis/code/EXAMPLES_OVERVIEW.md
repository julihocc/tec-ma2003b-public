# Discriminant Analysis Examples Overview

This document provides a comparative guide to Linear Discriminant Analysis (LDA) and Quadratic Discriminant Analysis (QDA) applications across different domains. Each example demonstrates the strengths and limitations of both methods in real-world classification scenarios.

## LDA vs QDA: Key Differences

### Linear Discriminant Analysis (LDA)
- **Assumption**: Equal covariance matrices across all groups
- **Decision Boundaries**: Linear (hyperplanes)
- **Parameters**: Fewer parameters to estimate (more stable)
- **Best For**: Groups with similar variability patterns
- **Computational**: Faster, less prone to overfitting

### Quadratic Discriminant Analysis (QDA)
- **Assumption**: Different covariance matrices for each group
- **Decision Boundaries**: Quadratic curves
- **Parameters**: More parameters (can overfit with small samples)
- **Best For**: Groups with different variability patterns
- **Computational**: More complex, requires larger sample sizes

## Example Applications

### 1. Marketing Customer Segmentation

**Context**: Classifying customers into High-Value, Loyal, and Occasional segments based on behavioral metrics.

**Dataset**: 1,200 customers × 8 features (purchase frequency, order value, engagement metrics)

**LDA Performance**:
- Accuracy: 100%
- Strengths: Perfect classification with synthetic data, interpretable discriminant functions
- LD1: Separates High-Value from Occasional (spending + engagement)
- LD2: Distinguishes Loyal customers (frequency vs. browsing behavior)

**QDA Performance**:
- Accuracy: 100%
- Strengths: Perfect classification, handles different segment variances
- Both methods achieve perfect accuracy with well-separated synthetic data

**Recommendation**: Use LDA for stability, QDA when segments show different behavioral variability

### 2. Quality Control in Manufacturing

**Context**: Classifying products as Acceptable, Borderline, or Defective based on quality measurements.

**Dataset**: 800 products × 6 features (dimensions, tolerances, material properties)

**LDA Performance**:
- Accuracy: 93.3%
- Strengths: Robust classification with feature selection, clear quality thresholds
- Effective for standard manufacturing quality control processes
- Cross-validation: 93.3% (±0.0%)

**QDA Performance**:
- Accuracy: 94.6%
- Strengths: Better at detecting complex defect patterns, higher precision for acceptable products
- More sensitive to subtle quality variations
- Cross-validation: 94.6% (±0.0%)

**Recommendation**: QDA preferred when defect patterns are complex and non-linear

### 3. Sports Analytics: Athlete Classification

**Context**: Classifying athletes into Elite, Competitive, and Developing categories based on performance metrics.

**Dataset**: 300 athletes × 7 features (speed, endurance, strength, technique, agility, power, consistency)

**LDA Performance**:
- Accuracy: 100%
- Strengths: Perfect classification, clear performance level separations, easy interpretation
- Useful for talent identification and training program assignment
- Cross-validation: 100% (±0.0%)

**QDA Performance**:
- Accuracy: 100%
- Strengths: Perfect classification, captures sport-specific performance curves
- Both methods achieve perfect accuracy with well-separated synthetic data

**Recommendation**: Both methods work perfectly for this well-structured synthetic dataset

## Method Selection Guidelines

### When to Choose LDA

1. **Small Sample Sizes**: Requires fewer parameters, less prone to overfitting
2. **Equal Group Variances**: When covariance matrices are similar across groups
3. **Interpretability**: When linear decision boundaries are desired
4. **Computational Efficiency**: For real-time or resource-constrained applications
5. **Stability**: When robustness to training data variations is important

### When to Choose QDA

1. **Large Sample Sizes**: Sufficient data to estimate group-specific covariance matrices
2. **Different Group Variances**: When groups have distinct variability patterns
3. **Complex Boundaries**: When non-linear decision boundaries better fit the data
4. **Higher Accuracy**: When maximum classification accuracy is the primary goal
5. **Flexible Modeling**: When capturing group-specific relationships is important

## Performance Comparison Summary

| Domain | LDA Accuracy | QDA Accuracy | Winner | Reason |
|--------|-------------|-------------|--------|---------|
| Marketing | 100% | 100% | Tie | Perfect classification with synthetic data |
| Quality Control | 93.3% | 94.6% | QDA | Better precision for acceptable products |
| Sports | 100% | 100% | Tie | Perfect classification with synthetic data |
| **Average** | **97.8%** | **98.2%** | **QDA** | **Slight edge in complex scenarios** |

## Implementation Considerations

### Sample Size Requirements

- **LDA**: Minimum 2-3 samples per parameter (more stable)
- **QDA**: Minimum 5-10 samples per parameter per group (more data needed)

### Computational Complexity

- **LDA**: O(n_features × n_classes) - Linear scaling
- **QDA**: O(n_features² × n_classes) - Quadratic scaling

### Overfitting Risk

- **LDA**: Lower risk, better generalization
- **QDA**: Higher risk with small samples, may require regularization

## Best Practices

### Model Validation
1. Always use cross-validation to assess stability
2. Compare both methods on your specific dataset
3. Check confusion matrices for class-specific performance
4. Validate assumptions (especially covariance equality for LDA)

### Feature Engineering
1. Standardize features before discriminant analysis
2. Consider feature selection to reduce dimensionality
3. Check for multicollinearity (especially affects LDA interpretation)

### Business Considerations
1. **LDA**: Preferred for operational systems requiring stability
2. **QDA**: Better for research applications needing maximum accuracy
3. Consider computational costs for real-time applications
4. Think about interpretability vs. predictive power trade-offs

## Common Pitfalls

### LDA Pitfalls
- Poor performance when covariance matrices truly differ
- May underfit complex group relationships
- Less flexible decision boundaries

### QDA Pitfalls
- Overfitting with small sample sizes
- Unstable estimates with high-dimensional data
- Higher computational requirements
- More complex interpretation

## Advanced Techniques

### Regularized Discriminant Analysis
- Combines LDA/QDA benefits
- Adds regularization parameter to control flexibility
- Useful when sample size is moderate

### Stepwise Variable Selection
- Automatically selects important features
- Reduces dimensionality and improves stability
- Particularly useful for LDA interpretation

### Cross-Validation for Model Selection
- Use nested CV to avoid overfitting
- Compare LDA vs QDA performance reliably
- Assess stability across different data subsets

---

## Running the Examples

Each example directory contains complete implementations:

```bash
# Marketing segmentation
cd code/marketing_segmentation/
python fetch_marketing.py  # Generate data
python marketing_lda.py    # Run LDA analysis
python marketing_qda.py    # Run QDA analysis

# Quality control
cd ../quality_control/
python fetch_quality.py
python quality_lda.py

# Sports analytics
cd ../sports_analytics/
python fetch_sports.py
python sports_lda.py
```

This overview demonstrates how discriminant analysis provides powerful classification tools for multivariate data across diverse application domains, with the choice between LDA and QDA depending on data characteristics and analytical requirements.