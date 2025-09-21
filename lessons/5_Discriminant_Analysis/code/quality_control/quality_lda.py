# %%
# Quality Control Discriminant Analysis
# Chapter 5 - Discriminant Analysis Example
# Manufacturing quality classification using LDA and QDA

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SequentialFeatureSelector
import warnings
warnings.filterwarnings('ignore')

# %%
# Setup logging and paths
from utils import setup_logger
logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "quality.csv"
scores_plot = script_dir / "quality_scores.png"
confusion_plot = script_dir / "quality_confusion.png"
roc_plot = script_dir / "quality_roc.png"

logger.info("Starting quality control discriminant analysis")

# %%
# Load quality control data
logger.info("Loading manufacturing quality data")
df = pd.read_csv(data_file)
logger.info(f"Dataset shape: {df.shape}")
logger.info(f"Columns: {list(df.columns)}")

# %%
# Data exploration
print("=== Quality Control Dataset ===")
print(f"Total products: {len(df)}")
print(f"Quality classes: {df['quality_class'].unique()}")
print("\nClass distribution:")
print(df['quality_class'].value_counts())

print("\nFeature summary:")
print(df.describe())

# %%
# Prepare data for discriminant analysis
features = ['dimension1', 'dimension2', 'thickness', 'surface_roughness',
           'material_hardness', 'defect_density']

X = df[features]
y = df['quality_class']

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
lda_scores_df = pd.DataFrame(X_lda, columns=[f'LD{i+1}' for i in range(X_lda.shape[1])])
lda_scores_df['quality_class'] = y_train.reset_index(drop=True)

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
print(f"LDA Cross-validation accuracy: {cv_scores_lda.mean():.3f} "
      f"(+/- {cv_scores_lda.std() * 2:.3f})")

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
print(f"QDA Cross-validation accuracy: {cv_scores_qda.mean():.3f} "
      f"(+/- {cv_scores_qda.std() * 2:.3f})")

# %%
# Discriminant function coefficients interpretation
print("\n=== Discriminant Function Coefficients ===")
coef_df = pd.DataFrame(
    lda.scalings_,
    index=features,
    columns=[f'LD{i+1}' for i in range(lda.scalings_.shape[1])]
)
print("Coefficients (standardized):")
print(coef_df.round(3))

# %%
# Group means on discriminant functions
print("\n=== Group Means on Discriminant Functions ===")
means_df = pd.DataFrame(lda.means_, index=lda.classes_, columns=features)
print(means_df.round(3))

# %%
# Stepwise feature selection for LDA
print("\n=== Stepwise Feature Selection ===")
sfs = SequentialFeatureSelector(lda, n_features_to_select='auto',
                               direction='forward', cv=3)
sfs.fit(X_train, y_train)

selected_features = X_train.columns[sfs.get_support()].tolist()
print(f"Selected features: {selected_features}")
print(f"Original features: {features}")

# Fit LDA with selected features
X_train_selected = X_train[selected_features]
X_test_selected = X_test[selected_features]

lda_selected = LinearDiscriminantAnalysis()
lda_selected.fit(X_train_selected, y_train)
y_pred_selected = lda_selected.predict(X_test_selected)
selected_accuracy = accuracy_score(y_test, y_pred_selected)

print(f"Accuracy with selected features: {selected_accuracy:.3f}")

# %%
# Visualization: Discriminant scores
plt.figure(figsize=(12, 8))

# Plot first two discriminant functions
colors = ['green', 'orange', 'red']
classes = lda.classes_

for i, quality_class in enumerate(classes):
    mask = lda_scores_df['quality_class'] == quality_class
    plt.scatter(lda_scores_df.loc[mask, 'LD1'],
               lda_scores_df.loc[mask, 'LD2'],
               c=colors[i], label=f'{quality_class} Products',
               alpha=0.7, s=50)

# Add group centroids
centroids = lda.transform(lda.means_)
for i, quality_class in enumerate(classes):
    plt.scatter(centroids[i, 0], centroids[i, 1],
               c=colors[i], marker='x', s=200, linewidth=3,
               label=f'{quality_class} Centroid')

plt.xlabel('First Linear Discriminant (LD1)')
plt.ylabel('Second Linear Discriminant (LD2)')
plt.title('Quality Control: Discriminant Function Scores')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(scores_plot, dpi=300, bbox_inches='tight')
logger.info(f"Saved discriminant scores plot to {scores_plot}")
plt.show()

# %%
# Confusion matrices comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# LDA confusion matrix
cm_lda = confusion_matrix(y_test, y_pred_lda)
sns.heatmap(cm_lda, annot=True, fmt='d', cmap='Blues',
            xticklabels=lda.classes_, yticklabels=lda.classes_, ax=ax1)
ax1.set_title(f'LDA Confusion Matrix\nAccuracy: {lda_accuracy:.3f}')
ax1.set_ylabel('True Label')
ax1.set_xlabel('Predicted Label')

# QDA confusion matrix
cm_qda = confusion_matrix(y_test, y_pred_qda)
sns.heatmap(cm_qda, annot=True, fmt='d', cmap='Oranges',
            xticklabels=qda.classes_, yticklabels=qda.classes_, ax=ax2)
ax2.set_title(f'QDA Confusion Matrix\nAccuracy: {qda_accuracy:.3f}')
ax2.set_ylabel('True Label')
ax2.set_xlabel('Predicted Label')

plt.tight_layout()
plt.savefig(confusion_plot, dpi=300, bbox_inches='tight')
plt.show()

# %%
# Feature importance analysis
plt.figure(figsize=(10, 6))
feature_importance = np.abs(lda.scalings_).mean(axis=1)
plt.barh(features, feature_importance, color='skyblue')
plt.xlabel('Mean Absolute Coefficient')
plt.ylabel('Features')
plt.title('Feature Importance in Quality Classification')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(script_dir / "quality_feature_importance.png", dpi=300, bbox_inches='tight')
plt.show()

# %%
# Summary and interpretation
print("\n=== Quality Control Summary ===")
print("1. Discriminant Analysis successfully classified product quality")
print("2. LDA assumes equal covariance matrices across quality classes")
print("3. QDA allows different covariance matrices for more flexibility")
print(f"4. LDA Accuracy: {lda_accuracy:.3f}, QDA Accuracy: {qda_accuracy:.3f}")
print("5. First discriminant function separates defective from acceptable products")
print("6. Second discriminant function distinguishes borderline quality")
print(f"7. Stepwise selection identified key features: {selected_features}")

logger.info("Quality control discriminant analysis completed")
print("\nAnalysis complete! Check generated plots and summary statistics.")