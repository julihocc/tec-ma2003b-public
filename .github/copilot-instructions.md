---
---
# AI coding agent instructions for tec-ma2003b-public

Purpose: short, actionable guidance so an AI coding agent can be productive quickly in this repository.

Quick start (most common developer flow)
- Create & activate the local venv used by the project:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Install the package in editable mode so practice scripts import local modules:
  ```bash
  pip install -e .
  ```
- Run tests from repo root:
  ```bash
  .venv/bin/python -m pytest -q
  ```

What this repo contains (big picture)
- `beamers/` — course materials grouped by topic/chapter. Each chapter contains subfolders with `python/` practice scripts, optional `julia/`, `latex/` slides, and a `_report.txt` or `_report.md` artifact used by teaching materials.
- `utils/` — small shared utilities exported via `utils/__init__.py`. Important file: `utils/logger.py` (use `setup_logger(...)`).
- `scripts/` — helper scripts (e.g., `scripts/pull_data.py`) that may use absolute paths; prefer environment parametrization.

Key developer workflows & concrete commands
- Run a single practice script (example):
  ```bash
  .venv/bin/python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py
  ```
- Compile Beamer slides (example): run `pdflatex` twice on the `.tex` file in the lesson folder (e.g. `beamers/4_Factor_Analysis/lesson/factor_analysis.tex`).
- Add runtime dependency: update `requirements.txt` and add a one-line note in the exercise `README.md` inside the relevant `python/` folder.

Project-specific conventions (follow these exactly)
- Preserve the `beamers/` folder layout and its `latex/` and `_report` artifacts — other materials rely on these paths.
- Practice scripts must write a human-readable report file beside the script (see `beamers/*/*/python/*_practice.py`) and should use the repository logger for progress and errors:
  ```py
  from utils.logger import setup_logger
  logger = setup_logger(__name__)
  logger.info('writing report to %s', report_path)
  ```
- Tests for utilities live next to the module (e.g., `utils/test_logger.py`) — update tests when changing `utils/`.

Integration points and gotchas (frequent issues to watch)
- `scripts/pull_data.py` contains an absolute path; prefer parameterization with `MA2003B_ORIGIN_PATH` and add tests covering both fallback and override.
- Some practice scripts expect optional libraries (e.g., `scikit-learn`, `factor_analyzer` for factor-analysis demos). If you add those, update `requirements.txt` accordingly.
- Many slides use fragile `frame` + `verbatim` for code. Programmatic edits must preserve `frame`/`verbatim` boundaries to avoid LaTeX fatal errors (e.g., unmatched `egin{frame}`/`egin{verbatim}` pairs).

Concrete examples in this repo
- Shared logger: `utils/logger.py` — use `setup_logger(name=None, level=logging.INFO, logfile=None)`; it disables propagation to avoid duplicate handlers.
- Practice script report pattern: see `beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py` — scripts open a report file next to the script and write demonstration text (prefer file writes over prints).
- Slides build: `beamers/4_Factor_Analysis/lesson/factor_analysis.tex` — when editing slides programmatically, ensure each R snippet/`verbatim` block is isolated on its own `frame` to avoid line-wrapping/compilation problems.

When updating this file
- Merge changes; do not overwrite maintainers' notes. Keep this document concise (20–50 lines). Preserve any custom guidance already present.

If something is unclear or you want a CI snippet / example test updates, point to which chapter or file and I will expand that section.

---

Full CLAUDE.md reference (verbatim):

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the MA2003B - Application of Multivariate Methods in Data Science course repository, an intermediate mathematics course focusing on analyzing multidimensional large databases using multivariate statistical techniques.

**Course Topics:** Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression.

## Development Setup

Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Key Commands

**Run tests:**
```bash
.venv/bin/python -m pytest -q
```

**Run practice scripts (when implemented):**
```bash
# Single subtopic practice script (template - folders don't exist yet)
cd beamers/4_Factor_Analysis/practice/4.1_objectives
python objectives_factor_analysis_practice.py

# All subtopics in a chapter (template - folders don't exist yet)
for dir in beamers/4_Factor_Analysis/practice/4.*/; do
  cd "$dir" && python *_practice.py && cd - > /dev/null
done

# Alternative execution from repo root (recommended when implemented)
.venv/bin/python beamers/4_Factor_Analysis/practice/4.1_objectives/objectives_factor_analysis_practice.py

# All subtopics using repo root execution (template)
for f in beamers/4_Factor_Analysis/practice/*/*_practice.py; do
  echo "--- running $f ---"
  .venv/bin/python "$f" || break
done
```

