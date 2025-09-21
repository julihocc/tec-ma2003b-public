# Quality Control Data Dictionary

## Overview

This data dictionary describes the synthetic manufacturing quality control dataset used for discriminant analysis. The dataset contains 800 product measurements across three quality classes, designed to reflect realistic manufacturing quality control scenarios.

## Dataset Structure

- **File**: `quality.csv`
- **Rows**: 800 (products)
- **Columns**: 7 (6 features + 1 target)
- **Data Type**: CSV with header row

## Variables

### Target Variable

| Variable | Type | Description | Values |
|----------|------|-------------|---------|
| `quality_class` | Categorical | Product quality classification | 'Acceptable', 'Borderline', 'Defective' |

### Feature Variables

| Variable | Type | Description | Range | Units |
|----------|------|-------------|-------|-------|
| `dimension1` | Numeric | Primary dimension measurement | 8.5 - 12.0 | mm |
| `dimension2` | Numeric | Secondary dimension measurement | 3.5 - 6.5 | mm |
| `thickness` | Numeric | Material thickness | 1.8 - 3.2 | mm |
| `surface_roughness` | Numeric | Surface finish quality | 0.005 - 0.2 | μm |
| `material_hardness` | Numeric | Material hardness | 70 - 120 | HV |
| `defect_density` | Numeric | Surface defect density | 0 - 2.0 | defects/cm² |

## Quality Class Definitions

### Acceptable Products (75% of dataset)
High-quality products that meet all manufacturing specifications and are ready for shipment without additional processing.

**Characteristics**:
- Precise dimensional control
- Low surface roughness
- Consistent material properties
- Minimal defect density
- Within specification tolerances

**Business Action**: Direct shipment to customers

### Borderline Products (20% of dataset)
Products with marginal quality that may require additional inspection, rework, or special handling before shipment.

**Characteristics**:
- Slight dimensional variations
- Moderate surface roughness
- Acceptable material properties
- Low to moderate defect density
- Near specification limits

**Business Action**: Additional inspection or rework

### Defective Products (5% of dataset)
Products that fail to meet minimum quality standards and require repair, scrap, or return to supplier.

**Characteristics**:
- Significant dimensional deviations
- High surface roughness
- Inconsistent material properties
- High defect density
- Outside specification tolerances

**Business Action**: Repair, scrap, or return to supplier

## Data Generation Methodology

### Statistical Approach
- **Multivariate Normal Distribution**: Each quality class generated from distinct multivariate normal distributions
- **Realistic Manufacturing Variability**: Different covariance structures reflect actual production process variations
- **Quality Separation**: Means designed to create clear quality boundaries while maintaining realistic manufacturing distributions

### Key Parameters

#### Acceptable Products
- **Sample Size**: 600 products
- **Mean Vector**: [10.0, 5.0, 2.5, 0.02, 98.5, 0.15]
- **Covariance Structure**: Low variance, tight quality control

#### Borderline Products
- **Sample Size**: 160 products
- **Mean Vector**: [10.2, 4.9, 2.4, 0.05, 95.0, 0.35]
- **Covariance Structure**: Moderate variance, process drift indicators

#### Defective Products
- **Sample Size**: 40 products
- **Mean Vector**: [10.5, 4.7, 2.2, 0.12, 85.0, 1.2]
- **Covariance Structure**: High variance, out-of-control process indicators

## Data Quality Notes

### Engineering Bounds and Constraints
- All dimensional measurements constrained to realistic manufacturing ranges
- Material properties reflect typical engineering specifications
- Surface quality metrics based on standard manufacturing tolerances
- Defect density represents practical inspection capabilities

### Random Seed
- **Seed**: 42 (for reproducibility)
- Ensures consistent results across multiple runs

## Usage in Analysis

### Discriminant Analysis Setup
- **Features**: All 6 quality measurements (standardized for analysis)
- **Target**: Quality class (3-class classification)
- **Validation**: 70/30 train/test split with stratification

### Expected Performance
- **LDA Accuracy**: ~90-95% (equal covariance assumption reasonable for quality control)
- **QDA Accuracy**: ~92-97% (allows different variability patterns)
- **Cross-validation**: Stable performance across 5-fold CV

## Educational Applications

### Learning Objectives
1. **Manufacturing Applications**: Understanding industrial quality control
2. **Feature Selection**: Identifying critical quality parameters
3. **Process Control**: Using statistics for manufacturing decisions
4. **Cost-Benefit Analysis**: Balancing quality inspection costs

### Common Analysis Questions
- Which quality measurements best predict product defects?
- How do LDA and QDA compare in manufacturing quality control?
- What are the cost implications of different classification thresholds?
- How can discriminant analysis improve manufacturing processes?

## Extensions and Modifications

### Additional Quality Metrics
- Geometric dimensioning and tolerancing (GD&T)
- Material composition analysis
- Functional testing results
- Environmental testing data

### Process Integration
- Real-time quality monitoring
- Statistical process control (SPC) integration
- Automated inspection systems
- Supplier quality management

### Advanced Analytics
- Time series quality analysis
- Root cause analysis integration
- Predictive maintenance linkage
- Quality cost optimization

---

**Note**: This synthetic dataset is designed for educational purposes and reflects generalized patterns observed in real manufacturing quality control data. Actual quality measurements may vary based on product type, manufacturing process, and industry standards.