"""5.3 Basic discrimination

Compute confusion matrix and basic diagnostics for a linear discriminant rule.
"""

import numpy as np


def confusion(y, yhat):
    tp = int(((y == 1) & (yhat == 1)).sum())
    tn = int(((y == 0) & (yhat == 0)).sum())
    fp = int(((y == 0) & (yhat == 1)).sum())
    fn = int(((y == 1) & (yhat == 0)).sum())
    return np.array([[tn, fp], [fn, tp]])


if __name__ == '__main__':
    # tiny example
    y = np.array([0,0,1,1,1,0,1,0])
    yhat = np.array([0,1,1,1,0,0,1,0])
    print('Confusion matrix (tn, fp; fn, tp):')
    print(confusion(y, yhat))
    print('Accuracy:', (y==yhat).mean())
