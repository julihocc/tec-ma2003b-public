# AI coding agent instructions for this repository

Purpose
- Provide a short, actionable orientation so an AI coding agent can be productive quickly in this repo.

Quick start
- Create and activate the project virtualenv (this repo uses a local `.venv`):
  - python3 -m venv .venv
  - source .venv/bin/activate
- Prefer editable install to allow scripts to import package modules during development:
  - pip install -e .
- Run tests from repo root:
  - .venv/bin/python -m pytest -q

Repository snapshot (big picture)
- Course materials for MA2003B live under `contents/` (e.g., `contents/1_Regression_Analysis/`).
- Each exercise folder contains a practice script, a LaTeX source and a short report. New/organized exercises may add `python/`, `latex/`, and `julia/` subfolders.
- Small utilities live in `utils/` and are exported via `utils/__init__.py` (for example `utils/logger.py`).
- Convenience scripts live in `scripts/` (e.g., `scripts/pull_data.py`), and may reference local machine paths.

Key files & patterns
- `utils/logger.py`: exposes `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`; avoid duplicate handlers and set `logger.propagate = False`.
- `scripts/pull_data.py`: uses a machine-specific path by default; prefer an environment variable override `MA2003B_ORIGIN_PATH` if parameterizing it.
- Exercises: follow the existing artifact pattern: `*_practice.py`, `*.tex`, and `*_report.txt` (or use organized subfolders with `python/`, `latex/`, `julia/`).

Developer workflows
- Create venv, activate, install editable package, run tests:
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install -e .
  - .venv/bin/python -m pytest -q
- Run convenience scripts using the venv python to ensure imports work:
  - .venv/bin/python scripts/pull_data.py

Testing and changes
- Add or update tests alongside code changes and run pytest locally before opening a PR.
- Tests are lightweight pytest files colocated with modules (see `utils/test_logger.py`). Use `tmp_path` and fixtures as needed.
- When changing `utils/logger.py`, update `utils/test_logger.py` accordingly.

Packaging and dependencies
- The repo contains a legacy `setup.py`; a `pyproject.toml` and `requirements.txt` may also exist. If you add runtime or dev dependencies, add them to `requirements.txt` and document installation in README.

Conventions and cautions
- Preserve exercise folder structure under `contents/` when adding code or slides; avoid moving `.tex` or `_report.txt` files unless reorganizing the course structure with an explicit plan.
- Avoid changing machine-specific constants in `scripts/pull_data.py` unless you also add a configurable alternative and update tests.
- Prefer using utilities in `utils/` rather than introducing ad-hoc helpers.

Small example tasks an agent might perform
- Replace hard-coded `ORIGIN_PATH` in `scripts/pull_data.py` with an env var fallback `MA2003B_ORIGIN_PATH` and add a log message when missing; add tests for both behaviors.
- Add a `requirements.txt` (e.g., containing `pytest`, `numpy`, `scipy`) and document `pip install -r requirements.txt` in README.
- Create an organized exercise folder (with `python/`, `latex/`, `julia/` subfolders), move legacy files there, and add a short `README.md` explaining structure.

If you update this file
- Merge changes rather than overwrite when maintainers have already added guidance. Keep the file concise (20–50 lines) and repo-focused.

Questions or missing info
- If you want CI templates, packaging modernization, or a different test layout, tell me which part to expand and I will add an updated suggestion or implementation.
