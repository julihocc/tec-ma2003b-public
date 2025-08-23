"""5.1 Discrimination for two multivariate normal populations

Practice script: simulate two Gaussian populations, compute LDA coefficients
using pooled covariance, and evaluate classification performance.

This demonstrates the key concepts from the presentation:
- Two populations with equal covariance matrices
- Linear discriminant function: w^T x + b > 0
- Pooled covariance estimation
- Classification accuracy
"""

import numpy as np
from numpy.linalg import inv

np.random.seed(42)


def simulate_data(n=300, dim=3):
    """Simulate two multivariate normal populations with equal covariance."""

    # Population parameters
    mu0 = np.zeros(dim)
    mu1 = np.ones(dim) * 1.5
    cov = np.eye(dim)

    print("Two-Population Discriminant Analysis")
    print("===================================")
    print(f"Population π₀: μ₀ = {mu0}")
    print(f"Population π₁: μ₁ = {mu1}")
    print(f"Common covariance: identity matrix")

    # Generate samples
    n0 = n // 2
    n1 = n - n0

    X0 = np.random.multivariate_normal(mu0, cov, size=n0)
    X1 = np.random.multivariate_normal(mu1, cov, size=n1)

    X = np.vstack([X0, X1])
    y = np.hstack([np.zeros(n0, dtype=int), np.ones(n1, dtype=int)])

    print(f"Generated {n0} samples from π₀ and {n1} samples from π₁")
    return X, y


def train_lda(X, y):
    """Train Linear Discriminant Analysis classifier."""

    print("\nParameter Estimation:")
    print("====================")

    # Estimate sample means
    mu0_hat = X[y == 0].mean(axis=0)
    mu1_hat = X[y == 1].mean(axis=0)

    print(f"Sample mean μ̂₀ = {mu0_hat}")
    print(f"Sample mean μ̂₁ = {mu1_hat}")

    # Estimate sample covariances
    S0 = np.cov(X[y == 0], rowvar=False)
    S1 = np.cov(X[y == 1], rowvar=False)

    # Pooled covariance
    n0, n1 = np.sum(y == 0), np.sum(y == 1)
    pooled_cov = ((n0 - 1) * S0 + (n1 - 1) * S1) / (n0 + n1 - 2)

    print("Pooled covariance Σ̂:")
    print(pooled_cov)

    # Linear discriminant coefficients
    # w = Σ⁻¹(μ₁ - μ₀)
    # b = -½(μ₁ᵀΣ⁻¹μ₁ - μ₀ᵀΣ⁻¹μ₀)
    inv_cov = inv(pooled_cov)
    w = inv_cov @ (mu1_hat - mu0_hat)
    b = -0.5 * (mu1_hat.T @ inv_cov @ mu1_hat - mu0_hat.T @ inv_cov @ mu0_hat)

    print("\nLinear Discriminant Function:")
    print("============================")
    print("Classification rule: assign to π₁ if w^T x + b > 0")
    print(f"Coefficient vector w = {w}")
    print(f"Intercept b = {b:.4f}")

    return w, b


def predict_lda(X, w, b):
    """Make predictions using LDA classifier."""
    scores = X @ w + b
    predictions = (scores > 0).astype(int)
    return predictions, scores


def evaluate_classifier(y_true, y_pred):
    """Evaluate classification performance."""

    print("\nClassification Results:")
    print("======================")

    # Overall accuracy
    accuracy = (y_pred == y_true).mean()
    print(f"Accuracy: {accuracy:.4f}")

    # Confusion matrix
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    print("Confusion Matrix:")
    print(f"           Predicted")
    print(f"         π₀    π₁")
    print(f"Actual π₀ {tn:3d}  {fp:3d}")
    print(f"       π₁ {fn:3d}  {tp:3d}")

    # Error rates
    error_rate = 1 - accuracy
    print(f"Error rate: {error_rate:.4f}")

    return accuracy


def main():
    """Main function demonstrating two-population discriminant analysis."""

    # 1. Generate data
    X, y = simulate_data(n=300, dim=3)

    # 2. Train LDA classifier
    w, b = train_lda(X, y)

    # 3. Make predictions
    y_pred, scores = predict_lda(X, w, b)

    # 4. Evaluate performance
    accuracy = evaluate_classifier(y, y_pred)

    print("\nSummary:")
    print("========")
    print("✓ Simulated two multivariate normal populations")
    print("✓ Estimated parameters using pooled covariance")
    print("✓ Computed linear discriminant function")
    print("✓ Classified observations and evaluated accuracy")
    print(f"Final accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    main()
