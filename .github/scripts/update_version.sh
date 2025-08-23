#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage: $(basename "$0") [--version vX.Y.Z]

Create and push a semantic version git tag for the current HEAD.

Options:
  --version, -v    Create the explicit tag provided (must not already exist)
  --help, -h       Show this help message

Behavior (auto mode):
  - Finds the latest tag matching vX.Y.Z. If none exists, creates v0.1.0.
  - Lists commits since the latest tag and decides bump:
      * BREAK or '!' in messages -> major
      * 'feat' or 'feature' -> minor
      * otherwise -> patch
  - Computes candidate next version. If that tag already exists, increments patch until a free tag name is found.
  - Creates an annotated tag at HEAD and pushes it.

Examples:
  # automatic bump based on commits
  .github/scripts/update_version.sh

  # create an explicit version
  .github/scripts/update_version.sh --version v0.2.0
EOF
}

EXPLICIT_VERSION=""
while [[ ${1:-} != "" ]]; do
  case "$1" in
    -v|--version)
      EXPLICIT_VERSION="$2"; shift 2;;
    -h|--help)
      usage; exit 0;;
    *) echo "Unknown arg: $1"; usage; exit 1;;
  esac
done

git fetch --tags >/dev/null 2>&1 || true

if [[ -n "$EXPLICIT_VERSION" ]]; then
  if git rev-parse "$EXPLICIT_VERSION" >/dev/null 2>&1; then
    echo "Error: tag $EXPLICIT_VERSION already exists." >&2
    exit 1
  fi
  NEW_TAG="$EXPLICIT_VERSION"
  git tag -a "$NEW_TAG" -m "Release $NEW_TAG (explicit)"
  git push origin "$NEW_TAG"
  echo "Created explicit tag: $NEW_TAG"
  exit 0
fi

LATEST_TAG=$(git tag --list 'v*' --sort=-v:refname | head -n1 || true)
if [[ -z "$LATEST_TAG" ]]; then
  echo "No existing semantic tags found. Creating initial tag v0.1.0"
  NEW_TAG="v0.1.0"
  git tag -a "$NEW_TAG" -m "Initial release $NEW_TAG"
  git push origin "$NEW_TAG"
  echo "PREV:none"
  echo "NEW:$NEW_TAG"
  git log -n 10 --pretty=oneline
  exit 0
fi

echo "Latest tag: $LATEST_TAG"

COMMITS=$(git log "$LATEST_TAG"..HEAD --pretty=format:"%h %s")
if [[ -z "$COMMITS" ]]; then
  echo "No new commits since $LATEST_TAG; nothing to tag."; exit 0
fi

# Decide bump type heuristically
BUMP="patch"
if echo "$COMMITS" | grep -E "BREAK|BREAKING|!" >/dev/null; then
  BUMP="major"
elif echo "$COMMITS" | grep -Ei "feat|feature" >/dev/null; then
  BUMP="minor"
fi

# Parse latest tag
ver=${LATEST_TAG#v}
MAJ=${ver%%.*}
rest=${ver#*.}
MIN=${rest%%.*}
PATCH=${rest#*.}
if [[ -z "$PATCH" ]]; then PATCH=0; fi

case "$BUMP" in
  major)
    MAJ=$((MAJ+1)); MIN=0; PATCH=0;;
  minor)
    MIN=$((MIN+1)); PATCH=0;;
  *)
    PATCH=$((PATCH+1));;
esac

NEW_TAG="v${MAJ}.${MIN}.${PATCH}"

# If candidate exists, increment patch until free
while git rev-parse "$NEW_TAG" >/dev/null 2>&1; do
  PATCH=$((PATCH+1))
  NEW_TAG="v${MAJ}.${MIN}.${PATCH}"
done

git tag -a "$NEW_TAG" -m "Release $NEW_TAG (bump: $BUMP)"
git push origin "$NEW_TAG"

echo "PREV:$LATEST_TAG"
echo "NEW:$NEW_TAG"
echo "BUMP_TYPE:$BUMP"
echo "COMMITS:"
echo "$COMMITS"

exit 0
