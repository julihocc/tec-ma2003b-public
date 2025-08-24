---
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
