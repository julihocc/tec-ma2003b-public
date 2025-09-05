// Complete Factor Analysis Presentation - Full 419-slide Content from LaTeX
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

== Introduction to Multivariate Analysis

#slide(title: [Multivariate Analysis Overview])[
  - *Multivariate Analysis*: Statistical methods for analyzing multiple variables simultaneously
  - *Key Challenge*: Understanding relationships among many correlated variables
  - *Two Main Approaches*:
    - _Principal Component Analysis (PCA)_: Dimensionality reduction technique
    - _Factor Analysis_: Latent variable modeling technique
  - *This Course*: We'll explore both methods using the same datasets for direct comparison
]

#slide(title: [Course Structure: Pedagogical Approach])[
  *Interleaved Learning Structure:*
  1. PCA Theory → Example 1 PCA → FA Theory → Example 1 FA → Comparison
  2. Example 2 PCA → Example 2 FA → Comparison
  3. Example 3 PCA → Example 3 FA → Comparison  
  4. Example 4 PCA → Example 4 FA → Comparison
  5. Overall Guidelines and Best Practices

  *Benefits*: Immediate application and comparison reinforces understanding
]

== Principal Component Analysis Theory

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

// ============================================================================
// PART II: EXAMPLE 1 - EDUCATIONAL ASSESSMENT
// ============================================================================

#part-slide[Part II: Example 1 - Educational Assessment]

== Example 1A: Educational Assessment PCA

== Example 1A: Educational Assessment PCA

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

#slide(title: [PCA Results: Factor Recovery])[
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

#slide(title: [PCA Interpretation: Method Validation])[
  *Method Validation Results:*
  - _Factor Recovery_: Meaningful variables show loading strength ~0.45-0.50
  - _Noise Separation_: Random variables show much weaker loadings (< 0.33)
  - _Structure Detection_: Clear eigenvalue drop separates signal from noise
  - *Conclusion*: PCA successfully recovers the underlying factor structure
]

== Factor Analysis Theory

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

#slide(title: [Factor Analysis vs PCA: Key Differences])[
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

== Example 1B: Educational Assessment Factor Analysis

#slide(title: [Educational Assessment: Factor Analysis])[
  *Reanalyzing our synthetic student data with Factor Analysis*
  - *Same Dataset*: 100 students, 6 variables (MathTest, VerbalTest, SocialSkills, Leadership, RandomVar1, RandomVar2)
  - *Known Structure*: Intelligence factor + Personality factor + noise
  - *FA Advantage*: Should better identify the true 2-factor structure
  - *Comparison Goal*: See how FA handles measurement error vs PCA
]

#slide(title: [FA Results: Expected Factor Structure])[
  *Factor Analysis Findings:*
  - *Factor 1*: Intelligence (Math and Verbal tests)
    - High loadings on cognitive measures
    - Low loadings on social measures and noise variables
  - *Factor 2*: Personality (Social skills and Leadership)
    - High loadings on interpersonal measures
    - Low loadings on cognitive measures and noise variables
  - *Unique Variances*: Captures measurement error in each variable
]

#slide(title: [FA Advantages: Cleaner Structure])[
  *Factor Analysis Benefits Over PCA:*
  - _Cleaner factor interpretation_: Each factor loads primarily on theoretically related variables
  - _Measurement error modeling_: Separates true score variance from error variance
  - _Factor rotation available_: Can improve interpretability further
  - _Better theory testing_: Explicitly models hypothesized latent constructs
]

== Example 1: PCA vs FA Comparison

#slide(title: [Educational Assessment: Method Comparison])[
  #align(center)[
    #table(
      columns: (1fr, 1fr, 1fr),
      [*Aspect*], [*PCA Results*], [*Factor Analysis Results*],
      [Components/Factors], [6 components], [2 meaningful factors],
      [Variance Explained], [67% by first 2 PC], [85% of common variance],
      [Structure Clarity], [General + mixed factors], [Clean Intelligence + Personality],
      [Noise Handling], [Noise components identified], [Noise in unique variances],
      [Interpretability], [Good but mixed loadings], [Excellent factor separation]
    )
  ]
]

