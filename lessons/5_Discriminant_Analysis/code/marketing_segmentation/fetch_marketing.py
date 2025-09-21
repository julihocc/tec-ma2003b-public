# %%
# Marketing Segmentation Data Generation
# Chapter 5 - Discriminant Analysis Example
# Generates synthetic customer behavior data for segmentation analysis

# %%
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# %%
# Setup logging and paths
from utils import setup_logger

logger = setup_logger(__name__)

script_dir = Path(__file__).resolve().parent
data_file = script_dir / "marketing.csv"

logger.info("Starting marketing segmentation data generation")

# %%
# Define customer segments with distinct behavioral patterns
np.random.seed(42)  # For reproducibility

n_samples = 1200
segments = ["High-Value", "Loyal", "Occasional"]

# Segment proportions
segment_sizes = {
    "High-Value": int(0.3 * n_samples),  # 30% - Premium customers
    "Loyal": int(0.4 * n_samples),  # 40% - Regular loyal customers
    "Occasional": int(0.3 * n_samples),  # 30% - Infrequent buyers
}

logger.info(f"Generating {n_samples} customers across {len(segments)} segments")

# %%
# Generate data for each segment with different multivariate distributions

# High-Value Customers: High spending, frequent purchases, engaged
high_value_mean = np.array(
    [
        25.0,  # purchase_freq (purchases per month)
        150.0,  # avg_order_value ($)
        45.0,  # browsing_time (minutes per session)
        0.15,  # cart_abandonment (rate)
        0.85,  # email_open_rate
        500.0,  # loyalty_points
        0.5,  # support_tickets (per month)
        8.5,  # social_engagement (interactions per month)
    ]
)

high_value_cov = np.array(
    [
        [4.0, 20.0, 8.0, -0.02, 0.05, 50.0, 0.1, 1.5],  # purchase_freq
        [20.0, 400.0, 30.0, -0.5, 0.2, 200.0, 0.3, 5.0],  # avg_order_value
        [8.0, 30.0, 25.0, -0.1, 0.1, 40.0, 0.2, 2.0],  # browsing_time
        [-0.02, -0.5, -0.1, 0.01, -0.005, -1.0, 0.01, -0.1],  # cart_abandonment
        [0.05, 0.2, 0.1, -0.005, 0.02, 2.0, 0.01, 0.3],  # email_open_rate
        [50.0, 200.0, 40.0, -1.0, 2.0, 2500.0, 1.0, 15.0],  # loyalty_points
        [0.1, 0.3, 0.2, 0.01, 0.01, 1.0, 0.25, 0.5],  # support_tickets
        [1.5, 5.0, 2.0, -0.1, 0.3, 15.0, 0.5, 4.0],  # social_engagement
    ]
)

# Loyal Customers: Moderate spending, very frequent, highly engaged
loyal_mean = np.array(
    [
        15.0,  # purchase_freq
        75.0,  # avg_order_value
        35.0,  # browsing_time
        0.25,  # cart_abandonment
        0.75,  # email_open_rate
        300.0,  # loyalty_points
        1.0,  # support_tickets
        6.0,  # social_engagement
    ]
)

loyal_cov = np.array(
    [
        [2.25, 8.0, 4.0, -0.03, 0.04, 25.0, 0.15, 1.0],  # purchase_freq
        [8.0, 100.0, 15.0, -0.3, 0.15, 100.0, 0.4, 3.0],  # avg_order_value
        [4.0, 15.0, 16.0, -0.08, 0.08, 20.0, 0.25, 1.5],  # browsing_time
        [-0.03, -0.3, -0.08, 0.015, -0.01, -1.5, 0.02, -0.15],  # cart_abandonment
        [0.04, 0.15, 0.08, -0.01, 0.025, 1.5, 0.015, 0.25],  # email_open_rate
        [25.0, 100.0, 20.0, -1.5, 1.5, 900.0, 1.5, 10.0],  # loyalty_points
        [0.15, 0.4, 0.25, 0.02, 0.015, 1.5, 0.5, 0.8],  # support_tickets
        [1.0, 3.0, 1.5, -0.15, 0.25, 10.0, 0.8, 3.0],  # social_engagement
    ]
)

