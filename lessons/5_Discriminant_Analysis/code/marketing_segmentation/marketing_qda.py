# %%
# Marketing Segmentation QDA Comparison
# Chapter 5 - Discriminant Analysis Example
# Quadratic Discriminant Analysis for customer segmentation

# %%
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import (
    accuracy_score,
    auc,
    classification_report,
    confusion_matrix,
    roc_curve,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# %%
# Setup logging and paths
from utils import setup_logger

logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "marketing.csv"
qda_plot = script_dir / "marketing_qda_decision.png"
roc_plot = script_dir / "marketing_qda_roc.png"

logger.info("Starting marketing segmentation QDA analysis")

# %%
# Load customer data
logger.info("Loading customer segmentation data")
df = pd.read_csv(data_file)
logger.info(f"Dataset shape: {df.shape}")

# %%
# Prepare data for QDA
features = [
    "purchase_freq",
    "avg_order_value",
    "browsing_time",
    "cart_abandonment",
    "email_open_rate",
    "loyalty_points",
    "support_tickets",
    "social_engagement",
]

X = df[features]
y = df["segment"]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=features)

logger.info(f"Features: {features}")
logger.info(f"Target classes: {y.unique()}")

# %%
# Split data for validation
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

logger.info(f"Training set: {X_train.shape}, Test set: {X_test.shape}")

# %%
# Quadratic Discriminant Analysis
logger.info("Fitting Quadratic Discriminant Analysis")
qda = QuadraticDiscriminantAnalysis()
qda.fit(X_train, y_train)

print("\n=== Quadratic Discriminant Analysis Results ===")
print(f"Number of features: {qda.n_features_in_}")
print(f"Classes: {qda.classes_}")

# %%
# Predictions and evaluation
y_pred_qda = qda.predict(X_test)
qda_accuracy = accuracy_score(y_test, y_pred_qda)
y_prob_qda = qda.predict_proba(X_test)

print("\nQDA Classification Report:")
print(classification_report(y_test, y_pred_qda))

print(f"QDA Accuracy: {qda_accuracy:.3f}")

# Cross-validation
cv_scores_qda = cross_val_score(qda, X_scaled, y, cv=5)
print(
    f"QDA Cross-validation accuracy: {cv_scores_qda.mean():.3f} (+/- {cv_scores_qda.std() * 2:.3f})"
)

# %%
# Get discriminant scores (QDA doesn't provide discriminant functions like LDA)
# Instead, we can look at the log-likelihoods or posterior probabilities
print("\n=== Posterior Probabilities Analysis ===")
posterior_df = pd.DataFrame(y_prob_qda, columns=[f"P({cls})" for cls in qda.classes_])
posterior_df["Predicted"] = y_pred_qda
posterior_df["Actual"] = y_test.reset_index(drop=True)

print("Sample posterior probabilities:")
print(posterior_df.head(10))

# %%
# Confusion matrix
plt.figure(figsize=(8, 6))
cm_qda = confusion_matrix(y_test, y_pred_qda)
sns.heatmap(
    cm_qda,
    annot=True,
    fmt="d",
    cmap="Oranges",
    xticklabels=qda.classes_,
    yticklabels=qda.classes_,
)
plt.title(f"QDA Confusion Matrix\nAccuracy: {qda_accuracy:.3f}")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.tight_layout()
plt.savefig(script_dir / "marketing_qda_confusion.png", dpi=300, bbox_inches="tight")
plt.show()

# %%
# Decision boundaries visualization (2D projection)
plt.figure(figsize=(12, 8))

# Use first two features for visualization
X_vis = X_scaled[["purchase_freq", "avg_order_value"]].values
y_vis = y.values

# Fit QDA on 2D data for visualization
qda_2d = QuadraticDiscriminantAnalysis()
qda_2d.fit(X_vis, y_vis)

