import numpy as np
import pandas as pd
import statsmodels.api as sm
import os

# Generate synthetic data for demonstration
np.random.seed(42)
X = pd.DataFrame(
    {
        "X1": np.random.rand(100) * 10,
        "X2": np.random.rand(100) * 10,
        "X3": np.random.rand(100) * 10,
    }
)
y = 2 + 0.5 * X["X1"] + 0.3 * X["X2"] + np.random.normal(0, 1, size=100)


# Forward selection function
def forward_selection(X, y):
    selected_features = []
    remaining_features = list(X.columns)
    current_score, best_new_score = float("inf"), float("inf")

    while remaining_features:
        scores_with_candidates = []
        for candidate in remaining_features:
            model = sm.OLS(y, sm.add_constant(X[selected_features + [candidate]])).fit()
            score = model.aic
            scores_with_candidates.append((score, candidate))

        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates[0]

        if current_score > best_new_score:
            remaining_features.remove(best_candidate)
            selected_features.append(best_candidate)
            current_score = best_new_score
        else:
            break

    return selected_features


# Perform forward selection
selected_features = forward_selection(X, y)

# Fit final model
final_model = sm.OLS(y, sm.add_constant(X[selected_features])).fit()

# Write results to a report
report_path = os.path.join(os.path.dirname(__file__), "forward_selection_report.txt")
with open(report_path, "w") as report:
    report.write("Forward Selection Report\n")
    report.write("=" * 30 + "\n")
    report.write(f"Selected Features: {selected_features}\n\n")
    report.write(f"Model Summary:\n{final_model.summary()}\n")

print("Practice script executed successfully. Check the generated report.")
