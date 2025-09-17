# Copilot Instructions - MA2003B Multivariate Statistics Course

## Project Architecture

This is an **academic course repository** for MA2003B - Application of Multivariate Methods in Data Science. The codebase follows **educational-first principles** with self-contained examples using real-world datasets.

### Key Structure
- `lessons/X_Topic/` - Chapter materials with `beamer/` presentations and `code/` examples
- `evaluations/` - Assessment materials (private submodule with QTI quizzes)  
- `utils/` - Shared utilities package with centralized logging
- `scripts/` - Data synchronization and maintenance tools

### Package Setup
**Always use the editable install workflow:**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .  # Enables `from utils import setup_logger`
```

## Essential Development Patterns

### Interactive Code Structure
**All analysis scripts use py-percent cells** for VS Code/Jupyter compatibility:
```python
# %%
# Cell for data loading and preprocessing

# %% [markdown] 
# ## Analysis Section Title

# %%
# Cell for statistical analysis
```

### Centralized Logging  
**Always import and use the shared logger:**
```python
from utils import setup_logger
logger = setup_logger(__name__)
logger.info("Analysis starting...")  # Never plain print() for analysis steps
```

### File Path Conventions
**Use pathlib for all file operations:**
```python
from pathlib import Path
script_dir = Path(__file__).resolve().parent
data_file = script_dir / "data.csv"
output_file = script_dir / "results.png"
```

### Factor Analysis Workflow Pattern
**Follow the established 6-step structure** seen in `kuiper_fa.py`, `invest_fa.py`:
1. **Assumptions Testing** (KMO, Bartlett's sphericity)
2. **Factor Retention** (Kaiser criterion, scree plot)  
3. **Extraction** (Principal/ML methods)
4. **Rotation** (Varimax/Promax comparison)
5. **Interpretation** (loadings matrix, communalities)
6. **Validation** (factor scores, residuals)

## Assessment Integration

### QTI Quiz Generation
**Use txttoqti for educational assessments:**
```python
# Current v0.8.0 workflow with total points distribution
from txttoqti import TxtToQtiConverter
converter = TxtToQtiConverter()
converter.convert_file(
    txt_file="quiz.txt",
    qti_file="output.zip", 
    total_points=100,
    qti_version="qti12"
)
```

### Business Case Structure
**Follow the competent/outstanding solution hierarchy** in `business_case/`:
- **Competent**: Core statistical workflow with standard interpretations
- **Outstanding**: Advanced methods, strategic recommendations, executive summaries

## Data and Domain Patterns

### Dataset Organization  
**Each example follows fetch → analyze pattern:**
- `fetch_*.py` - Data acquisition/generation script
- `*_fa.py` - Factor analysis implementation
- `*_pca.py` - PCA comparison analysis
- `README.md` - Educational context and data dictionary

### Cross-Domain Examples
**Current active domains** (Chapter 4):
- **Finance** (`invest_example/`) - European stock market factor models
- **Astronomy** (`kuiper_example/`) - Kuiper Belt orbital dynamics  
- **Healthcare** (`hospitals_example/`) - Hospital quality assessment

## Critical Dependencies

**Core scientific stack** (in pyproject.toml):
```python
dependencies = ["numpy>=1.24", "pandas>=2.0", "matplotlib>=3.8", 
               "scikit-learn>=1.3", "seaborn>=0.12", "txttoqti"]
```

**Factor analysis specialist packages:**
```python
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
```

## Command Patterns

### Running Examples
```bash
# Standard workflow: fetch data, then analyze
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/fetch_invest.py
.venv/bin/python lessons/4_Factor_Analysis/code/invest_example/invest_fa.py
```

### Assessment Conversion
```bash
# QTI conversion with total points (v0.8.0 feature)
cd evaluations/4_Factor_Analysis/qti_quiz/
uv run txttoqti -i quiz.txt -o output.zip --total-points 100 --qti-version qti12
```

### Testing and Quality
```bash
.venv/bin/python -m pytest -q  # Run from repo root
ruff check . && ruff format .  # Code quality
```

## Educational Code Principles

- **Self-documenting**: Each script generates human-readable output files, not just console logs
- **Standalone**: Examples work independently with embedded data dictionaries
- **Authentic**: Use realistic datasets with domain-specific interpretation challenges  
- **Comparative**: Always compare PCA vs Factor Analysis on same data
- **Reproducible**: Fixed random seeds, deterministic outputs for educational consistency

## Submodule Management

The `evaluations/` directory is a **private submodule** for assessment materials:
```bash
git submodule update --init --recursive  # First setup
cd evaluations && git pull origin main && cd ..  # Update evaluations
git add evaluations && git commit -m "update evaluations"  # Commit pointer
```