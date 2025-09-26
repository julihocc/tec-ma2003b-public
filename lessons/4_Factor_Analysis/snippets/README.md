# Factor Analysis Python Snippets

This folder contains all Python code snippets extracted from the Factor Analysis presentation.

## Files

1. **01_pca_basic_example.py** - Basic PCA implementation with simple data
2. **02_component_retention.py** - Component retention methods (Kaiser criterion, scree plot)
3. **03_factor_analysis_basic.py** - Basic Factor Analysis with correlation matrix
4. **04_factor_rotation.py** - Factor rotation examples (Varimax, Promax)
5. **05_complete_workflow.py** - Complete end-to-end factor analysis workflow

## Requirements

Install required packages:
```bash
pip install numpy pandas scikit-learn matplotlib factor-analyzer
```

## Running the Examples

Each file can be run independently:
```bash
python 01_pca_basic_example.py
python 02_component_retention.py
python 03_factor_analysis_basic.py
python 04_factor_rotation.py
python 05_complete_workflow.py
```

## Test All Snippets

Run the test script to verify all snippets work:
```bash
python test_all_snippets.py
```