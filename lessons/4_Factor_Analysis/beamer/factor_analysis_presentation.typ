// Complete Factor Analysis Presentation - RESTRUCTURED
// Pedagogical approach: PCA theory → FA theory → Theory comparison → Examples with PCA → FA → Comparison pattern

// Tec de Monterrey color palette
#let tec-blue = rgb("#003f7f")      // Tec de Monterrey signature blue
#let tec-light-blue = rgb("#0066cc") // Lighter blue for accents

#set page(
  width: 16cm,
  height: 9cm,
  margin: (x: 1.5cm, y: 1cm),
  numbering: "1",
)

#set document(
  title: "Factor Analysis",
  author: "Dr. Juliho Castillo",
)

#set text(
  font: "Liberation Sans",
  size: 12pt,
  lang: "es",
)
#set math.equation(numbering: "(1)")

// Custom slide function with Tec blue titles
#let slide(title: none, content) = {
  pagebreak(weak: true)
  if title != none [
    #set text(size: 18pt, weight: "bold", fill: tec-blue)
    #title
    #v(0.8cm)
  ]
  content
}


// Section slide function with Tec blue
#let section-slide(title) = {
  pagebreak(weak: true)
  // Create invisible heading for table of contents after page break
  hide[#heading(level: 2, outlined: true, bookmarked: true)[#title]]
  set text(size: 20pt, weight: "bold", fill: tec-blue)
  align(center + horizon)[#title]
}

// Part slide function with Tec blue
#let part-slide(title) = {
  pagebreak(weak: true)
  set text(size: 24pt, weight: "bold", fill: tec-blue)
  align(center + horizon)[#title]
}

// Title slide with Tec colors
#align(center)[
  #v(2cm)
  #text(size: 28pt, weight: "bold", fill: tec-blue)[Factor Analysis]
  #v(0.6cm)
  #text(size: 16pt, fill: tec-light-blue)[Dr. Juliho Castillo]
  #v(0.4cm)
  #text(size: 14pt, fill: tec-blue)[Tecnológico de Monterrey]
  #v(0.4cm)
  #text(size: 12pt)[#datetime.today().display()]
]

// Table of contents
#slide(title: [Table of contents])[
  #outline()
]

// ============================================================================
// PART I: THEORETICAL FOUNDATIONS
// ============================================================================

#part-slide[Part I: Theoretical Foundations]

#section-slide[Principal Component Analysis Theory]

#slide(title: [Understanding PCA: The Big Picture])[
  *Imagine you're a photographer trying to capture the best view of a 3D sculpture.*

  You want to find the *single best angle* that shows the most interesting features and variations of the sculpture. That's essentially what Principal Component Analysis does with data!

  *What PCA does in simple terms:*
  - Takes your data with many variables (dimensions)
  - Finds the "best directions" to look at your data
  - These directions capture the most variation and patterns
  - Reduces complexity while keeping the most important information

  *Why is this useful?*
  - Makes complex data easier to visualize and understand
  - Removes noise and redundant information
  - Helps identify the most important patterns in your data
]

#slide(title: [Refresher: What is PCA?])[
  - Principal Component Analysis (PCA) is a linear method for *dimension reduction*.
  - It finds orthogonal directions (principal components) that capture the largest possible variance in the data.
  - PCA produces new variables (components) that are linear combinations of the original observed variables.
  - Use cases: visualization, noise reduction, pre-processing before supervised learning, and exploratory data analysis.
]

#slide(title: [Refresher: Eigen Decomposition])[
  Eigen decomposition is a fundamental matrix factorization technique used in multivariate analysis.

  *Definition*: For a square matrix $bold(A)$, if it can be diagonalized, we can write:
  $bold(A) = bold(P) bold(D) bold(P)^(-1)$

  Where:
  - $bold(D)$ is a diagonal matrix containing the eigenvalues $lambda_1, lambda_2, ..., lambda_n$
  - $bold(P)$ is the matrix whose columns are the eigenvectors $bold(v)_1, bold(v)_2, ..., bold(v)_n$
  - Each eigenvector satisfies: $bold(A) bold(v)_j = lambda_j bold(v)_j$

  *Deeper Meaning and Significance:*
  - *Eigenvalues* ($lambda_j$) measure the "strength" or "importance" of each underlying pattern in your data
  - *Eigenvectors* ($bold(v)_j$) reveal the "direction" or "profile" of these patterns
  - This decomposition is fundamental because it *separates complex multivariate relationships into independent, interpretable components*
  - In factor analysis context: eigenvalues help determine how many meaningful factors exist, while eigenvectors show how variables cluster together

  *For symmetric matrices* (like covariance matrices in PCA/FA):
  - The eigenvectors are orthonormal ($bold(P)^top bold(P) = bold(I)$)
  - The decomposition simplifies to: $bold(A) = bold(P) bold(D) bold(P)^top$

  *Geometric interpretation*: Eigenvectors represent directions of maximum variance, eigenvalues represent the magnitude of variance in those directions.

  *In multivariate statistics*: This decomposition underlies both PCA (principal components) and Factor Analysis (latent factors).

  _For detailed matrix algebra foundations, see Appendix._
]

#slide(title: [Why PCA Works: The Big Idea])[
  *The Goal:* Find the direction that captures the most variance in your data

  *The Problem:* We want to maximize variance, but prevent the solution from becoming infinite

  *The Solution in Simple Terms:*
  1. *What we want:* Direction with maximum variance
  2. *Constraint:* Direction must have unit length (prevents infinity)
  3. *Mathematical magic:* This leads to the eigenvalue problem
  4. *Key insight:* $bold(S) bold(v) = lambda bold(v)$
  5. *Result:* Largest eigenvalue = maximum variance

  *Why This Works:*
  - Eigenvalues tell us how much variance each direction captures
  - Eigenvectors tell us what those directions are
  - We pick the directions with the most variance

  *In Practice:*
  - Computer finds eigenvalues and eigenvectors
  - We sort them from largest to smallest
  - First few capture most of the interesting patterns
]

#slide(title: [Why Factor Analysis Works: Simple Logic])[
  *The Factor Model:* Each variable = Common factors + Unique part
  $ X_i = lambda_(i 1) F_1 + lambda_(i 2) F_2 + ... + U_i $

  *What this means:*
  - Common factors (F) affect multiple variables
  - Unique parts (U) affect only one variable
  - Loadings (λ) tell us how much each factor affects each variable

  *Key Insight:* If two variables share the same factors, they will be correlated!

  *Simple Example:*
  - Math and Science both depend on "Analytical Ability" → they correlate
  - But each also has unique aspects (Math has geometry, Science has memorization)

  *The Magic Formula:*
  $ bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi) $
  - $bold(Lambda) bold(Lambda)^top$: correlations due to shared factors
  - $bold(Psi)$: unique variance for each variable

  *Bottom Line:* Observable correlations come from shared hidden factors!
]

#slide(title: [Mathematical Formulation: Foundation])[
  Let $bold(x) in RR^p$ be a random vector with mean $bold(mu)$ and covariance matrix $bold(Sigma)$.

  *Data Matrix Representation:*
  - Data matrix $bold(X) in RR^(n times p)$ with $n$ observations and $p$ variables
  - Each row $bold(x)_i^top$ is an observation vector
  - Centered data: $bold(X)_c = bold(X) - bold(1)_n overline(bold(x))^top$ where $bold(1)_n$ is vector of ones

  *Sample Covariance Matrix:*
  $ bold(S) = frac(1, n-1) bold(X)_c^top bold(X)_c $

  *Pointwise Form:*
  $ s_(i j) = frac(1, n-1) sum_(l=1)^n (x_(l i) - overline(x)_i)(x_(l j) - overline(x)_j) $

  *Eigenvalue Problem:*
  Find eigenvalues $lambda_1 >= lambda_2 >= ... >= lambda_p >= 0$ and orthonormal eigenvectors $bold(v)_1, bold(v)_2, ..., bold(v)_p$ such that:
  $ bold(S) bold(v)_j = lambda_j bold(v)_j quad "for" j = 1, 2, ..., p $
]

#slide(title: [Mathematical Formulation: Spectral Decomposition])[
  *Spectral Decomposition of Covariance Matrix:*
  $ bold(S) = bold(V) bold(Lambda) bold(V)^top = sum_(j=1)^p lambda_j bold(v)_j bold(v)_j^top $

  *Pointwise Form:*
  $ s_(i j) = sum_(l=1)^p lambda_l v_(i l) v_(j l) $

  where:
  - $bold(V) = [bold(v)_1 | bold(v)_2 | ... | bold(v)_p] in RR^(p times p)$ (eigenvector matrix)
  - $bold(Lambda) = "diag"(lambda_1, lambda_2, ..., lambda_p)$ (diagonal eigenvalue matrix)
  - $bold(V)^top bold(V) = bold(V) bold(V)^top = bold(I)_p$ (orthonormality condition)

  *Principal Components:*
  The $j$-th principal component for observation $i$ is:
  $ z_(i j) = bold(v)_j^top (bold(x)_i - overline(bold(x))) = bold(v)_j^top bold(x)_(c i) $

  *Pointwise Form:*
  $ z_(i j) = sum_(l=1)^p v_(j l) (x_(i l) - overline(x)_l) $

  *Component Score Matrix:*
  $ bold(Z) = bold(X)_c bold(V) in RR^(n times p) $
]

#slide(title: [Mathematical Formulation: Variance Properties])[
  *Variance of Principal Components:*
  $ "Var"(Z_j) = "Var"(bold(v)_j^top bold(X)_c) = bold(v)_j^top bold(S) bold(v)_j = lambda_j $

  *Total Variance Decomposition:*
  $ "tr"(bold(S)) = sum_(j=1)^p s_(j j) = sum_(j=1)^p lambda_j $

  *Proportion of Variance Explained:*
  By component $j$: $rho_j = frac(lambda_j, sum_(k=1)^p lambda_k)$

  Cumulative: $rho_(1:k) = frac(sum_(j=1)^k lambda_j, sum_(j=1)^p lambda_j)$

  *Reconstruction Formula:*
  Using first $k$ components: $hat(bold(x)) = overline(bold(x)) + sum_(j=1)^k z_j bold(v)_j$

  *Pointwise Form:*
  $hat(x)_i = overline(x)_i + sum_(j=1)^k z_j v_(j i)$

  *Mean Squared Reconstruction Error:*
  $"MSE" = frac(1, n) ||bold(X)_c - bold(Z)_(1:k) bold(V)_(1:k)^top||_F^2 = sum_(j=k+1)^p lambda_j$
]

#slide(title: [From Concept to Computation: PCA Algorithm])[
  *Ready to turn theory into practice?*

  The PCA algorithm is like a recipe for finding the best viewpoints of your data. Think of it as teaching a computer to be that photographer we mentioned earlier!

  *What the algorithm does step-by-step:*
  1. *Preparation*: Clean and standardize the data (like focusing the camera)
  2. *Find relationships*: Calculate how variables relate to each other
  3. *Discover directions*: Find the best angles (principal components)
  4. *Transform data*: Project data onto these new viewpoints
  5. *Decide*: How many viewpoints do we actually need?

  *Why follow this exact sequence?*
  - Each step builds on the previous one
  - Mathematical guarantees that we find the *optimal* solution
  - Practical choices (like standardization) can dramatically affect results

  Let's see the detailed mathematical recipe:
]

#slide(title: [Algorithm: Principal Component Analysis])[
  *Input:* Data matrix $bold(X) in RR^(n times p)$ (n observations, p variables), standardization choice
  *Output:* Principal components $bold(V)$, eigenvalues $bold(Lambda)$, component scores $bold(Z)$

  1. *Prepare Your Data*
     - *Different units?* (age vs income) → Standardize all variables
     - *Same units?* (all test scores) → Just center the data
     - *Rule of thumb:* When in doubt, standardize

  2. *Calculate Relationships Between Variables*
     - Compute correlation matrix: How do variables relate?
     - This captures all the patterns in your data

  3. *Find the Best Directions* (Eigenvalues & Eigenvectors)
     - Computer finds the directions with most variance
     - Eigenvalues = how much variance each direction captures
     - Eigenvectors = what those directions are

  4. *Transform Your Data*
     - Project data onto the new directions
     - Get principal component scores for each observation

  5. *Decide How Many Components to Keep*
     - Use Kaiser rule: keep eigenvalues > 1
     - Or pick enough to explain 70-80% of variance
     - Fewer components = simpler interpretation
]

#slide(title: [PCA Algorithm: Simple Numerical Example])[
  *Given Data:* 3 observations, 2 variables
  $ bold(X) = mat(5, 3; 3, 1; 1, 3) quad "and" quad overline(bold(x)) = mat(3; 2.33) $

  *Step 1: Center the data*
  $ bold(X)_c = bold(X) - bold(1)_3 overline(bold(x))^top = mat(5, 3; 3, 1; 1, 3) - mat(3, 2.33; 3, 2.33; 3, 2.33) = mat(2, 0.67; 0, -1.33; -2, 0.67) $

  *Step 2: Compute sample covariance matrix*
  $ bold(S) = frac(1, 2) bold(X)_c^top bold(X)_c = frac(1, 2) mat(2, 0, -2; 0.67, -1.33, 0.67) mat(2, 0.67; 0, -1.33; -2, 0.67) = mat(4, -0.67; -0.67, 1.33) $

  *Step 3: Solve eigenvalue problem* $bold(S) bold(v) = lambda bold(v)$
  - Characteristic equation: $det(bold(S) - lambda bold(I)) = (4-lambda)(1.33-lambda) - 0.67^2 = 0$
  - Eigenvalues: $lambda_1 = 4.45$, $lambda_2 = 0.88$
  - Eigenvectors: $bold(v)_1 = mat(0.95; -0.32)$, $bold(v)_2 = mat(0.32; 0.95)$

  *Step 4: Compute PC scores*
  $ bold(Z) = bold(X)_c bold(V) = mat(2, 0.67; 0, -1.33; -2, 0.67) mat(0.95, 0.32; -0.32, 0.95) = mat(1.69, 1.28; 0.43, -1.26; -2.12, 0.00) $

  *Interpretation:* PC1 explains $frac(4.45, 5.33) = 83.5%$ of total variance
]

