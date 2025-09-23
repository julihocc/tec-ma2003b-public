#!/usr/bin/env python3
"""
fetch_kuiper.py

Minimal script to generate synthetic Kuiper Belt object orbital data that closely
resembles real trans-Neptunian object parameters and save it as `kuiper.csv`
in the same folder. Creates realistic orbital elements with appropriate correlations.

Usage:
    python fetch_kuiper.py

"""

import os
import sys

import numpy as np
import pandas as pd


def main():
    """Generate synthetic Kuiper Belt object orbital parameters"""
    dst = os.path.join(os.path.dirname(__file__), "kuiper.csv")

    # Set random seed for reproducible data
    np.random.seed(42)

    # Number of objects (matching original dataset)
    n_objects = 98

    # Generate object designations (using realistic numbering pattern)
    # Mix of numbered asteroids (15000-100000 range) like real Kuiper objects
    designations = []
    base_numbers = np.random.choice(range(15000, 100000), size=n_objects, replace=False)
    designations = [str(num) for num in sorted(base_numbers)]

    # Generate correlated orbital parameters
    # Based on real Kuiper Belt object populations and dynamical groups

    # Semi-major axis (AU) - determines orbital period and classification
    # Real Kuiper objects range from ~30 AU (classical) to >100 AU (scattered disk)
    # Create different populations: classical (~40-45 AU), scattered (>50 AU), resonant

    population_type = np.random.choice(
        ["classical", "scattered", "resonant"], size=n_objects, p=[0.6, 0.3, 0.1]
    )  # Rough population fractions

    a_values = np.zeros(n_objects)
    e_values = np.zeros(n_objects)
    i_values = np.zeros(n_objects)

    for idx in range(n_objects):
        if population_type[idx] == "classical":
            # Classical Kuiper Belt: low eccentricity, low inclination, a ~ 39-48 AU
            a_values[idx] = np.random.normal(43, 3)  # Semi-major axis
            e_values[idx] = np.random.beta(2, 8) * 0.3  # Low eccentricity (0-0.3)
            i_values[idx] = np.random.exponential(5) + np.random.normal(
                0, 2
            )  # Low inclination

        elif population_type[idx] == "scattered":
            # Scattered disk: high eccentricity, moderate inclination, a > 50 AU
            a_values[idx] = np.random.exponential(30) + 50  # Larger semi-major axis
            e_values[idx] = (
                np.random.beta(3, 4) * 0.8 + 0.2
            )  # High eccentricity (0.2-1.0)
            i_values[idx] = np.random.gamma(2, 8)  # Moderate to high inclination

        else:  # resonant
            # Resonant objects: various a values, moderate e and i
            resonances = [39.4, 47.8, 55.4]  # 3:2, 2:1, 5:3 resonances with Neptune
            a_values[idx] = np.random.choice(resonances) + np.random.normal(0, 1)
            e_values[idx] = np.random.beta(3, 5) * 0.5  # Moderate eccentricity
            i_values[idx] = np.random.gamma(1.5, 6)  # Moderate inclination

    # Apply realistic bounds
    a_values = np.clip(a_values, 30, 150)  # Semi-major axis bounds
    e_values = np.clip(
        e_values, 0.01, 0.97
    )  # Eccentricity bounds (0-1, avoid exactly 1)
    i_values = np.clip(
        np.abs(i_values), 0.1, 50
    )  # Inclination bounds (0-180°, but most <50°)

    # Create correlation between a and e (observed in real data)
    # Add some additional correlation structure
    for idx in range(n_objects):
        if a_values[idx] > 50:  # Distant objects tend to be more eccentric
            e_values[idx] += np.random.normal(0, 0.1)
            e_values[idx] = np.clip(e_values[idx], 0.01, 0.97)

    # Absolute magnitude H (brightness) - anticorrelated with size
    # Typical range for Kuiper objects: 3-12 mag
    # Larger objects (brighter, lower H) tend to be found first (lower designation numbers)
    H_base = np.random.normal(6.5, 1.5, n_objects)  # Base magnitude

    # Add some correlation with designation (earlier discoveries tend to be brighter/larger)
    designation_rank = np.argsort([int(d) for d in designations])
    H_correction = -2.0 * (designation_rank / n_objects) + 1.0  # Earlier = brighter
    H_values = H_base + H_correction + np.random.normal(0, 0.5, n_objects)
    H_values = np.clip(H_values, 1.0, 12.5)

    # Create DataFrame
    data = {
        "designation": designations,
        "a": np.round(a_values, 7),  # Match precision of original
        "e": np.round(e_values, 7),
        "i": np.round(i_values, 5),
        "H": np.round(H_values, 2),
    }

    df = pd.DataFrame(data)

    # Save to CSV
    try:
        df.to_csv(dst, index=False)
        print(f"Generated {len(df)} Kuiper Belt objects")
        print(f"Saved: {dst}")

        # Print summary statistics
        print("\nSummary statistics:")
        numeric_cols = ["a", "e", "i", "H"]
        print(df[numeric_cols].describe().round(2))

        print("\nCorrelation matrix:")
        print(df[numeric_cols].corr().round(3))

        return 0

    except Exception as e:
        print("Write failed:", e, file=sys.stderr)
        return 5


if __name__ == "__main__":
    sys.exit(main())
