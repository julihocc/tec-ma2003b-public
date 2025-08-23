# 1.5 Backward Selection

This folder contains materials for Topic 1.5: Backward elimination method for stepwise variable selection in regression.

## Learning Objectives

- Understand the backward elimination algorithm
- Apply statistical criteria for variable removal
- Implement backward selection from scratch
- Compare forward vs. backward selection approaches
- Recognize when to use backward elimination

## Key Concepts

### Backward Selection Algorithm
1. **Start**: With all variables in the model
2. **Remove Variables**: One at a time based on statistical criteria
3. **Stopping Rule**: When all remaining variables meet retention criteria
4. **Final Model**: Contains significant variables

### Selection Criteria
- **p-value threshold**: Usually 0.05 or 0.10 for removal
- **AIC/BIC**: Remove variables that improve information criteria
- **F-statistic**: For partial F-tests of variable significance
- **t-statistic**: For individual coefficient significance

### Comparison with Forward Selection
- **Backward**: Better when most variables are relevant
- **Forward**: Better when few variables are relevant
- **Different Results**: May yield different final models
- **Computational Cost**: Backward starts with more complex model

## Usage

```bash
cd python/
python backward_selection_practice.py
```