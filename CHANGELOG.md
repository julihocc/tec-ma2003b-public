# Changelog

All notable changes to this repository are documented in this file.

## v1.8.0 - 2025-09-23

Highlights:


- Expanded Chapter 5 Discriminant Analysis with new domain examples (sports analytics, quality control)
- Significant pedagogical enhancements to Factor Analysis chapter (clearer slides, modularization of dense content, improved PCA vs FA comparisons)
- Added `factor-analyzer` dependency enabling authentic factor extraction and validation workflows
- Multiple improvements to educational examples: refined PCA and FA scripts, added educational assessment data example, clarified variable naming
- Enhanced AI assistant guidance (`CLAUDE.md`) and extension recommendations for a consistent developer environment
- Evaluations submodule: iterative refinements to competent/outstanding business case solutions and customer satisfaction case materials

Commit Categories (selected):

Features:

- Add discriminant analysis lesson and supporting examples (sports analytics, quality control)
- Add `factor-analyzer` dependency for factor analysis examples
- Implement Factor Analysis on educational data; improve PCA educational example
- Add educational assessment example and refined presentation slides (factor model, eigen decomposition refresher, parallel analysis explanation)
- Add slide set clarifying FA vs PCA distinctions; restructure FA presentation content

Refactor / Style:

- Repository structure cleanup and guideline relocation
- Code quality fixes across lesson examples (imports, formatting, minor typos)

Documentation:

- Update course repository documentation and PCA guidelines
- Add `CLAUDE.md` and recommend Claude Code extension
- Clarify LaTeX / math formatting consistency; fix notation typos

Evaluations Submodule Enhancements:

- Iterative improvements to competent and outstanding customer satisfaction solutions
- Refinements to employee engagement materials and factor analysis restructuring
- Bug fixes and final outstanding solution refinements

## v1.8.1 - 2025-09-23

Patch Release: Centralized Logging Utilities

Changes:

- Introduced centralized logging package `utils` with `setup_logger` helper
  - Consistent format and optional ANSI coloring
  - Prevents duplicate handlers in interactive sessions
  - Resolves previously missing `from utils import setup_logger` imports

No other code changes; pure infrastructure addition.

## v1.7.0 - 2025-09-20

Release: Chapter 5 Discriminant Analysis

Key Additions:

- Introduced Discriminant Analysis chapter with lesson materials
- Added domain-specific examples and supporting submodule updates

Notable Commits (selected):

- Release v1.7.0: Add Chapter 5 Discriminant Analysis
- Add Google Drive knowledge base download system; add `gdown` dependency
- Add VSCode extensions recommendations and AI chat modes
- Enhance commit and release workflows; update versioning prompts
- Multiple evaluations submodule updates (clarified roles, folder renames, syntax fixes)

## v1.6.0 - 2025-09-17

Release: Submodule Conversion & Assessment Automation

Highlights:

- Converted evaluations from subtree to submodule with ongoing iterative updates
- Integrated `txttoqti` upgrades (v0.6.0 → v0.7.0 → v0.8.0) adding Total Points Distribution System
- Added authenticity report for Factor Analysis presentation
- Refined AI agent instructions and workflow automation prompts
- Cleaned repository by removing obsolete scripts, temporary files, and drafts

Notable Commits (selected):

- refactor: convert evaluations from subtree to submodule
- chore: update evaluations submodule to include business case materials
- feat: upgrade `txttoqti` to v0.8.0 with Total Points Distribution System
- feat: sequential updates of `txttoqti` dependency (v0.6.0 → v0.7.0 → v0.8.0)
- docs: comprehensive AI agent instructions for educational codebase
- feat: update evaluations submodule with factor analysis template consolidation
- feat: update evaluations submodule with quiz improvements and test files
- cleanup: remove obsolete scripts and temporary files

## v1.5.0 - 2025-09-11

Major Updates:

- **Business Case Optimization**: Updated Factor Analysis business case requirements
  - Reduced weight from 25% to 5% of total course grade
  - Compressed timeline from 2 weeks to 1-week intensive schedule
  - Shortened deliverables: 10-12 min video (vs 18-22 min), 4-page report (vs 8 pages)
  - Maintained educational rigor while adapting scope to lighter assignment weight

- **Complete English Localization**: Translated all Spanish educational content
  - Comprehensive business case instructions (617 lines) fully translated
  - Code template with English function names, docstrings, and comments
  - Reflection questions and assessment rubrics adapted for English academic context

- **Enhanced Assessment Framework**: Refined evaluation structure
  - Updated penalties to match shorter presentation requirements
  - Added daily time investment guidance for 1-week schedule
  - Preserved multi-dimensional rubric system with 5-level performance anchors

Infrastructure:

- Systematic version management with consistent tagging across files
- Updated documentation to reflect v1.5.0 across repository
- Enhanced git commit organization following clean history practices

## v1.4.0 - 2025-01-27

Included commits (selected):

Major Features:

