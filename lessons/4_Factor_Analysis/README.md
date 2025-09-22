# Chapter 4 — Factor Analysis

This chapter covers Factor Analysis techniques for dimensionality reduction and latent variable modeling in multivariate data.

## Chapter Overview

Factor Analysis is a statistical method used to identify underlying latent variables (factors) that explain the patterns of correlations within a set of observed variables. Unlike Principal Component Analysis (PCA), which focuses on explaining maximum variance, Factor Analysis specifically models the common variance shared among variables while treating unique variance as measurement error or specific factors.

The fundamental goal is to find a smaller number of latent factors that can adequately reproduce the observed correlation matrix, providing insights into the underlying structure of the data.

## Learning Objectives

By the end of this chapter, students will be able to:

- Distinguish between Factor Analysis and Principal Component Analysis
- Understand the common factor model and its mathematical formulation
- Apply different factor extraction methods (Principal Axis, Maximum Likelihood)
- Determine the optimal number of factors using multiple criteria
- Interpret factor loadings, communalities, and uniquenesses
- Apply orthogonal and oblique rotation techniques for better interpretation
- Use Python and other statistical software for factor analysis implementation

## Chapter Structure

### 4.1 Objectives of Factor Analysis
- Purpose and applications of factor analysis
- Factor Analysis vs. Principal Component Analysis
- Common factor model: shared and unique variance
- Applications in psychology, education, marketing, and finance

### 4.2 Factor Analysis Equations
- Mathematical formulation: X = ΛF + ε
- Factor loadings matrix (Λ) and interpretation
- Communalities and uniquenesses
- Factor extraction methods: Principal Axis Factoring, Maximum Likelihood

### 4.3 Choosing the Appropriate Number of Factors
- Kaiser criterion (eigenvalue > 1) limitations in FA
- Scree plot interpretation for common factors
- Parallel analysis for factor retention
- Goodness-of-fit indices (RMSEA, TLI, CFI)
- Interpretability and theoretical considerations

### 4.4 Factor Rotation
- The rotation problem: achieving simple structure
- Orthogonal rotation methods (Varimax, Quartimax, Equimax)
- Comparison of rotation criteria
- Interpretation of rotated factor loadings
- When orthogonal assumptions are appropriate

### 4.5 Oblique Rotation Method
- Allowing correlated factors: when and why
- Direct Oblimin and Promax rotation
- Pattern matrix vs. Structure matrix interpretation
- Factor correlation matrices
- Hierarchical factor structures

### 4.6 Coding and Commercial Software
- Python implementation: factor_analyzer package
- scikit-learn limitations for true factor analysis
- R packages: psych, GPArotation, lavaan for SEM
- SPSS FACTOR procedure
- Practical workflow and interpretation guidelines

## Chapter Implementation Status

The chapter currently includes:
- ✅ **Complete Beamer presentation** covering all 6 subtopics with comprehensive factor analysis theory and applications
- ✅ **Four working factor analysis examples** across different domains (education, finance, astronomy, healthcare)
- ✅ **PCA comparison examples** for pedagogical contrast and understanding
- ✅ **Comprehensive documentation** with detailed README files and data dictionaries
- ✅ **Interactive development support** with py-percent cells for VS Code/Jupyter integration
- ⏳ **Advanced factor analysis applications** including confirmatory factor analysis (planned)

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
├── educational_example/               # Synthetic educational PCA demonstration (for comparison)
│   ├── educational_pca.py        # Educational assessment scenario with PCA
│   ├── educational_fa.py         # Same data analyzed with Factor Analysis
│   ├── README.md             # Detailed pedagogical documentation
│   ├── pca_scree.png         # PCA component selection visualization
│   ├── fa_scree.png          # FA factor selection visualization
│   └── fa_loadings.png       # Factor loadings heatmap
├── invest_example/           # European stock market Factor Analysis
│   ├── fetch_invest.py       # Generates synthetic European market data
│   ├── invest_example.py     # Financial market PCA analysis (existing)
│   ├── invest_fa.py          # Financial market Factor Analysis
│   ├── invest.csv            # 1,860 trading days × 4 market indices
│   ├── invest_fa_loadings.png # Factor loadings for market factors
│   ├── invest_fa_scree.png   # Factor selection visualization
│   ├── README.md             # Financial context and interpretation
│   └── EUROPEAN_STOCKS_DATA_DICTIONARY.md # Detailed market definitions
├── kuiper_example/           # Astronomical Factor Analysis with Kuiper Belt objects
│   ├── fetch_kuiper.py       # Generates synthetic orbital data
│   ├── kuiper_example.py     # Orbital dynamics PCA analysis (existing)
│   ├── kuiper_fa.py          # Orbital dynamics Factor Analysis
│   ├── kuiper.csv            # 98 objects × 5 orbital parameters
│   ├── kuiper_fa_loadings.png # Factor structure of orbital parameters
│   ├── kuiper_fa_scree.png   # Factor retention criteria
│   ├── README.md             # Astronomical context and interpretation
│   └── KUIPER_BELT_DATA_DICTIONARY.md # Orbital parameter definitions
├── hospitals_example/        # Healthcare quality Factor Analysis
│   ├── fetch_hospitals.py    # Generates synthetic hospital quality data
│   ├── hospitals_example.py  # Healthcare quality PCA analysis (existing)
│   ├── hospitals_fa.py       # Healthcare quality Factor Analysis
│   ├── hospitals.csv         # 50 hospitals × 8 quality metrics
│   ├── hospitals_fa_loadings.png # Quality factors structure
│   ├── hospitals_fa_rotation.png # Before/after rotation comparison
│   ├── README.md             # Healthcare context and interpretation
│   └── HOSPITAL_OUTCOMES_DATA_DICTIONARY.md # Quality metric definitions
└── EXAMPLES_OVERVIEW.md      # Comparative guide: PCA vs Factor Analysis
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
# Educational example: PCA vs Factor Analysis comparison
.venv/bin/python code/educational_example/educational_pca.py     # PCA analysis (existing)
.venv/bin/python code/educational_example/educational_fa.py      # Factor Analysis on same data

