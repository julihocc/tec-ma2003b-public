# Collaborative Business Case - Factor Analysis

## Customer Satisfaction Intelligence: TechnoServe Solutions

**Modality:** Collaborative (teams of 2-3 students)  
**Weight:** 5% of total course grade  
**Duration:** 1 week  
**Deliverables:** Jupyter Notebook + Executive Report + Presentation Video (YouTube)

---

## Problem Context

You are part of a data science consulting team tasked with helping **TechnoServe Solutions**, a technology consulting firm, transform their customer satisfaction data into actionable business intelligence.

**Business Situation:** TechnoServe has collected extensive customer satisfaction data across multiple service dimensions, but they struggle to identify the underlying factors that truly drive customer retention and revenue growth.

**Your Mission:** Apply Factor Analysis to discover the latent structure in satisfaction data, develop strategic insights, and present executive recommendations based on statistical evidence.

---

## Learning Objectives

Upon completing this business case, students will be able to:

- **Technical:** Implement and validate Factor Analysis using Python/R with rigorous statistical interpretation
- **Methodological:** Evaluate factorability, select appropriate extraction methods, and apply factor rotations
- **Analytical:** Interpret factors in business context and develop factor scores for predictive modeling
- **Professional:** Communicate complex statistical findings to non-technical executive audiences
- **Collaborative:** Work effectively in teams to solve multifaceted analytical problems

---

## Dataset and Business Context

### Customer Satisfaction Intelligence Dataset

**Source:** Customer satisfaction surveys (Q1-Q4 2024)
- **Observations:** 3,400 survey responses
- **Clients:** 850 enterprise customers
- **Variables:** 23 satisfaction dimensions (Likert scale 1-7) + 5 outcome variables
- **Temporal Context:** Longitudinal data by quarter with temporal trends

### Satisfaction Dimensions (Observed Variables)

**Technical Excellence:**
- `technical_expertise`, `problem_solving`, `innovation_solutions`, `technical_documentation`, `system_integration`

**Relationship Management:**
- `account_manager_responsive`, `executive_access`, `trust_reliability`, `long_term_partnership`, `communication_clarity`

**Project Delivery:**
- `project_management`, `timeline_adherence`, `budget_control`, `quality_deliverables`, `change_management`

**Value and Costs:**
- `cost_transparency`, `value_for_money`, `roi_demonstration`, `competitive_pricing`, `billing_accuracy`

**Support and Service:**
- `support_responsiveness`, `training_quality`, `documentation_help`

### Business Outcome Variables

- **`overall_satisfaction`** (1-7): Overall satisfaction with TechnoServe Solutions
- **`nps_score`** (0-10): Net Promoter Score (likelihood to recommend)
- **`renewal_likelihood`** (1-5): Contract renewal probability
- **`revenue_growth_pct`** (continuous): Year-over-year revenue growth
- **`referrals_generated`** (integer): Number of referrals generated per quarter

### Statistical Overview of Dataset

| Metric | Value |
|---------|-------|
| Total observations | 3,400 |
| Unique customers | 850 |
| Satisfaction variables | 23 |
| Outcome variables | 5 |
| Missing data | ~5% (MCAR) |
| Correlations > 0.3 | 48.2% of pairs |

---

## Business Case Structure

### Part 1: Factorability Assessment and Exploration (25 points)

#### 1.1 Advanced Exploratory Analysis (8 points)

**Technical Tasks:**
- Implement complete descriptive analysis with outlier identification
- Generate correlation matrix with cluster pattern visualization
- Evaluate multivariate normality assumptions using appropriate tests
- Analyze missing data patterns and implement handling strategy

**Reflection Question:** *What patterns do you observe in the correlation matrix? How do these patterns suggest the presence of underlying latent factors?*

#### 1.2 Statistical Factorability Tests (10 points)

**Required Implementation:**
- **Kaiser-Meyer-Olkin (KMO) Test:** Calculate and interpret global and per-variable KMO
- **Bartlett's Sphericity Test:** Implement and evaluate statistical significance
- **Anti-image Matrix:** Examine partial correlations and individual MSA values
- **Matrix Determinant:** Evaluate extreme multicollinearity

