# 5.2 Cost Function and Prior Probabilities

This folder contains materials for Topic 5.2: Incorporating prior probabilities and misclassification costs into discriminant analysis.

## Learning Objectives

After completing this topic, students will be able to:

- Incorporate prior probabilities into Bayes classification rule
- Understand the impact of unequal prior probabilities on decision boundaries
- Apply asymmetric misclassification costs to classification problems
- Modify decision thresholds based on cost considerations
- Evaluate the trade-offs between different types of classification errors

## Key Concepts

### Prior Probabilities
- **Equal Priors**: π₁ = π₂ = 0.5 (default assumption)
- **Unequal Priors**: π₁ ≠ π₂ (reflects true population proportions)
- **Impact on Classification**: Shifts decision boundaries toward less probable groups

### Misclassification Costs
- **Symmetric Costs**: c(1|2) = c(2|1) (equal penalty for both error types)
- **Asymmetric Costs**: c(1|2) ≠ c(2|1) (different penalties for different errors)
- **Cost Matrix**: C where C[i,j] = cost of classifying as group i when true group is j

### Modified Decision Rule
**Bayes Rule with Costs and Priors:**
Classify to group 1 if:
```
π₁ × f₁(x) / π₂ × f₂(x) > c(1|2) / c(2|1)
```

Where:
- π₁, π₂: Prior probabilities
- f₁(x), f₂(x): Likelihood functions  
- c(1|2), c(2|1): Misclassification costs

## Applications

### Medical Diagnosis
- **High Cost of False Negative**: Missing a disease (Type II error)
- **Lower Cost of False Positive**: Unnecessary treatment (Type I error)
- **Adjusted Threshold**: More sensitive to detect disease

### Quality Control
- **Cost of Defective Products**: High cost of shipping defective items
- **Cost of Good Products Rejected**: Lower cost of over-inspection
- **Decision**: Err on side of rejecting borderline items

### Financial Risk
- **Cost of Bad Loans**: High cost of default
- **Cost of Rejected Good Applicants**: Lower opportunity cost
- **Strategy**: More conservative lending criteria

## Folder Structure

### 📁 `latex/`
- `costs_priors.tex` - Beamer presentation covering theory and applications

### 📁 `python/`
- `costs_priors_practice.py` - Demonstrate effect of priors and costs on classification
- `test_costs_priors.py` - Unit tests for implementations

### 📁 `julia/`
- Ready for `costs_priors_practice.jl` - Mathematical pseudocode version

## Usage

```bash
cd python/
python costs_priors_practice.py
```

## Mathematical Formulation

**Expected Cost of Misclassification:**
```
ECM = π₁ × c(2|1) × P(classify as 2|true = 1) + π₂ × c(1|2) × P(classify as 1|true = 2)
```

**Optimal Decision Threshold:**
Classify to group 1 if the posterior probability ratio exceeds:
```
threshold = [c(1|2) × π₂] / [c(2|1) × π₁]
```

## Prerequisites

- Understanding of Bayes theorem and conditional probability
- Knowledge of Type I and Type II errors
- Familiarity with basic discriminant analysis (Topic 5.1)
- Understanding of decision theory concepts