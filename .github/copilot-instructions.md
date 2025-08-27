---
---
# AI coding agent instructions for tec-ma2003b-public

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
│                                      # • Usage instructions & examples
├── lesson/
│   ├── [chapter].tex                 # Unified Beamer presentation
│   └── [chapter].pdf                 # Compiled slides
└── practice/
    ├── X.1_subtopic_name/            # Independent practice modules
    │   ├── README.md                  # Brief usage instructions
    │   └── [subtopic]_practice.py     # Self-documented executable
    ├── X.2_subtopic_name/
    │   └── ... (same pattern)
    └── X.N_final_subtopic/
```

**Implementation Guidelines:**
- **Chapter README structure**: Follow Factor Analysis README as template (learning objectives, structure outline, prerequisites, key concepts, mathematical notation)
- **Unified presentation**: Single Beamer file with clear section breaks for each subtopic
- **Independent subtopics**: Each practice folder should work standalone with clean modular structure
- **Embedded documentation**: Practice scripts contain purpose, workflow sections, and usage examples
- **Consistent naming**: Always use `X.Y_descriptive_name` pattern
- **Minimal redundancy**: Subtopic READMEs should only contain essential usage info

**Practice Implementation Pattern:**
1. **Create orchestration script** (`[subtopic]_practice.py`):
   - Import from local computation and reporter modules
   - Use centralized logger from utils
   - Coordinate workflow: data → computation → formatting → output
   - Write human-readable report to `*_report.txt`

2. **Create computation module** (`[subject].py`):
   - Define dataclasses for structured results
   - Write pure functions with clear type hints
   - No I/O operations or side effects
   - Focus on statistical/mathematical operations

3. **Create reporter module** (`[subject]_reporter.py`):
   - Functions that take computation results and return formatted strings
   - Handle all output formatting and display logic
   - Clear section headers and educational explanations
# AI coding agent instructions for this repository

Purpose: short, actionable guidance so an AI coding agent can be productive quickly in tec-ma2003b-public.

Quick start (most common developer flow)
- Create & activate the local venv used by the project:
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install editable package so practice scripts import local modules:
  - pip install -e .
- Run tests from repo root:
  - .venv/bin/python -m pytest -q

What this repo contains (big picture)
- Course materials arranged under `beamers/`. Each topic (chapter) folder contains subfolders for exercises with: a `python/` practice script, optional `julia/` examples, `latex/` slides, and a `_report.txt` or `_report.md` output artifact.
- Small utilities under `utils/` (exported via `utils/__init__.py`) provide shared helpers — e.g. `utils/logger.py` exposes `setup_logger(...)` and configures a repository logger used by practice scripts.
- Top-level packaging files: `setup.py`, `pyproject.toml` (optional), and `requirements.txt` drive local development.

Key developer workflows and commands
- Run a single practice script (example):
  - .venv/bin/python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py
- Run a chapter smoke test (example pattern):
  - for f in beamers/5_Discriminant_Analysis/*/*_practice.py; do .venv/bin/python "$f" || break; done
- Install new runtime dependency: add to `requirements.txt` and include a one-line note in the exercise `README.md` under the relevant `python/` folder.

Project-specific conventions (important to follow)
- Preserve the `beamers/` folder layout. Do not move `.tex` files or `_report.txt` artifacts — they are referenced by teaching materials.
- Practice scripts should write human-readable reports to a report file in their folder (e.g. `objectives_factor_analysis_report.txt`) and use the repository logger for informational/errors. Shared logger: `from utils.logger import setup_logger`.
- Tests are lightweight and sit next to modules. When changing `utils/` utilities, update their tests in the same folder.

Integration points and gotchas
- `scripts/pull_data.py` contains an absolute path; prefer parameterizing with `MA2003B_ORIGIN_PATH` env var when changing it and add tests for both fallback and override.
- Packaging: `setup.py` is present (legacy); prefer editable install (`pip install -e .`) for development and tests.
- Some practice scripts support both Python and Julia; the Python scripts may expect `scikit-learn` and `factor_analyzer`. If you add or require these, update `requirements.txt`.

Examples and concrete references
- Shared logger: `utils/logger.py` — create a logger with `setup_logger(__name__)` and call `logger.info(...)` for progress messages; do not replace the global logger behavior unless necessary.
- Report pattern: practice script opens a report file next to the script and writes the demonstration text there (see `beamers/.../objectives_factor_analysis_practice.py`). Keep prints for interactive debugging only; prefer writing reports to files.
- Absolute-path helper: `scripts/pull_data.py` — convert hard-coded paths to use `os.getenv('MA2003B_ORIGIN_PATH', '<fallback>')` when parameterizing.

Additional practical notes (from internal guidance)
- Logger details: `setup_logger(name=None, level=logging.INFO, logfile=None)` is the common helper; it configures stream+file handlers and sets `logger.propagate = False` to avoid duplicated messages — prefer this helper over ad-hoc loggers.
- Conversation exports: save chat/conversation exports to `.claude/backup/conversations/` using a clear name like `YYYY-MM-DD-brief-description.txt` so development history is reproducible and auditable.
- Standard lesson template (short): each topic should follow the `lesson/`, `practice/`, `notes/` layout to keep materials consistent across chapters.

When updating this file
- Merge, do not overwrite. Keep guidance short (20-50 lines). Preserve maintainers' custom notes when present.

If anything is unclear or you want a CI snippet, packaging details, or example test updates added, tell me which section to expand.

---
