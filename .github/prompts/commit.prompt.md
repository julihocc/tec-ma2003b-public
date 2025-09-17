---
mode: agent
---

- Execute instructions given in .github/prompts/summarize-changes.prompt.md
- Realize an strategy to commit these changes incluiding those on submodules
- Utilize the dev branch for each submodule to avoid conflicts with main branch
- If needed, create dev branches on submodules to commit changes
- Commit changes in suitable chunks to maintain a clean history.
- Rely on chat history to compose commits.
- Use descriptive commit messages that summarize the changes made.
- Sync the submodules 