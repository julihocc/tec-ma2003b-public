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

== Applied Examples and Case Studies

This section presents detailed examples of Factor Analysis applications across different domains, illustrating the complete analytical process from data preparation to interpretation.

=== Case Study 1: Psychological Assessment - Big Five Personality

*Background:*
A researcher wants to validate the Big Five personality model using a 25-item personality questionnaire administered to 500 adults. Each item is rated on a 5-point Likert scale.

*Research Questions:*
1. Do the items cluster into five distinct personality factors?
2. How well do the factors correspond to theoretical expectations?
3. What is the reliability of each factor?

*Step-by-Step Analysis:*

*Data Preparation:*
- Sample: N = 500 adults
- Variables: 25 personality items (5 items per expected factor)
- Scale: 1 = Strongly Disagree to 5 = Strongly Agree
- Missing data: 2.3% handled via listwise deletion

*Factorability Assessment:*
- KMO = 0.87 (Good factorability)
- Bartlett's test: χ² = 4,832.5, df = 300, p \< 0.001
- All individual MSA values \> 0.75

*Factor Extraction:*
- Method: Principal Axis Factoring
- Initial eigenvalues: 6.84, 3.21, 2.67, 1.89, 1.43, 0.89, 0.76...
- Parallel analysis suggests 5 factors
- Five factors explain 64.2% of total variance

*Factor Rotation:*
- Method: Promax (oblique) - personality factors expected to correlate
- Factor correlations range from 0.12 to 0.38

*Factor Structure and Interpretation:*

*Factor 1: Extraversion (15.2% variance)*
```
Item                                    Loading
"I am the life of the party"              0.78
"I talk to a lot of different people"     0.74
"I feel comfortable around people"        0.71
"I start conversations"                   0.68
"I make friends easily"                   0.66
```

*Factor 2: Conscientiousness (12.8% variance)*
```
Item                                    Loading
"I am always prepared"                    0.81
"I pay attention to details"              0.76
"I get chores done right away"            0.73
"I like order"                           0.69
"I follow a schedule"                    0.65
```

*Factor 3: Neuroticism (11.7% variance)*
```
Item                                    Loading
"I get stressed out easily"               0.79
"I worry about things"                    0.75
"I get irritated easily"                  0.71
"I often feel blue"                      0.68
"I panic easily"                         0.63
```

*Factor 4: Agreeableness (12.3% variance)*
```
Item                                    Loading
"I sympathize with others' feelings"      0.77
"I have a soft heart"                     0.74
"I take time out for others"              0.70
"I feel others' emotions"                 0.67
"I make people feel at ease"              0.64
```

*Factor 5: Openness (12.2% variance)*
```
Item                                    Loading
"I have a vivid imagination"              0.76
"I have excellent ideas"                  0.73
"I am quick to understand things"         0.69
"I use difficult words"                   0.66
"I spend time reflecting on things"       0.62
```

*Results Summary:*
- All communalities \> 0.45
- No problematic cross-loadings (\> 0.40)
- Factor structure matches theoretical expectations
- Coefficient alpha reliability: 0.82-0.89 for all factors

*Interpretation:*
The analysis successfully replicated the Big Five personality structure with strong factor loadings and good reliability. The moderate factor intercorrelations (0.12-0.38) support the use of oblique rotation and align with personality theory.

=== Case Study 2: Market Research - Consumer Technology Preferences

*Background:*
A technology company surveyed 800 consumers about their preferences for smartphone features using 20 attributes rated on importance (1-7 scale).

*Research Objective:*
Identify underlying preference dimensions to guide product development and marketing strategy.

*Analysis Overview:*

*Preliminary Analysis:*
- KMO = 0.91 (Excellent)
- Bartlett's test significant (p \< 0.001)
- No multicollinearity issues detected

*Factor Solution:*
- Method: Maximum Likelihood with Varimax rotation
- Four factors extracted (eigenvalues \> 1.0)
- Total variance explained: 67.8%

*Factor Interpretation:*

*Factor 1: Performance & Technology (24.3% variance)*
- Processor speed (0.84)
- RAM capacity (0.79)
- Graphics performance (0.76)
- Operating system (0.71)
- Storage capacity (0.68)

*Factor 2: Design & Aesthetics (18.7% variance)*
- Physical appearance (0.82)
- Color options (0.78)
- Build quality (0.75)
- Weight and thickness (0.72)
- Screen size (0.65)