# Create mesh grid
x_min, x_max = X_vis[:, 0].min() - 1, X_vis[:, 0].max() + 1
y_min, y_max = X_vis[:, 1].min() - 1, X_vis[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Predict on mesh
Z = qda_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundaries
plt.contourf(xx, yy, Z, alpha=0.3, cmap="RdYlBu")

# Plot data points
colors = ["red", "blue", "green"]
segments = qda.classes_

for i, segment in enumerate(segments):
    mask = y_vis == segment
    plt.scatter(
        X_vis[mask, 0],
        X_vis[mask, 1],
        c=colors[i],
        label=f"{segment} Customers",
        alpha=0.7,
        edgecolors="black",
        s=50,
    )

plt.xlabel("Purchase Frequency (standardized)")
plt.ylabel("Average Order Value (standardized)")
plt.title("Customer Segmentation: QDA Decision Boundaries (2D View)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(qda_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved QDA decision boundaries plot to {qda_plot}")
plt.show()

# %%
# ROC Curves for multiclass classification
# Convert to binary classification problems (One-vs-Rest)
plt.figure(figsize=(10, 8))

colors = ["red", "blue", "green"]
segments = qda.classes_

for i, segment in enumerate(segments):
    # Create binary labels for this class
    y_binary = (y_test == segment).astype(int)
    y_prob_segment = y_prob_qda[:, i]

    # Calculate ROC curve
    fpr, tpr, _ = roc_curve(y_binary, y_prob_segment)
    roc_auc = auc(fpr, tpr)

    # Plot ROC curve
    plt.plot(
        fpr, tpr, color=colors[i], linewidth=2, label=f"{segment} (AUC = {roc_auc:.3f})"
    )

# Plot diagonal line
plt.plot([0, 1], [0, 1], "k--", linewidth=2)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("QDA ROC Curves: Customer Segmentation")
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(roc_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved ROC curves plot to {roc_plot}")
plt.show()

# %%
# Posterior probability distributions
plt.figure(figsize=(15, 5))

for i, segment in enumerate(segments):
    plt.subplot(1, 3, i + 1)

    # Get posterior probabilities for this class
    probs = y_prob_qda[:, i]

    # Plot distribution
    plt.hist(probs, bins=20, alpha=0.7, color=colors[i], edgecolor="black")
    plt.axvline(
        np.mean(probs),
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mean: {np.mean(probs):.3f}",
    )

    plt.xlabel("Posterior Probability")
    plt.ylabel("Frequency")
    plt.title(f"QDA Posterior Probabilities\n{segment} Customers")
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(script_dir / "marketing_qda_posteriors.png", dpi=300, bbox_inches="tight")
plt.show()

# %%
# Summary and interpretation
print("\n=== QDA Marketing Segmentation Summary ===")
print("1. QDA allows different covariance matrices for each customer segment")
print("2. More flexible than LDA but requires more parameters to estimate")
print(f"3. QDA Accuracy: {qda_accuracy:.3f}")
print("4. QDA provides posterior probabilities for classification confidence")
print("5. Decision boundaries are quadratic curves rather than linear")
print("6. Particularly useful when segments have different variability patterns")

# %%
# Compare with LDA (import and run LDA analysis)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
y_pred_lda = lda.predict(X_test)
lda_accuracy = accuracy_score(y_test, y_pred_lda)

print("\n=== LDA vs QDA Comparison ===")
print(f"LDA Accuracy: {lda_accuracy:.3f}")
print(f"QDA Accuracy: {qda_accuracy:.3f}")
print(f"Difference: {abs(qda_accuracy - lda_accuracy):.3f}")

if qda_accuracy > lda_accuracy:
    print(
        "QDA outperformed LDA, suggesting different covariance structures across segments"
    )
else:
    print(
        "LDA performed similarly or better, suggesting equal covariance assumption is reasonable"
    )

logger.info("Marketing segmentation QDA analysis completed")
print("\nQDA analysis complete! Check generated plots and summary statistics.")
