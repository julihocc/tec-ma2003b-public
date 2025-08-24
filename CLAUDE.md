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
# Single Python script (standardized structure)
cd beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/practice
python objectives_factor_analysis_practice.py

# All Python scripts in a chapter (standardized structure)
for f in beamers/4_Factor_Analysis/*/practice/*_practice.py; do
  echo "--- running $f ---"
  python "$f" || break
done

# All Python scripts across chapters
for chapter in beamers/{1_Regression_Analysis,4_Factor_Analysis,5_Discriminant_Analysis}; do
  for f in $chapter/*/practice/*_practice.py; do
    echo "--- running $f ---"
    python "$f" || break
  done
done

# Compile lesson presentations
cd beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/lesson
pdflatex objectives_factor_analysis.tex

# Compile comprehensive notes
cd beamers/4_Factor_Analysis/4.1_Objectives_of_factor_analysis/notes
pdflatex objectives_factor_analysis_notes.tex
```

**Data pull script:**
```bash
.venv/bin/python scripts/pull_data.py
# Override source path: MA2003B_ORIGIN_PATH="/path/to/origin" .venv/bin/python scripts/pull_data.py
```

## Repository Structure

**Course Materials:**
- `beamers/1_Regression_Analysis/` - Regression analysis exercises and materials (5 topics, fully refactored)
- `beamers/4_Factor_Analysis/` - Factor analysis exercises and materials (6 topics, organized structure)
- `beamers/5_Discriminant_Analysis/` - Discriminant analysis exercises and materials (6 topics, fully refactored)
- Each exercise folder contains organized subfolders (see Course Content Structure below)

**Utilities:**
- `utils/` - Shared utilities package with logging functionality (exported via `__init__.py`)
- `utils/logger.py` - Centralized logging: `setup_logger(name=None, level=logging.INFO, logfile=None, fmt=None)`
  - Supports both stream and file logging, prevents duplication with `propagate = False`
- `utils/test_logger.py` - Unit tests for logger functionality

**Scripts:**
- `scripts/pull_data.py` - Data synchronization script that copies course materials from OneDrive source to local `backup/ma2003b/` directory

**Documentation:**
- `documentation/` - Course planning documents including hour allocation tables
- `backup/` - Contains course materials copied from the OneDrive source
- `.claude/backup/conversations/` - Claude Code conversation exports for development history

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
**IMPORTANT: Use standardized folder structure for all lessons:**

```
X.Y_Topic_Name/
├── README.md                          # Comprehensive overview (merged content)
├── lesson/                            # Student presentation materials
│   ├── [topic].tex                    # Beamer presentation source
│   ├── [topic].pdf                    # Compiled presentation
│   └── ... (LaTeX auxiliary files)
├── practice/                          # Hands-on programming exercises
│   ├── [topic]_practice.py           # Main practice script
│   ├── [topic]_analysis.py           # Core analysis functions (modular)
│   ├── [topic]_reporter.py           # Report generation functions
│   └── README.md                      # Practice-specific instructions
└── notes/                             # Expanded content and guidance
    ├── [topic]_notes.tex              # Comprehensive LaTeX article
    ├── [topic]_notes.pdf              # Compiled documentation
    └── additional_resources/          # Extra materials, datasets, etc.
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

## Chapter Status and Organization

**Standardized Structure (New Format):**
- ✅ **Chapter 4**: Factor Analysis (6 topics, using new standardized structure)
  - Topic 4.1: Objectives of Factor Analysis (lesson/, practice/, notes/ structure)

**Legacy Structure (Needs Migration):**
- ✅ **Chapter 1**: Regression Analysis (5 topics, organized subfolders - needs standardization)
- ✅ **Chapter 5**: Discriminant Analysis (6 topics, organized subfolders - needs standardization)

**Future Chapters (Need Organization):**
- Chapter 2: Multivariate Analysis
- Chapter 3: Principal Component Analysis (PCA)
- Chapter 6: Cluster Analysis  
- Chapter 7: Multivariate Regression

**Migration Priority:**
1. Standardize existing Chapter 1 and Chapter 5 topics to new structure
2. Remove Julia implementations from all chapters
3. Consolidate report files into README.md files
4. Create comprehensive notes/ folders for instructor guidance

## Conversation Management

When working with this repository, conversation exports should be saved to maintain development history:

**Export Location:** `.claude/backup/conversations/`

**Usage:**
- Use `/export` command in Claude Code to save conversation history
- Recommended naming: `YYYY-MM-DD-brief-description.txt`
- Helpful for tracking development decisions and maintaining context

## Important Notes

- The `scripts/pull_data.py` contains machine-specific OneDrive paths and may not work on all systems
- Some practice scripts use optional libraries (numpy, scipy, scikit-learn, factor_analyzer)
- **LaTeX Compilation**: Use `pdflatex` to compile .tex files in `lesson/` and `notes/` subfolders
- **Practice Scripts**: All practice implementations are in Python for maintainability
- **Virtual Environment**: Always use `pip install -e .` for development to access utils module
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