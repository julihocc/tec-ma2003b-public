// Complete Factor Analysis Presentation in Typst
#set page(
  width: 16cm,
  height: 9cm,
  margin: (x: 1.5cm, y: 1cm),
  numbering: "1"
)

#set document(
  title: "Factor Analysis",
  author: "Dr. Juliho Castillo"
)

#set text(
  font: "Liberation Sans",
  size: 12pt,
  lang: "es"
)
#set math.equation(numbering: none)

// Custom slide function
#let slide(title: none, content) = {
  pagebreak(weak: true)
  if title != none [
    #set text(size: 18pt, weight: "bold")
    #title
    #v(0.8cm)
  ]
  content
}

// Section slide function
#let section-slide(title) = {
  pagebreak(weak: true)
  set text(size: 20pt, weight: "bold")
  align(center + horizon)[#title]
}

// Title slide
#align(center)[
  #v(2cm)
  #text(size: 24pt, weight: "bold")[Factor Analysis]
  #v(0.5cm)
  #text(size: 16pt)[Dr. Juliho Castillo]
  #v(0.3cm)
  #text(size: 14pt)[Tecnológico de Monterrey]
  #v(0.3cm)
  #text(size: 12pt)[#datetime.today().display()]
]

// Table of contents
#slide(title: [Contenido])[
  = Principal Component Analysis
    - Introduction to Multivariate Analysis
    - Principal Component Analysis
    - Educational Assessment: Synthetic PCA Example
    - Investment allocation example
    - Kuiper Belt Objects: Astronomical PCA
    - Hospital Health Outcomes: Healthcare PCA

  = Factor Analysis
    - Introduction to Factor Analysis
    - Factor Analysis: Educational Assessment Example
    - Kuiper Belt Objects: Factor Analysis

  = Comparison and Applications
    - PCA vs Factor Analysis: Direct Comparison
    - Guidelines for Method Selection
]

#section-slide[PART I: Principal Component Analysis]

== Introduction to Multivariate Analysis

#slide(title: [Multivariate Analysis Overview])[
  - *Multivariate Analysis*: Statistical methods for analyzing multiple variables simultaneously
  - *Key Challenge*: Understanding relationships among many correlated variables
  - *Two Main Approaches*:
    - _Principal Component Analysis (PCA)_: Dimensionality reduction technique
    - _Factor Analysis_: Latent variable modeling technique
  - *This Course*: We'll explore both methods using the same datasets for direct comparison
]

#slide(title: [Course Structure Overview])[
  *Part I: Principal Component Analysis*
  - PCA theory and mathematical foundation
  - Four comprehensive examples across different domains
]

#slide(title: [Course Structure: Factor Analysis])[
  *Part II: Factor Analysis*
  - Factor Analysis theory and modeling approach
  - Same datasets analyzed with Factor Analysis
]

#slide(title: [Course Structure: Comparison])[
  *Part III: Comparison and Applications*
  - Side-by-side comparison of results
  - Guidelines for choosing the appropriate method
]

== Principal Component Analysis

#slide(title: [Refresher: What is PCA?])[
  - Principal Component Analysis (PCA) is a linear method for *dimension reduction*.
  - It finds orthogonal directions (principal components) that capture the largest possible variance in the data.
  - PCA produces new variables (components) that are linear combinations of the original observed variables.
  - Use cases: visualization, noise reduction, pre-processing before supervised learning, and exploratory data analysis.
]

#slide(title: [Mathematical formulation])[
  Let $bold(x) in RR^p$ be a random vector with mean $mu$ and covariance matrix $Sigma$. After centering the data $(bold(x)-mu)$:
  - Find eigenvalues $lambda_1 >= lambda_2 >= ... >= lambda_p$ and orthonormal eigenvectors $bold(v)_1, ..., bold(v)_p$ of $Sigma$: $Sigma bold(v)_j = lambda_j bold(v)_j$.
  - The $j$-th principal component is $z_j = bold(v)_j^top (bold(x)-mu)$.
  - Variance explained by component $j$ is $"Var"(z_j) = lambda_j$. The proportion explained is $lambda_j / sum_(k=1)^p lambda_k$.
]

