#!/usr/bin/env python3
"""
fetch_educational.py

Minimal script to generate synthetic educational assessment data for PCA/FA comparison
and save it as `educational.csv` in the same folder. This creates controlled
educational assessment data with known underlying factor structure.

Usage:
    python fetch_educational.py

Note: This generates synthetic but pedagogically useful data with known
latent factors for method comparison.
"""

import os

import numpy as np
import pandas as pd


def main():
    """Generate synthetic educational assessment data"""
    dst = os.path.join(os.path.dirname(__file__), "educational.csv")

    # Set random seed for reproducible data
    np.random.seed(42)

    # Number of students
    n_students = 100

    # Generate student IDs
    student_ids = [f"STUD_{i:03d}" for i in range(1, n_students + 1)]

    # Generate two orthogonal latent factors
    intelligence_factor = np.random.normal(
        size=(n_students, 1)
    )  # Cognitive ability factor
    personality_factor = np.random.normal(
        size=(n_students, 1)
    )  # Social/emotional factor

    # Define noise terms for measurement error
    measurement_noise_low = np.random.normal(
        size=(n_students, 1)
    )  # Low noise (σ = 0.2)
    measurement_noise_med = np.random.normal(
        size=(n_students, 1)
    )  # Medium noise (σ = 0.25)
    pure_noise_1 = np.random.normal(size=(n_students, 1))  # Pure noise variable 1
    pure_noise_2 = np.random.normal(size=(n_students, 1))  # Pure noise variable 2

    # Define factor loadings
    strong_loading = 0.85  # Strong relationship to latent factor
    moderate_loading = 0.80  # Moderate relationship to latent factor
    low_noise_level = 0.2  # Low measurement error
    med_noise_level = 0.25  # Medium measurement error
    noise_variance_1 = 0.6  # Variance for first noise variable
    noise_variance_2 = 0.5  # Variance for second noise variable

    # Create observed variables with meaningful structure
    math_test = (
        strong_loading * intelligence_factor + low_noise_level * measurement_noise_low
    )
    verbal_test = (
        moderate_loading * intelligence_factor + med_noise_level * measurement_noise_med
    )
    social_skills = (
        strong_loading * personality_factor + low_noise_level * measurement_noise_low
    )
    leadership = (
        moderate_loading * personality_factor + med_noise_level * measurement_noise_med
    )
    random_var1 = noise_variance_1 * pure_noise_1  # Pure noise (no latent structure)
    random_var2 = noise_variance_2 * pure_noise_2  # Pure noise (no latent structure)

    # Create DataFrame
    data = {
        "Student": student_ids,
        "MathTest": np.round(math_test.flatten(), 2),
        "VerbalTest": np.round(verbal_test.flatten(), 2),
        "SocialSkills": np.round(social_skills.flatten(), 2),
        "Leadership": np.round(leadership.flatten(), 2),
        "RandomVar1": np.round(random_var1.flatten(), 2),
        "RandomVar2": np.round(random_var2.flatten(), 2),
    }

    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(dst, index=False)
    print(f"Generated {len(df)} student records")
    print(f"Saved to {dst}")

    # Print summary statistics
    print("\nSummary statistics:")
    print(df.describe().round(2))

    return 0


if __name__ == "__main__":
    exit(main())
