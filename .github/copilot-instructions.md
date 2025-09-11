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
# AI coding agent instructions — tec-ma2003b-public

Purpose: concise, actionable guidance so an AI coding agent can be productive quickly.

Quick start (common developer flow)
- Create & activate venv:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Install package editable so practice scripts import local modules:
  ```bash
  pip install -e .
  ```
- Run tests from repo root:
  ```bash
  .venv/bin/python -m pytest -q
  ```

Repo layout (big picture)
- `lessons/` — course content per chapter. Each chapter contains `lesson/`, `practice/` (exercises), and example `code/` folders.
- `evaluations/` — comprehensive business case studies with rubrics, templates, and assessment frameworks.
- `utils/` — shared helpers; key file: `utils/logger.py` (`setup_logger(...)`) used across practice scripts.
- `scripts/` — automation helpers (e.g., `scripts/pull_data.py`); some use absolute paths and expect env overrides.

Key workflows & concrete commands
- Run one practice script:
  ```bash
  .venv/bin/python lessons/4_Factor_Analysis/code/invest_example/invest_example.py
  ```
- Convert `.py` to notebook with jupytext (project uses py-percent cells):
  ```bash
  jupytext --to ipynb lessons/**/*.py
  ```
- Compile Beamer slides (run twice):
  ```bash
  cd lessons/4_Factor_Analysis/lesson && pdflatex factor_analysis.tex
  ```

Project conventions (follow these exactly)
- Practice scripts should write a human-readable report file next to the script (not only print). See `utils/test_logger.py` and practice examples.
- Use the shared logger:
  ```py
  from utils.logger import setup_logger
  logger = setup_logger(__name__)
  ```
  The helper sets `propagate=False`; prefer it over ad-hoc loggers.
- Keep `lesson/` `.tex` and `_report` artifacts and folder layout unchanged — other materials reference these paths.

Style & interactive patterns (code authorship details)
- Scripts use py-percent cell markers (`# %%` / `# %% [markdown]`) so they run as interactive cells in VS Code. Preserve cell boundaries when editing.
- Prefer commented markdown blocks for rendered text in interactive mode, e.g.:
  ```py
  # %% [markdown]
  # # Title
  # explanatory text...
  ```
- Use `pathlib.Path(__file__).resolve().parent` for file outputs and create parent dirs with `mkdir(parents=True, exist_ok=True)` (pattern used in `pca_example.py` and `invest_example.py`).

Integration notes & gotchas
- `scripts/pull_data.py` uses an absolute OneDrive path; use `MA2003B_ORIGIN_PATH` env var to override in CI.
- LaTeX edits are fragile: avoid breaking `\begin{frame}`/`\end{frame}` or verbatim blocks when programmatically modifying slides.
- When adding runtime deps (e.g., `scikit-learn`, `factor_analyzer`), update `requirements.txt` and mention the change in the chapter README.

Files to inspect first (fast path)
- `utils/logger.py` — logger pattern and helper signature
- `lessons/4_Factor_Analysis/code/*` — examples of practice scripts (PCA, invest) showing py-percent cells and Path usage
- `scripts/pull_data.py` — example with absolute-path gotcha

If you change behavior
- Add or update a lightweight test next to the module (project keeps tests adjacent to code).
- If you introduce external data paths, add CI-friendly env overrides and document them in the chapter README.

When editing this file
- Merge, don't overwrite. Keep guidance short (20–50 lines). If you'd like, I can expand with CI snippets or a script to standardize py-percent styling across lessons.

If anything is unclear or you want a follow-up (eg. auto-format all lesson scripts to this style), tell me which folder to target and I'll implement it.
- Absolute-path helper: `scripts/pull_data.py` — convert hard-coded paths to use `os.getenv('MA2003B_ORIGIN_PATH', '<fallback>')` when parameterizing.

## Style ingestion — learn the maintainer's voice and patterns

When making edits, follow these explicit style and workflow rules so the
agent's output matches the author's expectations.

- Preserve docstrings and teaching text verbatim unless asked; do not rewrite
  protected narrative files (e.g., `objectives_factor_analysis_practice.py`).
- Use py-percent cells (`# %%` / `# %% [markdown]`) and commented markdown for
  educational text. Place short explanatory markdown cells immediately next to
  the code or plot they describe (preamble → code → short interpretation).
- Prefer concise, concrete explanations with example numbers. Example:
  - After PCA prints, add a small markdown cell that shows typical eigenvalues
    and an interpretation (do not append a long appendix at the file end).
- File outputs and figures go next to the script using Path(). Example pattern:
  - `scree_out = script_dir / "kuiper_scree.png"; scree_out.parent.mkdir(...); plt.savefig(scree_out)`
- Always use the repo logger for progress / report lines (`from utils.logger import setup_logger`) and write human-readable report files next to practice scripts (see `utils/test_logger.py`).
- Respect LaTeX fragility: never programmatically break `\begin{frame}`/`\end{frame}` or verbatim blocks; if an edit touches `lesson/*.tex`, run a quick `pdflatex` compile locally to check.
- When adding runtime dependencies (scikit-learn, factor_analyzer, etc.), update `requirements.txt` and add a one-line note in the chapter README beside the changed script.
- Validation rule: after any substantive code edit, run the relevant script or tests in the project's `.venv` and confirm it prints expected outputs and writes expected artifacts. If the edit touches data fetching, ensure `fetch_*` scripts produce CSVs in the expected location.
- Prefer small, local edits over broad refactors. If a larger refactor is needed, summarize the plan and ask one clarifying question before proceeding.

If you want the agent to internalize additional stylistic signals (commit message phrasing, doc tone, preferred variable names), provide 2–3 representative example commits or a short sample note and I will incorporate them into this file.