#slide(title: [Python Implementation: PCA Example])[
  ```python
  import numpy as np
  from sklearn.decomposition import PCA
  import pandas as pd

  # Step 1: Create the data
  X = np.array([[5, 3],
                [3, 1],
                [1, 3]])

  # Step 2: Apply PCA
  pca = PCA()
  X_transformed = pca.fit_transform(X)

  # Step 3: Get results
  eigenvalues = pca.explained_variance_
  eigenvectors = pca.components_.T
  variance_ratio = pca.explained_variance_ratio_

  print(f"Eigenvalues: {eigenvalues}")
  print(f"PC1 explains {variance_ratio[0]:.1%} of variance")
  print(f"Transformed data:\n{X_transformed}")
  ```

  *Output matches our manual calculation!*
]

#slide(title: [Deciding how many components to retain])[
  Common heuristics and formal approaches:
  - Kaiser criterion: keep components with eigenvalue $> 1$ (applies when using correlation matrix).
  - Cumulative variance: keep the smallest number of components that explain a target (e.g., 70--90%) of total variance.
  - Scree plot: look for the "elbow" where additional components contribute little incremental variance.
  - Parallel analysis: compare empirical eigenvalues to those obtained from random data — keep components with larger eigenvalues than random.
    - *How it works*: Generate random datasets with same dimensions (n observations × p variables) as your data
    - *Compare*: For each component k, if $lambda_k "(actual)" > lambda_k "(random)"$, retain component k
    - *Advantage*: Accounts for sampling error and prevents over-extraction
    - *Conservative approach*: Often retains fewer components than Kaiser criterion
]

#slide(title: [Algorithm: Component/Factor Retention Decision])[
  *Input:* Eigenvalues $lambda_1 >= lambda_2 >= ... >= lambda_p$, variance threshold $alpha$

  *Output:* Optimal number of components/factors $k^*$

  1. *Kaiser Criterion* (Rule of Thumb)
     - Keep components with eigenvalue > 1
     - *Why?* Each component should explain more variance than a single variable
     - *Easy rule:* Count how many eigenvalues are bigger than 1

  2. *Cumulative Variance* (Practical Goal)
     - Keep enough components to explain 70-80% of total variance
     - *Example:* If first 3 components explain 75%, keep 3
     - *Trade-off:* More components = more complexity

  3. *Scree Plot* (Visual Method)
     - Plot eigenvalues from largest to smallest
     - Look for the "elbow" - where the line flattens out
     - Keep components before the elbow

  4. *Parallel Analysis* (Statistical Test)
     - Compare your eigenvalues to random data
     - Keep components larger than random ones
     - *Software does this automatically*

  5. *Final Decision*
     - Use multiple methods and find agreement
     - When in doubt, choose fewer components (simpler is better)
     - *Recommendation:* Use parallel analysis as primary criterion
]

#slide(title: [Component Retention: Simple Numerical Example])[
  *Given Eigenvalues:* From 5-variable correlation matrix
  $ lambda = [2.8, 1.2, 0.7, 0.2, 0.1] $

  *Step 1: Kaiser Criterion*
  $ k_"Kaiser" = |{j : lambda_j > 1}| = |{1, 2}| = 2 $ components

  *Step 2: Cumulative Variance (80% threshold)*
  - Total variance: $sum lambda_j = 5.0$
  - Cumulative proportions: $[0.56, 0.80, 0.94, 0.98, 1.00]$
  - $k_"variance" = min{j : rho_j >= 0.80} = 2$ components

  *Step 3: Parallel Analysis (simplified)*
  - Random eigenvalues (average): $overline(lambda)^"random" = [1.4, 1.1, 0.9, 0.7, 0.5]$
  - Compare: $lambda_j > overline(lambda)_j^"random"$
    - Factor 1: $2.8 > 1.4$ ✓
    - Factor 2: $1.2 > 1.1$ ✓
    - Factor 3: $0.7 < 0.9$ ✗
  - $k_"parallel" = 2$ components

  *Step 4: Consensus Decision*
  $ k^* = "consensus"(2, 2, 2) = 2 $ components

  *Result:* All criteria agree → retain 2 components explaining 80% of variance
]

#slide(title: [Python Implementation: Component Retention])[
  ```python
  import numpy as np
  from sklearn.decomposition import PCA
  import matplotlib.pyplot as plt

  # Simulated data with 5 variables
  np.random.seed(42)
  X = np.random.randn(100, 5)

  # Apply PCA
  pca = PCA()
  pca.fit(X)

  eigenvalues = pca.explained_variance_
  cumvar = pca.explained_variance_ratio_.cumsum()

  # Kaiser criterion
  n_kaiser = sum(eigenvalues > 1)

  # Cumulative variance (80% threshold)
  n_cumvar = np.argmax(cumvar >= 0.8) + 1

  print(f"Kaiser criterion: {n_kaiser} components")
  print(f"80% variance: {n_cumvar} components")
  print(f"Cumulative variance: {cumvar}")

  # Scree plot
  plt.plot(range(1, 6), eigenvalues, 'bo-')
  plt.axhline(y=1, color='r', linestyle='--')
  plt.title('Scree Plot')
  plt.show()
  ```
]

#slide(title: [Algorithm: PCA Data Analysis Checklist])[
  *Input:* Raw data matrix, research objectives

  *Output:* Validated PCA results and interpretation

  1. *Data Quality Assessment*
     - Check for missing values; handle via imputation or deletion
     - Detect outliers using Mahalanobis distance or visualization
     - *if* outliers are excessive *then* consider robust PCA methods

  2. *Variable Scaling Decision*
     - Examine variable scales and units
     - *if* variables have different scales *then*
       - Standardize: Use correlation matrix for PCA
     - *else*
       - Use covariance matrix for PCA

  3. *Component Interpretation*
     - Examine loading matrix $bold(V)$
     - *for* each component $j$ *do*
       - Identify variables with $|v_(i j)| > 0.3$ (substantial loading)
       - Name component based on dominant variables

  4. *Results Validation and Reporting*
     - Generate eigenvalue table with variance proportions
     - Create scree plot for visual component selection
     - Report cumulative variance explained
     - Include rotated component matrix if rotation applied
]

#section-slide[Factor Analysis Theory]

#slide(title: [Understanding Factor Analysis: The Detective Story])[
  *Imagine you're a detective investigating what makes students perform well in school.*

  You observe their grades in Math, Science, Literature, and History. But you suspect there are *hidden influences* behind these grades - things like "intelligence," "motivation," and "study habits" that you can't directly measure.

  *What Factor Analysis does:*
  - Looks for these *hidden factors* that explain why variables move together
  - Separates what's *common* (shared patterns) from what's *unique* (individual noise)
  - Tells you how much each hidden factor influences each observed variable

  *The key insight:*
  If Math and Science grades are highly correlated, there might be a hidden "quantitative ability" factor. If all subjects correlate, there might be a "general intelligence" factor.

  *Why this matters:*
  - Helps understand the *underlying structure* of phenomena
  - Validates *theoretical models* (like intelligence theory)
  - Separates *signal from noise* in measurements
]

#slide(title: [What is Factor Analysis?])[
  - A statistical method for modeling relationships among *observed variables* using *latent factors*.
  - It uses a smaller number of _unobserved variables_, known as *common factors*.
  - *Key Distinction from PCA*: Explicitly models measurement error and unique variance
  - Often used to discover and validate underlying theoretical constructs
]

// Split the long FA content into smaller, focused slides

#slide(title: [Factor Analysis Model: Mathematical Foundation])[
  *The General Factor Model for Variable i:*
  $ X_i = mu_i + sum_(j=1)^k lambda_(i j) F_j + U_i quad "for" i = 1, 2, ..., p $

  *Centered Factor Model (Standard Practice):*
  $ X_i - mu_i = sum_(j=1)^k lambda_(i j) F_j + U_i quad "for" i = 1, 2, ..., p $

  where:
  - $X_i$: Observed variable $i$
  - $mu_i$: Mean of variable $i$ (estimated from data: $mu_i = overline(x)_i = frac(1, n) sum_(l=1)^n X_(i l)$)
  - $F_j$: Common factor $j$ with $F_j tilde N(0,1)$, independent
  - $lambda_(i j)$: Factor loading of variable $i$ on factor $j$
  - $U_i$: Unique factor for variable $i$ with $U_i tilde N(0, psi_i^2)$
  - $k < p$: Number of common factors

  *Profound Significance of This Model:*
  - *Theoretical Foundation*: This equation captures the belief that observed phenomena are driven by *underlying latent causes*
  - *Parsimony Principle*: A few common factors ($k << p$) can explain most relationships among many variables
  - *Measurement Theory*: Separates systematic variance (common factors) from random measurement error (unique factors)
  - *Scientific Discovery*: Enables identification of unobservable constructs (like intelligence, personality dimensions)
  - *Practical Relevance*: Reduces complex multivariate data to interpretable, meaningful dimensions for decision-making

  *Matrix Form (for centered data):*
  $ bold(X)_c = bold(Lambda) bold(F) + bold(U) $

  where:
  - $bold(X)_c = bold(X) - bold(1)_n overline(bold(x))^top in RR^(n times p)$ (centered data matrix)
  - $overline(bold(x)) = (overline(x)_1, overline(x)_2, dots, overline(x)_p)^top$ (sample mean vector)
  - $bold(Lambda) in RR^(p times k)$ (factor loadings matrix)
  - $bold(F) in RR^(n times k)$ (factor scores matrix)
  - $bold(U) in RR^(n times p)$ (unique factors matrix)

  *Why we center:* Factor Analysis models the covariance structure, not the means
]

#slide(title: [Variance Decomposition: Communality and Uniqueness])[
  *Variance of Observed Variable i (Scalar Form):*
  $ "Var"(X_i) = "Var"(sum_(j=1)^k lambda_(i j) F_j) + "Var"(U_i) $

  Since $F_j$ are independent with unit variance and $U_i$ is independent of all $F_j$:
  $ "Var"(X_i) = sum_(j=1)^k lambda_(i j)^2 + psi_i^2 = h_i^2 + psi_i^2 $

  *Matrix Form (Variance Structure):*
  $ "Var"(bold(X)) = bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi) $
  where each diagonal element: $sigma_(i i) = sum_(j=1)^k lambda_(i j)^2 + psi_i^2$

  *Fundamental Insight Behind Variance Decomposition:*
  - *Total Variance* = *Systematic Variance* + *Random Variance*
  - This decomposition is the *mathematical foundation of measurement theory*
  - *Systematic variance* ($h_i^2$) represents what the variable shares with underlying constructs
  - *Random variance* ($psi_i^2$) captures measurement error and variable-specific effects
  - *Critical for Quality Assessment*: High communality indicates reliable measurement; high uniqueness suggests measurement problems or variable-specific factors
  - *Model Evaluation*: If most variance is unique, the factor model may be inappropriate for the data

  *Communality (Scalar and Matrix Forms):*
  - *Scalar:* $h_i^2 = sum_(j=1)^k lambda_(i j)^2$ (variance explained by common factors)
  - *Matrix:* $bold(h)^2 = "diag"(bold(Lambda) bold(Lambda)^top)$ (communality vector)

  *Deeper Meaning of Communality:*
  - *Reliability Indicator*: High $h_i^2$ (close to 1) means variable is well-explained by common factors
  - *Construct Validity*: Variables measuring the same construct should have similar communalities
  - *Practical Threshold*: $h_i^2 > 0.5$ suggests variable belongs in the factor structure; $h_i^2 < 0.3$ may indicate poor fit

  *Uniqueness (Scalar and Matrix Forms):*
  - *Scalar:* $psi_i^2 = "Var"(U_i)$ (unique variance: specific + measurement error)
  - *Matrix:* $bold(Psi) = "diag"(psi_1^2, psi_2^2, dots, psi_p^2)$ (uniqueness matrix)

  *Deeper Meaning of Uniqueness:*
  - *Measurement Quality*: High $psi_i^2$ may indicate measurement problems or variable doesn't fit the factor structure
  - *Specificity vs. Error*: Includes both legitimate specific variance and random measurement error
  - *Model Diagnostics*: Variables with $psi_i^2 > 0.7$ should be examined for potential removal or model revision

  *Total Variance Decomposition:*
  For standardized variables: $"Var"(X_i) = 1 = h_i^2 + psi_i^2$

  *Critical Insight*: This decomposition enables *quantitative assessment of measurement quality* and guides decisions about variable retention and model adequacy.
]

