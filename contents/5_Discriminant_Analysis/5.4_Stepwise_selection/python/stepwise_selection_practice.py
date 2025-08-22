"""5.4 Stepwise selection (illustrative)

A tiny, illustrative forward-selection routine using accuracy as a selection criterion.
Not intended for production; show need for cross-validation.
"""

import numpy as np
from itertools import combinations


def forward_greedy(X, y, k=2):
    p = X.shape[1]
    selected = []
    for _ in range(k):
        best = None
        best_acc = -1
        for j in range(p):
            if j in selected:
                continue
            cand = selected + [j]
            # trivial classifier: majority class in selected dimensions
            preds = (X[:, cand].mean(axis=1) > X[:, cand].mean()).astype(int)
            acc = (preds == y).mean()
            if acc > best_acc:
                best_acc = acc
                best = j
        if best is None:
            break
        selected.append(best)
    return selected


if __name__ == "__main__":
    np.random.seed(3)
    X = np.random.randn(50, 5)
    y = (X[:, 0] + 0.5 * X[:, 2] > 0).astype(int)
    print("Selected features (greedy):", forward_greedy(X, y, k=3))