#slide(title: [Educational Assessment: When to Use Each Method])[
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

== Example 2A: European Stock Markets PCA

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

#slide(title: [PCA Results: Market Integration])[
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

#slide(title: [PCA Interpretation: Systematic Risk])[
  *PC1 as Systematic Risk:*
  - Captures _systematic risk_ — movements common to all markets
  - Driven by: EU-wide economic conditions, global financial sentiment, central bank policies
  - High loadings on all indices → European markets are highly integrated
  - *Implication*: Limited diversification benefit from spreading across European markets alone
]

== Example 2B: European Stock Markets Factor Analysis

#slide(title: [European Stock Markets: Factor Analysis])[
  *Applying Factor Analysis to financial market data:*
  - *Same Dataset*: 4 European indices with daily returns
  - *FA Perspective*: Model latent market factors driving stock correlations
  - *Expected Factors*: European market factor, country-specific factors
  - *Comparison Goal*: See how FA models market structure vs PCA
]

#slide(title: [FA Results: Market Factor Structure])[
  *Factor Analysis Findings:*
  - *Factor 1*: European Market Factor
    - High loadings on all four indices (0.85-0.95)
    - Explains ~90% of common variance among markets
    - Represents systematic European market movements
  - *Unique Variances*: Country-specific market movements
    - Captures idiosyncratic national economic effects
    - Brexit effects (FTSE), German industrial cycles (DAX), etc.
]

#slide(title: [FA Advantages: Market Modeling])[
  *Factor Analysis Benefits for Finance:*
  - _Risk decomposition_: Separates systematic from idiosyncratic risk
  - _Portfolio construction_: Clear factor exposures for risk management
  - _Stress testing_: Model extreme factor movements separately
  - _Performance attribution_: Distinguish market timing from stock selection
]

== Example 2: PCA vs FA Comparison

#slide(title: [European Markets: Method Comparison])[
  #align(center)[
    #table(
      columns: (1fr, 1fr, 1fr),
      [*Aspect*], [*PCA Results*], [*Factor Analysis Results*],
      [Components/Factors], [1 dominant component], [1 market factor + unique variances],
      [Variance Explained], [97% by PC1], [90% of common variance],
      [Market Integration], [High correlation evident], [Systematic vs idiosyncratic risk],
      [Risk Management], [Single risk dimension], [Factor + unique risk components],
      [Portfolio Application], [Limited diversification], [Clear risk decomposition]
    )
  ]
]

#slide(title: [European Markets: When to Use Each Method])[
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

#slide(title: [Visualization: Scree Plot Analysis])[
  The scree plot shows a dramatic _"cliff"_ pattern:
  - Sharp drop from PC1 ($lambda approx 3.9$) to PC2 ($lambda approx 0.09$)
  - Clear "elbow" indicates one dominant factor
  - Remaining components are essentially flat (noise floor)
]

#slide(title: [Component Selection Decision])[
  *Decision Rules Applied:*
  - Kaiser criterion: Retain PC1 only ($lambda > 1$)
  - Variance threshold: PC1 alone exceeds any reasonable cutoff (80%, 90%, 95%)
  - Practical conclusion: European markets can be summarized by a single factor
]

#slide(title: [Biplot: Markets and Time Periods])[
  The biplot reveals the factor structure:
  - *Variable arrows* (red): Show market loadings on PC1-PC2
    - All arrows point in similar direction → positive correlation
    - Arrow length reflects contribution to variance
    - Angle between arrows shows correlation strength
  - *Observation points*: Individual trading days in PC space
    - Horizontal spread (PC1): Common market movements
    - Vertical spread (PC2): Minor market-specific deviations
    - Outliers may represent crisis periods or major events
]

