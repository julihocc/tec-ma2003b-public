# %%
# Marketing Segmentation Discriminant Analysis
# Chapter 5 - Discriminant Analysis Example
# Customer behavior classification using LDA and QDA

# %%
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis,
)
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# %%
# Setup logging and paths
from utils import setup_logger

logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "marketing.csv"
scores_plot = script_dir / "marketing_scores.png"
boundaries_plot = script_dir / "marketing_boundaries.png"

logger.info("Starting marketing segmentation discriminant analysis")

# %%
# Load customer data
logger.info("Loading customer segmentation data")
df = pd.read_csv(data_file)
logger.info(f"Dataset shape: {df.shape}")
logger.info(f"Columns: {list(df.columns)}")

# %%
# Data exploration
print("=== Customer Segmentation Dataset ===")
print(f"Total customers: {len(df)}")
print(f"Segments: {df['segment'].unique()}")
print("\nSegment distribution:")
print(df["segment"].value_counts())

print("\nFeature summary:")
print(df.describe())

# %%
# Prepare data for discriminant analysis
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
# Linear Discriminant Analysis
logger.info("Fitting Linear Discriminant Analysis")
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# Get discriminant scores for training data
X_lda = lda.transform(X_train)
lda_scores_df = pd.DataFrame(
    X_lda, columns=[f"LD{i + 1}" for i in range(X_lda.shape[1])]
)
lda_scores_df["segment"] = y_train.reset_index(drop=True)

print("\n=== Linear Discriminant Analysis Results ===")
print(f"Number of discriminant functions: {lda.n_features_in_}")
print(f"Classes: {lda.classes_}")
print(f"Explained variance ratios: {lda.explained_variance_ratio_}")

# %%
# Predictions and evaluation
y_pred_lda = lda.predict(X_test)
lda_accuracy = accuracy_score(y_test, y_pred_lda)

print("\nLDA Classification Report:")
print(classification_report(y_test, y_pred_lda))

print(f"LDA Accuracy: {lda_accuracy:.3f}")

# Cross-validation
cv_scores_lda = cross_val_score(lda, X_scaled, y, cv=5)
print(
    f"LDA Cross-validation accuracy: {cv_scores_lda.mean():.3f} (+/- {cv_scores_lda.std() * 2:.3f})"
)

# %%
# Quadratic Discriminant Analysis
logger.info("Fitting Quadratic Discriminant Analysis")
qda = QuadraticDiscriminantAnalysis()
qda.fit(X_train, y_train)

y_pred_qda = qda.predict(X_test)
qda_accuracy = accuracy_score(y_test, y_pred_qda)

print("\n=== Quadratic Discriminant Analysis Results ===")
print("QDA Classification Report:")
print(classification_report(y_test, y_pred_qda))

print(f"QDA Accuracy: {qda_accuracy:.3f}")

cv_scores_qda = cross_val_score(qda, X_scaled, y, cv=5)
print(
    f"QDA Cross-validation accuracy: {cv_scores_qda.mean():.3f} (+/- {cv_scores_qda.std() * 2:.3f})"
)

# %%
# Discriminant function coefficients interpretation
print("\n=== Discriminant Function Coefficients ===")
coef_df = pd.DataFrame(
    lda.scalings_,
    index=features,
    columns=[f"LD{i + 1}" for i in range(lda.scalings_.shape[1])],
)
print("Coefficients (standardized):")
print(coef_df.round(3))

# %%
# Group means on discriminant functions
print("\n=== Group Means on Discriminant Functions ===")
means_df = pd.DataFrame(lda.means_, index=lda.classes_, columns=features)
print(means_df.round(3))

# %%
# Visualization: Discriminant scores
plt.figure(figsize=(12, 8))

# Plot first two discriminant functions
colors = ["red", "blue", "green"]
segments = lda.classes_

for i, segment in enumerate(segments):
    mask = lda_scores_df["segment"] == segment
    plt.scatter(
        lda_scores_df.loc[mask, "LD1"],
        lda_scores_df.loc[mask, "LD2"],
        c=colors[i],
        label=f"{segment} Customers",
        alpha=0.7,
        s=50,
    )

# Add group centroids
centroids = lda.transform(lda.means_)
for i, segment in enumerate(segments):
    plt.scatter(
        centroids[i, 0],
        centroids[i, 1],
        c=colors[i],
        marker="x",
        s=200,
        linewidth=3,
        label=f"{segment} Centroid",
    )

plt.xlabel("First Linear Discriminant (LD1)")
plt.ylabel("Second Linear Discriminant (LD2)")
plt.title("Customer Segmentation: Discriminant Function Scores")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(scores_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved discriminant scores plot to {scores_plot}")
plt.show()

# %%
# Decision boundaries visualization (simplified 2D view)
# Note: Contour plotting can be complex with categorical predictions
# Using scatter plot instead for clearer visualization

plt.figure(figsize=(10, 8))

# Use first two features for visualization
X_vis = X_scaled[["purchase_freq", "avg_order_value"]].values
y_vis = y.values

# Plot data points colored by actual segment
colors = ["red", "blue", "green"]
segments = np.unique(y_vis)

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
plt.title("Customer Segmentation: Feature Space Distribution")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(boundaries_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved feature space plot to {boundaries_plot}")
plt.show()

# %%
# Confusion matrices
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# LDA confusion matrix
cm_lda = confusion_matrix(y_test, y_pred_lda)
sns.heatmap(
    cm_lda,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=lda.classes_,
    yticklabels=lda.classes_,
    ax=ax1,
)
ax1.set_title(f"LDA Confusion Matrix\nAccuracy: {lda_accuracy:.3f}")
ax1.set_ylabel("True Label")
ax1.set_xlabel("Predicted Label")

# QDA confusion matrix
cm_qda = confusion_matrix(y_test, y_pred_qda)
sns.heatmap(
    cm_qda,
    annot=True,
    fmt="d",
    cmap="Oranges",
    xticklabels=qda.classes_,
    yticklabels=qda.classes_,
    ax=ax2,
)
ax2.set_title(f"QDA Confusion Matrix\nAccuracy: {qda_accuracy:.3f}")
ax2.set_ylabel("True Label")
ax2.set_xlabel("Predicted Label")

plt.tight_layout()
plt.savefig(
    script_dir / "marketing_confusion_matrices.png", dpi=300, bbox_inches="tight"
)
plt.show()

# %%
# Summary and interpretation
print("\n=== Marketing Segmentation Summary ===")
print("1. Discriminant Analysis successfully classified customers into segments")
print("2. LDA assumes equal covariance matrices across groups")
print("3. QDA allows different covariance matrices for more flexibility")
print(f"4. LDA Accuracy: {lda_accuracy:.3f}, QDA Accuracy: {qda_accuracy:.3f}")
print("5. First discriminant function separates high-value from low-value customers")
print("6. Second discriminant function distinguishes loyal from occasional buyers")

logger.info("Marketing segmentation discriminant analysis completed")
print("\nAnalysis complete! Check generated plots and summary statistics.")