#slide(title: [Algorithm: Communality and Uniqueness Calculation])[
  *Input:* Factor loading matrix $bold(Lambda) in RR^(p times k)$

  *Output:* Communalities $bold(h)^2$, uniquenesses $bold(psi)^2$

  1. *Initialize Arrays*
     - $bold(h)^2 = $ zero vector of length $p$
     - $bold(psi)^2 = $ zero vector of length $p$

  2. *Compute Communalities*
     - *for* $i = 1$ to $p$ *do*
       - $h_i^2 = sum_(j=1)^k lambda_(i j)^2$ (sum of squared loadings for variable $i$)

  3. *Compute Uniquenesses*
     - *for* $i = 1$ to $p$ *do*
       - $psi_i^2 = 1 - h_i^2$ (for standardized variables)
       - *if* $psi_i^2 < 0$ *then* $psi_i^2 = 0.005$ (Heywood case correction)

  4. *Validation Check*
     - *for* $i = 1$ to $p$ *do*
       - *assert* $h_i^2 + psi_i^2 = 1$ (variance decomposition property)
       - *assert* $0 <= h_i^2 <= 1$ and $0 <= psi_i^2 <= 1$ (valid proportions)
]

#slide(title: [Factor Extraction Methods: Mathematical Approaches])[
  *1. Principal Axis Factoring (PAF):*
  - Initialize communality estimates: $h_i^2 = R_(i i) - 1/R^(-1)_(i i)$ (squared multiple correlation)
  - Form reduced correlation matrix: $bold(R)^* = bold(R) - "diag"(psi_1^2, ..., psi_p^2)$
  - Eigendecomposition: $bold(R)^* = bold(V) bold(Lambda) bold(V)^top$
  - Factor loadings: $bold(Lambda) = bold(V)_k sqrt(bold(Lambda)_k)$ (first $k$ factors)
  - Iterate until convergence: Update $h_i^2 = sum_(j=1)^k lambda_(i j)^2$

  *2. Maximum Likelihood (ML) Factoring:*
  - Assumes multivariate normality: $bold(X) tilde N(bold(0), bold(Sigma))$
  - Covariance structure: $bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi)$
  - Minimize: $F_"ML" = "tr"(bold(S) bold(Sigma)^(-1)) - ln|bold(Sigma)^(-1)| - p$
  - Provides $chi^2$ goodness-of-fit test and confidence intervals
]

#slide(title: [Algorithm: Factor Analysis with Principal Axis Factoring])[
  *Input:* Data matrix $bold(X) in RR^(n times p)$ (n observations, p variables), number of factors $k$
  *Output:* Factor loadings $bold(Lambda)$, uniquenesses $bold(Psi)$, factor scores $hat(bold(F))$

  1. *Data Preprocessing and Suitability Assessment*
     - *Standardize variables:* $bold(Z) = (bold(X) - bold(1)_n overline(bold(x))^top) bold(D)^(-1/2)$
       where $bold(D) = "diag"(s_1^2, dots, s_p^2)$ (variable variances)
     - *Compute correlation matrix:* $bold(R) = frac(1, n-1) bold(Z)^top bold(Z)$
     - *Test data suitability for factoring:*
       - Bartlett's sphericity test: $H_0$: $bold(R) = bold(I)$ (variables uncorrelated)
       - Kaiser-Meyer-Olkin (KMO) measure: assess sampling adequacy

  2. *Initialize Communality Estimates*
     - *Purpose:* Estimate how much variance each variable shares with factors
     - *for* each variable $i = 1$ to $p$:
       - *Compute initial estimate:* $h_i^2 = 1 - frac(1, (bold(R)^(-1))_(i i))$
         (squared multiple correlation with other variables)
       - *Alternative:* Use maximum absolute correlation: $h_i^2 = max_j |r_(i j)|$ for $j != i$
       - *Interpretation:* Proportion of variable i's variance explained by common factors

  3. *Principal Axis Factoring Iteration*
     - *Iterative refinement:* Improve communality estimates until convergence
     - *repeat*:
       - *Form reduced correlation matrix:* $bold(R)^* = bold(R) - "diag"(1-h_1^2, dots, 1-h_p^2)$
         (Replace diagonal with communalities instead of 1's)
       - *Eigenvalue decomposition:* $bold(R)^* = bold(V) bold(Lambda) bold(V)^top$
       - *Extract k factors:* $bold(L) = bold(V)_k bold(Lambda)_k^(1/2)$ (first k columns and eigenvalues)
       - *Update communalities:* $h_i^2 = sum_(j=1)^k l_(i j)^2$ for each $i = 1, dots, p$
         (Sum of squared loadings for variable i)
     - *until* $max_i |h_i^2_"new" - h_i^2_"old"| < epsilon$ (convergence achieved)

  4. *Factor Rotation* (Optional but Recommended)
     - *Purpose:* Achieve simpler, more interpretable factor structure
     - *Apply rotation method:*
       - Varimax (orthogonal): maintains factor independence, $bold(Lambda)^* = bold(L) bold(T)$
       - Promax (oblique): allows correlated factors for more flexibility
     - *Result:* Rotated loadings $bold(Lambda)^*$ with cleaner interpretation

  5. *Factor Score Estimation*
     - *Estimate individual factor scores for each observation*
     - *Regression method:* $hat(bold(F)) = bold(Z) bold(Lambda) (bold(Lambda)^top bold(Lambda))^(-1)$
       (Simple, but scores may be correlated even with orthogonal factors)
     - *Bartlett method:* $hat(bold(F)) = bold(Z) bold(Lambda) (bold(Lambda)^top bold(Psi)^(-1) bold(Lambda))^(-1) bold(Lambda)^top bold(Psi)^(-1)$
       (More complex, but preserves factor orthogonality if assumed)
]

#slide(title: [Factor Analysis: Simple Numerical Example])[
  *Given Data:* 3 variables, 1 factor model
  $ bold(R) = mat(1.00, 0.60, 0.48; 0.60, 1.00, 0.72; 0.48, 0.72, 1.00) $

  *Step 1: Initial communality estimates (SMC)*
  - Compute $bold(R)^(-1)$ and extract diagonal elements
  - $h_1^2 = 1 - frac(1, (bold(R)^(-1))_(11)) = 1 - frac(1, 2.78) = 0.64$
  - $h_2^2 = 1 - frac(1, (bold(R)^(-1))_(22)) = 1 - frac(1, 3.57) = 0.72$
  - $h_3^2 = 1 - frac(1, (bold(R)^(-1))_(33)) = 1 - frac(1, 2.17) = 0.54$

  *Step 2: Form reduced correlation matrix*
  $ bold(R)^* = mat(0.64, 0.60, 0.48; 0.60, 0.72, 0.72; 0.48, 0.72, 0.54) $

  *Step 3: Eigenvalue decomposition*
  - Largest eigenvalue: $lambda_1 = 1.84$
  - Corresponding eigenvector: $bold(v)_1 = mat(0.53; 0.67; 0.52)$

  *Step 4: Factor loadings*
  $ bold(L) = bold(v)_1 sqrt(lambda_1) = mat(0.53; 0.67; 0.52) times 1.36 = mat(0.72; 0.91; 0.71) $

  *Pointwise Form:*
  $ lambda_(i 1) = v_(i 1) sqrt(lambda_1) quad "for" i = 1, 2, 3 $

  *Step 5: Updated communalities*
  $ h_1^2 = 0.72^2 = 0.52, quad h_2^2 = 0.91^2 = 0.83, quad h_3^2 = 0.71^2 = 0.50 $

  *Final Model:* $bold(Sigma) = bold(L) bold(L)^top + bold(Psi)$
  $ = mat(0.72; 0.91; 0.71) mat(0.72, 0.91, 0.71) + mat(0.48, 0, 0; 0, 0.17, 0; 0, 0, 0.50) $

  *Pointwise Form:*
  $ sigma_(i j) = lambda_(i 1) lambda_(j 1) + psi_i^2 delta_(i j) $
]

#slide(title: [Python Implementation: Factor Analysis Example])[
  ```python
  import numpy as np
  from factor_analyzer import FactorAnalyzer
  from sklearn.datasets import make_spd_matrix

  # Create correlation matrix (our example)
  R = np.array([[1.00, 0.60, 0.48],
                [0.60, 1.00, 0.72],
                [0.48, 0.72, 1.00]])

  # For real data, you'd start with raw data:
  # X = your_data  # shape (n_samples, n_features)
  # R = np.corrcoef(X.T)  # correlation matrix

  # Perform Factor Analysis
  fa = FactorAnalyzer(n_factors=1, rotation=None)
  fa.fit(R)  # For correlation matrix
  # fa.fit(X)  # For raw data

  # Get results
  loadings = fa.loadings_
  communalities = fa.get_communalities()
  uniqueness = fa.get_uniquenesses()

  print(f"Factor loadings:\n{loadings}")
  print(f"Communalities: {communalities}")
  print(f"Uniqueness: {uniqueness}")
  ```

  *Note: Install with: pip install factor_analyzer*
]

#slide(title: [From Detective Work to Algorithm: Factor Analysis])[
  *Now let's turn our detective story into a systematic investigation!*

  Remember, Factor Analysis is like being a detective looking for hidden influences. The algorithm is our systematic method for uncovering these hidden factors.

  *What makes FA algorithm different from PCA?*
  - *Iterative process*: Like refining a theory through multiple rounds of evidence
  - *Two unknowns*: We don't know the factors OR how they influence variables
  - *Modeling errors*: Accounts for measurement noise (like witness reliability)
  - *Maximum Likelihood*: Finds the most probable explanation for what we observe

  *The detective's toolkit:*
  1. *Start with a guess* (initial hypothesis)
  2. *Estimate hidden factors* (what would the suspects be doing?)
  3. *Update our theory* (revise how factors influence variables)
  4. *Repeat until story makes sense* (convergence)
  5. *Test the theory* (does it explain the data well?)

  This is more complex than PCA, but gives us *richer insights* about underlying structure!
]

#slide(title: [Algorithm: Maximum Likelihood Factor Analysis])[
  *Input:* Data matrix $bold(X) in RR^(n times p)$, number of factors $k$, tolerance $epsilon$

  *Output:* ML factor loadings $bold(Lambda)$, uniquenesses $bold(Psi)$, model fit statistics

  1. *Start with Initial Guess*
     - Make first estimate of factor loadings
     - Use simple method (like PCA) as starting point

  2. *Iterative Improvement* (EM Algorithm)
     - Step E: Estimate what the hidden factors would be
     - Step M: Update loadings based on those estimates
     - Repeat until no more improvement
     - *Why this works:* Each step makes the model fit better

  3. *Check How Well It Fits*
     - Does our model explain the correlations well?
     - Statistical tests tell us if the fit is good enough
     - *Good fit:* Model explains most observed relationships

  4. *Get Final Results*
     - Factor loadings (how factors affect variables)
     - Confidence intervals (how certain are we?)
     - *Software does the complex calculations automatically*
]

#slide(title: [Making Sense of the Results: Factor Rotation])[
  *You've found the hidden factors, but they're still confusing! Now what?*

  Imagine you've identified two hidden factors in student performance, but:
  - Factor 1 loads on Math (0.6), Science (0.7), Literature (0.5), History (0.4)
  - Factor 2 loads on Math (0.4), Science (0.3), Literature (0.6), History (0.7)

  *This is messy!* What do these factors actually represent?

  *Factor Rotation is like adjusting the camera angle* after taking the photo:
  - We want *simple structure*: each factor should clearly represent something
  - Goal: High loadings for relevant variables, low for irrelevant ones
  - Like rotating a map so north points up - same information, clearer presentation

  *Two types of rotation:*
  - *Orthogonal* (factors stay independent): Clean, simple interpretation
  - *Oblique* (factors can correlate): More realistic, factors can be related

  This is where art meets science in factor analysis!
]

#slide(title: [Factor Rotation: Mathematical Transformation])[
  *Purpose:* Transform initial factor loadings $bold(Lambda)$ to rotated loadings $bold(Lambda)^* = bold(Lambda) bold(T)$ where $bold(T)$ is transformation matrix.

  *Profound Significance of Factor Loadings ($lambda_(i j)$):*
  - *Conceptual Meaning*: Each loading represents the *strength of relationship* between observed variable $i$ and latent factor $j$
  - *Statistical Interpretation*: Correlation between variable and factor (in standardized form)
  - *Practical Meaning*: How much a 1-unit change in the factor affects the observed variable
  - *Measurement Perspective*: Quality indicator - high loadings suggest variable is a good indicator of the construct

  *Orthogonal Rotation (Varimax):*
  - Constraint: $bold(T)^top bold(T) = bold(I)$ (orthogonal transformation)
  - Objective: Maximize variance of squared loadings within each factor
  - Varimax criterion: $V = frac(1, p) sum_(j=1)^k [sum_(i=1)^p (lambda_(i j)^*)^4 - frac(1, p)(sum_(i=1)^p (lambda_(i j)^*)^2)^2]$
  - Seeks "simple structure": high loadings for few variables, low for others

  *Why Rotation Matters*: Initial loadings may be mathematically optimal but practically uninterpretable. Rotation preserves statistical properties while achieving *psychological/theoretical interpretability*.

  *Oblique Rotation (Promax):*
  - Allows factor correlations: $bold(Phi) = "Corr"(bold(F))$ may be non-diagonal
  - Pattern matrix $bold(P)$: direct effects (regression coefficients)
  - Structure matrix $bold(S) = bold(P) bold(Phi)$: correlations with factors
  - Relationship: $bold(Sigma) = bold(P) bold(Phi) bold(P)^top + bold(Psi)^2$
]