#slide(title: [Practical Applications: Risk Management])[
  *Risk Management:*
  - Use PC1 scores as a single _European market risk factor_
  - Portfolio $beta$ to PC1 determines systematic risk exposure
  - Stress testing: model extreme PC1 movements
]

#slide(title: [Practical Applications: Portfolio Construction])[
  *Portfolio Construction:*
  - Market-neutral strategies require offsetting PC1 exposure
  - Alpha generation focuses on PC2-PC4 (idiosyncratic components)
  - Diversification requires assets uncorrelated with European factor
]

#slide(title: [Practical Applications: Performance Attribution])[
  *Performance Attribution:*
  - Decompose returns into market factor (PC1) + specific factors (PC2+)
  - Distinguish skill from market timing
]

#slide(title: [Code Example: Running the Analysis])[
  - *Data preparation*: `fetch_invest.py` generates synthetic European market data
  - *Main analysis*: `invest_pca.py` performs PCA with detailed financial interpretation
  - *Outputs*:
    - Eigenvalues, explained variance ratios, cumulative variance
    - `invest_scree.png`: Scree plot for component selection
    - `invest_biplot.png`: Biplot of markets and time periods
  - *Usage*: `cd code/invest_example && python invest_pca.py`
  - *Factor Analysis*: `invest_fa.py` analyzes European market factors

  #v(6pt)
  The script includes detailed py-percent comments for interactive exploration and financial interpretation of all results.
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

#slide(title: [Dataset: Physical Context])[
  *Physical Context:*
  - Objects beyond Neptune's orbit (~30 AU) in the outer solar system
  - Different units require standardization for meaningful PCA
  - Orbital correlations reflect gravitational interactions and formation history
]

#slide(title: [Dynamical Populations in the Kuiper Belt])[
  Three main populations with distinct orbital signatures:
  - *Classical Kuiper Belt* (60%): Low eccentricity, low inclination
    - Nearly circular orbits around 39-48 AU
    - "Cold" population — likely formed in place
  - *Scattered Disk Objects* (30%): High eccentricity, distant
    - $e > 0.3$, semi-major axis $> 50$ AU
    - Scattered outward by gravitational encounters with Neptune
  - *Resonant Objects* (10%): Locked in orbital resonances
    - 3:2 resonance at ~39.4 AU (like Pluto)
    - Captured during Neptune's outward migration
]

#slide(title: [Typical PCA Results: Orbital Excitation])[
  When running the analysis, we observe a more balanced variance distribution:
  - *PC1* (36.5% variance): Orbital excitation dimension
    - Correlates semi-major axis, eccentricity, and inclination
    - Separates dynamically "hot" (excited) from "cold" (pristine) populations
  - *PC2* (23.2% variance): Size-distance relationship
    - May reflect observational bias or physical size distribution
  - *PC3* (17.8% variance): Additional orbital structure
    - First 3 components explain ~77.5% of variance
    - More complex structure than financial markets example
]

#slide(title: [Astronomical Interpretation: Dynamical Evolution])[
  *PC1 as Dynamical Excitation:*
  - High loadings on distance (a), eccentricity (e), and inclination (i)
  - Represents gravitational "heating" of orbits over solar system history
  - Separates pristine objects from those scattered by planetary migration
]

#slide(title: [Astronomical Interpretation: Astrophysical Implications])[
  *Astrophysical Implications:*
  - _Formation models_: PC1 scores distinguish formation mechanisms
  - _Dynamical families_: Objects with similar PC scores likely share evolutionary history
  - _Size segregation_: Large objects may preferentially survive in certain orbital regions
]

#slide(title: [Scree Plot: Multiple Components Matter])[
  Unlike financial markets, the Kuiper Belt shows more distributed variance:
  - Gradual decline rather than sharp cliff — no single dominant factor
  - First eigenvalue ~1.8, others ~1.2, 0.9, 0.8 (above noise level)
  - Suggests 2-3 meaningful components for dimensional reduction
]

