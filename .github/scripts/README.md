
# Update version script

This folder contains helper scripts used by repository maintainers and CI.

## update_version.sh

- Detects the latest semantic tag (vMAJOR.MINOR.PATCH), inspects commits since that tag,
  decides on a bump (major if commit messages contain BREAK or '!', minor if 'feat' present,
  otherwise patch), computes the next free tag name, creates an annotated tag at HEAD,
  and pushes it to the origin remote. Optionally accepts `--version vX.Y.Z` to create a
  specific tag.

## Usage examples

- Automatic bump based on commit messages:

  .github/scripts/update_version.sh

- Create an explicit tag:

  .github/scripts/update_version.sh --version v0.2.0

## CI snippet (GitHub Actions)

Use this in a workflow to create a tag from a merge to main/branch when appropriate.

```yaml
jobs:
  tag_release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run update_version script
        run: .github/scripts/update_version.sh
```

Note: The script will push tags to the `origin` remote. Ensure the workflow has write
permissions to the repository (GITHUB_TOKEN or a deploy key with push rights).