#slide(title: [Computation steps (practical)])[
  + Standardize variables if they are on different scales (use correlation matrix) or center only if scales are comparable (use covariance matrix).
  + Compute covariance (or correlation) matrix $S$ from the data.
  + Compute eigen decomposition $S = V Lambda V^top$.
  + Form principal component scores: $Z = X_c V$ (where $X_c$ is centered data and columns of $V$ are eigenvectors).
  + Inspect eigenvalues, cumulative variance, and scree plot to decide how many components to keep.
]

#slide(title: [Deciding how many components to retain])[
  Common heuristics and formal approaches:
  - Kaiser criterion: keep components with eigenvalue $> 1$ (applies when using correlation matrix).
  - Cumulative variance: keep the smallest number of components that explain a target (e.g., 70--90%) of total variance.
  - Scree plot: look for the "elbow" where additional components contribute little incremental variance.
  - Parallel analysis: compare empirical eigenvalues to those obtained from random data — keep components with larger eigenvalues than random.
]

#slide(title: [PCA vs Factor Analysis (reminder)])[
  - PCA: descriptive linear combinations that maximize variance; components are exact linear functions of observed variables and need not have a causal or measurement model interpretation.
  - Factor Analysis: a statistical model that explicitly decomposes observed variance into common (shared) variance explained by latent factors and unique variance (errors).
  - Practical rule: use PCA for dimension reduction and data compression; use Factor Analysis when your goal is to model latent constructs and separate common from unique variance.
]

#slide(title: [Practical tips and pitfalls])[
  - Always check variable scales; standardize when necessary.
  - PCA is sensitive to outliers — inspect data and consider robust alternatives if needed.
  - Interpret components via loadings (eigenvectors) and by examining which variables contribute strongly to each component.
  - Rotation is not standard in PCA (rotation reassigns variance) — if interpretability is a priority, consider Factor Analysis with rotation.
  - When reporting, include: eigenvalues table, proportion of variance, cumulative variance, scree plot, and a table of loadings (component matrix).
]

== Educational Assessment: Synthetic PCA Example

#slide(title: [Educational Assessment: Synthetic PCA Example])[
  This section demonstrates PCA using controlled synthetic data with known factor structure to validate the method and teach key concepts.
  - *Dataset*: Student assessment data with 6 variables (100 students)
  - *Research Question*: Can PCA recover the underlying ability factors? How does it separate meaningful structure from noise?
  - *Method*: Standardized PCA on synthetic data with known latent factors

  #v(6pt)
  Scripts: `educational_pca.py` (PCA) | `educational_fa.py` (FA comparison)
]

#slide(title: [Dataset: Student Assessment Variables])[
  Six variables representing different aspects of student ability:
  - *MathTest*: Mathematics assessment score
  - *VerbalTest*: Verbal reasoning assessment score
  - *SocialSkills*: Social competency rating
  - *Leadership*: Leadership ability rating
  - *RandomVar1, RandomVar2*: Pure noise controls
]

#slide(title: [Known Factor Structure])[
  *Ground Truth for Validation:*
  - _Intelligence Factor_: Affects MathTest (0.85 loading) and VerbalTest (0.80 loading)
  - _Personality Factor_: Affects SocialSkills (0.85 loading) and Leadership (0.80 loading)
  - Measurement error added to all meaningful variables (0.2-0.25 noise levels)
]

#slide(title: [Educational Context: Pedagogical Value])[
  *Why This Example Works for Learning:*
  - Ground truth known → can validate PCA's ability to recover factors
  - Realistic psychological assessment scenario that students understand
  - Clear separation between meaningful variables and pure noise
]

