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
# Single subtopic practice script
cd beamers/4_Factor_Analysis/practice/4.1_objectives
python objectives_factor_analysis_practice.py

# All subtopics in a chapter
for dir in beamers/4_Factor_Analysis/practice/4.*/; do
  cd "$dir" && python *_practice.py && cd - > /dev/null
done

# Alternative execution from repo root (recommended)
.venv/bin/python beamers/4_Factor_Analysis/practice/4.1_objectives/objectives_factor_analysis_practice.py

# All subtopics using repo root execution
for f in beamers/4_Factor_Analysis/practice/*/*_practice.py; do
  echo "--- running $f ---"
  .venv/bin/python "$f" || break
done

# Compile chapter presentation
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
- **Chapter presentations** should cover all subtopics in a unified narrative flow
- **Practice exercises** should be self-contained with clear documentation and real-world applications
- **Chapter README** serves as the primary learning resource with comprehensive overview
- **Subtopic READMs** should be minimal - just usage instructions and file descriptions
- **Practice scripts** must include embedded documentation explaining purpose and workflow sections

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
1. Complete Factor Analysis practice implementations (4.5_oblique_rotation missing)
2. Test all existing practice scripts for functionality
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
│                                      # • Mathematical notation guide
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
- **Independent subtopics**: Each practice folder should work standalone
- **Embedded documentation**: Practice scripts contain purpose, workflow sections, and usage examples
- **Consistent naming**: Always use `X.Y_descriptive_name` pattern
- **Minimal redundancy**: Subtopic READMEs should only contain essential usage info