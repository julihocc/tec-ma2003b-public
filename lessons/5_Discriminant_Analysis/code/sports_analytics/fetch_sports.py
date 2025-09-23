# %%
# Sports Analytics Data Generation
# Chapter 5 - Discriminant Analysis Example
# Generates synthetic athlete performance data for classification

# %%
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from utils import setup_logger

warnings.filterwarnings("ignore")
logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "sports.csv"

logger.info("Starting sports analytics data generation")

# %%
# Define athlete performance categories with distinct ability profiles
np.random.seed(42)  # For reproducibility

n_samples = 300
performance_categories = ["Elite", "Competitive", "Developing"]

# Category proportions (realistic sports development distribution)
category_sizes = {
    "Elite": int(0.2 * n_samples),  # 20% - Top performers
    "Competitive": int(0.5 * n_samples),  # 50% - Regular competitors
    "Developing": int(0.3 * n_samples),  # 30% - Developing athletes
}

logger.info(
    f"Generating {n_samples} athletes across "
    f"{len(performance_categories)} performance categories"
)

# %%
# Generate data for each performance category with different multivariate
# distributions

# Elite Athletes: Exceptional performance across all metrics
elite_mean = np.array(
    [
        95.0,  # speed (100m time in seconds, lower is better)
        85.0,  # endurance (VO2 max, ml/kg/min)
        95.0,  # strength (1RM bench press % bodyweight)
        90.0,  # technique (composite skill score)
        88.0,  # agility (T-test time in seconds, lower is better)
        92.0,  # power (vertical jump in cm)
        85.0,  # consistency (performance stability score)
    ]
)

elite_cov = np.array(
    [
        [0.25, 2.0, 1.5, 1.0, 0.36, 4.0, 1.2],  # speed
        [2.0, 9.0, 3.0, 2.5, 1.0, 8.0, 2.0],  # endurance
        [1.5, 3.0, 4.0, 2.0, 0.8, 6.0, 1.5],  # strength
        [1.0, 2.5, 2.0, 4.0, 0.6, 4.0, 2.0],  # technique
        [0.36, 1.0, 0.8, 0.6, 0.16, 1.6, 0.5],  # agility
        [4.0, 8.0, 6.0, 4.0, 1.6, 16.0, 3.0],  # power
        [1.2, 2.0, 1.5, 2.0, 0.5, 3.0, 4.0],  # consistency
    ]
)

# Competitive Athletes: Good performance with some specialization
competitive_mean = np.array(
    [
        105.0,  # speed (slower than elite)
        70.0,  # endurance (lower than elite)
        75.0,  # strength (moderate)
        75.0,  # technique (good but not exceptional)
        95.0,  # agility (moderate)
        75.0,  # power (moderate)
        70.0,  # consistency (moderate)
    ]
)

competitive_cov = np.array(
    [
        [1.0, 4.0, 2.5, 2.0, 0.64, 6.0, 1.8],  # speed
        [4.0, 25.0, 6.0, 5.0, 2.0, 12.0, 4.0],  # endurance
        [2.5, 6.0, 9.0, 4.0, 1.2, 9.0, 2.5],  # strength
        [2.0, 5.0, 4.0, 9.0, 1.2, 8.0, 3.0],  # technique
        [0.64, 2.0, 1.2, 1.2, 0.36, 2.4, 0.8],  # agility
        [6.0, 12.0, 9.0, 8.0, 2.4, 25.0, 5.0],  # power
        [1.8, 4.0, 2.5, 3.0, 0.8, 5.0, 9.0],  # consistency
    ]
)

# Developing Athletes: Lower performance with high variability
developing_mean = np.array(
    [
        115.0,  # speed (much slower)
        55.0,  # endurance (lower)
        60.0,  # strength (developing)
        60.0,  # technique (needs improvement)
        105.0,  # agility (slower)
        60.0,  # power (lower)
        55.0,  # consistency (inconsistent)
    ]
)

developing_cov = np.array(
    [
        [4.0, 8.0, 5.0, 4.0, 1.6, 12.0, 3.6],  # speed
        [8.0, 36.0, 10.0, 8.0, 4.0, 20.0, 8.0],  # endurance
        [5.0, 10.0, 16.0, 6.0, 2.0, 15.0, 4.0],  # strength
        [4.0, 8.0, 6.0, 16.0, 2.0, 12.0, 5.0],  # technique
        [1.6, 4.0, 2.0, 2.0, 1.0, 4.0, 1.6],  # agility
        [12.0, 20.0, 15.0, 12.0, 4.0, 36.0, 8.0],  # power
        [3.6, 8.0, 4.0, 5.0, 1.6, 8.0, 16.0],  # consistency
    ]
)

# %%
# Generate multivariate normal data for each performance category
data_frames = []

for category, size in category_sizes.items():
    if category == "Elite":
        mean = elite_mean
        cov = elite_cov
    elif category == "Competitive":
        mean = competitive_mean
        cov = competitive_cov
    else:  # Developing
        mean = developing_mean
        cov = developing_cov

    # Generate data
    category_data = np.random.multivariate_normal(mean, cov, size)

    # Create DataFrame
    df_category = pd.DataFrame(
        category_data,
        columns=[
            "speed",
            "endurance",
            "strength",
            "technique",
            "agility",
            "power",
            "consistency",
        ],
    )
    df_category["performance_category"] = category

    data_frames.append(df_category)
    logger.info(f"Generated {size} {category} athletes")

# %%
# Combine all categories
df = pd.concat(data_frames, ignore_index=True)

# Ensure realistic bounds (performance metrics have natural limits)
df["speed"] = df["speed"].clip(85, 140)  # 100m time range
df["endurance"] = df["endurance"].clip(30, 100)  # VO2 max range
df["strength"] = df["strength"].clip(40, 120)  # Strength % bodyweight
df["technique"] = df["technique"].clip(30, 100)  # Skill score
df["agility"] = df["agility"].clip(80, 130)  # T-test time
df["power"] = df["power"].clip(30, 110)  # Vertical jump
df["consistency"] = df["consistency"].clip(20, 100)  # Stability score

# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# %%
# Save the dataset
df.to_csv(data_file, index=False)
logger.info(f"Saved sports analytics data to {data_file}")

# %%
# Data summary
print("=== Sports Analytics Dataset Generated ===")
print(f"Total athletes: {len(df)}")
print(f"File saved: {data_file}")
print("\nPerformance category distribution:")
print(df["performance_category"].value_counts())

print("\nFeature summary:")
print(df.describe().round(2))

print("\nCategory means by feature:")
print(df.groupby("performance_category").mean().round(2))

logger.info("Sports analytics data generation completed")
