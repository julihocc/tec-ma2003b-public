# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the configuration repository for MA2003B - Application of Multivariate Methods in Data Science, an intermediate mathematics course focusing on analyzing multidimensional large databases using multivariate statistical techniques.

## Repository Structure

- `backup/`: Contains course materials copied from the OneDrive source
- `documentacion/`: Course planning documents including hour allocation tables
- `scripts/`: Utility scripts for data management 
- `utils/`: Shared utilities package with logging functionality

## Common Commands

### Installation and Setup
```bash
pip install -e .
```

### Data Management
```bash
python scripts/pull_data.py
```
This script backs up course materials from the OneDrive source to the local `backup/ma2003b/` directory.

### Testing
```bash
python -m pytest utils/test_logger.py
```

## Code Architecture

### Utilities Package (`utils/`)
- **`logger.py`**: Centralized logging configuration with `setup_logger()` function
  - Supports both stream and file logging
  - Configurable log levels and formats
  - Prevents message duplication with `propagate = False`
- **`__init__.py`**: Package initialization exporting `setup_logger`
- **`test_logger.py`**: Unit tests for logger functionality

### Scripts (`scripts/`)
- **`pull_data.py`**: Data synchronization script
  - Copies materials from OneDrive path to local backup
  - Uses the centralized logger from utils package
  - Handles both files and directories with proper error handling

## Course Structure

The course covers 7 main chapters:
1. Regression Analysis (Simple/multiple linear, ANOVA, residual analysis, variable selection)
2. Multivariate Analysis (Distributions, covariance matrices, missing data handling)
3. Principal Component Analysis (PCA)
4. Factor Analysis
5. Discriminant Analysis
6. Cluster Analysis
7. Multivariate Regression (Including logistic regression, MANOVA)

## Development Guidelines

- All scripts should use the centralized `setup_logger()` function from utils
- When adding new utilities, export them through `utils/__init__.py`
- Follow the existing error handling patterns seen in `pull_data.py`
- Use type hints as demonstrated in the logger module