# Occasional Customers: Low frequency, variable spending, low engagement
occasional_mean = np.array(
    [
        3.0,  # purchase_freq
        45.0,  # avg_order_value
        15.0,  # browsing_time
        0.6,  # cart_abandonment
        0.3,  # email_open_rate
        50.0,  # loyalty_points
        2.5,  # support_tickets
        1.5,  # social_engagement
    ]
)

occasional_cov = np.array(
    [
        [0.81, 3.0, 1.2, -0.05, 0.01, 5.0, 0.2, 0.2],  # purchase_freq
        [3.0, 25.0, 4.5, -0.8, 0.05, 15.0, 0.6, 0.8],  # avg_order_value
        [1.2, 4.5, 6.25, -0.15, 0.02, 3.0, 0.3, 0.4],  # browsing_time
        [-0.05, -0.8, -0.15, 0.04, -0.02, -2.0, 0.08, -0.1],  # cart_abandonment
        [0.01, 0.05, 0.02, -0.02, 0.01, 0.5, 0.01, 0.05],  # email_open_rate
        [5.0, 15.0, 3.0, -2.0, 0.5, 100.0, 1.0, 1.5],  # loyalty_points
        [0.2, 0.6, 0.3, 0.08, 0.01, 1.0, 1.0, 0.5],  # support_tickets
        [0.2, 0.8, 0.4, -0.1, 0.05, 1.5, 0.5, 1.0],  # social_engagement
    ]
)

# %%
# Generate multivariate normal data for each segment
data_frames = []

for segment, size in segment_sizes.items():
    if segment == "High-Value":
        mean = high_value_mean
        cov = high_value_cov
    elif segment == "Loyal":
        mean = loyal_mean
        cov = loyal_cov
    else:  # Occasional
        mean = occasional_mean
        cov = occasional_cov

    # Generate data
    segment_data = np.random.multivariate_normal(mean, cov, size)

    # Create DataFrame
    df_segment = pd.DataFrame(
        segment_data,
        columns=[
            "purchase_freq",
            "avg_order_value",
            "browsing_time",
            "cart_abandonment",
            "email_open_rate",
            "loyalty_points",
            "support_tickets",
            "social_engagement",
        ],
    )
    df_segment["segment"] = segment

    data_frames.append(df_segment)
    logger.info(f"Generated {size} {segment} customers")

# %%
# Combine all segments
df = pd.concat(data_frames, ignore_index=True)

# Ensure realistic bounds (clip negative values, etc.)
df["purchase_freq"] = df["purchase_freq"].clip(lower=0.5)
df["avg_order_value"] = df["avg_order_value"].clip(lower=10)
df["browsing_time"] = df["browsing_time"].clip(lower=1)
df["cart_abandonment"] = df["cart_abandonment"].clip(0, 1)
df["email_open_rate"] = df["email_open_rate"].clip(0, 1)
df["loyalty_points"] = df["loyalty_points"].clip(lower=0)
df["support_tickets"] = df["support_tickets"].clip(lower=0)
df["social_engagement"] = df["social_engagement"].clip(lower=0)

# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# %%
# Save the dataset
df.to_csv(data_file, index=False)
logger.info(f"Saved marketing segmentation data to {data_file}")

# %%
# Data summary
print("=== Marketing Segmentation Dataset Generated ===")
print(f"Total customers: {len(df)}")
print(f"File saved: {data_file}")
print("\nSegment distribution:")
print(df["segment"].value_counts())

print("\nFeature summary:")
print(df.describe().round(2))

print("\nSegment means by feature:")
print(df.groupby("segment").mean().round(2))

logger.info("Marketing segmentation data generation completed")
