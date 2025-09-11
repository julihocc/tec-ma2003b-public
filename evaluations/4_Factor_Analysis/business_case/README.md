# Factor Analysis Business Case - Instructor Guide

## Overview

This folder contains a complete **college-level Factor Analysis business case** designed for advanced statistics, data science, or quantitative methods courses. The case provides synthetic but realistic customer satisfaction data with a known 5-factor structure, challenging students to discover this structure through rigorous statistical analysis.

## Educational Framework

- **Target Level:** Upper-division undergraduate or graduate
- **Duration:** 2 weeks (25% of course weight)
- **Team Size:** 3 students per team with assigned expertise roles
- **Assessment:** Multi-modal (technical analysis + executive report + video presentation)

## Problem Statement

TechnoServe Solutions has collected extensive customer satisfaction data across multiple service dimensions but struggles to:

1. **Identify Key Drivers**: Which factors most influence overall customer satisfaction and loyalty?
2. **Reduce Complexity**: How can 20+ survey dimensions be simplified into manageable strategic areas?
3. **Prioritize Investments**: Where should the company focus limited resources for maximum impact?
4. **Predict Outcomes**: Can underlying factors predict customer retention and revenue growth?

## Dataset Overview

**Data Source**: Customer Satisfaction Survey (Q1-Q4 2024)
- **Sample Size**: 850 enterprise clients
- **Variables**: 22 satisfaction dimensions + 8 business outcome metrics
- **Time Period**: 12 months of quarterly measurements
- **Response Rate**: 78% (industry benchmark: 45%)

### Key Variable Categories

**Service Quality Dimensions** (1-7 Likert scale):
- Technical expertise and knowledge
- Project management efficiency
- Communication clarity and frequency
- Problem resolution speed
- Innovation and creative solutions
- Cost transparency and value

**Relationship Factors**:
- Account manager responsiveness
- Executive accessibility
- Trust and reliability
- Long-term partnership orientation

**Outcome Metrics**:
- Overall satisfaction score
- Net Promoter Score (NPS)
- Contract renewal likelihood
- Revenue growth per account
- Referral generation rate

## Learning Objectives

Students will demonstrate mastery of Factor Analysis by:

### 1. Exploratory Data Analysis
- Assess data suitability for Factor Analysis (KMO, Bartlett's test)
- Identify patterns in correlation matrices
- Handle missing data and outliers appropriately

### 2. Factor Extraction and Selection
- Compare extraction methods (PCA vs. Maximum Likelihood)
- Determine optimal number of factors using multiple criteria
- Interpret scree plots and eigenvalue patterns

### 3. Factor Rotation and Interpretation
- Apply and compare rotation methods (Varimax, Promax, Oblimin)
- Develop meaningful factor labels based on loading patterns
- Validate factor structure across different customer segments

### 4. Business Application
- Calculate factor scores for strategic segmentation
- Develop predictive models using factor scores
- Create actionable recommendations for management

## Deliverables

### Phase 1: Technical Analysis Report (40% of grade)
- **Data Preparation**: Missing data treatment, outlier analysis
- **Factorability Assessment**: KMO values, correlation analysis
- **Factor Extraction**: Method comparison and selection rationale
- **Factor Interpretation**: Clear business labels and descriptions

### Phase 2: Strategic Recommendations (35% of grade)
- **Customer Segmentation**: Factor-based clustering analysis
- **Priority Matrix**: Investment recommendations by factor importance
- **Predictive Insights**: Regression models using factor scores
- **Implementation Roadmap**: Actionable next steps

### Phase 3: Executive Presentation (25% of grade)
- **Business Summary**: 10-minute presentation to mock board
- **Visual Analytics**: Dashboard mockup using factor insights
- **ROI Projections**: Expected impact of recommendations
- **Q&A Defense**: Technical and business question handling

## Assessment Criteria

### Technical Proficiency (50%)
- Correct application of Factor Analysis methodology
- Appropriate use of statistical software (R/Python/SPSS)
- Valid interpretation of statistical outputs
- Proper handling of assumptions and limitations

### Business Acumen (30%)
- Clear translation of statistical findings to business context
- Realistic and actionable recommendations
- Understanding of consulting industry dynamics
- Cost-benefit analysis quality

### Communication Skills (20%)
- Professional report writing and formatting
- Effective data visualization and storytelling
- Presentation clarity and executive-level messaging
- Ability to defend analytical choices

## Timeline and Milestones

**Week 1-2**: Data exploration and preparation
- Initial EDA and data quality assessment
- Literature review on customer satisfaction factors
- Preliminary correlation analysis

**Week 3-4**: Factor analysis implementation
- Method selection and extraction
- Rotation comparison and selection
- Factor interpretation and validation

**Week 5-6**: Business application development
- Factor scoring and segmentation
- Predictive modeling
- Strategic recommendations formulation

**Week 7**: Final deliverable completion
- Report writing and presentation preparation
- Peer review and feedback incorporation
- Executive presentation practice

## Business Case Files

### Dataset and Documentation
- **`customer_satisfaction_data.csv`**: Complete synthetic dataset (3,400 observations)
- **`CUSTOMER_SATISFACTION_DATA_DICTIONARY.md`**: Comprehensive variable descriptions and analysis notes
- **`fetch_customer_data.py`**: Data generation script (for instructors/reproducibility)

### Analysis Templates
- **`customer_satisfaction_analysis_template.py`**: Starter template with EDA and factor analysis structure
- **`analysis_output/`**: Directory for student-generated plots, reports, and results

## Resources and Support

### Required Software
- Statistical software (Python recommended with pandas, scikit-learn, factor_analyzer packages)
- Data visualization tools (matplotlib, seaborn for Python; ggplot2 for R)
- Presentation software (PowerPoint, Google Slides)

### Industry Context Materials
- Consulting industry benchmarks and KPIs
- Customer experience best practices
- Technology services market analysis
- Sample executive presentation templates

### Technical Support
- Office hours with instructor for methodology questions
- TA support for software implementation issues
- Peer collaboration encouraged for concept discussion
- Industry mentor sessions (optional)

## Success Metrics

Students successfully completing this business case will demonstrate:

1. **Technical Mastery**: Proper Factor Analysis implementation with >85% methodology accuracy
2. **Business Impact**: Recommendations that address real consulting challenges
3. **Professional Skills**: Executive-quality deliverables suitable for client presentation
4. **Critical Thinking**: Thoughtful analysis of limitations and alternative approaches

## Extension Opportunities

Advanced students may explore:
- **Longitudinal Analysis**: Factor stability over time
- **Multi-group Analysis**: Factor invariance across client segments  
- **Advanced Methods**: Robust Factor Analysis or Sparse PCA
- **Machine Learning Integration**: Factor features in predictive models

---

**Note**: This business case is designed to simulate real-world consulting scenarios while providing structured learning opportunities. All company names and data are fictional but based on authentic industry patterns and challenges.