#slide(title: [Scree Plot: Decision Rules])[
  *Decision Rules:*
  - Kaiser criterion: Retain 2 components ($lambda > 1$)
  - 80% variance threshold: Need 3 components (77.5% with 3)
  - Physical interpretation: Multiple gravitational processes create complex structure
]

#slide(title: [Biplot: Objects in Orbital Space])[
  The biplot reveals orbital relationships:
  - *Variable arrows*: Orbital parameter loadings
    - Clustered arrows (a, e, i) show correlated excitation
    - H (brightness) may point differently — size-orbital coupling
  - *Object points*: Individual Kuiper Belt objects in PC space
    - Clustering reveals dynamical families
    - Outliers represent unusual objects (highly eccentric, large inclination)
    - Can identify candidates for detailed follow-up observations
]

#slide(title: [Scientific Applications: Population Studies])[
  *Population Studies:*
  - Classify objects into dynamical families using PC scores
  - Test formation and migration models against observed distributions
  - Identify rare populations (detached objects, extreme resonances)
]

#slide(title: [Scientific Applications: Observational Planning])[
  *Observational Planning:*
  - Target unusual objects (outliers in PC space) for detailed study
  - Optimize survey strategies based on population structure
  - Predict undiscovered populations in unsampled orbital regions
]

#slide(title: [Scientific Applications: Comparative Planetology])[
  *Comparative Planetology:*
  - Compare our solar system structure to exoplanetary debris disks
  - Understand how planetary migration shapes outer system architecture
]

#slide(title: [Code Example: Astronomical Data Analysis])[
  - *Data generation*: `fetch_kuiper.py` creates synthetic orbital database
  - *Main analysis*: `kuiper_pca.py` performs PCA with astronomical interpretation
  - *Outputs*:
    - Eigenvalues showing distributed variance structure
    - `kuiper_scree.png`: Scree plot for component selection
    - `kuiper_biplot.png`: Objects and orbital parameters in PC space
  - *Usage*: `cd code/kuiper_example && python kuiper_pca.py`
  - *Factor Analysis*: `kuiper_fa.py` applies FA to same orbital data

  #v(6pt)
  The script demonstrates PCA applied to scientific data with multiple meaningful components and physical interpretation of mathematical results.
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

#slide(title: [Healthcare Context: Quality Measurement])[
  *Clinical Significance:*
  - Metrics reflect different aspects of hospital care: safety, effectiveness, patient experience
  - Used by CMS for Hospital Compare and Value-Based Purchasing programs
  - Risk-adjusted for patient acuity and case mix differences

  #v(12pt)
  *Quality Improvement Context:*
  - Different units require standardization for meaningful comparison
  - Strong correlations expected due to organizational quality culture
  - "Halo effect": well-managed hospitals perform well across multiple domains
]

#slide(title: [Typical PCA Results: Strong Quality Factor])[
  When running the analysis, we observe strong factor concentration:
  - *PC1* (70.5% variance): Overall hospital quality dimension
    - Eigenvalue ≈ 5.6 (well above Kaiser threshold)
    - High loadings across all quality metrics
    - Represents systematic organizational excellence
  - *PC2* (8.5% variance): Efficiency vs. thoroughness trade-off
    - May separate length of stay patterns
    - Different care philosophies or patient populations
  - *PC1 dominance*: Similar to financial markets but for quality reasons
]

#slide(title: [Healthcare Interpretation: Quality Halo Effect])[
  *PC1 as Organizational Quality:*
  - Represents systematic differences in hospital management and culture
  - High-performing hospitals excel across: mortality, readmissions, infections, satisfaction
  - Reflects comprehensive quality improvement programs and leadership

  #v(12pt)
  *Clinical Implications:*
  - _System-wide improvement_: Quality is not isolated to single metrics
  - _Resource allocation_: Investment in organizational excellence pays dividends across domains
  - _Best practices_: High PC1 hospitals can serve as models for improvement
]