**Decision Criteria:**
- KMO > 0.8 (excellent), > 0.6 (acceptable)
- Bartlett: p < 0.05 (reject H₀ of identity matrix)
- Individual MSA > 0.5 per variable

**Reflection Question:** *Why is it crucial to evaluate factorability before proceeding with factor extraction? What implications would ignoring these tests have?*

#### 1.3 Preliminary Dimensionality Analysis (7 points)

**Evaluation Methods:**
- **Kaiser Criterion:** Eigenvalues > 1.0
- **Scree Plot:** Visual identification of "elbow" in eigenvalues
- **Parallel Analysis:** Comparison with eigenvalues from random data
- **Explained Variance:** Evaluation of % variance per component

**Reflection Question:** *What advantages and limitations does each method have for determining the optimal number of factors? How do you reconcile contradictory results between methods?*

---

### Part 2: Factor Extraction and Rotation (30 points)

#### 2.1 Comparative Extraction Methods (15 points)

**Required Implementation:**
- **Principal Component Analysis (PCA):** To establish baseline
- **Principal Axis Factoring (PAF):** Classic common factors method
- **Maximum Likelihood (ML):** With χ² goodness-of-fit tests

**Comparative Analysis:**
- Compare eigenvalues and % explained variance between methods
- Evaluate differences in estimated communalities
- Analyze residuals and goodness of fit
- Justify final method selection based on statistical criteria

**Reflection Question:** *When is it appropriate to use PCA vs. Factor Analysis? What fundamental assumptions differentiate these approaches and how do they affect business interpretation?*

#### 2.2 Factor Rotation Strategies (15 points)

**Rotations to Implement:**
- **Varimax (Orthogonal):** Maximization of variance in factor loadings
- **Promax (Oblique):** Allowing correlations between factors
- **Direct Oblimin:** Alternative oblique method

**Rotation Evaluation:**
- Compare simple structure interpretability
- Analyze interfactor correlations in oblique methods
- Evaluate % explained variance post-rotation
- Select optimal rotation based on theoretical and statistical criteria

**Reflection Question:** *Why might correlations between factors be theoretically justifiable in the context of customer satisfaction? What implications does this have for rotation selection?*

---

### Part 3: Interpretation and Business Application (25 points)

#### 3.1 Factor Interpretation and Labeling (12 points)

**Factor Loading Analysis:**
- Identify variables with loadings > |0.4| per factor
- Develop conceptual labels based on loading patterns
- Evaluate theoretical coherence with expected business dimensions
- Analyze variables with significant cross-loadings

**Structure Validation:**
- Compare emergent structure with initial theoretical framework
- Evaluate internal consistency using Cronbach's Alpha per factor
- Analyze communalities to identify poorly represented variables

**Reflection Question:** *How do you balance statistical parsimony with interpretative richness when labeling factors? What should be done with variables that don't clearly load on any factor?*

#### 3.2 Factor Score Calculation and Application (13 points)

**Scoring Methods:**
- **Regression Method:** Scores with optimal correlation properties  
- **Bartlett Method:** Unbiased scores with minimum variance
- Compare statistical properties between methods

**Predictive Application:**
- Use factor scores to predict outcome variables
- Implement multiple regression models: `nps_score ~ factor1 + factor2 + ...`
- Evaluate relative predictive power of each factor
- Develop impact matrix: Factor × Business Outcome

**Reflection Question:** *How do you interpret the differential predictive capacity of factors? Which factors are most critical for specific outcomes and why?*

---

### Part 4: Visualization and Strategic Communication (20 points)

#### 4.1 Advanced Analytical Visualization (12 points)

**Required Plots:**
- **Loading Plot:** Two-dimensional visualization of main factor loadings
- **Score Plot:** Customer distribution in factorial space
- **Correlation Heatmap:** Correlation matrix with hierarchical clustering
- **Factor Importance Plot:** Relative contribution by outcome variable

**Visual Quality:**
- Clear and professional labels in English
- Colors appropriate for executive audience
- Explanatory annotations for key insights
- Publication-ready design for executive report

**Reflection Question:** *What story does each visualization tell about the underlying structure of customer satisfaction? How would you use these charts to convince a skeptical CEO?*