*Factor 3: Value & Practicality (13.9% variance)*
- Price affordability (0.81)
- Battery life (0.77)
- Durability (0.74)
- Warranty coverage (0.69)
- Repair availability (0.63)

*Factor 4: Connectivity & Features (10.9% variance)*
- Camera quality (0.79)
- Wireless capabilities (0.75)
- Apps availability (0.71)
- Internet speed (0.68)
- Social media integration (0.64)

*Business Implications:*
- Four distinct consumer segments identified
- Product positioning strategies developed for each factor
- Marketing messages tailored to preference dimensions
- Feature prioritization based on factor importance

=== Case Study 3: Educational Research - Academic Motivation

*Background:*
Educational researchers administered a 36-item Academic Motivation Scale to 650 university students to understand different types of academic motivation.

*Theoretical Framework:*
Self-Determination Theory predicts seven types of motivation:
1. Intrinsic Motivation (3 types)
2. Extrinsic Motivation (3 types)  
3. Amotivation (1 type)

*Analytical Challenge:*
Test whether the data supports the theoretical seven-factor structure versus alternative models.

*Model Comparison Approach:*

*Model 1: Seven-Factor Solution*
- Factors: IM-Knowledge, IM-Accomplishment, IM-Stimulation, EM-Identified, EM-Introjected, EM-External, Amotivation
- Fit: χ² = 892.3, df = 573, CFI = 0.94, RMSEA = 0.058
- All factor loadings \> 0.50
- Good interpretability

*Model 2: Three-Factor Solution*
- Factors: Intrinsic, Extrinsic, Amotivation
- Fit: χ² = 1,247.8, df = 591, CFI = 0.89, RMSEA = 0.078
- Some loss of discriminant validity

*Model 3: One-Factor Solution*
- Single "Academic Motivation" factor
- Fit: χ² = 2,156.4, df = 594, CFI = 0.71, RMSEA = 0.122
- Poor fit, not theoretically meaningful

*Results:*
The seven-factor model provided the best fit to the data, supporting the theoretical distinction between different types of academic motivation.

*Factor Correlations (Oblique Rotation):*
```
                   IM-K  IM-A  IM-S  EM-I  EM-J  EM-E  AMOT
IM-Knowledge        1.00
IM-Accomplishment   0.73  1.00
IM-Stimulation      0.68  0.71  1.00
EM-Identified       0.45  0.52  0.41  1.00
EM-Introjected      0.21  0.28  0.18  0.65  1.00
EM-External         0.08  0.12  0.05  0.43  0.58  1.00
Amotivation        -0.35 -0.41 -0.38 -0.52 -0.28 -0.15  1.00
```

The pattern shows expected relationships: intrinsic motivation types correlate positively with each other and negatively with amotivation.

=== Case Study 4: Health Research - Quality of Life Assessment

*Background:*
Medical researchers developed a quality of life questionnaire for cancer patients with 28 items across multiple life domains.

*Methodological Considerations:*
- Small sample size (N = 185) relative to variables
- Missing data due to patient fatigue
- Ordinal rating scales (0-4)
- Potential floor/ceiling effects

*Special Analytical Approaches:*

*Missing Data Handling:*
- Multiple imputation (m = 20 imputations)
- Analysis conducted on each imputed dataset
- Results pooled using Rubin's rules

*Ordinal Data Treatment:*
- Polychoric correlation matrix used
- Weighted least squares estimation
- Robust standard errors computed

*Factor Structure:*
Four factors emerged representing different quality of life domains:

*Factor 1: Physical Functioning*
- Physical symptoms and limitations
- Energy and fatigue levels
- Daily activity capacity

*Factor 2: Emotional Well-being*
- Anxiety and depression
- Mood and emotional state
- Coping with illness

*Factor 3: Social Functioning*
- Relationships with family/friends
- Social activities participation
- Support system quality

*Factor 4: Treatment Impact*
- Side effects management
- Treatment satisfaction
- Healthcare communication

*Validation Results:*
- Cross-validation with independent sample (N = 142)
- Coefficient of congruence \> 0.85 for all factors
- Convergent validity with established QOL measures
- Known-groups validity confirmed

=== Common Challenges and Solutions