- Added comprehensive Factor Analysis study guide (factor_analysis_study_guide.typ)
- Integrated QTI quiz generation system with txttoqti package
- Established private evaluation materials system using git subtree
- Created systematic version tagging workflow

Educational Content:

- Complete Factor Analysis and PCA theoretical foundations
- Mathematical derivations and proofs
- Business case studies and practical implementations
- Software integration examples (Python, R, SPSS)
- Advanced topics including robust methods and sparse techniques

Infrastructure:

- Git subtree integration for private evaluation materials
- QTI-compatible quiz generation for LMS integration
- Systematic version management procedures
- Enhanced documentation and README updates

Notes

- Minor release: major educational content expansion with comprehensive Factor Analysis study guide, evaluation system infrastructure, and systematic version management workflows.
- Comprehensive 150+ page study guide covering theory to applications
- Private evaluation materials separated using git subtree
- QTI quiz generation for learning management system integration
- Enhanced infrastructure for course content development

## v1.3.0 - 2025-09-10

Included commits (selected):

- 559a364 — Adds TODO list for FA project
- 7c89165 — Integrates authentic hospital FA results into presentation
- b1e9edb — Refines factor analysis presentation
- d5aed43 — Revises FA results and comparison with PCA
- 13437f9 — Updates PCA results in presentation
- 5191376 — cleanup: remove original backup file after successful restructuring
- 78b3cad — cleanup: remove legacy and temporary files from beamer directory
- 5ae7155 — Restructures presentation for pedagogical flow
- 96566ec — feat: major pedagogical restructure of factor analysis presentation
- b80dc92 — Adds factor analysis presentation
- f5e2244 — Updates course presentation template with Tec colors

Notes

- Minor release: major pedagogical improvements to Factor Analysis chapter, including restructured presentations, refined content, and updated visual templates with institutional branding.
- Enhanced presentation structure for better pedagogical flow
- Integrated authentic hospital factor analysis results
- Updated course presentation template with Tec colors


## v0.1.2 - 2025-08-22

Included commits (selected):

- 2b3249e — Ignores local settings file
- e2b0c25 — Refactors AI agent instructions
- 0df5e28 — Refactors and documents course structure
- 87f547c — Adds discriminant analysis course content
- 2eef6bc — Adds regression analysis materials
- 304a766 — Adds factor analysis chapter content
- 230532b — Updates agent instructions for repository use
- 72f37a2 — Updates Claude guidance
- c5051ef — Updates CLAUDE.md with organized structure guidance
- 101defb — Implements LDA for two normal populations
- b530a7f — Adds CLAUDE.md for Claude Code guidance
- 5cc4c52 — Implements LDA for two Gaussian populations
- 08b0386 — Adds presentation on two-population discrimination

Notes

- This is an incremental (patch) release: documentation, tests, small examples, and course material additions.
- For future releases, follow the tagging procedure in `.github/prompts/update-version.prompt.md` and update this file with a short summary of included commits.

## v0.2.1 - 2025-08-24

Included commits (selected):

- 1271511 — Updates title font in head/foot
- 24366ec — Disables automatic section pages in the base theme
- cea2154 — Reduces contrast on section pages
- 824220f — Clarifies practice code architecture and structure
- f0f4cdb — Refactors course content structure documentation
- 7038521 — Restructures Factor Analysis chapter materials
- f64618e — Adds initial software practice file
- 61ce2eb — Implements factor rotation analysis practice
- c08a4cd — Adds factor retention analysis practice
- 09314f4 — Implements factor analysis equations for demonstration
- 983ca02 — Adds README for factor analysis objectives demo
- 35c761a — Creates factor analysis practice script
- 9db4d44 — Adds factor analysis computation module
- 64ef1a1 — docs: add factor analysis lecture notes (Chapter 4)
- 7e7f14f — Adds factor analysis reporting module
- 9b94c67 — Adds factor analysis objectives report
- 2a682df — Adds a lesson on Factor Analysis

Notes

- Patch release: primarily documentation, course materials, and practice exercises for the Factor Analysis chapter.
- Tag created: `v0.2.1` (patch bump from `v0.2.0`).

## v1.0.2 - 2025-08-28

Included commits (selected):

- 64adfe0a — Adds style guide for Copilot edits
- ce82c5b6 — Adds interpretation of PCA results
- 4e08ac5e — Clarifies PCA example interpretations
- b93a79ea — Refactors Kuiper PCA example script and improves CSV handling
- 203f6ef4 — Adds scripts to fetch Kuiper CSV data and perform PCA visualizations
- 5b18d6c4 — Improves readability of presentation
- 83ab9589 — Updates developer setup and chapter documentation
- 2d008973 — Simplifies environment setup instructions
- 8fdfc60d — Adds requirements installation step
- 09755108 — Improves factor analysis lesson structure

Notes

- Patch release: small feature additions (examples, fetch scripts), documentation, and educational refinements. This release updates example scripts to follow the project's py-percent interactive pattern and adds guidance for agent-driven edits.