#slide(title: [Educational Context: Learning Outcomes])[
  *Key Concepts Students Will Master:*
  - Understand how PCA handles correlated variables driven by latent factors
  - See how noise components are separated from meaningful structure
  - Learn to interpret component loadings in context of known relationships
  - Practice using scree plots and eigenvalue criteria for component selection
]

#slide(title: [Typical PCA Results: Factor Recovery])[
  When running the analysis, we observe meaningful factor separation:
  - *PC1* (36.7% variance): General ability factor
    - Eigenvalue ≈ 2.2 (well above Kaiser threshold)
    - Captures common variance across all meaningful measures
    - Reflects "halo effect" common in ability assessments
  - *PC2* (30.8% variance): Specific ability dimensions
    - May separate cognitive from social abilities
    - Shows how PCA can capture multiple meaningful factors
  - *PC3-PC4* (30.2% variance): Additional structure and measurement error
  - *PC5-PC6* (2.3% variance): Pure noise components
    - Very low eigenvalues (< 0.15) clearly identify noise floor
]

== Investment allocation example

#slide(title: [European Stock Markets: PCA Analysis])[
  This section demonstrates PCA applied to financial markets using synthetic European stock market data.
  - *Dataset*: 4 major European indices (DAX, SMI, CAC, FTSE) over 1,860 trading days.
  - *Research Question*: How integrated are European financial markets? Can we identify common market factors?
  - *Method*: Standardized PCA on correlation matrix of daily returns.

  #v(6pt)
  Scripts: `invest_pca.py` (PCA) | `invest_fa.py` (Factor Analysis)
]

#slide(title: [Dataset: European Market Indices])[
  - *DAX (Germany)*: Frankfurt Stock Exchange — largest European economy
  - *SMI (Switzerland)*: Swiss Market Index — major financial center
  - *CAC (France)*: Paris Stock Exchange — core eurozone market
  - *FTSE (UK)*: London Stock Exchange — major international hub
]

#slide(title: [Typical PCA Results: Market Integration])[
  When running the analysis, we observe:
  - *PC1*: Explains ~97% of total variance
    - Eigenvalue ≈ 3.9 (well above Kaiser threshold of 1.0)
    - Represents a _common European market factor_
    - All markets load positively — they move together
  - *PC2-PC4*: Explain only ~3% combined variance
    - Capture market-specific idiosyncrasies
    - Currency effects, country-specific political events
    - Largely noise for portfolio construction
]

#slide(title: [Financial Interpretation: Market Factor])[
  *PC1 as Systematic Risk:*
  - Captures _systematic risk_ — movements common to all markets
  - Driven by: EU-wide economic conditions, global financial sentiment, central bank policies
  - High loadings on all indices → European markets are highly integrated
]

#slide(title: [Portfolio Management Implications])[
  *Key Insights for Investors:*
  - _Limited diversification benefit_ from spreading across European markets alone
  - Most portfolio variance comes from exposure to the common factor
  - Geographic diversification requires markets with different factor exposures
]

== Kuiper Belt Objects: Astronomical PCA

#slide(title: [Kuiper Belt Objects: PCA Analysis])[
  This section demonstrates PCA applied to astronomical data from the outer solar system.
  - *Dataset*: Orbital parameters of 98 trans-Neptunian objects (TNOs) and Kuiper Belt objects
  - *Research Question*: What are the main modes of orbital variation? Can we identify distinct dynamical populations?
  - *Method*: Standardized PCA on 5 orbital elements with different physical units

  #v(6pt)
  Scripts: `kuiper_pca.py` (PCA) | `kuiper_fa.py` (Factor Analysis)
]

#slide(title: [Dataset: Orbital Parameters])[
  Five key orbital elements describe each object's motion:
  - *a* (AU): Semi-major axis — average distance from Sun (30-150 AU)
  - *e*: Eccentricity — orbital shape (0=circle, 1=parabola)
  - *i* (degrees): Inclination — tilt relative to solar system plane
  - *H* (magnitude): Absolute magnitude — brightness/size indicator
]

