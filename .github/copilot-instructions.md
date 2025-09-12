---
---
# AI coding agent instructions for tec-ma2003b-public

**Version:** 1.5.0

Purpose: short, actionable guidance so an AI coding agent can be productive quickly in this repository.

Quick start (most common developer flow)
- Create & activate the local venv used by the project:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Install the package in editable mode so practice scripts import local modules:
  ```bash
  pip install -e .
  ```
- Run tests from repo root:
  ```bash
  .venv/bin/python -m pytest -q
  ```

What this repo contains (big picture)
- `beamers/` — course materials grouped by topic/chapter. Each chapter contains subfolders with `python/` practice scripts, optional `julia/`, `latex/` slides, and a `_report.txt` or `_report.md` artifact used by teaching materials.
- `utils/` — small shared utilities exported via `utils/__init__.py`. Important file: `utils/logger.py` (use `setup_logger(...)`).
- `scripts/` — helper scripts (e.g., `scripts/pull_data.py`) that may use absolute paths; prefer environment parametrization.

Key developer workflows & concrete commands
- Run a single practice script (example):
  ```bash
  .venv/bin/python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py
  ```
- Compile Beamer slides (example): run `pdflatex` twice on the `.tex` file in the lesson folder (e.g. `beamers/4_Factor_Analysis/lesson/factor_analysis.tex`).
- Add runtime dependency: update `requirements.txt` and add a one-line note in the exercise `README.md` inside the relevant `python/` folder.

Project-specific conventions (follow these exactly)
---
# AI coding agent instructions — tec-ma2003b-public

Purpose: Short, actionable guidance so an AI coding agent can start delivering value in this repo immediately.

Quick start (most common dev flow)
- Create & activate venv: `python3 -m venv .venv && source .venv/bin/activate`
- Install package editable: `pip install -e .`
- Run tests: `.venv/bin/python -m pytest -q`

Essential structure (high-level)
- `lessons/` — course content organized by chapter (presentation in `lesson/`, exercises in `practice/`).
- `utils/` — shared utilities (important: `utils/logger.py` exposes `setup_logger(...)`).
- `scripts/` — helpers (notably `scripts/pull_data.py` which uses an absolute OneDrive path; prefer env override).

Key workflows & concrete commands
- Run one practice script: `.venv/bin/python lessons/4_Factor_Analysis/practice/4.1_objectives/*_practice.py`
- Compile slides: `cd lessons/4_Factor_Analysis/lesson && pdflatex factor_analysis.tex` (run twice). Use `xelatex`/`lualatex` if theme requests Fira fonts.
- Update deps: add package to `requirements.txt` and mention it in the exercise README next to the modified script.

Project-specific conventions (do this exactly)
- Practice scripts must write a human-readable report file next to the script (not only prints). See existing pattern in `utils/test_logger.py` and practice examples.
- Always use the repo logger: `from utils.logger import setup_logger; logger = setup_logger(__name__)` (logger sets `propagate=False`).
- Preserve `lesson/` `.tex` and `_report` artifacts and folder layout — other teaching material references assume these paths.

Integration notes & gotchas
- `scripts/pull_data.py` uses an absolute path; use `MA2003B_ORIGIN_PATH` to override when running CI or other machines.
- LaTeX slides often include `frame` + `verbatim` blocks that are fragile; programmatic edits must not break `\begin{frame}`/`\end{frame}` or verbatim boundaries.
- Some practice examples require optional scientific packages (e.g., `scikit-learn`, `factor_analyzer`, `lavaan` for R). If you introduce them, update `requirements.txt` and note it in the chapter README.

Quick examples (patterns to follow)
- Logger: `logger = setup_logger(__name__); logger.info('writing report to %s', report_path)`
- Parametrized pull: `MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py`
- Practice script skeleton: `*_practice.py` orchestrates, imports pure `*_analysis.py` functions, and writes `*_report.txt` beside the script.

When editing this file
- Merge, don't overwrite maintainers' custom notes. Keep this doc short (20–50 lines) and codebase-specific.

