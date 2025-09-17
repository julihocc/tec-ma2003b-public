# AI Manifest - MA2003B Application of Multivariate Methods

**Version:** 1.5.0  
**Repository:** tec-ma2003b-public  
**Created:** September 11, 2025  
**Last Updated:** September 11, 2025

## Overview

This is a comprehensive multivariate statistical analysis course repository with Factor Analysis business case evaluation system. The project serves as an educational platform for MA2003B - Application of Multivariate Methods in Data Science.

## Course Information

| Field | Value |
|-------|-------|
| **Course Code** | MA2003B |
| **Title** | Application of Multivariate Methods in Data Science |
| **Discipline** | Mathematics |
| **School** | Engineering and Sciences |
| **Prerequisites** | MA1036, TC2004B |
| **Credit Hours** | 5 |
| **Level** | Intermediate |

## Repository Structure

### 📚 Lessons

- **Description:** Course content organized by chapters with presentations and code examples
- **Active Chapters:** 4_Factor_Analysis
- **Structure:**
  - `lesson/` - Presentations and theoretical content
  - `code/` - Working examples and practice scripts

### 📊 Evaluations

- **Type:** Git submodule (private repository)
- **Repository:** [tec-ma2003b-evaluations](https://github.com/julihocc/tec-ma2003b-evaluations)
- **Description:** Comprehensive business case studies and assessment frameworks

#### Factor Analysis Business Case

- **Weight:** 5% of course grade
- **Duration:** 1 week intensive
- **Team Size:** 2-3 students
- **Deliverables:**
  - Jupyter notebook with technical analysis
  - Executive report with business recommendations
  - Presentation video demonstrating findings

### 🔧 Utils

- **Description:** Shared utilities and logging framework
- **Key Files:** `logger.py`, `__init__.py`

### 🤖 Scripts

- **Description:** Automation and data management scripts
- **Key Files:** `pull_data.py`

## Key Features

### Educational Frameworks

- Comprehensive Factor Analysis business case simulation
- Multi-dimensional assessment rubrics with 5-level performance anchors
- Synthetic dataset generation for customer satisfaction analysis
- Professional consulting simulation with executive deliverables

### Technical Stack

- **Python Scientific Computing:** pandas, numpy, scikit-learn
- **Factor Analysis:** factor_analyzer package for specialized methods
- **Interactive Development:** py-percent cells for VS Code/Jupyter integration
- **Notebook Integration:** jupytext for seamless conversion

### Assessment System

- **60%** Technical rigor and statistical methodology
- **25%** Business application and practical insights
- **15%** Communication and presentation quality
- Additional focus on:
  - Collaborative team evaluation
  - Professional presentation skills development
  - Real-world business problem solving

## Development Setup

| Component | Requirement |
|-----------|-------------|
| **Python Version** | ≥3.10 |
| **Environment** | `.venv` (virtual environment) |
| **Installation** | `pip install -e .` (editable mode) |
| **Testing** | `pytest -q` |
| **Interactive Mode** | py-percent cells for VS Code/Jupyter integration |

## Recent Updates

### Version 1.5.0 (September 11, 2025)

- Updated Factor Analysis business case for 5% weight and 1-week timeline
- Complete English localization of all educational materials
- Enhanced assessment framework with refined evaluation structure
- Systematic version management across repository

## AI Agent Guidance

### Primary Instructions

- **Main File:** `.github/copilot-instructions.md`
- Contains comprehensive coding patterns and project conventions

### Coding Patterns

- Use `utils.logger` for consistent logging across scripts
- Write human-readable report files next to practice scripts
- Preserve py-percent cell boundaries for interactive development
- Use `pathlib.Path` for robust file paths in examples

### Project Conventions

- Maintain `lesson/` folder structure for teaching materials
- Update `requirements.txt` when adding dependencies
- Follow clean git commit organization
- Preserve educational scaffolding and assessment rigor

## Repository Information

| Field | Value |
|-------|-------|
| **Owner** | julihocc |
| **Repository** | tec-ma2003b-public |
| **Primary Branch** | main |
| **Feature Branches** | ch4-biz-case |

## Contact & Contribution

This repository is maintained as part of the MA2003B course curriculum. For questions or contributions, please refer to the repository owner and follow the established educational guidelines.

---

*This manifest serves as a comprehensive guide for AI agents and developers working within the MA2003B educational repository ecosystem.*