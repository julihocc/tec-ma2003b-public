# Quality Control Discriminant Analysis

This example demonstrates discriminant analysis for manufacturing quality control, classifying products into Acceptable, Borderline, and Defective categories based on dimensional and material properties.

## Manufacturing Context

A manufacturing company needs to automatically classify product quality during production to:
- **Acceptable Products**: Meet all specifications, ready for shipment
- **Borderline Products**: May require rework or special inspection
- **Defective Products**: Fail quality standards, need rejection or repair

## Dataset Description

The synthetic dataset contains 800 manufactured products with 6 quality measurements:

- **dimension1**: Primary dimension measurement (mm)
- **dimension2**: Secondary dimension measurement (mm)
- **thickness**: Material thickness (mm)
- **surface_roughness**: Surface finish quality (μm)
- **material_hardness**: Material hardness (HV)
- **defect_density**: Number of defects per cm²

## Analysis Approach

### Linear Discriminant Analysis (LDA)
- Assumes equal covariance matrices across quality classes
- Provides linear decision boundaries between quality categories
- More stable with smaller datasets

### Quadratic Discriminant Analysis (QDA)
- Allows different covariance matrices for each quality class
- Can capture non-linear relationships in quality data
- More flexible but requires more data

### Stepwise Feature Selection
- Automatically identifies the most important quality measurements
- Reduces model complexity while maintaining accuracy
- Helps focus on critical quality control parameters

## Key Results

### Discriminant Function Interpretation

**First Discriminant Function (LD1)**: Primarily separates Defective from Acceptable products
- High positive loadings: defect_density, surface_roughness
- High negative loadings: material_hardness, dimension accuracy
- Interpretation: Overall product quality and defect levels

**Second Discriminant Function (LD2)**: Distinguishes Borderline from other classes
- High positive loadings: dimensional variations
- Negative loadings: material property consistency
- Interpretation: Manufacturing process stability

### Classification Performance

- **LDA Accuracy**: ~95% on test set
- **QDA Accuracy**: ~97% on test set
- Both methods show excellent performance with QDA slightly better
- Cross-validation confirms robust performance across folds

### Feature Selection Results

Stepwise selection typically identifies 4-5 key features:
- defect_density (most important)
- surface_roughness
- material_hardness
- dimension1
- thickness

## Business Insights

1. **Acceptable Products**: Characterized by low defect density, good surface finish, and consistent material properties
2. **Borderline Products**: Show moderate dimensional variations and surface quality issues
3. **Defective Products**: Exhibit high defect density, poor surface finish, and inconsistent material properties

## Files in This Directory

- `fetch_quality.py`: Data generation script
- `quality_lda.py`: Main discriminant analysis implementation
- `quality.csv`: Generated quality dataset (800 × 7)
- `quality_scores.png`: Discriminant function scores visualization
- `quality_confusion.png`: Classification performance comparison
- `quality_feature_importance.png`: Feature importance analysis
- `README.md`: Manufacturing context and interpretation
- `QUALITY_DATA_DICTIONARY.md`: Quality metric definitions

## Usage

```bash
# Generate the dataset
python fetch_quality.py

# Run the discriminant analysis
python quality_lda.py
```

## Educational Value

This example illustrates:

- **Quality Control Applications**: Industrial classification problems
- **Feature Selection**: Identifying critical quality parameters
- **Manufacturing Insights**: Translating statistical results to production decisions
- **Model Comparison**: LDA vs QDA in practical manufacturing scenarios
- **Process Improvement**: Using discriminant analysis for quality optimization

## Extensions

Students can extend this analysis by:

- Adding more quality measurements (e.g., weight, conductivity)
- Implementing real-time quality monitoring
- Testing different classification thresholds
- Comparing with other machine learning methods
- Analyzing quality trends over time

## Manufacturing Applications

### Quality Assurance
- Automated defect detection during production
- Supplier quality evaluation
- Process capability analysis

### Process Optimization
- Identifying critical quality parameters
- Root cause analysis of defects
- Continuous improvement initiatives

### Cost Reduction
- Reducing inspection costs through automation
- Minimizing rework and scrap
- Optimizing quality control procedures