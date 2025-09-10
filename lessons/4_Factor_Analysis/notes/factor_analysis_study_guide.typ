// Factor Analysis Study Guide - Comprehensive Lecture Notes
// Dr. Juliho Castillo - Tecnológico de Monterrey

#set document(
  title: "Factor Analysis Study Guide",
  author: "Dr. Juliho Castillo"
)

#set page(
  margin: (x: 2.5cm, y: 2cm)
)

#set text(
  font: "Liberation Sans",
  size: 11pt
)

#set heading(numbering: "1.1.")

#align(center)[
  #text(size: 24pt, weight: "bold")[Factor Analysis Study Guide]
  
  #v(0.5cm)
  #text(size: 14pt)[Comprehensive Lecture Notes]
  
  #v(0.3cm)
  #text(size: 12pt)[Dr. Juliho Castillo]
  
  #text(size: 12pt)[Tecnológico de Monterrey]
  
  #v(0.3cm)
  #text(size: 10pt)[#datetime.today().display()]
]

#v(1cm)

#outline()

#pagebreak()

= Introduction

This study guide provides comprehensive coverage of Principal Component Analysis (PCA) and Factor Analysis, two fundamental multivariate statistical techniques. The material is organized to help students understand both the theoretical foundations and practical applications of these methods.

*Learning Objectives:*
- Understand the mathematical foundations of PCA and Factor Analysis
- Learn when to apply each method appropriately
- Gain hands-on experience through real-world examples
- Develop skills in interpreting and communicating results

= Theoretical Foundations

== Principal Component Analysis (PCA) Theory

=== What is Principal Component Analysis?

Principal Component Analysis (PCA) is a fundamental technique in multivariate statistics and data science. At its core, PCA is a *linear transformation* that reduces the dimensionality of data while preserving as much variance as possible.

*Key Characteristics:*
- *Dimension Reduction*: Transforms high-dimensional data into a lower-dimensional space
- *Variance Maximization*: Each principal component captures the maximum possible variance
- *Orthogonality*: Principal components are uncorrelated (orthogonal to each other)
- *Linear Transformation*: Components are linear combinations of original variables

*Primary Applications:*
1. *Data Visualization*: Reducing data to 2D or 3D for plotting
2. *Noise Reduction*: Filtering out low-variance components
3. *Feature Engineering*: Creating new features for machine learning
4. *Exploratory Data Analysis*: Understanding data structure and patterns

=== Mathematical Foundation

Let $bold(X)$ be an $n times p$ data matrix where:
- $n$ = number of observations (rows)
- $p$ = number of variables (columns)
- Each row represents one observation
- Each column represents one variable

*Step 1: Data Centering*

First, we center the data by subtracting the mean from each variable:
$ bold(X)_"centered" = bold(X) - bold(1)_n bold(mu)^top $

where $bold(mu) = (mu_1, mu_2, ..., mu_p)^top$ is the vector of variable means.

*Step 2: Covariance Matrix*

The sample covariance matrix is:
$ bold(S) = frac(1, n-1) bold(X)_"centered"^top bold(X)_"centered" $

For standardized analysis (correlation matrix), we first standardize each variable:
$ bold(R) = frac(1, n-1) bold(Z)^top bold(Z) $

where $bold(Z)$ contains standardized variables (mean 0, variance 1).

*Step 3: Eigendecomposition*

The heart of PCA is the eigendecomposition of the covariance (or correlation) matrix:
$ bold(S) bold(v)_j = lambda_j bold(v)_j $

where:
- $lambda_1 >= lambda_2 >= ... >= lambda_p >= 0$ are eigenvalues
- $bold(v)_1, bold(v)_2, ..., bold(v)_p$ are corresponding eigenvectors
- Eigenvectors are orthonormal: $bold(v)_i^top bold(v)_j = delta_(i j)$

*Step 4: Principal Components*

The $j$-th principal component for observation $i$ is:
$ "PC"_(i j) = bold(v)_j^top (bold(x)_i - bold(mu)) $

In matrix form, the principal component scores are:
$ bold(Y) = bold(X)_"centered" bold(V) $