*Challenge 1: Small Sample Sizes*
*Solutions:*
- Use more conservative factor retention criteria
- Focus on replication rather than exploration
- Consider item parceling for complex models
- Report confidence intervals for loadings

*Challenge 2: Mixed Data Types*
*Solutions:*
- Use appropriate correlation matrices (polychoric, tetrachoric)
- Consider categorical factor analysis methods
- Transform variables when appropriate
- Report sensitivity analyses

*Challenge 3: Cross-Loadings and Complex Structure*
*Solutions:*
- Try different rotation methods
- Consider hierarchical factor models
- Use confirmatory factor analysis
- Examine item content for ambiguity

*Challenge 4: Non-Normal Data*
*Solutions:*
- Use robust estimation methods
- Consider non-parametric alternatives
- Transform variables when appropriate
- Report distributional assumptions

*Challenge 5: Interpretation Difficulties*
*Solutions:*
- Examine multiple solutions (different numbers of factors)
- Consider theoretical expectations
- Use external validation criteria
- Consult domain experts

---

*Study Questions for Section 2.4:*
1. In the personality case study, why was oblique rotation chosen over orthogonal rotation?
2. How would you handle a situation where parallel analysis suggests 3 factors but theory predicts 5?
3. What are the advantages and disadvantages of using polychoric correlations for ordinal data?
4. How do you interpret factor correlations in an oblique solution?
5. What validation strategies are most appropriate for small sample factor analyses?
6. When might you choose a hierarchical factor model over a simple structure model?

== Software Implementation and Advanced Topics

This section covers practical software implementation of Factor Analysis and advanced methodological considerations for complex research scenarios.

=== Software Packages and Implementation

*Python Implementation:*

*Primary Libraries:*
- `factor_analyzer`: Dedicated Factor Analysis library
- `sklearn.decomposition`: PCA and Factor Analysis
- `scipy.stats`: Statistical tests and correlations
- `pandas`: Data manipulation
- `numpy`: Numerical computations

*Basic Factor Analysis Workflow in Python:*
```python
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
import pandas as pd
import numpy as np

# Load and prepare data
data = pd.read_csv('survey_data.csv')
X = data.select_dtypes(include=[np.number])

# Test factorability
kmo_all, kmo_model = calculate_kmo(X)
chi_square_value, p_value = calculate_bartlett_sphericity(X)

print(f'KMO: {kmo_model:.3f}')
print(f'Bartlett p-value: {p_value:.3f}')

# Determine number of factors
fa = FactorAnalyzer(rotation=None, n_factors=X.shape[1])
fa.fit(X)
eigenvalues = fa.get_eigenvalues()[0]

# Perform Factor Analysis
fa_final = FactorAnalyzer(n_factors=5, rotation='promax')
fa_final.fit(X)

# Extract results
loadings = fa_final.loadings_
communalities = fa_final.get_communalities()
factor_variance = fa_final.get_factor_variance()
```

*R Implementation:*

*Primary Packages:*
- `psych`: Comprehensive psychometric package
- `GPArotation`: Advanced rotation methods
- `corrplot`: Correlation visualization
- `lavaan`: Confirmatory Factor Analysis

*Basic Factor Analysis in R:*
```r
library(psych)
library(GPArotation)

# Load data
data <- read.csv("survey_data.csv")

# Test factorability
KMO(data)
cortest.bartlett(cor(data), n = nrow(data))

# Determine number of factors
fa.parallel(data, fa = "fa")
VSS(data, rotate = "varimax")

# Perform Factor Analysis
fa_result <- fa(data, nfactors = 5, rotate = "promax", fm = "pa")

# Examine results
print(fa_result, cut = 0.3, sort = TRUE)
fa.diagram(fa_result)
```

*SPSS Implementation:*

*Menu Path: Analyze → Dimension Reduction → Factor*

*Key Options:*
- Extraction: Principal Axis Factoring or Maximum Likelihood
- Rotation: Varimax (orthogonal) or Promax (oblique)
- Scores: Save factor scores as variables
- Options: KMO and Bartlett's test, communalities

*Critical SPSS Settings:*
- Extraction Criteria: Eigenvalues over 1, or fixed number
- Maximum Iterations: Increase to 100 for convergence
- Convergence: 0.001 for precise solutions
- Display: Sorted by size, suppress small coefficients

=== Advanced Factor Analysis Topics

=== Confirmatory Factor Analysis (CFA)

