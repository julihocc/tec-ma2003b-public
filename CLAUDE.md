# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the MA2003B - Application of Multivariate Methods in Data Science course repository, an intermediate mathematics course focusing on analyzing multidimensional large databases using multivariate statistical techniques.

**Course Topics:** Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression.

## Development Setup

Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Key Commands

**Run tests:**
```bash
.venv/bin/python -m pytest -q
```

**Run practice scripts:**
```bash
# Single Python script (organized structure)
cd contents/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/python
python discrimination_two_populations_practice.py

# Single Julia script (organized structure)  
cd contents/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/julia
julia discrimination_two_populations_practice.jl

# All Python scripts in a section (legacy structure)
for f in contents/5_Discriminant_Analysis/*/*_practice.py; do
  echo "--- running $f ---"
  python "$f" || break
done

# All Python scripts in organized structure
for f in contents/5_Discriminant_Analysis/*/python/*_practice.py; do
  echo "--- running $f ---"
  python "$f" || break
done
```

**Data pull script:**
```bash
.venv/bin/python scripts/pull_data.py
# Override source path: MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
```

## Repository Structure

**Course Materials:**
- `contents/1_Regression_Analysis/` - Regression analysis exercises and materials
- `contents/5_Discriminant_Analysis/` - Discriminant analysis exercises and materials
- Each exercise folder contains organized subfolders (see Course Content Structure below)

**Utilities:**
- `utils/` - Shared utilities package with logging functionality (exported via `__init__.py`)
- `utils/logger.py` - Centralized logging: `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`
  - Supports both stream and file logging, prevents duplication with `propagate = False`
- `utils/test_logger.py` - Unit tests for logger functionality

**Scripts:**
- `scripts/pull_data.py` - Data synchronization script that copies course materials from OneDrive source to local `backup/ma2003b/` directory

**Documentation:**
- `documentation/` - Course planning documents including hour allocation tables
- `backup/` - Contains course materials copied from the OneDrive source

## Development Conventions

**File Organization:**
- Exercise materials stay in their respective folders under `contents/`
- New utilities go in `utils/` and are exported via `utils/__init__.py`
- Tests sit next to modules (e.g., `utils/test_logger.py`)

**Testing:**
- Use pytest with `tmp_path` fixtures for filesystem tests
- Run tests after changes: `.venv/bin/python -m pytest -q`

**Package Management:**
- Use editable install (`pip install -e .`) for development
- Dependencies: `requirements.txt` contains minimal runtime/dev dependencies
- `pyproject.toml` defines package metadata

**Course Content Structure:**
**IMPORTANT: Use organized folder structure for new/refactored exercises:**

```
X.Y_Topic_Name/
├── README.md                          # Organization guide and learning objectives
├── [topic]_report.txt                 # Exercise description and hints  
├── 📁 latex/                          # LaTeX presentation files
│   ├── [topic].tex                    # Beamer presentation source
│   ├── [topic].pdf                    # Compiled presentation
│   └── ... (LaTeX auxiliary files)
├── 📁 python/                         # Python implementation
│   ├── [topic]_practice.py           # Main practice script (simplified for 2-hour class)
│   └── test_[topic].py               # Unit tests
└── 📁 julia/                          # Julia pseudocode version
    └── [topic]_practice.jl           # Mathematical pseudocode implementation
```

**Legacy structure (for reference only):**
- `[topic]_practice.py` - Python implementation
- `[topic].tex` - LaTeX beamer presentation  
- `[topic]_report.txt` - Exercise description and hints
- `test_[topic].py` - Unit tests

**When refactoring existing exercises:** Create subfolders (`latex/`, `python/`, `julia/`) and organize files by type for cleaner structure. Always include a README.md explaining the organization.

**Key Utilities:**
- `setup_logger()` - Configured logger with duplicate handler prevention and `propagate = False`
- Use existing utilities instead of creating ad-hoc helpers

## Development Guidelines

- **All scripts should use** the centralized `setup_logger()` function from utils
- **When adding new utilities**, export them through `utils/__init__.py`
- **Follow existing error handling patterns** seen in `pull_data.py`
- **Use type hints** as demonstrated in the logger module
- **Preserve existing course content structure** when making changes
- **Always use the project's virtual environment** for consistency

## Important Notes

- The `scripts/pull_data.py` contains machine-specific OneDrive paths and may not work on all systems
- Some practice scripts use optional libraries (numpy, scipy, scikit-learn)
- Course covers 7 main topics: Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression