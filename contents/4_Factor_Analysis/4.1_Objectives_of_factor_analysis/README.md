# 4.1 Objectives of Factor Analysis

This folder contains materials for Topic 4.1: Understanding the objectives and applications of Factor Analysis.

## Learning Objectives

After completing this topic, students will be able to:

- Explain the primary objectives of factor analysis
- Distinguish between factor analysis and principal component analysis
- Identify appropriate use cases for factor analysis
- Understand the concept of latent variables and observed indicators
- Recognize the difference between exploratory and confirmatory factor analysis

## Key Concepts

### Main Objectives of Factor Analysis

1. **Dimensionality Reduction**: Reduce the number of variables while retaining most information
2. **Latent Variable Detection**: Identify unobserved factors that explain correlations among variables  
3. **Data Simplification**: Create simpler, more interpretable structure from complex data
4. **Theory Testing**: Test hypotheses about underlying factor structures
5. **Scale Development**: Create reliable and valid measurement instruments

### Factor Analysis vs. Principal Component Analysis

| Aspect | Factor Analysis | Principal Component Analysis |
|--------|----------------|------------------------------|
| **Purpose** | Identify latent factors | Reduce dimensionality |
| **Model** | X = ΛF + ε | X = PY |
| **Variance** | Explains common variance | Explains total variance |
| **Factors** | Fewer than variables | Can equal variables |
| **Interpretation** | Latent constructs | Linear combinations |

### Applications

- **Psychology**: Intelligence, personality traits, attitudes
- **Marketing**: Customer segmentation, brand perception
- **Social Sciences**: Quality of life, social capital measures  
- **Finance**: Risk factors, market indicators
- **Education**: Academic abilities, learning styles

## Folder Structure

### 📁 `latex/`
LaTeX beamer presentation covering:
- Introduction to factor analysis objectives
- Comparison with PCA
- Real-world applications and examples
- Theoretical foundations

### 📁 `python/`
Python implementation demonstrating:
- Simple factor analysis example
- Comparison of FA and PCA results
- Visualization of factor structure
- Interpretation of factor loadings

### 📁 `julia/`
Julia pseudocode version:
- Mathematical formulation
- Clean algorithmic presentation
- Factor model equations

## Usage

**For LaTeX presentation:**
```bash
cd latex/
pdflatex objectives_factor_analysis.tex
```

**For Python practice:**
```bash
cd python/
python objectives_factor_analysis_practice.py
```

**For Julia practice:**
```bash
cd julia/
julia objectives_factor_analysis_practice.jl
```

## Prerequisites

- Basic understanding of multivariate statistics
- Knowledge of correlation and covariance matrices
- Familiarity with linear algebra concepts
- Understanding of variance and explained variance