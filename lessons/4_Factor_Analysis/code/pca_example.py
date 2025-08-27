# %% [markdown]
"""
PCA example (py-percent style)

This file is organized with "# %%" cell markers so you can run it interactively
in VS Code (Run Cell) or convert it to a notebook. The script:

- builds a small synthetic dataset with two latent factors and noise
- standardizes the variables
- fits PCA and prints eigenvalues and explained-variance ratios
- saves a scree plot to `lessons/4_Factor_Analysis/code/pca_scree.png`

Requirements: numpy, matplotlib, scikit-learn
"""

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# %% [markdown]
# Parameters (edit these interactively before running the next cells)
# - n_samples: number of simulated observations
# - random_seed: reproducible RNG seed
# - save_path: where to save the scree plot
# - standardize: whether to standardize variables before PCA

# %%
n_samples = 100
random_seed = 0
save_path = "lessons/4_Factor_Analysis/code/pca_scree.png"
standardize = True

print(
    f"Parameters: n_samples={n_samples}, random_seed={random_seed}, standardize={standardize}"
)

# %% [markdown]
# Build synthetic dataset

# %%
rng = np.random.RandomState(random_seed)
# Two latent factors with variation in loadings
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

print("Data shape:", X.shape)

# %% [markdown]
# Preprocess and run PCA

# %%
if standardize:
    Xs = StandardScaler().fit_transform(X)
else:
    Xs = X - X.mean(axis=0)

pca = PCA()
Z = pca.fit_transform(Xs)
eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# %% [markdown]
# Scree plot (run this cell to generate the figure)

# %%
plt.figure(figsize=(6, 3))
components = np.arange(1, len(eigenvalues) + 1)
plt.plot(components, eigenvalues, "o-", lw=2)
plt.xticks(components)
plt.xlabel("Component")
plt.ylabel("Eigenvalue")
plt.title("Scree plot")
plt.grid(True, ls=":")
plt.tight_layout()
plt.savefig(save_path, dpi=150)
print(f"Scree plot saved to {save_path}")