where $bold(V) = [bold(v)_1, bold(v)_2, ..., bold(v)_p]$ is the matrix of eigenvectors.

=== Variance Explained

Each principal component explains a specific amount of variance:

*Individual Variance:*
$ "Var"("PC"_j) = lambda_j $

*Proportion of Variance Explained:*
$ "Proportion"_j = frac(lambda_j, sum_(k=1)^p lambda_k) $

*Cumulative Variance Explained:*
$ "Cumulative"_j = frac(sum_(k=1)^j lambda_k, sum_(k=1)^p lambda_k) $

*Important Property:*
The total variance is preserved: $sum_(j=1)^p lambda_j = sum_(j=1)^p "Var"(X_j)$

=== Practical Implementation Steps

*Step 1: Data Preparation*
```
1. Check for missing values and outliers
2. Decide on standardization:
   - Use correlation matrix if variables have different scales
   - Use covariance matrix if variables are on similar scales
3. Center (and possibly standardize) the data
```

*Step 2: Compute PCA*
```
1. Calculate covariance or correlation matrix
2. Perform eigendecomposition
3. Sort eigenvalues and eigenvectors in descending order
4. Compute principal component scores
```

*Step 3: Determine Number of Components*
```
1. Kaiser criterion: retain components with eigenvalue > 1
2. Scree plot: look for "elbow" where slope levels off
3. Cumulative variance: retain components explaining 70-90% of variance
4. Parallel analysis: compare to random data eigenvalues
```

*Step 4: Interpretation*
```
1. Examine component loadings (eigenvectors)
2. Identify which variables contribute most to each component
3. Name components based on variable patterns
4. Validate interpretation with domain knowledge
```

=== Component Loadings and Interpretation

The eigenvectors $bold(v)_j$ are called *loadings* and show how each original variable contributes to each principal component.

*Loading Interpretation:*
- Large absolute loading: variable strongly influences the component
- Positive loading: variable and component move in same direction
- Negative loading: variable and component move in opposite directions
- Small loading: variable has little influence on the component

*Rotation Consideration:*
Unlike Factor Analysis, PCA typically does not use rotation because:
- Rotation would redistribute variance among components
- The goal is maximum variance explanation, not interpretability
- Each component is defined to be orthogonal and capture maximum residual variance

=== Key Assumptions and Limitations

*Assumptions:*
1. *Linearity*: Relationships between variables are linear
2. *Large Sample Size*: Generally need $n > p$ (more observations than variables)
3. *Continuous Variables*: Works best with continuous, normally distributed variables
4. *No Perfect Multicollinearity*: Variables should not be perfectly correlated

*Limitations:*
1. *Interpretability*: Components may not have clear substantive meaning
2. *All Variance*: Includes both signal and noise variance
3. *Linear Only*: Cannot capture nonlinear relationships
4. *Outlier Sensitivity*: Sensitive to extreme values
5. *Scale Dependency*: Results depend on whether data is standardized

---

*Study Questions for Section 2.1:*
1. What is the fundamental goal of PCA?
2. Why do we center the data before computing PCA?
3. What does it mean for principal components to be orthogonal?
4. How do you interpret a component loading of -0.8 for a variable?
5. When would you use the correlation matrix vs. covariance matrix?

== Factor Analysis Theory

=== What is Factor Analysis?

Factor Analysis (FA) is a statistical method designed to model the relationships among observed variables through a smaller number of unobserved variables called *latent factors* or *common factors*. Unlike PCA, which focuses on variance maximization, Factor Analysis explicitly models the underlying structure that generates the observed correlations.

*Fundamental Concept:*
Factor Analysis assumes that observed variables are *manifestations* of underlying latent constructs. These latent factors cannot be directly measured but influence multiple observable variables.

*Key Distinctions from PCA:*
- *Purpose*: Models latent constructs rather than reducing dimensions
- *Variance*: Separates common variance from unique variance
- *Error Modeling*: Explicitly accounts for measurement error
- *Theory Testing*: Designed to test specific theoretical factor structures

