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

## Consolidated Structure

The chapter now uses a consolidated structure with:
- **Single beamer presentation** covering all 6 subtopics
- **Single comprehensive notes** document 
- **Modular practice exercises** organized by subtopic

### Contents

#### Lesson Materials
- `lesson/factor_analysis.tex` - Complete chapter presentation (Beamer)
- `lesson/factor_analysis.pdf` - Compiled presentation

#### Comprehensive Notes
- `notes/factor_analysis_notes.tex` - Complete chapter documentation
- `notes/factor_analysis_notes.pdf` - Compiled notes

#### Practice Exercises
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
cd lesson/
pdflatex factor_analysis.tex
```

#### Compile Notes
```bash
cd notes/
pdflatex factor_analysis_notes.tex
```

#### Run Practice Exercises
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