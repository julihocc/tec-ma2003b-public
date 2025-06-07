import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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

# Output the results
print(f"Simple Linear Regression Practice Example")
print(f"---------------------------------------")
print(f"Independent Variable (X): Experience (Years)")
print(f"Dependent Variable (Y): Salary (in $1000s)")
print(f"---------------------------------------")
print(f"Estimated Intercept (b0): {b0:.2f}")
print(f"Estimated Slope (b1): {b1:.2f}")
print(f"Regression Equation: Y_hat = {b0:.2f} + {b1:.2f} * X")
print(f"---------------------------------------")
print(f"R-squared: {r_squared:.4f}")
print(f"---------------------------------------")
print("\nInstructions for students:")
print("1. Review the code to understand how linear regression is implemented.")
print("2. Run this Python script.")
print("3. Observe the output: intercept, slope, and R-squared value.")
print(
    "4. Interpret the meaning of the slope (b1): For each additional year of experience, what is the estimated increase in salary?"
)
print(
    "5. Interpret the meaning of the R-squared value: What percentage of the variation in salary is explained by experience?"
)
print(
    "6. (Optional) Modify the X and Y data with your own examples and see how the results change."
)
print(
    "7. (Optional) Plot the data points and the regression line using matplotlib (uncomment the plotting code below)."
)

# Optional: Plotting (students can uncomment this part)
# plt.figure(figsize=(10, 6))
# plt.scatter(X, Y, color='blue', label='Actual Data Points')
# plt.plot(X, Y_pred, color='red', linewidth=2, label='Regression Line')
# plt.title('Simple Linear Regression: Experience vs. Salary')
# plt.xlabel('Experience (Years)')
# plt.ylabel('Salary (in $1000s)')
# plt.legend()
# plt.grid(True)
# plt.show()

# Example of how to predict a new value
# new_experience = np.array([[12]]) # Predict salary for 12 years of experience
# predicted_salary = model.predict(new_experience)
# print(f"\nPredicted salary for {new_experience[0][0]} years of experience: ${predicted_salary[0]:.2f}k")