== Hospital Health Outcomes: Healthcare PCA

#slide(title: [Hospital Health Outcomes: PCA Analysis])[
  This section demonstrates PCA applied to healthcare quality data from US hospitals.
  - *Dataset*: Health outcome metrics for 50 US hospitals across 8 performance indicators
  - *Research Question*: What are the main dimensions of hospital quality? Can we rank hospital performance?
  - *Method*: Standardized PCA on healthcare metrics with different units and scales

  #v(6pt)
  Script: `lessons/4_Factor_Analysis/code/hospitals_example/hospitals_example.py`
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

#section-slide[PART II: Factor Analysis]

== Introduction to Factor Analysis

#slide(title: [What is Factor Analysis?])[
  - A statistical method for modeling relationships among *observed variables* using *latent factors*.
  - It uses a smaller number of _unobserved variables_, known as *common factors*.
  - *Key Distinction from PCA*: Explicitly models measurement error and unique variance
  - Often used to discover and validate underlying theoretical constructs
]

#slide(title: [Factor Analysis Model])[
  - *Common Factors*: Latent variables that influence multiple observed variables
  - *Factor Loadings*: Relationships between observed variables and common factors
  - *Unique Factors*: Variable-specific variance not explained by common factors
  - *Core Assumption*: $X_i = lambda_(i 1) F_1 + lambda_(i 2) F_2 + ... + lambda_(i k) F_k + U_i$
    - $X_i$ = observed variable, $F_j$ = common factors, $U_i$ = unique factor
]

#slide(title: [Factor Analysis vs. PCA: Key Differences])[
  #align(center)[
    #table(
      columns: 2,
      stroke: 0.5pt,
      [*Principal Component Analysis*], [*Factor Analysis*],
      [Dimensionality reduction], [Latent variable modeling],
      [Components are linear combinations of all variables], [Factors are hypothetical constructs],
      [Explains total variance], [Explains common variance only],
      [No measurement error model], [Explicitly models unique variance],
      [Descriptive technique], [Statistical model with assumptions]
    )
  ]

  #v(12pt)
  *Next*: We'll analyze the same four datasets with Factor Analysis to see these differences in practice!
]

#section-slide[PART III: Comparison and Applications]

== PCA vs Factor Analysis: Direct Comparison

#slide(title: [Method Comparison Overview])[
  *We will compare PCA and Factor Analysis results for:*
  - *Educational Assessment*: Known 2-factor structure with noise
  - *European Stock Markets*: High correlation, potential single market factor
  - *Kuiper Belt Objects*: Natural population structure in astronomy
  - *Hospital Quality*: Healthcare performance measurement
]

== Guidelines for Method Selection

#slide(title: [When to Use PCA vs Factor Analysis])[
  *Use PCA when:*
  - Primary goal is dimensionality reduction
  - You want to maximize variance explained
  - Data compression or noise reduction is the objective
  - You don't have strong theoretical expectations about latent constructs
]

#slide(title: [When to Use Factor Analysis])[
  *Use Factor Analysis when:*
  - You want to model latent constructs or theoretical factors
  - Understanding measurement error and unique variance is important
  - You need factor rotation for cleaner interpretation
  - Confirmatory analysis of hypothesized factor structures
]

#slide(title: [Practical Recommendations])[
  - *Start with EDA*: Use PCA first to understand your data structure
  - *Theory-driven analysis*: Apply Factor Analysis when you have theoretical expectations
  - *Compare both methods*: Results convergence strengthens conclusions
  - *Consider sample size*: Factor Analysis requires larger samples
  - *Validate results*: Use cross-validation, external criteria, or confirmatory approaches
]

#slide(title: [A Word of Caution])[
  - Neither method can _prove_ a factor structure is correct
  - Multiple equally valid models may exist for the same dataset
  - Always combine statistical results with domain knowledge
]