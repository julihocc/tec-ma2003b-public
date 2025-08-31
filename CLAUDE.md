# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the MA2003B - Application of Multivariate Methods in Data Science course repository, focusing on analyzing multidimensional databases using multivariate statistical techniques.

**Course Topics:** Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression.

## Development Setup

Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib scikit-learn jupyter jupytext pytest
pip install -e .
```

## Key Commands

**Run tests:**
```bash
.venv/bin/python -m pytest -q
```

**Compile presentations:**
```bash
cd lessons/4_Factor_Analysis/beamer
pdflatex factor_analysis_presentation.tex
# Run twice for proper cross-references
pdflatex factor_analysis_presentation.tex
```

**Run code examples:**
```bash
# Fetch data first (for examples that need external data)
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/fetch_invest.py

# Current working examples
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/invest_example.py
.venv/bin/python lessons/4_Factor_Analysis/code/hospitals_example/hospitals_example.py
.venv/bin/python lessons/4_Factor_Analysis/code/kuiper_example/kuiper_example.py
.venv/bin/python lessons/4_Factor_Analysis/code/pca_example/pca_example.py
```

**Convert Python scripts to notebooks:**
```bash
jupytext --to ipynb lessons/4_Factor_Analysis/code/*/*.py
```

**Data synchronization:**
```bash
.venv/bin/python scripts/pull_data.py
# Override source: MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
```

## Repository Structure

**Course Materials:**
- `lessons/4_Factor_Analysis/` - Factor analysis chapter (current active content)
  - `beamer/` - LaTeX presentation source and compiled PDF
  - `code/` - Working examples with py-percent cells: `invest_example/`, `hospitals_example/`, `kuiper_example/`, `pca_example/`
  - Chapter README provides comprehensive learning guide

**Utilities:**
- `utils/` - Shared utilities package with centralized logging
- `utils/logger.py` - `setup_logger()` function with duplicate prevention and `propagate = False`
- `utils/test_logger.py` - Unit tests for logger functionality

**Scripts:**
- `scripts/pull_data.py` - Data synchronization from OneDrive source to local `backup/ma2003b/`

**Documentation:**
- `documentation/` - Course planning documents and timeline
- `backup/ma2003b/` - Synchronized course materials from external source

## Key Architecture Insights

**Package Structure:** Configured as editable Python package (`ma2003b-course`) enabling `from utils import setup_logger` imports.

**Centralized Logging:** All scripts use `setup_logger()` from `utils/logger.py` with duplicate prevention and `propagate = False`.

**Interactive Development:** Code examples use py-percent cells (`# %%` and `# %% [markdown]`) for VS Code/Jupyter integration.

**Data Workflow Separation:** Fetch scripts separate from analysis scripts (e.g., `fetch_invest.py` + `invest_example.py`).

**Chapter Organization:** Single comprehensive README and consolidated presentation covering all subtopics.

## Development Conventions

**File Organization:**
- Course materials in `lessons/` folders
- New utilities in `utils/` and exported via `utils/__init__.py`
- Tests next to modules (e.g., `utils/test_logger.py`)

**Code Architecture (Undergraduate Focus):**
- Use py-percent cells (`# %%` and `# %% [markdown]`) for interactive development
- Use `pathlib.Path(__file__).resolve().parent` for file operations
- Separate data fetching from analysis (e.g., `fetch_*.py` + `*_example.py`)
- Always use centralized logger: `from utils import setup_logger`

**Chapter Structure (Current Model):**

```
X_Chapter_Name/
├── README.md                          # Comprehensive learning guide
├── beamer/                            # Single consolidated presentation
│   ├── [chapter]_presentation.tex    # Beamer source
│   └── [chapter]_presentation.pdf    # Compiled slides
└── code/                              # Working examples with py-percent cells
    ├── example_name/
    │   ├── fetch_data.py             # Data fetching script
    │   ├── example.py                # Main analysis with # %% cells
    │   ├── data.csv                  # Downloaded/generated data
    │   └── *.png                     # Generated figures
    └── ...
```

**Key Principles:**
- Single comprehensive README per chapter
- Consolidated presentation covering all subtopics  
- Interactive examples with py-percent cells
- Self-contained scripts with embedded documentation
- Pure functions with type hints and docstrings

## Development Guidelines

**Code Quality:**
- Use centralized `setup_logger()` from utils
- Export new utilities through `utils/__init__.py`
- Use type hints and docstrings for clarity
- Follow existing error handling patterns

**Interactive Development:**
- Use py-percent cells for VS Code/Jupyter compatibility
- Keep statistical concepts clear - avoid over-engineering
- Generate output files next to scripts using pathlib
- Write human-readable report files, not just console output

**Testing:**
- Run tests after changes: `.venv/bin/python -m pytest -q`
- Use pytest with `tmp_path` fixtures for filesystem tests

## Current Repository State

**Active Content:**
- ✅ **Chapter 4**: Factor Analysis - Complete presentation and working examples
  - Location: `lessons/4_Factor_Analysis/`
  - Examples: `invest_example/`, `hospitals_example/`, `kuiper_example/`, `pca_example/`

**Future Chapters:** Multivariate Analysis, PCA, Discriminant Analysis, Cluster Analysis, Multivariate Regression

## Important Notes

- `scripts/pull_data.py` uses machine-specific paths; override with `MA2003B_ORIGIN_PATH` environment variable
- Dependencies in `requirements.txt` include complete scientific computing stack
- Use `pdflatex` twice for proper LaTeX cross-references
- Always use virtual environment with `pip install -e .` for development
- Scripts should write human-readable report files, not just console output
- After changes made, update the documentation given in the README.md files