#!/usr/bin/env python3
"""
Factor Analysis Basic Example
From Factor Analysis Presentation - Basic FA implementation
"""

import numpy as np
from factor_analyzer import FactorAnalyzer
from sklearn.datasets import make_spd_matrix

# Create correlation matrix (our example)
R = np.array([[1.00, 0.60, 0.48],
              [0.60, 1.00, 0.72],
              [0.48, 0.72, 1.00]])

# For real data, you'd start with raw data:
# X = your_data  # shape (n_samples, n_features)
# R = np.corrcoef(X.T)  # correlation matrix

# Perform Factor Analysis
fa = FactorAnalyzer(n_factors=1, rotation=None)
fa.fit(R)  # For correlation matrix
# fa.fit(X)  # For raw data

# Get results
loadings = fa.loadings_
communalities = fa.get_communalities()
uniqueness = fa.get_uniquenesses()

print(f"Factor loadings:\n{loadings}")
print(f"Communalities: {communalities}")
print(f"Uniqueness: {uniqueness}")

print("\nNote: Install with: pip install factor_analyzer")