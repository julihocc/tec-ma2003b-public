# Factor Analysis Examples - Data Dictionaries Overview

This directory contains three comprehensive PCA/Factor Analysis examples with synthetic but realistic datasets from different domains. Each example includes detailed data dictionaries that explain the variables, their measurement scales, and domain-specific context.

## Examples Overview

### 1. Kuiper Belt Objects (`kuiper_example/`)
**Domain**: Astronomy/Planetary Science  
**Dataset**: 98 trans-Neptunian objects × 5 orbital parameters  
**Data Dictionary**: `KUIPER_BELT_DATA_DICTIONARY.md`
- Orbital elements: semi-major axis, eccentricity, inclination, absolute magnitude
- Physical interpretation: Dynamical populations, gravitational perturbations
- Educational focus: Space science applications, astronomical data analysis

### 2. European Stock Markets (`invest_example/`)  
**Domain**: Finance/Economics  
**Dataset**: 1,860 trading days × 4 European stock indices  
**Data Dictionary**: `EUROPEAN_STOCKS_DATA_DICTIONARY.md`
- Market indices: DAX, SMI, CAC, FTSE (Germany, Switzerland, France, UK)
- Financial interpretation: Market integration, systematic vs idiosyncratic risk
- Educational focus: Factor models in finance, correlation structure

### 3. Hospital Health Outcomes (`hospitals_example/`)
**Domain**: Healthcare/Public Health  
**Dataset**: 50 US hospitals × 8 quality metrics  
**Data Dictionary**: `HOSPITAL_OUTCOMES_DATA_DICTIONARY.md`
- Quality indicators: mortality, readmissions, satisfaction, infections, staffing
- Clinical interpretation: Multi-dimensional quality assessment, organizational effectiveness  
- Educational focus: Healthcare analytics, quality improvement

## Data Dictionary Features

Each data dictionary provides:
- **Variable definitions** with units and measurement scales
- **Realistic ranges** and benchmarks for interpretation
- **Domain context** explaining practical significance
- **Correlation structure** and why variables relate to each other
- **Educational applications** and learning objectives
- **References** to real data sources and further reading

## Educational Progression

The examples are designed to demonstrate PCA/Factor Analysis across different:
- **Correlation structures**: From moderate (Kuiper) to very high (stocks) correlations
- **Variance explained**: Different patterns of eigenvalue distributions  
- **Interpretation challenges**: Physical (orbital), economic (systematic risk), clinical (quality)
- **Data scales**: Different units requiring standardization
- **Sample sizes**: From small (50 hospitals) to large (1,860 observations)

## Usage in Coursework

These examples support learning objectives in:
- **Multivariate statistics**: PCA, factor analysis, correlation analysis
- **Data science applications**: Domain-specific statistical modeling
- **Interpretation skills**: Connecting statistical results to substantive knowledge
- **Research methods**: Understanding measurement, validity, and generalization
- **Professional applications**: Real-world statistical consulting scenarios

Each example folder contains complete documentation, runnable code, and generated visualizations for self-contained learning experiences.
