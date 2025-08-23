# 1.4 Forward Selection

This folder contains materials for Topic 1.4: Forward selection method for stepwise variable selection in regression.

## Learning Objectives

- Understand the forward selection algorithm
- Apply statistical criteria for variable entry
- Implement forward selection from scratch
- Compare different selection criteria (AIC, BIC, p-values)
- Recognize advantages and limitations of forward selection

## Key Concepts

### Forward Selection Algorithm
1. **Start**: With intercept-only model
2. **Add Variables**: One at a time based on statistical criteria
3. **Stopping Rule**: When no remaining variables meet entry criteria
4. **Final Model**: Contains selected variables

### Selection Criteria
- **p-value threshold**: Usually 0.05 or 0.10
- **AIC (Akaike Information Criterion)**: Balances fit and complexity
- **BIC (Bayesian Information Criterion)**: More conservative than AIC
- **F-statistic**: For partial F-tests

### Advantages and Limitations
- **Advantages**: Computationally efficient, interpretable process
- **Limitations**: May miss optimal subset, selection bias

## Usage

```bash
cd python/
python forward_selection_practice.py
```