#### 4.2 Executive Dashboard and Recommendations (8 points)

**Strategic Synthesis:**
- Identify the 3 most critical factors for customer retention
- Develop prioritization matrix: Impact × Implementation Difficulty
- Calculate potential ROI of improvements in specific factors
- Propose 6-month implementation roadmap

**Actionable Recommendations:**
- Specific strategies per identified critical factor
- Tracking metrics and suggested KPIs
- Customer segmentation based on factor scores
- Communication plan for internal stakeholders

---

## Deliverables and Assessment

### Deliverable 1: Technical Notebook (`factor_analysis_team[X].ipynb`)

**Required Content:**
- Reproducible code with complete factor analysis
- Rigorous statistical interpretation with methodological justifications
- Answers to all embedded reflection questions
- Cross-validation and robustness analysis

### Deliverable 2: Executive Report (`executive_summary_team[X].pdf`)

**Specifications:**
- **Length:** Maximum 4 pages (including visualizations)
- **Audience:** TechnoServe Solutions management team
- **Format:** Professional with executive summary, key findings, top 3 recommendations
- **Focus:** Business impact and actionable insights, not statistical methodology

### Deliverable 3: Executive Presentation Video (YouTube)

**Technical Specifications:**
- **Duration:** 10-12 minutes (focused presentation)
- **Format:** Executive presentation with key findings and recommendations
- **Participation:** Each member presents 3-4 minutes with specific expertise
- **Quality:** Clear audio/video, professional slides

**Suggested Structure:**
- **Opening & Context** (2 min): Business problem and approach
- **Key Findings** (5-6 min): Identified factors and their business impact  
- **Strategic Recommendations** (3-4 min): Top 3 actionable recommendations

### IMPORTANT: Links and Metadata

**In final Markdown cell of notebook:**

```markdown
## Team Information and Deliverables

**Team:** [Team name]

**Members:**
- [Full Name 1] ([ID]) - Expertise: [Factorability and Extraction]
- [Full Name 2] ([ID]) - Expertise: [Interpretation and Scoring]  
- [Full Name 3] ([ID]) - Expertise: [Application and Communication]

**Deliverable Links:**
- **Presentation Video:** [TITLE](YOUTUBE_URL)
- **Executive Report:** [Available on Canvas]
- **Dataset:** `customer_satisfaction_data.csv`

**Dates:**
- Analysis completed: [DD/MM/YYYY]
- Recording made: [DD/MM/YYYY] 
- Final submission: [DD/MM/YYYY]
```

---

## Evaluation Rubric (100 points)

### Distribution: 60% Technical Rigor + 25% Business Application + 15% Communication

| Component | Points | Assessment Criteria |
|-----------|--------|-------------------|
| **Factorability and Exploration** | 25 | EDA (8) + Statistical tests (10) + Dimensionality (7) |
| **Extraction and Rotation** | 30 | Comparative methods (15) + Rotation strategies (15) |
| **Business Interpretation** | 25 | Factor labeling (12) + Scoring and prediction (13) |
| **Strategic Communication** | 20 | Advanced visualization (12) + Executive recommendations (8) |

### Detailed Rubric by Competency

#### 1. Technical and Methodological Rigor (60 points)

| Level | Outstanding (A) | Competent (B) | Sufficient (C) | Insufficient (D) | Not Submitted (F) |
|-------|-----------------|---------------|----------------|------------------|------------------|
| **Factorability** (25 pts) | **25-23 pts:** Flawless implementation of all tests, expert statistical interpretation, solid methodological justifications | **22-20 pts:** Tests correctly implemented, appropriate interpretation, decision criteria applied | **19-17 pts:** Basic tests present, functional interpretation, some minor errors | **16-10 pts:** Partial implementation, errors in interpretation, poorly applied criteria | **<10 pts:** Tests absent or fundamentally incorrect |
| **Extraction/Rotation** (30 pts) | **30-27 pts:** Exhaustive methodological comparison, statistically justified selection, robustness analysis | **26-24 pts:** Methods correctly implemented, basic comparison, appropriate selection | **23-21 pts:** Functional implementation, superficial comparison, reasonable selection | **20-12 pts:** Methodological errors, inadequate comparison, unjustified selection | **<12 pts:** Methods absent or fundamentally incorrect |
| **Technical Validation** (5 pts) | **5 pts:** Residual analysis, cross-validation, robustness tests | **4 pts:** Basic validation present, some statistical checks | **3 pts:** Minimal validation, minor errors | **2-1 pts:** Inadequate validation or significant errors | **0 pts:** No validation |

