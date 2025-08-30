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
- ✅ **Complete Beamer presentation** covering all 6 subtopics with 4 comprehensive example sections
- ✅ **Four working code examples** across different domains (education, finance, astronomy, healthcare)
- ✅ **Comprehensive documentation** with detailed README files and data dictionaries
- ✅ **Interactive development support** with py-percent cells for VS Code/Jupyter integration
- ⏳ **Practice exercises** organized by subtopic (planned for future implementation)

### Interactive Development Features
- All code examples use py-percent cells (`# %%` and `# %% [markdown]`) for VS Code/Jupyter integration
- Examples generate output files (plots, reports) using robust pathlib-based file handling
- Data fetching is separated from analysis for reproducibility across environments

### Current Contents

#### Lesson Materials
- `beamer/factor_analysis_presentation.tex` - Complete chapter presentation (Beamer LaTeX)
- `beamer/factor_analysis_presentation.pdf` - Compiled presentation with 4 comprehensive example sections

#### Working Code Examples
```
code/
├── pca_example/               # Synthetic educational PCA demonstration
│   ├── pca_example.py        # Educational assessment scenario with known factors
│   ├── README.md             # Detailed pedagogical documentation
│   ├── pca_scree.png         # Component selection visualization
│   └── pca_biplot.png        # Students and abilities in PC space
├── invest_example/           # European stock market PCA analysis
│   ├── fetch_invest.py       # Generates synthetic European market data
│   ├── invest_example.py     # Financial market integration analysis
│   ├── invest.csv            # 1,860 trading days × 4 market indices
│   ├── invest_scree.png      # Market factor identification
│   ├── invest_biplot.png     # Time series and market loadings
│   ├── README.md             # Financial context and interpretation
│   └── EUROPEAN_STOCKS_DATA_DICTIONARY.md # Detailed market definitions
├── kuiper_example/           # Astronomical PCA with Kuiper Belt objects
│   ├── fetch_kuiper.py       # Generates synthetic orbital data
│   ├── kuiper_example.py     # Orbital dynamics and population analysis
│   ├── kuiper.csv            # 98 objects × 5 orbital parameters
│   ├── kuiper_scree.png      # Dynamical component structure
│   ├── kuiper_biplot.png     # Objects in orbital parameter space
│   ├── README.md             # Astronomical context and interpretation
│   └── KUIPER_BELT_DATA_DICTIONARY.md # Orbital parameter definitions
├── hospitals_example/        # Healthcare quality PCA analysis
│   ├── fetch_hospitals.py    # Generates synthetic hospital quality data
│   ├── hospitals_example.py  # Healthcare quality assessment
│   ├── hospitals.csv         # 50 hospitals × 8 quality metrics
│   ├── hospitals_scree.png   # Quality factor identification
│   ├── hospitals_biplot.png  # Hospitals in quality space
│   ├── README.md             # Healthcare context and interpretation
│   └── HOSPITAL_OUTCOMES_DATA_DICTIONARY.md # Quality metric definitions
└── EXAMPLES_OVERVIEW.md      # Comparative guide to all examples
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
# Educational synthetic example (self-contained, no data fetching needed)
.venv/bin/python code/pca_example/pca_example.py

# Financial markets example  
.venv/bin/python code/invest_example/fetch_invest.py
.venv/bin/python code/invest_example/invest_example.py

# Astronomical example
.venv/bin/python code/kuiper_example/fetch_kuiper.py  
.venv/bin/python code/kuiper_example/kuiper_example.py

# Healthcare quality example
.venv/bin/python code/hospitals_example/fetch_hospitals.py
.venv/bin/python code/hospitals_example/hospitals_example.py
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

## Cross-Domain Examples Summary

The four working examples demonstrate PCA applications across diverse fields:

### 1. Educational Assessment (`pca_example/`)
- **Pedagogical Focus**: Known factor structure allows validation of PCA concepts
- **Variables**: MathTest, VerbalTest, SocialSkills, Leadership + noise controls
- **Learning Value**: Ground truth validation, factor recovery, noise separation

### 2. Financial Markets (`invest_example/`)  
- **Domain**: European stock market integration analysis
- **Variables**: DAX, SMI, CAC, FTSE indices over 1,860 trading days
- **Learning Value**: Systematic vs idiosyncratic risk, market factor models

### 3. Astronomy (`kuiper_example/`)
- **Domain**: Kuiper Belt object orbital dynamics
- **Variables**: 5 orbital parameters across 98 trans-Neptunian objects
- **Learning Value**: Natural population structure, physical interpretation

### 4. Healthcare (`hospitals_example/`)
- **Domain**: Hospital quality assessment and benchmarking  
- **Variables**: 8 quality metrics across 50 US hospitals
- **Learning Value**: Multi-dimensional quality, organizational effectiveness

Each example includes comprehensive documentation, data dictionaries, and domain-specific interpretation guides.

## Next Steps

After completing this chapter, students will be prepared for:
- Chapter 5: Discriminant Analysis
- Chapter 6: Cluster Analysis  
- Advanced multivariate modeling techniques
- Real-world statistical consulting across multiple domains