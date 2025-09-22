# Educational Assessment Data Dictionary

## Overview

This synthetic dataset contains educational assessment data for 100 students with 6 variables designed to demonstrate PCA vs Factor Analysis comparison. The data has known underlying factor structure for pedagogical purposes.

## Data Structure

- **Format**: CSV file (`educational.csv`)
- **Observations**: 100 students
- **Variables**: 6 assessment metrics + 1 identifier
- **Source**: Synthetic data with controlled factor structure

## Variables

### Identifier

- **Student**: Unique student identifier (format: STUD_001, STUD_002, etc.)

### Assessment Variables

#### Cognitive Domain (Intelligence Factor)

- **MathTest**: Mathematics assessment score
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Higher scores indicate better mathematical ability
  - **Factor Loading**: Strong positive loading on Intelligence factor

- **VerbalTest**: Verbal/language assessment score
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Higher scores indicate better verbal/language ability
  - **Factor Loading**: Moderate positive loading on Intelligence factor

#### Social-Emotional Domain (Personality Factor)

- **SocialSkills**: Social interaction and communication assessment
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Higher scores indicate better social skills
  - **Factor Loading**: Strong positive loading on Personality factor

- **Leadership**: Leadership and initiative assessment
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Higher scores indicate stronger leadership qualities
  - **Factor Loading**: Moderate positive loading on Personality factor

#### Control Variables (Noise)

- **RandomVar1**: Random noise variable (no latent structure)
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Pure noise, should not load on any meaningful factors
  - **Factor Loading**: Near zero on all factors

- **RandomVar2**: Random noise variable (no latent structure)
  - **Scale**: Continuous numeric
  - **Range**: Approximately -2.5 to +2.5 (standardized units)
  - **Interpretation**: Pure noise, should not load on any meaningful factors
  - **Factor Loading**: Near zero on all factors

## Known Factor Structure

This synthetic dataset was generated with two orthogonal latent factors:

### Intelligence Factor

- **Theoretical Construct**: General cognitive ability
- **Manifest Variables**: MathTest (strong), VerbalTest (moderate)
- **Expected Communality**: High for MathTest and VerbalTest
- **Expected Uniqueness**: Low to moderate measurement error

### Personality Factor

- **Theoretical Construct**: Social-emotional development
- **Manifest Variables**: SocialSkills (strong), Leadership (moderate)
- **Expected Communality**: High for SocialSkills and Leadership
- **Expected Uniqueness**: Low to moderate measurement error

### Noise Variables

- **Theoretical Construct**: None (pure error)
- **Manifest Variables**: RandomVar1, RandomVar2
- **Expected Communality**: Very low (near zero)
- **Expected Uniqueness**: High (near 1.0)

## Data Generation Parameters

- **Random Seed**: 42 (for reproducibility)
- **Latent Factors**: Two orthogonal standard normal variables
- **Factor Loadings**:
  - Strong: 0.85 (MathTest, SocialSkills)
  - Moderate: 0.80 (VerbalTest, Leadership)
- **Measurement Error**:
  - Low noise: σ = 0.2 (MathTest, SocialSkills)
  - Medium noise: σ = 0.25 (VerbalTest, Leadership)
- **Pure Noise**: σ = 0.6 and 0.5 for RandomVar1 and RandomVar2

## Expected Analysis Results

### PCA Results

- **PC1**: Should capture general ability (cognitive + social measures)
- **PC2**: Should separate cognitive vs social measures
- **PC3-PC4**: Additional structure and measurement error
- **PC5-PC6**: Pure noise components

### Factor Analysis Results

- **Factor 1**: Intelligence factor (MathTest, VerbalTest)
- **Factor 2**: Personality factor (SocialSkills, Leadership)
- **Communalities**: High for meaningful variables, low for noise
- **Simple Structure**: Clear separation after rotation

## Usage in Education

This dataset is designed for:

- **Method Comparison**: Direct PCA vs Factor Analysis comparison
- **Factor Recovery**: Testing how well methods identify known structure
- **Interpretation Practice**: Understanding loadings, communalities, uniqueness
- **Validation**: Ground truth available for assessing analysis quality

## References

- Generated using controlled synthetic data for pedagogical purposes
- Factor structure based on educational psychology literature
- Designed to demonstrate key differences between PCA and factor analysis