If anything is unclear or you want CI snippets, smoke-tests for a chapter, or a LaTeX build job, tell me which chapter and I will add them.
---
- **Logger Usage**: Always use `from utils import setup_logger` and call `setup_logger(__name__)` for consistent logging across scripts
- Course covers 7 main topics: Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression

## Chapter Template (Factor Analysis Model)

When creating new chapters, use this organizational structure:

```
X_Chapter_Name/
├── README.md                          # Complete chapter learning resource
│                                      # • Learning objectives & outcomes
│                                      # • Subtopic structure & overview
│                                      # • Prerequisites & key concepts  
# AI coding agent instructions for tec-ma2003b-public

**Version:** 2.0.0

Purpose: concise, actionable guidance so an AI coding agent can be productive immediately in this multivariate statistics course repository.

## Quick Start (Most Common Dev Flow)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
.venv/bin/python -m pytest -q
```

## Repository Architecture (Big Picture)

- **`lessons/`** — course content per chapter with `beamer/` presentations, `code/` examples, and comprehensive README
- **`evaluations/`** — git submodule (private repo: tec-ma2003b-evaluations) containing business case studies, templates, and rubrics
- **`utils/`** — shared package with centralized logging (`setup_logger`) and utilities  
- **`scripts/`** — automation helpers like `pull_data.py` (uses absolute paths, override with `MA2003B_ORIGIN_PATH`)

## Essential Workflows & Commands

**Run example scripts:**
```bash
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/invest_fa.py
```

**Handle evaluations submodule (branch-dependent):**
```bash
# Initialize submodule (branches with submodule)
git submodule update --init --recursive

# Switch between submodule/regular file branches
git submodule deinit evaluations  # before switching to non-submodule branch
```

**Convert to notebooks (project uses py-percent cells):**
```bash
jupytext --to ipynb lessons/**/*.py
```

**Compile presentations (Typst preferred, LaTeX legacy):**
```bash
cd lessons/4_Factor_Analysis/beamer
typst compile factor_analysis_presentation.typ
```

## Project Conventions (Follow Exactly)

**Logger Pattern:**
```python
from utils import setup_logger
logger = setup_logger(__name__)  # sets propagate=False
```

**Interactive Development:**
- Use py-percent cells (`# %%` / `# %% [markdown]`) for VS Code/Jupyter integration
- Place explanatory markdown cells immediately next to related code
- Use `pathlib.Path(__file__).resolve().parent` for robust file operations

**File Organization:**
- Practice scripts write human-readable report files next to the script (not just console output)
- Generate figures/data in same directory as script: `script_dir / "output.png"`
- Create parent directories: `output_path.parent.mkdir(parents=True, exist_ok=True)`

**Business Case Template Pattern:**
- TODO-driven structure for student completion
- Reflection questions interspersed with code sections  
- Executive visualization and recommendation functions
- Team information section for deliverables

## Integration Notes & Gotchas

**Submodule Management:** `evaluations/` exists as submodule in some branches, regular files in others. Use `git submodule deinit evaluations` before switching to avoid conflicts.

**Path Dependencies:** `scripts/pull_data.py` uses absolute OneDrive paths; override with `MA2003B_ORIGIN_PATH="/path"`.

**LaTeX Fragility:** Never programmatically break `\begin{frame}`/`\end{frame}` or verbatim blocks when editing presentations.

**Dependencies:** When adding packages (scikit-learn, factor_analyzer), update `requirements.txt` and note in chapter README.

## Key Files to Inspect

- `utils/logger.py` — centralized logging pattern
- `lessons/4_Factor_Analysis/code/invest_example/invest_fa.py` — example with py-percent cells
- `evaluations/4_Factor_Analysis/business_case/factor_analysis_business_case_template.py` — business case pattern
- `scripts/pull_data.py` — data synchronization with path override pattern

## Validation Rules

- After code changes: run script and verify expected outputs/artifacts
- Test imports work: `from utils import setup_logger` should succeed
- For evaluation materials: respect TODO structure and reflection question format
- Always validate LaTeX compilation after slide edits
