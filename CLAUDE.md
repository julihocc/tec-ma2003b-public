# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MA2003B is an academic course repository for "Application of Multivariate Methods in Data Science." This is an **educational codebase** focused on teaching multivariate statistical techniques through interactive examples and real-world datasets.

## Development Setup

**Essential setup pattern:**
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode (required for utils imports)
pip install -e .

# Core dependencies are in pyproject.toml, but quick start:
pip install numpy pandas matplotlib scikit-learn jupyter factor-analyzer seaborn
```

## Key Commands

**Testing:**
```bash
.venv/bin/python -m pytest -q
```

**Code quality:**
```bash
ruff check . && ruff format .
```

**Running examples:**
```bash
# Standard workflow: fetch data, then analyze
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/fetch_invest.py
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/invest_fa.py
```

**Convert Jupyter notebooks:**
```bash
jupytext --to ipynb lessons/4_Factor_Analysis/code/*/*.py
```

## Architecture

**Core structure:**
- `lessons/X_Topic/` - Chapter materials with presentations and code examples
- `utils/` - Shared utilities package (logger, common functions)
- `scripts/` - Data synchronization and maintenance tools
- `evaluations/` - Assessment materials (private submodule)

**Code organization pattern:**
- Each lesson has `beamer/` (presentations) and `code/` (examples)
- Each example follows: `fetch_*.py` → `*_fa.py` + `*_pca.py`
- Examples generate output files (plots, reports) alongside scripts

## Essential Development Patterns

**1. Interactive code structure (py-percent cells):**
```python
# %%
# Data loading and preprocessing

# %% [markdown]
# ## Analysis Section Title

# %%
# Statistical analysis
```

**2. Always use centralized logging:**
```python
from utils import setup_logger
logger = setup_logger(__name__)
logger.info("Analysis starting...")  # Never plain print()
```

**3. Robust file paths:**
```python
from pathlib import Path
script_dir = Path(__file__).resolve().parent
data_file = script_dir / "data.csv"
output_file = script_dir / "results.png"
```

**4. Factor Analysis workflow (6-step pattern):**
1. Assumptions Testing (KMO, Bartlett's sphericity)
2. Factor Retention (Kaiser criterion, scree plot)
3. Extraction (Principal/ML methods)
4. Rotation (Varimax/Promax comparison)
5. Interpretation (loadings matrix, communalities)
6. Validation (factor scores, residuals)

## Key Dependencies

**Core scientific stack:**
- `numpy>=1.24.0`, `pandas>=2.0.0`, `matplotlib>=3.8.0`
- `scikit-learn>=1.3.0`, `seaborn>=0.12.0`
- `factor-analyzer>=0.5.1` (specialist FA package)

**Educational tools:**
- `txttoqti` (QTI quiz generation)
- `jupytext` (notebook conversion)

## Working with Examples

**Current active domains (Chapter 4 Factor Analysis):**
- **Finance:** `invest_example/` - European stock market data
- **Astronomy:** `kuiper_example/` - Kuiper Belt orbital dynamics
- **Healthcare:** `hospitals_example/` - Hospital quality assessment
- **Education:** `educational_example/` - Student assessment data

**Chapter 5 (Discriminant Analysis) in development:**
- **Marketing:** `marketing_segmentation/` - Customer segmentation
- **Quality Control:** `quality_control/` - Manufacturing defects
- **Sports:** `sports_analytics/` - Player performance classification

## Submodule Management

The `evaluations/` directory contains assessment materials as a private submodule:
```bash
# Initialize on first clone
git submodule update --init --recursive

# Update evaluations
cd evaluations && git pull origin main && cd ..
git add evaluations && git commit -m "update evaluations submodule"
```

## Code Conventions

- **Self-documenting:** Scripts generate human-readable output files
- **Standalone:** Examples work independently with embedded data dictionaries
- **Comparative:** Always compare PCA vs Factor Analysis on same datasets
- **Reproducible:** Fixed random seeds, deterministic outputs
- **Educational-first:** Code optimized for learning, not production performance