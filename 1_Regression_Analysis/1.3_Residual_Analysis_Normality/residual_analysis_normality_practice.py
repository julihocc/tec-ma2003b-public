import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import shapiro
import os

# Generate synthetic data for demonstration
np.random.seed(42)
X = np.random.rand(100, 1) * 10
X = sm.add_constant(X)  # Add intercept
beta = [2, 0.5]
y = np.dot(X, beta) + np.random.normal(0, 1, size=100)

# Fit a linear regression model
model = sm.OLS(y, X).fit()
residuals = model.resid

# Plot residuals vs. fitted values
residuals_vs_fitted_path = os.path.join(
    os.path.dirname(__file__), "residuals_vs_fitted.png"
)
plt.scatter(model.fittedvalues, residuals, alpha=0.7)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs. Fitted Values")
plt.savefig(residuals_vs_fitted_path)
plt.show()
plt.close()

# Histogram of residuals
residuals_histogram_path = os.path.join(
    os.path.dirname(__file__), "residuals_histogram.png"
)
plt.hist(residuals, bins=15, edgecolor="black", alpha=0.7)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Histogram of Residuals")
plt.savefig(residuals_histogram_path)
plt.show()
plt.close()

# Perform Shapiro-Wilk test for normality
stat, p_value = shapiro(residuals)

# Write results to a report
report_path = os.path.join(os.path.dirname(__file__), "residual_analysis_report.txt")
with open(report_path, "w") as report:
    report.write("Residual Analysis Report\n")
    report.write("=" * 30 + "\n")
    report.write(f"Model Summary:\n{model.summary()}\n\n")
    report.write("Normality Test (Shapiro-Wilk):\n")
    report.write(f"Statistic: {stat:.4f}, p-value: {p_value:.4f}\n")
    if p_value > 0.05:
        report.write("Residuals appear to be normally distributed.\n")
    else:
        report.write("Residuals do not appear to be normally distributed.\n")

print("Practice script executed successfully. Check the generated report and plots.")
