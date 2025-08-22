# MA2003B - Application of Multivariate Methods in Data Science

**CIP:** 270501 Statistics, General  
**Discipline:** Mathematics  
**School:** Engineering and Sciences  
**Academic Department:** Sciences  
**Programs:** 5 IDM19 Modules  
**Prerequisites:** MA1036 and TC2004B  
**Equivalences:** None  

---

## Course Intention

This intermediate mathematics course focuses on analyzing multidimensional large databases. Students identify characteristics of problems that can be addressed using multivariate statistical techniques.

**Required prior knowledge:**

- Probability and statistics
- Probability functions
- Normal distribution
- Inferential statistics (hypothesis testing, confidence intervals)

---

## Learning Outcome

Students will analyze a multidimensional phenomenon or process using one or more multivariate statistical techniques learned in the course.

---

## Course Objectives

Upon completion, students will be able to:

- Build structured, analyzable databases.
- Extract relevant information using statistical methods and tools.
- Formulate mathematical models for large-scale optimization.
- Analyze systems with an integrated vision.
- Solve real-world problems ethically and responsibly.

---

## Course Topics and Subtopics

### 1. Regression Analysis

- 1.1 Simple linear regression  
- 1.2 ANOVA and confidence intervals  
- 1.3 Residual analysis and normality  
- 1.4 Forward selection  
- 1.5 Backward selection  
- 1.6 Non-linear regression  
- 1.7 Multiple linear regression  
- 1.8 Aberrant data and heteroskedasticity  

### 2. Multivariate Analysis

- 2.1 Multivariate distributions  
- 2.2 Mean vectors, variance, and covariance matrices  
- 2.3 Correlations and correlation matrices  
- 2.4 Multivariate normal PDF  
- 2.5 Handling missing/incorrect values  
- 2.6 Multivariate aberrant data  
- 2.7 Sample correlations, Fisher and Ruben intervals  
- 2.8 Descriptive analytics and visualization  

### 3. Principal Component Analysis (PCA)

- 3.1 Use cases  
- 3.2 Geometrical description  
- 3.3 Estimation of components  
- 3.4 Determining number of components  
- 3.5 Coding and software  

### 4. Factor Analysis

- 4.1 Objectives  
- 4.2 Equations  
- 4.3 Choosing number of factors  
- 4.4 Factor rotation  
- 4.5 Oblique rotation  
- 4.6 Coding and software  

### 5. Discriminant Analysis

- 5.1 Two-population discrimination  
- 5.2 Cost functions and prior probabilities  
- 5.3 Basic discrimination  
- 5.4 Stepwise selection  
- 5.5 Canonical discriminant functions  
- 5.6 Coding and software  

### 6. Cluster Analysis

- 6.1 Similarity/dissimilarity measures  
- 6.2 Graphical methods (scatter, PCA, Andrews)  
- 6.3 Non-hierarchical grouping  
- 6.4 Hierarchical grouping  
- 6.5 Nearest neighbor method  
- 6.6 Coding and software  

### 7. Multivariate Regression

- 7.1 Logistic regression  
- 7.2 Inference for variance/covariance matrices  
- 7.3 Inference for mean vectors  
- 7.4 MANOVA  
- 7.5 Canonical correlation analysis  
- 7.6 Factor analysis and regression  
- 7.7 Programming and software  

---

## Learning Methodologies

### Supervised Learning

1. Teacher-led conceptual reviews and modules  
2. Discussions and problem-solving  
3. Mentoring for real-world challenges  
4. Individual and group counseling  

### Independent Learning

1. Research on regression and multivariate methods  
2. Exercises and case studies  
3. Fieldwork on data acquisition and transformation  
4. Evidence generation for skill development  

**Deliverable:**  
A complete report on the real-world problem solution, including justification for the chosen statistical method.

---

## Evaluation

- **50%**: Activities, assignments, cases, and exams  
- **50%**: Performance in real-world challenge and evidence of competency

---

## Bibliography

### Textbooks

- Johnson, R.A.; Wichern, D.W. *Applied Multivariate Statistical Analysis*, 6th ed., Pearson, 2013. ISBN: 9781292024943

### Reference Books

- Anderson, T.W. *An Introduction to Multivariate Statistical Analysis*, 3rd ed., Wiley, 2003. ISBN: 0471360910  
- Wickham, H. *R for Data Science*, O’Reilly, 2016. ISBN: 9781491910399

---

## Teaching Requirements

**Academic Credentials:**

- Master’s or Doctoral Degree in:
  - Statistics (270501)
  - Mathematics (270101)
  - Applied Mathematics (270301)

## Developer setup & running scripts

Quick steps to set up a development environment and run the repository's convenience scripts:


1. Create and activate a local virtual environment in the repo root:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

1. Preferred: install the package in editable mode so `from utils import ...` works in scripts:

  ```bash
  pip install -e .
  # fallback: pip install pytest
  ```

1. Run the unit tests from the repo root:

  ```bash
  .venv/bin/python -m pytest -q
  ```

1. Run the convenience data-pull script (it expects the package to be importable). You can override the source path with an environment variable `MA2003B_ORIGIN_PATH`:

  ```bash
  # use env override if your data lives elsewhere
  MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
  ```

Notes:

- The `scripts/pull_data.py` script copies the course source files into `backup/ma2003b` under the repository; it includes a safety check to avoid copying when the backup directory would be inside the origin.
- If you add runtime dependencies, add a `requirements.txt` or `pyproject.toml` and document installation here.

## Contributing

Small changes, typos and lightweight utilities are welcome. Follow these conventions:

- Keep exercise materials inside their exercise folders under `1_Regression_Analysis/`.
- Add small utilities to `utils/` and export them through `utils/__init__.py`.
- Update or add tests next to the module you change and run `python -m pytest -q`.

## Agent guidance

This repository includes a short agent guide at `.github/copilot-instructions.md` with focused instructions for automated coding agents (venv, editable install, project conventions).

## pull_data CLI examples

`scripts/pull_data.py` includes a small CLI. Examples:

- Dry run (no changes):

```bash
.venv/bin/python scripts/pull_data.py --dry-run
```

- Run copying with env override:

```bash
MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
```

- Run copying with explicit paths and verbosity:

```bash
.venv/bin/python scripts/pull_data.py --origin /path/to/origin --backup ./backup/ma2003b --verbose
```