**Compile presentations:**
```bash
# Factor analysis presentation (available)
cd beamers/4_Factor_Analysis/lesson
pdflatex factor_analysis.tex
```

**Data pull script:**
```bash
.venv/bin/python scripts/pull_data.py
# Override source path: MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
```

## Repository Structure

**Course Materials:**
- `beamers/4_Factor_Analysis/` - Factor analysis exercises and materials (6 topics, current structure)
  - Contains centralized `lesson/` folder with compiled presentation materials
  - Practice folders (`practice/4.X_topic/`) planned but not yet implemented
  - Chapter README provides comprehensive learning guide
- Former `beamers/1_Regression_Analysis/` and `beamers/5_Discriminant_Analysis/` chapters have been removed in current working branch

**Utilities:**
- `utils/` - Shared utilities package with logging functionality (exported via `__init__.py`)
- `utils/logger.py` - Centralized logging: `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`
  - Supports both stream and file logging, prevents duplication with `propagate = False`
- `utils/test_logger.py` - Unit tests for logger functionality

**Scripts:**
- `scripts/pull_data.py` - Data synchronization script that copies course materials from OneDrive source to local `backup/ma2003b/` directory

**Documentation:**
- `documentation/` - Course planning documents including hour allocation tables  
- `.github/copilot-instructions.md` - Legacy AI coding assistant instructions (contains outdated paths, use CLAUDE.md instead)
- `.claude/backup/conversations/` - Claude Code conversation exports for development history
- `beamers/themes/` - LaTeX Beamer themes and styling for presentations (`ma2003b` custom theme)
- `factor_analysis_report.txt` - Generated report artifact at repo root

## Key Architecture Insights

**Package Structure:** The repository is configured as an editable Python package (`ma2003b-course`) with `utils` as a proper Python package. This allows practice scripts to import shared functionality using `from utils import setup_logger`.

**Centralized Logging Pattern:** All scripts use the `setup_logger()` utility from `utils/logger.py`. This logger:
- Prevents handler duplication through existing handler checks
- Sets `propagate = False` to avoid duplicate messages
- Supports both console and file logging
- Provides consistent formatting across all scripts

**Chapter-level Consolidation Model:** Unlike traditional per-topic folders, Factor Analysis uses:
- Single comprehensive README at chapter level
- Single consolidated presentation covering all 6 subtopics
- Modular practice exercises (planned but not implemented)
- Clear separation between lesson materials and hands-on exercises

**Data Management:** The `scripts/pull_data.py` implements a robust data synchronization pattern:
- Environment variable override support (`MA2003B_ORIGIN_PATH`)
- Safety checks to prevent recursive copying
- Comprehensive error handling and logging
- Dry-run capability for testing

## Development Conventions

**File Organization:**
- Exercise materials stay in their respective folders under `beamers/`
- New utilities go in `utils/` and are exported via `utils/__init__.py`
- Tests sit next to modules (e.g., `utils/test_logger.py`)
- Save conversation exports in `.claude/backup/conversations/` for organized documentation

**Testing:**
- Use pytest with `tmp_path` fixtures for filesystem tests
- Run tests after changes: `.venv/bin/python -m pytest -q`

**Package Management:**
- Use editable install (`pip install -e .`) for development
- Dependencies: `requirements.txt` contains minimal runtime/dev dependencies
- `pyproject.toml` defines package metadata

**Course Content Structure:**
**Current Chapter Organization (Factor Analysis Model):**

```
X_Chapter_Name/
├── README.md                          # Comprehensive chapter overview with:
│                                      #   - Learning objectives
│                                      #   - Chapter structure outline  
│                                      #   - Usage instructions
│                                      #   - Prerequisites and key concepts
├── lesson/                            # Single consolidated presentation
│   ├── [chapter].tex                 # Complete chapter Beamer presentation
│   ├── [chapter].pdf                 # Compiled presentation
│   └── ... (LaTeX auxiliary files)
└── practice/                          # Subtopic-organized exercises
    ├── X.1_subtopic_name/
    │   ├── README.md                  # Brief subtopic practice instructions
    │   ├── [subtopic]_practice.py     # Main executable practice script
    │   └── [optional analysis modules]
    ├── X.2_subtopic_name/
    │   ├── README.md
    │   └── [subtopic]_practice.py
    └── ... (continue for all subtopics)
```

