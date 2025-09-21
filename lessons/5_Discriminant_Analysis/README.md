# Chapter 5 — Discriminant Analysis

This chapter covers Discriminant Analysis techniques for classification and group separation in multivariate data.

## Chapter Overview

Discriminant Analysis is a statistical method used to classify observations into predefined groups based on multiple predictor variables. The goal is to find linear combinations of predictors (discriminant functions) that best separate the groups while maximizing between-group differences and minimizing within-group variation.

Unlike other classification methods, discriminant analysis provides interpretable functions that reveal which variables contribute most to group separation, making it valuable for understanding the underlying structure of group differences.

## Learning Objectives

By the end of this chapter, students will be able to:

- Understand the difference between descriptive and predictive discriminant analysis
- Apply Linear and Quadratic Discriminant Analysis appropriately
- Evaluate discriminant analysis assumptions (normality, homoscedasticity, group differences)
- Interpret discriminant functions and classification boundaries
- Use cross-validation and performance metrics for model evaluation
- Apply discriminant analysis in business and research contexts
- Implement discriminant analysis using Python and other statistical software

## Chapter Structure

### 5.1 Discrimination for Two Multivariate Normal Populations

- Fisher's Linear Discriminant for two-group separation
- Mathematical formulation and geometric interpretation
- Classification rules and decision boundaries
- Prior probabilities and misclassification costs

### 5.2 Cost Function and Prior Probabilities

- Incorporating business costs into classification decisions
- Adjusting for unequal prior probabilities
- Expected cost minimization approach
- Applications in medical diagnosis and fraud detection

### 5.3 Basic Discrimination

- Multiple discriminant functions for k > 2 groups
- Canonical discriminant analysis
- Stepwise variable selection methods
- Model parsimony vs. predictive accuracy trade-offs

### 5.4 Stepwise Selection

- Forward and backward selection algorithms
- Wilks' lambda and other selection criteria
- Cross-validation for variable selection stability
- Overfitting prevention in discriminant analysis

### 5.5 Canonical Discriminant Functions

- Canonical correlation interpretation
- Discriminant function scores and group centroids
- Classification accuracy assessment
- Business interpretation of discriminant coefficients

### 5.6 Coding and Commercial Software

- Python implementation: scikit-learn discriminant analysis
- R packages: MASS, caret for discriminant methods
- SPSS DISCRIMINANT procedure
- Practical workflow and validation guidelines

## Chapter Implementation Status

The chapter currently includes:

- ✅ **Complete Beamer presentation** covering all 6 subtopics with comprehensive discriminant analysis theory
- ✅ **Three working discriminant analysis examples** across different domains (marketing, manufacturing, sports)
- ✅ **Comprehensive documentation** with detailed README files and data dictionaries
- ✅ **Interactive development support** with py-percent cells for VS Code/Jupyter integration
- ⏳ **Advanced applications** including regularized discriminant analysis (planned)

### Interactive Development Features

- All code examples use py-percent cells (`# %%` and `# %% [markdown]`) for VS Code/Jupyter integration
- Examples generate output files (plots, reports) using robust pathlib-based file handling
- Data fetching is separated from analysis for reproducibility across environments

### Current Contents

#### Lesson Materials

- `beamer/discriminant_analysis_presentation.typ` - Complete chapter presentation (Typst)
- `notes/discriminant_analysis_study_guide.typ` - Comprehensive study guide

#### Working Code Examples

```plaintext
code/
├── marketing_segmentation/    # Customer segmentation discriminant analysis
│   ├── fetch_marketing.py     # Generates synthetic customer behavior data
│   ├── marketing_lda.py       # Linear discriminant analysis for segmentation
│   ├── marketing_qda.py       # Quadratic discriminant analysis comparison
│   ├── marketing.csv          # 1,200 customers × 8 behavioral metrics
│   ├── marketing_scores.png   # Discriminant scores visualization
│   ├── marketing_boundaries.png # Classification boundaries
│   ├── README.md              # Marketing context and interpretation
│   └── MARKETING_DATA_DICTIONARY.md # Customer behavior definitions
├── quality_control/           # Manufacturing quality control classification
│   ├── fetch_quality.py       # Generates synthetic product quality data
│   ├── quality_lda.py         # Quality control discriminant analysis
│   ├── quality_stepwise.py    # Stepwise variable selection
│   ├── quality.csv            # 800 products × 6 quality measurements
│   ├── quality_confusion.png  # Confusion matrix visualization
│   ├── quality_roc.png        # ROC curve analysis
│   ├── README.md              # Manufacturing context and interpretation
│   └── QUALITY_DATA_DICTIONARY.md # Quality metric definitions
├── sports_analytics/          # Athlete performance classification
│   ├── fetch_sports.py        # Generates synthetic athlete performance data
│   ├── sports_lda.py          # Sports performance discriminant analysis
│   ├── sports_canonical.py    # Canonical discriminant functions
│   ├── sports.csv             # 300 athletes × 7 performance metrics
│   ├── sports_loadings.png    # Discriminant function loadings
│   ├── sports_centroids.png   # Group centroids visualization
│   └── README.md              # Sports analytics context and interpretation
└── EXAMPLES_OVERVIEW.md       # Comparative guide: LDA vs QDA applications
```

### Usage

#### Compile Presentation

```bash
cd beamer/
typst compile discriminant_analysis_presentation.typ
```

#### Run Working Examples

```bash
# Marketing segmentation example
.venv/bin/python code/marketing_segmentation/marketing_lda.py

# Quality control example
.venv/bin/python code/quality_control/quality_lda.py

# Sports analytics example
.venv/bin/python code/sports_analytics/sports_lda.py
```

### Educational Applications

#### In-Class Demonstrations

- **Marketing Segmentation**: Live demonstration of customer classification
- **Quality Control**: Real-time defect classification simulation
- **Sports Analytics**: Performance-based athlete categorization

#### Student Exercises

- Modify prior probabilities and observe classification changes
- Compare LDA vs QDA performance on different datasets
- Implement custom variable selection algorithms
- Validate models using cross-validation techniques

### Assessment Integration

The chapter examples complement the evaluation materials by providing:

- Foundational understanding before business case applications
- Technical implementation practice before assessment
- Domain-specific context for different application areas
- Progressive complexity from basic to advanced techniques

---

**Note**: This chapter provides both theoretical foundations and practical applications of discriminant analysis, preparing students for the advanced business case studies in the evaluations module.