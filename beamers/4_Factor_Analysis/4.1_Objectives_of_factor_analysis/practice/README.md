Python demo for "Objectives of Factor Analysis"
===============================================

This folder contains the Python practice script `objectives_factor_analysis_practice.py` used in the MA2003B course (chapter 4.1). The Python demo uses scikit-learn for PCA and the `factor_analyzer` package for factor analysis.

Quick notes

- The Python demo assumes you have `numpy`, `scikit-learn`, and `factor_analyzer` installed in your environment.

- A minimal, educational implementation of PCA/FA is available in the companion Julia examples in the parent exercise folder (`../julia/`). Use the Julia code if you want a small algorithmic implementation rather than the production-quality Python packages.

Install (recommended using the project venv)

```bash
# from repository root
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you prefer to install only what is necessary for this demo:

```bash
pip install numpy scikit-learn factor_analyzer
```

Run the demo

```bash
# from repository root
python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py
```

Notes for instructors / maintainers

- The Python script intentionally uses the well-tested `factor_analyzer` package for factor analysis. If you want an in-repo pure-Python fallback, see the Julia companion folder for a compact eigen-based implementation and consider porting it to Python as a small teaching helper.

- If you change dependencies, update `requirements.txt` at the repository root so the environment setup remains consistent for students.

Contact

- For questions about this exercise, open an issue or contact the course maintainer listed in the repository README.
