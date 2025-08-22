# AI coding agent instructions for this repository

Purpose: give a concise, actionable orientation so an AI coding agent can be productive quickly in this repo.

Quick start (what humans and agents should run locally)
- Create and activate the project virtualenv (this repo uses a local `.venv`):
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install test tooling if there is no requirements file: pip install pytest
- Run unit tests: python -m pytest -q

Big picture
- This repository is a course materials repo for MA2003B (multivariate methods). Major content is organized under `1_Regression_Analysis/` with subfolders for exercises, reports, and notebooks/text files.
- There is a small `scripts/` folder (e.g., `scripts/pull_data.py`) for convenience scripts. That script currently contains a hard-coded Windows/OneDrive `ORIGIN_PATH` and raises FileNotFoundError if missing — treat it as a local helper, not canonical data ingestion logic.
- Small reusable utilities live in `utils/` (for example `utils/logger.py` implementing `setup_logger`). Prefer using those utilities rather than adding ad-hoc equivalents.

Key files and patterns (reference examples)
- `utils/logger.py`: provides `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`.
  - Behavior notes: it returns an existing logger if handlers are already present; it sets `logger.propagate = False` to avoid duplicated output.
  - Tests for it are under `utils/test_logger.py` showing how to capture stream and file output in pytest.
- `scripts/pull_data.py`: contains an absolute OS-specific path. Don't assume it will run on CI; modify only when you also add a cross-platform config (e.g., environment variable or CLI arg). Example line: ORIGIN_PATH = "/mnt/c/.../OneDrive ..."
- Exercise folders (e.g. `1.1_Simple_Linear_Regression/`) contain three artifacts per exercise: a practice script `.py`, a `.tex` file, and a `_report.txt` — when adding new exercises follow the same pattern.

Developer workflows and commands
- Use a local virtualenv at repository root named `.venv` (this is already used in development). Activate it before installing packages.
- Tests: use pytest and place tests next to the module they exercise (see `utils/test_logger.py`). Run `python -m pytest -q` from repo root.
- Running small scripts: call them through the `.venv` Python executable or activate the venv first. Example: `.venv/bin/python scripts/pull_data.py` (but note the script may raise if the path is not present).

Conventions and expectations for code changes
- Keep course content files (tex, reports) in their exercise directories — avoid moving them unless reorganizing the course structure.
- Add small utilities under `utils/` and expose them via `utils/__init__.py` (current pattern: `from .logger import setup_logger; __all__ = ['setup_logger']`).
- Tests should be lightweight and fast. Use `tmp_path` and pytest fixtures for filesystem tests (see existing tests).
- Avoid editing machine-specific constants (like ORIGIN_PATH) unless you add a configurable alternative (environment variable, CLI flag, or config file) and update tests accordingly.

Integration points & external dependencies
- There is no central requirements file; packages are installed per-environment during development. If you add dependencies, add a `requirements.txt` or `pyproject.toml` and document installation in this file.
- `scripts/pull_data.py` is the only script that references an external filesystem location. Treat network or external system integration as out-of-scope unless you add explicit configuration.

What an agent should do when making changes
- Preserve existing structure and naming in `1_Regression_Analysis/` when adding new exercises.
- When adding runtime dependencies, update `requirements.txt` and document installation steps in README and this file.
- If you change `utils/logger.py` behavior, update `utils/test_logger.py` accordingly and run pytest locally.
- Before opening a PR, run `python -m pytest -q` and ensure no tests fail.

When something is unclear
- If a script or path looks machine-specific (like `ORIGIN_PATH` in `scripts/pull_data.py`), ask a human whether to parameterize it or keep it as a local helper.
- If you need to introduce CI or standardize dependency management, propose adding `requirements.txt` or a simple GitHub Actions workflow and include the proposed YAML as part of the PR.

Example quick edits an agent might perform
- Replace hard-coded `ORIGIN_PATH` with reading from an environment variable `MA2003B_ORIGIN_PATH` and keep the previous behavior as a fallback; add tests to verify fallback and env override.
- Add a `requirements.txt` containing `pytest` and any new dependencies and update README with `pip install -r requirements.txt`.

If you update this file
- Merge existing content rather than overwrite if a maintainer has already added agent guidance.
- Keep this file short (20-50 lines) and focused on actionable, repo-specific knowledge.

Ask for feedback: If any section is unclear or I missed an important project-specific workflow, tell me which file or task you expect agent help with and I'll iterate.
