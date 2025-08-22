# 1.1 Simple Linear Regression

This folder contains materials for Topic 1.1: Simple Linear Regression analysis for modeling the relationship between two quantitative variables.

## Learning Objectives

After completing this topic, students will be able to:

- Understand the concept of simple linear regression
- Apply the least squares method to estimate regression parameters
- Interpret regression coefficients and their statistical significance
- Calculate and interpret the coefficient of determination (R²)
- Assess model assumptions and limitations
- Make predictions using the fitted regression model

## Key Concepts

### Simple Linear Regression Model

The basic model: **Y = β₀ + β₁X + ε**

Where:
- **Y**: Response (dependent) variable
- **X**: Predictor (independent) variable  
- **β₀**: Intercept (value of Y when X = 0)
- **β₁**: Slope (change in Y per unit change in X)
- **ε**: Random error term

### Least Squares Estimation

- **Objective**: Minimize the sum of squared residuals
- **Normal Equations**: System of equations for finding optimal coefficients
- **Properties**: Best Linear Unbiased Estimators (BLUE) under assumptions

### Model Assessment

- **R²**: Proportion of variance explained by the model
- **Residual Analysis**: Checking model assumptions
- **Statistical Significance**: t-tests for coefficients
- **Confidence Intervals**: Uncertainty quantification

## Applications

- **Economics**: Relationship between price and demand
- **Biology**: Growth rate vs. environmental factors
- **Engineering**: Stress-strain relationships
- **Social Sciences**: Income vs. education level
- **Business**: Sales vs. advertising expenditure

## Folder Structure

### 📁 `latex/`
LaTeX beamer presentation covering:
- Introduction to linear relationships
- Least squares method derivation
- Model interpretation and assessment
- Real-world examples and applications

### 📁 `python/`
Python implementation demonstrating:
- Data generation and visualization
- Least squares parameter estimation
- Model fitting using scikit-learn
- Residual analysis and diagnostics
- Confidence intervals and predictions

### 📁 `julia/`
Julia pseudocode version:
- Clean mathematical implementation
- Matrix formulation of least squares
- Statistical computations

## Usage

**For LaTeX presentation:**
```bash
cd latex/
pdflatex simple_linear_regression.tex
```

**For Python practice:**
```bash
cd python/
python simple_linear_regression_practice.py
```

**For Julia practice:**
```bash
cd julia/
julia simple_linear_regression_practice.jl
```

## Mathematical Formulas

**Parameter Estimates:**
- β̂₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
- β̂₀ = ȳ - β̂₁x̄

**Coefficient of Determination:**
- R² = 1 - SSE/SST = SSR/SST

**Standard Errors:**
- SE(β̂₁) = σ√[1/Σ(xᵢ - x̄)²]
- SE(β̂₀) = σ√[1/n + x̄²/Σ(xᵢ - x̄)²]

## Prerequisites

- Basic statistics (mean, variance, correlation)
- Understanding of linear relationships
- Elementary calculus concepts
- Familiarity with scatter plots and data visualization