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


# Backward selection function
def backward_selection(X, y):
    selected_features = list(X.columns)
    while len(selected_features) > 0:
        model = sm.OLS(y, sm.add_constant(X[selected_features])).fit()
        p_values = model.pvalues.iloc[1:]  # Exclude intercept
        max_p_value = p_values.max()
        if max_p_value > 0.05:
            worst_feature = p_values.idxmax()
            selected_features.remove(worst_feature)
        else:
            break
    return selected_features


# Perform backward selection
selected_features = backward_selection(X, y)

# Fit final model
final_model = sm.OLS(y, sm.add_constant(X[selected_features])).fit()

# Write results to a report
report_path = os.path.join(os.path.dirname(__file__), "backward_selection_report.txt")
with open(report_path, "w") as report:
    report.write("Backward Selection Report\n")
    report.write("=" * 30 + "\n")
    report.write(f"Selected Features: {selected_features}\n\n")
    report.write(f"Model Summary:\n{final_model.summary()}\n")

print("Practice script executed successfully. Check the generated report.")
