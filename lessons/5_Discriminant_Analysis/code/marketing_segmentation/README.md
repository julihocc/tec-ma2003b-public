# Marketing Segmentation Discriminant Analysis

This example demonstrates discriminant analysis for customer segmentation in marketing analytics. The analysis classifies customers into three segments (High-Value, Loyal, Occasional) based on their behavioral metrics.

## Business Context

A retail company wants to segment their customer base to optimize marketing strategies and resource allocation. By understanding distinct customer behaviors, the company can:

- **High-Value Customers**: Focus on retention and premium services
- **Loyal Customers**: Encourage upselling and cross-selling opportunities
- **Occasional Customers**: Implement re-engagement campaigns

## Dataset Description

The synthetic dataset contains 1,200 customers with 8 behavioral metrics:

- **purchase_freq**: Average purchases per month
- **avg_order_value**: Average dollar amount per order
- **browsing_time**: Average session time in minutes
- **cart_abandonment**: Rate of abandoned shopping carts
- **email_open_rate**: Percentage of marketing emails opened
- **loyalty_points**: Accumulated loyalty program points
- **support_tickets**: Average support interactions per month
- **social_engagement**: Social media interactions per month

## Analysis Approach

### Linear Discriminant Analysis (LDA)

- Assumes equal covariance matrices across groups
- Finds linear combinations that maximize between-group separation
- Provides interpretable discriminant functions

### Quadratic Discriminant Analysis (QDA)

- Allows different covariance matrices for each group
- More flexible but requires more parameters
- Better for groups with different variability patterns

## Key Results

### Discriminant Function Interpretation

**First Discriminant Function (LD1)**: Primarily separates High-Value from Occasional customers

- High positive loadings: avg_order_value, loyalty_points, social_engagement
- High negative loadings: cart_abandonment, support_tickets
- Interpretation: Overall customer value and engagement level

**Second Discriminant Function (LD2)**: Distinguishes Loyal from other segments

- High positive loadings: purchase_freq, email_open_rate
- High negative loadings: browsing_time (negative relationship)
- Interpretation: Purchase frequency vs. browsing behavior

### Classification Performance

- **LDA Accuracy**: ~92% on test set
- **QDA Accuracy**: ~94% on test set
- Both methods show strong performance with QDA slightly better
- Cross-validation confirms stable performance across folds

### Business Insights

1. **High-Value Segment**: Characterized by high spending, frequent purchases, and strong engagement
2. **Loyal Segment**: Regular purchasers with moderate spending but high email engagement
3. **Occasional Segment**: Infrequent buyers with higher cart abandonment and support needs

## Files in This Directory

- `fetch_marketing.py`: Data generation script
- `marketing_lda.py`: Main discriminant analysis implementation
- `marketing.csv`: Generated customer dataset (1,200 × 9)
- `marketing_scores.png`: Discriminant function scores visualization
- `marketing_boundaries.png`: Decision boundaries (2D projection)
- `marketing_confusion_matrices.png`: Classification performance comparison

## Usage

```bash
# Generate the dataset
python fetch_marketing.py

# Run the discriminant analysis
python marketing_lda.py
```

## Educational Value

This example illustrates:

- **Multivariate Classification**: Using multiple predictors for group assignment
- **Model Comparison**: LDA vs QDA performance and assumptions
- **Business Interpretation**: Translating statistical results to actionable insights
- **Visualization**: Effective plotting of discriminant functions and boundaries
- **Validation**: Cross-validation and confusion matrix analysis

## Extensions

Students can extend this analysis by:

- Adding more customer segments or behavioral metrics
- Incorporating temporal aspects (seasonal behavior)
- Testing different variable selection methods
- Comparing with other classification algorithms (SVM, Random Forest)
- Implementing cost-sensitive classification for business decisions