*Primary Applications:*
1. *Psychological Testing*: Measuring intelligence, personality traits, attitudes
2. *Market Research*: Understanding consumer preferences and behavior patterns
3. *Educational Assessment*: Identifying academic ability factors
4. *Medical Research*: Discovering disease symptom clusters
5. *Social Sciences*: Measuring abstract concepts like socioeconomic status

=== The Factor Analysis Model

The core Factor Analysis model expresses each observed variable as a linear combination of common factors plus a unique component:

$ X_i = lambda_(i,1) F_1 + lambda_(i,2) F_2 + ... + lambda_(i,k) F_k + U_i $

where:
- $X_i$ = $i$-th observed variable (standardized)
- $F_j$ = $j$-th common factor ($j = 1, 2, ..., k$)
- $lambda_(i,j)$ = factor loading of variable $i$ on factor $j$
- $U_i$ = unique factor for variable $i$
- $k$ = number of common factors (typically $k << p$)

*In Matrix Form:*
$ bold(X) = bold(Lambda) bold(F) + bold(U) $

where:
- $bold(X)$ = $p times 1$ vector of observed variables
- $bold(Lambda)$ = $p times k$ matrix of factor loadings
- $bold(F)$ = $k times 1$ vector of common factors
- $bold(U)$ = $p times 1$ vector of unique factors

=== Model Assumptions

*Assumptions about Factors:*
1. $E[bold(F)] = bold(0)$ (factors have zero mean)
2. $"Var"(bold(F)) = bold(I)$ (factors are standardized and uncorrelated)
3. $E[bold(U)] = bold(0)$ (unique factors have zero mean)
4. $"Cov"(bold(F), bold(U)) = bold(0)$ (common and unique factors are uncorrelated)
5. $"Cov"(bold(U)) = bold(Psi)$ (unique factors may be correlated in some models)

*Classical Factor Model Assumptions:*
In the classical model, unique factors are also assumed uncorrelated:
$ "Cov"(U_i, U_j) = 0 text(" for ") i != j $

This means $bold(Psi) = "diag"(psi_1, psi_2, ..., psi_p)$.

=== Variance Decomposition

Factor Analysis provides a fundamental decomposition of each variable's variance:

*Total Variance = Common Variance + Unique Variance*

For variable $i$:
$ "Var"(X_i) = sum_(j=1)^k lambda_(i,j)^2 + psi_i = h_i^2 + psi_i $

where:
- $h_i^2 = sum_(j=1)^k lambda_(i,j)^2$ = *communality* (variance explained by common factors)
- $psi_i$ = *unique variance* (specific variance + error variance)

*Key Concepts:*
- *Communality* ($h_i^2$): Proportion of variable's variance explained by common factors
- *Uniqueness* ($psi_i$): Proportion of variance not explained by common factors
- *Specific Variance*: Systematic variance unique to one variable
- *Error Variance*: Random measurement error

=== The Correlation Structure

Under the factor model, the correlation matrix has a specific structure:

$ bold(R) = bold(Lambda) bold(Lambda)^top + bold(Psi) $

This fundamental equation shows that:
- Correlations between variables arise from shared common factors
- The diagonal elements equal 1.0 (correlation of variable with itself)
- Off-diagonal elements depend on factor loadings

*Reduced Correlation Matrix:*
The *reduced correlation matrix* replaces the diagonal 1's with communality estimates:
$ bold(R)^* = bold(Lambda) bold(Lambda)^top $

This matrix contains only the variance attributable to common factors.

=== Factor Extraction Methods

Several methods exist for estimating factor loadings:

*1. Principal Axis Factoring (PAF)*
- Most common method
- Iteratively estimates communalities
- Uses reduced correlation matrix
- Procedure:
  1. Start with initial communality estimates
  2. Perform eigendecomposition of reduced correlation matrix
  3. Extract factors and update communality estimates
  4. Repeat until convergence

*2. Maximum Likelihood (ML)*
- Assumes multivariate normal distribution
- Provides statistical tests for number of factors
- Allows goodness-of-fit testing
- Computationally more intensive

