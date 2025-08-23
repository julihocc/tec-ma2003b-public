# 1.3 Residual Analysis and Normality

This folder contains materials for Topic 1.3: Residual analysis techniques and normality testing for regression models.

## Learning Objectives

- Conduct comprehensive residual analysis
- Create and interpret residual plots
- Test for normality of residuals
- Identify outliers and influential observations
- Assess model adequacy and assumptions

## Key Concepts

### Residual Analysis
- **Residuals**: eᵢ = yᵢ - ŷᵢ (observed - predicted)
- **Standardized Residuals**: eᵢ/σ̂
- **Studentized Residuals**: Account for leverage

### Diagnostic Plots
- **Residuals vs. Fitted Values**: Check homoskedasticity
- **Q-Q Plot**: Assess normality assumption
- **Residuals vs. Predictor**: Check linearity
- **Scale-Location Plot**: Check constant variance

### Normality Tests
- **Shapiro-Wilk Test**: For small samples
- **Kolmogorov-Smirnov Test**: General normality test
- **Anderson-Darling Test**: More powerful than K-S
- **Visual Methods**: Histograms, Q-Q plots

## Usage

```bash
cd python/
python residual_analysis_normality_practice.py
```