#slide(title: [Algorithm: Varimax Rotation for Simple Structure])[
  *Input:* Initial factor loadings $bold(Lambda) in RR^(p times k)$, convergence tolerance $epsilon$

  *Output:* Rotated loadings $bold(Lambda)^*$, rotation matrix $bold(T)$

  1. *Initialize Rotation Matrix*
     - $bold(T) = bold(I)_k$ (identity matrix)
     - $bold(Lambda)^* = bold(Lambda)$ (initial loadings)

  2. *Rotate for Simple Structure*
     - *Goal:* Make each factor load highly on few variables
     - Algorithm finds the best rotation angle automatically
     - *Process:*
       - Compare pairs of factors
       - Rotate them to maximize simple structure
       - Repeat until no more improvement

  3. *Check the Results*
     - Verify factors are still independent (orthogonal)
     - Loadings should be clearer: high or low, not medium
]

#slide(title: [Varimax Rotation: Simple Numerical Example])[
  *Given Factor Loadings:* 3 variables, 2 factors (before rotation)
  $ bold(Lambda) = mat(0.71, 0.45; 0.89, 0.32; 0.67, -0.58) $

  *Before Rotation:* Mixed loadings (hard to interpret)
  - Variable 1: loads on both factors (0.71, 0.45)
  - Variable 2: loads on both factors (0.89, 0.32)
  - Variable 3: loads on both factors (0.67, -0.58)

  *After Rotation:* Clearer structure
  $ bold(Lambda)^* = mat(0.78, 0.33; 0.93, 0.16; 0.56, -0.67) $
  - Variable 1: mainly Factor 1 (0.78 vs 0.33)
  - Variable 2: mainly Factor 1 (0.93 vs 0.16)
  - Variable 3: mainly Factor 2 (0.56 vs -0.67)

  *Interpretation:*
  - Factor 1: Variables 1 & 2 (maybe "Verbal ability")
  - Factor 2: Variable 3 (maybe "Spatial ability")

  *Software handles the complex rotation calculations automatically!*
]

#slide(title: [Python Implementation: Factor Rotation])[
  ```python
  import numpy as np
  from factor_analyzer import FactorAnalyzer

  # Simulate data that would produce our example loadings
  np.random.seed(42)
  X = np.random.randn(100, 3)

  # Apply Factor Analysis with rotation
  fa_no_rotation = FactorAnalyzer(n_factors=2, rotation=None)
  fa_varimax = FactorAnalyzer(n_factors=2, rotation='varimax')

  fa_no_rotation.fit(X)
  fa_varimax.fit(X)

  # Compare loadings before and after rotation
  loadings_before = fa_no_rotation.loadings_
  loadings_after = fa_varimax.loadings_

  print("Before rotation:")
  print(loadings_before)
  print("\nAfter Varimax rotation:")
  print(loadings_after)

  # Other rotation options: 'promax', 'oblimin', 'quartimax'
  fa_promax = FactorAnalyzer(n_factors=2, rotation='promax')
  fa_promax.fit(X)
  print("\nAfter Promax rotation:")
  print(fa_promax.loadings_)
  ```
]

#slide(title: [Quick Decision Guide: PCA vs Factor Analysis])[
  *Use PCA when:*
  - You want to reduce dimensions for visualization
  - You want to compress data (remove redundancy)
  - You don't have specific theory about hidden factors
  - You want the mathematically optimal solution

  *Use Factor Analysis when:*
  - You want to test a theory (like "intelligence" causes test performance)
  - You want to understand underlying causes
  - You want to separate "signal" from "noise"
  - You care more about interpretation than data compression

  *Quick Rules:*
  - Psychology/Education → Usually Factor Analysis
  - Data compression/Machine learning → Usually PCA
  - Exploratory analysis → Try both and compare!
]

#slide(title: [Practical Checklist for Your Analysis])[
  *Before You Start:*
  1. Do variables measure similar things? (similar units?)
  2. Do you have enough data? (at least 100 observations)
  3. Are variables correlated? (if not, both methods will fail)

  *Choosing the Method:*
  4. Do you have a theory about hidden factors? → Factor Analysis
  5. Just want to reduce dimensions? → PCA
  6. Want to understand causes? → Factor Analysis

  *Interpreting Results:*
  7. PCA: How much variance explained by first few components?
  8. FA: Do factor loadings make sense theoretically?
  9. Rotation: Does it make interpretation clearer?

  *Red Flags:*
  - Eigenvalues all very similar → No clear structure
  - Factors don't make theoretical sense → Reconsider approach
  - Too many factors needed → Maybe not suitable for these methods
]

#slide(title: [Complete Python Workflow Example])[
  ```python
  import numpy as np
  import pandas as pd
  from sklearn.decomposition import PCA
  from sklearn.preprocessing import StandardScaler
  from factor_analyzer import FactorAnalyzer
  from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
  import matplotlib.pyplot as plt

  # 1. Load and prepare data
  # X = pd.read_csv('your_data.csv')  # Your actual data
  X = np.random.randn(100, 5)  # Simulated data for demo

  # 2. Standardize if needed
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)

  # 3. Check suitability for factor analysis
  kmo_all, kmo_model = calculate_kmo(X_scaled)
  chi_square_value, p_value = calculate_bartlett_sphericity(X_scaled)

  print(f"KMO: {kmo_model:.3f} (>0.6 is good)")
  print(f"Bartlett's test p-value: {p_value:.3f} (<0.05 is good)")

  # 4. Determine number of factors
  pca = PCA()
  pca.fit(X_scaled)
  eigenvalues = pca.explained_variance_
  n_factors = sum(eigenvalues > 1)  # Kaiser criterion

  print(f"Suggested factors: {n_factors}")

  # 5. Perform Factor Analysis with rotation
  fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax')
  fa.fit(X_scaled)

  # 6. Get and interpret results
  loadings = fa.loadings_
  communalities = fa.get_communalities()
  variance_explained = fa.get_factor_variance()

  print(f"Factor loadings:\n{loadings}")
  print(f"Communalities: {communalities}")
  print(f"Variance explained: {variance_explained[1]}")  # Proportional variance

  # 7. Compare with PCA
  pca_result = pca.transform(X_scaled)
  fa_scores = fa.transform(X_scaled)

  print("\nPCA vs FA comparison completed!")
  ```

  *This workflow covers the complete analysis pipeline!*
]

#slide(title: [Covariance Structure and Model Identification])[
  *Implied Covariance Matrix:*
  $bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi)$

  where $bold(Psi) = "diag"(psi_1^2, psi_2^2, ..., psi_p^2)$ is the uniqueness matrix.

  *Pointwise Form:*
  $sigma_(i j) = sum_(l=1)^k lambda_(i l) lambda_(j l) + psi_i^2 delta_(i j)$
  where $delta_(i j) = 1$ if $i = j$, $0$ otherwise.

  *Model Parameters:*
  - Factor loadings: $k times p$ parameters in $bold(Lambda)$
  - Unique variances: $p$ parameters in $bold(Psi)$
  - Total: $k p + p$ parameters to estimate

  *Identification Constraints:*
  - Sample covariance matrix has $p(p+1)/2$ unique elements
  - For identification: $k p + p <= p(p+1)/2$
  - Simplifies to: $k <= frac(p(p-1)/2 - p, p) = frac(p-1, 2) - 1$
  - Additional constraint: Fix factor scale (unit variance) or loading scale

  *Degrees of Freedom:* $"df" = p(p+1)/2 - (k p + p - k)$
]

#slide(title: [Algorithm: Factor Analysis Suitability Tests])[
  *Input:* Correlation matrix $bold(R) in RR^(p times p)$, significance level $alpha$

  *Output:* KMO measure, Bartlett test statistic, suitability decision

  1. *Kaiser-Meyer-Olkin (KMO) Test*
     - Compute anti-image correlation matrix: $bold(A) = -"diag"(bold(R)^(-1))^(-1) bold(R)^(-1) "diag"(bold(R)^(-1))^(-1)$
     - *for* $i,j = 1$ to $p$ *do*
       - $a_(i j) = A_(i j) / sqrt(A_(i i) A_(j j))$ (off-diagonal anti-image correlations)
     - Compute KMO: $"KMO" = frac(sum_(i != j) R_(i j)^2, sum_(i != j) R_(i j)^2 + sum_(i != j) a_(i j)^2)$

  2. *Interpret KMO Value*
     - *if* KMO $>= 0.9$ *then* "marvelous"
     - *else if* KMO $>= 0.8$ *then* "meritorious"
     - *else if* KMO $>= 0.7$ *then* "middling"
     - *else if* KMO $>= 0.6$ *then* "mediocre"
     - *else if* KMO $>= 0.5$ *then* "miserable"
     - *else* "unacceptable for FA"

  3. *Bartlett's Test of Sphericity*
     - $chi^2 = -(n - 1 - frac(2p + 5, 6)) ln(|bold(R)|)$
     - Degrees of freedom: $"df" = frac(p(p-1), 2)$
     - *if* $chi^2 >$ critical value at $alpha$ *then* reject sphericity (good for FA)

  4. *Final Decision*
     - *if* KMO $>= 0.6$ *and* Bartlett significant *then* "proceed with FA"
     - *else* "reconsider data or variables"
]

#slide(title: [FA vs PCA — Quick comparison])[
  - PCA: descriptive, decomposes total variance via $S = V Lambda V^T$, components are orthogonal
  - FA: model-based, explains common variance; explicitly models uniqueness ($U_i$)
  - When to use: PCA for compression/visualization; FA when modeling latent constructs & measurement error
]

#section-slide[Theoretical Comparison: PCA vs Factor Analysis]

#slide(title: [Conceptual Differences])[
  #align(center)[
    #table(
      columns: (1fr, 1fr),
      [*Principal Component Analysis*], [*Factor Analysis*],
      [Dimensionality reduction], [Latent variable modeling],
      [Components are linear combinations of all variables], [Factors are hypothetical constructs],
      [Explains total variance], [Explains common variance only],
      [No measurement error model], [Explicitly models unique variance],
      [Descriptive technique], [Statistical model with assumptions],
    )
  ]
]

#slide(title: [Mathematical Perspective])[
  *PCA Approach:*
  - Components are exact linear combinations: $"PC"_j = sum_(i=1)^p w_(i j) X_i$
  - Maximizes variance explained: $max "Var"("PC"_j)$ subject to orthogonality
  - All variance (including noise) is retained in the full solution

  #v(12pt)
  *Factor Analysis Approach:*
  - Models observed variables: $X_i = sum_(j=1)^k lambda_(i j) F_j + U_i$
  - Separates common factors from unique variance
  - Estimates factor loadings and unique variances simultaneously
]

#slide(title: [When Theory Guides Method Selection])[
  *Choose PCA when:*
  - Goal is data compression or visualization
  - Want to capture maximum variance with minimal components
  - No strong assumptions about underlying constructs

  #v(12pt)
  *Choose Factor Analysis when:*
  - Testing specific theories about latent constructs
  - Need to separate measurement error from true factors
  - Interpretability of factors is primary concern
  - Building models for prediction or explanation
]

// ============================================================================
// PART II: EXAMPLE 1 - EDUCATIONAL ASSESSMENT
// ============================================================================

#part-slide[Part II: Example 1 - Educational Assessment]

#section-slide[Example 1A: Educational Assessment PCA]

#slide(title: [Educational Assessment: PCA Analysis])[
  This section demonstrates PCA using controlled synthetic data with known factor structure to validate the method and teach key concepts.
  - *Dataset*: Student assessment data with 6 variables (100 students)
  - *Research Question*: Can PCA recover the underlying ability factors? How does it separate meaningful structure from noise?
  - *Method*: Standardized PCA on synthetic data with known latent factors
  - *Scripts*: `educational_pca.py`
]

#slide(title: [Dataset: Student Assessment Variables])[
  Six variables representing different aspects of student ability:
  - *MathTest*: Mathematics assessment score
  - *VerbalTest*: Verbal reasoning assessment score
  - *SocialSkills*: Social competency rating
  - *Leadership*: Leadership ability rating
  - *RandomVar1, RandomVar2*: Pure noise controls
]

#slide(title: [Known Factor Structure (Ground Truth)])[
  *Ground Truth for Validation:*
  - _Intelligence Factor_: Affects MathTest (0.85 loading) and VerbalTest (0.80 loading)
  - _Personality Factor_: Affects SocialSkills (0.85 loading) and Leadership (0.80 loading)
  - Measurement error added to all meaningful variables (0.2-0.25 noise levels)
]

#slide(title: [PCA Results: Factor Recovery])[
  *Running `educational_pca.py` reveals clear factor structure:*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Component*], [*Eigenvalue*], [*% Variance*], [*Cumulative %*],
      [PC1], [2.203], [36.7%], [36.7%],
      [PC2], [1.608], [26.8%], [63.5%],
      [PC3], [0.842], [14.0%], [77.6%],
      [PC4], [0.736], [12.3%], [89.8%],
      [PC5], [0.322], [5.4%], [95.2%],
      [PC6], [0.289], [4.8%], [100.0%],
    )]

  - *Kaiser Criterion*: Retain PC1-PC2 (eigenvalues > 1.0)
  - *Scree Test*: Clear elbow after PC2
  - *Variance*: Two factors explain 63.5% of total variance
]

#slide(title: [Component Loadings: Structure Discovery])[
  *Loadings matrix reveals underlying factor structure:*

  #text(size: 0.8em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Variable*], [*PC1*], [*PC2*], [*PC3*],
      [MathTest], [0.489], [0.502], [-0.148],
      [VerbalTest], [0.467], [0.518], [0.184],
      [SocialSkills], [0.488], [-0.483], [0.345],
      [Leadership], [0.466], [-0.498], [-0.412],
      [RandomVar1], [0.325], [0.124], [0.634],
      [RandomVar2], [-0.283], [-0.032], [0.502],
    )]

  - *PC1*: General ability factor (all meaningful variables ~0.47-0.49)
  - *PC2*: Cognitive vs. Social separation (positive: Math/Verbal, negative: Social/Leadership)
  - *Noise Validation*: Random variables show weaker, inconsistent patterns
]

