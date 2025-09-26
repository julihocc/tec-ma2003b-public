#!/usr/bin/env python3
"""
Complete Factor Analysis Workflow
From Factor Analysis Presentation - End-to-end analysis pipeline
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
import matplotlib.pyplot as plt

# 1. Load and prepare data
# X = pd.read_csv('your_data.csv')  # Your actual data
X = np.random.randn(100, 5)  # Simulated data for demo

# 2. Standardize if needed
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Check suitability for factor analysis
kmo_all, kmo_model = calculate_kmo(X_scaled)
chi_square_value, p_value = calculate_bartlett_sphericity(X_scaled)

print(f"KMO: {kmo_model:.3f} (>0.6 is good)")
print(f"Bartlett's test p-value: {p_value:.3f} (<0.05 is good)")

# 4. Determine number of factors
pca = PCA()
pca.fit(X_scaled)
eigenvalues = pca.explained_variance_
n_factors = sum(eigenvalues > 1)  # Kaiser criterion

print(f"Suggested factors: {n_factors}")

# 5. Perform Factor Analysis with rotation
fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax')
fa.fit(X_scaled)

# 6. Get and interpret results
loadings = fa.loadings_
communalities = fa.get_communalities()
variance_explained = fa.get_factor_variance()

print(f"Factor loadings:\n{loadings}")
print(f"Communalities: {communalities}")
print(f"Variance explained: {variance_explained[1]}")  # Proportional variance

# 7. Compare with PCA
pca_result = pca.transform(X_scaled)
fa_scores = fa.transform(X_scaled)

print("\nPCA vs FA comparison completed!")