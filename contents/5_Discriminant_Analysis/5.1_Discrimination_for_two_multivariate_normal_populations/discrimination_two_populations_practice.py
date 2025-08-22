"""5.1 Discrimination for two multivariate normal populations

Small runnable demo: simulate two Gaussians, compute LDA linear rule (pooled covariance)
and report simple classification accuracy.
"""

import numpy as np
from numpy.linalg import inv

np.random.seed(1)


def simulate(n=200, dim=2, mu0=None, mu1=None, cov=None):
    if mu0 is None:
        mu0 = np.zeros(dim)
    if mu1 is None:
        mu1 = np.ones(dim) * 1.5
    if cov is None:
        cov = np.eye(dim)
    n0 = n // 2
    n1 = n - n0
    X0 = np.random.multivariate_normal(mu0, cov, size=n0)
    X1 = np.random.multivariate_normal(mu1, cov, size=n1)
    X = np.vstack([X0, X1])
    y = np.hstack([np.zeros(n0, dtype=int), np.ones(n1, dtype=int)])
    return X, y


def lda_train(X, y):
    mu0 = X[y == 0].mean(axis=0)
    mu1 = X[y == 1].mean(axis=0)
    S0 = np.cov(X[y == 0], rowvar=False)
    S1 = np.cov(X[y == 1], rowvar=False)
    n = len(y)
    pooled = ((X[y == 0].shape[0] - 1) * S0 + (X[y == 1].shape[0] - 1) * S1) / (n - 2)
    w = inv(pooled).dot(mu1 - mu0)
    b = -0.5 * (mu1.dot(inv(pooled)).dot(mu1) - mu0.dot(inv(pooled)).dot(mu0))
    return w, b, mu0, mu1


def predict(X, w, b):
    return (X.dot(w) + b > 0).astype(int)


def main():
    X, y = simulate(n=300, dim=3)
    w, b, _, _ = lda_train(X, y)
    yhat = predict(X, w, b)
    acc = (yhat == y).mean()
    print(f"LDA accuracy (simulated 3-d): {acc:.3f}")


if __name__ == '__main__':
    main()
