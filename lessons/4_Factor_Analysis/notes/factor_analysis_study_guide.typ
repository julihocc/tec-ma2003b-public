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
