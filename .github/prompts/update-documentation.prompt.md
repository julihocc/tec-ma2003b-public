---
mode: agent
---

- Execute .github/prompts/commit.prompt.md to commit the changes in suitable chunks to maintain a clean git history.
- Exclude dependencies or virtual enviroments like .venv or node_modules
- Check for the recent history commit messages to identify the last version bump.
- Update the documentation accordingly.
- Rewrite README files accross the repo to reflect the new version.
- Ensure the version in all relevant files (e.g., `pyproject.toml`, `setup.py`, `__init__.py`) is consistent.
- Update any AI agent instructions to reflect the new version.
- Update AI Manifest files if applicable. If there are no manifest files, create one in Markdown Format.
- Place any documentation meant to be read by final user in a folder documentation/
- Place any other documentation meant to be read by another developer or agent in a folder .context/
- Create a new commit with the updated documentation and version changes.
- Tag the new version in Git and push the changes.

