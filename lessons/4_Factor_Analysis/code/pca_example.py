"""
Simple PCA example for the course materials.
Saves a scree plot and prints eigenvalues + explained variance.
Requires: numpy, matplotlib, scikit-learn
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Small synthetic dataset (5 variables, 100 samples)
rng = np.random.RandomState(0)
n_samples = 100
# Construct two latent factors and unique noise
f1 = rng.normal(size=(n_samples, 1))
f2 = rng.normal(size=(n_samples, 1))
X = np.hstack(
    [
        0.9 * f1 + 0.1 * rng.normal(size=(n_samples, 1)),
        0.8 * f1 + 0.2 * rng.normal(size=(n_samples, 1)),
        0.7 * f2 + 0.3 * rng.normal(size=(n_samples, 1)),
        0.6 * f2 + 0.4 * rng.normal(size=(n_samples, 1)),
        rng.normal(size=(n_samples, 1)),
    ]
)

# Standardize (use correlation matrix behavior)
Xs = StandardScaler().fit_transform(X)

pca = PCA()
Z = pca.fit_transform(Xs)
eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# Scree plot
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
plt.savefig("lessons/4_Factor_Analysis/code/pca_scree.png", dpi=150)
print("Scree plot saved to lessons/4_Factor_Analysis/code/pca_scree.png")
