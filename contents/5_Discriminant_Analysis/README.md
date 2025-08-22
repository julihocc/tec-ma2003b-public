# Chapter 5 — Discriminant analysis (index)

This folder mirrors the course structure and contains short practice scripts, a LaTeX section, and a brief report for each subtopic.

Subfolders and contents

- 5.1_Discrimination_for_two_multivariate_normal_populations/
  - discrimination_two_populations_practice.py — simulate two Gaussians and compute a pooled-covariance LDA rule.
  - discrimination_two_populations.tex — theory notes for section 5.1.
  - discrimination_two_populations_report.txt — short exercise and hints.

- 5.2_Cost_function_and_prior_probabilities/
  - costs_priors_practice.py — illustrate effect of priors and asymmetric costs on thresholds.
  - costs_priors.tex
  - costs_priors_report.txt

- 5.3_Basic_discrimination/
  - basic_discrimination_practice.py — confusion matrix, sensitivity/specificity examples.
  - basic_discrimination.tex
  - basic_discrimination_report.txt

- 5.4_Stepwise_selection/
  - stepwise_selection_practice.py — illustrative forward-selection demo (use CV for real tasks).
  - stepwise_selection.tex
  - stepwise_selection_report.txt

- 5.5_Canonical_discriminant_functions/
  - canonical_practice.py — compute S_w, S_b and solve the generalized eigenproblem.
  - canonical.tex
  - canonical_report.txt

- 5.6_Coding_and_commercial_software/
  - coding_software_practice.py — small scikit-learn example (falls back if sklearn not installed).
  - coding_software.tex
  - coding_software_report.txt

Quick run / smoke-test

Use the project virtual environment (recommended) before running the examples. From the repository root (zsh):

```bash
# activate venv (if created at .venv)
source .venv/bin/activate

# run a single practice script
python contents/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/discrimination_two_populations_practice.py

# run all practice scripts (simple smoke test)
for f in contents/5_Discriminant_Analysis/*/*_practice.py; do
  echo "--- running $f ---"
  python "$f" || break
done
```

Notes and recommendations

- Some examples use optional libraries (scikit-learn). If you plan to run all demos, install common scientific packages (numpy, scipy, scikit-learn) in the venv.
- The practice scripts are intentionally small and illustrative. I recommend adding minimal unit tests and cleaning minor lint warnings before using them in assessments.
- If you want, I can run a smoke test now, or clean the small lint issues found in a couple of practice scripts.

