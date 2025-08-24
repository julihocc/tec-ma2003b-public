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

**Run practice scripts:**
```bash
# Single Python script (current Factor Analysis structure)
cd beamers/4_Factor_Analysis/practice/4.1_objectives
python objectives_factor_analysis_practice.py

# All Python scripts in Factor Analysis chapter
for f in beamers/4_Factor_Analysis/practice/*/*_practice.py; do
  echo "--- running $f ---"
  .venv/bin/python "$f" || break
done

# Alternative single script execution from repo root
.venv/bin/python beamers/4_Factor_Analysis/practice/4.1_objectives/objectives_factor_analysis_practice.py

# Compile lesson presentations (Factor Analysis chapter)
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
  - Uses `practice/4.X_topic/` folder organization for exercise scripts
  - Contains centralized `lesson/` folder with presentation materials
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
- `.github/copilot-instructions.md` - AI coding assistant instructions (contains some outdated paths)
- `.claude/backup/conversations/` - Claude Code conversation exports for development history
- `beamers/themes/` - LaTeX Beamer themes and styling for presentations

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
**Current Factor Analysis Structure:**

```
4_Factor_Analysis/
├── README.md                          # Chapter overview
├── lesson/                            # Centralized presentation materials
│   ├── factor_analysis.tex           # Main Beamer presentation
│   ├── factor_analysis.pdf           # Compiled presentation  
│   └── ... (LaTeX auxiliary files)
└── practice/                          # Topic-organized exercises
    ├── 4.1_objectives/
    │   ├── README.md
    │   ├── objectives_factor_analysis_practice.py
    │   └── [additional analysis modules]
    ├── 4.2_equations/
    │   ├── README.md
    │   └── equations_practice.py
    ├── 4.3_number_of_factors/
    ├── 4.4_rotation/
    ├── 4.5_oblique_rotation/
    └── 4.6_software/
```

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

**When refactoring existing exercises:**
1. **Eliminate redundancy**: Remove separate report files, merge content into README.md
2. **Remove Julia implementations**: Single Python codebase is easier to maintain  
3. **Rename folders**: `latex/` → `lesson/`, `python/` → `practice/`
4. **Create notes**: Add comprehensive `notes/` folder with LaTeX article
5. **Modular code**: Separate analysis functions from reporting in practice folder

**Key Utilities:**
- `setup_logger()` - Configured logger with duplicate handler prevention and `propagate = False`
- Use existing utilities instead of creating ad-hoc helpers

## Development Guidelines

### Code Quality
- **All scripts should use** the centralized `setup_logger()` function from utils
- **When adding new utilities**, export them through `utils/__init__.py`
- **Follow existing error handling patterns** seen in `pull_data.py`
- **Use type hints** as demonstrated in the logger module
- **Always use the project's virtual environment** for consistency

### Lesson Development
- **Use standardized structure** for all new lessons (lesson/, practice/, notes/)
- **Consolidate documentation** in comprehensive README.md files
- **Create modular practice code** with separate analysis and reporting functions
- **Focus on student learning** in lesson presentations, not implementation details
- **Provide expanded notes** for instructors and advanced learners
- **Test practice scripts** to ensure they work out-of-the-box

### Content Guidelines  
- **Student presentations** should focus on statistical problems, objectives, and interpretation
- **Practice exercises** should demonstrate real-world applications with meaningful data
- **Notes documentation** should provide pedagogical guidance and teaching strategies
- **README files** serve as comprehensive overviews - eliminate redundant report files

## Current Repository State

**Active Content (improving-design branch):**
- ✅ **Chapter 4**: Factor Analysis (6 topics, using chapter-level organization)
  - Topics: 4.1 Objectives, 4.2 Equations, 4.3 Number of Factors, 4.4 Rotation, 4.5 Oblique Rotation, 4.6 Software
  - Structure: Central `lesson/` folder + `practice/4.X_topic/` subfolders
  - Status: Partially implemented practice scripts

**Removed Content (staged for deletion):**
- ❌ **Chapter 1**: Regression Analysis (5 topics) - removed from current branch
- ❌ **Chapter 5**: Discriminant Analysis (6 topics) - removed from current branch

**Future Development:**
- Chapter 2: Multivariate Analysis
- Chapter 3: Principal Component Analysis (PCA)  
- Chapter 6: Cluster Analysis
- Chapter 7: Multivariate Regression

**Current Priorities:**
1. Complete Factor Analysis practice implementations
2. Implement missing practice scripts (4.5_oblique_rotation currently missing)
3. Test all existing practice scripts for functionality
4. Consider migration to standardized per-topic structure for better organization

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

## Standardized Lesson Template

When creating new lessons, use this template structure:

```
X.Y_Topic_Name/
├── README.md                          # Comprehensive overview
├── lesson/                            # Beamer presentation for students  
├── practice/                          # Modular Python implementation
└── notes/                             # LaTeX article for instructors/learners
```

**Key principles:**
- **Student-focused lessons**: Problem-oriented presentations, not code architecture
- **Modular practice code**: Separate analysis from reporting for reusability
- **Comprehensive documentation**: README as single source of truth
- **Pedagogical guidance**: Notes folder with teaching strategies and tips