#### 2. Business Application (25 points)

| Level | Outstanding (A) | Competent (B) | Sufficient (C) | Insufficient (D) | Not Submitted (F) |
|-------|-----------------|---------------|----------------|------------------|------------------|
| **Factor Interpretation** (12 pts) | **12-11 pts:** Conceptually rich labels, exceptional theoretical coherence, sophisticated cross-loading analysis | **10-9 pts:** Appropriate labels, solid theoretical coherence, clear interpretation | **8-7 pts:** Basic labels, acceptable coherence, functional interpretation | **6-4 pts:** Vague labels, weak coherence, superficial interpretation | **<4 pts:** Interpretation absent or incorrect |
| **Scoring and Prediction** (13 pts) | **13-12 pts:** Scoring methods compared, rigorous predictive models, differential impact analysis | **11-10 pts:** Scoring correctly implemented, functional prediction, impact analyzed | **9-8 pts:** Basic scoring, simple prediction, impact identified | **7-5 pts:** Scoring with errors, weak prediction, superficial impact | **<5 pts:** Scoring absent or incorrect |

#### 3. Communication and Presentation (15 points)

| Level | Outstanding (A) | Competent (B) | Sufficient (C) | Insufficient (D) | Not Submitted (F) |
|-------|-----------------|---------------|----------------|------------------|------------------|
| **Visualization** (8 pts) | **8 pts:** Publication-ready graphics, clear visual insights, effective storytelling | **7 pts:** Professional visualization, clear message, good technical quality | **6 pts:** Functional graphics, message present, acceptable quality | **5-3 pts:** Basic visualization, weak message, low quality | **<3 pts:** Visualization absent or non-functional |
| **Executive Video** (7 pts) | **7 pts:** Masterful executive presentation, balanced participation, broadcast quality | **6 pts:** Clear and professional presentation, good participation, high quality | **5 pts:** Functional presentation, appropriate participation, acceptable quality | **4-2 pts:** Weak presentation, unequal participation, low quality | **<2 pts:** Video absent or inaccessible |

### Additional Excellence Criteria

#### Innovation Bonus (up to +5 points)
- Implementation of advanced methods not covered in class
- Temporal stability analysis in longitudinal data  
- Creative integration with machine learning techniques
- Development of interactive tools for stakeholders

#### Academic Penalties

- **-10 points:** Academic integrity violations (plagiarism, copied code)
- **-5 points:** Video exceeds 15 minutes or less than 8 minutes
- **-3 points:** Unequal participation in video (>1 minute difference between members)
- **-5 points:** Notebook doesn't execute completely due to code errors
- **-2 points:** Variables or comments in Spanish without justification

---

## Schedule and Work Methodology

### Intensive 1-Week Schedule

| Day | Team Activities | Partial Deliverable |
|-----|----------------|-------------------|
| **Day 1-2** | Team formation, role division, technical setup, complete EDA and factorability tests | Work plan + Notebook Part 1 |
| **Day 3-4** | Dimensionality determination, factor extraction, method comparison, interpretation and scoring | Notebook Parts 2-3 |
| **Day 5-7** | Predictive models, visualization, executive report, video recording | Final deliverables |

**Submission deadline:** [To be defined by instructor]  
**Submission method:** Notebook + PDF + YouTube link on course platform

### Recommended Daily Time Investment

- **Individual work:** 2-3 hours per day
- **Team coordination:** 1 hour per day (online meetings)
- **Total team investment:** ~20-25 hours over 7 days

---

## Templates and Support Resources

### Template: Factorability Assessment

