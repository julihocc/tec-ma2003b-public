"""5.6 Coding and commercial software

Short examples showing how to call scikit-learn LDA if available; otherwise print guidance.
"""
try:
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    import numpy as np
except Exception:
    LinearDiscriminantAnalysis = None


def demo_sklearn():
    if LinearDiscriminantAnalysis is None:
        print('sklearn not available in this environment. Install scikit-learn to run this demo.')
        return
    import numpy as np
    np.random.seed(5)
    X = np.vstack([np.random.randn(50,3)+i for i in range(2)])
    y = np.hstack([[0]*50, [1]*50])
    clf = LinearDiscriminantAnalysis()
    clf.fit(X,y)
    print('sklearn LDA score (train):', clf.score(X,y))


if __name__ == '__main__':
    demo_sklearn()
