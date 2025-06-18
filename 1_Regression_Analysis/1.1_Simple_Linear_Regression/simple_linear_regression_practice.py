import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# Sample Data
# Experience (Years)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# Salary (in $1000s)
Y = np.array([30, 35, 40, 48, 55, 60, 62, 68, 70, 75])

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, Y)

# Get the coefficients
b0 = model.intercept_
b1 = model.coef_[0]

# Predict Y values
Y_pred = model.predict(X)

# Calculate R-squared
r_squared = model.score(X, Y)

# --- Write results to a report file ---
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path for report.txt in the same directory as the script
report_file_path = os.path.join(script_dir, "simple_linear_regression_report.txt")

with open(report_file_path, "w") as f:
    f.write("Simple Linear Regression Practice Example\n")
    f.write("---------------------------------------\n")
    f.write("Independent Variable (X): Experience (Years)\n")
    f.write("Dependent Variable (Y): Salary (in $1000s)\n")
    f.write("---------------------------------------\n")
    f.write(f"Estimated Intercept (b0): {b0:.2f}\n")
    f.write(f"Estimated Slope (b1): {b1:.2f}\n")
    f.write(f"Regression Equation: Y_hat = {b0:.2f} + {b1:.2f} * X\n")
    f.write("---------------------------------------\n")
    f.write(f"R-squared: {r_squared:.4f}\n")
    f.write("---------------------------------------\n")

    # Example of how to predict a new value - also written to file
    new_experience_value = 12
    new_experience_array = np.array([[new_experience_value]])
    predicted_salary_for_new = model.predict(new_experience_array)
    f.write(
        f"\nPredicted salary for {new_experience_value} years of experience: ${predicted_salary_for_new[0]:.2f}k\n"
    )
# --- End of writing results to report file ---

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color="blue", label="Actual Data Points")
plt.plot(X, Y_pred, color="red", linewidth=2, label="Regression Line")
plt.title("Simple Linear Regression: Experience vs. Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (in $1000s)")
plt.legend()
plt.grid(True)
plt.show()
