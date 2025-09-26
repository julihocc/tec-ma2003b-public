#!/usr/bin/env python3
"""
Factor Rotation Example
From Factor Analysis Presentation - Varimax and Promax rotation
"""

import numpy as np
from factor_analyzer import FactorAnalyzer

# Simulate data that would produce our example loadings
np.random.seed(42)
X = np.random.randn(100, 3)

# Apply Factor Analysis with rotation
fa_no_rotation = FactorAnalyzer(n_factors=2, rotation=None)
fa_varimax = FactorAnalyzer(n_factors=2, rotation='varimax')

fa_no_rotation.fit(X)
fa_varimax.fit(X)

# Compare loadings before and after rotation
loadings_before = fa_no_rotation.loadings_
loadings_after = fa_varimax.loadings_

print("Before rotation:")
print(loadings_before)
print("\nAfter Varimax rotation:")
print(loadings_after)

# Other rotation options: 'promax', 'oblimin', 'quartimax'
fa_promax = FactorAnalyzer(n_factors=2, rotation='promax')
fa_promax.fit(X)
print("\nAfter Promax rotation:")
print(fa_promax.loadings_)