```python
def evaluate_factorability(satisfaction_data: pd.DataFrame) -> dict:
    """
    Evaluates whether data is appropriate for Factor Analysis.
    
    Args:
        satisfaction_data: DataFrame with satisfaction variables (1-7 scale)
    
    Returns:
        dict: Factorability test results
    """
    results = {}
    
    # TODO: Implement global and per-variable KMO test
    # TODO: Implement Bartlett's test
    # TODO: Calculate anti-image matrix and MSA values
    # TODO: Evaluate correlation matrix determinant
    
    return results

# Expected decision criteria:
# - Global KMO > 0.8 (excellent) or > 0.6 (acceptable)
# - Bartlett p-value < 0.05
# - Individual MSA > 0.5
# - Determinant ≠ 0 (non-singularity)
```

### Template: Extraction Methods Comparison

```python
def compare_extraction_methods(data: pd.DataFrame, n_factors: int) -> dict:
    """
    Compares PCA, PAF, and ML factor analysis.
    
    Args:
        data: DataFrame with standardized variables
        n_factors: Number of factors to extract
    
    Returns:
        dict: Comparative results by method
    """
    results = {}
    
    # TODO: Implement PCA with sklearn
    # TODO: Implement Factor Analysis with factor_analyzer
    # TODO: Compare eigenvalues, explained variance, communalities
    # TODO: Evaluate goodness of fit (for ML method)
    
    return results

# Expected comparison metrics:
# - % explained variance by method
# - Estimated communalities per variable
# - Chi-square goodness-of-fit (ML)
# - Factor structure interpretability
```

### Template: Rotation Analysis

```python
def analyze_rotations(factor_loadings: np.ndarray) -> dict:
    """
    Compares Varimax, Promax, and Oblimin rotations.
    
    Args:
        factor_loadings: Pre-rotation factor loading matrix
    
    Returns:
        dict: Post-rotation loadings and quality metrics
    """
    rotations = {}
    
    # TODO: Apply Varimax rotation (orthogonal)
    # TODO: Apply Promax rotation (oblique)
    # TODO: Evaluate simple structure (simplicity)
    # TODO: Analyze interfactor correlations
    
    return rotations

# Expected evaluation criteria:
# - Simple structure (loading > |0.4| on one factor)
# - Conceptual interpretability
# - Correlations between factors (oblique)
# - % variance preserved post-rotation
```

### Template: Scoring and Predictive Application

```python
def calculate_scores_and_predict(factor_model, data: pd.DataFrame, 
                               outcomes: pd.DataFrame) -> dict:
    """
    Calculates factor scores and evaluates predictive capacity.
    
    Args:
        factor_model: Fitted factor model
        data: Satisfaction variables
        outcomes: Business outcome variables
    
    Returns:
        dict: Factor scores and predictive models
    """
    results = {}
    
    # TODO: Calculate factor scores (regression method)
    # TODO: Implement predictive models per outcome
    # TODO: Evaluate R² and significance per factor
    # TODO: Develop Factor × Outcome impact matrix
    
    return results

# Expected business applications:
# - Customer segmentation by factor scores
# - Predictive models: NPS ~ factors
# - Improvement prioritization matrix
# - Estimated ROI per improvement factor
```

---

## Technical Resources and References

### Required Software and Libraries

**Python (Recommended):**
```python
# Essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import scipy.stats as stats
```

**R (Alternative):**
```r
# Essential libraries
library(psych)
library(GPArotation)  
library(corrplot)
library(FactoMineR)
library(factoextra)
```

### Reference Datasets

- **`customer_satisfaction_data.csv`**: Main dataset (3,400 obs)
- **`CUSTOMER_SATISFACTION_DATA_DICTIONARY.md`**: Complete variable documentation
- **`customer_satisfaction_analysis_template.py`**: Initial template with TODOs

### Essential Academic References

1. **Tabachnick, B.G. & Fidell, L.S.** (2019). *Using Multivariate Statistics* (7th ed.) - Chapters 13-14
2. **Hair, J.F., et al.** (2010). *Multivariate Data Analysis* (7th ed.) - Factor Analysis methodology
3. **Thompson, B.** (2004). *Exploratory and Confirmatory Factor Analysis* - Advanced interpretation
4. **Costello, A.B. & Osborne, J.W.** (2005). Best practices in exploratory factor analysis. *Practical Assessment Research & Evaluation*

