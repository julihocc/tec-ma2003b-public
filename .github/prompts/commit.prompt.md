# Robust Commit Prompt

Use this checklist and commit message template to create clear, traceable commits.

## Checklist (run before committing)

- Create & activate venv if needed: assume `.venv` at repo root.
- Run tests: `.venv/bin/python -m pytest -q`
- Format code: `.venv/bin/python -m pip install -r requirements.txt && black .`
- Lint: `flake8 .`
- Update docs or `CHANGELOG.md` if needed.
- Inspect staged changes: `git diff --staged`

## Commit message template

- Header: `type(scope): short summary (<=72 chars)`
  - `type`: feat, fix, docs, style, refactor, perf, test, chore
  - `scope`: optional module/package affected
- Body: blank line + detailed motivation, what changed, and high-level approach
- Footer: references, breaking changes, and related issue IDs

### Example

```
feat(utils/logger): stop propagation by default

Ensure logger.propagate is false so logs do not duplicate when used in
scripts. This prevents duplicate messages when a root logger is configured.

Refs: #123
BREAKING CHANGE: logger API now requires explicit propagation handling
```

### Quick shell snippet (zsh)

Copy and run this before committing to run tests, format, lint and inspect staged changes.

```bash
#!/usr/bin/env zsh
set -e
source .venv/bin/activate
.venv/bin/python -m pytest -q
.venv/bin/python -m pip install -r requirements.txt
black .
flake8 .
git add -A
git status --porcelain
git diff --staged
echo "Now run: git commit -e"  # Opens editor to fill the template above
```

## Last recorded commit (branch `notas-de-clase`)

- Short SHA: `fb4b0bd`
- Header: `refactor(content): move course materials into \`beamers/\` and update docs`
- Body:

  Reorganize the repository layout by relocating course contents from
  `contents/` into the structured `beamers/` directory. This keeps each
  chapter/exercise grouped (latex, python, julia, reports) and makes the
  repository layout clearer for students and CI tooling.

  Also updated repository metadata and docs: small edits to `.github/*`
  and `CLAUDE.md` to reflect the new structure. Files were moved with
  history preserved where possible; total ~68 files changed (mostly
  renames/moves and minor doc edits).

  No functional code changes were made. This is purely a repository
  restructure and documentation cleanup.

---

Use this prompt when asking Copilot (or contributors) to generate commit
messages for repository restructures or documentation cleanups. Adapt the
`type` and `scope` as appropriate for the change.