#slide(title: [PCA Interpretation: Method Validation])[
  *Factor Recovery Validation (comparing to ground truth):*
  - _Structure Detection_: PCA successfully identifies 2-factor structure
  - _Meaningful vs. Noise_: Max loading for random variables (0.325) < meaningful variables (~0.47)
  - _Factor Separation_: PC2 cleanly separates cognitive (Math/Verbal) from social (Social/Leadership) abilities

  *Practical Insights:*
  - PC1 captures general "ability" factor common in educational assessments
  - PC2 reveals specific cognitive vs. social skill dimensions
  - Noise components (PC5-PC6) have eigenvalues < 0.35, clearly distinguishable

  *Conclusion*: PCA successfully recovers the underlying latent structure from observable variables
]

#section-slide[Example 1B: Educational Assessment Factor Analysis]

#slide(title: [Educational Assessment: Factor Analysis])[
  *Reanalyzing our synthetic student data with Factor Analysis*
  - *Same Dataset*: 100 students, 6 variables (MathTest, VerbalTest, SocialSkills, Leadership, RandomVar1, RandomVar2)
  - *Known Structure*: Intelligence factor + Personality factor + noise
  - *FA Advantage*: Should better identify the true 2-factor structure
  - *Scripts*: `educational_fa.py`
]

#slide(title: [FA Results: Two-Factor Solution])[
  *Running Factor Analysis with Principal Axis Factoring:*

  - *Factor Extraction*: 2 factors retained (eigenvalues > 1.0)
  - *Common Variance*: 63.5% of total variance explained by factors
  - *Communalities*: Range from 0.15 (noise) to 0.74 (meaningful variables)

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Factor*], [*Eigenvalue*], [*% Common Variance*],
      [Factor 1], [2.115], [52.9%],
      [Factor 2], [1.421], [35.5%],
      [Total], [], [88.4%],
    )]
]

#slide(title: [Varimax Rotated Factor Loadings])[
  *After Varimax rotation for cleaner interpretation:*

  #text(size: 0.8em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Variable*], [*Factor 1*], [*Factor 2*], [*Communality*],
      [MathTest], [0.853], [0.054], [0.731],
      [VerbalTest], [0.824], [0.102], [0.690],
      [SocialSkills], [0.089], [0.851], [0.732],
      [Leadership], [0.134], [0.823], [0.695],
      [RandomVar1], [0.182], [0.325], [0.139],
      [RandomVar2], [-0.089], [0.198], [0.047],
    )]

  - *Factor 1*: Intelligence factor (Math/Verbal loadings > 0.82)
  - *Factor 2*: Personality factor (Social/Leadership loadings > 0.82)
  - *Clean structure*: Cross-loadings < 0.15 for meaningful variables
]

#slide(title: [Algorithm: Factor Structure Validation])[
  *Input:* Factor loadings matrix $bold(L)$, communalities $h^2$, theoretical expectations
  *Output:* Validation assessment and interpretability score

  1. *Structure Assessment*
     - *for* each factor $j = 1, dots, k$
       - Identify variables with loadings $|l_(i j)| >$ threshold (typically 0.4)
       - *if* theoretical construct expected
         - Check alignment with expected variables
         - Compute construct recovery score

  2. *Loading Quality Check*
     - *for* each variable $i = 1, dots, p$
       - Count factors with $|l_(i j)| > 0.4$
       - *if* count = 1: simple structure achieved
       - *if* count > 1: complex loading detected

  3. *Communality Analysis*
     - *for* each variable $i$
       - *if* $h^2_i > 0.5$: adequate shared variance
       - *if* $h^2_i < 0.2$: mostly unique variance (potential noise)

  4. *Cross-loading Assessment*
     - Compute $max_(j != j')$ ratio of secondary to primary loadings
     - *if* ratio < 0.3: clean simple structure
     - *if* ratio > 0.7: poor discriminant validity

  5. *return* validation report with construct recovery and structure quality metrics
]

#slide(title: [FA Model Validation: Structure Recovery])[
  *Factor Analysis successfully recovers the true latent structure:*

  - *Perfect Factor Separation*: Each factor loads on exactly the expected variables
    - Factor 1: Math (0.853) + Verbal (0.824) = Intelligence construct
    - Factor 2: Social (0.851) + Leadership (0.823) = Personality construct

  - *Communality Analysis*:
    - Meaningful variables: h² = 0.69-0.73 (good shared variance)
    - Noise variables: h² = 0.05-0.14 (mostly unique variance)

  - *Model Advantages*:
    - Cleaner interpretation than PCA (no cross-loadings)
    - Separates common variance from measurement error
    - Directly tests theoretical factor structure
]

#section-slide[Example 1: PCA vs FA Comparison]

#slide(title: [Real-World Examples: Seeing Theory in Action])[
  *Now that we understand the theory, let's see how PCA and Factor Analysis work with real data!*

  We'll explore several fascinating examples that show the power and differences between these methods:

  *Example 1: Educational Assessment*
  - Can we identify underlying "intelligence" and "personality" factors from test scores?
  - Perfect case to see how FA finds hidden psychological constructs

  *Example 2: Financial Markets*
  - How connected are European stock markets?
  - Shows PCA finding market integration patterns

  *Example 3: Astronomy (Kuiper Belt)*
  - What drives the orbital patterns of distant celestial objects?
  - Demonstrates both methods on high-dimensional scientific data

  *What you'll learn:*
  - When each method gives better insights
  - How to interpret results in context
  - Practical decision-making guidelines
]

#slide(title: [Educational Assessment: Method Comparison])[
  *Direct numerical comparison of PCA vs FA on same data:*

  #text(size: 0.75em)[
    #table(
      columns: (1.2fr, 0.9fr, 0.9fr, 0.9fr, 0.9fr),
      stroke: none,
      [*Variable*], [*PCA-PC1*], [*PCA-PC2*], [*FA-F1*], [*FA-F2*],
      [MathTest], [0.489], [0.502], [0.853], [0.054],
      [VerbalTest], [0.467], [0.518], [0.824], [0.102],
      [SocialSkills], [0.488], [-0.483], [0.089], [0.851],
      [Leadership], [0.466], [-0.498], [0.134], [0.823],
      [RandomVar1], [0.325], [0.124], [0.182], [0.325],
      [RandomVar2], [-0.283], [-0.032], [-0.089], [0.198],
    )]

  - *PCA*: Mixed loadings, harder to interpret (PC1 = general factor)
  - *FA*: Clean factor separation, perfect theoretical alignment
  - *Variance*: PCA explains 63.5% total variance, FA explains 88.4% common variance
]

#slide(title: [Educational Assessment: Decision Guidelines])[
  *Use PCA when:*
  - Goal is dimensionality reduction for visualization or compression
  - Want to maximize variance explained regardless of interpretability
  - No strong theoretical expectations about factor structure

  #v(12pt)
  *Use Factor Analysis when:*
  - Testing specific theoretical models (Intelligence + Personality)
  - Need to separate measurement error from true constructs
  - Interpretability of factors is primary concern
  - Developing or validating psychological assessments
]

// ============================================================================
// PART III: EXAMPLE 2 - EUROPEAN STOCK MARKETS
// ============================================================================

#part-slide[Part III: Example 2 - European Stock Markets]

#section-slide[Example 2A: European Stock Markets PCA]

#slide(title: [European Stock Markets: PCA Analysis])[
  This section demonstrates PCA applied to financial markets using synthetic European stock market data.
  - *Dataset*: 4 major European indices (DAX, SMI, CAC, FTSE) over 1,860 trading days
  - *Research Question*: How integrated are European financial markets? Can we identify common market factors?
  - *Method*: Standardized PCA on correlation matrix of daily returns
  - *Scripts*: `invest_pca.py`
]

#slide(title: [Dataset: European Market Indices])[
  - *DAX (Germany)*: Frankfurt Stock Exchange — largest European economy
  - *SMI (Switzerland)*: Swiss Market Index — major financial center
  - *CAC (France)*: Paris Stock Exchange — core eurozone market
  - *FTSE (UK)*: London Stock Exchange — major international hub
]

#slide(title: [PCA Results: Market Integration])[
  *Running `invest_pca.py` reveals extraordinary market integration:*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Component*], [*Eigenvalue*], [*% Variance*], [*Cumulative %*],
      [PC1], [3.895], [97.3%], [97.3%],
      [PC2], [0.092], [2.3%], [99.6%],
      [PC3], [0.011], [0.3%], [99.9%],
      [PC4], [0.004], [0.1%], [100.0%],
    )]

  - *Dominant PC1*: Captures almost all variance (97.3%)
  - *Kaiser Criterion*: Only PC1 has eigenvalue > 1.0
  - *Interpretation*: European markets move as a single integrated system
  - *Implication*: Extremely limited diversification within Europe
]

#slide(title: [Component Loadings: Perfect Market Synchronization])[
  *All European markets load equally on PC1 (common market factor):*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Market Index*], [*PC1 Loading*], [*PC2 Loading*],
      [DAX (Germany)], [0.501], [0.502],
      [SMI (Switzerland)], [0.501], [-0.513],
      [CAC (France)], [0.500], [0.351],
      [FTSE (UK)], [0.499], [-0.625],
    )]

  - *PC1 Interpretation*: Uniform loadings (~0.50) = perfect market integration
  - *PC2 Interpretation*: Subtle Brexit effect (FTSE vs continental markets)
  - *Financial Reality*: Global/EU-wide factors dominate individual market performance
]

#slide(title: [Financial Interpretation: Systematic Risk Dominance])[
  *PC1 as European Systematic Risk Factor:*

  - *Market Integration*: 97.3% shared variance indicates extreme integration
    - European markets behave as single economic unit
    - Global economic conditions affect all markets simultaneously
    - ECB monetary policy, EU regulations, major political events

  - *Portfolio Implications*:
    - Diversification within Europe provides minimal risk reduction
    - Need global (non-European) assets for meaningful diversification
    - European "diversified" portfolio = ~97% systematic risk exposure

  - *Risk Management*:
    - PC1 represents non-diversifiable risk within European context
    - PC2-PC4 (2.7% total) = market-specific idiosyncratic opportunities
    - Brexit effect visible in PC2 (FTSE vs continental separation)
]

#section-slide[Example 2B: European Stock Markets Factor Analysis]

#slide(title: [European Stock Markets: Factor Analysis])[
  *Applying Factor Analysis to financial market data:*
  - *Same Dataset*: 4 European indices with daily returns over 1,860 days
  - *FA Perspective*: Model latent market factors driving stock correlations
  - *Research Question*: How many common market factors underlie European integration?
  - *Scripts*: `invest_fa.py`
]

#slide(title: [FA Results: Single-Factor Market Structure])[
  *Factor Analysis confirms PCA findings with cleaner interpretation:*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Market Index*], [*Factor 1 Loading*], [*Communality*],
      [DAX (Germany)], [0.987], [0.974],
      [SMI (Switzerland)], [0.987], [0.974],
      [CAC (France)], [0.986], [0.972],
      [FTSE (UK)], [0.985], [0.970],
    )]

  - *Single Factor Solution*: 1 factor retained (eigenvalue = 3.891)
  - *Factor Interpretation*: Common European Market Factor
  - *Variance Explained*: 97.3% of common variance among markets
  - *High Communalities*: 97%+ shared variance for all markets
]

#slide(title: [FA Model: Financial Risk Decomposition])[
  *Factor Analysis provides clean financial interpretation:*

  - *Systematic Risk Factor*: Single factor with near-perfect loadings (~0.986)
    - Represents common exposure to EU economic conditions
    - ECB monetary policy, European political events, global risk sentiment
    - All markets equally exposed to systematic European risk

  - *Unique Variances*: Only 2.7% unexplained (idiosyncratic risk)
    - DAX: German-specific industrial/manufacturing cycles
    - FTSE: Brexit-related UK political developments
    - SMI: Swiss franc currency effects
    - CAC: France-specific fiscal/political events

  - *Portfolio Theory Application*:
    - Single-factor model: R_i = α_i + β_i F + ε_i
    - All β_i ≈ 0.986 (equal systematic risk exposure)
    - Diversification requires assets outside European factor space
]

#section-slide[Example 2: PCA vs FA Comparison]

#slide(title: [European Markets: PCA vs FA Comparison])[
  *Both methods converge on single-factor structure, but with different perspectives:*

  #text(size: 0.8em)[
    #table(
      columns: (1.1fr, 1fr, 1fr),
      stroke: none,
      [*Aspect*], [*PCA Results*], [*FA Results*],
      [Eigenvalue/Factor], [3.895], [3.891],
      [Variance Explained], [97.3% total variance], [97.3% common variance],
      [Loadings Range], [0.499-0.501], [0.985-0.987],
      [Interpretation], [Principal component], [Latent market factor],
      [Risk Decomposition], [PC1 + noise components], [Systematic + unique variances],
      [Application], [Data reduction], [Risk modeling],
    )]

  - *Convergence*: Both identify single dominant dimension
  - *Difference*: FA provides cleaner risk interpretation
  - *Financial Context*: FA loadings directly interpretable as risk exposures
]

