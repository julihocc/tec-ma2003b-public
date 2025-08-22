"""5.5 Canonical discriminant functions

Compute between/within scatter matrices and solve generalized eigenproblem.
"""

import numpy as np
from numpy.linalg import eig, inv


def canonical(X, y):
    classes = np.unique(y)
    p = X.shape[1]
    overall = X.mean(axis=0)
    S_w = np.zeros((p, p))
    S_b = np.zeros((p, p))
    for c in classes:
        Xc = X[y == c]
        nc = Xc.shape[0]
        meanc = Xc.mean(axis=0)
        S_w += (nc - 1) * np.cov(Xc, rowvar=False)
        d = (meanc - overall).reshape(-1, 1)
        S_b += nc * d.dot(d.T)
    vals, vecs = eig(inv(S_w).dot(S_b))
    idx = np.argsort(vals)[::-1]
    return vals[idx], vecs[:, idx]


if __name__ == "__main__":
    np.random.seed(4)
    X = np.vstack([np.random.randn(30, 4) + i for i in range(3)])
    y = np.hstack([[i] * 30 for i in range(3)])
    vals, vecs = canonical(X, y)
    print("Leading eigenvalues:", vals[:2])