*3. Principal Components Method*
- Uses principal components as initial solution
- Simpler but less theoretically justified
- May overextract factors

*4. Minimum Residual (MINRES)*
- Minimizes squared residuals
- Good compromise between PAF and ML
- Robust to distributional assumptions

=== Determining the Number of Factors

*1. Kaiser Criterion*
- Retain factors with eigenvalues > 1.0
- Applied to reduced correlation matrix
- May overextract in some cases

*2. Scree Test*
- Plot eigenvalues and look for "elbow"
- Retain factors before the sharp drop
- Subjective but often effective

*3. Parallel Analysis*
- Compare eigenvalues to those from random data
- More accurate than Kaiser criterion
- Accounts for sampling variability

*4. Theoretical Considerations*
- Based on substantive theory
- Number of expected constructs
- Interpretability of factors

*5. Goodness-of-Fit Tests (ML only)*
- Chi-square test for model fit
- Various fit indices (CFI, TLI, RMSEA)
- Formal statistical criteria

=== Factor Rotation

Raw factor solutions are often difficult to interpret. *Factor rotation* seeks a more interpretable solution while maintaining the same overall fit.

*Goals of Rotation:*
- Achieve "simple structure"
- Each variable loads highly on few factors
- Each factor is defined by several variables
- Minimize cross-loadings

*Types of Rotation:*

*Orthogonal Rotation* (factors remain uncorrelated):
- *Varimax*: Maximizes variance of squared loadings within factors
- *Quartimax*: Minimizes number of factors needed to explain each variable
- *Equamax*: Compromise between Varimax and Quartimax

*Oblique Rotation* (factors allowed to correlate):
- *Promax*: Oblique version of Varimax
- *Direct Oblimin*: Controls degree of correlation between factors
- *Harris-Kaiser*: Orthogonal followed by oblique transformation

*Choosing Rotation Method:*
- Use orthogonal if factors should be uncorrelated theoretically
- Use oblique if factors are expected to correlate
- Varimax is most popular for orthogonal rotation
- Promax is most popular for oblique rotation

=== Interpretation Guidelines

*Factor Loading Interpretation:*
- $|lambda_(i,j)| >= 0.70$: Excellent indicator of factor
- $|lambda_(i,j)| >= 0.60$: Good indicator of factor
- $|lambda_(i,j)| >= 0.50$: Fair indicator of factor
- $|lambda_(i,j)| >= 0.40$: Poor but possibly significant
- $|lambda_(i,j)| < 0.40$: Generally not interpretable

*Cross-Loadings:*
- Variables should load highly on one factor
- Cross-loadings > 0.40 may indicate:
  - Variable measures multiple constructs
  - Need for additional factors
  - Poor item design

*Factor Naming:*
- Examine variables with highest loadings
- Consider theoretical meaning
- Use domain knowledge
- Avoid over-interpretation

=== Model Evaluation

*Communality Assessment:*
- High communalities ($h^2 > 0.70$): Variables well-explained by factors
- Low communalities ($h^2 < 0.40$): Variables poorly explained
- Very low communalities may indicate:
  - Variable doesn't belong in analysis
  - Additional factors needed
  - Measurement problems

*Overall Model Fit:*
- Proportion of variance explained by common factors
- Residual correlations should be small
- Theoretical sensibility of factor structure

*Replication and Validation:*
- Cross-validation with independent samples
- Confirmatory factor analysis
- External validity checks

---

*Study Questions for Section 2.2:*
1. What is the key difference between Factor Analysis and PCA in terms of their goals?
2. Explain the concept of communality and how it differs from total variance.
3. Why is factor rotation necessary, and when would you choose oblique over orthogonal rotation?
4. How do you interpret a factor loading of 0.75 for a variable on a factor?
5. What does it mean when a variable has low communality in a factor analysis?

== Practical Implementation of Factor Analysis

=== Step-by-Step Factor Analysis Process

Factor Analysis involves a systematic sequence of steps, each requiring careful consideration and validation. This section provides a comprehensive guide to conducting Factor Analysis in practice.