# Financial markets Factor Analysis  
.venv/bin/python code/invest_example/fetch_invest.py
.venv/bin/python code/invest_example/invest_fa.py    # Factor Analysis
.venv/bin/python code/invest_example/invest_example.py  # PCA comparison

# Astronomical Factor Analysis
.venv/bin/python code/kuiper_example/fetch_kuiper.py  
.venv/bin/python code/kuiper_example/kuiper_fa.py    # Factor Analysis
.venv/bin/python code/kuiper_example/kuiper_example.py  # PCA comparison

# Healthcare quality Factor Analysis
.venv/bin/python code/hospitals_example/fetch_hospitals.py
.venv/bin/python code/hospitals_example/hospitals_fa.py    # Factor Analysis
.venv/bin/python code/hospitals_example/hospitals_example.py  # PCA comparison
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

- **Factor**: An unobserved latent variable that explains correlations among observed variables
- **Factor Loading**: The regression coefficient relating an observed variable to a factor
- **Communality (h²)**: The proportion of a variable's variance explained by common factors
- **Uniqueness (u²)**: The proportion of variance unique to each variable (1 - h²)
- **Simple Structure**: Thurstone's ideal where each variable loads highly on few factors
- **Rotation**: Mathematical transformation to improve factor interpretability
- **Common Variance**: Variance shared among variables, explained by factors
- **Specific Variance**: Variance unique to each variable, not shared with others

## Mathematical Notation

- **X**: Observed variables matrix (n × p)
- **Λ**: Factor loadings matrix (p × k)  
- **F**: Factor scores matrix (n × k)
- **ε**: Unique/specific factors matrix (n × p)
- **Ψ**: Unique variances diagonal matrix (p × p)
- **Φ**: Factor correlation matrix for oblique rotation (k × k)
- **R**: Observed correlation matrix (p × p)
- **R̂**: Reproduced correlation matrix ΛΛ' + Ψ

## Cross-Domain Examples Summary

The four working examples demonstrate Factor Analysis applications across diverse fields, with PCA comparisons for pedagogical contrast:

### 1. Educational Assessment (`educational_example/`)
- **Pedagogical Focus**: Direct comparison of PCA vs Factor Analysis on synthetic data
- **Variables**: MathTest, VerbalTest, SocialSkills, Leadership + noise controls
- **Learning Value**: Factor recovery validation, communalities interpretation, rotation effects
- **FA-Specific**: Demonstrates common vs unique variance partitioning

### 2. Financial Markets (`invest_example/`)  
- **Domain**: European stock market factor structure analysis
- **Variables**: DAX, SMI, CAC, FTSE indices over 1,860 trading days
- **Learning Value**: Market integration factors, systematic risk identification
- **FA-Specific**: Common market factors vs idiosyncratic movements

### 3. Astronomy (`kuiper_example/`)
- **Domain**: Kuiper Belt object orbital parameter factor structure
- **Variables**: 5 orbital parameters across 98 trans-Neptunian objects
- **Learning Value**: Dynamical family identification, orbital resonance factors
- **FA-Specific**: Physical factor interpretation in celestial mechanics

### 4. Healthcare (`hospitals_example/`)
- **Domain**: Hospital quality assessment factor structure
- **Variables**: 8 quality metrics across 50 US hospitals
- **Learning Value**: Quality dimensions, performance factor identification
- **FA-Specific**: Healthcare latent constructs, rotation for simple structure

Each example includes comprehensive documentation, data dictionaries, PCA vs FA comparative analysis, and rotation demonstrations.

## Next Steps

After completing this chapter, students will be prepared for:
- Chapter 5: Discriminant Analysis
- Chapter 6: Cluster Analysis  
- Advanced multivariate modeling techniques
- Real-world statistical consulting across multiple domains