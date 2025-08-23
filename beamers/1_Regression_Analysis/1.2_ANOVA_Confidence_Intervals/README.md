# 1.2 ANOVA and Confidence Intervals

This folder contains materials for Topic 1.2: Analysis of Variance for regression models and construction of confidence intervals.

## Learning Objectives

- Perform ANOVA decomposition for regression models
- Test overall model significance using F-statistics
- Construct confidence intervals for regression parameters
- Create prediction intervals for new observations
- Interpret ANOVA tables and statistical outputs

## Key Concepts

### ANOVA Decomposition
- **Total Sum of Squares (SST)**: Σ(yᵢ - ȳ)²
- **Regression Sum of Squares (SSR)**: Σ(ŷᵢ - ȳ)²  
- **Error Sum of Squares (SSE)**: Σ(yᵢ - ŷᵢ)²
- **Relationship**: SST = SSR + SSE

### F-Test for Model Significance
- **Null Hypothesis**: β₁ = 0 (no linear relationship)
- **F-statistic**: F = MSR/MSE = (SSR/1)/(SSE/(n-2))
- **Decision Rule**: Reject H₀ if F > F₍₁,ₙ₋₂₎₍α₎

### Confidence and Prediction Intervals
- **Confidence Interval**: For the mean response at given X
- **Prediction Interval**: For individual response at given X
- **Prediction intervals are wider** than confidence intervals

## Usage

```bash
cd python/
python anova_confidence_intervals_practice.py
```