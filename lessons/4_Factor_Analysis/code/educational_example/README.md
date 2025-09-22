# Educational Example — PCA & FA comparison

This folder contains scripts demonstrating PCA and Factor Analysis on the same synthetic educational assessment dataset. The examples are intended for classroom use and direct method comparison.

## Files

- `fetch_educational.py` - Generates synthetic educational assessment data and saves as `educational.csv`
- `educational_pca.py` - PCA analysis on the synthetic educational data
- `educational_fa.py` - Factor Analysis using the same synthetic data for direct comparison
- `educational.csv` - Generated synthetic dataset (100 students × 6 variables)
- `EDUCATIONAL_ASSESSMENT_DATA_DICTIONARY.md` - Detailed data dictionary with known factor structure
- `pca_scree.png`, `pca_biplot.png`, `fa_loadings.png`, `fa_scree.png` - figures produced by the scripts

## Usage

First, generate the synthetic data:

```bash
python fetch_educational.py
```

Then run either analysis script from this folder (recommended using the virtual environment):

```bash
python educational_pca.py
python educational_fa.py
```

## Dataset Description

The synthetic dataset contains educational assessment data for 100 students with known underlying factor structure:

- **Intelligence Factor**: Affects MathTest, VerbalTest (cognitive domain)
- **Personality Factor**: Affects SocialSkills, Leadership (social-emotional domain)
- **Noise Variables**: RandomVar1, RandomVar2 (pure noise, no latent structure)

This controlled structure allows validation of whether PCA and Factor Analysis correctly recover the known latent factors.

## Educational Purpose

This example demonstrates:

- **Method Comparison**: Direct PCA vs Factor Analysis on identical data
- **Factor Recovery**: Testing how well methods identify known latent structure
- **Interpretation**: Understanding loadings, communalities, and uniqueness
- **Validation**: Ground truth available for assessing analysis quality

## Notes

- These scripts follow the same pattern as other examples in the course (hospitals, invest, kuiper)
- The data has known factor structure for pedagogical validation
- Both PCA and FA use the same preprocessing (standardization) for fair comparison
- If other parts of the repository reference `pca_example`, update those references to `educational_example`.
