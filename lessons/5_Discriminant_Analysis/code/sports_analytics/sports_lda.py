# %%
# Sports Analytics Discriminant Analysis
# Chapter 5 - Discriminant Analysis Example
# Athlete performance classification using LDA and QDA

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
from utils import setup_logger

warnings.filterwarnings("ignore")

logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "sports.csv"
scores_plot = script_dir / "sports_scores.png"
loadings_plot = script_dir / "sports_loadings.png"
centroids_plot = script_dir / "sports_centroids.png"

logger.info("Starting sports analytics discriminant analysis")

# %%
# Load athlete performance data
logger.info("Loading athlete performance data")
df = pd.read_csv(data_file)
logger.info(f"Dataset shape: {df.shape}")
logger.info(f"Columns: {list(df.columns)}")

# %%
# Data exploration
print("=== Sports Analytics Dataset ===")
print(f"Total athletes: {len(df)}")
print(f"Performance categories: {df['performance_category'].unique()}")
print("\nCategory distribution:")
print(df["performance_category"].value_counts())

print("\nFeature summary:")
print(df.describe())

# %%
# Prepare data for discriminant analysis
features = [
    "speed",
    "endurance",
    "strength",
    "technique",
    "agility",
    "power",
    "consistency",
]

X = df[features]
y = df["performance_category"]

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
lda_scores_df["performance_category"] = y_train.reset_index(drop=True)

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
    f"LDA Cross-validation accuracy: {cv_scores_lda.mean():.3f} "
    f"(+/- {cv_scores_lda.std() * 2:.3f})"
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
    f"QDA Cross-validation accuracy: {cv_scores_qda.mean():.3f} "
    f"(+/- {cv_scores_qda.std() * 2:.3f})"
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
# Canonical discriminant analysis interpretation
print("\n=== Canonical Discriminant Analysis ===")
print("First discriminant function (LD1) interpretation:")
ld1_top = coef_df["LD1"].abs().nlargest(3)
print(f"Top contributors: {ld1_top.index.tolist()}")
print(f"Coefficients: {ld1_top.values}")

print("\nSecond discriminant function (LD2) interpretation:")
ld2_top = coef_df["LD2"].abs().nlargest(3)
print(f"Top contributors: {ld2_top.index.tolist()}")
print(f"Coefficients: {ld2_top.values}")

# %%
# Visualization: Discriminant scores
plt.figure(figsize=(12, 8))

# Plot first two discriminant functions
colors = ["gold", "silver", "peru"]
categories = lda.classes_

for i, category in enumerate(categories):
    mask = lda_scores_df["performance_category"] == category
    plt.scatter(
        lda_scores_df.loc[mask, "LD1"],
        lda_scores_df.loc[mask, "LD2"],
        c=colors[i],
        label=f"{category} Athletes",
        alpha=0.7,
        s=50,
        edgecolors="black",
    )

# Add group centroids
centroids = lda.transform(lda.means_)
for i, category in enumerate(categories):
    plt.scatter(
        centroids[i, 0],
        centroids[i, 1],
        c=colors[i],
        marker="x",
        s=200,
        linewidth=3,
        label=f"{category} Centroid",
    )

plt.xlabel("First Linear Discriminant (LD1)")
plt.ylabel("Second Linear Discriminant (LD2)")
plt.title("Athlete Performance: Discriminant Function Scores")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(scores_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved discriminant scores plot to {scores_plot}")
plt.show()

# %%
# Discriminant function loadings visualization
plt.figure(figsize=(10, 6))
loadings = lda.scalings_

# Plot loadings for first two discriminant functions
x = np.arange(len(features))
width = 0.35

plt.bar(x - width / 2, loadings[:, 0], width, label="LD1", alpha=0.8, color="blue")
plt.bar(x + width / 2, loadings[:, 1], width, label="LD2", alpha=0.8, color="red")

plt.xlabel("Performance Metrics")
plt.ylabel("Discriminant Loadings")
plt.title("Discriminant Function Loadings: Performance Metrics")
plt.xticks(x, [f.replace("_", "\n") for f in features], rotation=45, ha="right")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(loadings_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved loadings plot to {loadings_plot}")
plt.show()

# %%
# Group centroids visualization
plt.figure(figsize=(12, 8))

# Plot centroids in the original feature space (first 4 features for readability)
centroids_original = scaler.inverse_transform(lda.means_)
features_subset = features[:4]

x = np.arange(len(features_subset))
width = 0.25

for i, category in enumerate(categories):
    plt.bar(
        x + i * width,
        centroids_original[i, :4],
        width,
        label=f"{category} Athletes",
        alpha=0.7,
        color=colors[i],
    )

plt.xlabel("Performance Metrics")
plt.ylabel("Mean Performance Values")
plt.title("Group Centroids: Athlete Performance Categories")
plt.xticks(x + width, [f.replace("_", "\n") for f in features_subset])
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(centroids_plot, dpi=300, bbox_inches="tight")
logger.info(f"Saved centroids plot to {centroids_plot}")
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
plt.savefig(script_dir / "sports_confusion_matrices.png", dpi=300, bbox_inches="tight")
plt.show()

# %%
# Summary and interpretation
print("\n=== Sports Analytics Summary ===")
print("1. Discriminant Analysis successfully classified athlete performance")
print("2. LDA assumes equal covariance matrices across performance categories")
print("3. QDA allows different covariance matrices for more flexibility")
print(f"4. LDA Accuracy: {lda_accuracy:.3f}, QDA Accuracy: {qda_accuracy:.3f}")
print("5. First discriminant function separates elite from developing athletes")
print("6. Second discriminant function distinguishes competitive athletes")
print("7. Key performance metrics: speed, endurance, technique, and consistency")

logger.info("Sports analytics discriminant analysis completed")
print("\nAnalysis complete! Check generated plots and summary statistics.")
