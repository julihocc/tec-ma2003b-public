# Chapter 5 — Discriminant Analysis

This chapter covers discriminant analysis techniques for classification and pattern recognition in multivariate data.

## Chapter Overview

Discriminant Analysis is a statistical technique used to classify observations into predefined groups or categories based on their characteristics. This chapter progresses from basic two-population discrimination to advanced techniques including canonical discriminant analysis and practical software implementations.

## Learning Objectives

By the end of this chapter, students will be able to:

- Perform linear and quadratic discriminant analysis for classification
- Understand the role of prior probabilities and misclassification costs
- Apply basic discrimination techniques with performance evaluation
- Use stepwise selection for variable selection in discriminant analysis
- Compute canonical discriminant functions for dimensionality reduction
- Implement discriminant analysis using various software tools

## Chapter Structure

### 5.1 Discrimination for Two Multivariate Normal Populations
- Linear Discriminant Analysis (LDA) for two groups
- Bayes optimal classification rule
- Pooled covariance estimation and assumptions
- Decision boundaries and geometric interpretation

### 5.2 Cost Function and Prior Probabilities
- Incorporating prior probabilities into classification
- Asymmetric misclassification costs
- Modified decision rules and thresholds
- Real-world cost considerations

### 5.3 Basic Discrimination
- Performance evaluation metrics
- Confusion matrices and error rates
- Sensitivity, specificity, and accuracy measures
- Cross-validation for model assessment

### 5.4 Stepwise Selection
- Variable selection in discriminant analysis
- Forward, backward, and bidirectional selection
- Statistical criteria for variable inclusion
- Model parsimony and interpretability

### 5.5 Canonical Discriminant Functions
- Dimensionality reduction in classification
- Within-group and between-group covariance matrices
- Generalized eigenvalue problem solution
- Interpretation of canonical variates

### 5.6 Coding and Commercial Software
- Python implementation (scikit-learn, scipy)
- R packages for discriminant analysis
- SPSS and SAS procedures
- Comparison of software capabilities

## Folder Organization

Each subtopic follows the organized structure:

```
5.X_Topic_Name/
├── README.md                          # Topic-specific learning objectives
├── [topic]_report.txt                 # Exercise description and hints
├── 📁 latex/                          # LaTeX presentation files
│   ├── [topic].tex                    # Beamer presentation source
│   ├── [topic].pdf                    # Compiled presentation (where available)
│   └── ... (LaTeX auxiliary files)
├── 📁 python/                         # Python implementation
│   ├── [topic]_practice.py           # Main practice script
│   └── test_[topic].py               # Unit tests
└── 📁 julia/                          # Julia pseudocode version
    └── [topic]_practice.jl           # Mathematical pseudocode
```

## Usage Examples

**For organized structure scripts:**
```bash
# Activate environment
source .venv/bin/activate

# Run single script (organized structure)
cd beamers/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/python
python discrimination_two_populations_practice.py

# Run all Python scripts in organized structure
for f in beamers/5_Discriminant_Analysis/*/python/*_practice.py; do
  echo "--- running $f ---"
  python "$f" || break
done
```

## Prerequisites

- Understanding of multivariate normal distributions
- Knowledge of linear algebra (eigenvalues, eigenvectors)
- Basic statistical inference and hypothesis testing
- Familiarity with covariance matrices and correlation
- Understanding of classification concepts

## Key Concepts

- **Linear Discriminant Analysis (LDA)**: Classification with equal covariances
- **Quadratic Discriminant Analysis (QDA)**: Classification with unequal covariances
- **Bayes Rule**: Optimal classification under probabilistic assumptions
- **Prior Probabilities**: Known or estimated group proportions
- **Posterior Probabilities**: Updated probabilities after observing data
- **Canonical Variates**: Linear combinations maximizing group separation

## Mathematical Notation

- **π_k**: Population k (k = 1, 2, ..., g groups)
- **μ_k**: Mean vector for population k
- **Σ_k**: Covariance matrix for population k
- **π(k)**: Prior probability for population k
- **c(i|k)**: Cost of classifying as group i when true group is k
- **W**: Within-group sum of squares matrix
- **B**: Between-group sum of squares matrix

## Software and Dependencies

- **Python**: numpy, scipy, scikit-learn, matplotlib
- **R**: MASS package for LDA/QDA, candisc for canonical analysis
- **Statistical Packages**: SPSS DISCRIMINANT, SAS PROC DISCRIM

## Next Steps

After completing this chapter, students will be prepared for:
- Chapter 6: Cluster Analysis
- Chapter 7: Multivariate Regression
- Advanced pattern recognition and machine learning techniques

