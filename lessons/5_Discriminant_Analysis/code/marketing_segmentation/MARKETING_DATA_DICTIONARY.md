# Marketing Segmentation Data Dictionary

## Overview

This data dictionary describes the synthetic customer behavior dataset used for discriminant analysis in marketing segmentation. The dataset contains 1,200 customer records across three distinct segments, generated to reflect realistic e-commerce customer behavior patterns.

## Dataset Structure

- **File**: `marketing.csv`
- **Rows**: 1,200 (customers)
- **Columns**: 9 (8 features + 1 target)
- **Data Type**: CSV with header row

## Variables

### Target Variable

| Variable | Type | Description | Values |
|----------|------|-------------|---------|
| `segment` | Categorical | Customer segment classification | 'High-Value', 'Loyal', 'Occasional' |

### Feature Variables

| Variable | Type | Description | Range | Units |
|----------|------|-------------|-------|-------|
| `purchase_freq` | Numeric | Average number of purchases per month | 0.5 - 35.0 | purchases/month |
| `avg_order_value` | Numeric | Average dollar amount spent per order | $10.0 - $250.0 | USD |
| `browsing_time` | Numeric | Average time spent browsing per session | 1.0 - 70.0 | minutes |
| `cart_abandonment` | Numeric | Proportion of shopping carts abandoned | 0.0 - 1.0 | rate (0-1) |
| `email_open_rate` | Numeric | Proportion of marketing emails opened | 0.0 - 1.0 | rate (0-1) |
| `loyalty_points` | Numeric | Accumulated loyalty program points | 0.0 - 750.0 | points |
| `support_tickets` | Numeric | Average customer support interactions per month | 0.0 - 5.0 | tickets/month |
| `social_engagement` | Numeric | Social media interactions per month | 0.0 - 15.0 | interactions/month |

## Segment Definitions

### High-Value Customers (30% of dataset)

Premium customers who drive significant revenue through frequent high-value purchases and strong engagement.

**Characteristics**:

- High purchase frequency and order values
- Low cart abandonment rates
- High email engagement and loyalty points
- Active social media participation
- Minimal support interactions

**Business Strategy**: Retention focus, premium services, personalized recommendations

### Loyal Customers (40% of dataset)

Regular customers with consistent purchasing patterns and moderate spending levels.

**Characteristics**:

- Moderate purchase frequency
- Consistent order values
- Good email engagement
- Building loyalty points over time
- Occasional support needs

**Business Strategy**: Upselling opportunities, cross-selling, loyalty program enhancement

### Occasional Customers (30% of dataset)

Infrequent buyers who require re-engagement efforts to increase purchase activity.

**Characteristics**:

- Low purchase frequency
- Variable order values
- High cart abandonment rates
- Low email and social engagement
- Higher support ticket volume

**Business Strategy**: Re-engagement campaigns, cart recovery, customer education

## Data Generation Methodology

### Statistical Approach

- **Multivariate Normal Distribution**: Each segment generated from distinct multivariate normal distributions
- **Realistic Correlations**: Features exhibit plausible relationships (e.g., high loyalty points correlate with purchase frequency)
- **Segment Separation**: Means designed to create clear discriminant boundaries while maintaining realistic variability

### Key Parameters

#### High-Value Segment

- **Sample Size**: 360 customers
- **Mean Vector**: [25.0, 150.0, 45.0, 0.15, 0.85, 500.0, 0.5, 8.5]
- **Covariance Structure**: Higher variance in spending metrics, positive correlations between engagement variables

#### Loyal Segment

- **Sample Size**: 480 customers
- **Mean Vector**: [15.0, 75.0, 35.0, 0.25, 0.75, 300.0, 1.0, 6.0]
- **Covariance Structure**: Moderate correlations, balanced variability across features

#### Occasional Segment

- **Sample Size**: 360 customers
- **Mean Vector**: [3.0, 45.0, 15.0, 0.6, 0.3, 50.0, 2.5, 1.5]
- **Covariance Structure**: Higher variance in abandonment and support metrics

## Data Quality Notes

### Bounds and Constraints

- All rates (cart_abandonment, email_open_rate) constrained to [0,1]
- Time and frequency variables constrained to realistic positive values
- Monetary values reflect typical e-commerce ranges

### Random Seed

- **Seed**: 42 (for reproducibility)
- Ensures consistent results across multiple runs

## Usage in Analysis

### Discriminant Analysis Setup

- **Features**: All 8 behavioral metrics (standardized for analysis)
- **Target**: Customer segment (3-class classification)
- **Validation**: 70/30 train/test split with stratification

### Expected Performance

- **LDA Accuracy**: ~90-95% (equal covariance assumption holds reasonably well)
- **QDA Accuracy**: ~92-96% (allows different covariance matrices)
- **Cross-validation**: Stable performance across 5-fold CV

## Educational Applications

### Learning Objectives

1. **Multivariate Classification**: Understanding group separation in high-dimensional space
2. **Assumption Testing**: Evaluating LDA vs QDA appropriateness
3. **Interpretation**: Translating discriminant functions to business insights
4. **Model Validation**: Cross-validation and performance metrics

### Common Analysis Questions

- Which behavioral metrics best distinguish customer segments?
- How do LDA and QDA compare in this application?
- What are the business implications of each discriminant function?
- How stable are the classifications across different data samples?

## Extensions and Modifications

### Additional Features

- Seasonal purchasing patterns
- Geographic location data
- Product category preferences
- Customer lifetime value metrics

### Alternative Segmentations

- Recency-Frequency-Monetary (RFM) based segments
- Behavioral vs. Demographic clustering
- Churn risk segmentation

---

**Note**: This synthetic dataset is designed for educational purposes and reflects generalized patterns observed in real e-commerce customer data. Actual customer behavior may vary based on industry, market conditions, and business model.