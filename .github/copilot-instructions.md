# AI coding agent instructions for this repository

Purpose: short, actionable guidance so an AI coding agent can be productive quickly.

Quick start
- Create & activate the project venv (this repo uses a local `.venv`):
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install editable package so practice scripts import local modules:
  - pip install -e .
- Run tests from repo root:
  - .venv/bin/python -m pytest -q

Project snapshot & patterns
- Course materials live under `beamers/` (each topic folder contains: practice script, `.tex`, and `_report.txt`).
- Utilities in `utils/` are exported via `utils/__init__.py`. Example: `utils/logger.py` exports `setup_logger(...)` and sets `logger.propagate = False`.
- Small helper scripts live in `scripts/` (e.g., `scripts/pull_data.py` uses a machine path).

Critical, repo-specific commands
- Run one practice script (example):
  - .venv/bin/python beamers/5_Discriminant_Analysis/5.1_Discrimination_for_two_multivariate_normal_populations/discrimination_two_populations_practice.py
- Smoke-test all practice scripts in chapter 5:
  - for f in beamers/5_Discriminant_Analysis/*/*_practice.py; do python "$f" || break; done

Conventions agents must follow
- Preserve the `beamers/` exercise layout (do not move `.tex` or `_report.txt` unintentionally).
- When adding runtime deps, update `requirements.txt` and document install in README.
- Tests sit next to modules (lightweight pytest). Update tests when changing `utils/` utilities.

Integration points & notes
- `scripts/pull_data.py` contains an absolute path; prefer adding `MA2003B_ORIGIN_PATH` as an env-var override when parameterizing. Add tests for both fallback and override if you change it.
- Packaging: `setup.py` is present (legacy). `pyproject.toml` may exist; prefer editable install during development.

If you update this file
- Keep it short and repository-specific. Merge rather than overwrite if maintainers have already customized it.

Questions? Tell me which part you'd like expanded (CI, packaging, or example tests) and I will update this file.
