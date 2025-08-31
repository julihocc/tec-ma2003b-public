#!/usr/bin/env python3
"""
fetch_hospitals.py

Minimal script to generate synthetic health outcomes data for US hospitals
and save it as `hospitals.csv` in the same folder. This creates realistic
hospital performance metrics for PCA analysis.

Usage:
    python fetch_hospitals.py

Note: This generates synthetic but realistic data based on typical ranges
for hospital quality metrics.
"""

import os
import pandas as pd
import numpy as np


def main():
    """Generate synthetic hospital health outcomes data"""
    dst = os.path.join(os.path.dirname(__file__), "hospitals.csv")

    # Set random seed for reproducible data
    np.random.seed(42)

    # Number of hospitals
    n_hospitals = 50

    # Generate hospital IDs
    hospital_ids = [f"HOSP_{i:03d}" for i in range(1, n_hospitals + 1)]

    # Generate correlated health outcome variables
    # We'll create correlations that make sense for hospital quality

    # Base quality factor (latent variable)
    quality_factor = np.random.normal(0, 1, n_hospitals)

    # Mortality Rate (%) - higher is worse, inversely related to quality
    mortality_rate = 4.5 - 1.2 * quality_factor + np.random.normal(0, 0.8, n_hospitals)
    mortality_rate = np.clip(mortality_rate, 1.0, 8.0)  # Realistic range

    # 30-day Readmission Rate (%) - higher is worse
    readmission_rate = (
        12.0 - 1.5 * quality_factor + np.random.normal(0, 1.2, n_hospitals)
    )
    readmission_rate = np.clip(readmission_rate, 6.0, 20.0)

    # Patient Satisfaction Score (0-100) - higher is better
    patient_satisfaction = (
        75.0 + 8.0 * quality_factor + np.random.normal(0, 3.0, n_hospitals)
    )
    patient_satisfaction = np.clip(patient_satisfaction, 50.0, 95.0)

    # Average Length of Stay (days) - shorter is generally better
    avg_length_stay = 5.2 - 0.8 * quality_factor + np.random.normal(0, 0.6, n_hospitals)
    avg_length_stay = np.clip(avg_length_stay, 3.0, 8.0)

    # Hospital-Acquired Infection Rate (%) - lower is better
    infection_rate = 3.2 - 1.0 * quality_factor + np.random.normal(0, 0.7, n_hospitals)
    infection_rate = np.clip(infection_rate, 0.5, 6.0)

    # Nurse-to-Patient Ratio - higher is better
    nurse_ratio = 0.35 + 0.08 * quality_factor + np.random.normal(0, 0.04, n_hospitals)
    nurse_ratio = np.clip(nurse_ratio, 0.20, 0.50)

    # Surgical Complication Rate (%) - lower is better
    surgical_complications = (
        2.8 - 0.9 * quality_factor + np.random.normal(0, 0.5, n_hospitals)
    )
    surgical_complications = np.clip(surgical_complications, 0.8, 5.5)

    # Emergency Department Wait Time (minutes) - lower is better
    ed_wait_time = 45.0 - 8.0 * quality_factor + np.random.normal(0, 8.0, n_hospitals)
    ed_wait_time = np.clip(ed_wait_time, 15.0, 90.0)

    # Create DataFrame
    data = {
        "Hospital": hospital_ids,
        "MortalityRate": np.round(mortality_rate, 2),
        "ReadmissionRate": np.round(readmission_rate, 2),
        "PatientSatisfaction": np.round(patient_satisfaction, 1),
        "AvgLengthStay": np.round(avg_length_stay, 1),
        "InfectionRate": np.round(infection_rate, 2),
        "NurseRatio": np.round(nurse_ratio, 3),
        "SurgicalComplications": np.round(surgical_complications, 2),
        "EDWaitTime": np.round(ed_wait_time, 1),
    }

    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(dst, index=False)
    print(f"Generated {len(df)} hospital records")
    print(f"Saved to {dst}")

    # Print summary statistics
    print("\nSummary statistics:")
    print(df.describe().round(2))

    return 0


if __name__ == "__main__":
    exit(main())
