```instructions
# AI coding agent instructions for this repository

Purpose: give a concise, actionable orientation so an AI coding agent can be productive quickly in this repo.

Quick start
- Create and activate the repository virtualenv (the project uses a local `.venv`):
  ## AI coding agent instructions for this repository

  Purpose: short, actionable guidance so an AI coding agent can be productive quickly.

  Quick start
  - Create and activate the repo virtualenv (this project uses a local `.venv`):
    - python3 -m venv .venv
    - source .venv/bin/activate
  - Prefer editable install so scripts can import package modules:
    - pip install -e .
  - Run tests from repo root:
    - .venv/bin/python -m pytest -q

  Repo snapshot (big picture)
  - This repo holds MA2003B course materials under `contents/1_Regression_Analysis/`. Each exercise folder typically contains: `*_practice.py`, `*.tex`, and `*_report.txt`.
  - Small utility code lives in `utils/` (exported via `utils/__init__.py`). Use these utilities instead of adding ad-hoc helpers.
  - Convenience scripts live in `scripts/` (not production pipelines). `scripts/pull_data.py` references a local machine path and is a local helper.

  Key files & patterns
  - `utils/logger.py`: single logger setup function `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`. It avoids duplicate handlers and sets `logger.propagate = False`.
  - Tests: lightweight pytest tests sit next to modules (see `utils/test_logger.py`). They use `tmp_path` and fixtures like `capsys`.
  - Packaging: `setup.py` exists (legacy). Prefer editable install or add `pyproject.toml` if modernizing packaging.

  Developer workflows & commands (concrete)
  - Create venv, activate, editable install, run tests:
    - python3 -m venv .venv
    - source .venv/bin/activate
    - pip install -e .
    - .venv/bin/python -m pytest -q
  - Run convenience scripts with the venv python to ensure imports work:
    - .venv/bin/python scripts/pull_data.py

  Project conventions and cautions (do not change lightly)
  - Preserve exercise folder structure inside `contents/1_Regression_Analysis/` — do not move `.tex` or `_report.txt` files when adding code.
  - Avoid changing machine-specific paths in `scripts/pull_data.py`; if you must, add an environment variable override (`MA2003B_ORIGIN_PATH`) and update tests.
  - Add new utilities under `utils/` and export them in `utils/__init__.py`.

  Integration points & dependencies
  - No central requirements file exists. If you add runtime or dev dependencies, add `requirements.txt` or `pyproject.toml` and document install steps in README.
  - There are no external network integrations; `pull_data.py` reads local data paths only.

  When making changes
  - Update or add tests alongside code changes and run pytest locally before opening a PR.
  - If you modify `utils/logger.py`, update `utils/test_logger.py` to reflect behavior changes.
  - Keep edits minimal and focused; maintain the course content layout.

  Example small tasks an agent might perform
  - Replace the hard-coded `ORIGIN_PATH` in `scripts/pull_data.py` with an env var fallback (`MA2003B_ORIGIN_PATH`) and log a clear message when missing.
  - Add `requirements.txt` with `pytest` and any needed deps; document `pip install -r requirements.txt` in README.

  If you update this file
  - Merge instead of overwrite; keep the file concise (20–50 lines) and repository-specific.

  Questions or missing info
  - If anything here is unclear or you want CI/packaging templates added, tell me which parts you'd like expanded and I will update this file.

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
