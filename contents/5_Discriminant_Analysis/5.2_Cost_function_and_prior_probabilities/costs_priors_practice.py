"""5.2 Cost function and prior probabilities

Illustrate how prior probabilities and asymmetric costs change decision thresholds.
"""

import numpy as np

np.random.seed(2)


def demo_prior_effect():
    # simple 1D example for clarity
    mu0, mu1 = 0.0, 1.0
    sigma = 1.0
    x = np.linspace(-3, 4, 200)
    # likelihood ratio threshold depends on log(pi1/pi0) and cost ratio
    for pi1 in [0.5, 0.2, 0.8]:
        log_prior = np.log(pi1 / (1 - pi1))
        # show numeric threshold where decision flips for linearized score
        # here decision rule reduces to x > thresh with thresh = function(log_prior)
        thresh = (np.log(1) - log_prior)  # illustrative placeholder
        print(f"pi1={pi1}: illustrative threshold (approx) = {thresh:.3f}")


if __name__ == '__main__':
    demo_prior_effect()
