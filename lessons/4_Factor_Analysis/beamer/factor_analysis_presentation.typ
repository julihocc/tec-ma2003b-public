// Complete Factor Analysis Presentation - RESTRUCTURED  
// Pedagogical approach: PCA theory → FA theory → Theory comparison → Examples with PCA → FA → Comparison pattern

// Tec de Monterrey color palette
#let tec-blue = rgb("#003f7f")      // Tec de Monterrey signature blue
#let tec-light-blue = rgb("#0066cc") // Lighter blue for accents

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

#slide(title: [Practical tips and pitfalls])[
  - Always check variable scales; standardize when necessary.
  - PCA is sensitive to outliers — inspect data and consider robust alternatives if needed.
  - Interpret components via loadings (eigenvectors) and by examining which variables contribute strongly to each component.
  - Rotation is not standard in PCA (rotation reassigns variance) — if interpretability is a priority, consider Factor Analysis with rotation.
  - When reporting, include: eigenvalues table, proportion of variance, cumulative variance, scree plot, and a table of loadings (component matrix).
]

#section-slide[Factor Analysis Theory]

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
  - *Core Equation*: $X_i = lambda_(i 1) F_1 + lambda_(i 2) F_2 + ... + lambda_(i k) F_k + U_i$
    - $X_i$ = observed variable, $F_j$ = common factors, $U_i$ = unique factor
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
      [Descriptive technique], [Statistical model with assumptions]
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
    [PC6], [0.289], [4.8%], [100.0%]
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
    [RandomVar2], [-0.283], [-0.032], [0.502]
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
    [Total], [], [88.4%]
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
    [RandomVar2], [-0.089], [0.198], [0.047]
  )]
  
  - *Factor 1*: Intelligence factor (Math/Verbal loadings > 0.82)
  - *Factor 2*: Personality factor (Social/Leadership loadings > 0.82)
  - *Clean structure*: Cross-loadings < 0.15 for meaningful variables
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
    [RandomVar2], [-0.283], [-0.032], [-0.089], [0.198]
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
    [PC4], [0.004], [0.1%], [100.0%]
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
    [FTSE (UK)], [0.499], [-0.625]
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
    [FTSE (UK)], [0.985], [0.970]
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
    [Application], [Data reduction], [Risk modeling]
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
    [PC5], [0.299], [5.9%], [100.0%]
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
    [H (magnitude)], [-0.157], [0.905], [-0.393]
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
    [designation], [-0.049], [0.940], [-0.084], [0.892]
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
    [H (magnitude)], [-0.157], [-0.048], [PCA mixed, FA separates as Factor 3]
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
    [PC4-PC8], [all below 0.50], [15.1%], [100.0%]
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
    [AvgLengthStay (↓)], [-0.302], [0.723], [0.226]
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
    [AvgLengthStay], [-0.717], [0.515]
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
    [ReadmissionRate], [-0.352], [-0.823], [Strong negative correlation]
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
      [Kuiper Belt Objects], [Astronomy], [Population classification], [Physical process modeling], [FA for theory testing],
      [Hospital Quality], [Healthcare], [Quality rankings], [Quality dimensions], [PCA for rankings, FA for policy]
    )
  ]
]

#section-slide[Guidelines for Method Selection]

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
