import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os

# Example data: Experience (X) vs. Salary (Y)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([35, 37, 39, 41, 44, 46, 48, 51, 53, 55])

data = pd.DataFrame({"X": X, "Y": Y})

# Fit regression model using formula API
model = smf.ols("Y ~ X", data=data).fit()

# ANOVA table
anova_table = sm.stats.anova_lm(model, typ=2)

# Confidence interval for the slope
conf_int = model.conf_int(alpha=0.05)

# Predict mean response and prediction interval for X=5
X_new = pd.DataFrame({"X": [5]})
pred = model.get_prediction(X_new)
summary_frame = pred.summary_frame(alpha=0.05)

# Write report to text file in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(script_dir, "anova_confidence_intervals_report.txt")
with open(report_path, "w") as f:
    f.write("Regression Summary:\n")
    f.write(str(model.summary()) + "\n\n")
    f.write("ANOVA Table:\n")
    f.write(str(anova_table) + "\n\n")
    f.write("95% Confidence Intervals for coefficients:\n")
    f.write(str(conf_int) + "\n\n")
    f.write("Prediction for X=5:\n")
    f.write(str(summary_frame) + "\n")