=== Step 1: Data Preparation and Assessment

*Data Requirements:*
- *Sample Size*: Minimum 5-10 observations per variable
- *Recommended*: At least 200 observations for stable results
- *Variables*: Continuous or ordinal variables
- *Missing Data*: Handle before analysis (listwise deletion, imputation)

*Data Quality Checks:*
1. *Outliers*: Identify and handle extreme values
2. *Normality*: Check distribution of variables (especially for ML estimation)
3. *Linearity*: Examine scatterplots between variables
4. *Multicollinearity*: Check for extremely high correlations (r > 0.90)

*Variable Selection:*
- Include variables theoretically related to expected factors
- Remove variables with very low correlations with others
- Consider reverse-coding negatively worded items
- Ensure adequate representation of each expected factor

=== Step 2: Testing Factorability

Before conducting Factor Analysis, verify that the data is suitable for factoring.

*Correlation Matrix Inspection:*
- Most correlations should be ≥ 0.30
- Look for patterns suggesting underlying factors
- Identify variables that don't correlate with others

*Kaiser-Meyer-Olkin (KMO) Test:*
$ "KMO" = (sum sum r_(i j)^2) / (sum sum r_(i j)^2 + sum sum a_(i j)^2) $

where $a_(i j)$ are partial correlations.

*KMO Interpretation:*
- KMO ≥ 0.90: Excellent factorability
- KMO ≥ 0.80: Good factorability  
- KMO ≥ 0.70: Adequate factorability
- KMO ≥ 0.60: Marginal factorability
- KMO \< 0.60: Poor factorability (consider removing variables)

*Bartlett's Test of Sphericity:*
Tests the null hypothesis: $H_0: bold(R) = bold(I)$ (correlation matrix is identity)

A significant result (p \< 0.05) indicates that Factor Analysis is appropriate.

*Anti-image Correlation Matrix:*
- Examine diagonal elements (MSA values)
- Variables with MSA \< 0.50 should be considered for removal
- Off-diagonal elements should be small

=== Step 3: Factor Extraction

*Choosing Extraction Method:*

*Principal Axis Factoring (PAF) - Most Common:*
```
1. Start with communality estimates in diagonal
2. Compute eigenvalues and eigenvectors of reduced R
3. Extract factors based on eigenvalues > 0
4. Compute new communality estimates
5. Repeat until convergence
```

*Maximum Likelihood (ML) - When Normality Assumed:*
```
1. Assume multivariate normal distribution
2. Iteratively estimate parameters
3. Provides goodness-of-fit tests
4. Allows statistical inference
```

*Implementation Considerations:*
- PAF is more robust to distributional violations
- ML provides formal statistical tests
- Both methods usually yield similar results
- Start with PAF for exploratory analysis

=== Step 4: Determining Number of Factors

*Multiple Criteria Approach:*

*1. Eigenvalue Criteria:*
- Kaiser Rule: Retain factors with eigenvalues > 1.0
- Modified Kaiser Rule: Use for correlation matrices only
- Plot eigenvalues (scree plot)

*2. Parallel Analysis:*
```
For each number of factors k:
1. Generate random correlation matrices
2. Compute mean eigenvalues from random data
3. Compare actual eigenvalues to random ones
4. Retain factors where actual > random
```

*3. Percentage of Variance:*
- Retain factors explaining meaningful variance
- Social sciences: 50-60% total variance
- Natural sciences: 80%+ total variance

*4. Interpretability:*
- Can factors be meaningfully named?
- Do factors make theoretical sense?
- Are factors sufficiently different?

*5. Statistical Tests (ML only):*
- Chi-square test for number of factors
- Likelihood ratio tests
- Information criteria (AIC, BIC)

*Decision Strategy:*
1. Apply multiple criteria
2. Consider theoretical expectations
3. Examine interpretability of solutions
4. Choose most parsimonious interpretable solution

=== Step 5: Factor Rotation

*Rotation Goals:*
- Achieve simple structure
- Maximize interpretability
- Minimize cross-loadings

