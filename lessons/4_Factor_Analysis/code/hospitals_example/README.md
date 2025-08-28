# Hospital Health Outcomes PCA Example

## Overview

This example demonstrates Principal Component Analysis (PCA) applied to hospital health outcome metrics. It analyzes synthetic data for 50 US hospitals across 8 key performance indicators to understand patterns in hospital quality and identify the main dimensions of healthcare performance variation.

## Files

- `fetch_hospitals.py` - Generates synthetic but realistic hospital health outcome data
- `hospitals_example.py` - Main PCA analysis script with detailed explanations
- `hospitals.csv` - Generated dataset (50 hospitals × 8 metrics)
- `hospitals_scree.png` - Scree plot for component selection
- `hospitals_biplot.png` - Biplot visualization of hospitals and variables
- `HOSPITAL_OUTCOMES_DATA_DICTIONARY.md` - Detailed variable definitions and clinical context

## Health Outcome Variables

The dataset includes 8 key hospital performance metrics:

1. **MortalityRate** (%) - Hospital mortality rate (lower is better)
2. **ReadmissionRate** (%) - 30-day readmission rate (lower is better)
3. **PatientSatisfaction** (0-100) - Patient satisfaction score (higher is better)
4. **AvgLengthStay** (days) - Average length of stay (shorter generally better)
5. **InfectionRate** (%) - Hospital-acquired infection rate (lower is better)
6. **NurseRatio** - Nurse-to-patient ratio (higher is better)
7. **SurgicalComplications** (%) - Surgical complication rate (lower is better)
8. **EDWaitTime** (minutes) - Emergency department wait time (lower is better)

## Usage

```bash
# Generate the synthetic hospital data
python fetch_hospitals.py

# Run the PCA analysis
python hospitals_example.py
```

## Key Findings

The PCA analysis reveals:

- **PC1 (70.5% variance)**: Represents overall hospital quality
  - High-quality hospitals have lower mortality, readmissions, infections, complications, and wait times
  - They also have higher patient satisfaction and better nurse-to-patient ratios
  - This is a classic "halo effect" where good hospitals perform well across multiple metrics

- **PC2 (8.5% variance)**: May capture efficiency vs. thoroughness trade-offs
  - Separates hospitals with different length-of-stay patterns
  - Could represent different care philosophies or patient populations

## Educational Value

This example illustrates:

- **Healthcare quality measurement**: How multiple outcome metrics relate to each other
- **Dimensionality reduction**: 8 metrics can be effectively summarized by 2-3 principal components
- **Quality assessment**: Use PC1 scores to rank hospital performance
- **Policy implications**: Identify best practices from high-performing hospitals
- **Correlation structure**: Understanding how different aspects of hospital care are interconnected

## Clinical Interpretation

The strong first principal component suggests that hospital quality is largely unidimensional - hospitals that perform well on one metric tend to perform well on others. This supports:

- **System-wide quality improvement**: Focusing on overall organizational excellence rather than isolated metrics
- **Benchmarking**: Using composite quality scores based on PC1 for hospital comparisons
- **Resource allocation**: Identifying hospitals needing comprehensive quality improvement

## Extensions

Consider exploring:

- Longitudinal analysis to track quality improvements over time
- Clustering hospitals based on PC scores to identify distinct quality profiles
- Factor rotation for more interpretable quality dimensions
- Validation against external hospital ratings (e.g., CMS star ratings)
- Incorporation of additional metrics (cost, efficiency, specialty care quality)