**Key Organizational Principles:**
- **Chapter-level consolidation**: Single presentation covers all subtopics
- **Comprehensive chapter README**: Serves as complete learning guide
- **Modular practice exercises**: Each subtopic has independent practice folder
- **Separation of concerns**: Practice folders split into computation, reporting, and orchestration
- **Clean code architecture**: Pure functions, dataclasses, type hints for undergraduate learning
- **Self-contained scripts**: Practice scripts include embedded documentation
- **Consistent naming**: `X.Y_descriptive_name` pattern for subtopic folders

**Future Standardized Structure (Target):**

```
X.Y_Topic_Name/
├── README.md                          # Comprehensive overview
├── lesson/                            # Student presentation materials
│   ├── [topic].tex                    # Beamer presentation source
│   └── [topic].pdf                    # Compiled presentation
├── practice/                          # Hands-on programming exercises
│   ├── [topic]_practice.py           # Main practice script
│   ├── [topic]_analysis.py           # Core analysis functions (modular)
│   └── [topic]_reporter.py           # Report generation functions
└── notes/                             # Expanded content and guidance
    ├── [topic]_notes.tex              # Comprehensive LaTeX article
    └── [topic]_notes.pdf              # Compiled documentation
```

**Legacy structure (deprecated):**
- `[topic]_report.txt` - Exercise description (now merged into README.md)
- `julia/` folder - Julia implementations (removed for maintainability)
- Separate `latex/` and `python/` folders (now `lesson/` and `practice/`)

**Chapter Development Pattern (Based on Factor Analysis):**
1. **Create comprehensive chapter README**: Include learning objectives, structure outline, prerequisites, and usage examples
2. **Single consolidated presentation**: One Beamer file covers all chapter subtopics with clear section breaks
3. **Modular subtopic practice folders**: Each `X.Y_subtopic/` folder contains independent practice implementation
4. **Self-documenting practice scripts**: Each script includes embedded purpose, workflow, and section documentation
5. **Minimal subtopic READMEs**: Brief usage instructions since main documentation is in chapter README
6. **Consistent naming convention**: Use `X.Y_descriptive_name` pattern for all subtopic folders

**Practice Folder Structure (Modular Pattern):**
Each `X.Y_subtopic/` folder should contain:

```
X.Y_subtopic_name/
├── README.md                          # Brief usage instructions
├── [subtopic]_practice.py             # Main orchestration script
├── [subject].py                       # Pure computational functions
├── [subject]_reporter.py              # Output formatting functions
└── [subject]_report.txt               # Generated demonstration output
```

**Separation of Concerns Pattern:**
- **Orchestration script** (`*_practice.py`): Workflow coordination, logging, main() function
- **Computation module** (`*.py`): Pure functions, dataclasses, type hints, no I/O
- **Reporter module** (`*_reporter.py`): Output formatting, string generation, display logic
- **Generated report** (`*_report.txt`): Human-readable demonstration output

**Key Utilities:**
- `setup_logger()` - Configured logger with duplicate handler prevention and `propagate = False`
- Use existing utilities instead of creating ad-hoc helpers

## Development Guidelines

### Code Quality
- **All scripts should use** the centralized `setup_logger()` function from utils
- **When adding new utilities**, export them through `utils/__init__.py`
- **Follow existing error handling patterns** seen in `pull_data.py`
- **Use type hints** as demonstrated in the logger module and Factor Analysis computational functions
- **Always use the project's virtual environment** for consistency

### Practice Code Architecture (Undergraduate Focus)
- **Keep it simple**: Priority is understanding statistical concepts, not software engineering
- **Clean separation**: Computation, reporting, and orchestration in separate modules
- **Type hints for learning**: Use dataclasses and type annotations to make data flow clear
- **Pure functions**: Computational modules should have no side effects or I/O
- **Self-documenting**: Each function includes docstrings with Args/Returns
- **Avoid overengineering**: No complex abstractions - direct, readable implementations

### Lesson Development
- **Use standardized structure** for all new lessons (lesson/, practice/, notes/)
- **Consolidate documentation** in comprehensive README.md files
- **Create modular practice code** with separate analysis and reporting functions
- **Focus on student learning** in lesson presentations, not implementation details
- **Provide expanded notes** for instructors and advanced learners
- **Test practice scripts** to ensure they work out-of-the-box

