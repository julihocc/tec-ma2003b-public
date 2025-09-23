#!/usr/bin/env python3
"""
fetch_invest.py

Minimal script to generate synthetic European stock market data that closely
resembles the EuStockMarkets dataset and save it as `invest.csv` in the same
folder. Creates realistic time series with high correlations between indices.

Usage:
    python fetch_invest.py

"""

import os
import sys

import numpy as np
import pandas as pd


def main():
    """Generate synthetic European stock market indices data"""
    dst = os.path.join(os.path.dirname(__file__), "invest.csv")

    # Set random seed for reproducible data
    np.random.seed(42)

    # Parameters based on original EuStockMarkets data analysis
    n_days = 1860  # Same number of observations as original

    # Starting values (approximate means from original data)
    start_values = {"DAX": 2500, "SMI": 3400, "CAC": 2200, "FTSE": 3600}

    # Generate correlated random walks to simulate stock market behavior
    # Create a common market factor that drives all indices
    market_factor = np.random.normal(0, 0.01, n_days)  # Daily market returns

    # Add some regional factors to create more realistic correlation structure
    european_factor = np.random.normal(0, 0.008, n_days)  # European region factor
    uk_factor = np.random.normal(0, 0.006, n_days)  # UK-specific factor

    # Individual noise for each index (different volatilities to create varied correlations)
    individual_noise = {
        "DAX": np.random.normal(0, 0.008, n_days),
        "SMI": np.random.normal(0, 0.006, n_days),  # SMI correlated but distinct
        "CAC": np.random.normal(0, 0.010, n_days),  # CAC more independent
        "FTSE": np.random.normal(0, 0.007, n_days),
    }

    # Weight of market factor vs individual noise (creates high but realistic correlation)
    market_weight = 0.75  # Reduced from 0.85
    individual_weight = 0.25  # Increased from 0.15

    # Generate the time series
    indices = {}
    for index, start_val in start_values.items():
        # Different factor loadings for each index to create varied correlations
        if index == "FTSE":
            # FTSE gets less European factor, more UK factor
            returns = (
                market_weight * market_factor
                + 0.1 * european_factor
                + 0.15 * uk_factor
                + individual_weight * individual_noise[index]
            )
        elif index == "CAC":
            # CAC gets more individual noise, less correlated
            returns = (
                0.65 * market_factor
                + 0.2 * european_factor
                + 0.15 * individual_noise[index]
            )
        else:
            # DAX and SMI more European-focused
            returns = (
                market_weight * market_factor
                + 0.15 * european_factor
                + individual_weight * individual_noise[index]
            )

        # Convert returns to price levels using cumulative product
        price_series = start_val * np.cumprod(1 + returns)
        indices[index] = price_series

    # Create DataFrame matching original structure
    data = {
        "rownames": range(1, n_days + 1),
        "DAX": np.round(indices["DAX"], 2),
        "SMI": np.round(indices["SMI"], 1),
        "CAC": np.round(indices["CAC"], 1),
        "FTSE": np.round(indices["FTSE"], 1),
    }

    df = pd.DataFrame(data)

    # Save to CSV
    try:
        df.to_csv(dst, index=False)
        print(f"Generated {len(df)} stock market observations")
        print(f"Saved: {dst}")

        # Print summary statistics
        print("\nSummary statistics:")
        print(df.iloc[:, 1:].describe().round(1))

        print("\nCorrelation matrix:")
        print(df.iloc[:, 1:].corr().round(3))

        return 0

    except Exception as e:
        print("Write failed:", e, file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