*Rotation Decision Tree:*
```
Are factors expected to be correlated?
├─ Yes → Use Oblique Rotation
│   ├─ Promax (most common)
│   ├─ Direct Oblimin
│   └─ Harris-Kaiser
└─ No → Use Orthogonal Rotation
    ├─ Varimax (most common)
    ├─ Quartimax
    └─ Equamax
```

*Rotation Procedure:*
1. Start with unrotated solution
2. Apply chosen rotation method
3. Examine factor loading matrix
4. Check for simple structure
5. Consider alternative rotations if needed

*Evaluating Rotation Quality:*
- High loadings (>0.50) on target factors
- Low cross-loadings (\<0.40)
- Each factor defined by multiple variables
- Factors are interpretable

=== Step 6: Interpretation and Naming

*Factor Interpretation Process:*

*1. Examine Factor Loadings:*
- Focus on loadings ≥ |0.50|
- Consider both positive and negative loadings
- Look for patterns across variables

*2. Identify Marker Variables:*
- Variables with highest loadings on each factor
- Variables that load on only one factor
- Use these to understand factor meaning

*3. Factor Naming Strategy:*
- Examine content of highest-loading variables
- Consider theoretical framework
- Use descriptive, meaningful names
- Avoid over-interpretation

*Example Interpretation Process:*
```
Factor 1 Loadings:
- Math Achievement: 0.85
- Science Achievement: 0.78
- Reading Achievement: 0.72
- Vocabulary: 0.65

Interpretation: "Academic Achievement" factor
```

*4. Check for Problematic Patterns:*
- Factors with few indicator variables (\<3)
- Variables that don't load substantially on any factor
- Factors that are difficult to interpret
- Unexpected cross-loadings

=== Step 7: Model Evaluation and Validation

*Adequacy of Factor Solution:*

*1. Communality Assessment:*
- Examine communalities for each variable
- Low communalities (\<0.40) indicate poor fit
- Consider removing poorly explained variables

*2. Residual Analysis:*
- Examine residual correlations
- Large residuals suggest additional factors needed
- Systematic patterns in residuals indicate model problems

*3. Percentage of Variance Explained:*
- Total variance explained by common factors
- Variance explained by each factor
- Compare to established benchmarks

*4. Theoretical Consistency:*
- Do factors match theoretical expectations?
- Are factor intercorrelations reasonable?
- Can results be replicated?

*Validation Strategies:*

*1. Cross-Validation:*
- Split sample randomly
- Conduct FA on each half
- Compare factor structures
- Use coefficient of congruence

*2. Confirmatory Factor Analysis:*
- Test specific factor structure
- Use structural equation modeling
- Assess model fit indices
- Compare alternative models

*3. External Validation:*
- Correlate factors with external criteria
- Examine predictive validity
- Test known-groups validity
- Assess convergent/discriminant validity

=== Step 8: Reporting Results

*Essential Elements to Report:*

*1. Sample and Variables:*
- Sample size and characteristics
- Number and type of variables
- Missing data handling

*2. Factorability Assessment:*
- KMO measure
- Bartlett's test results
- Any variables removed

*3. Extraction Details:*
- Method used (PAF, ML, etc.)
- Criteria for number of factors
- Total variance explained

*4. Rotation Information:*
- Type of rotation used
- Rationale for choice

*5. Factor Structure:*
- Factor loading matrix
- Factor correlations (if oblique)
- Communalities

*6. Interpretation:*
- Factor names and descriptions
- Theoretical implications
- Limitations and assumptions

*Common Reporting Mistakes to Avoid:*
- Reporting only rotated or only unrotated loadings
- Not reporting communalities
- Insufficient detail about methodology
- Over-interpreting small loadings
- Not discussing limitations

---

*Study Questions for Section 2.3:*
1. What is the minimum recommended sample size for Factor Analysis and why?
2. How do you interpret a KMO value of 0.65?
3. What is the difference between Bartlett's test and the KMO test?
4. When would you choose Maximum Likelihood over Principal Axis Factoring?
5. What makes a factor solution "interpretable"?
6. How do you validate a factor analysis solution?