### Specialized Online Resources

- **Factor Analysis in Python**: [scikit-learn documentation](https://scikit-learn.org/stable/modules/decomposition.html)
- **Business Intelligence Context**: Harvard Business Review articles on customer analytics
- **Statistical Validation**: UCLA Statistical Consulting tutorials

---

## Frequently Asked Questions and Troubleshooting

### Methodological Questions

**Q: What to do if KMO < 0.6 but business context suggests latent factors?**
A: Examine individual variables with MSA < 0.5, consider elimination or transformation, evaluate if sample size is sufficient.

**Q: How to decide between PCA and Factor Analysis for this context?**
A: Factor Analysis is preferable when seeking latent factors that explain correlations (like satisfaction dimensions), PCA when seeking dimensionality reduction preserving variance.

**Q: What to do with variables that don't load > |0.4| on any factor?**
A: Evaluate if they represent unique factors, consider elimination, or examine if more factors are needed. In business context, they may represent important unique aspects.

### Technical Questions

**Q: How to handle missing data in Factor Analysis?**
A: Evaluate pattern (MCAR, MAR, MNAR), use listwise deletion if <5%, consider multiple imputation if higher, avoid mean imputation which affects correlations.

**Q: Should the analysis include all 23 variables?**
A: Not necessarily. Evaluate communalities (<0.3 candidates for elimination), analyze factor loadings, maintain business theoretical coherence.

### Common Errors and Prevention

#### Frequent Statistical Errors

1. **Not evaluating assumptions**: Always verify normality, linearity, factorability
2. **Factor over-interpretation**: Factors must make theoretical sense, not just statistical  
3. **Ignoring interfactor correlations**: In oblique rotation, evaluate if correlations are substantive
4. **Misuse of factor scores**: Understand they are estimations with error, not exact values

#### Business Interpretation Errors

1. **Overly specific labels**: Factors represent latent dimensions, not precise constructs
2. **Inferred causality**: Factor analysis is exploratory, doesn't establish causality
3. **Ignoring business context**: Factors must be actionable for TechnoServe Solutions

#### Communication Errors

1. **Overly technical language**: Executive audience needs insights, not methodology
2. **Overloaded visualization**: Graphics should communicate clear message, not show all data
3. **Vague recommendations**: Should be specific, measurable, actionable, relevant, temporal (SMART)

---

## Success Criteria and Final Reflection

### Project Success Indicators

#### Technical Excellence
- [ ] Factor solution is statistically valid (KMO > 0.8, significant Bartlett)
- [ ] Factor interpretation is coherent with business theory
- [ ] Predictive models show significant factor-outcome relationships
- [ ] Analysis includes validation and robustness evaluation

#### Business Impact  
- [ ] Identified factors are actionable for TechnoServe Solutions
- [ ] Recommendations are prioritized by impact and feasibility
- [ ] Estimated ROI is realistic and well-founded
- [ ] Insights generate demonstrable strategic value

#### Professional Communication
- [ ] Video presents insights as senior consultants to C-Suite
- [ ] Visualizations tell coherent and convincing story
- [ ] Executive report balances rigor with accessibility
- [ ] Team demonstrates content mastery in Q&A

### Mandatory Final Reflection

**INCLUDE IN FINAL NOTEBOOK SECTION**

Respond reflectively (4-6 lines each) to **THREE** of the following five questions:

1. **Methodological Validity:** How would you evaluate the robustness of your factor solution? What additional analyses would you perform to strengthen the conclusions?

2. **Business Interpretation:** Which factor represents the greatest strategic opportunity for TechnoServe Solutions and why? How do you justify this prioritization?

3. **Analytical Limitations:** What fundamental limitations does the Factor Analysis approach have for this business problem? What complementary methods would you consider?

4. **Scalability and Implementation:** How would you adapt your analysis if TechnoServe had 10,000 clients and 50 satisfaction variables? What methodological challenges would emerge?

5. **Professional Development:** What aspect of factor analysis did you find most challenging and how did you develop competence in that area? What would you do differently in a similar project?

---

*This business case integrates advanced statistical rigor, meaningful business application, and professional communication skills development, preparing students for senior roles in analytics and data consulting.*