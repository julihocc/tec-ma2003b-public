# 5.1 Discrimination for Two Multivariate Normal Populations

This folder contains materials for Topic 5.1: Linear Discriminant Analysis for two populations with equal covariance matrices.

## Folder Structure

### 📄 `discrimination_two_populations_report.txt`
Brief exercise description and learning objectives.

### 📁 `latex/`
LaTeX beamer presentation and compiled files:
- `discrimination_two_populations.tex` - Source presentation file
- `discrimination_two_populations.pdf` - Compiled presentation
- Other LaTeX auxiliary files (.aux, .log, .nav, etc.)

### 📁 `python/`
Python implementation and tests:
- `discrimination_two_populations_practice.py` - Main practice script (simplified for 2-hour class)
- `test_discrimination_two_populations.py` - Unit tests

### 📁 `julia/`
Julia pseudocode-style implementation:
- `discrimination_two_populations_practice.jl` - Mathematical pseudocode version

## Usage

**For LaTeX presentation:**
```bash
cd latex/
pdflatex discrimination_two_populations.tex
```

**For Python practice:**
```bash
cd python/
python discrimination_two_populations_practice.py
```

**For Julia practice:**
```bash
cd julia/
julia discrimination_two_populations_practice.jl
```

## Learning Objectives

- Understand Linear Discriminant Analysis for two populations
- Implement Bayes optimal classifier with equal covariances
- Compute linear decision boundaries using pooled covariance
- Evaluate classification performance with confusion matrices
- Connect mathematical theory to practical implementation