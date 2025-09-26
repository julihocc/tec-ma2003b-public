#!/usr/bin/env python3
"""
PCA Basic Example
From Factor Analysis Presentation - Basic PCA implementation
"""

import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

# Step 1: Create the data
X = np.array([[5, 3],
              [3, 1],
              [1, 3]])

# Step 2: Apply PCA
pca = PCA()
X_transformed = pca.fit_transform(X)

# Step 3: Get results
eigenvalues = pca.explained_variance_
eigenvectors = pca.components_.T
variance_ratio = pca.explained_variance_ratio_

print(f"Eigenvalues: {eigenvalues}")
print(f"PC1 explains {variance_ratio[0]:.1%} of variance")
print(f"Transformed data:\n{X_transformed}")