# %%
# Quality Control Data Generation
# Chapter 5 - Discriminant Analysis Example
# Generates synthetic manufacturing quality control data

# %%
import numpy as np
import pandas as pd
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# Setup logging and paths
from utils import setup_logger

logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "quality.csv"

logger.info("Starting quality control data generation")

# %%
# Define product quality classes with distinct manufacturing
# characteristics
np.random.seed(42)  # For reproducibility

n_samples = 800
quality_classes = ['Acceptable', 'Borderline', 'Defective']

# Class proportions (realistic manufacturing distribution)
class_sizes = {
    'Acceptable': int(0.75 * n_samples),    # 75% - Good products
    'Borderline': int(0.20 * n_samples),    # 20% - Marginal quality
    'Defective': int(0.05 * n_samples)      # 5% - Defective products
}

logger.info(f"Generating {n_samples} products across "
            f"{len(quality_classes)} quality classes")

# %%
# Generate data for each quality class with different multivariate
# distributions

# Acceptable Products: High quality, consistent manufacturing
acceptable_mean = np.array([
    10.0,   # dimension1 (mm)
    5.0,    # dimension2 (mm)
    2.5,    # thickness (mm)
    0.02,   # surface_roughness (μm)
    98.5,   # material_hardness (HV)
    0.15    # defect_density (defects/cm²)
])

acceptable_cov = np.array([
    [0.25, 0.05, 0.02, 0.001, 2.0, 0.005],      # dimension1
    [0.05, 0.16, 0.01, 0.0005, 1.0, 0.003],     # dimension2
    [0.02, 0.01, 0.04, 0.0002, 0.5, 0.001],     # thickness
    [0.001, 0.0005, 0.0002, 0.0001, 0.05, 0.0001],  # surface_roughness
    [2.0, 1.0, 0.5, 0.05, 9.0, 0.1],            # material_hardness
    [0.005, 0.003, 0.001, 0.0001, 0.1, 0.01]    # defect_density
])

# Borderline Products: Moderate quality, some variability
borderline_mean = np.array([
    10.2,   # dimension1 (slightly off)
    4.9,    # dimension2 (slightly off)
    2.4,    # thickness (slightly thin)
    0.05,   # surface_roughness (rougher)
    95.0,   # material_hardness (softer)
    0.35    # defect_density (higher)
])

borderline_cov = np.array([
    [0.49, 0.08, 0.03, 0.002, 3.0, 0.008],      # dimension1
    [0.08, 0.25, 0.015, 0.0008, 1.5, 0.005],    # dimension2
    [0.03, 0.015, 0.06, 0.0003, 0.8, 0.002],    # thickness
    [0.002, 0.0008, 0.0003, 0.0002, 0.08, 0.0002],  # surface_roughness
    [3.0, 1.5, 0.8, 0.08, 16.0, 0.15],          # material_hardness
    [0.008, 0.005, 0.002, 0.0002, 0.15, 0.02]   # defect_density
])

# Defective Products: Poor quality, high variability
defective_mean = np.array([
    10.5,   # dimension1 (way off)
    4.7,    # dimension2 (way off)
    2.2,    # thickness (too thin)
    0.12,   # surface_roughness (very rough)
    85.0,   # material_hardness (too soft)
    1.2     # defect_density (very high)
])

defective_cov = np.array([
    [1.0, 0.15, 0.06, 0.005, 5.0, 0.02],        # dimension1
    [0.15, 0.49, 0.03, 0.002, 3.0, 0.01],       # dimension2
    [0.06, 0.03, 0.16, 0.001, 2.0, 0.008],      # thickness
    [0.005, 0.002, 0.001, 0.0005, 0.2, 0.001],  # surface_roughness
    [5.0, 3.0, 2.0, 0.2, 36.0, 0.4],            # material_hardness
    [0.02, 0.01, 0.008, 0.001, 0.4, 0.08]       # defect_density
])

# %%
# Generate multivariate normal data for each quality class
data_frames = []

for quality_class, size in class_sizes.items():
    if quality_class == 'Acceptable':
        mean = acceptable_mean
        cov = acceptable_cov
    elif quality_class == 'Borderline':
        mean = borderline_mean
        cov = borderline_cov
    else:  # Defective
        mean = defective_mean
        cov = defective_cov

    # Generate data
    class_data = np.random.multivariate_normal(mean, cov, size)

    # Create DataFrame
    df_class = pd.DataFrame(class_data, columns=[
        'dimension1', 'dimension2', 'thickness', 'surface_roughness',
        'material_hardness', 'defect_density'
    ])
    df_class['quality_class'] = quality_class

    data_frames.append(df_class)
    logger.info(f"Generated {size} {quality_class} products")

# %%
# Combine all classes
df = pd.concat(data_frames, ignore_index=True)

# Ensure realistic bounds
df['dimension1'] = df['dimension1'].clip(8.5, 12.0)
df['dimension2'] = df['dimension2'].clip(3.5, 6.5)
df['thickness'] = df['thickness'].clip(1.8, 3.2)
df['surface_roughness'] = df['surface_roughness'].clip(0.005, 0.2)
df['material_hardness'] = df['material_hardness'].clip(70, 120)
df['defect_density'] = df['defect_density'].clip(0, 2.0)

# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# %%
# Save the dataset
df.to_csv(data_file, index=False)
logger.info(f"Saved quality control data to {data_file}")

# %%
# Data summary
print("=== Quality Control Dataset Generated ===")
print(f"Total products: {len(df)}")
print(f"File saved: {data_file}")
print("\nQuality class distribution:")
print(df['quality_class'].value_counts())

print("\nFeature summary:")
print(df.describe().round(3))

print("\nClass means by feature:")
print(df.groupby('quality_class').mean().round(3))

logger.info("Quality control data generation completed")