# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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
# Single script
python contents/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/discrimination_two_populations_practice.py

# All scripts in a section
for f in contents/5_Discriminant_Analysis/*/*_practice.py; do
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
- Each exercise folder contains: `*_practice.py`, `*.tex`, `*_report.txt`, and `test_*.py`

**Utilities:**
- `utils/` - Shared utilities (exported via `__init__.py`)
- `utils/logger.py` - Logger setup: `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`

**Scripts:**
- `scripts/pull_data.py` - Copies course source files to backup directory (machine-specific paths)

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
Each exercise follows the pattern:
- `[topic]_practice.py` - Python implementation
- `[topic].tex` - LaTeX theory notes  
- `[topic]_report.txt` - Exercise description and hints
- `test_[topic].py` - Unit tests (in discriminant analysis sections)

**Key Utilities:**
- `setup_logger()` - Configured logger with duplicate handler prevention and `propagate = False`
- Use existing utilities instead of creating ad-hoc helpers

## Important Notes

- The `scripts/pull_data.py` contains machine-specific paths and may not work on all systems
- Some practice scripts use optional libraries (numpy, scipy, scikit-learn)
- Preserve existing course content structure when making changes
- Always use the project's virtual environment for consistency