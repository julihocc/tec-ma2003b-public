---
mode: agent
---

- Execute .github/prompts/release-new-version.prompt.md to ensure the versioning and documentation are up to date and the new version is tagged in git.
- Build the source and wheel distributions of the package using a tool like `build`.
- Test the new package version locally to ensure it can be installed and functions as expected.
- Publish the new package version to PyPI using `twine`.
- Create a new commit with the build artifacts and push the changes.
- Push the new tags to the remote repository.