#slide(title: [Hospital Quality Rankings])[
  PC1 scores enable comprehensive hospital ranking:
  - *Top performers* (high PC1): Low mortality, infections, wait times + high satisfaction, nurse ratios
  - *Bottom performers* (low PC1): High mortality, readmissions + low satisfaction, poor staffing
  - *Composite quality score*: Single metric capturing 70% of quality variation

  #v(12pt)
  *Policy Applications:*
  - _Public reporting_: PC1-based hospital star ratings
  - _Value-based purchasing_: Reimbursement tied to PC1 performance
  - _Quality improvement_: Target comprehensive organizational change
]

#slide(title: [Scree Plot: Dominant Quality Factor])[
  The scree plot shows strong factor concentration similar to financial markets:
  - Sharp drop from PC1 ($lambda approx 5.6$) to PC2 ($lambda approx 0.7$)
  - Clear evidence of single dominant quality factor
  - Remaining components capture minor variations and noise

  #v(12pt)
  *Healthcare Decision Rules:*
  - Kaiser criterion: Retain PC1 only for overall quality assessment
  - 70% variance: PC1 alone exceeds most reasonable cutoffs
  - Clinical interpretation: Hospital quality is largely unidimensional
  - Practical conclusion: Focus quality improvement efforts system-wide
]

#slide(title: [Biplot: Hospitals in Quality Space])[
  The biplot reveals quality structure and hospital positioning:
  - *Variable arrows*: All point in similar direction (quality halo effect)
    - Mortality, infections, complications load negatively (lower = better)
    - Satisfaction, nurse ratios load positively (higher = better)
    - Arrow clustering confirms correlated quality dimensions
  - *Hospital points*: Individual hospitals positioned by quality profile
    - Right side: High-quality hospitals across multiple metrics
    - Left side: Hospitals needing comprehensive improvement
    - Outliers: Unique performance patterns for investigation
]

#slide(title: [Healthcare Management Applications])[
  *Quality Assessment & Benchmarking:*
  - Use PC1 scores for comprehensive hospital quality rankings
  - Identify peer groups with similar quality profiles for comparison
  - Track quality improvement over time using longitudinal PC1 trends

  #v(6pt)
  *Strategic Planning & Improvement:*
  - Target system-wide organizational excellence rather than isolated metrics
  - Study best practices from high PC1 hospitals for replication
  - Allocate resources to comprehensive quality programs with broad impact

  #v(6pt)
  *Regulatory & Policy Applications:*
  - Inform value-based purchasing and quality incentive programs
  - Support public reporting initiatives with composite quality measures
]

#slide(title: [Code Example: Healthcare Quality Analysis])[
  - *Data generation*: `fetch_hospitals.py` creates realistic hospital quality data
  - *Main analysis*: `hospitals_example.py` performs PCA with healthcare interpretation
  - *Outputs*:
    - Hospital quality rankings based on PC1 scores
    - Component loadings showing quality metric relationships
    - `hospitals_scree.png`: Scree plot showing factor concentration
    - `hospitals_biplot.png`: Hospitals and metrics in quality space
  - *Usage*: `cd code/hospitals_example && python hospitals_example.py`

  #v(6pt)
  The script demonstrates PCA applied to healthcare quality assessment with practical applications for hospital management and healthcare policy.
]

// ============================================================================
// PART II: FACTOR ANALYSIS
// ============================================================================

#part-slide[Factor Analysis]

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
      columns: (1fr, 1fr),
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

== Factor Analysis: Educational Assessment Example