#slide(title: [European Markets: Decision Guidelines])[
  *Use PCA when:*
  - Goal is dimensionality reduction for portfolio optimization
  - Want to capture maximum variance with fewest components
  - Creating market indices or risk monitoring systems

  #v(12pt)
  *Use Factor Analysis when:*
  - Building risk models for portfolio management
  - Need to separate systematic from idiosyncratic risk
  - Developing factor-based trading strategies
  - Stress testing with specific factor scenarios
]

// ============================================================================
// PART IV: EXAMPLE 3 - KUIPER BELT OBJECTS
// ============================================================================

#part-slide[Part IV: Example 3 - Kuiper Belt Objects]

#section-slide[Example 3A: Kuiper Belt Objects PCA]

#slide(title: [Kuiper Belt Objects: PCA Analysis])[
  This section demonstrates PCA applied to astronomical data from the outer solar system.
  - *Dataset*: Orbital parameters of 98 trans-Neptunian objects (TNOs) and Kuiper Belt objects
  - *Research Question*: What are the main modes of orbital variation? Can we identify distinct dynamical populations?
  - *Method*: Standardized PCA on 5 orbital elements with different physical units
  - *Scripts*: `kuiper_pca.py`
]

#slide(title: [Dataset: Orbital Parameters])[
  Five key orbital elements describe each object's motion:
  - *a* (AU): Semi-major axis — average distance from Sun (30-150 AU)
  - *e*: Eccentricity — orbital shape (0=circle, 1=parabola)
  - *i* (degrees): Inclination — tilt relative to solar system plane
  - *H* (magnitude): Absolute magnitude — brightness/size indicator
]

#slide(title: [Known Dynamical Populations])[
  Three main populations with distinct orbital signatures:
  - *Classical Kuiper Belt* (60%): Low eccentricity, low inclination
    - Nearly circular orbits around 39-48 AU
    - "Cold" population — likely formed in place
  - *Scattered Disk Objects* (30%): High eccentricity, distant
    - $e > 0.3$, semi-major axis $> 50$ AU
    - Scattered outward by gravitational encounters with Neptune
  - *Resonant Objects* (10%): Locked in orbital resonances
    - 3:2 resonance at ~39.4 AU (like Pluto)
]

#slide(title: [PCA Results: Multi-Component Structure])[
  *Running `kuiper_pca.py` reveals distributed variance across components:*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Component*], [*Eigenvalue*], [*% Variance*], [*Cumulative %*],
      [PC1], [2.009], [39.8%], [39.8%],
      [PC2], [1.079], [21.4%], [61.1%],
      [PC3], [1.036], [20.5%], [81.6%],
      [PC4], [0.628], [12.4%], [94.1%],
      [PC5], [0.299], [5.9%], [100.0%],
    )]

  - *Kaiser Criterion*: Retain PC1-PC3 (eigenvalues > 1.0)
  - *Variance Distribution*: More balanced than previous examples
  - *Interpretation*: Complex astronomical system requires multiple dimensions
]

#slide(title: [Component Loadings: Astronomical Interpretation])[
  *Each component captures distinct aspects of orbital architecture:*

  #text(size: 0.8em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Variable*], [*PC1*], [*PC2*], [*PC3*],
      [a (distance)], [0.571], [-0.172], [-0.578],
      [e (eccentricity)], [0.642], [0.087], [-0.117],
      [i (inclination)], [0.487], [0.378], [0.705],
      [H (magnitude)], [-0.157], [0.905], [-0.393],
    )]

  - *PC1*: "Orbital Excitation" - distance (a), eccentricity (e), inclination (i) correlate
  - *PC2*: "Observational Bias" - brightness (H) dominates, reflecting size-distance effects
  - *PC3*: "Resonant Structure" - inclination vs distance separation, identifies resonant families
]

#slide(title: [PCA Interpretation: Dynamical Evolution])[
  *PC1 as Dynamical Excitation:*
  - High loadings on distance (a), eccentricity (e), and inclination (i)
  - Represents gravitational "heating" of orbits over solar system history
  - Separates pristine objects from those scattered by planetary migration
  - *Implication*: Multiple gravitational processes create complex structure
]

#section-slide[Example 3B: Kuiper Belt Objects Factor Analysis]

#slide(title: [Kuiper Belt Objects: Factor Analysis])[
  *Applying Factor Analysis to astronomical orbital dynamics data:*
  - *Same Dataset*: 98 trans-Neptunian objects with 5 orbital parameters
  - *FA Approach*: Model latent dynamical factors affecting orbital elements
  - *Expected Factors*: Dynamical excitation, size-distance relationships, resonance effects
  - *Scripts*: `kuiper_fa.py`
]

#slide(title: [FA Results: Three-Factor Solution])[
  *Principal Axis Factoring with Varimax rotation yields clear structure:*

  #text(size: 0.8em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Parameter*], [*Factor 1*], [*Factor 2*], [*Factor 3*], [*Communality*],
      [a (distance)], [0.733], [-0.296], [-0.307], [0.725],
      [e (eccentricity)], [0.896], [-0.114], [-0.082], [0.821],
      [i (inclination)], [0.770], [0.301], [0.218], [0.732],
      [H (magnitude)], [-0.048], [-0.081], [0.953], [0.917],
      [designation], [-0.049], [0.940], [-0.084], [0.892],
    )]

  - *3 factors retained*: Eigenvalues [1.989, 1.068, 1.025]
  - *Common variance*: 81.7% explained by factors
  - *Clean structure*: Varimax rotation provides clear interpretation
]

#slide(title: [Astrophysical Factor Interpretation])[
  *Each factor represents distinct physical processes:*

  - *Factor 1: Dynamical Excitation* (a=0.733, e=0.896, i=0.770)
    - Orbital "heating" by gravitational scattering with Neptune
    - High scores: Scattered Disk Objects with excited orbits
    - Low scores: Classical Kuiper Belt with pristine, cold orbits

  - *Factor 2: Discovery Sequence* (designation=0.940)
    - Data artifact reflecting discovery order bias
    - Brighter objects discovered first (lower designation numbers)
    - Demonstrates importance of recognizing non-physical factors

  - *Factor 3: Size/Brightness Factor* (H=0.953)
    - Absolute magnitude as proxy for object size
    - Selection effects: larger objects easier to detect at distance
    - Physical process: size-dependent collisional evolution
]

#section-slide[Example 3: PCA vs FA Comparison]

#slide(title: [Kuiper Belt: PCA vs FA Comparison])[
  *Both methods identify 3-factor structure with different emphases:*

  #text(size: 0.75em)[
    #table(
      columns: (1fr, 1fr, 1fr, 1fr),
      stroke: none,
      [*Orbital Parameter*], [*PCA-PC1*], [*FA-Factor1*], [*Interpretation*],
      [a (distance)], [0.571], [0.733], [FA stronger dynamical grouping],
      [e (eccentricity)], [0.642], [0.896], [FA emphasizes orbital excitation],
      [i (inclination)], [0.487], [0.770], [FA cleaner dynamical factor],
      [H (magnitude)], [-0.157], [-0.048], [PCA mixed, FA separates as Factor 3],
    )]

  - *Variance explained*: PCA 81.6% (3 PCs), FA 81.7% (3 factors)
  - *Structure clarity*: FA provides cleaner separation of physical processes
  - *Scientific value*: FA factors directly map to astrophysical theories
  - *Discovery bias*: FA explicitly identifies designation artifact (Factor 2)
]

#slide(title: [Kuiper Belt: Decision Guidelines])[
  *Use PCA when:*
  - Goal is reducing orbital parameter dimensionality
  - Want to capture maximum orbital variation
  - Creating classification schemes for large surveys

  #v(12pt)
  *Use Factor Analysis when:*
  - Testing theories about solar system formation and evolution
  - Need to separate observational bias from physical processes
  - Modeling specific dynamical mechanisms
  - Comparing our solar system to exoplanetary debris disks
]

// ============================================================================
// PART V: EXAMPLE 4 - HOSPITAL HEALTH OUTCOMES
// ============================================================================

#part-slide[Part V: Example 4 - Hospital Health Outcomes]

#section-slide[Example 4A: Hospital Health Outcomes PCA]

#slide(title: [Hospital Health Outcomes: PCA Analysis])[
  This section demonstrates PCA applied to healthcare quality data from US hospitals.
  - *Dataset*: Health outcome metrics for 50 US hospitals across 8 performance indicators
  - *Research Question*: What are the main dimensions of hospital quality? Can we rank hospital performance?
  - *Method*: Standardized PCA on healthcare metrics with different units and scales
  - *Scripts*: `hospitals_example.py`
]

#slide(title: [Dataset: Hospital Performance Metrics])[
  Eight key hospital quality indicators (with desired direction):
  - *MortalityRate* (%): Hospital mortality rate (lower → better)
  - *ReadmissionRate* (%): 30-day readmission rate (lower → better)
  - *PatientSatisfaction* (0-100): Patient satisfaction score (higher → better)
  - *AvgLengthStay* (days): Average length of stay (shorter → better)
  - *InfectionRate* (%): Hospital-acquired infections (lower → better)
  - *NurseRatio*: Nurse-to-patient ratio (higher → better)
  - *SurgicalComplications* (%): Surgical complication rate (lower → better)
  - *EDWaitTime* (minutes): Emergency dept. wait time (lower → better)
]

#slide(title: [PCA Results: Strong Quality Factor])[
  *Running `hospitals_pca.py` reveals dominant quality dimension:*

  #text(size: 0.85em)[
    #table(
      columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Component*], [*Eigenvalue*], [*% Variance*], [*Cumulative %*],
      [PC1], [5.752], [70.5%], [70.5%],
      [PC2], [0.695], [8.5%], [79.0%],
      [PC3], [0.480], [5.9%], [84.9%],
      [PC4-PC8], [all below 0.50], [15.1%], [100.0%],
    )]

  - *Dominant PC1*: Single quality factor explains 70.5% variance
  - *Kaiser Criterion*: Only PC1 has eigenvalue > 1.0
  - *Interpretation*: Hospital quality is largely unidimensional
  - *Healthcare Insight*: Organizational excellence affects all metrics simultaneously
]

#slide(title: [Component Loadings: Quality Halo Effect])[
  *PC1 shows consistent quality pattern across all metrics:*

  #text(size: 0.8em)[
    #table(
      columns: (1.4fr, 0.8fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Health Outcome Metric*], [*PC1*], [*PC2*], [*PC3*],
      [SurgicalComplications (↓)], [-0.378], [-0.002], [-0.156],
      [MortalityRate (↓)], [-0.353], [-0.368], [-0.337],
      [ReadmissionRate (↓)], [-0.352], [0.150], [0.515],
      [PatientSatisfaction (↑)], [0.402], [0.059], [0.188],
      [NurseRatio (↑)], [0.381], [0.041], [0.160],
      [InfectionRate (↓)], [-0.337], [0.187], [-0.358],
      [EDWaitTime (↓)], [-0.311], [-0.528], [0.597],
      [AvgLengthStay (↓)], [-0.302], [0.723], [0.226],
    )]

  - *Consistent Pattern*: All "bad" outcomes load negatively, "good" outcomes positively
  - *Quality Halo*: Excellent hospitals excel across all dimensions
  - *PC2*: Efficiency dimension (length of stay vs wait time trade-off)
]

#slide(title: [Healthcare Interpretation: Organizational Excellence])[
  *PC1 as Systematic Quality Factor:*

  - *Organizational Culture*: Leadership, processes, and culture affect all outcomes
    - Quality improvement programs create hospital-wide excellence
    - Poor management leads to problems across multiple domains
    - Safety culture and continuous improvement mindset crucial

  - *Policy Implications*:
    - Hospital rankings can use single composite score (PC1)
    - Quality interventions should be comprehensive, not focused on single metrics
    - Resource allocation should target hospitals with low PC1 scores

  - *Healthcare Economics*:
    - High-quality hospitals are more efficient (better outcomes at lower cost)
    - Bundled payments incentivize comprehensive quality improvement
    - Value-based care models align with PC1 structure
]

#section-slide[Example 4B: Hospital Health Outcomes Factor Analysis]

#slide(title: [Hospital Health Outcomes: Factor Analysis])[
  *Applying Factor Analysis to healthcare quality data:*
  - *Same Dataset*: 50 hospitals with 8 quality indicators
  - *FA Perspective*: Model latent quality factors driving performance correlations
  - *Expected Factors*: Overall quality factor, specific care dimensions
  - *Scripts*: `hospitals_fa.py`
]

#slide(title: [FA Results: Single Quality Factor Model])[
  *Principal Axis Factoring confirms unidimensional quality structure:*

  #text(size: 0.8em)[
    #table(
      columns: (1.4fr, 0.8fr, 0.8fr),
      stroke: none,
      [*Health Outcome Metric*], [*Factor 1*], [*Communality*],
      [PatientSatisfaction], [0.954], [0.911],
      [NurseRatio], [0.905], [0.820],
      [SurgicalComplications], [-0.896], [0.804],
      [MortalityRate], [-0.838], [0.702],
      [ReadmissionRate], [-0.836], [0.699],
      [InfectionRate], [-0.800], [0.640],
      [EDWaitTime], [-0.739], [0.546],
      [AvgLengthStay], [-0.717], [0.515],
    )]

  - *Single Factor Solution*: 1 factor retained (eigenvalue = 5.637)
  - *Common Variance*: 70.5% explained by quality factor
  - *Clean Structure*: All metrics load appropriately on general quality
]

