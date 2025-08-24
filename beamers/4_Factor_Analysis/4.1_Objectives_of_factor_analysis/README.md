# 4.1 Objectives of Factor Analysis

This folder contains comprehensive materials for Topic 4.1: Understanding the objectives and applications of Factor Analysis in multivariate data science.

## Contents Overview

- **Lesson**: Student presentation materials (Beamer slides)
- **Practice**: Hands-on Python implementation with real-world examples
- **Notes**: Expanded documentation with pedagogical guidance

## Learning Objectives

After completing this topic, students will be able to:

- **Understand** the primary objectives of factor analysis in multivariate data analysis
- **Distinguish** between factor analysis and principal component analysis approaches  
- **Identify** latent variable structures in real-world applications
- **Compare** exploratory vs confirmatory factor analysis methodologies
- **Apply** factor analysis to psychological, business, and research contexts

## Learning Goals

Students will demonstrate mastery by:

- Explaining the fundamental objectives: dimensionality reduction, latent variable identification, and data structure understanding
- Describing how factor analysis models measurement error and common variance
- Comparing factor analysis and PCA in terms of purpose, interpretation, and application
- Recognizing when factor analysis is more appropriate than other multivariate techniques
- Applying factor analysis concepts to practical research scenarios

## Key Concepts

### Factor Analysis Fundamentals

- **Latent Variables**: Unobserved constructs that influence multiple observed variables
- **Factor Loadings**: Correlations between observed variables and underlying factors  
- **Communalities**: Proportion of variable variance explained by all factors
- **Common vs Unique Variance**: Shared variance explained by factors vs variable-specific variance
- **Factor Model**: X = ΛF + ε (observed = loadings × factors + error)

### Primary Objectives

1. **Dimensionality Reduction**: Transform p observed variables into k factors (k < p)
2. **Latent Variable Identification**: Discover unobserved constructs that influence multiple variables
3. **Data Structure Understanding**: Identify patterns of relationships among variables
4. **Measurement Purification**: Remove measurement error from analysis
5. **Theory Development**: Generate hypotheses about underlying structures

### Factor Analysis vs. Principal Component Analysis

| Aspect | Factor Analysis | Principal Component Analysis |
|--------|----------------|------------------------------|
| **Purpose** | Identify latent constructs | Reduce dimensionality |
| **Model** | X = ΛF + ε | X = PY |
| **Variance Explained** | Common variance only | Total variance |
| **Factors/Components** | Usually < p variables | Can be = p variables |
| **Interpretation** | Latent constructs | Linear combinations |
| **Unique Variance** | Explicitly modeled | Not considered |

**When to Choose:**
- **Factor Analysis**: Theory-driven research, latent variable identification, measurement model validation
- **PCA**: Data compression, dimensionality reduction, exploratory data analysis

## Applications Demonstrated

### Psychology
- Intelligence testing (g-factor)
- Personality assessment (Big Five)
- Attitude measurement
- Clinical assessment scales

### Marketing  
- Customer segmentation
- Brand positioning
- Product attribute analysis
- Market research simplification

### Finance
- Risk factor identification
- Portfolio analysis
- Economic indicator grouping
- Credit scoring models

### Education
- Academic ability assessment
- Learning style identification
- Curriculum evaluation
- Student performance analysis

## Practice Activities

The hands-on practice includes:

- **Synthetic Data Generation**: Psychology test data with known 2-factor structure
- **Correlation Analysis**: Identify potential factor patterns in data
- **Comparative Analysis**: Factor analysis vs PCA results on same dataset
- **Results Interpretation**: Factor loadings and communalities in practical contexts
- **Real-world Application**: Demonstrate concepts across multiple domains

### Research Problem

Students work with a psychology research scenario:
- 6 cognitive tests administered to 200 students
- **Challenge**: Are these really 6 separate abilities?
- **Hypothesis**: Fewer underlying cognitive factors exist
- **Research Question**: How many latent factors explain performance?

## Folder Structure

```
4.1_Objectives_of_factor_analysis/
├── README.md                          # This overview document
├── lesson/                            # Student presentation materials
│   ├── objectives_factor_analysis.tex # Beamer presentation source
│   └── objectives_factor_analysis.pdf # Compiled presentation
├── practice/                          # Hands-on programming exercises
│   ├── objectives_factor_analysis_practice.py  # Main practice script
│   ├── factor_analysis.py            # Core analysis functions
│   ├── factor_analysis_reporter.py   # Report generation functions
│   └── README.md                      # Practice instructions
└── notes/                             # Expanded content and guidance
    ├── objectives_factor_analysis_notes.tex # Comprehensive documentation
    └── additional_resources/          # Extra materials, datasets, etc.
```

## Usage Instructions

### Running the Lesson
```bash
# Compile presentation slides
cd lesson/
pdflatex objectives_factor_analysis.tex
```

### Running the Practice
```bash
# Execute the hands-on analysis
cd practice/
python objectives_factor_analysis_practice.py
```

**Output**: Complete analysis report saved to `factor_analysis_report.txt`

### Accessing Extended Notes
```bash
# Compile comprehensive documentation
cd notes/
pdflatex objectives_factor_analysis_notes.tex
```

## Prerequisites

### Statistical Knowledge
- Basic understanding of multivariate statistics
- Knowledge of correlation and covariance matrices
- Familiarity with linear algebra concepts
- Understanding of variance and explained variance

### Technical Requirements
- Python 3.8+ with numpy, scikit-learn, factor_analyzer
- LaTeX distribution for compiling documents
- Virtual environment setup (recommended)

## Types of Factor Analysis

### Exploratory Factor Analysis (EFA)
- No prior theory about factor structure
- Let data determine number of factors and loadings
- Used for theory generation and scale development

### Confirmatory Factor Analysis (CFA)  
- Test specific theoretical model
- Researcher specifies factor structure a priori
- Used for theory testing and model validation