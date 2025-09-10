---
mode: agent
—

- Execute .github/prompts/commit.prompt.md to commit the changes in suitable chunks to maintain a clean git history.
- Check for the recent history commit messages to identify the last version bump.
- Update the documentation accordingly.
- Rewrite README files accross the repo to reflect the new version.
- Ensure the version in all relevant files (e.g., `pyproject.toml`, `setup.py`, `__init__.py`) is consistent.
- Update any AI agent instructions to reflect the new version.
- Update AI Manifest files if applicable. If there are no manifest files, create one.
- Create a new commit with the updated documentation and version changes.
- Tag the new version in Git and push the changes.