#slide(title: [FA Model: Healthcare Quality Theory])[
  *Factor Analysis validates theoretical quality model:*

  - *Unidimensional Quality*: Single latent factor drives all observable outcomes
    - Organizational excellence affects all aspects of care delivery
    - Leadership quality cascades through clinical and operational metrics
    - Quality culture creates systematic improvements across domains

  - *Unique Variances*: Hospital-specific factors
    - AvgLengthStay (48.5% unique): Care philosophy and patient population effects
    - EDWaitTime (45.4% unique): Operational efficiency and facility design
    - Higher communalities for clinical outcomes than operational metrics

  - *Healthcare Policy*: Evidence for holistic quality improvement
    - Single quality factor supports composite hospital rating systems
    - Interventions should target organizational culture, not isolated metrics
]

#section-slide[Example 4: PCA vs FA Comparison]

#slide(title: [Hospital Quality: PCA vs FA Comparison])[
  *Both methods converge on single quality dimension with excellent agreement:*

  #text(size: 0.75em)[
    #table(
      columns: (1.3fr, 0.8fr, 0.8fr, 1fr),
      stroke: none,
      [*Health Metric*], [*PCA-PC1*], [*FA-Factor1*], [*Interpretation Agreement*],
      [SurgicalComplications], [-0.378], [-0.892], [Strong negative correlation],
      [MortalityRate], [-0.353], [-0.854], [Strong negative correlation],
      [PatientSatisfaction], [0.402], [0.801], [Strong positive correlation],
      [NurseRatio], [0.381], [0.785], [Strong positive correlation],
      [InfectionRate], [-0.337], [-0.831], [Strong negative correlation],
      [ReadmissionRate], [-0.352], [-0.823], [Strong negative correlation],
    )]

  - *Convergent validity*: Both methods identify identical quality structure
  - *FA advantage*: Cleaner loadings and direct latent factor interpretation
  - *Healthcare application*: Single quality score validated by both approaches
]

#slide(title: [Hospital Quality: Decision Guidelines])[
  *Use PCA when:*
  - Creating hospital quality rankings and public report cards
  - Developing single composite quality scores for value-based payments
  - Identifying best and worst performing hospitals for recognition/intervention
  - Data reduction for large healthcare surveillance systems

  #v(12pt)
  *Use Factor Analysis when:*
  - Building theoretical models of healthcare quality for policy research
  - Developing targeted quality improvement interventions
  - Validating quality assessment instruments and surveys
  - Understanding organizational vs. clinical vs. operational quality factors
  - Testing healthcare quality theories with empirical data
]

// ============================================================================
// PART VI: OVERALL COMPARISON AND GUIDELINES
// ============================================================================

#part-slide[Part VI: Overall Comparison and Guidelines]

#section-slide[Summary: Method Comparison Across Examples]

#slide(title: [Cross-Example Summary])[
  #align(center)[
    #table(
      columns: (1fr, 1fr, 1fr, 1fr, 1fr),
      [*Example*], [*Domain*], [*PCA Strength*], [*FA Strength*], [*Recommendation*],
      [Educational Assessment], [Psychology], [Factor discovery], [Theory testing], [FA for construct validation],
      [European Markets], [Finance], [Risk factor identification], [Risk decomposition], [Both methods valuable],
      [Kuiper Belt Objects],
      [Astronomy],
      [Population classification],
      [Physical process modeling],
      [FA for theory testing],

      [Hospital Quality], [Healthcare], [Quality rankings], [Quality dimensions], [PCA for rankings, FA for policy],
    )
  ]
]

#section-slide[Guidelines for Method Selection]

#slide(title: [Algorithm: Method Selection Decision Procedure])[
  *Input:* Dataset characteristics, research goals, theoretical knowledge
  *Output:* Recommended method (PCA, FA, or both)

  1. *Goal Assessment*
     - *if* primary goal = dimensionality reduction → score_PCA += 2
     - *if* primary goal = latent construct modeling → score_FA += 2
     - *if* primary goal = data compression → score_PCA += 1
     - *if* primary goal = theory testing → score_FA += 2

  2. *Theoretical Knowledge Check*
     - *if* strong theoretical expectations about factors exist → score_FA += 2
     - *if* no theoretical framework available → score_PCA += 1
     - *if* exploratory analysis needed → score_PCA += 1

  3. *Practical Requirements*
     - *if* need interpretable factors with rotation → score_FA += 1
     - *if* need maximum variance explained → score_PCA += 1
     - *if* measurement error modeling important → score_FA += 2
     - *if* simple index/ranking needed → score_PCA += 2

  4. *Sample Size Consideration*
     - *if* n < 5p → recommend PCA (more stable)
     - *if* n >= 10p → both methods suitable

  5. *Decision Rule*
     - *if* score_FA > score_PCA + 1 → recommend Factor Analysis
     - *if* score_PCA > score_FA + 1 → recommend PCA
     - *else* → recommend both methods for comparison
]

#slide(title: [When to Use PCA vs Factor Analysis])[
  *Use PCA when:*
  - Primary goal is dimensionality reduction
  - You want to maximize variance explained
  - Data compression or noise reduction is the objective
  - You don't have strong theoretical expectations about latent constructs
  - Creating indices or rankings

  #v(12pt)
  *Use Factor Analysis when:*
  - You want to model latent constructs or theoretical factors
  - Understanding measurement error and unique variance is important
  - You need factor rotation for cleaner interpretation
  - Confirmatory analysis of hypothesized factor structures
  - Building predictive models with interpretable factors
]

#slide(title: [Algorithm: Cross-Validation for Factor/Component Models])[
  *Input:* Dataset $bold(X)$, proposed model (PCA/FA), number of factors $k$
  *Output:* Cross-validation error, model stability assessment

  1. *Split Data*
     - Randomly partition $bold(X)$ into training (80%) and testing (20%) sets
     - Ensure balanced representation across variables

  2. *Training Phase*
     - Fit model on training data: extract $k$ factors/components
     - Obtain loadings matrix $bold(L)_"train"$ and transformation $bold(W)_"train"$
     - Record eigenvalues $lambda_"train" = (lambda_1, dots, lambda_k)$

  3. *Testing Phase*
     - Apply $bold(W)_"train"$ to testing data: $bold(F)_"test" = bold(X)_"test" bold(W)_"train"$
     - Reconstruct testing data: $hat(bold(X))_"test" = bold(F)_"test" bold(L)_"train"^top$
     - Compute reconstruction error: $"RMSE" = ||bold(X)_"test" - hat(bold(X))_"test"||_F / sqrt(n_"test" times p)$

  4. *Stability Assessment*
     - *repeat* steps 1-3 for $B$ bootstrap samples
     - Compute variance of eigenvalues: $sigma^2(lambda_j)$ for each factor
     - Check loading consistency: correlation between $bold(L)_b$ across bootstrap samples

  5. *Model Selection*
     - *if* RMSE increases substantially with testing data → overfitting detected
     - *if* eigenvalue variance high → unstable factor structure
     - Select $k$ that minimizes average RMSE with acceptable stability
]

#slide(title: [Practical Recommendations])[
  - *Start with EDA*: Use PCA first to understand your data structure
  - *Theory-driven analysis*: Apply Factor Analysis when you have theoretical expectations
  - *Compare both methods*: Results convergence strengthens conclusions
  - *Consider sample size*: Factor Analysis requires larger samples
  - *Validate results*: Use cross-validation, external criteria, or confirmatory approaches
]

#slide(title: [Algorithm: Comprehensive PCA vs FA Comparison Workflow])[
  *Input:* Dataset $bold(X)$, research question, theoretical background
  *Output:* Method recommendation with supporting evidence

  1. *Exploratory Phase*
     - Run PCA with standardized data
     - Apply Kaiser criterion and scree test for factor retention
     - Examine explained variance and component interpretability

  2. *Confirmatory Phase*
     - Run Factor Analysis with same factor number as PCA
     - Apply both orthogonal (Varimax) and oblique (Promax) rotation
     - Compute model fit statistics (RMSEA, TLI, CFI if available)

  3. *Comparison Metrics*
     - Loading similarity: $r(bold(L)_"PCA", bold(L)_"FA")$ for each factor
     - Interpretability score: count of "clean" loadings (> 0.4, < 0.3 cross-loadings)
     - Variance explained: total and per-factor comparison
     - Factor score correlation: $r(bold(F)_"PCA", bold(F)_"FA")$

  4. *Decision Matrix*
     - Rate each method on: interpretability, variance explained, theoretical fit
     - Weight criteria based on research goals
     - *if* high agreement (r > 0.85) → either method acceptable
     - *if* FA provides cleaner structure → recommend FA
     - *if* PCA explains substantially more variance → recommend PCA

  5. *Final Validation*
     - Cross-validate selected method using Algorithm: Cross-Validation
     - Test robustness with different sample splits
     - Assess generalizability to similar datasets if available
]

#slide(title: [A Word of Caution])[
  - Neither method can _prove_ a factor structure is correct
  - Multiple equally valid models may exist for the same dataset
  - Always combine statistical results with domain knowledge
  - Consider the interpretability-variance trade-off
  - Be cautious about overgeneralization from single datasets
]

#slide(title: [Course Conclusion])[
  *Key Takeaways:*
  - PCA and Factor Analysis serve different but complementary purposes
  - The choice of method should align with your research goals
  - Both methods reveal important structure in multivariate data
  - Pedagogical approach: theory → application → comparison enhances understanding
  - Real-world applications span multiple domains with different requirements

  #v(12pt)
  *Next Steps:*
  - Practice with your own datasets
  - Explore advanced techniques (confirmatory FA, structural equation modeling)
  - Consider modern alternatives (nonlinear methods, sparse PCA)
]

// ============================================================================
// APPENDIX: MATHEMATICAL FOUNDATIONS
// ============================================================================

#part-slide[Appendix: Mathematical Foundations]

#section-slide[Matrix Algebra Foundations]

#slide(title: [Essential Matrix Operations for Multivariate Analysis])[
  *Matrix Transpose Properties:*
  - $(bold(A)^top)^top = bold(A)$
  - $(bold(A) bold(B))^top = bold(B)^top bold(A)^top$
  - $(bold(A) + bold(B))^top = bold(A)^top + bold(B)^top$

  *Matrix Multiplication Rules:*
  - $bold(A) bold(B)$ defined when columns of $bold(A) =$ rows of $bold(B)$
  - $(bold(A) bold(B)) bold(C) = bold(A) (bold(B) bold(C))$ (associative)
  - $bold(A) (bold(B) + bold(C)) = bold(A) bold(B) + bold(A) bold(C)$ (distributive)

  *Trace of Matrix:*
  - $"tr"(bold(A)) = sum_(i=1)^n a_(i i)$ (sum of diagonal elements)
  - $"tr"(bold(A) + bold(B)) = "tr"(bold(A)) + "tr"(bold(B))$
  - $"tr"(bold(A) bold(B)) = "tr"(bold(B) bold(A))$ (cyclic property)
  - $"tr"(bold(A)^top bold(A)) = sum_(i,j) a_(i j)^2 = ||bold(A)||_F^2$ (Frobenius norm)
]

#slide(title: [Quadratic Forms and Positive Definite Matrices])[
  *Quadratic Form:* $Q(bold(x)) = bold(x)^top bold(A) bold(x)$ where $bold(A)$ is symmetric

  *Positive Definite Matrix:* $bold(A)$ is positive definite if:
  - $bold(x)^top bold(A) bold(x) > 0$ for all $bold(x) != bold(0)$
  - All eigenvalues $lambda_i > 0$
  - Determinant $|bold(A)| > 0$

  *Positive Semi-definite Matrix:* $bold(A)$ is positive semi-definite if:
  - $bold(x)^top bold(A) bold(x) >= 0$ for all $bold(x)$
  - All eigenvalues $lambda_i >= 0$

  *Covariance Matrix Properties:*
  - Always symmetric: $bold(Sigma) = bold(Sigma)^top$
  - Always positive semi-definite: $bold(x)^top bold(Sigma) bold(x) >= 0$
  - If non-singular: positive definite with $|bold(Sigma)| > 0$
]

#slide(title: [Matrix Norms and Distances])[
  *Vector Norms:*
  - $L_2$ norm: $||bold(x)||_2 = sqrt(bold(x)^top bold(x)) = sqrt(sum_(i=1)^p x_i^2)$
  - Unit vector: $||bold(x)||_2 = 1$

  *Matrix Norms:*
  - Frobenius norm: $||bold(A)||_F = sqrt("tr"(bold(A)^top bold(A))) = sqrt(sum_(i,j) a_(i j)^2)$
  - Spectral norm: $||bold(A)||_2 = sqrt(lambda_"max"(bold(A)^top bold(A)))$

  *Distance Measures:*
  - Euclidean distance: $d(bold(x), bold(y)) = ||bold(x) - bold(y)||_2$
  - Mahalanobis distance: $d_M(bold(x), bold(y)) = sqrt((bold(x) - bold(y))^top bold(Sigma)^(-1) (bold(x) - bold(y)))$

  *Orthogonality:*
  - Vectors orthogonal: $bold(x)^top bold(y) = 0$
  - Orthogonal matrix: $bold(Q)^top bold(Q) = bold(I)$, preserves lengths and angles
]

#slide(title: [Advanced Matrix Algebra for Factor Analysis])[
  *Matrix Inverse Properties:*
  - $(bold(A)^(-1))^(-1) = bold(A)$
  - $(bold(A) bold(B))^(-1) = bold(B)^(-1) bold(A)^(-1)$
  - $(bold(A)^top)^(-1) = (bold(A)^(-1))^top$

  *Sherman-Morrison-Woodbury Formula:*
  For factor model covariance $bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi)$:
  $bold(Sigma)^(-1) = bold(Psi)^(-1) - bold(Psi)^(-1) bold(Lambda) (bold(I) + bold(Lambda)^top bold(Psi)^(-1) bold(Lambda))^(-1) bold(Lambda)^top bold(Psi)^(-1)$
]

