#!/usr/bin/env python3
"""
fetch_customer_data.py

Generate synthetic customer satisfaction data for the TechnoServe Solutions
business case. Creates realistic multi-dimensional survey data with underlying
factor structure suitable for Factor Analysis.

Usage:
    python fetch_customer_data.py

"""

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def main():
    """Generate synthetic customer satisfaction survey data"""
    dst = os.path.join(os.path.dirname(__file__), "customer_satisfaction_data.csv")

    # Set random seed for reproducible data
    np.random.seed(42)

    # Parameters
    n_customers = 850  # Enterprise clients as specified in business case
    n_quarters = 4  # Q1-Q4 2024 data

    # Define underlying factor structure (what we want students to discover)
    # Factor 1: Technical Excellence (35% of variance)
    technical_items = [
        "technical_expertise",
        "problem_solving",
        "innovation_solutions",
        "technical_documentation",
        "system_integration",
    ]

    # Factor 2: Relationship Management (25% of variance)
    relationship_items = [
        "account_manager_responsive",
        "executive_access",
        "trust_reliability",
        "long_term_partnership",
        "communication_clarity",
    ]

    # Factor 3: Project Delivery (20% of variance)
    delivery_items = [
        "project_management",
        "timeline_adherence",
        "budget_control",
        "quality_deliverables",
        "change_management",
    ]

    # Factor 4: Value & Cost (15% of variance)
    value_items = [
        "cost_transparency",
        "value_for_money",
        "roi_demonstration",
        "competitive_pricing",
        "billing_accuracy",
    ]

    # Factor 5: Support & Service (5% of variance)
    support_items = ["support_responsiveness", "training_quality", "documentation_help"]

    # All satisfaction items (7-point Likert scale: 1=Very Dissatisfied, 7=Very Satisfied)
    all_items = (
        technical_items
        + relationship_items
        + delivery_items
        + value_items
        + support_items
    )

    # Generate underlying factor scores for each customer
    # Create correlation structure between factors (realistic business scenario)
    factor_corr_matrix = np.array(
        [
            [1.00, 0.65, 0.72, 0.45, 0.58],  # Technical with others
            [0.65, 1.00, 0.68, 0.52, 0.61],  # Relationship with others
            [0.72, 0.68, 1.00, 0.59, 0.54],  # Delivery with others
            [0.45, 0.52, 0.59, 1.00, 0.48],  # Value with others
            [0.58, 0.61, 0.54, 0.48, 1.00],  # Support with others
        ]
    )

    # Generate correlated factor scores using Cholesky decomposition
    L = np.linalg.cholesky(factor_corr_matrix)

    data_list = []

    for quarter in range(1, n_quarters + 1):
        # Generate independent standard normal variables
        independent_factors = np.random.normal(0, 1, (n_customers, 5))

        # Create correlated factors
        correlated_factors = independent_factors @ L.T

        # Add some quarterly trends (slight improvement over time)
        quarterly_improvement = (quarter - 1) * 0.1
        correlated_factors += quarterly_improvement

        for customer_id in range(1, n_customers + 1):
            customer_factors = correlated_factors[customer_id - 1]

            # Generate observed item scores based on factor loadings
            customer_data = {
                "customer_id": f"CUST_{customer_id:03d}",
                "quarter": f"Q{quarter}_2024",
                "survey_date": (
                    datetime(2024, quarter * 3, 15)
                    + timedelta(days=np.random.randint(-10, 11))
                ).strftime("%Y-%m-%d"),
            }

            # Factor 1: Technical Excellence (high loadings: 0.7-0.9)
            for item in technical_items:
                loading = np.random.uniform(0.7, 0.9)
                error = np.random.normal(0, 0.5)
                raw_score = 4 + loading * customer_factors[0] + error  # Center around 4
                customer_data[item] = max(1, min(7, round(raw_score)))

            # Factor 2: Relationship Management (high loadings: 0.6-0.8)
            for item in relationship_items:
                loading = np.random.uniform(0.6, 0.8)
                error = np.random.normal(0, 0.6)
                raw_score = 4 + loading * customer_factors[1] + error
                customer_data[item] = max(1, min(7, round(raw_score)))

            # Factor 3: Project Delivery (high loadings: 0.65-0.85)
            for item in delivery_items:
                loading = np.random.uniform(0.65, 0.85)
                error = np.random.normal(0, 0.55)
                raw_score = 4 + loading * customer_factors[2] + error
                customer_data[item] = max(1, min(7, round(raw_score)))

            # Factor 4: Value & Cost (moderate loadings: 0.5-0.7)
            for item in value_items:
                loading = np.random.uniform(0.5, 0.7)
                error = np.random.normal(0, 0.7)
                raw_score = 4 + loading * customer_factors[3] + error
                customer_data[item] = max(1, min(7, round(raw_score)))

            # Factor 5: Support & Service (moderate loadings: 0.4-0.6)
            for item in support_items:
                loading = np.random.uniform(0.4, 0.6)
                error = np.random.normal(0, 0.8)
                raw_score = 4 + loading * customer_factors[4] + error
                customer_data[item] = max(1, min(7, round(raw_score)))

            # Generate outcome variables based on weighted factor scores
            # Overall satisfaction (combination of all factors)
            overall_raw = 4 + 0.8 * np.mean(customer_factors) + np.random.normal(0, 0.4)
            customer_data["overall_satisfaction"] = max(1, min(7, round(overall_raw)))

            # NPS (Net Promoter Score: 0-10 scale)
            nps_raw = 6 + 1.2 * np.mean(customer_factors) + np.random.normal(0, 1.5)
            customer_data["nps_score"] = max(0, min(10, round(nps_raw)))

            # Contract renewal likelihood (1-5 scale)
            renewal_raw = 3 + 0.6 * np.mean(customer_factors) + np.random.normal(0, 0.5)
            customer_data["renewal_likelihood"] = max(1, min(5, round(renewal_raw)))

            # Revenue growth percentage (can be negative)
            revenue_growth = 5 + 8 * np.mean(customer_factors) + np.random.normal(0, 5)
            customer_data["revenue_growth_pct"] = round(revenue_growth, 1)

            # Referral generation (0-3 referrals in quarter)
            referral_prob = 1 / (1 + np.exp(-2 * np.mean(customer_factors)))  # Sigmoid
            customer_data["referrals_generated"] = np.random.poisson(3 * referral_prob)

            # Add some missing data (realistic survey scenario)
            if np.random.random() < 0.05:  # 5% missing rate
                missing_items = np.random.choice(
                    all_items, size=np.random.randint(1, 4), replace=False
                )
                for item in missing_items:
                    customer_data[item] = np.nan

            data_list.append(customer_data)

    # Create DataFrame
    df = pd.DataFrame(data_list)

    # Reorder columns for better readability
    id_cols = ["customer_id", "quarter", "survey_date"]
    satisfaction_cols = sorted(
        [
            col
            for col in df.columns
            if col
            not in id_cols
            + [
                "overall_satisfaction",
                "nps_score",
                "renewal_likelihood",
                "revenue_growth_pct",
                "referrals_generated",
            ]
        ]
    )
    outcome_cols = [
        "overall_satisfaction",
        "nps_score",
        "renewal_likelihood",
        "revenue_growth_pct",
        "referrals_generated",
    ]

    df = df[id_cols + satisfaction_cols + outcome_cols]

    # Save to CSV
    try:
        df.to_csv(dst, index=False)
        print(f"Generated {len(df)} customer satisfaction survey responses")
        print(f"Customers: {n_customers}, Quarters: {n_quarters}")
        print(f"Saved: {dst}")

        # Print summary statistics for satisfaction items only
        satisfaction_data = df[satisfaction_cols]
        print(f"\nSatisfaction items summary (1-7 scale, n={len(satisfaction_cols)}):")
        print(satisfaction_data.describe().round(2))

        print(f"\nOutcome variables summary:")
        outcome_data = df[outcome_cols]
        print(outcome_data.describe().round(2))

        print(f"\nMissing data pattern:")
        missing_counts = satisfaction_data.isnull().sum()
        print(f"Items with missing data: {(missing_counts > 0).sum()}")
        print(f"Total missing values: {missing_counts.sum()}")

        # Show correlation matrix for first few items (preview)
        print(f"\nSample correlation matrix (first 8 items):")
        sample_corr = satisfaction_data.iloc[:, :8].corr()
        print(sample_corr.round(3))

        return 0

    except Exception as e:
        print("Write failed:", e, file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
