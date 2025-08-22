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
        - If there are new commits, determine the appropriate next version and create the tag at HEAD.
            Use the following conservative heuristic unless instructed otherwise:
                * If commit messages include BREAK or BREAKING or '!' -> bump MAJOR.
                * Else if commit messages include 'feat' or 'feature' -> bump MINOR.
                * Otherwise -> bump PATCH.
        - Compute the candidate next version (semantic). If the candidate tag name already exists, increment the patch number until a free tag name is found (do not overwrite tags).
        - Create an annotated tag at HEAD with the chosen version and push it to the remote.
4. Push the new tag to the remote repository.
5. Output a summary: previous version, new version, and commits included in the new version.

Be sure to follow semantic versioning and do not overwrite existing tags.

Extras / overrides:
- If the caller provides an explicit version (e.g., v0.2.0), validate it does not exist and create that tag instead of auto-calculating.
- Print the chosen bump type (major/minor/patch) and the short list of included commits (hash + subject).
- If no commits are found since the latest tag, print a clear message and do not create a duplicate tag.