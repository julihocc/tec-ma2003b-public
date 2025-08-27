# %% [markdown]
"""
PCA example (py-percent style)

This script demonstrates a minimal PCA workflow using a small synthetic
dataset. It is split into py-percent cells so you can run it interactively
in editors that support the Run Cell feature (for example, VS Code).

High-level steps:
- build a synthetic dataset with two latent factors and additive noise
- optionally standardize variables
- fit PCA, inspect eigenvalues and explained-variance ratios
- save a scree plot to a PNG file

Requirements: numpy, matplotlib, scikit-learn

Contract (what this script expects and produces):
- Inputs (variables you can edit in the Parameters cell):
    - n_samples: int, number of simulated observations
    - random_seed: int, RNG seed for reproducible simulation
    - save_path: str, path to write the scree plot image
    - standardize: bool, whether to z-score variables before PCA
- Outputs (printed and written files):
    - printed eigenvalues, explained ratios, and cumulative explained
    - a scree plot saved to `save_path`

Edge cases and notes:
- PCA is applied to the preprocessed matrix `Xs` (same shape as `X`).
- If `n_samples` is small relative to the number of variables the
    eigenvalue estimates may be noisy. This script does not perform
    cross-validation or statistical testing — it's meant for pedagogy.
"""

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# %% [markdown]
# Parameters
# Edit these variables before executing the rest of the notebook-style cells.
# - n_samples: number of simulated observations (rows)
# - random_seed: RNG seed for reproducibility
# - save_path: file path where the scree plot will be saved
# - standardize: if True, variables are z-scored before PCA (recommended)

# %%

n_samples = 100
random_seed = 0
# Build a robust path for the output image. The file will be placed next to
# this script by default which makes the location independent of the current
# working directory used to run the script. Use Path to allow safe path
# manipulations and mkdir to create parent folders if they don't exist.
save_path = Path(__file__).resolve().parent / "pca_scree.png"
standardize = True

# Quick parameter summary printed for the user. This is harmless to leave on
# in scripts executed non-interactively.
print(
    f"Parameters: n_samples={n_samples}, random_seed={random_seed}, standardize={standardize}"
)

# Make sure the destination directory exists so saving the figure won't fail
save_path.parent.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# Build synthetic dataset
#
# We create two latent factors (f1, f2). Each observed variable is a linear
# combination of one factor plus Gaussian noise. This produces a small
# multivariate dataset where the first two components should capture most of
# the variance.

# %%
rng = np.random.RandomState(random_seed)
# Two latent factors (column vectors with n_samples rows)
f1 = rng.normal(size=(n_samples, 1))
f2 = rng.normal(size=(n_samples, 1))

# Observed variables (5 columns): the first 4 are noisy loadings on f1/f2
# and the last is an independent noise variable. Keep the stacking explicit so
# the data shape is clearly (n_samples, n_features).
X = np.hstack(
    [
        0.9 * f1 + 0.1 * rng.normal(size=(n_samples, 1)),  # variable 1 ~ f1
        0.8 * f1 + 0.2 * rng.normal(size=(n_samples, 1)),  # variable 2 ~ f1
        0.7 * f2 + 0.3 * rng.normal(size=(n_samples, 1)),  # variable 3 ~ f2
        0.6 * f2 + 0.4 * rng.normal(size=(n_samples, 1)),  # variable 4 ~ f2
        rng.normal(size=(n_samples, 1)),  # variable 5 is pure noise
    ]
)

print("Data shape:", X.shape)  # (n_samples, n_features)

# %% [markdown]
# Preprocess and run PCA
#
# - If `standardize` is True we z-score each column so variables with different
#   scales do not dominate the PCA. If False we simply center by the mean.
# - `pca.explained_variance_` holds the eigenvalues of the covariance matrix
#   (or correlation matrix if standardized).

# %%
if standardize:
    # StandardScaler returns an array with the same shape as X. Each column
    # will have mean ~0 and variance ~1 (sample variance with n-1 denom).
    Xs = StandardScaler().fit_transform(X)
else:
    # Centering only (useful to inspect raw-variance PCA)
    Xs = X - X.mean(axis=0)

# Fit PCA to the preprocessed data. PCA().fit_transform returns the
# scores Z with shape (n_samples, n_components). By default n_components = min(n_samples, n_features).
pca = PCA()
Z = pca.fit_transform(Xs)
eigenvalues = pca.explained_variance_
explained_ratio = pca.explained_variance_ratio_

# Print rounded summaries: eigenvalues, explained ratio per component, and
# the cumulative explained variance which helps decide how many components to keep.
print("Eigenvalues:", np.round(eigenvalues, 3))
print("Explained ratio:", np.round(explained_ratio, 3))
print("Cumulative:", np.round(np.cumsum(explained_ratio), 3))

# %% [markdown]
# Scree plot
#
# The scree plot displays eigenvalues by component index. A steep drop after
# the first components followed by a long tail is a classical visual cue that
# only the first few components are relevant.

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