#slide(title: [Algorithm: Efficient Covariance Matrix Inversion])[
  *Input:* Factor loadings $bold(Lambda) in RR^(p times k)$, uniquenesses $bold(Psi) in RR^(p times p)$

  *Output:* Inverse covariance matrix $bold(Sigma)^(-1)$

  1. *Direct Inversion* (computational cost: $O(p^3)$)
     - Compute $bold(Sigma) = bold(Lambda) bold(Lambda)^top + bold(Psi)$
     - Invert: $bold(Sigma)^(-1) = (bold(Lambda) bold(Lambda)^top + bold(Psi))^(-1)$

  2. *Sherman-Morrison-Woodbury Method* (computational cost: $O(k^3 + k^2 p)$ where $k << p$)
     - *Step 1:* Compute $bold(Psi)^(-1)$ (diagonal, so $O(p)$)
     - *Step 2:* Compute $bold(M) = bold(I) + bold(Lambda)^top bold(Psi)^(-1) bold(Lambda)$ ($k times k$ matrix)
     - *Step 3:* Invert small matrix: $bold(M)^(-1)$ (cost: $O(k^3)$)
     - *Step 4:* Apply formula:
       $bold(Sigma)^(-1) = bold(Psi)^(-1) - bold(Psi)^(-1) bold(Lambda) bold(M)^(-1) bold(Lambda)^top bold(Psi)^(-1)$

  3. *Computational Efficiency Analysis*
     - *if* $k << p$ *then* use Sherman-Morrison-Woodbury
     - *else* use direct inversion
     - *Typical case:* $k approx p/5$ gives $approx 100times$ speedup

  4. *Numerical Stability Check*
     - Verify $bold(Psi)$ is positive definite (all diagonal elements $> 0$)
     - Check condition number of $bold(M)$ before inversion
]

#slide(title: [Algorithm: Matrix Calculus for ML Estimation])[
  *Input:* Scalar function $f(bold(X))$ where $bold(X) in RR^(m times n)$

  *Output:* Gradient matrix $frac(partial f, partial bold(X)) in RR^(m times n)$

  1. *Linear Trace Function: $f(bold(X)) = "tr"(bold(A) bold(X))$*
     - *Rule:* $frac(partial, partial bold(X)) "tr"(bold(A) bold(X)) = bold(A)^top$
     - *Derivation:* Use index notation and sum rule
     - *Application:* Linear terms in likelihood functions

  2. *Quadratic Trace Function: $f(bold(X)) = "tr"(bold(X)^top bold(A) bold(X))$*
     - *Rule:* $frac(partial, partial bold(X)) "tr"(bold(X)^top bold(A) bold(X)) = (bold(A) + bold(A)^top) bold(X)$
     - *Special case:* If $bold(A)$ is symmetric, then $frac(partial, partial bold(X)) "tr"(bold(X)^top bold(A) bold(X)) = 2 bold(A) bold(X)$
     - *Application:* Quadratic forms in likelihood functions

  3. *Log-Determinant Function: $f(bold(X)) = ln|bold(X)|$*
     - *Rule:* $frac(partial, partial bold(X)) ln|bold(X)| = (bold(X)^(-1))^top$
     - *Constraint:* $bold(X)$ must be invertible
     - *Application:* Normalizing constants in multivariate normal densities

  4. *Chain Rule Application*
     - For composite functions: $frac(partial, partial bold(X)) f(g(bold(X))) = frac(partial f, partial g) frac(partial g, partial bold(X))$
     - *Example:* $frac(partial, partial bold(Lambda)) ln|bold(Lambda) bold(Lambda)^top + bold(Psi)| = $ (requires chain rule)

  *ML Estimation Context:* These derivatives compute gradients of log-likelihood functions for optimization.
]

#slide(title: [Algorithm: Eigenvalue Decomposition Methods])[
  *Input:* Symmetric matrix $bold(A) in RR^(p times p)$, tolerance $epsilon$

  *Output:* Eigenvalues $lambda_1 >= ... >= lambda_p$, eigenvectors $bold(V)$

  1. *Power Method* (for largest eigenvalue)
     - Initialize: $bold(v)^((0)) =$ random unit vector
     - *repeat*
       - $bold(w) = bold(A) bold(v)^((k))$ (matrix-vector multiply)
       - $lambda^((k+1)) = bold(v)^((k)top) bold(w)$ (Rayleigh quotient)
       - $bold(v)^((k+1)) = bold(w) / ||bold(w)||$ (normalize)
     - *until* $|lambda^((k+1)) - lambda^((k))| < epsilon$

  2. *QR Algorithm* (for all eigenvalues)
     - $bold(A)^((0)) = bold(A)$
     - *for* $k = 0, 1, 2, ...$ *do*
       - QR decomposition: $bold(A)^((k)) = bold(Q)^((k)) bold(R)^((k))$
       - Update: $bold(A)^((k+1)) = bold(R)^((k)) bold(Q)^((k))$
     - *until* off-diagonal elements $< epsilon$
     - Eigenvalues = diagonal of $bold(A)^((k))$

  3. *Practical Implementation* (for Factor Analysis)
     - Use LAPACK/BLAS routines (DSYEV, SSYEV)
     - *if* only need largest $k$ eigenvalues *then* use Arnoldi iteration
     - *Computational complexity:* $O(p^3)$ for full decomposition
]

#section-slide[Statistical Foundations]

#slide(title: [Multivariate Normal Distribution])[
  *Definition:* A random vector $bold(X) in RR^p$ follows a multivariate normal distribution:
  $bold(X) tilde N_p(bold(mu), bold(Sigma))$

  *Probability Density Function:*
  $f(bold(x)) = frac(1, (2pi)^(p/2) |bold(Sigma)|^(1/2)) exp(-frac(1, 2)(bold(x) - bold(mu))^top bold(Sigma)^(-1) (bold(x) - bold(mu)))$

  *Key Properties:*
  - Mean vector: $E[bold(X)] = bold(mu)$
  - Covariance matrix: $"Cov"(bold(X)) = bold(Sigma)$
  - Linear combinations are also normal: $bold(a)^top bold(X) tilde N(bold(a)^top bold(mu), bold(a)^top bold(Sigma) bold(a))$
  - Marginal distributions are normal
  - Conditional distributions are normal

  *Importance for Factor Analysis:* ML estimation assumes multivariate normality
]

#slide(title: [Sample Statistics and Estimation])[
  *Sample Mean Vector:*
  $overline(bold(x)) = frac(1, n) sum_(i=1)^n bold(x)_i$

  *Pointwise Form:*
  $overline(x)_j = frac(1, n) sum_(i=1)^n x_(i j)$

  *Sample Covariance Matrix:*
  $bold(S) = frac(1, n-1) sum_(i=1)^n (bold(x)_i - overline(bold(x)))(bold(x)_i - overline(bold(x)))^top$

  *Pointwise Form:*
  $s_(j k) = frac(1, n-1) sum_(i=1)^n (x_(i j) - overline(x)_j)(x_(i k) - overline(x)_k)$

  *Sample Correlation Matrix:*
  $bold(R) = bold(D)^(-1/2) bold(S) bold(D)^(-1/2)$ where $bold(D) = "diag"(s_1^2, s_2^2, ..., s_p^2)$

  *Pointwise Form:*
  $r_(j k) = frac(s_(j k), sqrt(s_(j j) s_(k k)))$

  *Central Limit Theorem for Multivariate Case:*
  $sqrt(n)(overline(bold(x)) - bold(mu)) arrow.r N_p(bold(0), bold(Sigma))$ as $n arrow infinity$

  *Wishart Distribution:*
  $(n-1)bold(S) tilde W_p(n-1, bold(Sigma))$ when $bold(x)_i tilde N_p(bold(mu), bold(Sigma))$
]

#slide(title: [Maximum Likelihood Estimation Principles])[
  *Likelihood Function:* For sample $bold(x)_1, ..., bold(x)_n$:
  $L(bold(theta)) = product_(i=1)^n f(bold(x)_i; bold(theta))$

  *Log-Likelihood:*
  $ell(bold(theta)) = ln L(bold(theta)) = sum_(i=1)^n ln f(bold(x)_i; bold(theta))$

  *MLE Principle:* Find $hat(bold(theta))$ that maximizes $ell(bold(theta))$:
  $hat(bold(theta)) = arg max_(bold(theta)) ell(bold(theta))$

  *Profound Significance of Maximum Likelihood in Factor Analysis:*
  - *Philosophical Foundation*: Seeks parameter values that make the observed data *most probable*
  - *Statistical Optimality*: Under regularity conditions, MLE provides *asymptotically efficient* estimates
  - *Factor Analysis Context*: Simultaneously estimates factor loadings ($bold(Lambda)$) and unique variances ($bold(Psi)$) that best explain observed covariances
  - *Model Comparison*: Likelihood values enable rigorous statistical testing of competing factor structures
  - *Uncertainty Quantification*: Provides standard errors and confidence intervals for all parameters
  - *Practical Advantage*: Handles complex constraints (e.g., non-negative uniquenesses) through iterative optimization

  *For Multivariate Normal Distribution:*
  - $hat(bold(mu)) = overline(bold(x))$
  - $hat(bold(Sigma)) = frac(1, n) sum_(i=1)^n (bold(x)_i - overline(bold(x)))(bold(x)_i - overline(bold(x)))^top$

  *Asymptotic Properties:*
  - Consistency: $hat(bold(theta)) arrow.r bold(theta)$ as $n arrow infinity$
  - Asymptotic normality: $sqrt(n)(hat(bold(theta)) - bold(theta)) arrow.r N(bold(0), bold(I)^(-1)(bold(theta)))$
]

#slide(title: [Hypothesis Testing Framework])[
  *Likelihood Ratio Test:*
  For nested models $H_0: bold(theta) in bold(Theta)_0$ vs $H_1: bold(theta) in bold(Theta)_1$:
  $Lambda = frac(max_(bold(theta) in bold(Theta)_0) L(bold(theta)), max_(bold(theta) in bold(Theta)_1) L(bold(theta)))$

  *Test Statistic:*
  $-2 ln Lambda arrow.r chi^2_"df"$ under $H_0$ (Wilks' theorem)
  where df = $"dim"(bold(Theta)_1) - "dim"(bold(Theta)_0)$

  *Model Fit Indices:*
  - Akaike Information Criterion: $"AIC" = -2 ell(hat(bold(theta))) + 2k$
  - Bayesian Information Criterion: $"BIC" = -2 ell(hat(bold(theta))) + k ln(n)$
  - Root Mean Square Error of Approximation: $"RMSEA" = sqrt(max(0, frac(chi^2 - "df", ("df")(n-1))))$

  *Applications in Factor Analysis:* Testing number of factors, model fit assessment
]

#slide(title: [Correlation and Dependence Concepts])[
  *Pearson Correlation:*
  $rho_(i j) = frac("Cov"(X_i, X_j), sqrt("Var"(X_i) "Var"(X_j)))$, $rho_(i j) in [-1, 1]$

  *Partial Correlation:* Correlation between $X_i$ and $X_j$ controlling for other variables
  $rho_(i j | "rest") = frac(-sigma^(i j), sqrt(sigma^(i i) sigma^(j j)))$ where $sigma^(i j)$ are elements of $bold(Sigma)^(-1)$

  *Multiple Correlation:* Correlation between $X_i$ and linear combination of other variables
  $R_i^2 = 1 - frac(1, sigma^(i i) sigma_(i i))$ (proportion of variance explained)

  *Key Insight:* In factor analysis, high correlations among observed variables suggest underlying common factors

  *Kaiser-Meyer-Olkin (KMO) Measure:*
  $"KMO" = frac(sum_(i != j) r_(i j)^2, sum_(i != j) r_(i j)^2 + sum_(i != j) a_(i j)^2)$
  where $a_(i j)$ are anti-image correlations

  *Profound Significance of KMO:*
  - *Conceptual Meaning*: Measures the proportion of variance among variables that might be *common variance*
  - *Statistical Logic*: Compares *observed correlations* against *partial correlations* controlling for all other variables
  - *Practical Interpretation*: High KMO (> 0.8) indicates variables share substantial common variance, making factor analysis appropriate
  - *Quality Control*: Low KMO (< 0.6) suggests variables are too independent for meaningful factor extraction
  - *Diagnostic Power*: Identifies when factor analysis will likely fail due to insufficient shared variance
  - *Research Validity*: Ensures factor solution represents genuine underlying constructs, not statistical artifacts
]

#slide(title: [Dimensionality and Degrees of Freedom])[
  *Parameter Counting in Factor Models:*
  - Observed covariance matrix: $p(p+1)/2$ unique elements
  - $k$-factor model parameters: $k p + p$ (loadings + uniquenesses)
  - Degrees of freedom: $"df" = p(p+1)/2 - (k p + p - k)$

  *Model Identification Requirements:*
  - Necessary: $"df" >= 0$
  - Sufficient: Additional constraints (factor scaling, rotation restrictions)

  *Saturation Point:* Maximum number of identifiable factors:
  $k_"max" = frac(2p + 1 - sqrt((2p+1)^2 - 8p), 2)$

  *Practical Rule:* For $p$ variables, typically extract $k <= p/3$ factors

  *Statistical Power Considerations:*
  - Sample size requirements: $n >= 100$ minimum, preferably $n >= 200$
  - Subject-to-variable ratio: At least 5:1, preferably 10:1 or higher
]
