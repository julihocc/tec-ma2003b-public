#!/usr/bin/env python3
"""
Component Retention Example
From Factor Analysis Presentation - Kaiser criterion and scree plot
"""

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Simulated data with 5 variables
np.random.seed(42)
X = np.random.randn(100, 5)

# Apply PCA
pca = PCA()
pca.fit(X)

eigenvalues = pca.explained_variance_
cumvar = pca.explained_variance_ratio_.cumsum()

# Kaiser criterion
n_kaiser = sum(eigenvalues > 1)

# Cumulative variance (80% threshold)
n_cumvar = np.argmax(cumvar >= 0.8) + 1

print(f"Kaiser criterion: {n_kaiser} components")
print(f"80% variance: {n_cumvar} components")
print(f"Cumulative variance: {cumvar}")

# Scree plot
plt.figure(figsize=(8, 6))
plt.plot(range(1, 6), eigenvalues, 'bo-')
plt.axhline(y=1, color='r', linestyle='--')
plt.title('Scree Plot')
plt.xlabel('Component Number')
plt.ylabel('Eigenvalue')
plt.grid(True)

# Save plot instead of showing (for non-interactive environments)
try:
    plt.savefig('scree_plot.png', dpi=150, bbox_inches='tight')
    print("Scree plot saved as 'scree_plot.png'")
except:
    pass

# Try to show plot if in interactive environment
try:
    plt.show()
except:
    pass