*When to Use CFA:*
- Testing specific theoretical models
- Validating measurement instruments
- Cross-group comparisons
- Longitudinal factor invariance

*CFA vs. Exploratory FA:*
```
Exploratory FA:
- Data-driven approach
- Discovers factor structure
- All variables can load on all factors
- Generates hypotheses

Confirmatory FA:
- Theory-driven approach
- Tests predetermined structure
- Specified loadings pattern
- Tests hypotheses
```

*Model Specification in CFA:*
- Fixed parameters (typically loadings set to 0)
- Free parameters (estimated from data)
- Constraints (equality restrictions)
- Identification requirements

*Fit Indices for CFA Models:*
- Chi-square test: Model vs. saturated model
- CFI (Comparative Fit Index): ≥ 0.95 excellent
- TLI (Tucker-Lewis Index): ≥ 0.95 excellent
- RMSEA (Root Mean Square Error): \< 0.06 excellent
- SRMR (Standardized Root Mean Residual): \< 0.08 good

=== Hierarchical Factor Analysis

*Concept:*
Higher-order factors that explain correlations among first-order factors.

*Model Structure:*
```
Second-Order Factor
    ├── First-Order Factor 1
    │   ├── Variable 1
    │   ├── Variable 2
    │   └── Variable 3
    ├── First-Order Factor 2
    │   ├── Variable 4
    │   ├── Variable 5
    │   └── Variable 6
    └── First-Order Factor 3
        ├── Variable 7
        ├── Variable 8
        └── Variable 9
```

*Applications:*
- Intelligence research (g-factor)
- Personality assessment (higher-order traits)
- Quality of life measurement
- Organizational behavior

*Advantages:*
- Parsimonious representation
- Theoretical alignment
- Explains factor correlations
- Hierarchical interpretation

=== Bifactor Models

*Structure:*
All variables load on a general factor plus specific factors.

*Key Features:*
- General factor: Common to all variables
- Specific factors: Orthogonal to general factor
- No correlations between specific factors
- Direct modeling of multidimensionality

*When to Use:*
- Unidimensionality assumption violated
- Interest in general and specific components
- Educational and psychological testing
- Quality control applications

*Model Comparison:*
```
Traditional Model: F1 ↔ F2 ↔ F3 (correlated factors)
Hierarchical Model: G → F1, F2, F3 (higher-order)
Bifactor Model: G + S1, S2, S3 (general + specific)
```

=== Factor Analysis with Ordinal Data

*Challenges with Ordinal Data:*
- Pearson correlations underestimate relationships
- Distributional assumptions violated
- Floor and ceiling effects
- Limited response categories

*Polychoric Correlations:*
Assume underlying continuous variables for ordinal responses.

*Estimation Methods:*
- Weighted Least Squares (WLS)
- Diagonally Weighted Least Squares (DWLS)
- Robust Maximum Likelihood
- Bayesian estimation

*Practical Considerations:*
- Minimum 5 response categories preferred
- Check threshold parameters
- Examine residuals carefully
- Consider alternative models

=== Missing Data in Factor Analysis

*Missing Data Mechanisms:*
- MCAR (Missing Completely at Random)
- MAR (Missing at Random)
- MNAR (Missing Not at Random)

*Handling Strategies:*

*1. Listwise Deletion:*
- Simple but reduces sample size
- Assumes MCAR mechanism
- May introduce bias

*2. Pairwise Deletion:*
- Uses available data for each correlation
- May produce non-positive definite matrices
- Inconsistent sample sizes

*3. Multiple Imputation:*
- Creates multiple complete datasets
- Accounts for uncertainty
- Requires MAR assumption

*4. Full Information Maximum Likelihood (FIML):*
- Uses all available information
- Efficient and unbiased under MAR
- Available in SEM software

*Best Practices:*
- Examine missing data patterns
- Test missing data assumptions
- Use appropriate method for mechanism
- Report sensitivity analyses

=== Factor Score Estimation

*Methods for Computing Factor Scores:*

*1. Regression Method:*
$ hat(bold(F)) = bold(Lambda)^top bold(R)^(-1) bold(X) $

- Minimizes squared error
- Correlated even for orthogonal factors
- Most commonly used

*2. Bartlett Method:*
$ hat(bold(F)) = (bold(Lambda)^top bold(Psi)^(-1) bold(Lambda))^(-1) bold(Lambda)^top bold(Psi)^(-1) bold(X) $