### Content Guidelines  
- **Chapter presentations** should cover all subtopics in a unified narrative flow
- **Practice exercises** should be self-contained with clear documentation and real-world applications
- **Chapter README** serves as the primary learning resource with comprehensive overview
- **Subtopic READMs** should be minimal - just usage instructions and file descriptions
- **Practice scripts** must include embedded documentation explaining purpose and workflow sections

## Current Repository State

**Active Content (analisis-por-factores branch):**
- ✅ **Chapter 4**: Factor Analysis (6 topics, using chapter-level organization)
  - Topics: 4.1 Objectives, 4.2 Equations, 4.3 Number of Factors, 4.4 Rotation, 4.5 Oblique Rotation, 4.6 Software
  - Structure: Central `lesson/` folder with compiled presentation, practice folders need implementation
  - Status: Presentation materials complete, practice scripts not yet implemented

**Removed Content (staged for deletion):**
- ❌ **Chapter 1**: Regression Analysis (5 topics) - removed from current branch
- ❌ **Chapter 5**: Discriminant Analysis (6 topics) - removed from current branch

**Future Development:**
- Chapter 2: Multivariate Analysis
- Chapter 3: Principal Component Analysis (PCA)  
- Chapter 6: Cluster Analysis
- Chapter 7: Multivariate Regression

