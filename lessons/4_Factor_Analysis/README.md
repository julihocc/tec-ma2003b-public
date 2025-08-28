# Chapter 4 — Factor Analysis

This chapter covers Factor Analysis techniques for dimensionality reduction and latent variable modeling in multivariate data.

## Chapter Overview

Factor Analysis is a statistical method used to describe variability among observed, correlated variables in terms of fewer unobserved variables called factors. It seeks to find if the observed variables can be explained largely or entirely by fewer latent variables.

## Learning Objectives

By the end of this chapter, students will be able to:

- Understand the objectives and applications of factor analysis
- Formulate and solve factor analysis equations
- Determine the appropriate number of factors using various criteria
- Apply factor rotation techniques to improve interpretability
- Implement oblique rotation methods for correlated factors
- Use commercial software and coding tools for factor analysis

## Chapter Structure

### 4.1 Objectives of Factor Analysis
- Purpose and applications of factor analysis
- Relationship to Principal Component Analysis (PCA)
- Common factor model vs. principal factor model
- Use cases in psychology, marketing, and social sciences

### 4.2 Factor Analysis Equations
- Mathematical formulation of the factor model
- Factor loadings and communalities
- Unique factors and specific variance
- Maximum likelihood estimation methods

### 4.3 Choosing the Appropriate Number of Factors
- Kaiser criterion (eigenvalue > 1)
- Scree plot method
- Parallel analysis
- Goodness-of-fit measures
- Cross-validation approaches

### 4.4 Factor Rotation
- Need for factor rotation
- Orthogonal rotation methods
- Varimax rotation for simple structure
- Quartimax and equimax criteria
- Comparison of rotation methods

### 4.5 Oblique Rotation Method
- When to use oblique rotation
- Direct oblimin rotation
- Promax rotation
- Interpretation of pattern vs. structure matrices
- Factor correlations

### 4.6 Coding and Commercial Software
- Implementation in Python (scikit-learn, factor_analyzer)
- R packages (psych, GPArotation, lavaan)
- SPSS and SAS procedures
- Practical considerations and best practices

## Chapter Implementation Status

The chapter currently includes:
- ✅ **Complete Beamer presentation** covering all 6 subtopics
- ✅ **Working code examples** with py-percent cells for interactive development
- ⏳ **Practice exercises** organized by subtopic (planned for future implementation)

### Interactive Development Features
- All code examples use py-percent cells (`# %%` and `# %% [markdown]`) for VS Code/Jupyter integration
- Examples generate output files (plots, reports) using robust pathlib-based file handling
- Data fetching is separated from analysis for reproducibility across environments

### Current Contents

#### Lesson Materials
- `beamer/factor_analysis_presentation.tex` - Complete chapter presentation (Beamer)
- `beamer/factor_analysis_presentation.pdf` - Compiled presentation

#### Working Code Examples
```
code/
├── invest_example/          # PCA analysis with real stock market data
│   ├── fetch_invest.py     # Data fetching script
│   ├── invest_example.py   # Main PCA analysis with py-percent cells
│   ├── invest.csv          # Downloaded data (created by fetch script)
│   └── invest_*.png        # Generated figures
└── pca_example/            # Synthetic PCA demonstration
    ├── pca_example.py      # Self-contained PCA demo with py-percent cells
    └── pca_scree.png       # Generated scree plot
```

#### Planned Practice Exercises (Future)
```
practice/
├── 4.1_objectives/           # Objectives and applications
├── 4.2_equations/           # Mathematical foundations
├── 4.3_number_of_factors/   # Factor retention methods
├── 4.4_rotation/            # Orthogonal rotation
├── 4.5_oblique_rotation/    # Oblique rotation methods
└── 4.6_software/            # Cross-platform implementation
```

### Usage

#### Compile Presentation
```bash
cd beamer/
pdflatex factor_analysis_presentation.tex
# Run twice for proper cross-references
pdflatex factor_analysis_presentation.tex
```

#### Run Working Examples
```bash
# Fetch data first (for invest example)
.venv/bin/python code/invest_example/fetch_invest.py

# Run PCA examples
.venv/bin/python code/invest_example/invest_example.py
.venv/bin/python code/pca_example/pca_example.py
```

#### Interactive Development
```bash
# Convert py-percent cell scripts to Jupyter notebooks
jupytext --to ipynb code/*/*.py
```

#### Future Practice Exercises (when implemented)
```bash
# Individual subtopic
cd practice/4.1_objectives/
python objectives_factor_analysis_practice.py

# All subtopics
for dir in practice/4.*/; do
  cd "$dir"
  python *_practice.py
  cd ../..
done
```

## Prerequisites

- Understanding of linear algebra (eigenvalues, eigenvectors, matrix operations)
- Basic knowledge of multivariate statistics
- Familiarity with Principal Component Analysis (Chapter 3)
- Understanding of correlation and covariance matrices

## Key Concepts

- **Factor**: An unobserved variable that influences multiple observed variables
- **Loading**: The correlation between an observed variable and a factor
- **Communality**: The proportion of variance in a variable explained by all factors
- **Uniqueness**: The proportion of variance unique to each variable
- **Simple Structure**: An ideal factor solution where each variable loads highly on one factor

## Mathematical Notation

- **X**: Observed variables matrix (n × p)
- **Λ**: Factor loadings matrix (p × k)  
- **F**: Factor scores matrix (n × k)
- **ε**: Unique factors matrix (n × p)
- **Ψ**: Unique variances (diagonal matrix)
- **Φ**: Factor correlation matrix (for oblique rotation)

## Next Steps

After completing this chapter, students will be prepared for:
- Chapter 5: Discriminant Analysis
- Chapter 6: Cluster Analysis
- Advanced multivariate modeling techniques