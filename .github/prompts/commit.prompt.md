---
mode: agent
---

- Execute instructions given in .github/prompts/summarize-changes.prompt.md
- Realize an strategy to commit these changes incluiding those on submodules
- Commit changes in suitable chunks to maintain a clean history.
- Rely on chat history to compose commits.
- Use descriptive commit messages that summarize the changes made.
- Sync the submodules 