**Current Priorities:**
1. Create Factor Analysis practice implementations (practice folders don't exist yet - need all 6 subtopics)
2. Test all practice scripts for functionality once implemented
3. Apply this organizational pattern to future chapters
4. Validate the chapter-level consolidation approach before expanding

## Conversation Management

When working with this repository, conversation exports should be saved to maintain development history:

**Export Location:** `.claude/backup/conversations/`

**Usage:**
- Use `/export` command in Claude Code to save conversation history
- Recommended naming: `YYYY-MM-DD-brief-description.txt`
- Helpful for tracking development decisions and maintaining context

## Important Notes

- The `scripts/pull_data.py` contains machine-specific OneDrive paths; use `MA2003B_ORIGIN_PATH` environment variable to override
- **Required dependencies**: numpy, scipy, scikit-learn, factor_analyzer (see `requirements.txt`)
- **LaTeX Compilation**: Use `pdflatex` to compile .tex files in `lesson/` folders
- **Practice Scripts**: All practice implementations are in Python for maintainability
- **Virtual Environment**: Always use `pip install -e .` for development to access utils module
- **Report Pattern**: Practice scripts should write human-readable reports to files (e.g., `*_report.txt`) rather than just printing to console
- **Logger Usage**: Always use `from utils import setup_logger` and call `setup_logger(__name__)` for consistent logging across scripts
- Course covers 7 main topics: Regression Analysis, Multivariate Analysis, PCA, Factor Analysis, Discriminant Analysis, Cluster Analysis, and Multivariate Regression

## Chapter Template (Factor Analysis Model)

When creating new chapters, use this organizational structure:

```
X_Chapter_Name/
├── README.md                          # Complete chapter learning resource
│                                      # • Learning objectives & outcomes
│                                      # • Subtopic structure & overview
│                                      # • Prerequisites & key concepts  
│                                      # • Usage instructions & examples
├── lesson/
│   ├── [chapter].tex                 # Unified Beamer presentation
│   └── [chapter].pdf                 # Compiled slides
└── practice/
    ├── X.1_subtopic_name/            # Independent practice modules
    │   ├── README.md                  # Brief usage instructions
    │   └── [subtopic]_practice.py     # Self-documented executable
    ├── X.2_subtopic_name/
    │   └── ... (same pattern)
    └── X.N_final_subtopic/
```

**Implementation Guidelines:**
- **Chapter README structure**: Follow Factor Analysis README as template (learning objectives, structure outline, prerequisites, key concepts, mathematical notation)
- **Unified presentation**: Single Beamer file with clear section breaks for each subtopic
- **Independent subtopics**: Each practice folder should work standalone with clean modular structure
- **Embedded documentation**: Practice scripts contain purpose, workflow sections, and usage examples
- **Consistent naming**: Always use `X.Y_descriptive_name` pattern
- **Minimal redundancy**: Subtopic READMEs should only contain essential usage info

**Practice Implementation Pattern:**
1. **Create orchestration script** (`[subtopic]_practice.py`):
   - Import from local computation and reporter modules
   - Use centralized logger from utils
   - Coordinate workflow: data → computation → formatting → output
   - Write human-readable report to `*_report.txt`

2. **Create computation module** (`[subject].py`):
   - Define dataclasses for structured results
   - Write pure functions with clear type hints
   - No I/O operations or side effects
   - Focus on statistical/mathematical operations

3. **Create reporter module** (`[subject]_reporter.py`):
   - Functions that take computation results and return formatted strings
   - Handle all output formatting and display logic
   - Clear section headers and educational explanations
# AI coding agent instructions for this repository

Purpose: short, actionable guidance so an AI coding agent can be productive quickly in tec-ma2003b-public.

Quick start (most common developer flow)
- Create & activate the local venv used by the project:
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install editable package so practice scripts import local modules:
  - pip install -e .
- Run tests from repo root:
  - .venv/bin/python -m pytest -q

What this repo contains (big picture)
- Course materials arranged under `beamers/`. Each topic (chapter) folder contains subfolders for exercises with: a `python/` practice script, optional `julia/` examples, `latex/` slides, and a `_report.txt` or `_report.md` output artifact.
- Small utilities under `utils/` (exported via `utils/__init__.py`) provide shared helpers — e.g. `utils/logger.py` exposes `setup_logger(...)` and configures a repository logger used by practice scripts.
- Top-level packaging files: `setup.py`, `pyproject.toml` (optional), and `requirements.txt` drive local development.

Key developer workflows and commands
- Run a single practice script (example):
  - .venv/bin/python beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/python/objectives_factor_analysis_practice.py
- Run a chapter smoke test (example pattern):
  - for f in beamers/5_Discriminant_Analysis/*/*_practice.py; do .venv/bin/python "$f" || break; done
- Install new runtime dependency: add to `requirements.txt` and include a one-line note in the exercise `README.md` under the relevant `python/` folder.

Project-specific conventions (important to follow)
- Preserve the `beamers/` folder layout. Do not move `.tex` files or `_report.txt` artifacts — they are referenced by teaching materials.
- Practice scripts should write human-readable reports to a report file in their folder (e.g. `objectives_factor_analysis_report.txt`) and use the repository logger for informational/errors. Shared logger: `from utils.logger import setup_logger`.
- Tests are lightweight and sit next to modules. When changing `utils/` utilities, update their tests in the same folder.

Integration points and gotchas
- `scripts/pull_data.py` contains an absolute path; prefer parameterizing with `MA2003B_ORIGIN_PATH` env var when changing it and add tests for both fallback and override.
- Packaging: `setup.py` is present (legacy); prefer editable install (`pip install -e .`) for development and tests.
- Some practice scripts support both Python and Julia; the Python scripts may expect `scikit-learn` and `factor_analyzer`. If you add or require these, update `requirements.txt`.

Examples and concrete references
- Shared logger: `utils/logger.py` — create a logger with `setup_logger(__name__)` and call `logger.info(...)` for progress messages; do not replace the global logger behavior unless necessary.
- Report pattern: practice script opens a report file next to the script and writes the demonstration text there (see `beamers/.../objectives_factor_analysis_practice.py`). Keep prints for interactive debugging only; prefer writing reports to files.
- Absolute-path helper: `scripts/pull_data.py` — convert hard-coded paths to use `os.getenv('MA2003B_ORIGIN_PATH', '<fallback>')` when parameterizing.

Additional practical notes (from internal guidance)
- Logger details: `setup_logger(name=None, level=logging.INFO, logfile=None)` is the common helper; it configures stream+file handlers and sets `logger.propagate = False` to avoid duplicated messages — prefer this helper over ad-hoc loggers.
- Conversation exports: save chat/conversation exports to `.claude/backup/conversations/` using a clear name like `YYYY-MM-DD-brief-description.txt` so development history is reproducible and auditable.
- Standard lesson template (short): each topic should follow the `lesson/`, `practice/`, `notes/` layout to keep materials consistent across chapters.

When updating this file
- Merge, do not overwrite. Keep guidance short (20-50 lines). Preserve maintainers' custom notes when present.

If anything is unclear or you want a CI snippet, packaging details, or example test updates added, tell me which section to expand.

---