#slide(title: [Educational Assessment: Factor Analysis])[
  *Reanalyzing our synthetic student data with Factor Analysis*
  - *Same Dataset*: 100 students, 6 variables (MathTest, VerbalTest, SocialSkills, Leadership, RandomVar1, RandomVar2)
  - *Known Structure*: Intelligence factor + Personality factor + noise
  - *FA Advantage*: Should better identify the true 2-factor structure
  - *Comparison Goal*: See how FA handles measurement error vs PCA
  - *Scripts*: `educational_pca.py` vs `educational_fa.py`
]

#slide(title: [Expected Factor Analysis Results])[
  *Anticipated Findings:*
  - Factor 1: Intelligence (Math, Verbal tests)
  - Factor 2: Personality (Social skills, Leadership)
  - Random variables should show low communalities
]

== Kuiper Belt Objects: Factor Analysis

#slide(title: [Kuiper Belt Objects: Factor Analysis])[
  Applying Factor Analysis to astronomical orbital dynamics data:
  - *Same Dataset*: 98 trans-Neptunian objects with 5 orbital parameters
  - *FA Approach*: Model latent dynamical factors affecting orbital elements
  - *Key Difference*: FA focuses on common dynamical processes vs PCA's variance maximization
  - *Expected Factors*: Dynamical excitation, size-distance relationships, resonance effects

  #v(6pt)
  Script: `kuiper_fa.py`
]

#slide(title: [Kuiper Belt FA: Factor Assumptions])[
  *Factor Analysis Assumptions for Orbital Data:*
  - *Bartlett's Test*: Tests correlation structure suitability
  - *KMO Test*: Measures sampling adequacy for orbital parameters
  - *Individual MSA*: Each orbital parameter's factor analysis suitability
  - *Result*: Most orbital parameters show acceptable to good MSA values
]

#slide(title: [Kuiper Belt FA: Factor Extraction Results])[
  *Principal Axis Factoring Results:*
  - *Kaiser Criterion*: Suggests 3 factors (eigenvalues > 1.0)
  - *Factor 1*: Orbital excitation (high loadings on a, e, i)
    - Represents dynamical "heating" of orbits over solar system history
  - *Factor 2*: Object designation effects (data artifact)
  - *Factor 3*: Size factor (high loading on absolute magnitude H)
    - Separates size-related observational effects
]

#slide(title: [Kuiper Belt FA: Astronomical Interpretation])[
  *Astrophysical Meaning of Factors:*
  - *Dynamical Excitation Factor*: Captures gravitational scattering effects
    - Objects with high Factor 1 scores: scattered by planetary migration
    - Objects with low Factor 1 scores: pristine, formed in-place
  - *Size Factor*: Reflects observational selection and physical processes
    - Large objects more easily detected at great distances
    - May indicate size-dependent survival mechanisms
]

#slide(title: [Kuiper Belt FA: Model Validation])[
  *Factor Model Quality Assessment:*
  - *RMSR*: Root mean square residuals indicate model fit quality
  - *Residual Correlations*: Proportion of large residual correlations
  - *Factor Determinacy*: Reliability of factor score estimates
  - *Communalities*: How much variance each orbital parameter shares with factors

  #v(6pt)
  *Result*: 3-factor model explains 84% of common variance in orbital parameters
]

// ============================================================================
// PART III: COMPARISON AND APPLICATIONS
// ============================================================================

#part-slide[Comparison and Applications]

== PCA vs Factor Analysis: Direct Comparison

#slide(title: [Method Comparison Overview])[
  *We will compare PCA and Factor Analysis results for:*
  - *Educational Assessment*: Known 2-factor structure with noise
  - *European Stock Markets*: High correlation, potential single market factor
  - *Kuiper Belt Objects*: Natural population structure in astronomy
  - *Hospital Quality*: Healthcare performance measurement
]

#slide(title: [Method Comparison Criteria])[
  *Evaluation Framework:*
  - Variance explained vs factor interpretability
  - Treatment of measurement error and unique variance
  - Practical applications and domain fit
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