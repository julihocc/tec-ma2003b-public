---
mode: agent
---

- Execute .github/prompts/tag-new-version.prompt.md to tag the new version in Git and push the tags.
- Also tag this version as 'latest'
- Merge this release into main branch if not already done.
- Create a new release on GitHub with release notes summarizing the changes in this version.