- Unbiased estimates
- Preserves factor correlations
- Computationally intensive

*3. Anderson-Rubin Method:*
- Orthogonal scores
- Unit variance
- Zero correlations maintained

*Choosing Score Method:*
- Regression: General purpose, most interpretable
- Bartlett: When factor correlations important
- Anderson-Rubin: When orthogonality required

*Factor Score Applications:*
- Further statistical analyses
- Group comparisons
- Predictive modeling
- Clustering analysis

=== Advanced Rotation Methods

*Gradient Projection Algorithms:*
- Faster convergence
- Better local optima
- Handles constraints efficiently

*Procrustes Rotation:*
- Rotates to target matrix
- Cross-study comparisons
- Theoretical alignment

*Independent Cluster Rotation:*
- Separate rotation of clusters
- Complex factor structures
- Exploratory-confirmatory hybrid

*Robust Rotation Methods:*
- Outlier-resistant
- Non-normal data
- Contaminated samples

=== Model Selection and Comparison

*Information Criteria:*
- AIC (Akaike Information Criterion)
- BIC (Bayesian Information Criterion)
- Sample-size adjusted BIC
- CAIC (Consistent AIC)

*Cross-Validation Approaches:*
- Split-sample validation
- K-fold cross-validation
- Bootstrap validation
- Permutation tests

*Nested Model Comparisons:*
- Likelihood ratio tests
- Chi-square difference tests
- Sequential model building
- Parsimony considerations

*Non-Nested Comparisons:*
- Information criteria
- Predictive accuracy
- Theoretical coherence
- Practical utility

=== Contemporary Developments

*Machine Learning Integration:*
- Factor Analysis as dimensionality reduction
- Integration with clustering algorithms
- Deep learning applications
- Automated model selection

*Bayesian Factor Analysis:*
- Prior specification
- Posterior distributions
- Model uncertainty
- Flexible modeling frameworks

*Network Psychometrics:*
- Alternative to latent variable models
- Direct variable relationships
- Partial correlation networks
- Dynamic systems approach

*Big Data Considerations:*
- Scalable algorithms
- Streaming factor analysis
- Distributed computing
- Approximate methods

---

= Conclusion and Summary

This comprehensive study guide has covered the theoretical foundations, practical implementation, and advanced applications of Principal Component Analysis and Factor Analysis. These powerful multivariate techniques provide researchers with tools to:

- Reduce data dimensionality while preserving essential information
- Discover underlying latent structures in complex datasets
- Validate theoretical models and measurement instruments
- Extract meaningful patterns from large-scale surveys and assessments

*Key Takeaways:*

*Methodological Rigor:*
- Proper assessment of data suitability is crucial
- Multiple criteria should guide factor retention decisions
- Rotation method selection impacts interpretability
- Validation is essential for reliable results

*Practical Application:*
- Software implementation requires understanding of underlying theory
- Real-world data presents challenges requiring adaptive strategies
- Domain expertise enhances statistical analysis
- Communication of results must balance technical accuracy with accessibility

*Future Directions:*
- Integration with machine learning methods
- Handling of big data and streaming applications
- Development of robust methods for complex data
- Advancement in Bayesian and network approaches

The field continues to evolve with new methodological developments and computational advances, making these techniques increasingly powerful and accessible for researchers across disciplines.

---

*Final Study Questions - Integration and Application:*
1. Compare and contrast the assumptions and applications of PCA versus Factor Analysis.
2. Design a complete factor analysis study for your research area, including power analysis and validation strategy.
3. How would you handle a dataset with mixed continuous and ordinal variables in factor analysis?
4. What are the trade-offs between exploratory and confirmatory approaches in factor analysis?
5. How do modern machine learning approaches complement traditional factor analysis methods?
6. What ethical considerations arise when using factor analysis in high-stakes assessment contexts?

*Recommended Further Reading:*
- Fabrigar, L. R., & Wegener, D. T. (2012). *Exploratory Factor Analysis*
- Brown, T. A. (2015). *Confirmatory Factor Analysis for Applied Research*
- Hayton, J. C., Allen, D. G., & Scarpello, V. (2004). Factor retention decisions in exploratory factor analysis
- Howard, M. C. (2016). A review of exploratory factor analysis decisions and overview of current practices
