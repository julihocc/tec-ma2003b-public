---
mode: agent
---
You are tasked with updating the repository version using Git tags.

Instructions:
1. Check for existing version tags (format: vX.Y.Z).
2. If no version tags exist, create an initial version tag (e.g., v0.1.0) at the current HEAD.
3. If version tags exist:
    - Identify the latest version tag.
    - List all commits since the latest version tag.
    - If there are new commits, determine the appropriate next version (e.g., increment patch/minor/major as needed).
    - Create a new version tag at the latest commit.
4. Push the new tag to the remote repository.
5. Output a summary: previous version, new version, and commits included in the new version.

Be sure to follow semantic versioning and do not overwrite existing tags.